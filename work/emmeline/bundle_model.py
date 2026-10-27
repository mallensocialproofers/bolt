#!/usr/bin/env python3
"""Emmeline eye cream + face mist bundle model (2026-10-27).

Inputs are tagged:
  SRC    read directly from a page or screenshot the owner supplied
  SRC-U  from a secondary page or search snippet, UNVERIFIED
  ASM    assumption (scenario, not a fact)
  ARITH  derived
No supplier quote exists; every cost below is a catalogue price read from a screenshot
of selfnamed.com Face Care (2026-10-27). Which price (pink badge vs black) applies to a
dropshipped order is UNVERIFIED, so three cost tiers are modelled.

Run:  python3 bundle_model.py   (writes bundle_model_*.csv next to this file)
"""
import csv
import itertools
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- inputs
# SelfNamed catalogue, 15 ml eye creams and 100 ml Microbiome Prebiotics Face Mist (screenshot, SRC)
COST_TIERS = {
    # name: (eye_cost, mist_cost, note)
    "A pink-badge (Pro?) prices": (5.44, 5.78, "Smoothing Eye Cream $5.44; Face Mist $5.78 (SRC; badge meaning UNVERIFIED)"),
    "B mid / promo prices":       (9.10, 8.89, "Peptide Eye Cream $9.10; Face Mist $8.89 after -30% (SRC)"),
    "C full list prices":         (13.60, 12.70, "Smoothing Eye Cream $13.60; Face Mist $12.70 before promo (SRC)"),
}
CUSTOM_PACK_PER_ORDER = {"included": 0.00, "extra": 2.00}      # ASM: label/box customisation not priced on page
SHIP_COST = {"low 5.50": 5.50, "high 8.40": 8.40, "1lb 10.67": 10.67}  # USPS Ground Advantage under 1 lb commercial (SRC-U)
SHIP_CHARGED_BELOW_THRESHOLD = 5.95   # ASM: what a customer pays under the free-shipping line
FREE_SHIP_THRESHOLD = 60.00           # ASM
PAY_PCT, PAY_FIXED = 0.029, 0.30      # Shopify/Stripe online card (SRC-U)
SUBAPP_PCT, SUBAPP_FIXED = 0.0149, 0.19  # Recharge Starter per renewal order (SRC-U; own help centre says 1.25%)
REFUND_RATES = {"3%": 0.03, "8%": 0.08}  # ASM (no sourced rate)
SUB_DISCOUNT = 0.10                   # ASM: subscription price off eye cream list
CYCLE_DAYS = 56                       # ASM: 15 ml eye cream used twice daily at ~0.2 ml/day -> ~75 days; 8 weeks is a cadence choice
RETENTION_PER_CYCLE = {"70%": 0.70, "80%": 0.80, "90%": 0.90}  # ASM
SUB_TAKE_RATE = {"15%": 0.15, "30%": 0.30, "45%": 0.45}        # ASM share of first-order customers who subscribe
CAC = [25, 40, 60]                    # ASM test points carried from earlier models

# Retail price ladders, anchored to comparables (SRC-U): Kiehl's eye $40-$60, Caudalie mist 100 ml $59 (or $42.86),
# Inkey List duos $22-$35, Augustinus Bader eye $205-$215. All prices below are ASM.
LADDERS = {
    "L1 accessible-luxury": dict(eye=44.0, mist=29.0, duo=62.0),
    "L2 luxury":            dict(eye=54.0, mist=34.0, duo=74.0),
    "L3 impulse":           dict(eye=38.0, mist=26.0, duo=52.0),
}
# first-order offer mix (share of orders): eye-only, mist-only, duo  (ASM)
MIXES = {
    "singles-led 70/10/20": (0.70, 0.10, 0.20),
    "balanced 40/10/50":    (0.40, 0.10, 0.50),
    "bundle-led 20/5/75":   (0.20, 0.05, 0.75),
}


# ---------------------------------------------------------------- functions
def pay_fees(rev):
    return PAY_PCT * rev + PAY_FIXED


def order_contribution(price, cogs, ship_cost, custom, refund, renewal=False):
    """Contribution of one order. price = merchandise price. Returns dict (all USD)."""
    ship_charged = 0.0 if (renewal or price >= FREE_SHIP_THRESHOLD) else SHIP_CHARGED_BELOW_THRESHOLD
    rev = price + ship_charged
    fees = pay_fees(rev) + ((SUBAPP_PCT * rev + SUBAPP_FIXED) if renewal else 0.0)
    refunds = refund * rev
    contrib = rev - cogs - custom - ship_cost - fees - refunds
    return dict(revenue=rev, cogs=cogs, custom=custom, ship_cost=ship_cost, fees=fees,
                refunds=refunds, contribution=contrib)


def expected_renewals(retention, cycles=6):
    # renewals at day 56, 112, ..., 336 (6 within 365 days); survival r^k to reach k-th renewal
    return sum(retention ** k for k in range(1, cycles + 1))


def evaluate(ladder, cost_tier, ship_label, custom_label, refund_label, mix_label,
             retention_label, take_label):
    L = LADDERS[ladder]
    eye_c, mist_c, _ = COST_TIERS[cost_tier]
    ship = SHIP_COST[ship_label]
    custom = CUSTOM_PACK_PER_ORDER[custom_label]
    ref = REFUND_RATES[refund_label]
    eye_only = order_contribution(L["eye"], eye_c, ship, custom, ref)
    mist_only = order_contribution(L["mist"], mist_c, ship, custom, ref)
    duo = order_contribution(L["duo"], eye_c + mist_c, ship, custom, ref)
    w_e, w_m, w_d = MIXES[mix_label]
    blended_first = w_e * eye_only["contribution"] + w_m * mist_only["contribution"] + w_d * duo["contribution"]
    blended_aov = w_e * eye_only["revenue"] + w_m * mist_only["revenue"] + w_d * duo["revenue"]
    reorder_price = L["eye"] * (1 - SUB_DISCOUNT)
    reorder = order_contribution(reorder_price, eye_c, ship, 0.0, ref, renewal=True)
    r = RETENTION_PER_CYCLE[retention_label]
    take = SUB_TAKE_RATE[take_label]
    exp_ren = expected_renewals(r)
    value_12m = blended_first + take * exp_ren * reorder["contribution"]
    return dict(ladder=ladder, cost_tier=cost_tier, ship=ship_label, custom=custom_label, refund=refund_label,
                mix=mix_label, retention=retention_label, take_rate=take_label,
                eye_only_cm=eye_only["contribution"], mist_only_cm=mist_only["contribution"],
                duo_cm=duo["contribution"], duo_revenue=duo["revenue"],
                blended_aov=blended_aov, blended_first_cm=blended_first,
                reorder_cm=reorder["contribution"], expected_renewals=exp_ren,
                value_12m=value_12m, breakeven_cac_12m=value_12m,
                duo_discount_vs_singles=1 - L["duo"] / (L["eye"] + L["mist"]))


def main():
    # ------------------------------------------------------------ assertions
    for ladder, cost_tier in itertools.product(LADDERS, COST_TIERS):
        eye_c, mist_c, _ = COST_TIERS[cost_tier]
        o = order_contribution(LADDERS[ladder]["duo"], eye_c + mist_c, 5.50, 0.0, 0.03)
        # waterfall identity two ways
        lhs = o["revenue"] - (o["cogs"] + o["custom"] + o["ship_cost"] + o["fees"] + o["refunds"])
        assert abs(lhs - o["contribution"]) < 1e-9
        rev2 = LADDERS[ladder]["duo"]  # duo is above the free-shipping line in every ladder
        assert LADDERS[ladder]["duo"] >= FREE_SHIP_THRESHOLD or ladder == "L3 impulse"
        assert abs(o["fees"] - (0.029 * rev2 + 0.30 + 0)) < 1e-9 or o["revenue"] != rev2
    # expected renewals: monotone in retention, bounded by 6
    assert expected_renewals(0.9) > expected_renewals(0.8) > expected_renewals(0.7)
    assert 0 < expected_renewals(0.9) < 6
    assert abs(expected_renewals(1.0) - 6) < 1e-9
    # hand-check one cell: L1, tier B, ship 5.50, no custom, 3% refunds, duo
    price, cogs = 62.0, 9.10 + 8.89
    rev = price                       # >= 60 -> free shipping
    expect = rev - cogs - 5.50 - (0.029 * rev + 0.30) - 0.03 * rev
    got = order_contribution(price, cogs, 5.50, 0.0, 0.03)["contribution"]
    assert abs(expect - got) < 1e-9, (expect, got)
    # re-sum: blended contribution equals mix-weighted parts
    row = evaluate("L1 accessible-luxury", "B mid / promo prices", "low 5.50", "included", "3%",
                   "balanced 40/10/50", "80%", "30%")
    assert abs(row["blended_first_cm"] - (0.4 * row["eye_only_cm"] + 0.1 * row["mist_only_cm"]
                                          + 0.5 * row["duo_cm"])) < 1e-9
    # more discount on bundle never raises duo revenue
    assert all(LADDERS[l]["duo"] < LADDERS[l]["eye"] + LADDERS[l]["mist"] for l in LADDERS)

    # ------------------------------------------------------------ full grid
    rows = []
    for combo in itertools.product(LADDERS, COST_TIERS, SHIP_COST, CUSTOM_PACK_PER_ORDER, REFUND_RATES,
                                   MIXES, RETENTION_PER_CYCLE, SUB_TAKE_RATE):
        rows.append(evaluate(*combo))
    path = os.path.join(HERE, "bundle_model_grid.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ------------------------------------------------------------ report tables
    def base(ladder, tier, mix="balanced 40/10/50", ship="low 5.50", custom="included", refund="3%",
             ret="80%", take="30%"):
        return evaluate(ladder, tier, ship, custom, refund, mix, ret, take)

    print("BASE CASE: ship $5.50, label/box included, refunds 3%, mix 40/10/50, retention 80%/cycle, 30% subscribe")
    print(f"{'ladder':24}{'cost tier':30}{'eye-only CM':>12}{'mist-only CM':>13}{'duo CM':>9}{'duo disc':>9}"
          f"{'blend AOV':>10}{'blend 1st CM':>13}{'reorder CM':>11}{'12m value':>10}")
    base_rows = []
    for ladder, tier in itertools.product(LADDERS, COST_TIERS):
        r = base(ladder, tier)
        base_rows.append(r)
        print(f"{ladder:24}{tier:30}{r['eye_only_cm']:12.2f}{r['mist_only_cm']:13.2f}{r['duo_cm']:9.2f}"
              f"{r['duo_discount_vs_singles']*100:8.0f}%{r['blended_aov']:10.2f}{r['blended_first_cm']:13.2f}"
              f"{r['reorder_cm']:11.2f}{r['value_12m']:10.2f}")
    with open(os.path.join(HERE, "bundle_model_base.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(base_rows[0].keys()))
        w.writeheader()
        w.writerows(base_rows)

    print("\nMIX EFFECT (L1, cost tier B): blended first-order contribution and 12m value by offer mix")
    for mix in MIXES:
        r = base("L1 accessible-luxury", "B mid / promo prices", mix=mix)
        print(f"  {mix:24} AOV {r['blended_aov']:6.2f}  first CM {r['blended_first_cm']:6.2f}  12m value {r['value_12m']:6.2f}")

    print("\nSHIPPING + REFUND STRESS (L1, tier B, mix 40/10/50): duo CM")
    for ship in SHIP_COST:
        for ref in REFUND_RATES:
            r = base("L1 accessible-luxury", "B mid / promo prices", ship=ship, refund=ref)
            print(f"  ship {ship:10} refunds {ref:3}: duo CM {r['duo_cm']:6.2f}  eye-only CM {r['eye_only_cm']:6.2f}  mist-only CM {r['mist_only_cm']:6.2f}")

    print("\nCUSTOM LABEL/BOX EXTRA $2.00 per order (L1, tier B)")
    r0 = base("L1 accessible-luxury", "B mid / promo prices")
    r1 = base("L1 accessible-luxury", "B mid / promo prices", custom="extra")
    print(f"  duo CM {r0['duo_cm']:.2f} -> {r1['duo_cm']:.2f}; 12m value {r0['value_12m']:.2f} -> {r1['value_12m']:.2f}")

    print("\nBREAK-EVEN CAC (= 12-month value) vs test CAC, L1 tier B, by retention and take rate")
    for ret in RETENTION_PER_CYCLE:
        line = []
        for take in SUB_TAKE_RATE:
            r = base("L1 accessible-luxury", "B mid / promo prices", ret=ret, take=take)
            line.append(f"take {take}: {r['value_12m']:6.2f}")
        print(f"  retention {ret}: " + " | ".join(line))
    print("  CAC test points:", CAC, "(a first-order contribution above CAC pays back on order 1)")

    print("\nFIRST-ORDER PAYBACK on duo (L1, tier B) vs CAC")
    r = base("L1 accessible-luxury", "B mid / promo prices")
    for c in CAC:
        print(f"  CAC ${c}: duo first-order CM {r['duo_cm']:.2f} -> net {r['duo_cm']-c:+.2f}")

    # eye-cream reorder cadence arithmetic (ASM)
    print("\nUSAGE ARITHMETIC (ASM): 15 ml eye cream at 2 uses/day x 0.10 ml = 0.20 ml/day -> %.0f days; "
          "x 0.15 ml = 0.30 ml/day -> %.0f days" % (15 / 0.20, 15 / 0.30))
    print("100 ml mist at 4 sprays/day x 0.10 ml = 0.4 ml/day -> %.0f days" % (100 / 0.4))
    print("Grid rows written:", len(rows), "->", path)


if __name__ == "__main__":
    main()
