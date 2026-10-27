#!/usr/bin/env python3
"""Delphine 25 mg caffeine pouch: cost model. Extends (does not import) the research scripts:
  research_notes/Caffeine pouch niche selection research/unit_economics.py   (parent)
  research_notes/Overnight women nurses niche research/nurse_economics.py    (nurse extension)
No supplier quote exists. Every input is tagged SRC (sourced, file cited), SRC-U (sourced but UNVERIFIED
vendor/secondary source), ASM (scenario placeholder, no source) or MISSING (not modelled).
Run:  python3 2026-10-27-delphine-cost-model.py [markdown_fragment_out]
Writes 2026-10-27-delphine-cost-model.csv next to this file (long format: section,row,column,value)."""
import csv, os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
STEM = os.path.join(HERE, "2026-10-27-delphine-cost-model")
NURSE_CSV = "/home/user/bolt/research_notes/Overnight women nurses niche research/nurse_offer_cm.csv"
NURSE_HC = "/home/user/bolt/research_notes/Overnight women nurses niche research/nurse_healthcare_discount.csv"

# ---------------- INPUTS ----------------
PPT = 20                         # ASM pouches per tin (competitors 15/18/20)
PCT, FIX = 0.029, 0.30           # SRC stripe.com/pricing, shopify.com/pricing (unit_economics.md s3)
DISPUTE_FEE = 15.0               # SRC stripe.com/pricing
REFUND = 0.02                    # ASM refunds+chargebacks as share of revenue (no benchmark found)
PICK = 2.50                      # ASM 3PL pick/pack + mailer per order
COGS = [1.50, 2.50, 3.50]        # ASM per 20-pouch tin; NO supplier quote (only low-reliability FOB hint $0.78-2.60, unit undefined)
SHIP = [5.50, 8.00]              # SRC-U USPS commercial <=4 oz pre 2026-07-12 / Pitney retail zone 1 post; flat across tins (optimistic)
SIG = 10.00                      # SRC-U adult signature ~$9-11 (3plcenter, lateshipment); legal need unknown
SUB_DISC = 0.15                  # SRC-U Wip 15% (via Roon)
CHURN = 0.08                     # SRC-U vendor blogs 5-12%/month
DAYS = 30
PRICES = [8.99, 9.99, 10.99]     # scenarios (owner brief); anchors Bucked Up 8.99, Nectr 10.99
LADDER_A = {1: 8.99, 2: 8.49, 3: 7.99, 4: 7.99, 5: 7.49}   # ASM from nurse_economics.py
SHIFTS_PER_WEEK = 3              # ASM (Elite Learning, UNVERIFIED)
SHIFTS_PER_MONTH = SHIFTS_PER_WEEK * 52 / 12
USE_LEVELS = [3, 5, 8]           # scenario pouches per shift (or per day); NOT a target
CAFFEINE_KG_PRICE = 455.0        # SRC lab reagent upper bound (Sigma); bulk food grade price: MISSING
# fixed costs (annual)
INS_LOW, INS_HIGH = 700.0, 4500.0            # SRC-U broker blogs (Assureful, Insurance Canopy)
AGE_APP_LOW, AGE_APP_HIGH = 2.0 * 12, 29.99 * 12  # SRC-U Shopify app listings: ApexAge $2/mo .. GateKeeper $29.99/mo (workplace_regulatory_claims.md)
# wholesale
WS_FREIGHT = 0.25                # ASM per tin
WS_DISCOUNTS = [("33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED)", 1 - 1 / 1.5),
                ("40% off retail (ASM)", 0.40),
                ("50% off retail (=keystone 100% markup; common, UNVERIFIED)", 0.50)]
# cash scenarios (all ASM; no supplier terms exist)
LEAD_MONTHS = 2                  # Daily Mfg self-reported ~6 weeks (UNVERIFIED), rounded up; transit MISSING

# ---------------- OUTPUT PLUMBING ----------------
csv_rows, md = [], []
def tbl(section, headers, rows, note=None):
    md.append(f"\n**{section}**\n")
    if note: md.append(note + "\n")
    md.append("| " + " | ".join(headers) + " |")
    md.append("|" + "---|" * len(headers))
    for r in rows:
        md.append("| " + " | ".join(str(c) for c in r) + " |")
        for h, c in zip(headers[1:], r[1:]):
            csv_rows.append([section, r[0], h, c])
    md.append("")
def money(x): return f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}"
def pct(x): return f"{x*100:.1f}%"

# ---------------- CORE ----------------
def order(price_tin, tins, cogs, ship, disc=0.0, sig=0.0, ship_rev=0.0, extra=0.0,
          pick=None, refund=None, pc=None, fx=None):
    pick = PICK if pick is None else pick; refund = REFUND if refund is None else refund
    pc = PCT if pc is None else pc; fx = FIX if fx is None else fx
    aov = price_tin * tins * (1 - disc)
    rev = aov + ship_rev
    c = dict(aov=aov, rev=rev, cogs=cogs * tins, fee=rev * pc + fx, refund=rev * refund,
             ship=ship, pick=pick, sig=sig, extra=extra)
    c["cm"] = rev - c["cogs"] - c["fee"] - c["refund"] - ship - pick - sig - extra
    return c
def cm(*a, **k): return order(*a, **k)["cm"]

def curve(cm1, cmr, cycle, churn, horizon):
    t = tot = 0.0; first = True
    while t < horizon:
        tot += (cm1 if first else cmr) * (1 - churn) ** int(t // DAYS); first = False; t += cycle
    return tot
def rev_curve(r1, rr, cycle, churn, horizon):
    return curve(r1, rr, cycle, churn, horizon)

checks = []
def check(name, a, b, tol=0.005):
    ok = abs(a - b) <= tol
    checks.append((name, a, b, ok))
    assert ok, f"CHECK FAILED {name}: {a} vs {b}"

# ================= 1. UNIT COSTS =================
caff = 0.025 * PPT / 1000 * CAFFEINE_KG_PRICE   # 25 mg x 20 pouches in kg x $/kg
rows = [["Caffeine active (25 mg x 20 = 0.5 g/tin at $455/kg reagent price)", money(caff), money(caff/PPT), "SRC arithmetic, upper bound (reagent, not bulk food grade)"],
        ["Fleece/pouch material, filler, sweetener, flavor", "MISSING", "MISSING", "needs supplier quote"],
        ["Tin, lid, label, insert, case packing", "MISSING", "MISSING", "needs supplier quote"],
        ["Labor, machine time, QC/testing, supplier margin", "MISSING", "MISSING", "needs supplier quote"],
        ["Inbound freight, duties (if imported), tooling/setup", "MISSING", "MISSING", "needs supplier quote"]]
for c_ in COGS:
    rows.append([f"Landed COGS scenario (all components combined)", money(c_), money(c_/PPT), f"ASM placeholder, not a quote (scenario {money(c_)})"])
tbl("1a. COGS components (every component listed; only the active is derivable)", ["Component", "Per tin", "Per pouch (20/tin)", "Status"], rows)

rows = []
for tins in (1, 3, 4):
    for cg in COGS:
        for sh in SHIP:
            p = LADDER_A[tins]; o = order(p, tins, cg, sh)
            tot_cost = o["cogs"] + o["fee"] + o["refund"] + o["ship"] + o["pick"]
            check(f"unit cost waterfall {tins}t cogs{cg} ship{sh}", o["rev"] - tot_cost, o["cm"])
            rows.append([f"{tins} tin(s) @ {money(p)}", money(cg), money(sh), money(o["aov"]),
                         money(o["cogs"]), money(o["fee"]), money(o["refund"]), money(o["ship"]), money(o["pick"]),
                         money(tot_cost), money(tot_cost/tins), money(tot_cost/tins/PPT), money(o["cm"])])
tbl("1b. Fully loaded cost per order, per tin and per pouch (free shipping, ladder A prices, no CAC, no adult signature)",
    ["Order", "COGS/tin (ASM)", "Ship cost (SRC-U)", "AOV", "COGS", "Card fee 2.9%+$0.30", "Refund 2% (ASM)", "Shipping", "Pick-pack $2.50 (ASM)",
     "Total cost", "Cost per tin", "Cost per pouch", "Contribution"], rows,
    "Formula: contribution = AOV - tins x COGS - (2.9% x AOV + 0.30) - 2% x AOV - shipping - pick-pack. Cost per tin = total cost / tins; per pouch = per tin / 20.")

# ================= 2. MARGIN =================
rows = []
for p in PRICES:
    for cg in COGS:
        rows.append([money(p), money(cg), money(p-cg), pct((p-cg)/p), money((p-cg)/PPT)])
tbl("2a. Product gross margin per tin at three retail prices (price - COGS; before fees, shipping, pick-pack)",
    ["Retail price/tin", "COGS/tin (ASM)", "Gross profit/tin", "Gross margin %", "Gross profit/pouch"], rows)

rows = []
for p in PRICES:
    for tins in (1, 3, 4):
        for sh in SHIP:
            o = order(p, tins, 2.50, sh)
            rows.append([money(p), tins, money(sh), money(o["aov"]), money(o["cm"]), pct(o["cm"]/o["aov"]), money(o["cm"]/tins)])
tbl("2b. DTC contribution at three flat retail prices (COGS $2.50 ASM, free shipping, 2% refunds, $2.50 pick-pack, no CAC)",
    ["Retail price/tin", "Tins in order", "Ship cost", "AOV", "Contribution/order", "Contribution % of AOV", "Contribution/tin"], rows)

rows = []
for p in PRICES:
    for cg in COGS:
        o = order(p, 4, cg, 5.50, disc=SUB_DISC)
        rows.append([money(p), money(cg), money(o["aov"]), money(o["cm"]), pct(o["cm"]/o["aov"])])
tbl("2c. Subscription reorder (4 tins, 15% subscription discount SRC-U, ship $5.50) contribution", ["Retail price/tin", "COGS/tin", "AOV after discount", "Contribution", "% of AOV"], rows)

rows = []
for p in PRICES:
    for lab, d in WS_DISCOUNTS:
        net = p * (1 - d)
        for cg in COGS:
            m = net - cg - WS_FREIGHT
            rows.append([money(p), lab, money(net), money(cg), money(m), pct(m/net)])
tbl("2d. Wholesale margin per tin (owner's wholesale discount is MISSING; three scenarios; freight $0.25/tin ASM; no card fee, no CAC; payment terms unknown)",
    ["Retail price/tin", "Discount off retail", "Wholesale net/tin", "COGS/tin", "Contribution/tin", "% of wholesale net"], rows)

# ---- re-verification of carried-forward conclusions against nurse CSV (independent source) ----
nurse = list(csv.DictReader(open(NURSE_CSV)))
def nurse_row(lad, tins, cogs, ship):
    return [r for r in nurse if r["ladder"] == lad and int(r["tins"]) == tins and float(r["cogs_tin"]) == cogs and float(r["ship_cost"]) == ship][0]
rows = []
for tins in (1, 2, 3, 4, 5):
    p = LADDER_A[tins]
    free = cm(p, tins, 2.50, 5.50)
    worst = cm(p, tins, 3.50, 8.00)
    sig_free = cm(p, tins, 2.50, 5.50, sig=SIG)
    aov0 = p * tins
    sr = 0.0 if aov0 >= 35 else 4.99
    thr = cm(p, tins, 2.50, 5.50, ship_rev=sr)
    thr_sig = cm(p, tins, 2.50, 5.50, ship_rev=sr, sig=SIG)
    nr = nurse_row("A_anchor_8.99", tins, 2.5, 5.5)
    check(f"match nurse csv threshold CM {tins}t", thr, float(nr["cm_first_order"]))
    check(f"match nurse csv sig CM {tins}t", thr_sig, float(nr["cm_first_order_with_10usd_adult_signature"]))
    rows.append([tins, money(p), money(free), money(worst), money(sig_free), money(thr), money(thr_sig), "yes" if free > 0 else "NO"])
tbl("2e. Re-verification of carried-forward conclusions (ladder A, COGS $2.50, ship $5.50 unless stated)",
    ["Tins", "Price/tin", "CM free ship", "CM worst case (COGS 3.50, ship 8.00)", "CM free ship + $10 adult sig", "CM with $4.99 ship fee under $35", "Same + $10 adult sig", "Positive (free ship)?"], rows,
    "Check: the threshold and adult-signature columns reproduce `nurse_offer_cm.csv` row by row (asserted in the script). Result: 1 tin loses $2.25 under free shipping, 3-4 tins is the floor, and a $10 adult-signature fee turns 1-3 tin free-shipping orders negative.")

rows = []
for tins in (3, 4):
    p = LADDER_A[tins]
    for h in (0.10, 0.15, 0.20):
        aov0 = p * tins * (1 - h); sr = 0.0 if aov0 >= 35 else 4.99
        cm1 = cm(p, tins, 2.50, 5.50, disc=h, ship_rev=sr)
        replace = cm(p, tins, 2.50, 5.50, disc=max(h, SUB_DISC), ship_rev=sr)
        stack = cm(p, tins, 2.50, 5.50, disc=1 - (1 - h) * (1 - SUB_DISC), ship_rev=sr)
        rows.append([tins, pct(h), money(cm1), money(replace), money(stack), money(replace - stack)])
        assert replace >= stack
nh = list(csv.DictReader(open(NURSE_HC)))
mm = [r for r in nh if int(r["tins"]) == 4 and float(r["healthcare_discount"]) == 0.15][0]
check("match nurse healthcare csv 4t 15% reorder no-stack", cm(7.99, 4, 2.5, 5.5, disc=0.15, ship_rev=4.99), float(mm["cm_reorder_no_stack"]))
check("match nurse healthcare csv 4t 15% stacked", cm(7.99, 4, 2.5, 5.5, disc=1-(0.85*0.85), ship_rev=4.99), float(mm["cm_reorder_stacked_with_15pct_sub"]))
tbl("2f. Healthcare discount: replace vs stack with the 15% subscription discount",
    ["Tins", "Healthcare discount", "First-order CM", "Reorder CM (replace: larger of the two)", "Reorder CM (stacked)", "CM lost by stacking"], rows,
    "Result: stacking 15% + 15% takes the 4-tin reorder from $12.28 to $8.41, so the healthcare discount should replace, not stack.")

# ================= 3. BREAK-EVEN =================
base_cm = {}
rows = []
for p in PRICES:
    o = order(p, 4, 2.50, 5.50)
    base_cm[p] = o["cm"] / 4
fixed_known_lo = INS_LOW + AGE_APP_LOW
fixed_known_hi = INS_HIGH + AGE_APP_HIGH
rows = [["Product liability insurance (annual)", money(INS_LOW), money(INS_HIGH), "SRC-U broker blogs: unit_economics.md s3 (Assureful, Insurance Canopy)"],
        ["Age-verification Shopify app (annual)", money(AGE_APP_LOW), money(AGE_APP_HIGH), "SRC-U app listing prices, $2/mo to $29.99/mo: workplace_regulatory_claims.md l.119; vendor choice not made"],
        ["Shopify plan / store software (annual)", "MISSING", "MISSING", "plan fee not recorded in any research file; owner to supply"],
        ["Trademark clearance + filing, legal/label review (one-time)", "MISSING", "MISSING", "no sourced figure; attorney quote needed"],
        ["Regulatory counsel, accountant, bookkeeping", "MISSING", "MISSING", "no sourced figure"],
        ["Product testing / COA, label design, tin tooling, photography", "MISSING", "MISSING", "no sourced figure; supplier quote"],
        ["Sourced subtotal (annual)", money(fixed_known_lo), money(fixed_known_hi), "lower bound only; true fixed costs are higher"]]
tbl("3a. Fixed costs (placeholders; MISSING items are not modelled)", ["Fixed cost", "Low", "High", "Source / status"], rows)

rows = []
for p in PRICES:
    dtc = base_cm[p]
    ws = p * (1 - 0.50) - 2.50 - WS_FREIGHT
    for lab, fx in (("sourced subtotal, low", fixed_known_lo), ("sourced subtotal, high", fixed_known_hi), ("per extra $1,000 of MISSING fixed costs", 1000.0)):
        u_dtc = fx / dtc; u_ws = fx / ws
        rows.append([money(p), lab, money(fx), money(dtc), f"{u_dtc:,.0f}", money(u_dtc * p), money(ws), f"{u_ws:,.0f}", money(u_ws * p * 0.5)])
        check(f"BE DTC back-multiply {p} {lab}", u_dtc * dtc, fx, 0.01)
tbl("3b. Break-even units and revenue (COGS $2.50 ASM; DTC = 4-tin free-ship order, ship $5.50, before CAC; wholesale = 50% off retail)",
    ["Retail price/tin", "Fixed-cost case", "Fixed costs", "DTC contribution/tin", "DTC break-even tins", "DTC break-even revenue", "Wholesale contribution/tin", "Wholesale break-even tins", "Wholesale break-even revenue"], rows,
    "Formulas: break-even tins = fixed costs / contribution per tin; break-even revenue = tins x revenue per tin (retail price for DTC, 50% of retail for wholesale). Checked by multiplying back.")

rows = []
for p in PRICES:
    c1 = order(p, 4, 2.50, 5.50)["cm"]
    for cac in (25.0, 40.0):
        rows.append([money(p), money(cac), money(c1), money(c1 - cac), "n/a (never positive on first order)" if c1 - cac <= 0 else f"{fixed_known_lo/(c1-cac):,.0f} orders"])
tbl("3c. First-order contribution after CAC (4 tins, COGS $2.50, ship $5.50). CAC values are report thresholds, not data", ["Retail price/tin", "CAC", "First-order contribution", "After CAC", "Break-even on low sourced fixed costs"], rows)

# ================= 4. CASH, FIRST THREE POs =================
def sim(Q, dep, cogs, S, fixed0, horizon=240, L=LEAD_MONTHS, n_po=3):
    cash_in_per_tin = order(7.99, 4, cogs, 5.50)["cm"] / 4 + cogs      # net receipt per tin before COGS
    cash = -fixed0; on_hand = 0.0; incoming = []; pos = []; log = []
    po_count = 0; min_cash = cash; min_m = 0; recovered = None
    for m in range(horizon + 1):
        out = 0.0; inn = 0.0; ev = []
        # arrivals
        for a in [x for x in incoming if x[0] == m]:
            out += a[2]; on_hand += Q; ev.append(f"PO{a[1]} arrives, balance paid")
        incoming = [x for x in incoming if x[0] != m]
        # place PO
        pending = sum(Q for _ in incoming)
        if po_count < n_po and (on_hand + pending <= L * S or m == 0):
            po_count += 1; d = Q * cogs * dep; out += d
            incoming.append((m + L, po_count, Q * cogs - d)); pos.append((po_count, m, m + L)); ev.append(f"PO{po_count} placed, deposit paid")
        # sell (sales in month m use stock on hand at start of month, after arrival)
        sold = min(S, on_hand) if m > 0 or on_hand > 0 else 0
        on_hand -= sold; inn = sold * cash_in_per_tin
        # supplier cost of sold units is already paid; cash_in_per_tin excludes COGS
        cash += inn - out
        if cash < min_cash: min_cash, min_m = cash, m
        log.append([m, "; ".join(ev), round(out, 2), round(inn, 2), round(cash, 2), round(on_hand, 0)])
        if po_count == n_po and not incoming and on_hand <= 0.5: break
    return min_cash, min_m, pos, log

scen = []
rows = []
fixed0 = INS_LOW + AGE_APP_LOW
for Q, qlab in ((5000, "5,000 tins (ASM, illustrative small run)"), (25000, "25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED)")):
    for dep in (0.30, 0.50, 1.00):
        for S in (500, 1500, 3000):
            mc, mm_, pos, _ = sim(Q, dep, 2.50, S, fixed0)
            rows.append([qlab, f"{int(dep*100)}%", f"{S:,}", money(Q * 2.50), money(-mc), f"month {mm_}",
                         "; ".join(f"PO{n}: m{a}->m{b}" for n, a, b in pos)])
tbl("4a. Peak funding need for the first three POs (COGS $2.50 ASM; lead time 2 months ASM; reorder when stock = lead-time demand; DTC only; excludes marketing, MISSING fixed costs, inventory not sold)",
    ["PO size", "Deposit at order", "Tins sold/month (ASM)", "One PO at COGS", "Peak cumulative cash need", "Peak occurs", "PO timing (placed -> arrives)"], rows,
    "No supplier terms exist: deposit %, balance timing, lead time, MOQ and payout timing are all scenarios. Net receipt per tin is the 4-tin ladder-A contribution plus COGS ($7.99 tin, ship $5.50), so shipping, fees, refunds and pick-pack are paid out of each sale. Marketing is excluded: at a $25 CAC (report threshold) every 100 new customers needs $2,500 cash before any reorder revenue.")

rows = []
for cg in COGS:
    mc, mm_, pos, _ = sim(25000, 0.50, cg, 1500, fixed0)
    rows.append([money(cg), money(25000 * cg), money(-mc), f"month {mm_}"])
tbl("4b. COGS sensitivity of peak cash need (25,000-tin PO, 50% deposit, 1,500 tins/month)", ["COGS/tin (ASM)", "One 25,000-tin PO", "Peak cash need", "Peak occurs"], rows)

mc, mm_, pos, log = sim(25000, 0.50, 2.50, 1500, fixed0)
tbl("4c. Monthly cash, central scenario (25,000 tins, 50% deposit, COGS $2.50, 1,500 tins/month, 2-month lead). Negative = cumulative cash below start",
    ["Month", "Events", "Cash out", "Cash in (sales)", "Cumulative cash", "Tins on hand"], [[l[0], l[1], money(l[2]), money(l[3]), money(l[4]), f"{l[5]:,.0f}"] for l in log if l[1] or l[0] % 6 == 0 or l[0] == len(log)-1])
first_rev = LEAD_MONTHS
md.append(f"Gap between first supplier payment and first revenue in this scenario: month 0 deposit to month {first_rev} receipt of stock, then sales; about 6 weeks per Daily Manufacturing's self-reported lead time (UNVERIFIED) plus MISSING transit, label/artwork and compliance holds. Payout timing from the processor is MISSING (not recorded in sources).\n")
for l in log: csv_rows.append(["4c-full monthly series", f"month {l[0]}", "cumulative cash", l[4]])
# two-way check on cash: recompute cumulative from flows
cum = -fixed0
for l in log: cum += l[3] - l[2]
check("cash series re-summed", cum, log[-1][4], 1.0)

# ================= 5. USAGE MODEL =================
rows = []
for pps in USE_LEVELS:
    pm = pps * SHIFTS_PER_MONTH
    tins_m = pm / PPT
    shifts_per_tin = PPT / pps
    cal_days_tin = shifts_per_tin / (SHIFTS_PER_WEEK / 7)
    cyc3, cyc4 = 3 * PPT / pm * DAYS, 4 * PPT / pm * DAYS
    rev_m = tins_m * LADDER_A[4] * (1 - SUB_DISC)
    cm_m = tins_m * cm(LADDER_A[4], 4, 2.50, 5.50, disc=SUB_DISC) / 4
    r1 = order(LADDER_A[4], 4, 2.50, 5.50)["aov"]; rr = order(LADDER_A[4], 4, 2.50, 5.50, disc=SUB_DISC)["aov"]
    c1 = cm(LADDER_A[4], 4, 2.50, 5.50); cr = cm(LADDER_A[4], 4, 2.50, 5.50, disc=SUB_DISC)
    rev12 = rev_curve(r1, rr, cyc4, CHURN, 365); cm12 = curve(c1, cr, cyc4, CHURN, 365)
    rows.append([f"{pps} per shift ({pps*25} mg per shift)", f"{pm:.0f}", f"{tins_m:.2f}", f"{shifts_per_tin:.1f} shifts = {cal_days_tin:.0f} calendar days", f"{cyc3:.0f} / {cyc4:.0f} days",
                 money(rev_m), money(cm_m), money(rev12), money(cm12)])
tbl("5a. SCENARIO, NOT A FORECAST: nurse pattern, 3 shifts/week = 13.0 shifts/month, pouches only on shift days (ASM)",
    ["Pouches per 12-h shift", "Pouches/month", "Tins/month", "A 20-pouch tin lasts", "Reorder cadence: 3-tin / 4-tin bundle", "Subscriber revenue/month (15% sub disc.)", "Contribution/month", "Expected 12-month revenue (8% monthly churn, 4-tin bundle)", "Expected 12-month contribution"], rows,
    "Formulas: pouches/month = per-shift x 13.0; tins/month = pouches/20; days between orders = tins in bundle x 20 / pouches per month x 30; revenue/month = tins/month x $7.99 x 0.85. Churn 8%/month (SRC-U), survival (1-0.08)^completed months. Reorder cadence is where unit counts and cash come from, not a target for customers. Usage is the customer's own choice; Delphine copy must not promote it.")
rows = []
for pps in USE_LEVELS:
    pm = pps * DAYS; tins_m = pm / PPT
    rows.append([f"{pps} per calendar day ({pps*25} mg/day)", f"{pm:.0f}", f"{tins_m:.2f}", f"{PPT/pps:.1f} days", f"{4*PPT/pm*DAYS:.0f} days", money(tins_m * LADDER_A[4] * (1 - SUB_DISC)), pct(pps * 25 / 400)])
tbl("5b. SCENARIO, NOT A FORECAST: same levels as pouches per calendar day (every day), for contrast",
    ["Pouches per day", "Pouches/month", "Tins/month", "A tin lasts", "4-tin bundle lasts", "Subscriber revenue/month", "Share of the 400 mg/day FDA reference figure"], rows,
    "400 mg/day comes from the trade explainer in CLAUDE.md (tobaccoinsider.com, not FDA); counsel decides how daily totals are shown. Higher usage means faster revenue only mechanically; none of these is a goal, a target or customer-facing copy.")

# ================= 6. SENSITIVITIES =================
BASE = dict(price=LADDER_A[4], tins=4, cogs=2.50, ship=5.50, pick=PICK, refund=REFUND, pc=PCT, fx=FIX)
def base_cm_with(**ov):
    b = dict(BASE); b.update(ov)
    return cm(b["price"], b["tins"], b["cogs"], b["ship"], pick=b["pick"], refund=b["refund"], pc=b["pc"], fx=b["fx"])
B = base_cm_with(); BA = order(7.99, 4, 2.5, 5.5)["aov"]
check("sensitivity base = 12.09", B, 12.09, 0.01)
check("sensitivity base two ways", B, 31.96 - 10.0 - (31.96*0.029+0.30) - 31.96*0.02 - 5.50 - 2.50, 0.005)
rows = []; swings = []
for name, f in (("Supplier price (COGS/tin)", lambda k: dict(cogs=2.50*k)),
                ("Shipping cost", lambda k: dict(ship=5.50*k)),
                ("Processor fees (2.9% and $0.30 scaled together)", lambda k: dict(pc=PCT*k, fx=FIX*k)),
                ("Returns/refunds rate (2% scaled)", lambda k: dict(refund=REFUND*k)),
                ("Pick-pack (ASM)", lambda k: dict(pick=PICK*k)),
                ("Retail price/tin", lambda k: dict(price=7.99*k))):
    vals = {}
    for d in (-0.20, -0.10, 0.10, 0.20):
        v = base_cm_with(**f(1 + d)); vals[d] = v
        rows.append([name, f"{d*100:+.0f}%", money(v), money(v - B), pct(v / (BA*(1+d) if name.startswith("Retail") else BA))])
    swings.append((name, abs(vals[0.20] - vals[-0.20]), vals[-0.20] - B, vals[0.20] - B))
tbl("6a. Sensitivity of 4-tin first-order contribution (ladder A $7.99/tin, COGS $2.50, ship $5.50, free shipping; base = $12.09 on $31.96 AOV)",
    ["Variable", "Change", "Contribution", "Change vs base", "Contribution % of AOV"], rows,
    "Each variable moved alone by -20%, -10%, +10%, +20%. Positive change in price improves contribution; positive change in the others reduces it.")
rows = []
for k in (0.5, 1.0, 2.0, 2.5, 5.0):
    rate = REFUND * k
    rows.append([pct(rate), money(base_cm_with(refund=rate)), money(base_cm_with(refund=rate) - B)])
tbl("6b. Returns rate beyond +/-20% (the 2% base has no benchmark behind it; +/-20% of 2% is only 0.4 points)", ["Refund + chargeback rate of revenue", "Contribution", "Change vs base"], rows,
    f"A single lost dispute also costs the ${DISPUTE_FEE:.0f} Stripe dispute fee (SRC) on top of the order value.")

# ================= 7. RANKED ASSUMPTIONS =================
full = []
full.append(("Supplier price: COGS $1.50 to $3.50 per tin", abs(base_cm_with(cogs=1.5) - base_cm_with(cogs=3.5)), "ASM, no quote"))
full.append(("Tins per order: 1 tin vs 4 tins (free shipping)", abs(cm(8.99, 1, 2.5, 5.5) - B), "ASM mix, no data"))
full.append(("Adult signature on/off ($10)", SIG, "SRC-U fee; legal need unknown"))
full.append(("Shipping cost $5.50 vs $8.00", abs(base_cm_with(ship=8.0) - B), "SRC-U"))
full.append(("Retail price per tin +/-10% ($7.99 base)", abs(base_cm_with(price=7.99*1.1) - base_cm_with(price=7.99*0.9)), "ASM ladder"))
full.append(("Pick-pack/3PL $1.50 to $3.50 (+/-$1)", abs(base_cm_with(pick=3.5) - base_cm_with(pick=1.5)), "ASM"))
full.append(("Refund rate 0% to 5%", abs(base_cm_with(refund=0.0) - base_cm_with(refund=0.05)), "ASM"))
full.append(("Processor fees +/-20%", abs(base_cm_with(pc=PCT*1.2, fx=FIX*1.2) - base_cm_with(pc=PCT*0.8, fx=FIX*0.8)), "SRC"))
full.sort(key=lambda x: -x[1])
rows = [[i + 1, n, money(s), f"{s/B*100:.0f}% of base contribution", st] for i, (n, s, st) in enumerate(full)]
tbl("7. Assumptions ranked by how much they move 4-tin first-order contribution (largest swing first)", ["Rank", "Assumption and range tested", "Swing in contribution", "Relative to base ($12.09)", "Input status"], rows)
rows = [[i + 1, n, money(s), money(a), money(b)] for i, (n, s, a, b) in enumerate(sorted(swings, key=lambda x: -x[1]))]
tbl("7b. Same ranking restricted to uniform +/-20% moves", ["Rank", "Variable", "Swing (-20% to +20%)", "Change at -20%", "Change at +20%"], rows)
# check ranking two ways: swing sum equals direct difference
for n, s_, a, b in swings: check(f"swing {n}", s_, abs((B + b) - (B + a)), 1e-9)

# ================= 8. WHAT MUST BE TRUE =================
def bisect_cogs(target, f):
    lo, hi = 0.0, 20.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(mid) >= target: lo = mid
        else: hi = mid
    return lo
c4 = lambda cg: cm(7.99, 4, cg, 5.50); c3 = lambda cg: cm(7.99, 3, cg, 5.50)
mix = lambda cg, share_small=0.30: (1 - share_small) / 2 * (c3(cg) + c4(cg)) + share_small * cm(8.99, 1, cg, 5.50)
def cust12(cg, pps=3, tins=4):
    pm = pps * SHIFTS_PER_MONTH; cyc = tins * PPT / pm * DAYS
    return curve(cm(7.99, tins, cg, 5.50), cm(7.99, tins, cg, 5.50, disc=SUB_DISC), cyc, CHURN, 365)
rows = [
 ["Blended first-order contribution is positive with 70% of orders at 3-4 tins and 30% at 1 tin", f"mix contribution at COGS $2.50 = {money(mix(2.50))}", f"max COGS/tin = {money(bisect_cogs(0, mix))}", "PASS at ASM inputs" if mix(2.50) > 0 else "FAIL"],
 ["The same mix with 50% of orders at 1 tin", f"{money(mix(2.50, 0.5))}", f"max COGS/tin = {money(bisect_cogs(0, lambda c: mix(c, 0.5)))}", "PASS" if mix(2.50, 0.5) > 0 else "FAIL (1-tin share must stay small)"],
 ["COGS near $2.50 per tin (report threshold)", "needs supplier quote", f"4-tin order breaks even on CM at COGS {money(bisect_cogs(0, c4))}; first-order contribution never reaches a $25 CAC (even $0 COGS gives {money(c4(0))})", "UNKNOWN until quote"],
 ["12-month contribution per customer covers a $25 CAC (4-tin bundle, 3 pouches/shift scenario, 8% churn)", f"{money(cust12(2.50))} at COGS $2.50", f"max COGS/tin = {money(bisect_cogs(25, cust12))}", "PASS at ASM inputs" if cust12(2.50) >= 25 else "FAIL"],
 ["Same at a $40 CAC", f"{money(cust12(2.50))}", f"max COGS/tin = {money(bisect_cogs(40, cust12)) if cust12(0.0)>=40 else 'not reachable'}", "PASS" if cust12(2.50) >= 40 else "FAIL (needs higher usage or price; usage is not a lever to promote)"],
 ["Shipping near $5.50 per order", "SRC-U pre 2026-07-12; retail zone 1 is $7.90", f"4-tin CM at ship $8.00 = {money(cm(7.99,4,2.5,8.0))}; 3-tin = {money(cm(7.99,3,2.5,8.0))}", "UNKNOWN until 3PL quote and tin weight"],
 ["No adult signature on delivery", f"4-tin CM with $10 signature = {money(cm(7.99,4,2.5,5.5,sig=SIG))}; 3-tin = {money(cm(7.99,3,2.5,5.5,sig=SIG))}", "needs counsel: is a signature required?", "OPEN (counsel)"],
 ["Healthcare discount replaces, never stacks", f"4-tin reorder {money(cm(7.99,4,2.5,5.5,disc=0.15,ship_rev=4.99))} replaced vs {money(cm(7.99,4,2.5,5.5,disc=1-0.85*0.85,ship_rev=4.99))} stacked (incl. $4.99 customer shipping under $35)", "policy decision", "OWNER DECISION"],
 ["Disputes stay under card-network thresholds (Visa monitoring reported 0.9% to 1.5%, conflicting)", f"each dispute costs ${DISPUTE_FEE:.0f} plus the order", "processor underwriting must accept the category", "UNKNOWN"],
 ["Counsel clearances: trademark (Delphine), regulatory category, label, age policy, adult-signature, state laws", "none recorded in decisions.md", "gate", "NOT CLEARED: no inventory spend"],
 ["Supplier terms: MOQ, deposit, lead time, price breaks", "none exist", f"one 25,000-tin PO is {money(25000*1.5)} to {money(25000*3.5)} at scenario COGS", "UNKNOWN until RFQ (not sent)"],
]
tbl("8. Go/no-go: what must be true", ["Condition", "Modelled result", "Threshold / what it needs", "Status"], rows,
    "This is a model screen, not an approval. Nothing here clears the compliance gate in CLAUDE.md.")

# ---------------- WRITE ----------------
with open(STEM + ".csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["section", "row", "column", "value"]); w.writerows(csv_rows)
md.append("\nSelf-checks passed (asserted in script): " + "; ".join(f"{n}" for n, a, b, ok in checks[:6]) + f"; ... total {len(checks)} checks, all within tolerance.\n")
out = "\n".join(md)
if len(sys.argv) > 1: open(sys.argv[1], "w").write(out)
else: print(out)
print(f"checks passed: {len(checks)}; csv rows: {len(csv_rows)}", file=sys.stderr)
