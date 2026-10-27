# Unit economics and pricing benchmarks: 25 mg caffeine pouch (US, DTC plus wholesale), as of 2026-10-27

Method: WebFetch and WebSearch only (Firecrawl out of credits), about 30 calls, all checked 2026-10-27. WebFetch answers are LLM page summaries, so exact figures need a live recheck. Files next to this note: `unit_economics.py` (model, rerunnable), `unit_economics_competitors.csv`, `unit_economics_model.csv` (432 scenario rows), `unit_economics_wholesale.csv`. Daily usage figures (4/8/12 = 100/200/300 mg; 3/6/10 for cadence) are arithmetic scenarios only, not a customer-facing goal; FDA's 400 mg/day (16 pouches at 25 mg) is the ceiling, not a target.

## 1. Competitor pricing (own-site where possible), Nectr conflict, per-100 mg

### Takeaway
The Nectr conflict is resolved by inference: nectr.energy's $29.99 to $39.99 are multipack prices (4 or 5 tins), not single tins; single tins are about $8.99 to $11.99. Per pouch the field clusters at $0.33 to $0.60 (only Roon one-time $1.00 and Ultra $1.07 are above), and the only 25 mg comparable (Grinds) is about $0.33/pouch, about $1.32 per 100 mg, the most expensive per mg in the set.

### Cited Findings
- nectr.energy lists Focus+ $39.99, Energy Jalapeno Lime $32.99, Zero $29.99; "Each tin contains 20 pouches"; no bundle prices listed, only "Subscribe & Save 35% on Every Order", "Free Shipping on Orders Over $50"; Energy "50mg of pure caffeine" — [nectr.energy](https://nectr.energy/), 2026-10-27 (fetched)
- Roon-published Nectr reviews put singles at Energy $10.99, Focus+ $11.99 (also $8.99 Fresh Mint / $11.99 others as of 2026-10-17), Zero 4-pack $7.50 per tin, 8-pack $6.75; and in another Roon table Focus+ $8.00 per tin in a 5-pack, Energy $8.25 in a 4-pack — [Roon cheapest-per-serving](https://www.takeroon.com/blog/cheapest-nootropic-pouches-per-serving-compared), [Roon ranked](https://www.takeroon.com/blog/best-caffeine-pouches-ranked) (competitor-authored; UNVERIFIED). A June 2026 Roon piece also quotes "$4.99 per 20-pouch tin" for Nectr, which fits nothing else — [search summary of Roon pages](https://www.takeroon.com/blog/nectr-pouches-review), UNVERIFIED
- Arithmetic check (mine): $39.99/5 = $8.00, $32.99/4 = $8.25, $29.99/4 = $7.50, matching Roon's per-tin figures exactly, so the site prices are very likely 4-/5-tin packs. The page text itself does not say so. The $9.99/$10.99 vs $8.99/$11.99 single-tin spread is unresolved (Roon cites different dates).
- Roon: "From $9.16/tin", 15 pouches/tin, "8 tins every 8 weeks" plan, "Free U.S. shipping on orders $35+" — [takeroon.com](https://www.takeroon.com/), 2026-10-27 (fetched). One-time $15.00 per tin, 80 mg — [Roon price page](https://www.takeroon.com/pouches/buy-caffeine-direct-not-marketplace). Another Roon page header says free shipping "$45+", so the threshold is inconsistent across Roon's own pages.
- Wild Pouches: 5-can pack $39.96 (struck $49.95, "YOU'RE SAVING 20%"), "20 pouches per can", free shipping on first order, ships 1-2 business days from US fulfillment, 60 mg or 120 mg options; no subscription % stated — [wild-pouches.com buy box](https://wild-pouches.com/pages/lp-buy-box-v9), 2026-10-27 (fetched). Which mg this price covers is not stated.
- Wip: SRP $5.99 per 10-pouch can at launch; Walmart 3-can 15-pouch 100 mg listing $21.99 (about $0.49/pouch); 200 mg 3-pack about $0.555/pouch — [Webull release](https://www.webull.com/news/12926888717902848), [search results](https://www.walmart.com/ip/17799674254). getwip.com is a domain-for-sale page ("$4,000 - $8,500"), so Wip's own site was not readable; subscription terms (Roon says 15%) UNVERIFIED — [getwip.com](https://www.getwip.com/)
- Bucked Up PWR Buck: $8.99 per 20-pouch tin, 50 mg + 63.5 mg citicoline, buy-3+ $8.09; listings show sold out — [living.fit](https://www.living.fit/products/bucked-up-pwr-buck-energy-pouches) (retailer, via search)
- Grinds: $5.95 to $5.99 per can, about 18 pouches, 20-25 mg, no subscription (bulk discount); Walmart says 15 — [Roon](https://www.takeroon.com/blog/cheapest-nootropic-pouches-per-serving-compared); grinds.com returned HTTP 503 again, so UNVERIFIED against the brand site
- NZE: $34.99 per 5 tins, 15/tin, 50 mg (about $0.47/pouch) — Roon tables, UNVERIFIED. Mojo $7.99 (50 mg) / $8.99 (100 mg), 15/tin — Roon, UNVERIFIED. Ultra Focus $16.00, 15/tin, 0 mg caffeine; its Energy page 404'd — Roon, UNVERIFIED
- Plopii: caffeine line reported at 60 mg + 50 mg L-theanine + 50 mg Alpha GPC on Amazon; no tin count/price found. Its paraxanthine Focus launched at $9.99 per 20-pouch can — [Roon review](https://www.takeroon.com/blog/plopii-focus-pouches-review), search summary, UNVERIFIED

Computed price points (script, `unit_economics_competitors.csv`): per pouch / per 100 mg: Wip 200 mg $0.56 / $0.28; Wip 100 mg $0.49 / $0.49; Mojo 100 mg $0.60 / $0.60; Wild 5-pack $0.40 / $0.67 (if 60 mg); Roon sub $0.61 / $0.76; Nectr 5-pack $0.40 / $0.80; Nectr single $0.55-0.60 / $1.10-1.20; Bucked Up $0.45 / $0.90; NZE $0.47 / $0.93; Mojo 50 mg $0.53 / $1.06; Roon one-time $1.00 / $1.25; Grinds 25 mg $0.33 / $1.32.

### Inferences
- A 25 mg product at $0.33 to $0.45/pouch is $1.32 to $1.80 per 100 mg, which is above every 100-200 mg product. A buyer who thinks per mg will see Bolt as expensive; per pouch it competes with Grinds, Nectr multipacks and Bucked Up.
- Typical tin price points to model: about $6 (Grinds/Wip SRP), about $9 (Bucked Up/Nectr single), about $11 (Nectr Energy single). Multipack per-tin price is roughly 10-30% below single.

### Gaps
- Own-site verification failed for Wip, Grinds, Mojo, Ultra, NZE, Plopii, Bucked Up (404/503/domain parked/not retrieved); most are via Roon, a competitor. Subscription % known only for Nectr (35%, own site) and Wip (15%, Roon).
- Shipping threshold known for Nectr ($50) and Roon ($35 vs $45); Wild first order free. Others unknown.

## 2. Wholesale, convenience margins, slotting

### Takeaway
No published wholesale terms or Bolt-relevant category margin were found. Only vendor-grade ranges exist: distributor 15-35%, retailer markup 38-45% on cost (about 27-31% of retail). Slotting data is a single unverified source. Wholesale is the thinnest channel on current evidence.

### Cited Findings
- Distributors typically take 15%-35%; stores then add about 38%-45% markup — [mrcheckout.net distribution FAQ](https://mrcheckout.net/convenience-store-distribution-faq/) (distributor-services vendor; UNVERIFIED). A second vendor: distributor 20-30% and a store markup at least keystone — same site's [distributors page](https://mrcheckout.net/convenience-store-distributors/), UNVERIFIED
- NACS 2021: packaged beverages 23.26% of inside gross margin contribution (22.06% in 2020), energy drinks 26.8% of that category; cigarettes 10.4%, other tobacco 6.5% — [NACS Magazine, July 2021](https://nacsmagazine.com/Issues/July-2021/hot-sellers). Contribution share, not margin percent. One site cites 37.4% average inside-sales gross margin for 2022 — [Gitnux](https://gitnux.org/c-store-industry-statistics/) (unreliable aggregator, UNVERIFIED)
- Slotting: about $100 low / $500 average / $2,000 high per SKU per store — [Smithery skill page](https://smithery.ai/skills/kishorkukreja/slotting-fees-optimization), UNVERIFIED, no underlying data
- Wip retail proof: launch SRP $5.99/10-pouch can, in 330+ Walmart Fuel Centers — [FITT Insider](https://insider.fitt.co/press-release/wip-energy-pouches-now-available-in-over-330-walmart-fuel-centers-nationwide/). Nectr has a wholesale page and store locator but no terms — [nectr.energy](https://nectr.energy/)
- 5-Hour ENERGY says average retailer profit is $1.50 per bottle (brand claim) — via search summary of a 5-Hour-sponsored piece, UNVERIFIED

Wholesale model (script, `unit_economics_wholesale.csv`; retailer margin 28-40% of MSRP and distributor 0-35% are assumptions anchored on the ranges above; COGS $1.50-3.50/tin and $0.25 freight/tin are assumptions): at MSRP $5.99, brand net per tin is $4.31 direct (28% retailer margin) falling to $2.34 via distributor at 35% with a 40% retailer margin; contribution per tin ranges from +$2.56 (COGS $1.50, direct) to -$1.41 (COGS $3.50, 40%/35%). At MSRP $8.99 contribution stays positive in nearly every cell (about +$0.30 to +$4.72) except COGS $3.50 with 40%/35% margins (-$0.24).

### Inferences
- At a $5.99 MSRP, wholesale only works if COGS is at or below about $2.50 and the distributor layer is thin or absent; at $8.99 it has room. Wholesale tin margin per unit is below DTC single-order margin but has zero CAC and no shipping/processing.

### Gaps
- No NACS/CSP pouch-category margin, no published wholesale price lists, no slotting benchmark for non-nicotine pouches, no distributor terms (Core-Mark/McLane were not reached).

## 3. Costs (COGS, MOQ, processing, shipping, age verification, insurance, chargebacks)

### Takeaway
COGS has no credible source: assumed $1.50 / $2.50 / $3.50 per 20-pouch tin as a scenario range. Processing (2.9% + $0.30) and dispute fees ($15) are published. Shipping: $5.50 per small parcel was the pre-July-2026 commercial rate; later published commercial rates bill sub-1 lb parcels at the 15.999 oz rate, so it is likely higher.

### Cited Findings
- Stripe US: 2.9% + 30c per domestic card; dispute received fee $15 (returned on won disputes only if countered); original processing fees not returned on refunds — [stripe.com/pricing](https://stripe.com/pricing), 2026-10-27 (fetched)
- Shopify Payments online: Basic 2.9% + 30c, Grow 2.7% + 30c, Advanced 2.5% + 30c; premium cards +0.6 pt; third-party gateway fee 2%/1%/0.6% — [shopify.com/pricing](https://www.shopify.com/pricing), 2026-10-27 (fetched). High-risk processor published ranges: none found (gap).
- Visa monitoring threshold reported as 1.5% from April 1, 2026 (0.9% in another source; conflicting); about $8 per disputed transaction above threshold; Mastercard excessive at 100 chargebacks/month and 1.5%-2.99% — [ChargebackStop](https://www.chargebackstop.com/blog/chargeback-ratio-whats-an-acceptable-rate-in-2026), [Chargeflow](https://www.chargeflow.io/blog/vamp-visa-acquirer-monitoring-program), vendor blogs, UNVERIFIED. No DTC returns rate benchmark for consumables found.
- USPS Ground Advantage commercial, up to 4 oz: $5.50 (zones 1-2), $5.83 (zone 5), $6.36 (zone 8) before 2026-07-12; after that, published commercial bills sub-1 lb at the 15.999 oz tier; retail Zone 1 1-4 oz $7.90 effective 2026-07-12 — [Ship.com](https://www.ship.com/post/cheapest-way-to-ship-a-package-2026), [Pitney Bowes rate guide](https://www.pitneybowes.com/content/dam/pitneybowes/us/en/postal-information/2026jan_uspsrateguide.pdf) (secondary; USPS Notice 123 not read)
- Adult signature: UPS and FedEx roughly $9-$11 per package (third-party estimate); FedEx $10.00 in 2026, up from $8.65 — [3PL Center](https://3plcenter.com/shipping-surcharges-an-in-depth-look-at-additional-fees-from-fedex-ups-and-usps/), [Lateshipment](https://www.lateshipment.com/blog/fedex-and-ups-delivery-signature/); no official UPS figure found, UNVERIFIED. Whether a signature is legally needed for caffeine: not established (earlier notes say no federal age limit).
- Product liability: most online sellers $700-$3,000/yr; supplement businesses via one broker $2,800-$4,500/yr, energy-drink-type products $3,500-$4,500; a pay-as-you-sell option from about $26/month — [Assureful](https://www.assureful.com/blog/how-much-does-product-liability-insurance-cost-data-driven-pricing-stats-you-need), [Insurance Canopy](https://www.insurancecanopy.com/?p=37679) (brokers, UNVERIFIED)
- Co-packing: Daily Manufacturing (La Verne, CA; www.dlymfg.com) is a white-label pouch maker per ZoomInfo; the 25,000-can MOQ in the brief could not be confirmed from any page found — [ZoomInfo](https://www.zoominfo.com/c/daily-manufacturing/546700659). JD Quality, Global Snus, Luna publish no MOQ or price (see sourcing.md). Only quantitative cost hint: Sourcify FOB $0.78-$2.60 (unit undefined, self-contradicting, low reliability) — [Sourcify](https://www.sourcifychina.com/caffeine-pouch-manufacturer/)
- Caffeine anhydrous: lab reagent $455/kg (Sigma) and about EUR 199/kg pharma grade — [Sigma](https://www.sigmaaldrich.com/US/en/product/sial/c7731), [ITW](https://www.itwreagents.com/italy/en/product/caffeine-anhydrous-bp-ph-eur-pure-pharma-grade/142833). Arithmetic (mine): 25 mg per pouch x 20 = 0.5 g per tin, so even at $455/kg caffeine is about $0.23 per tin; the active is a minor cost, and filler, fleece, flavor, tin and labor dominate.

### Inferences
- Tin COGS $1.50-$3.50 is scenario only. Fixed exposure at 25,000 cans would be $37.5k-$87.5k of inventory at those scenario costs, plus insurance $700-$4,500/yr.
- Shipping held flat across 1-5 tins in the model is optimistic: tin weight is unsourced and 3-5 tins likely exceed 4 oz.

### Gaps
- Real co-packer quote, tin/label/fleece costs, 3PL pick/pack fees, high-risk processing, returns benchmark, official UPS/USPS tables, age-verification app cost.

## 4. Repeat purchase and subscription retention

### Takeaway
Cadence is pure arithmetic: one 20-pouch tin lasts 20/pouches-per-day days. Vendor churn benchmarks for supplement subscriptions are 5-12% per month with a steep early drop; none is consumable-pouch-specific.

### Cited Findings (arithmetic mine, 20 pouches/tin assumed)
- 3/day = 75 mg: 6.7 days/tin, 4.5 tins per 30 d. 4/day = 100 mg: 5.0 d, 6.0 tins. 6/day = 150 mg: 3.3 d, 9.0 tins. 8/day = 200 mg: 2.5 d, 12 tins. 10/day = 250 mg: 2.0 d, 15 tins. 12/day = 300 mg: 1.7 d, 18 tins. 16/day = 400 mg (FDA benchmark, all sources combined, not pouches only) — [FDA](https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much)
- Supplement subscriptions typically churn 5-8%/month (below 5% strong, above 10% a problem) — [Eightx](https://eightx.co/blog/supplement-subscription-churn-rate-benchmark); 8-12%/month — [JeriCommerce, March 2026](https://blog.jericommerce.com/resources/supplement-vitamin-brands-retention-statistics); Recurly consumer categories 6.5%/month; Recharge 45% active at 6 months, 33% at 12; 60-70% drop between orders 1 and 3 (Eightx) — via [search summary](https://eightx.co/blog/supplement-subscription-churn-rate-benchmark). All vendor blogs; Eightx's numbers are modelled, UNVERIFIED
- Roon's own plan is 8 tins every 8 weeks (about one tin per week at 15 pouches) — [takeroon.com](https://www.takeroon.com/)

### Inferences
- A customer using fewer pouches reorders every few weeks; sales per customer scale with usage, but this is a modelling variable, not a marketing aim. Brand statements (Ultra: max 2 energy/day; Nectr: about 8 at 50 mg) show the category itself caps use.

### Gaps
- No pouch-specific retention or reorder data; no source for tins per order or typical pouches/day in real customers.

## 5. Marketing cost context

### Takeaway
No supplement-specific CAC with a clear source. Usable anchors: generic DTC Meta ROAS median about 2.7-2.96 (IQR 2.5-5.3), supplement MER 3.0-5.5 (one agency), skincare CAC $25-$80.

### Cited Findings
- Meta purchase ROAS median 2.96 (15 DTC brands, IQR 2.50-5.30); 2.70 (19 stores; CTR 1.57%, CPM about $12.30) — [Top Growth Marketing](https://topgrowthmarketing.com/dtc-ecommerce-benchmarks/meta-ads-benchmarks/)
- Supplements and wellness MER 3.0-5.5 — [Eightx channel mix](https://eightx.co/blog/marketing-channel-mix-benchmarks-meta-vs-google-vs-tiktok) (agency; via search summary)
- Skincare CPA/CAC $25-$80, strong below $45 (beauty, not supplements) — [Webtonic](https://www.webtonic.io/blog/beauty-skincare-facebook-ads-statistics)
- Meta incrementality factor 1.13x across 299 DTC brands (Q1 2026) — [CTC Research](https://commonthreadco.com/pages/q1-2026-channel-mix-benchmark)
- Whether paid platforms accept caffeine pouch ads: not checked here (see channels_and_acquisition.md).

### Inferences
- With ROAS 3 the implied first-order CAC equals AOV/3 ($3-$18 across the model's AOVs); the model's break-even CAC beyond first order depends on repeat. For a single-tin order, first-order CAC is not recoverable at any scenario (see below).

### Gaps
- Real CAC for caffeine pouches; platform ad-policy limits could raise it.

## 6. Contribution-margin model: results (run: `python3 unit_economics.py`)

### Takeaway
Under these scenarios the business only works with multi-tin orders (about $27+ AOV at $8.99/tin) or higher tin prices ($10.99); one-tin orders have negative first-order contribution at nearly every price and COGS scenario because flat shipping ($5.50) plus pick-pack ($2.50 assumed) exceed the margin. Payback is driven by AOV and reorder cadence far more than by dose per pouch.

### Cited Findings (all outputs are my computed values from the listed inputs)
Formulas: AOV = price x tins; CM1 = AOV - tins x COGS - (2.9% x AOV + $0.30) - 2% x AOV (refund/chargeback allowance, ASSUMPTION) - shipping - $2.50 pick-pack (ASSUMPTION). Reorders at 15% subscription discount (Wip, Roon-reported, UNVERIFIED). Cumulative CM with monthly survival (1-churn); order cycle = tins x 20 / pouches per day days. Break-even CAC = cumulative CM over the horizon. Payback = days until cumulative CM >= CAC.

Inputs tagged: SOURCED = price anchors ($5.99/$8.99/$10.99), Stripe/Shopify 2.9% + $0.30, shipping $5.50 or $8.00 (secondary), churn 5/8/12%, ROAS 2.5-3.5. ASSUMPTION = 20 pouches/tin, COGS $1.50/$2.50/$3.50 per tin, pick-pack $2.50, refund/chargeback 2%, $0.25/tin wholesale freight, retailer/distributor splits, CAC test points $25/$40/$60, flat shipping regardless of tin count, no adult-signature fee, no fixed costs.

Mid case ($8.99/tin, COGS $2.50, ship $5.50), 8% churn, break-even CAC (first order / 90 d / 180 d / 365 d) and payback days at CAC $25 / $40 / $60:

| Tins per order (AOV) | CM first order | Pouches/day | Days per order | BE-CAC 1st | 90 d | 180 d | 365 d | Payback days $25/$40/$60 |
|---|---|---|---|---|---|---|---|---|
| 1 ($8.99) | -$2.25 | 3 / 6 / 10 | 6.7 / 3.3 / 2.0 | -$2.25 | negative | negative | negative | never |
| 2 ($17.98) | $3.80 | 3 | 13.3 | $3.80 | $10.63 | $16.91 | $25.40 | 360 / never / never |
| 2 ($17.98) | $3.80 | 6 | 6.7 | $3.80 | $18.59 | $30.92 | $46.88 | 133 / 273 / 613 |
| 2 ($17.98) | $3.80 | 10 | 4.0 | $3.80 | $28.74 | $48.24 | $75.93 | 76 / 140 / 244 |
| 3 ($26.97) | $9.85 | 3 | 20.0 | $9.85 | $31.53 | $48.76 | $75.99 | 60 / 120 / 240 |
| 3 ($26.97) | $9.85 | 6 | 10.0 | $9.85 | $53.65 | $92.44 | $146.15 | 30 / 60 / 100 |
| 3 ($26.97) | $9.85 | 10 | 6.0 | $9.85 | $86.86 | $151.49 | $241.02 | 18 / 36 / 54 |
| 5 ($44.95) | $21.95 | 3 | 33.3 | $21.95 | $49.39 | $82.85 | $121.87 | 33 / 67 / 100 |
| 5 ($44.95) | $21.95 | 6 | 16.7 | $21.95 | $92.37 | $148.17 | $233.54 | 17 / 33 / 50 |

Sensitivities (same table, `unit_economics_model.csv`): at $5.99/tin, 1-3 tins are negative or near zero (3 tins CM1 $1.29; 5 tins $7.68, 365 d BE-CAC $29.6-$85.1 at 3-10/day); at $10.99/tin, 2 tins CM1 $7.60 and 365 d BE-CAC $85.8-$268.7. Shipping $8.00 cuts CM1 by $2.50 per order (3 tins at $8.99: $7.35). COGS $1.50 vs $3.50 moves CM1 by $1.00 per tin each way. Churn 5% vs 12% moves the 365 d break-even for 3 tins at 6/day from $146 (8%) to $169 (5%) and $122 (12%). Implied CAC at ROAS 3.0 is AOV/3 ($3.00 to $18.32 in the grid); at that CAC a 2-tin order pays back within 1 reorder in all but the $5.99 case.

### Inferences
- Binding constraint is AOV per order: below about 2-3 tins at $9-$11 per tin the shipping and handling assumption absorbs the margin. Bundles/multipacks and a shipping threshold matter more than the choice of daily-use pattern.
- Faster payback at high pouches/day is mechanical (shorter reorder cycle) and also reflects higher exposure to the 400 mg ceiling; do not treat it as a target segment. A niche choice should rest on AOV, retention and CAC, not on encouraging heavier use.
- At a 25 mg dose, price per mg is the weakest part of the offer; margin has to come from multipacks and low COGS.

### Gaps
- All COGS-dependent conclusions are scenario-only until a co-packer quote exists. Subscription take-rate, real CAC, returns/chargeback rate, 3PL fees, tin weight, ad-platform acceptance, and whether adult-signature shipping is required are unknown. Niche-specific price points and CAC (by niche) could not be sourced; the model is niche-agnostic and the niche enters only through the price, AOV and CAC inputs.
