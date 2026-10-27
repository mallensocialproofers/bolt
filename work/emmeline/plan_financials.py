#!/usr/bin/env python3
"""Emmeline 12-month plan financials on SelfNamed 'face value' (2026-10-27).

Face value = SelfNamed's page claims taken as true: no MOQ, made on demand, dropshipped to the
customer, Pro plan $29/month (SRC), catalogue prices read from the owner's screenshot (SRC).
Everything else is a labelled scenario: nothing here is a forecast.

Tags: SRC read from a page/screenshot, SRC-U unverified secondary source, ASM assumption, ARITH derived.
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bundle_model as m  # noqa: E402

# ------------------------------------------------------------------ offer (ASM)
EYE, MIST, PAIR = 48.0, 32.0, 72.0           # retail prices (ASM; pair = 10% under singles)
MIX = (0.40, 0.10, 0.50)                      # eye-only, mist-only, pair share of first orders (ASM)
SHIP = 5.50                                   # USPS under 1 lb, low end (SRC-U); high end $8.40 tested elsewhere
REFUND = 0.03                                 # ASM
RENEW_EVERY_MONTHS = 2                        # ASM, 8-week cadence rounded to 2 months
MAX_RENEWALS = 6

# ------------------------------------------------------------------ cost tiers
TIERS = {
    "face-value list (tier B)": (m.COST_TIERS["B mid / promo prices"][0], m.COST_TIERS["B mid / promo prices"][1], 0.0),
    "Pro prices (tier A) + Pro fee": (m.COST_TIERS["A pink-badge (Pro?) prices"][0], m.COST_TIERS["A pink-badge (Pro?) prices"][1], 29.0),
}

# ------------------------------------------------------------------ outcome cases (ASM)
CASES = {
    "pessimistic": dict(cac=60, retention=0.70, take=0.15, organic=[3] * 12),
    "base":        dict(cac=40, retention=0.80, take=0.30, organic=[5, 5, 8, 8, 10, 10, 12, 12, 15, 15, 15, 15]),
    "optimistic":  dict(cac=25, retention=0.90, take=0.45, organic=[8, 8, 12, 15, 18, 20, 22, 24, 26, 28, 30, 30]),
}

# ------------------------------------------------------------------ paid budget envelopes (ASM)
ENVELOPES = {
    "lean $5k paid": [0, 0, 250, 250, 500, 500, 500, 750, 750, 750, 0, 0],
    "growth $20k paid": [0, 0, 500, 1000, 1500, 2000, 2500, 3000, 3000, 3000, 2500, 1000],
}

# ------------------------------------------------------------------ fixed costs (monthly unless noted)
FIXED_MONTHLY = {
    "Shopify plan (ASM; plan price not sourced here)": 39.0,
    "Subscription app: Shopify Subscriptions, reported free (SRC-U)": 0.0,
    "Email/SMS tool and misc apps (ASM)": 30.0,
}
FIXED_ONE_TIME = {      # all unsourced placeholders; owner/counsel must replace
    "Trademark attorney search (placeholder, missing input)": 1500.0,
    "Cosmetics counsel: MoCRA, claims, label review (placeholder, missing input)": 1500.0,
    "Samples from SelfNamed, 3 products (price not on page; placeholder)": 150.0,
    "Product liability insurance, first year (sourced range $700-$4,500, SRC-U; midpoint-ish)": 1500.0,
    "Domain, email, photography/AI imagery (ASM)": 150.0,
}


def unit_economics(tier):
    eye_c, mist_c, _ = TIERS[tier]
    eo = m.order_contribution(EYE, eye_c, SHIP, 0.0, REFUND)
    mo = m.order_contribution(MIST, mist_c, SHIP, 0.0, REFUND)
    pr = m.order_contribution(PAIR, eye_c + mist_c, SHIP, 0.0, REFUND)
    first_cm = MIX[0] * eo["contribution"] + MIX[1] * mo["contribution"] + MIX[2] * pr["contribution"]
    first_rev = MIX[0] * eo["revenue"] + MIX[1] * mo["revenue"] + MIX[2] * pr["revenue"]
    ren = m.order_contribution(EYE * (1 - m.SUB_DISCOUNT), eye_c, SHIP, 0.0, REFUND, renewal=True)
    return dict(eye_only=eo, mist_only=mo, pair=pr, first_cm=first_cm, first_rev=first_rev, renewal=ren)


def run(case, envelope, tier):
    ue = unit_economics(tier)
    c = CASES[case]
    paid = ENVELOPES[envelope]
    new = [paid[i] / c["cac"] + c["organic"][i] for i in range(12)]
    subs = [c["take"] * n for n in new]
    renewals = []
    for mth in range(12):
        tot = 0.0
        for coh in range(12):
            d = mth - coh
            if d > 0 and d % RENEW_EVERY_MONTHS == 0:
                k = d // RENEW_EVERY_MONTHS
                if k <= MAX_RENEWALS:
                    tot += subs[coh] * (c["retention"] ** k)
        renewals.append(tot)
    pro_fee = TIERS[tier][2]
    rows = []
    cum = -sum(FIXED_ONE_TIME.values())
    min_cum = cum
    first_month_pos = None
    for mth in range(12):
        first_rev = new[mth] * ue["first_rev"]
        first_cm = new[mth] * ue["first_cm"]
        ren_rev = renewals[mth] * ue["renewal"]["revenue"]
        ren_cm = renewals[mth] * ue["renewal"]["contribution"]
        fixed = sum(FIXED_MONTHLY.values()) + pro_fee
        net = first_cm + ren_cm - fixed - paid[mth]
        cum += net
        min_cum = min(min_cum, cum)
        if first_month_pos is None and cum > 0:
            first_month_pos = mth + 1
        rows.append(dict(case=case, envelope=envelope, tier=tier, month=mth + 1, new_customers=new[mth],
                         renewals=renewals[mth], revenue=first_rev + ren_rev, contribution=first_cm + ren_cm,
                         fixed=fixed, ad_spend=paid[mth], net=net, cumulative=cum))
    # assertions: re-sum two ways
    tot_net = sum(r["net"] for r in rows)
    assert abs(tot_net - (sum(r["contribution"] for r in rows) - sum(r["fixed"] for r in rows)
                          - sum(r["ad_spend"] for r in rows))) < 1e-6
    assert abs(rows[-1]["cumulative"] - (tot_net - sum(FIXED_ONE_TIME.values()))) < 1e-6
    summary = dict(case=case, envelope=envelope, tier=tier,
                   customers=sum(new), orders=sum(new) + sum(renewals),
                   revenue=sum(r["revenue"] for r in rows),
                   contribution=sum(r["contribution"] for r in rows),
                   ad_spend=sum(paid), fixed=sum(r["fixed"] for r in rows) + sum(FIXED_ONE_TIME.values()),
                   net_12m=rows[-1]["cumulative"], peak_cash_need=-min_cum,
                   cumulative_positive_month=first_month_pos)
    return rows, summary


def main():
    # unit-economics sanity: hand-check the pair in tier B
    ue = unit_economics("face-value list (tier B)")
    rev = PAIR
    expect = rev - (9.10 + 8.89) - SHIP - (0.029 * rev + 0.30) - REFUND * rev
    assert abs(ue["pair"]["contribution"] - expect) < 1e-9
    # Pro plan break-even: monthly savings on pair orders vs $29
    save_per_pair = (9.10 + 8.89) - (5.44 + 5.78)
    print("PRO PLAN: saves $%.2f per pair order (COGS 17.99 -> 11.22), $%.2f per eye-only order (9.10 -> 5.44), "
          "$%.2f per mist-only order (8.89 -> 5.78). $29/month breaks even at about %.1f pair orders a month."
          % (save_per_pair, 9.10 - 5.44, 8.89 - 5.78, 29 / save_per_pair))
    print()
    for tier in TIERS:
        u = unit_economics(tier)
        print(f"UNIT ECONOMICS [{tier}] eye ${EYE:.0f} / mist ${MIST:.0f} / pair ${PAIR:.0f}, ship ${SHIP}, refunds {REFUND:.0%}")
        print(f"  eye-only CM {u['eye_only']['contribution']:.2f} (rev {u['eye_only']['revenue']:.2f}) | mist-only CM {u['mist_only']['contribution']:.2f} | "
              f"pair CM {u['pair']['contribution']:.2f} ({u['pair']['contribution']/u['pair']['revenue']:.0%} of revenue) | blended 1st-order CM {u['first_cm']:.2f} on AOV {u['first_rev']:.2f} | "
              f"renewal (eye at 10% off) CM {u['renewal']['contribution']:.2f}")
    print()
    all_rows, summaries = [], []
    for tier in TIERS:
        for env in ENVELOPES:
            for case in CASES:
                rows, s = run(case, env, tier)
                all_rows += rows
                summaries.append(s)
    hdr = f"{'tier':32}{'envelope':18}{'case':13}{'cust':>7}{'orders':>8}{'revenue':>10}{'contrib':>9}{'ads':>8}{'fixed':>8}{'12m net':>9}{'peak cash':>10}{'cum>0 mo':>9}"
    print(hdr)
    for s in summaries:
        print(f"{s['tier']:32}{s['envelope']:18}{s['case']:13}{s['customers']:7.0f}{s['orders']:8.0f}{s['revenue']:10.0f}"
              f"{s['contribution']:9.0f}{s['ad_spend']:8.0f}{s['fixed']:8.0f}{s['net_12m']:9.0f}{s['peak_cash_need']:10.0f}"
              f"{str(s['cumulative_positive_month']):>9}")
    with open(os.path.join(HERE, "plan_financials_monthly.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)
    with open(os.path.join(HERE, "plan_financials_summary.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summaries[0].keys()))
        w.writeheader()
        w.writerows(summaries)
    print("\nOne-time costs included (placeholders, all UNSOURCED unless tagged):")
    for k, v in FIXED_ONE_TIME.items():
        print(f"  ${v:,.0f}  {k}")
    print("Monthly fixed:")
    for k, v in FIXED_MONTHLY.items():
        print(f"  ${v:,.0f}  {k}")
    print(f"  (+ $29 Pro plan in the Pro-prices tier)")


if __name__ == "__main__":
    main()
