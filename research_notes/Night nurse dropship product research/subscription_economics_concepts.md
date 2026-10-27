# Subscription economics and concept shortlist for women overnight nurses (US, zero/low-inventory fulfilment), as of 2026-10-27

Method. Reused the inherited contribution formula and churn curve from `/home/user/bolt/research_notes/Overnight women nurses niche research/nurse_economics.py` and `/home/user/bolt/work/finance/2026-10-27-delphine-cost-model.py` (CM = price - item cost - (2.9% x price + $0.30) - 2% refunds - shipping - packaging - pick/pack - app fee; cumulative CM = sum over orders at t = 0, c, 2c... of CM x (1-churn)^floor(t/30)). The new script `subscription_economics_concepts.py` (same folder; run `python3 subscription_economics_concepts.py`) prints every table, asserts the identities and writes `subscription_economics_concepts.csv` (outputs) and `subscription_economics_concepts_inputs.csv` (input registry with tags). Tags: SRC = read on the page; SRC-U = UNVERIFIED (secondary, vendor-authored, search-result snippet, undated or cached); ASM = assumption with no source; ARITH = arithmetic on tagged inputs. Firecrawl was out of credits; WebSearch and WebFetch only. WebSearch answers are summaries and WebFetch answers are model summaries of pages, so every figure below that came from a search snippet is SRC-U. Checked 2026-10-27 unless stated. The age policy is not recorded in `work/decisions.md` (21+ assumed for the pouch comparator). Nothing here is a legal conclusion; items for counsel are under "For a professional". Per CLAUDE.md, no spend on inventory, branding or ads is recommended before the compliance gate is cleared.

Scope limits that matter: (1) I could NOT retrieve any true wholesale or dropship price from CJ (page redirected to a bot validation), AliExpress, Spocket or Faire (wholesale prices are login-gated; one product page returned 403). Supplier costs below are therefore retail-benchmark-derived (cost = 50%/75%/100% of a retail benchmark) or placeholders, and are labelled as such. (2) Subscription prices are ASM price points chosen inside sourced retail bands; no willingness-to-pay data was found. (3) Weights are ASM (boxes kept under 16 oz); the USPS 2 lb rate was not found.

## 1. What do the common cost inputs look like (shipping, payment, subscription app, churn, packaging)?

### Takeaway
Payment is 2.9% + $0.30 (inherited); USPS Ground Advantage commercial for a sub-1-lb parcel is $5.50 to $8.40 and $7.61 to $10.67 at 1 lb (Pirate Ship card, 30 Jun 2026, via a Ship.com article); the Shopify Subscriptions app is reported free while Recharge Starter is $99/month + 1.49% + $0.19 per order and Loop Starter is $99/month + 1.0%. Published monthly churn for curated boxes is 10-15%, for replenishment/retail subscriptions 5-8%, so the model runs 5% / 8% / 12.5% scenarios.

### Cited Findings
- Stripe/Shopify card fee 2.9% + $0.30 — inherited, [Stripe pricing](https://stripe.com/pricing) and [Shopify pricing](https://www.shopify.com/pricing), as recorded in `unit_economics.md`; not re-fetched in this run (2026-10-27)
- USPS Ground Advantage commercial (discounted) prices from a June 30, 2026 Pirate Ship rate sheet: under 1 lb $5.50 (4 oz, near zone) to $8.40 (15.999 oz, zone 8); 1 lb $7.61 to $10.67; 5 lb $9.70 to $19.19; retail starting price $7.90; 2 lb not given — [Ship.com, July 15 2026](https://www.ship.com/post/cheapest-way-to-ship-a-package-2026), fetched 2026-10-27, SRC-U (third-party reseller article). Another search summary puts retail 1 lb zone 5 at $10.95 and commercial $8.74 under the April 26, 2026 list, plus an 8% fuel surcharge April 26, 2026 to Jan 17, 2027 — [Shippo](https://goshippo.com/blog/usps-parcel-select-ground-cost-sizes-and-how-it-works), search summary only, SRC-U; the two sources are not fully consistent (the fuel surcharge may not be in the $5.50-$10.67 range)
- Printful US shipping: socks, embroidered aprons, hand towels $4.69 first item + $2.00 each additional; hats/beanies $4.69 + $2.00; US production 2-5 business days then 3-4 business days standard (1-3 express); a $0.40 surcharge applies to US orders from Oct 15, 2026 to Jan 17, 2027 — [Printful shipping](https://www.printful.com/shipping), fetched 2026-10-27 (SRC)
- Shopify Subscriptions app "is free for Shopify sellers" — [Shopify blog](https://www.shopify.com/blog/subscription-management-tools), fetched 2026-10-27, SRC-U (the Shopify Help Center page fetched did not state fees; app-listing page not opened). Same article: Bold $24.99/month + 2%; Recharge "starts at $99 per month, 1.49% plus 19 cents"
- Recharge: Starter $99/month + 1.49% + $0.19 per transaction; Plus $499 + 1.34% + $0.19; a $25/month plan waives the per-order fee for the first 50 subscribers; the Help Center billing article says 1.25% for Starter; percentage is charged on shipping, taxes and refunded orders — [Kanal, updated 2026-10-19](https://getkanal.com/blog/recharge-pricing), fetched 2026-10-27, SRC-U (third party; Recharge's own pricing page returned 404). A search summary also notes a 1.25% vs 1.49% conflict across sites
- Loop: Starter $99/month, 1.0% transaction fee, $0 per order; Pro $399, 0.75%; free plan up to 50 active subscribers; 14-day trial — [Loop pricing](https://loopwork.co/pricing), fetched 2026-10-27 (vendor page; SRC for the vendor's own list price)
- Churn: curated/e-commerce subscription boxes 10-15% monthly; retail subscriptions 5-7%; the page names no underlying study (published 2024-10-02, updated 2025-06-27) — [Churnkey](https://churnkey.co/blog/the-average-churn-rate-for-subscription-services/), fetched 2026-10-27, SRC-U. A search summary of other vendor blogs gives replenishment <4% or 5-8%, beauty boxes 8-14% — [Ringly](https://www.ringly.io/blog/subscription-box-statistics-2026), search summary, SRC-U. The inherited 5-8% range is from vendor blogs (`unit_economics.md`)
- Faire's own support article says retailers typically look for a 50% margin, "2x the wholesale price"; Faire pages call 2x a starting point, not a fixed rule — [Faire pricing policy](https://www.faire.com/support/articles/360019040531), search summary 2026-10-27, SRC-U. Third-party blogs say Faire takes up to 25% on a new retailer's first order and 15% on reorders ([Eightx](https://eightx.co/blog/faire-wholesale-take-rate-margin-impact), SRC-U) — this affects what small makers charge, not your cost directly

### Inferences
- Churn model: 5% (low), 8% (base, inherited), 12.5% (high; midpoint of the 10-15% box range, ARITH). Quarterly boxes are modelled with the same per-30-day survival, so a 90-day cadence reaches order 2 with (1-churn)^3 survival (ARITH on the churn assumption, not an observed quarterly rate).
- Supplier cost model for Faire-type goods: cost = retail benchmark x 0.50 (low, SRC-U Faire 2x rule), x 0.75 (base, ASM midpoint), x 1.00 (high, buying at retail). This is a proxy because wholesale prices were gated.
- Shipping for sub-1-lb boxes: low $5.50, high $8.40, base $6.95 (mean, ARITH). Packaging $1.00 mailer / $1.50 box and pick/pack $2.50 are ASM (pick/pack inherited, no 3PL quote). Refunds 2% ASM.
- The Shopify Subscriptions app is the base case ($0); Recharge and Loop Starter are shown as sensitivities with the $99 fixed fee converted to "subscribers needed to cover it".

### Gaps
- No 3PL quote (kitting, receiving, storage), no sourced refund/return rate for any of these categories, no 2 lb USPS rate, no Shopify Subscriptions fee from Shopify's own page, and no confirmation whether Shopify Subscriptions has product/category restrictions.

## 2. What do comparable products sell for, and what could supply cost? (per concept)

### Takeaway
Retail benchmarks exist for every concept, but sourced no-MOQ supplier costs exist only for POD socks (Printful) and a few Faire MSRPs; imported compression socks, snacks, white-label electrolytes and private-label hand care have no sourced wholesale price, so those costs are benchmark-derived or placeholders.

### Cited Findings
Socks
- Bombas women's everyday compression knee-high 3-pack (15-20 mmHg) $91.50 ($30.50/pair); merino 3-pack $121.50; travel 3-pack $106.50; performance 20-30 mmHg 3-pack $108; ankle 3-pack $60-$61.50 — [Bombas product page](https://bombas.com/products/womens-compression-calf-sock-3-pack) and [collection](https://bombas.com/collections/womens-compression-socks), search snippets 2026-10-27 (direct fetch returned 429), SRC-U on current price. Bombas runs a one-purchased-one-donated policy per a nurse guide ([AJC](https://ajc.com/pulse/nurses-recommend-these-compression-socks-heres-why/XTXZGFA3DVG2HIO6UTSSWIOB4A), snippet, SRC-U)
- Sock Fancy (monthly sock subscription): $9 a month + $2 shipping for one pair per a My Subscription Addiction page updated Nov 2023; older listings $11 one pair, $19 two, $57 six — [MSA](https://www.mysubscriptionaddiction.com/b/sock-fancy), 2026-10-27, SRC-U (site redirects to custom.sockfancy.com; current price not confirmed)
- eBay US-listed nurse/compression socks: one pair $10.44, 3-pack $16.08, 6 pairs $21.03 (US seller, Oregon, since ended), Chinese-seller listings $1.62 and $2.99 per pair; Nurse Mates 3-pack $39.95; Walmart 4-pack 20-30 mmHg $21.99 — [eBay 6-pair](https://www.ebay.de/itm/406168057260), [Walmart](https://www.walmart.com/ip/6053367747), search snippets 2026-10-27, SRC-U (retail prices, not wholesale)
- Printful custom socks "from $9.06 to $24.94", no minimum ("1 pair or 1,000"), 25+ pair discount up to 26%; embroidered SOCCO SC200 $23.36; sublimation sock $7.14 in page data (conflicts with the $9.06 'from' figure); fulfilment centres and production time not stated on the sock page — [Printful socks](https://www.printful.com/custom-socks), fetched 2026-10-27 (SRC). POD socks are not graduated-compression garments (my reading of the product types listed)
- CJ Dropshipping: a CJ blog says suppliers offer 15-20 and 20-30 mmHg; no compression sock price retrieved; the CJ list page redirected to a validation page — [CJ medical supplies blog](https://cjdropshipping.com/blogs/selling-strategies/Dropshipping-Medical-Supplies), search snippet, SRC-U; AliExpress/Alibaba listings not retrieved
Snack and tea
- Tea with Tae individually wrapped sachets, set of 50, MSRP $0.70 each, wholesale price gated, min order varies by brand ($75-$170 seen on other tea brands) — [Faire listing](https://faire.com/product/p_xv8z2y8q7e), search summary 2026-10-27, SRC-U
- KIND bars 12-count mixed $13.22 ($1.10 each) at Walmart — [Walmart](https://www.walmart.com/c/ep/kind-snack-bars), snippet, undated, SRC-U
- Comparable curated boxes: TheraBox $34.99-$39.99/month, Lady Box from $18, Bath Bevy about $39.56-$43.21, Hopebox from $58.99 plus $9.93 shipping; roundup says $15-$60 per month — [My Subscription Addiction self-care roundup](https://www.mysubscriptionaddiction.com/self-care-subscription-boxes?msa=hp) and [TheraBox](https://mytherabox.com/pages/therabox-subscription-box-lp1b), snippets, SRC-U
Hand and lip care
- O'Keeffe's Working Hands 3 oz $14.05 at Walmart; Burt's Bees 0.15 oz lip balm $3.58-$3.79 — [Walmart O'Keeffe's](https://www.walmart.com/brand/okeeffes/10049657), [ShopRite lip balms](https://shoprite.com/sm/pickup/rsid/594/categories/skin-care/lip-balms-treatments-id-519597), snippets, SRC-U
- Faire: mini scented hand cream from IngrossoBeauty shows $0 minimum and a $3.34 figure (the snippet labels it both WSP and MSRP, so it is ambiguous); lip balm minimums $50-$150 (Fabula Nebulae $75, ANA Soaps $50, Victoria's Lavender $100); Farmersbody direct private-label lip balm $150 minimum on every order — [Faire hand cream](https://www.faire.com/product/p_rwbb95f9fh) (direct fetch 403), [Farmersbody](https://farmersbody.com/pages/private-label-lip-balm), SRC-U
Sleep environment (comfort/convenience copy only)
- Mack's foam earplugs 50 pair $9.37-$15 (Walmart/eBay/72hours.ca, undated snapshots); Loop Quiet 2 $24.95 (Tom's Guide says Amazon sale $15.49) — [Walmart Mack's brand page](https://walmart.com/brand/macks/10023669), [Loop](https://us.loopearplugs.com/products/quiet), [Tom's Guide](https://www.tomsguide.com/wellness/sleep-tech/loop-quiet-2-earplugs-review), SRC-U
- Faire silk eye masks: MSRP $6-$30 with minimums $100-$250 (CALA $10 MSRP/$100 min; Moonlit $18/$150); a bulk promo supplier lists a personalised sleep mask at $1.65-$1.82 each, MOQ 100 — [Faire CALA](https://www.faire.com/product/p_w942jzjhhv), [Promotional Product Inc](https://promotionalproductinc.com/sleep-eye-mask--1), snippets, SRC-U
Electrolyte
- Liquid I.V. Hydration Multiplier 16 sticks $24.99 on its own product pages (cached 400-1,900 days, so possibly stale); $17.60 on Amazon (Slickdeals, Feb 2026); 15-stick box $21.29-$23.59; Pedialyte about $0.59 per stick; sticks are 16 g each ("15x16gm" listing) — [Liquid I.V.](https://www.liquid-iv.com/products/lemon-lime-hydration-multiplier), [Slickdeals](https://slickdeals.net/f/19191832-17-60-liquid-i-v-hydration-multiplier-lemon-lime-electrolyte-powder-drink-mix-1-pack-16-servings), SRC-U
- Private-label electrolyte MOQ/cost per stick: nothing found (see Gaps)
Fashion and scrubs
- Satin scrunchie 5-packs on Faire: Morning Glamour MSRP $7.99, $0 minimum; Gifty set MSRP $7.00, $50 minimum; KITSCH sets $150 minimum — [Faire search](https://www.faire.com/product/p_q4vcsjp825), snippet, SRC-U
- FIGS scrub caps: Scrub Cap With Buttonholes $22.00; Modern Expandable $18.00 (page showed them sold out) — [FIGS](https://www.wearfigs.com/collections/scrub-caps), fetched 2026-10-27 (SRC). Cherokee scrub hat on Walmart: no price retrieved — [Walmart](https://www.walmart.com/ip/136038763)
- POD scrub caps: WonderWink scrub cap via a POD shop $15.43 ("varies by colour or size"); Merchize lists an all-over-print scrub cap (price not retrieved) — [Ninja POD](https://ninjaprintondemand.com/products/wonderwink-ww3040), [Merchize](https://merchize.com/product/all-over-print-scrub-cap/), snippets, SRC-U
Digital
- Nurse shift planners are sold one-time at $2.99 (10 pages), $5.99 (six templates + 55 stickers), $7 (Gumroad starter kit), $9.90 (11 templates); no recurring-price benchmark found — [Payhip](https://payhip.com/b/fzNM1), [Gumroad](https://fowziee.gumroad.com/l/clinical-shift-starter-kit), snippets 2026-10-27, SRC-U

### Inferences
- Reselling known retail brands (hand cream, lip balm, snacks, Mack's earplugs) means the supplier price is near retail unless a wholesale account exists, which squeezes margin before $5.50-$8.40 shipping; the model's high-cost case (100% of retail) is realistic for a no-minimum, no-wholesale-account start.
- Imported compression socks: the eBay retail prices ($1.62-$3.51 per pair) cap what a landed cost plausibly is, but they say nothing about compression accuracy, sizing, lead time (overseas shipping times were not retrieved) or quality.
- Printful's sock page offers no graduated compression and the cheapest POD sock ($7.14-$9.06) plus $4.69/$2.00 shipping is about $25 of cost for two pairs, which sits close to a $34.99 price.

### Gaps
- No wholesale quote from CJ, AliExpress, Alibaba, Spocket or Faire for any item; no shipping-time data from CJ/AliExpress; no private-label electrolyte, hand-cream or tea MOQs; no Cherokee scrub-cap price; no current Bombas price confirmed on the live page (429); Sock Fancy's current price unconfirmed; Manta/Hatch sleep-mask official prices not retrieved.

## 3. What do the unit economics look like, and how do the concepts rank?

### Takeaway
At ASM price points, only four physical or digital concepts have positive base-case contribution above about $20 per customer over 12 months: the snack + tea box ($55.89, but $14.19 in the high-cost case), imported compression socks ($38.73, range $25.51 to $61.60), the digital membership ($50.17, range $40.55-$58.35, with no demand evidence) and POD comfort socks ($22.19, but -$50.41 if the supplier is the $23.36 embroidered sock). Hand/lip care, sleep consumables, electrolytes, scrunchies and the mixed self-care box lose money or break even at base cost because $5.50-$8.40 parcel shipping plus $2.50 pick/pack consumes most of a $13-$20 price. The caffeine pouch comparator earns $29.61 over 12 months at base inputs, which is similar to the best physical concepts but carries the unresolved compliance gate and large inventory.

### Cited Findings
All numbers below are model outputs (ARITH) from `subscription_economics_concepts.py` using the inputs in Sections 1-2; SRC-U/ASM tags apply to the inputs, not to the outputs. Orders in 12 months (360 days): 4 for 90-day cadence, 6 for 60-day, 12 for 30-day, 6 for 61.5-day.

Per-order economics, base case (item cost at 75% of retail benchmark or the mid placeholder; shipping $6.95; Shopify Subscriptions app $0):

| ID | Concept (cadence) | Price first / reorder | Fulfilment | Item cost | Ship | Gross margin (price - items) | CM / order | CM % of price |
|---|---|---|---|---|---|---|---|---|
| 1a | POD printed comfort socks, 2 pairs (90 d) | $34.99 | POD US, Printful | $18.12 | $7.09 (Printful) | 48.2% | $7.77 | 22.2% |
| 1b | Imported compression socks, 3 pairs (90 d) | $34.99 | Overseas -> US 3PL | $8.97 | $6.95 | 74.4% | $13.56 | 38.7% |
| 2 | Snack + tea box (30 d) | $29.99 | US 3PL kitting | $10.20 | $6.95 | 66.0% | $7.07 | 23.6% |
| 3 | Hand + lip pack (60 d) | $19.99 | 3PL / dropship | $13.38 | $6.95 | 33.1% | -$5.12 | -25.6% |
| 4 | Earplug refill + first-box mask (60 d) | $14.99 | 3PL / dropship | $6.50 (+$7.50 mask, first box) | $6.95 | 56.6% | reorder -$3.00; first -$10.50 | -20.0% |
| 5 | White-label electrolyte, 16 sticks (30 d) | $19.99 | Contract mfr + 3PL | $9.60 (ASM placeholder) | $6.95 | 52.0% | -$1.34 | -6.7% |
| 6a | Scrunchie 5-pack club (30 d) | $12.99 | Wholesale -> 3PL | $5.99 | $6.95 | 53.9% | -$4.39 | -33.8% |
| 6b | POD scrub cap (90 d) | $24.99 | POD (shipping proxy) | $15.43 | $5.09 (proxy) | 38.3% | $2.95 | 11.8% |
| 7 | Mixed self-care box (30 d) | $34.99 | 3PL kitting | $27.92 | $6.95 | 20.2% | -$5.90 | -16.9% |
| 8 | Digital membership (30 d) | $6.99 | none | $0 | $0 | 100% | $6.35 | 90.8% |
| 9 | Caffeine pouches comparator, 4 tins (61.5 d) | $31.96 / $27.17 | Contract mfr, inventory | $10.00 (ASM) | $6.95 | 63.2% | first $10.64 / reorder $6.08 | 22.4% |

Formula per row (example 1b base): CM = 34.99 - 8.97 - (34.99 x 0.029 + 0.30) - 34.99 x 0.02 - 6.95 - 1.00 packaging - 2.50 pick/pack = $13.56. Comparator check: with inherited inputs (COGS $2.50, shipping $5.50, free shipping, no packaging) the script reproduces the inherited first-order CM of $12.09 (asserted).

12-month contribution per customer (= break-even CAC before fixed costs). LOW = low item cost + low ship + 5% churn; BASE = base cost/ship + 8%; HIGH = 100%-of-retail or high placeholder + $8.40 ship + 12.5% churn. Sensitivity columns hold base costs and change churn or the subscription app.

| ID | Low | Base | High | Base cost, churn 5% / 8% / 12.5% | Base with Recharge Starter / Loop Starter | Subscribers to cover Recharge's $99/mo (base) |
|---|---|---|---|---|---|---|
| 2 Snack + tea | $109.58 | $55.89 | $14.19 | $65.00 / $55.89 / $45.17 | $50.85 / $53.52 | 15 |
| 8 Digital | $58.35 | $50.17 | $40.55 | $58.35 / $50.17 / $40.55 | $47.85 / $49.62 | 16 |
| 1b Imported compression socks | $61.60 | $38.73 | $25.51 | $43.69 / $38.73 / $32.80 | $36.70 / $37.73 | 22 |
| 9 Caffeine pouch comparator | $58.94 | $29.61 | $6.72 | $33.24 / $29.61 / $25.29 | $27.09 / $28.44 | 34 |
| 1a POD comfort socks | $37.40 | $22.19 | -$50.41 | $25.03 / $22.19 / $18.79 | $20.16 / $21.19 | 39 |
| 6b POD scrub cap | $9.49 | $8.42 | $7.13 | $9.49 / $8.42 / $7.13 | $6.81 / $7.70 | 101 |
| 5 Electrolyte | $30.43 | -$10.59 | -$38.26 | negative | negative | never |
| 4 Sleep consumables | -$2.07 | -$19.84 | -$32.54 | negative | negative | never |
| 3 Hand + lip | $3.73 | -$21.08 | -$37.58 | negative | negative | never |
| 6a Scrunchie club | -$8.66 | -$34.69 | -$50.06 | negative | negative | never |
| 7 Mixed self-care box | $44.68 | -$46.61 | -$106.40 | negative | negative | never |

Against the inherited CAC thresholds ($25 hard ceiling, $40 fail line in the Delphine model; Meta healthcare ROAS benchmarks in `economics_offer_positioning.md`, SRC-U): base-case 12-month contribution clears $25 for 2, 8, 1b and 9, clears $40 for 2 and 8 only, and clears $60 for none. The high-cost cases of 1b and 2 clear $25 only for 1b.

Qualitative ranking (judgment, INFERENCE; regulation uses general knowledge and is UNVERIFIED in this run, another researcher covers regulation in detail). Scores 1 (worst) to 5 (best):

| ID | Margin (base CM%, 12-m CM) | Repeat-purchase fit | Regulatory burden (5 = light) | Zero-inventory ease | Risk (5 = lower) | Comment |
|---|---|---|---|---|---|---|
| 1b Imported compression socks | 4 | 5 (wear-out replacement every 3-6 months is the owner's stated cadence; no repeat-rate data) | 3 (comfort copy only; "compression/circulation/swelling/DVT" language reads as medical; flagged) | 3 (small stock, overseas lead time unknown) | 3 (quality/sizing, cost unverified) | Best margin of physical concepts; costs unsourced |
| 1a POD comfort socks | 3 | 3 | 4 | 5 | 4 | True zero inventory but thin and one bad supplier choice flips it negative |
| 2 Snack + tea box | 3 | 4 (consumed monthly) | 3 (food labeling/allergens/shelf life; kitting of finished goods lighter than manufacturing) | 3 (3PL kitting, small MOQs per Faire brand) | 2 (churn 10-15% typical, shipping heavy, CM% 23.6) | Highest base 12-m CM, widest range ($14-$110) |
| 8 Digital membership | 5 | 3 (no recurring-price evidence; one-time planners $3-$10) | 5 | 5 | 2 (demand unproven; ongoing content labour not costed) | Cheapest test of the nurse audience's willingness to pay |
| 6b POD scrub cap | 2 | 2 | 4 | 5 | 3 | CM $2.95 per order, never covers app fees |
| 5 Electrolyte | 2 | 5 | 2 (supplement/food rules, label and claims; MOQ) | 1 | 2 | Margin depends on an unsourced stick cost |
| 3 Hand + lip | 1 | 4 | 2 (cosmetic rules; lip balm with SPF is a drug; claims) | 3 | 3 | Negative at base because retail goods cost near retail |
| 4 Sleep consumables | 1 | 3 | 3 (no sleep claims per Rule 4; earplug NRR labeling) | 3 | 3 | Price too low for shipping |
| 6a Scrunchie club | 1 | 2 | 5 | 3 | 3 | Shipping > item cost |
| 7 Mixed self-care box | 1 | 3 | 3 | 2 | 2 | Cost of five items at 75-100% of retail exceeds price margin |
| 9 Caffeine pouches (comparator) | 3 | 4 | 1 (gate not cleared; state laws, platforms, payments unresearched) | 1 (large MOQ in the inherited model) | 1 | Not eligible to spend against until the compliance gate clears |

### Inferences
- Structural result: with $5.50-$8.40 postage and $2.50 pick/pack, a physical subscription needs roughly $30+ per shipment (or a 90-day cadence) to leave a positive contribution; every concept priced at $12.99-$19.99 failed at base. This is arithmetic on the shipping and fee inputs, not a market finding. Raising price is limited by the sourced bands ($34.99-$39.99 for TheraBox; Sock Fancy at about $11 per month).
- Quarterly cadence concepts (socks) earn fewer orders but each order carries a higher CM%; the replacement interval maps to the owner's "replace every 3-6 months" idea, but no source shows what share of buyers reorder.
- The digital membership's 90.8% CM% comes from zero COGS and no shipping; it excludes the author's time, any hosting/community platform fee, and the fact that comparable nurse planners sell one-time for $2.99-$9.90. A recurring $6.99 price is an assumption.
- If the caffeine pouch plan is kept as a long-run goal, the above suggests a non-regulated launch product could build the nurse audience and email list first; that is a judgment, and the compliance gate in CLAUDE.md still governs spend.

### Gaps
- No observed repeat rate, refund rate, or willingness-to-pay for any concept; all prices are ASM; no CAC data for these categories (inherited ROAS figures are for healthcare/generic DTC ads and SRC-U); Bombas, Sock Fancy and others do not publish retention.

## 4. Who are the competitors and comparable brands?

### Takeaway
Nurse-specific incumbents (FIGS, Cherokee, Bombas, compression brands) sell the same sock/cap items at $18-$30 per item without a subscription; nurse gift boxes exist but are mostly one-off or unpriced in what I could retrieve; generic self-care subscription boxes anchor at $35-$40 a month.

### Cited Findings
- FIGS scrub caps $18-$22 — [FIGS](https://www.wearfigs.com/collections/scrub-caps), fetched 2026-10-27
- Cherokee scrub hat (Walmart listing, no price retrieved) — [Walmart](https://www.walmart.com/ip/136038763)
- Bombas compression socks $60-$121.50 per 3-pack — [Bombas](https://bombas.com/collections/womens-compression-socks), snippet, SRC-U
- Sock Fancy monthly sock subscription (men and women), about $9 + $2 shipping per pair per a Nov 2023 listing — [MSA](https://www.mysubscriptionaddiction.com/b/sock-fancy), SRC-U; Sock Fancy domain now redirects to custom.sockfancy.com — [Sock Fancy](https://www.sockfancy.com/)
- Nurse boxes named in a Nursa blog ranking: Nurse RX Box (designed by a former RN; hand sanitizer to books and gear), Nurse Gift Box (tee shirt, compression socks, badge reel), NurseLuxe (reusable straws to compression socks to candles), Single Cup Club (coffee), Snack Voyage — [Nursa](https://nursa.com/blog/10-nursing-subscription-boxes-to-try), snippet 2026-10-27, SRC-U; their prices and whether they still operate were not confirmed
- Nurse-specific compression brand pages exist (Pro Compression nurse offer; Nurse Mates 3-packs about $39.95 on eBay) — [Pro Compression](https://procompression.com/pages/best-compression-socks-for-nurses), snippet, SRC-U
- Self-care subscription anchors: TheraBox $34.99-$39.99/month; Lady Box from $18 — [MSA roundup](https://www.mysubscriptionaddiction.com/self-care-subscription-boxes?msa=hp), SRC-U
- Pouch competitor targeting nurses: Roon (4 tins $49.96 billed every 4 weeks) — [Roon](https://www.takeroon.com/pouches/er-nurse-no-drinks-past-the-doors), inherited from `economics_offer_positioning.md`

### Inferences
- Sock and cap differentiation will have to come from print/style and the subscription convenience, not price: FIGS sells a cap for $18-$22 one time, while a quarterly $24.99 POD cap leaves $2.95 CM.
- A named nurse-box niche exists with several small players, so there is demand-side signal for "nurse box" but no sourced evidence of their retention or size.

### Gaps
- Cherokee price, Nurse RX Box/NurseLuxe prices, FIGS sock prices, and any nurse-specific subscription churn were not retrieved.

## 5. Which three concepts should be tested first, and what must be true?

### Takeaway
Test, in this order: (1) quarterly compression/comfort socks sourced from a small-MOQ importer (1b), (2) a digital shift-planner membership as the cheapest audience test (8, optionally bundled with sock shipments), and (3) the snack + tea box priced at $34.99 or more with a sub-16 oz weight (2). Each needs a real supplier quote before any spend, and none should be started until the owner clears the compliance gate in `work/decisions.md` (CLAUDE.md rule on spend).

### Cited Findings
- (Model outputs, ARITH) 1b: base 12-month CM $38.73 (low $61.60, high $25.51), CM $13.56 per order at $34.99; 2: $55.89 (low $109.58, high $14.19); 8: $50.17 (low $58.35, high $40.55). Inputs and sources are in Sections 1-2. Comparator 9: $29.61 (low $58.94, high $6.72).

### Inferences
- Why socks first: best margin among physical concepts after shipping and fees, the only concept with a natural 3-6 month replacement cadence matching the owner's idea, and the highest named nurse demand in the incumbent boxes (compression socks are in the Nurse Gift Box and NurseLuxe per Nursa). Kill/continue test: per-order CM at base shipping/fees falls to zero at a landed cost of about $7.51 per pair and is $6.03 at $5.50 per pair (ARITH: non-item costs are $12.46 per order at $34.99; to be recomputed with real quotes), a first-order delivery time and size-return rate from a 20-30 unit pilot, and counsel's view on compression wording.
- Why digital second: zero COGS and shipping let you test willingness to pay and the nurse audience for the cost of a payment fee plus a subscription app; fails if people only buy one-time at $3-$10 as the sourced listings suggest. Success criterion to set: paid conversions and 3-month retention, not a figure I can source.
- Why snack + tea third: highest base-case 12-month CM but the widest range ($14-$110), so it only works with real wholesale pricing (50% of retail or better), a 3PL kitting quote, and a box under 16 oz; if wholesale only reaches 100% of retail, the CM per order is $2.22 and it fails. Run it as a limited pre-sold batch rather than an open subscription.
- Drop for now: hand/lip care, sleep consumables, electrolytes, scrunchie club and the mixed self-care box (negative base CM at the tested prices), and POD scrub caps (CM $2.95, below the cost of a $99/month Recharge plan). POD comfort socks (1a) is a fallback only if no importer quote is acceptable; avoid the $23.36 embroidered option.
- Caffeine pouches (9) stay as the comparator until the compliance gate clears; they should not be funded from this analysis.

For a professional (not conclusions):
- Counsel: wording for socks (compression, circulation, "medical" grades; whether 20-30 mmHg is treated as a regulated medical product), electrolyte or hand/lip products (supplement/food/cosmetic labeling, SPF drug status) and food kitting (labeling, allergens, state rules); auto-renewal and cancellation law for subscriptions (federal ROSCA and state automatic-renewal statutes; general knowledge, UNVERIFIED in this run); the Bolt/replacement name clearance still blocks branding spend.
- Accountant: sales tax on physical subscriptions across states, 3PL and POD nexus.
- Insurance broker: product liability for imported goods and food.

### Gaps
- Supplier quotes (importer, 3PL, Faire wholesale accounts, white-label electrolyte), real pilot repeat data, nurse willingness-to-pay for a recurring digital product, shipping time from overseas suppliers, and a sourced refund rate are all missing; owner decisions needed: price points (all ASM), minimum age policy, whether to pause pouch spend while testing, and acceptable pilot budget.
