#!/usr/bin/env python3
"""Nurse-niche extension of ../Caffeine pouch niche selection research/unit_economics.py.
Self-contained (does NOT import the parent script, so it writes nothing into that folder).
Input tags: SRC = sourced (see economics_offer_positioning.md), ASM = assumption/scenario.
Run: python3 nurse_economics.py   -> prints tables, writes nurse_*.csv next to this file."""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
# ---- inherited inputs (unit_economics.py) ----
PPT = 20                      # ASM pouches per tin (competitors 15/18/20)
STRIPE_PCT, STRIPE_FIX = 0.029, 0.30   # SRC stripe.com/pricing, shopify.com/pricing
REFUND = 0.02                 # ASM refund+chargeback share of revenue
PICKPACK = 2.50               # ASM
COGS = [1.50, 2.50, 3.50]     # ASM per 20-pouch tin, no source
SHIP = [5.50, 8.00]           # SRC-anchored (Ship.com pre-7/12; Pitney retail), flat regardless of tins (optimistic)
SUB_DISC = 0.15               # SRC-UNVERIFIED (Wip via Roon)
CHURN = 0.08                  # SRC-UNVERIFIED vendor blogs 5-12%; mid
DAYS = 30
# ---- nurse-specific scenario inputs ----
SHIFTS_PER_WEEK = 3           # ASM-labelled: "3 x 12-hour" pattern (Elite Learning, UNVERIFIED; 36 h/wk)
SHIFTS_PER_MONTH = SHIFTS_PER_WEEK*52/12     # = 13.0 (arithmetic)
PER_SHIFT = [3, 5, 8]         # ASM illustrative pouches per 12-h shift; NOT a target

def cm_order(price_tin, tins, cogs, ship, disc=0.0, adult_sig=0.0, ship_rev=0.0, extra=0.0):
    """CM = AOV - COGS - (2.9% AOV+0.30) - 2% AOV - shipping - pick/pack - adult sig - extra packaging + customer-paid shipping."""
    aov = price_tin*tins*(1-disc)
    rev = aov + ship_rev
    cm = rev - cogs*tins - (rev*STRIPE_PCT+STRIPE_FIX) - rev*REFUND - ship - PICKPACK - adult_sig - extra
    return aov, cm

def curve(cm1, cmr, cycle_days, churn, horizon_days):
    t=0.0; tot=0.0; first=True
    while t < horizon_days:
        tot += (cm1 if first else cmr)*(1-churn)**int(t//DAYS); first=False; t+=cycle_days
    return tot

def payback(cm1, cmr, cycle_days, churn, cac, cap=730):
    t=0.0; cum=0.0; first=True
    while t<cap:
        cum += (cm1 if first else cmr)*(1-churn)**int(t//DAYS); first=False
        if cum>=cac: return int(round(t))
        t+=cycle_days
    return None

# ---------- A. cadence ----------
cad=[]
print("A. CADENCE (3 shifts/wk -> %.1f shifts/month; pouches only on shift days, ASM)"%SHIFTS_PER_MONTH)
for pps in PER_SHIFT:
    pm = pps*SHIFTS_PER_MONTH
    for ppt in (15,20):
        tins_m = pm/ppt
        row=[pps, pps*25, round(pm,1), ppt, round(tins_m,2)]
        for b in (3,4,5):
            row.append(round(b*ppt/pm*DAYS,1))   # days a b-tin bundle lasts
        cad.append(row)
        print(f" {pps}/shift ({pps*25} mg/shift) {pm:5.1f} pouches/mo | {ppt}/tin -> {tins_m:4.2f} tins/mo | bundle lasts days 3/4/5 tins: {row[5]}/{row[6]}/{row[7]}")
with open(os.path.join(HERE,"nurse_cadence.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["pouches_per_shift","mg_per_shift","pouches_per_month","pouches_per_tin","tins_per_month","days_3tin_bundle","days_4tin_bundle","days_5tin_bundle"]); w.writerows(cad)

# ---------- B. offer ladders ----------
LADDERS = {"A_anchor_8.99":{1:8.99,2:8.49,3:7.99,4:7.99,5:7.49},      # ASM, anchored to sourced $7.50-$8.25 multipack per tin & $8.99 single
           "B_anchor_10.99":{1:10.99,2:10.49,3:9.99,4:9.99,5:9.49}}   # ASM, anchored to Nectr Energy single / Roon sub $9.16-12.49
THRESH = 35.0   # SRC Roon free-ship threshold (also $45 on other Roon pages; Nectr $50)
CUST_SHIP = 4.99  # ASM customer-paid shipping below threshold
print("\nB. FIRST-ORDER CM by ladder / tins / COGS / ship (free shipping at AOV>=$%.0f, else customer pays $%.2f; no adult signature)"%(THRESH,CUST_SHIP))
rows=[]
for lname,lad in LADDERS.items():
    for tins,p in lad.items():
        for cogs in COGS:
            for ship in SHIP:
                aov0=p*tins
                sr = 0.0 if aov0>=THRESH else CUST_SHIP
                aov,cm = cm_order(p,tins,cogs,ship,ship_rev=sr)
                _,cm_sig = cm_order(p,tins,cogs,ship,ship_rev=sr,adult_sig=10.0)
                rows.append([lname,tins,p,round(aov0,2),cogs,ship,sr,round(cm,2),round(cm_sig,2)])
with open(os.path.join(HERE,"nurse_offer_cm.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["ladder","tins","price_per_tin","aov","cogs_tin","ship_cost","customer_paid_ship","cm_first_order","cm_first_order_with_10usd_adult_signature"]); w.writerows(rows)
for lname in LADDERS:
    print(f" {lname}: CM1 at COGS 1.50/2.50/3.50, ship 5.50  |  ship 8.00  |  with $10 adult signature (COGS 2.50, ship 5.50)")
    for tins in (1,2,3,4,5):
        g=lambda c,s:[r for r in rows if r[0]==lname and r[1]==tins and r[4]==c and r[5]==s][0]
        a=[g(c,5.5)[7] for c in COGS]; b=[g(c,8.0)[7] for c in COGS]; r0=g(2.5,5.5)
        print(f"   {tins} tin(s) ${r0[2]}/tin AOV ${r0[3]:>6}: {a} | {b} | sig {r0[8]}")

# ---------- C. healthcare-verified discount ----------
print("\nC. VERIFIED-HEALTHCARE DISCOUNT: first-order CM and reorder CM (COGS 2.50, ship 5.50, ladder A; reorder discount = max(healthcare, 15% sub) i.e. NOT stacked)")
drows=[]
for tins in (3,4,5):
    p=LADDERS["A_anchor_8.99"][tins]
    for h in (0.0,0.10,0.15,0.20):
        aov0=p*tins*(1-h); sr=0.0 if aov0>=THRESH else CUST_SHIP
        aov,cm1=cm_order(p,tins,2.5,5.5,disc=h,ship_rev=sr)
        _,cmr=cm_order(p,tins,2.5,5.5,disc=max(h,SUB_DISC),ship_rev=0.0 if aov0>=THRESH else CUST_SHIP)
        _,cmr_stack=cm_order(p,tins,2.5,5.5,disc=1-(1-h)*(1-SUB_DISC),ship_rev=sr)
        drows.append([tins,p,h,round(aov,2),round(cm1,2),round(cmr,2),round(cmr_stack,2)])
        print(f" {tins} tins disc {int(h*100):>2}%: AOV ${aov:6.2f} CM1 ${cm1:6.2f} | reorder CM (no stack) ${cmr:6.2f} | stacked w/15% sub ${cmr_stack:6.2f}")
with open(os.path.join(HERE,"nurse_healthcare_discount.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["tins","price_per_tin_list","healthcare_discount","aov_after_discount","cm_first_order","cm_reorder_no_stack","cm_reorder_stacked_with_15pct_sub"]); w.writerows(drows)

# ---------- D. break-even CAC and payback at nurse cadence ----------
print("\nD. NURSE CADENCE: break-even CAC (8% churn) and payback days at CAC $25/$40/$60. COGS 2.50, ship 5.50, ladder A, 15% sub on reorders, 20 pouches/tin")
prow=[]
for tins in (3,4,5):
    p=LADDERS["A_anchor_8.99"][tins]
    aov0=p*tins; sr=0.0 if aov0>=THRESH else CUST_SHIP
    _,cm1=cm_order(p,tins,2.5,5.5,ship_rev=sr)
    _,cmr=cm_order(p,tins,2.5,5.5,disc=SUB_DISC,ship_rev=sr)
    for pps in PER_SHIFT:
        pm=pps*SHIFTS_PER_MONTH; cyc=tins*PPT/pm*DAYS
        be=[round(curve(cm1,cmr,cyc,CHURN,h),2) for h in (90,180,365)]
        pb=[payback(cm1,cmr,cyc,CHURN,c) for c in (25,40,60)]
        prow.append([tins,round(aov0,2),pps,round(pm,1),round(cyc,1),round(cm1,2),round(cmr,2),*be,*pb])
        print(f" {tins}t AOV ${aov0:6.2f} {pps}/shift cycle {cyc:5.1f}d CM1 {cm1:6.2f} CMre {cmr:6.2f} | BE-CAC 1st {cm1:6.2f} 90d {be[0]:7.2f} 180d {be[1]:7.2f} 365d {be[2]:7.2f} | payback {pb}")
with open(os.path.join(HERE,"nurse_payback.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["tins","aov","pouches_per_shift","pouches_per_month","days_between_orders","cm_first","cm_reorder_sub15","be_cac_90d","be_cac_180d","be_cac_365d","payback_days_cac25","payback_days_cac40","payback_days_cac60"]); w.writerows(prow)

# ---------- E. CAC implied by sourced benchmarks (arithmetic) ----------
print("\nE. CAC IMPLIED BY BENCHMARKS (first-order, AOV/ROAS). ROAS SRC-UNVERIFIED: healthcare Meta 2.8 avg, prospecting 1.8-3.2 (Ryze via Webtonic); generic DTC median 2.7-2.96 (Top Growth)")
for tins in (3,4,5):
    aov=LADDERS["A_anchor_8.99"][tins]*tins
    print(f" {tins} tins AOV ${aov:.2f}: CAC at ROAS 1.8/2.8/3.2 = "+"/".join(f"${aov/r:.2f}" for r in (1.8,2.8,3.2)))
print(" CPC->CAC (CPC SRC-UNVERIFIED $1.58 healthcare avg Superads/Oyova; $2.64 health&fitness Hawky; conversion rate ASM):")
for cpc in (1.58,2.64):
    print("  CPC $%.2f: CAC at 1%%/2%%/3%% site conversion = "%cpc + "/".join(f"${cpc/c:.2f}" for c in (0.01,0.02,0.03)))

# ---------- F. gifting + wholesale ----------
print("\nF. GIFT BUNDLE (ASM: 4 tins + gift sleeve/insert $2.00 extra cost, premium price) CM, COGS 2.50, ship 5.50, free ship")
for price in (34.99,39.99,44.99):
    aov,cm=cm_order(price/4,4,2.5,5.5,extra=2.0)
    print(f"  gift 4-tin ${price}: per tin ${price/4:.2f} CM1 ${cm:.2f} ({cm/aov*100:.0f}%)")
print("\nG. HOSPITAL GIFT SHOP / CAFE WHOLESALE: retailer markup on cost (SRC-UNVERIFIED: >=50% consultant via Clarivate; keystone 100% common) ; MSRP ASM; freight $0.25/tin ASM; optional distributor 20% (ASM, vendor range 15-35%)")
wr=[]
for msrp in (7.99,8.99,10.99):
    for mk,lab in ((0.5,"50% markup"),(1.0,"keystone 100%")):
        for dm in (0.0,0.20):
            cost=msrp/(1+mk); net=cost*(1-dm)
            cms=[round(net-c-0.25,2) for c in COGS]
            wr.append([msrp,lab,dm,round(cost,2),round(net,2),*cms])
            print(f"  MSRP {msrp} {lab:14s} dist {int(dm*100):>2}%: retailer pays ${cost:5.2f}, brand net ${net:5.2f}, CM/tin at COGS 1.50/2.50/3.50 = {cms}")
with open(os.path.join(HERE,"nurse_wholesale_gift.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["msrp","retailer_markup_on_cost","distributor_pct","retailer_cost","brand_net","cm_cogs1.50","cm_cogs2.50","cm_cogs3.50"]); w.writerows(wr)
