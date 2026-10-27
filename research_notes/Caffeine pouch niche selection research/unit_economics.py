#!/usr/bin/env python3
"""Contribution-margin model for a 25 mg caffeine pouch. Every input is tagged
SRC (sourced, see unit_economics.md) or ASSUMPTION (scenario, no source).
Outputs: unit_economics_competitors.csv, unit_economics_model.csv, stdout tables."""
import csv, itertools, os
HERE = os.path.dirname(os.path.abspath(__file__))
STEM = os.path.join(HERE, "unit_economics")

# ---------- 1. competitor per-pouch / per-100mg (SRC: see md section 1) ----------
# brand, label, price_total, tins, pouches_per_tin, mg, source_note
comp = [
 ("Nectr Energy","site 4-pack (inferred)",32.99,4,20,50,"nectr.energy 2026-10-27; 4 tins inferred from Roon $8.25/tin"),
 ("Nectr Focus+","site 5-pack (inferred)",39.99,5,20,50,"nectr.energy; Roon $8.00 in 5-pack"),
 ("Nectr Zero","site 4-pack (inferred)",29.99,4,20,0,"caffeine-free; excluded from per-100mg"),
 ("Nectr Energy","single tin",10.99,1,20,50,"Roon takeroon.com cheapest-nootropic page, 'early 2026'"),
 ("Nectr Focus+","single tin",11.99,1,20,50,"same"),
 ("Roon","one-time tin",15.00,1,15,80,"takeroon.com 2026-10-27 / Roon page"),
 ("Roon","subscription tin",9.16,1,15,80,"takeroon.com '$9.16/tin' 12-tin plan"),
 ("Wip 100mg","3-can Walmart",21.99,3,15,100,"Walmart listing via search; Roon $0.489"),
 ("Wip 200mg","3-can",24.99,3,15,200,"Roon table; UNVERIFIED"),
 ("Wip","SRP per can",5.99,1,10,100,"Prepared Foods/Webull: $5.99 per 10-pouch can (launch; mg not stated)"),
 ("Mojo 50mg","single",7.99,1,15,50,"Roon table; UNVERIFIED"),
 ("Mojo 100mg","single",8.99,1,15,100,"Roon table; UNVERIFIED"),
 ("Ultra Focus (0 mg caff.)","can",16.00,1,15,0,"Roon; no caffeine - excluded"),
 ("Grinds 25mg","can",5.95,1,18,25,"Roon table; Walmart lists 15/18/20 per can - UNVERIFIED count"),
 ("Grinds 25mg","can (alt)",5.99,1,18,25,"Roon cheapest-per-serving page"),
 ("NZE 50mg","5-pack",34.99,5,15,50,"Roon table; nzepouches per search"),
 ("Bucked Up PWR Buck","tin",8.99,1,20,50,"living.fit retailer page (search), sold out"),
 ("Bucked Up PWR Buck","tin, buy 3+",8.09,1,20,50,"living.fit retailer tier"),
 ("Plopii Focus (paraxanthine)","can",9.99,1,20,0,"launch price, Roon review; not caffeine"),
 ("Wild Pouches","5 cans",39.96,5,20,60,"wild-pouches.com/pages/lp-buy-box-v9 (20% off $49.95); 60 or 120 mg; mg of this pack not stated"),
]
rows=[]
for b,l,p,t,n,mg,src in comp:
    pp=p/(t*n)
    per100=(pp/mg*100) if mg else None
    rows.append([b,l,p,t,n,mg,round(pp,3),round(per100,3) if per100 else "",src])
with open(STEM+"_competitors.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["brand","pack","price_usd","tins","pouches_per_tin","mg_per_pouch","usd_per_pouch","usd_per_100mg","source_note"]); w.writerows(rows)
print("COMPETITORS (per pouch, per 100 mg)")
for r in rows: print(f"{r[0]:28s}{r[1]:24s} ${r[6]:.3f}/pouch  {('$%.2f'%r[7]) if r[7]!='' else 'n/a':>7}/100mg")

# ---------- 2. inputs ----------
POUCHES_PER_TIN = 20            # ASSUMPTION (competitors 15/18/20)
TIN_PRICES = [5.99, 8.99, 10.99]# SRC anchors: Grinds ~$5.95-5.99; Bucked Up $8.99; Nectr Energy $10.99
COGS_TIN = [1.50, 2.50, 3.50]   # ASSUMPTION - NO SOURCE (only a low-reliability FOB $0.78-2.60 range, unit undefined)
STRIPE_PCT, STRIPE_FIX = 0.029, 0.30   # SRC stripe.com/pricing, shopify.com/pricing (Basic 2.9%+30c)
SHIP = [5.50, 8.00]             # SRC anchor: Ship.com USPS GA commercial <=4oz $5.50 (pre 2026-07-12) / Pitney retail Zone1 1-4oz $7.90 (post)
PICKPACK = 2.50                 # ASSUMPTION - NO SOURCE (3PL pick/pack + mailer)
REFUND_RATE = 0.02              # ASSUMPTION - returns/refunds + chargebacks as % of revenue (no category benchmark found)
CHURN = [0.05,0.08,0.12]        # SRC: Eightx 5-8%, JeriCommerce 8-12% monthly (vendor blogs, UNVERIFIED method)
ROAS = [2.5,3.0,3.5]            # SRC: Meta median ROAS 2.7-2.96 (IQR 2.5-5.3), generic DTC not supplement
DAYS=30

def order_cm(price_tin, tins, cogs_tin, ship, adult_sig=0.0, disc=0.0):
    aov = price_tin*tins*(1-disc)
    cogs = cogs_tin*tins
    fee = aov*STRIPE_PCT+STRIPE_FIX
    refund = aov*REFUND_RATE
    cm = aov-cogs-fee-refund-ship-PICKPACK-adult_sig
    return aov, cm

def horizon_cm(cm_order, tins, ppd, churn, months):
    """expected cumulative CM per acquired customer over `months`.
    Order cadence: a tin lasts POUCHES_PER_TIN/ppd days; an order of `tins` tins lasts tins*that.
    Order 1 at t=0; reorders every cycle while subscribed; monthly survival=(1-churn)."""
    cycle = tins*POUCHES_PER_TIN/ppd
    total=0.0; t=0.0
    while t < months*DAYS:
        surv=(1-churn)**int(t//DAYS)
        total+=cm_order*surv
        t+=cycle
    return total

# ---------- 3. consumption / cadence (pure arithmetic of 20/tin) ----------
print("\nCADENCE: days per tin (20 pouches)")
for ppd in (3,4,6,8,10,12):
    print(f" {ppd}/day = {ppd*25} mg/day -> {POUCHES_PER_TIN/ppd:.1f} days/tin, {DAYS*ppd/POUCHES_PER_TIN:.2f} tins per 30 d")

# ---------- 4. model grid ----------
out=[]
hdr=["tin_price","tins_per_order","aov","cogs_tin","ship","pouches_day","mg_day","days_between_orders","cm_first_order","cm_pct_aov",
     "breakeven_cac_first_order","breakeven_cac_90d_churn8","breakeven_cac_180d_churn8","breakeven_cac_365d_churn8",
     "breakeven_cac_365d_churn5","breakeven_cac_365d_churn12","roas3_implied_cac","payback_months_at_cac_cm_x1"]
for price,cogs,ship in itertools.product(TIN_PRICES,COGS_TIN,SHIP):
  for tins in (1,2,3,5):
    for ppd in (3,4,6,8,10,12):
        aov,cm=order_cm(price,tins,cogs,ship)
        cyc=tins*POUCHES_PER_TIN/ppd
        be1=cm
        h=lambda ch,mo: horizon_cm(cm,tins,ppd,ch,mo)
        # payback: months until cumulative CM >= CAC where CAC = AOV/ROAS(3.0); churn 8%
        cac=aov/3.0
        pb=""
        for mo in range(0,37):
            if horizon_cm(cm,tins,ppd,0.08,max(mo,0.0001))>=cac: pb=mo if mo>0 else 0; break
        out.append([price,tins,round(aov,2),cogs,ship,ppd,ppd*25,round(cyc,1),round(cm,2),round(cm/aov*100,1),
            round(be1,2),round(h(.08,3),2),round(h(.08,6),2),round(h(.08,12),2),round(h(.05,12),2),round(h(.12,12),2),round(cac,2),pb])
with open(STEM+"_model.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(hdr); w.writerows(out)
print(f"\nwrote {len(out)} scenario rows")

# printed digest: mid COGS 2.50, ship 5.50 and 8.00 for 8.99
def show(price,cogs,ship):
    print(f"\n--- tin ${price}, COGS ${cogs}/tin (ASSUMPTION), ship ${ship}, pick-pack ${PICKPACK} (ASSUMPTION) ---")
    print("tins AOV   CM1   CM%  | ppd mg  days/order | BE-CAC 1st  90d@8%  180d@8%  365d@8%  365d@5%  365d@12% | CAC@ROAS3  payback(mo)")
    for r in out:
        if r[0]==price and r[3]==cogs and r[4]==ship and r[5] in (3,6,10):
            print(f"{r[1]:>4} {r[2]:>6} {r[8]:>5} {r[9]:>5}| {r[5]:>3} {r[6]:>3} {r[7]:>6}     | {r[10]:>8} {r[11]:>7} {r[12]:>8} {r[13]:>8} {r[14]:>8} {r[15]:>8} | {r[16]:>7} {str(r[17]):>6}")
for ship in SHIP: show(8.99,2.50,ship)
show(5.99,2.50,5.50); show(10.99,2.50,5.50); show(8.99,1.50,5.50); show(8.99,3.50,5.50)

# ---------- 5. wholesale ----------
print("\nWHOLESALE: brand net per tin. MSRP anchors SRC (Wip $5.99, Grinds 5.95-5.99, Bucked Up 8.99); margins: retailer & distributor shares are vendor-blog ranges (UNVERIFIED) / ASSUMPTION")
wrows=[]
for msrp in (5.99,7.99,8.99):
  for rm in (0.28,0.35,0.40):          # retailer gross margin as % of MSRP (vendor: 38-45% markup on cost = 27.5-31% margin; 37.4% inside-sales avg UNVERIFIED)
    for dm in (0.0,0.15,0.25,0.35):    # distributor margin % of its selling price (vendor 15-35%); 0 = direct to retailer
      ret_cost = msrp*(1-rm)
      brand = ret_cost*(1-dm)
      for cogs in (1.50,2.50,3.50):
        frt=0.25                         # ASSUMPTION per-tin bulk freight/pallet
        cm=brand-cogs-frt
        wrows.append([msrp,rm,dm,round(ret_cost,2),round(brand,2),cogs,round(cm,2),round(cm/brand*100,1)])
with open(STEM+"_wholesale.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["msrp","retailer_margin_pct_of_msrp","distributor_margin_pct","retailer_cost","brand_net_per_tin","cogs_tin_assump","cm_per_tin_after_0.25_freight_assump","cm_pct_of_brand_net"]); w.writerows(wrows)
print("msrp rm   dm   retail_cost brand_net | CM/tin at COGS 1.50 / 2.50 / 3.50")
for msrp in (5.99,8.99):
  for rm in (0.28,0.40):
    for dm in (0.0,0.25,0.35):
      sel=[r for r in wrows if r[0]==msrp and r[1]==rm and r[2]==dm]
      print(f"{msrp:5} {rm:.2f} {dm:.2f} {sel[0][3]:>9} {sel[0][4]:>9} | {sel[0][6]:>6} {sel[1][6]:>6} {sel[2][6]:>6}")
# fixed-cost context
print("\nFIXED: product liability $700-$4,500/yr (vendor ranges); Daily Mfg 25,000-can MOQ (brief; not re-verified) x COGS $1.50-3.50 =",
      "$%s - $%s inventory" % (format(25000*1.5,','),format(25000*3.5,',')))
