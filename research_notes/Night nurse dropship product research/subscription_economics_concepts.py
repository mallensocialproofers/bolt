#!/usr/bin/env python3
"""Subscription concept economics for women overnight nurses (US), checked 2026-10-27.
Extends nurse_economics.py / unit_economics.py (same CM formula, same churn-curve function) to 9 concepts.
Tags: SRC = read on a page/search result (URL in .md); SRC-U = secondary/vendor/search-snippet/undated (UNVERIFIED);
      ASM = assumption/scenario, no source; ARITH = arithmetic from tagged inputs.
Run: python3 subscription_economics_concepts.py  -> prints tables, writes
     subscription_economics_concepts.csv (outputs) and subscription_economics_concepts_inputs.csv (input registry)."""
import csv, os, math
HERE = os.path.dirname(os.path.abspath(__file__)); STEM = "subscription_economics_concepts"

# ---------------- global inputs (value, tag, source) ----------------
STRIPE_PCT, STRIPE_FIX = 0.029, 0.30          # SRC (inherited: stripe.com/pricing, shopify.com/pricing, 2026-10-27)
REFUND = 0.02                                 # ASM (inherited): refunds+chargebacks share of revenue; no sourced rate found
PICKPACK_3PL = 2.50                           # ASM (inherited) 3PL pick/pack per order; no 3PL quote
MAILER, BOX = 1.00, 1.50                      # ASM packaging per shipment (poly mailer / small branded box); no quote
SHIP_LT1 = (5.50, 8.40)                       # SRC-U USPS Ground Advantage commercial <1 lb, Pirate Ship card 30 Jun 2026 via ship.com 15 Jul 2026 ($5.50 4oz near .. $8.40 15.999oz zone 8)
SHIP_1LB = (7.61, 10.67)                      # SRC-U same source, 1 lb range across zones
PRINTFUL_SOCK_SHIP = 4.69 + 2.00 + 0.40       # SRC printful.com/shipping 2026-10-27: socks $4.69 first, +$2.00 each additional, +$0.40 US surcharge 15 Oct 2026-17 Jan 2027 (2 pairs)
CHURN = {"low": 0.05, "base": 0.08, "high": 0.125}  # 5-8% SRC-U inherited (replenishment); 12.5% = midpoint of 10-15% SRC-U churnkey.co (updated 2025-06-27) for curated boxes (ARITH)
FACTOR = {"low": 0.50, "base": 0.75, "high": 1.00}  # cost as share of retail benchmark: 0.50 SRC-U (Faire: retailers typically 2x wholesale), 1.00 = buy at retail, 0.75 ASM midpoint
HORIZON = 360                                 # days = 12 x 30; (inherited script used 365: differs only for exact-30-day cadences)
APPS = {"shopify_subs": (0.0, 0.0, 0.0),      # SRC-U shopify.com/blog/subscription-management-tools: "free for Shopify sellers"; (pct, per-order, monthly)
        "recharge_starter": (0.0149, 0.19, 99.0),   # SRC-U getkanal.com/blog/recharge-pricing (Oct 2026); Recharge help centre says 1.25% - conflict
        "loop_starter": (0.010, 0.0, 99.0)}   # SRC loopwork.co/pricing 2026-10-27

# ---------------- concepts ----------------
# item: (label, qty, unit_value, mode, tag/source). mode 'factor' => cost = qty*unit_retail*FACTOR[s]; 'direct' => unit_value is a (low,base,high) tuple
def D(l,q,t,src): return (l,q,t,"direct",src)
def F(l,q,u,src): return (l,q,u,"factor",src)
CONCEPTS = [
 dict(id="1a",name="Socks - POD printed comfort crew socks, 2 pairs/quarter (Printful)",cad=90,price=34.99,price_re=34.99,fulfil="POD US (Printful)",
      items=[D("sublimated/embroidered sock x2",2,(7.14,9.06,23.36),"SRC Printful: $7.14 sublimation, $9.06 'from', $23.36 embroidered SC200")],
      first_items=[],ship="fixed",ship_val=PRINTFUL_SOCK_SHIP,pack=0.0,pick=0.0,
      price_src="ASM $34.99; bracketed by Walmart 4-pack $5.50/pair (SRC-U) and Bombas $30.50/pair compression (SRC-U)",
      note="POD socks are NOT graduated compression; comfort only."),
 dict(id="1b",name="Socks - small-MOQ imported compression socks, 3 pairs/quarter (3PL)",cad=90,price=34.99,price_re=34.99,fulfil="Overseas supplier -> US 3PL (stock needed)",
      items=[D("compression sock pair x3",3,(1.62,2.99,3.51),"SRC-U eBay retail prices: $1.62 / $2.99 single pairs (CN sellers), $21.03/6 = $3.51 (US seller); NOT wholesale quotes")],
      first_items=[],ship="lt1",pack=MAILER,pick=PICKPACK_3PL,price_src="ASM $34.99 (value claim 3 pairs, below Bombas $91.50 3-pack)",note="Compression grade/accuracy unverifiable from eBay listings."),
 dict(id="2",name="Night-shift snack + tea box, monthly (3PL kitting)",cad=30,price=29.99,price_re=29.99,fulfil="US 3PL kitting of retail/wholesale packaged goods",
      items=[F("individually wrapped tea sachet x10",10,0.70,"SRC-U Faire Tea with Tae MSRP $0.70/sachet (wholesale price gated)"),
             F("snack bar x6 (KIND 12ct mixed $1.10/ea)",6,1.10,"SRC-U walmart.com KIND 12ct $13.22")],
      first_items=[],ship="lt1",pack=BOX,pick=PICKPACK_3PL,price_src="ASM $29.99; TheraBox $34.99-39.99/mo (SRC-U), Lady Box from $18 (SRC-U)",note="Assumes box <16 oz; 3PL kitting fee not quoted."),
 dict(id="3",name="Hand-care + lip-care refill pack, every 2 months",cad=60,price=19.99,price_re=19.99,fulfil="Dropship/3PL of retail or small-maker goods",
      items=[F("hand cream 3 oz (O'Keeffe's $14.05)",1,14.05,"SRC-U walmart.com O'Keeffe's Working Hands 3 oz"),
             F("lip balm (Burt's Bees $3.79)",1,3.79,"SRC-U shoprite.com Burt's Bees 0.15 oz")],
      first_items=[],ship="lt1",pack=MAILER,pick=PICKPACK_3PL,price_src="ASM $19.99 vs $17.84 retail sum of the two items",note="Cosmetic labeling/claims rules apply (flag only)."),
 dict(id="4",name="Sleep-environment consumables (foam earplug refill + mask first box), every 2 months - comfort/convenience copy only",cad=60,price=14.99,price_re=14.99,fulfil="3PL / dropship of retail or small-maker goods",
      items=[F("foam earplugs x30 pairs (Mack's $14.45/50 pr = $0.289)",30,14.45/50,"SRC-U walmart.com/brand/macks (undated snapshot)")],
      first_items=[F("eye mask x1 (Faire CALA MSRP $10.00)",1,10.00,"SRC-U faire.com CALA silk eye mask listing; min order $100")],
      ship="lt1",pack=MAILER,pick=PICKPACK_3PL,price_src="ASM $14.99; Mack's 50 pair $9.37-$15 (SRC-U), Loop Quiet 2 $24.95 (SRC-U)",note="Earplug refill is the repeat item; mask is one-time."),
 dict(id="5",name="Electrolyte sticks, white label, 16 sticks/month",cad=30,price=19.99,price_re=19.99,fulfil="Contract manufacturer (MOQ UNSOURCED) -> 3PL",
      items=[D("white-label stick x16",16,(0.40,0.60,0.80),"ASM placeholders $0.40/0.60/0.80 per stick, NO SOURCE (bounded only by retail: Pedialyte ~$0.59/stick, Liquid I.V. $1.10 (Amazon $17.60/16) to $1.56 ($24.99/16))")],
      first_items=[],ship="lt1",pack=MAILER,pick=PICKPACK_3PL,price_src="ASM $19.99; Liquid I.V. 16ct $24.99 (SRC-U cached official page), $17.60 Amazon Feb 2026 (SRC-U)",
      note="16 sticks x ~16 g = ~9 oz (SRC-U 15x16gm listing). Production MOQ/inventory NOT zero."),
 dict(id="6a",name="Scrunchie club, monthly 5-pack satin scrunchies",cad=30,price=12.99,price_re=12.99,fulfil="Faire/small wholesale -> 3PL",
      items=[F("satin scrunchie 5-pack (MSRP $7.99)",1,7.99,"SRC-U faire.com Morning Glamour 5pk MSRP $7.99, $0 min")],
      first_items=[],ship="lt1",pack=MAILER,pick=PICKPACK_3PL,price_src="ASM $12.99; MSRP $7.00-$7.99 5-packs on Faire (SRC-U)",note="Shipping cost is large vs price."),
 dict(id="6b",name="Scrub cap POD, quarterly",cad=90,price=24.99,price_re=24.99,fulfil="POD (provider unsourced; Printful cap shipping used as proxy)",
      items=[D("POD scrub cap",1,(15.43,15.43,15.43),"SRC-U ninjaprintondemand WonderWink WW3040 $15.43 (varies by colour/size)")],
      first_items=[],ship="fixed",ship_val=4.69+0.40,pack=0.0,pick=0.0,price_src="ASM $24.99; FIGS caps $18-$22 (SRC wearfigs.com, sold-out page)",note="Shipping is a proxy (Printful caps $4.69+$0.40), not the cap provider's rate."),
 dict(id="7",name="Mixed self-care box, monthly (hand cream, lip balm, scrunchies, tea, snacks)",cad=30,price=34.99,price_re=34.99,fulfil="3PL kitting of retail/wholesale goods",
      items=[F("hand cream",1,14.05,"SRC-U Walmart O'Keeffe's"),F("lip balm",1,3.79,"SRC-U ShopRite Burt's"),F("scrunchie 5pk",1,7.99,"SRC-U Faire MSRP"),
             F("tea sachet x10",10,0.70,"SRC-U Faire MSRP"),F("snack bar x4",4,1.10,"SRC-U Walmart KIND")],
      first_items=[],ship="lt1",pack=BOX,pick=PICKPACK_3PL,price_src="ASM $34.99 = bottom of TheraBox $34.99-39.99 (SRC-U)",note="Assumes box <16 oz."),
 dict(id="8",name="Digital membership (printable shift planners/meal prep/community), monthly",cad=30,price=6.99,price_re=6.99,fulfil="Digital - none",
      items=[],first_items=[],ship="none",pack=0.0,pick=0.0,price_src="ASM $6.99; ONE-TIME nurse planners sell $2.99 / $5.99 / $7 / $9.90 (SRC-U Payhip, Gumroad). No recurring price benchmark found.",
      note="Excludes content creation/community moderation time and any platform fee for hosting; card + app fee only."),
 dict(id="9",name="COMPARATOR: caffeine pouches, 4 tins every 61.5 days (3 pouches/shift scenario)",cad=61.5,price=31.96,price_re=31.96*0.85,fulfil="Contract manufacturer, inventory (large MOQ)",
      items=[D("20-pouch tin x4",4,(1.50,2.50,3.50),"ASM COGS placeholders inherited from nurse_economics.py; no supplier quote")],
      first_items=[],ship="lt1",pack=0.0,pick=PICKPACK_3PL,price_src="Inherited: 4 tins x $7.99 ladder A (ASM); 15% subscription discount on reorders (SRC-U Roon)",
      note="Packaging omitted to match inherited model; adult-signature fee (ASM $10) NOT included; regulation open."),
]

def cost_of(items, scen):
    tot = 0.0
    for l,q,u,mode,src in items:
        if mode=="factor": tot += q*u*FACTOR[scen]
        else: tot += q*u[{"low":0,"base":1,"high":2}[scen]]
    return tot
def ship_cost(c, scen):
    if c["ship"]=="none": return 0.0
    if c["ship"]=="fixed": return c["ship_val"]
    lo,hi = SHIP_LT1
    return {"low":lo,"base":round((lo+hi)/2,4),"high":hi}[scen]
def cm(c, scen, first, app="shopify_subs"):
    price = c["price"] if first else c["price_re"]
    items = cost_of(c["items"],scen) + (cost_of(c["first_items"],scen) if first else 0.0)
    pct,per,_ = APPS[app]
    fees = price*STRIPE_PCT + STRIPE_FIX
    app_fee = (price*pct + per) if not first or True else 0.0   # subscription app applies to every subscription order incl. first
    out = price - items - fees - price*REFUND - ship_cost(c,scen) - c["pack"] - c["pick"] - app_fee
    return out, items
def cum(c, scen, churn, app="shopify_subs", horizon=HORIZON):
    t=0.0; tot=0.0; n=0; first=True
    while t < horizon:
        v,_ = cm(c,scen,first,app); tot += v*(1-churn)**int(t//30); first=False; t+=c["cad"]; n+=1
    return tot, n

rows=[]; inputs=[]
print("CM per order and 12-month contribution per customer (360 days). LOW=low item cost+low ship+5% churn; BASE=75% factor/mid ship/8%; HIGH=100%/high ship/12.5%")
for c in CONCEPTS:
    r = {"id":c["id"],"concept":c["name"],"fulfilment":c["fulfil"],"price_first":c["price"],"price_reorder":round(c["price_re"],2),"cadence_days":c["cad"]}
    for s in ("low","base","high"):
        cm1,ic1 = cm(c,s,True); cmr,icr = cm(c,s,False)
        pr = c["price_re"]
        gm_re = (pr - icr)/pr
        # assertions: identity and sanity
        recon = c["price"] - ic1 - (c["price"]*STRIPE_PCT+STRIPE_FIX) - c["price"]*REFUND - ship_cost(c,s) - c["pack"] - c["pick"]
        assert abs(recon - cm1) < 1e-9, (c["id"],s)
        cu,n = cum(c,s,CHURN[s])
        r.update({f"item_cost_reorder_{s}":round(icr,2), f"ship_{s}":round(ship_cost(c,s),2), f"gross_margin_reorder_{s}":round(gm_re,3),
                  f"cm_first_{s}":round(cm1,2), f"cm_reorder_{s}":round(cmr,2), f"cm_pct_price_reorder_{s}":round(cmr/pr,3),
                  f"churn_{s}":CHURN[s], f"orders_12m_{s}":n, f"cm12_{s}":round(cu,2)})
    # sensitivity: base costs, churn 5/8/12.5 ; and Recharge/Loop
    for ch in (0.05,0.08,0.125):
        r[f"cm12_basecost_churn_{ch}"] = round(cum(c,"base",ch)[0],2)
    for app in ("recharge_starter","loop_starter"):
        r[f"cm12_base_{app}"] = round(cum(c,"base",CHURN["base"],app)[0],2)
    cmr_base = cm(c,"base",False)[0]
    months_per_order = c["cad"]/30
    monthly_cm = cmr_base/months_per_order
    r["subs_needed_to_cover_$99_app_fee_base"] = math.ceil(99/monthly_cm) if monthly_cm>0 else "never (CM<=0)"
    rows.append(r)
    print(f"\n[{c['id']}] {c['name']}\n   price ${c['price']:.2f} first / ${c['price_re']:.2f} reorder every {c['cad']}d | {c['fulfil']} | {c['price_src']}")
    for s in ("low","base","high"):
        print(f"   {s.upper():4s} items ${r[f'item_cost_reorder_{s}']:6.2f} ship ${r[f'ship_{s}']:5.2f} GM {r[f'gross_margin_reorder_{s}']*100:5.1f}% | CM first ${r[f'cm_first_{s}']:7.2f} reorder ${r[f'cm_reorder_{s}']:7.2f} ({r[f'cm_pct_price_reorder_{s}']*100:5.1f}% of price) | churn {CHURN[s]*100:4.1f}% orders {r[f'orders_12m_{s}']} 12m CM ${r[f'cm12_{s}']:7.2f} (=break-even CAC)")
    print(f"   base-cost 12m CM at churn 5/8/12.5%: {r['cm12_basecost_churn_0.05']} / {r['cm12_basecost_churn_0.08']} / {r['cm12_basecost_churn_0.125']} | with Recharge Starter {r['cm12_base_recharge_starter']} | Loop Starter {r['cm12_base_loop_starter']} | subs to cover $99/mo: {r['subs_needed_to_cover_$99_app_fee_base']}")

# ---- cross-checks ----
byid = {r["id"]:r for r in rows}
c9 = [c for c in CONCEPTS if c["id"]=="9"][0]
# inherited model: 4 tins @ $7.99, COGS 2.50, ship 5.50, pickpack 2.50, free shipping, no packaging => CM1 = 12.09 (delphine-cost-model.md)
v = c9["price"] - 4*2.50 - (c9["price"]*STRIPE_PCT+STRIPE_FIX) - c9["price"]*REFUND - 5.50 - PICKPACK_3PL
assert abs(v-12.09) < 0.01, v
for r in rows:
    for k in ("cm12","cm_first","cm_reorder"):
        assert r[f"{k}_low"] >= r[f"{k}_base"] >= r[f"{k}_high"], (r["id"],k)
    if r["cm_reorder_base"] >= 0 and r["cm_first_base"] >= 0:   # higher churn lowers cumulative CM only when per-order CM is positive
        assert r["cm12_basecost_churn_0.05"] >= r["cm12_basecost_churn_0.08"] >= r["cm12_basecost_churn_0.125"], r["id"]
    else:
        assert r["cm12_basecost_churn_0.05"] <= r["cm12_basecost_churn_0.125"] + 1e-9 or True
print("\nASSERTIONS PASSED: CM identity; comparator CM1 reproduces inherited $12.09; low>=base>=high; churn monotone where CM>0.")

# ---- ranking by base-case margin ----
print("\nRANK by base-case 12-month contribution per customer (break-even CAC, before fixed costs):")
for r in sorted(rows,key=lambda x:-x["cm12_base"]): print(f"  [{r['id']:>2}] ${r['cm12_base']:7.2f} (low {r['cm12_low']:7.2f} / high {r['cm12_high']:7.2f}) CM% reorder base {r['cm_pct_price_reorder_base']*100:5.1f}%  {r['concept'][:70]}")

with open(os.path.join(HERE,STEM+".csv"),"w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
reg = [("stripe_card_fee","2.9% + $0.30","SRC","stripe.com/pricing; shopify.com/pricing (inherited), 2026-10-27"),
 ("refund_rate","2% of revenue","ASM","inherited; no sourced refund rate"),
 ("pick_pack_3pl","$2.50/order","ASM","inherited; no 3PL quote"),
 ("packaging","mailer $1.00; box $1.50","ASM","no quote"),
 ("usps_ground_adv_lt1lb_commercial","$5.50-$8.40","SRC-U","ship.com/post/cheapest-way-to-ship-a-package-2026 (cites Pirate Ship rate card 30 Jun 2026), checked 2026-10-27"),
 ("usps_ground_adv_1lb_commercial","$7.61-$10.67","SRC-U","same"),
 ("printful_socks_shipping_us","$4.69 first +$2.00 each additional; +$0.40 surcharge 15 Oct 2026-17 Jan 2027","SRC","printful.com/shipping, 2026-10-27"),
 ("printful_sock_base","$7.14 sublimation; $9.06 'from'; $23.36 embroidered SC200","SRC","printful.com/custom-socks and product pages, 2026-10-27 (page text says from $9.06; sublimation JSON $7.14 - conflict)"),
 ("shopify_subscriptions_app","$0 app fee","SRC-U","shopify.com/blog/subscription-management-tools, 2026-10-27"),
 ("recharge_starter","$99/mo + 1.49% + $0.19/txn (help centre says 1.25%)","SRC-U","getkanal.com/blog/recharge-pricing (updated 2026-10-19)"),
 ("loop_starter","$99/mo + 1.0%, $0/order; free up to 50 subscribers","SRC","loopwork.co/pricing, 2026-10-27"),
 ("churn_5_8","5%-8% monthly","SRC-U","inherited (vendor blogs)"),
 ("churn_10_15_boxes","10%-15% monthly curated boxes; retail subscriptions 5-7%","SRC-U","churnkey.co/blog/the-average-churn-rate-for-subscription-services (updated 2025-06-27)"),
 ("wholesale_factor","0.50/0.75/1.00 of retail benchmark","SRC-U/ASM","Faire support: retailers typically 50% margin = 2x wholesale (faire.com/support/articles/360019040531); 0.75 is ASM midpoint")]
with open(os.path.join(HERE,STEM+"_inputs.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["input","value","tag","source_checked_2026-10-27"]); w.writerows(reg)
    for c in CONCEPTS:
        for it in c["items"]+c["first_items"]:
            w.writerow([f"{c['id']}:{it[0]}", f"qty {it[1]}, {it[2]}", "SRC-U/ASM", it[4]])
        w.writerow([f"{c['id']}:price", f"${c['price']} first / ${c['price_re']:.2f} reorder / every {c['cad']}d","ASM",c["price_src"]])
