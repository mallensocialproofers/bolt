# Economics, offer design and positioning for a 25 mg adults-only caffeine pouch sold to women night-shift nurses (Shopify DTC plus wholesale), as of 2026-10-27

Scope and method. Reused the parent model (`/home/user/bolt/research_notes/Caffeine pouch niche selection research/unit_economics.py` and `.md`) and extended it in a new self-contained script, `nurse_economics.py` (same folder as this note). It writes `nurse_cadence.csv`, `nurse_offer_cm.csv`, `nurse_healthcare_discount.csv`, `nurse_payback.csv` and `nurse_wholesale_gift.csv`. Run it with `python3 nurse_economics.py`. Firecrawl was out of credits, so this used WebSearch and WebFetch; WebSearch answers are summaries and WebFetch answers are LLM page summaries. Every source was checked 2026-10-27. Tags: **SRC** = sourced (URL given), **SRC-UNVERIFIED** = secondary, competitor-authored or search-summary only, **ASM** = assumption/scenario with no source. Pouch counts per shift are illustrative scenarios, not forecasts and not a goal; FDA's 400 mg/day is a ceiling, not a target. The age policy is not recorded in `work/decisions.md`, so 21+ is assumed throughout. Nothing here is a legal conclusion; items for counsel are marked "For a professional". Per CLAUDE.md, no spend on inventory, branding or ads is recommended before the compliance gate is cleared.

Inherited model formulas (unchanged): AOV = price per tin x tins x (1 - discount). CM1 = AOV + customer-paid shipping - tins x COGS - (2.9% x revenue + $0.30) - 2% x revenue - shipping cost - $2.50 pick-pack - adult-signature fee - extra packaging. Cumulative CM over horizon H = sum over orders at t = 0, c, 2c... < H of CM x (1 - churn)^floor(t/30), where c = order cycle in days. Break-even CAC = cumulative CM over H. Payback = first order date at which cumulative CM >= CAC. New in this extension: cycle c is derived from shifts, not days: c = tins x 20 / (pouches per shift x 13.0 shifts per month) x 30.

---

## 1. How do nurse schedules change tins per month, tin size, bundle size and subscription frequency?

### Takeaway
A nurse on three 12-hour shifts a week works about 13 shifts a month, so a pouches-per-shift scenario of 3, 5 or 8 means 39, 65 or 104 pouches a month, or 1.95, 3.25 or 5.2 twenty-pouch tins a month. That is lighter and lumpier than the parent model's daily-use cadence, so a 4-tin bundle lasts roughly 8.8 weeks at 3 per shift, 5.3 weeks at 5, and 3.3 weeks at 8, which favours a 3- to 4-tin first order and a skippable "every 6 to 8 weeks" subscription over weekly or monthly cadences.

### Cited Findings
- RNs: about 3,465,400 jobs in 2025, median pay $97,550/yr; hospital and nursing-care nurses "usually work in shifts to provide round-the-clock coverage" and "may work nights, weekends, and holidays." The BLS page does not state 12-hour shifts, full-time share or sex split — [BLS OOH Registered Nurses](https://www.bls.gov/ooh/healthcare/registered-nurses.htm), fetched 2026-10-27
- 70.2% of RN licensees were working full-time in NCSBN's 2022 survey (64.9% in 2020); HRSA's 2022 NSSRN counted 4,394,377 licensed RNs from 49,234 responses; LeadingAge summarising HRSA says 3.5 million RNs work full-time — via search summary of [LeadingAge on NSSRN](https://leadingage.org/national-sample-survey-of-registered-nurses/), 2026-10-27, SRC-UNVERIFIED (secondary; NCSBN and HRSA tables not opened)
- A learning-provider article says about 70% of nurses work full-time averaging 36 hours a week and that most work three 12-hour shifts to get there; it does not name its survey — [Elite Learning](https://www.elitelearning.com/?p=280918), 2026-10-27, SRC-UNVERIFIED. Two sites state 12-hour shifts are the most common night length — [Advance Study](https://advancestudy.org/how-long-are-night-shifts-for-nurses/), SRC-UNVERIFIED. A Nursa blog's "60% of non-ICU and 80% of ICU nurses work 12-hour shifts" has no cited source and is not used.
- Male nurses are 12% of the workforce (10% in 2018), implying roughly 88% female; Becker's does not state the female share outright — [Becker's](https://beckershospitalreview.com/nursing/the-nursing-workforce-in-21-numbers.html), via search summary, SRC-UNVERIFIED (HRSA dashboard not opened)
- Roon, a competitor, tells nurses "One pouch per shift," at 80 mg, "stop at least 8 hours before you plan to sleep," total caffeine "under 400 mg a day" — [Roon night-shift page](https://www.takeroon.com/pouches/night-shift-3am), fetched 2026-10-27, competitor copy, SRC-UNVERIFIED as to real use; it shows the brand expects low per-shift counts.

Computed cadence (script section A; ASM: pouches only on shift days, 3 shifts/week = 13.0 shifts/month; formula tins/month = pouches per shift x 13.0 / pouches per tin):

| Pouches per 12-h shift (mg/shift) | Pouches/month | Tins/month at 20/tin | Tins/month at 15/tin | Days a 3-tin bundle lasts (20/tin) | 4-tin | 5-tin |
|---|---|---|---|---|---|---|
| 3 (75 mg) | 39 | 1.95 | 2.60 | 46.2 | 61.5 | 76.9 |
| 5 (125 mg) | 65 | 3.25 | 4.33 | 27.7 | 36.9 | 46.2 |
| 8 (200 mg) | 104 | 5.20 | 6.93 | 17.3 | 23.1 | 28.8 |

One 20-pouch tin lasts 15.4, 9.2 and 5.8 days at 3, 5 and 8 per shift respectively (20 / pouches per month x 30).

### Inferences
- Tin size: 20 pouches/tin (the parent model's assumption; competitors list 15, 18 or 20) keeps tins-per-month near 2 to 3 for a light-use scenario. A 15-pouch tin raises shipping and pick-pack per pouch, which the model shows is the main cost problem, so 20 is the better working assumption; no data says nurses prefer either.
- Bundle size: 3 to 4 tins as the default first order. At 3 per shift a 4-tin bundle is about 8.8 weeks of supply; a 5-tin bundle is about 11 weeks, which delays the first reorder and slows payback (section 3).
- Subscription: offer "every 4 / 6 / 8 / 10 weeks" with skip and pause, since 3-on-4-off, rotating and per-diem schedules (and weeks off) make cadence irregular. A fixed monthly cadence would over-ship light users and raise cancellations. The pouches-per-shift figure is a modelling variable; the offer should not suggest more per shift.
- Intermittent use (shift days only) is a major difference from the parent model, which assumed daily use; reorder cycles here are 1.5 to 3 times longer at the same pouches-per-day, so payback is slower.

### Gaps
- No source for real pouches per shift, off-day use, night-shift share among women RNs, or how many nurses work 3 x 12. NSSRN and NCSBN tables were not opened (search returned only summaries). Share of RNs on nights is not established (the only BLS night-work share found in the parent notes is from 2004).

---

## 2. Offer design: bundles, price per tin, shipping threshold, adult signature, healthcare discount, gifting, wholesale

### Takeaway
At the model's assumptions (COGS $2.50, $5.50 shipping, $2.50 pick-pack, 2% refunds, free shipping on everything) a 1-tin order loses $2.25 and a 2-tin order earns only $2.85, while 3 tins at $7.99 earn $7.00 and 4 tins earn $12.09, so a 3- to 4-tin first order is the AOV floor. Charging $4.99 shipping below a threshold, or pricing at $10.99 per tin, changes this a lot; adult-signature at $10 would erase the margin on anything under 3 tins; a 10 to 20% verified-healthcare discount costs about $3 to $6 per 4-tin first order and is cheap if it replaces rather than stacks on the subscription discount.

### Cited Findings
- Price anchors: Nectr site packs $29.99 to $39.99 (inferred 4- or 5-tin packs, $7.50 to $8.25 per tin per Roon's tables), singles about $8.99 to $11.99; Grinds 25 mg about $5.95 to $5.99; Roon $9.16 to $15.00 a tin; free-shipping thresholds Nectr $50, Roon $35 on the nurse pages and $45 on others — parent note section 1 (`unit_economics.md`), and [Roon nurse page](https://www.takeroon.com/pouches/nurses-night-shift-focus), fetched 2026-10-27
- Roon's nurse page shows 4 tins at $49.96 (billed every 4 weeks, "Save 38%" against $79.96), 8 tins at $84.96, 12 tins at $109.92 ($9.16 a tin), and 4 tins one-time at $60.00 ($15.00 a tin) — [Roon ER-nurse page](https://www.takeroon.com/pouches/er-nurse-no-drinks-past-the-doors), fetched 2026-10-27. The "Save %" is against a higher reference list price ($19.99 a tin), so it is a reference-price device, not a cost saving. The same page set says shipping "$35+" in one header and "$45+" in search snippets of other pages (inconsistent).
- Verified-healthcare discounts at other brands (examples; terms change often): Wilson 15% via SheerID; Skechers 30% via ID.me; Under Armour 20%; ASICS 25% (SheerID); Crocs 15% (SheerID); New Balance 15% (ID.me); UGG 10%; Ashley Furniture 5%; Burton up to 50% on select goods; SheerID roundups put most offers at 10 to 30%, commonest 15 to 25%; Brooks limits to 3 single-use codes per rolling 12 months — [Wilson](https://www.wilson.com/pages/healthcare-worker-discount), [Trusted Health Nurses Week 2026](https://trustedhealth.com/blog/nurses-week-2026), [SheerID 2025 healthcare offers](https://www.sheerid.com/press-releases/special-2025-offers-for-healthcare-workers/), [CareRev nurse discounts](https://carerev.com/blog/ultimate-guide-to-nurse-discounts), all via search summary, SRC-UNVERIFIED
- Ultra (competitor): "We're proud to offer a discount to Military, Nurses, and First Responders," page says Ultra's Energy pouches "launched in September 2026" and deliver "180mg of caffeine alongside L-theanine"; no percent or verification provider stated — [Uncrate](https://uncrate.com/ultra-energy-pouches/), fetched 2026-10-27, SRC-UNVERIFIED (third-party editorial; ultrapouches.com returned HTTP 503). This conflicts with the parent notes, which listed Ultra as caffeine-free (Focus line); the 180 mg Energy product appears newer.
- Adult-signature: UPS and FedEx about $9 to $11 per package, FedEx $10.00 in 2026 (up from $8.65); no official UPS or USPS figure found — [3PL Center](https://3plcenter.com/shipping-surcharges-an-in-depth-look-at-additional-fees-from-fedex-ups-and-usps/), [Lateshipment](https://www.lateshipment.com/blog/fedex-and-ups-delivery-signature/) (from parent note; SRC-UNVERIFIED). Whether any signature is legally required for caffeine pouches is not established.
- Hospital gift shops: a consultant told Clarivate a hospital gift shop must mark goods up "50% or more" plus shipping and that about 80% of customers are hospital employees; a 50% markup equals a 33.3% margin, keystone (100% markup) equals 50% — [Clarivate](https://clarivate.com/?p=89933) (page returned HTTP 403 to fetch; figures from search summary), [markup/margin table](https://koronapos.com/blog/retail-markup-calculator/); SRC-UNVERIFIED. A vendor puts tourist gift-shop margins at 50 to 65% and food items at 33 to 50% — [Lamose](https://lamose.com/blogs/recipes/gift-shop-pricing-strategy-markup-margins-what-tourists-will-pay), SRC-UNVERIFIED
- Distributor 15 to 35%, store markup 38 to 45% on cost for convenience — parent note section 2 (mrcheckout.net, UNVERIFIED)

Computed (script sections B, C, F, G, H; offer price ladders are ASM anchored to the sourced multipack per-tin prices above):

**Ladder A** (per tin: 1 = $8.99, 2 = $8.49, 3 = $7.99, 4 = $7.99, 5 = $7.49; AOV $8.99, $16.98, $23.97, $31.96, $37.45). First-order CM, COGS $2.50, shipping cost $5.50:

| Tins | AOV | Free shipping on all | Customer pays $4.99 under $35 | Same, COGS $1.50 / $3.50 | Free-all, worst case COGS $3.50 + ship $8.00 | With $10 adult signature (threshold case) |
|---|---|---|---|---|---|---|
| 1 | $8.99 | -$2.25 | +$2.49 | +$3.49 / +$1.49 | -$5.75 | -$7.51 |
| 2 | $16.98 | +$2.85 | +$7.59 | +$9.59 / +$5.59 | -$1.65 | -$2.41 |
| 3 | $23.97 | +$7.00 | +$11.74 | +$14.74 / +$8.74 | +$1.50 | +$1.74 |
| 4 | $31.96 | +$12.09 | +$16.84 (free at $30 threshold: $12.09) | +$20.84 / +$12.84 | +$5.59 | +$6.84 |
| 5 | $37.45 | +$14.81 | +$14.81 | +$19.81 / +$9.81 | +$7.31 | +$4.81 |

**Ladder B** (per tin 10.99 / 10.49 / 9.99 / 9.99 / 9.49): CM1 at COGS $2.50, ship $5.50 is +$4.40, +$11.40, +$17.45, +$19.70, +$24.32 for 1 to 5 tins (threshold case); with $10 adult signature -$5.60, +$1.40, +$7.45, +$9.70, +$14.32.

Verified-healthcare discount (ladder A, COGS $2.50, ship $5.50; reorder = max(healthcare, 15% subscription) i.e. not stacked; "stacked" = both applied):

| Tins | List CM1 | 10% off CM1 | 15% off CM1 | 20% off CM1 | Reorder CM, not stacked | Reorder CM stacked at 10 / 15 / 20% |
|---|---|---|---|---|---|---|
| 3 | $11.74 | $9.46 | $8.32 | $7.18 | $8.32 (7.18 at 20%) | $6.38 / $5.42 / $4.45 |
| 4 | $16.84 | $13.80 | $12.28 | $10.76 | $12.28 (10.76 at 20%) | $9.70 / $8.41 / $7.11 |

On a 4-tin free-shipping order the discount costs $3.04 (10%), $4.56 (15%) and $6.08 (20%) of CM on the first order. (The 5-tin 10% row in `nurse_healthcare_discount.csv` looks better than list only because its AOV falls under $35 and the $4.99 customer shipping kicks in; read threshold effects, not the discount, from that row.)

Gift bundle (ASM: 4 tins plus $2.00 gift sleeve/insert, free shipping, COGS $2.50, ship $5.50): $34.99 gives CM1 $12.98 (37%); $39.99 gives $17.73 (44%); $44.99 gives $22.49 (50%).

Hospital gift shop or cafe wholesale (ASM MSRP; freight $0.25 a tin; CM per tin at COGS $1.50 / $2.50 / $3.50):

| MSRP | Retailer terms | Direct (no distributor) brand net and CM | With 20% distributor (ASM) |
|---|---|---|---|
| $8.99 | 50% markup on cost | net $5.99; $4.24 / $3.24 / $2.24 | net $4.79; $3.04 / $2.04 / $1.04 |
| $8.99 | keystone (100%) | net $4.50; $2.75 / $1.75 / $0.75 | net $3.60; $1.85 / $0.85 / -$0.15 |
| $10.99 | keystone | net $5.50; $3.75 / $2.75 / $1.75 | net $4.40; $2.65 / $1.65 / $0.65 |
| $7.99 | keystone | net $4.00; $2.25 / $1.25 / $0.25 | net $3.20; $1.45 / $0.45 / -$0.55 |

### Inferences
- What first order makes AOV positive: with free shipping on all orders, 3 tins at $7.99 (AOV $23.97) is the smallest bundle that stays positive in every scenario run (worst case COGS $3.50 + $8.00 shipping: +$1.50); 4 tins at $7.99 ($31.96) is positive even at COGS $3.50 + $8.00 shipping (+$5.59). 1 and 2 tin free-shipping orders are negative or marginal at the parent assumptions, matching the parent finding. A 5-tin bundle at $7.49 earns less CM1 ($14.81) than a 4-tin at $7.99 ($16.84 with customer-paid shipping, $12.09 free) because the extra discount eats the extra tin; its only advantage is higher AOV and fewer shipments per tin.
- Shipping threshold: a $30 to $35 free-shipping line placed just above a 3-tin AOV nudges buyers toward 4 tins. Charging $4.99 below the line makes even 1- and 2-tin orders profitable at these assumptions (+$2.49, +$7.59), but this is untested conversion risk and a competitor-vs-price perception question; the parent model did not include customer-paid shipping, so this is a design option, not a model finding. The 4-tin $31.96 AOV sits under Roon's $35 line, so a threshold of about $30 is simplest (ASM).
- Adult signature: if it is required or chosen, $10 per parcel erases CM on 1 to 2 tins and cuts a 3-tin first order to +$1.74. The option only works with bundles of 4+ tins or $9.99+ per tin. Whether a signature is needed at all is for counsel; prefer age verification at checkout and, if possible, no signature on delivery (see Gaps).
- Healthcare discount: use 10% or 15% on the first order only, via SheerID or ID.me, and make it replace (not stack on) the subscription discount. At 15% a 4-tin first order still returns $12.28. Stacking 15% + 15% drops the 4-tin reorder CM from $12.28 to $8.41 (-31%). Ultra's nurse discount, Wilson, Crocs, New Balance show 15% is a normal mid-point; Skechers and ASICS go higher on high-margin goods. The verification vendors' fees to merchants were not found (Gap).
- Gifting: gift-bundle margin is healthy only because of premium pricing ($39.99 or $44.99 for 4 tins, $10 to $11.25 a tin). Gift occasions are Nurses Week, graduation, holidays, but see Gaps; also a gift to a nursing student could reach someone under the age policy, so gifting needs recipient age handling (For a professional). A "thank-you" gift for a nurse is also a trap: the crude "tired nurse" caffeine trope is exactly the framing Bolt's rules forbid.
- Wholesale: at $8.99 MSRP with a 50% markup (the consultant's stated minimum) the brand nets $5.99 and keeps $3.24 a tin at COGS $2.50, per tin, with zero CAC and no processing fees (but no bundle-level AOV effect and unknown order sizes). At keystone or with a distributor layer it falls toward zero at COGS $3.50. Hospital cafe/gift shop buyers also buy in unit counts that cannot be inferred (no data), and the facility's own rules on oral products and caffeine are unknown.

### Gaps
- No published size of the nurse-gift market: the search for an NRF or other Nurses Week spend figure returned only Mother's Day data; a university page claims 68% of nurses called Nurses Week gifts insufficient but the survey has no named sponsor. National Nurses Week 2026 ran May 6 to 12 per [TimeTrex](https://www.timetrex.com/blog/national-nurses-week-2026) (UNVERIFIED); 2027 dates not checked.
- No hospital gift shop or cafe margin beyond one consultant quote; no hospital procurement terms, minimum orders or policy on selling caffeine pouches on campus.
- SheerID and ID.me merchant pricing; Ultra's discount percent and verifier; whether competitors Wip, Mojo, Grinds or Nectr give nurse discounts (search found none; weak evidence).
- Real COGS, 3PL fees, tin weight (shipping flat across 1 to 5 tins is optimistic), and adult-signature legal requirement remain unknown (inherited from parent note).

---

## 3. CAC and payback for a healthcare-worker audience

### Takeaway
No CAC, CPM or conversion benchmark exists for selling a consumer product to nurses, or for caffeine pouches; the closest sourced figures are healthcare-advertiser and health-and-wellness benchmarks (CPM $14 to $26, CPC $1.58 to $2.64, CPA $38.55 to $52.98, Meta prospecting ROAS 1.8 to 3.2) and they imply a first-order CAC of $7.49 to $20.81 if ROAS holds but $53 to $264 if converted from clicks, a gap that only a test can close. Against the model's $25 / $40 / $60 CAC test points, a 4-tin bundle at 5 per shift pays back in 37 / 111 / 185 days; at 3 per shift it pays back in 62 / 185 / 431.

### Cited Findings
- Healthcare Meta CPM about $25.79 (12-month average, about $3B spend dataset, roughly 30% above a $19.80 global baseline); a separate 2026 table lists $14.19 CPM and $14 to $22 for general health and fitness — [Oyova](https://www.oyova.com/blog/average-cost-of-facebook-ads-what-healthcare-pharma-businesses-should-expect/), [Superads CPM](https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/healthcare), [Webtonic, updated 2026-10-09](https://www.webtonic.io/blog/health-wellness-facebook-ads-statistics) (fetched 2026-10-27); SRC-UNVERIFIED (vendor datasets; sample sizes not disclosed)
- Healthcare CPC about $1.58 (mid-2025 to mid-2026, range $1.225 to $1.976) or $1.63 (older); Health & Fitness CPC $2.64 — [Superads CPC](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/healthcare), [Webtonic](https://www.webtonic.io/blog/health-wellness-facebook-ads-statistics); SRC-UNVERIFIED
- Health & wellness CPA $38.55 on Facebook in 2026 (Influee) vs $52.98 for Health & Fitness (Hawky) — the two conflict; healthcare Meta average ROAS 2.8, prospecting 1.8 to 3.2, retargeting 8+ (Ryze AI) — [Webtonic](https://www.webtonic.io/blog/health-wellness-facebook-ads-statistics), fetched 2026-10-27; SRC-UNVERIFIED. Webtonic gives no supplement-specific CPC/CPA/ROAS and notes an unsourced supplement AOV of $80 to $150.
- Healthcare cost per purchase US $84.66 vs global $47.73 — [Superads cost per purchase](https://www.superads.ai/facebook-ads-costs/cost-per-purchase/healthcare/united-states), search summary, SRC-UNVERIFIED
- Parent-note anchors: generic DTC Meta median ROAS 2.7 to 2.96, supplement MER 3.0 to 5.5 (one agency), skincare CAC $25 to $80 — `unit_economics.md` section 5
- Meta restricts health and wellness ad targeting to 18+ audiences (search summary only; not verified against Meta policy text) — [Oyova](https://www.oyova.com/blog/average-cost-of-facebook-ads-what-healthcare-pharma-businesses-should-expect/), SRC-UNVERIFIED. Meta ad-standards text found earlier bars nicotine pouches and "products that simulate smoking" and does not mention caffeine ([Meta](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/tobacco-related-products/), per brand-name report).

Computed (script sections D and E; ladder A, COGS $2.50, ship $5.50, $4.99 customer shipping under $35, 15% subscription discount on reorders, 8% monthly churn, 20/tin; break-even CAC = cumulative CM over the horizon):

| Bundle (AOV) | Pouches/shift | Days between orders | CM first / reorder | BE-CAC first order | 90 d | 180 d | 365 d | Payback days at CAC $25 / $40 / $60 |
|---|---|---|---|---|---|---|---|---|
| 3 tins ($23.97) | 3 | 46.2 | $11.74 / $8.32 | $11.74 | $19.40 | $31.84 | $49.07 | 92 / 231 / 554 |
| 3 tins | 5 | 27.7 | same | $11.74 | $34.76 | $52.69 | $80.84 | 55 / 111 / 222 |
| 3 tins | 8 | 17.3 | same | $11.74 | $49.46 | $78.83 | $123.58 | 35 / 69 / 121 |
| 4 tins ($31.96) | 3 | 61.5 | $16.84 / $12.28 | $16.84 | $27.23 | $36.03 | $55.11 | 62 / 185 / 431 |
| 4 tins | 5 | 36.9 | same | $16.84 | $38.53 | $56.89 | $88.20 | 37 / 111 / 185 |
| 4 tins | 8 | 23.1 | same | $16.84 | $50.81 | $86.83 | $136.71 | 23 / 46 / 92 |
| 5 tins ($37.45) | 3 | 76.9 | $14.81 / $9.47 | $14.81 | $22.83 | $29.08 | $38.48 | 154 / 385 / never in 24 months |
| 5 tins | 5 | 46.2 | same | $14.81 | $23.53 | $37.69 | $57.31 | 92 / 185 / 369 |
| 5 tins | 8 | 28.8 | same | $14.81 | $41.02 | $61.43 | $89.69 | 58 / 87 / 173 |

Benchmarks-to-CAC arithmetic: first-order CAC = AOV / ROAS. At ROAS 1.8 / 2.8 / 3.2 a 4-tin $31.96 order gives CAC $17.76 / $11.41 / $9.99 (3 tins: $13.32 / $8.56 / $7.49; 5 tins: $20.81 / $13.38 / $11.70). From clicks: CAC = CPC / site conversion rate. At CPC $1.58 and conversion 1% / 2% / 3% (conversion is ASM, no source) CAC is $158 / $79 / $53; at CPC $2.64 it is $264 / $132 / $88.

### Inferences
- A $25 CAC pays back inside a year only for 3- to 4-tin bundles; $40 needs 4+ tins and 5 per shift (or $10.99 pricing); $60 needs about 8 per shift or a long horizon, and 5 tins at 3 per shift never pays back at $60. Meanwhile faster payback at higher pouches per shift is mechanical and must not be a targeting goal. The scenario most relevant to Bolt's rules is the low-use one: at 3 per shift a $40 CAC needs about 6 months, so unit economics are workable only with a higher-priced tin, thin COGS or a lower CAC, not with encouragement to use more.
- The ROAS-based CAC ($7 to $21) and the click-based CAC ($53 to $264) differ by an order of magnitude. Which one applies depends on conversion rate and the audience's price tolerance for a $24 to $38 first order, which is unknown. First-order CAC cannot be repaid at either set in one order except at the ROAS-based figures (first-order BE-CAC is $11.74 to $16.84).
- Nurse-targeted channels (nurse communities, Reddit r/nursing, nurse creators, hospital cafe sampling, verified-discount directories) may have lower CAC than Meta cold traffic, but no data; see the sibling note on reach and channels in this folder for that coverage (`reach_and_channels.md`).
- Wholesale needs no CAC but a sales cost that is unmodelled (samples, broker time).

### Gaps
- No CAC, CPM or conversion data for nurse-targeted consumer ads, for caffeine pouches, or for supplements to women specifically; the "healthcare" figures are from clinics and pharma advertising to the public, a different audience and offer.
- Whether Meta, Google, TikTok or processors accept caffeine-pouch ads and whether occupation targeting (nurse job titles) is available for this category (not checked).
- Real conversion rate, repeat rate, subscription take-rate, churn (5 to 12% a month used, vendor blogs) and refund/chargeback rate.

---

## 4. Claim-free positioning territories for women night-shift nurses; name fit; packaging cues

### Takeaway
Five territories can be written without a single effect claim: price clarity, pocket format, dose transparency, taste, and solidarity (verified-nurse pricing and community). Increment fits the dose-transparency territory best but reads as a clinical dosing word and nudges "add more"; Hasp fits discretion and the lid-closing image but sits closest to the hard-consonant nicotine-pouch name pattern, so its tin must avoid look-alike cues. These are directions, not final copy; all copy is for `label-claims-reviewer` and counsel.

### Cited Findings
- Roon's nurse pages sell on format and effect: "Imagine caffeine that needs no mug, no lid and no free hand," "A TIN IN A SCRUB POCKET," "Drinks do not go past the doors, and the break room is two hallways and a badge swipe away," "It goes past the doors with you. A cup does not." — [Roon night-shift nurses page](https://www.takeroon.com/pouches/nurses-night-shift-focus), [Roon 12-hour nursing shifts page](https://www.takeroon.com/pouches/er-nurse-no-drinks-past-the-doors), fetched 2026-10-27, competitor copy
- Brand name candidates and their research status: INCREMENT (ranked first; "no live or pending mark in 5, 29, 30, 31, 32, 34 or 43" on USPTO's backend; Stripe owns increment.com; plural "increments" has a crude Urban Dictionary entry; "implied-claim risk mild but real") and HASP (ranked second; mirror data only; Travex LLC pending HASP Class 9/45 filed 2026-07-28; "moderate packaging look-alike risk (short hard word)"); neither is cleared — `/home/user/bolt/reports/Bolt replacement brand name research.md`, 2026-10-27. Existing pouch names cluster as hard short nicotine-style words vs coined caffeine words — same report, citing [Roon blog](https://www.takeroon.com/blog/who-owns-nicotine-pouch-brands), UNVERIFIED
- A Kansas school treats caffeine pouches under "tobacco and simulated tobacco" rules; youth nicknames include "lip pillows" and "deckies" — [Fortune, 2026-10-22](https://fortune.com/2026/10/22/schools-ban-caffeine-pouches-students-coffee/), per the brand report

### Inferences
Candidate territories (sample headline directions only; each must pass `label-claims-reviewer` and counsel; none makes a health, performance, alertness or sleep claim):

1. **Price clarity.** Per-pouch price printed, a published bundle ladder, no reference-price games. Directions: "25 mg a pouch. Price per pouch on the tin." / "The ladder: 1 tin, 3 tins, 4 tins." Risky: comparisons ("cheaper than coffee") need substantiation and a stable comparator; Roon-style "Save 38%" reference prices; "affordable energy".
2. **Pocket format and discretion.** A small, quiet, flat tin. Directions: "Small tin. Fits a pocket." / "No cup. No lid. 25 mg per pouch." Risky: "scrub pocket", "on the unit", "past the doors" invite on-shift, patient-care use and hospital-policy conflict (hospital rules unknown; see `workplace_regulatory_claims.md` in this folder if present); "discreet" can read as hiding use; "no crash", "no jitters" are effect claims.
3. **Dose transparency.** The number is the brand. Directions: "25 mg. Printed on every pouch and every tin." / "You know the number." Add a total-per-day line approved by counsel. Risky: "you decide how many", "stack as needed" (reads as a heavy-use invitation); "just a little" implies a benefit; any phrase that sounds like a recommendation to a clinician-audience, e.g. "titrate" or "dose", has a medical register.
4. **Taste.** A mint (or other plain flavor) and the experience of a pouch. Directions: "A mint with the number printed on it." Risky: candy, dessert, fruit-and-cartoon flavor cues and slang that appeal to minors; "refreshing" is borderline effect language; taste is entirely untested.
5. **Solidarity and verified-nurse pricing.** Community and a thank-you price, not a claimed outcome. Directions: "Nurse pricing, verified in under a minute." / "Made with night-shift schedules in mind: skip, pause, change your date." Risky: "hero", "angel", "fuel for the front line", "get through your shift", "for tired nurses" (fatigue/performance framing); implying nurse or hospital endorsement; medical imagery (scrubs, stethoscopes, lab coats) that implies a health benefit or authority; "night owl" and "3 a.m." imagery that signals staying alert.

Words to flag everywhere (list for the reviewer; not exhaustive): energy, boost, focus, alert/alertness, awake/wake, sharp, stamina, endurance, fatigue/tired/sleepy/exhausted, crash, jitters, clean (energy), calm, "all-day", "fuel", "performance", "no sleep", "recover/recharge", "natural", "safe", "healthy", "nootropic", "tolerance"; any reference to sleep timing (even a safety-style note such as Roon's "stop at least 8 hours before you plan to sleep"); nicotine, "quit", "alternative to smoking/vaping/dip"; "lip" and pillow/cushie slang; "high performer" (Ultra's positioning). Counsel to say whether safety language such as a daily maximum is allowed, since it may itself imply sleep/health effects.

Name fit for this audience (inferences, not research findings):
- INCREMENT: a clinical-leaning word; nurses meet "increment" in dosing and titration contexts, so it may read as medication-like, which sits close to the "implied disease/dose" register the brand report flags for DOSEO. It pairs well with "25 mg per pouch" and the territory 3, and it is neutral to nicotine and youth. Its "one more small step" meaning risks nudging toward adding pouches, so copy must avoid "one more", "build up" and "step up".
- HASP: short, hard, one-syllable and padlock-related, which suits territory 2 (discretion, a lid that clasps) and a nurse's locker/badge world. It sits nearest to the Zyn/Velo/Rogue naming pattern, may be misheard (gasp, hash), and "gasp" or breathing associations could read poorly to nurses (inference). It is also less obviously "calm".
- Neither name suggests a symptom or an effect; whichever is chosen, the trademark and counsel questions in the brand report are unresolved and branding spend is gated.

Packaging cues to avoid a nicotine-tin look-alike (describe, copy no brand): avoid a flat black or matte-saturated round tin with a bold single-colour strength band and a mint-green/ice-blue sub-brand coding, which is how nicotine-pouch tins are commonly recognised; avoid a bold uppercase single-word logo with a strength number as the largest element; avoid lip/mouth imagery, lightning or flame symbols and cool-guy photography; use a larger, plain "25 mg caffeine per pouch" panel, "Contains caffeine. Adults only (21+ until the owner decides)" and a total mg per tin, a warm paper-white or soft earth-tone label with a serif or humanist type, a clearly different lid and shape from pharmacy blister packs and nicotine tins, and no nurse icons or medical symbols. The child-resistance and exact warning wording are for counsel.

### Gaps
- No tested audience reaction to any name or territory; nurse samples were not available. "Fit" for each name is my reading, not a finding. Foreign-language and slang meanings of Increment and Hasp for nurses were not searched.
- Hospital and facility policy on oral caffeine products in clinical areas (not found; relevant to the format territory).

---

## 5. Competitor teardown: how others speak to nurses

### Takeaway
Only Roon addresses nurses with dedicated pages, and its copy is built on effect claims (focus, staying awake, "6 to 8 hours," "no crash") that Bolt must not use; Ultra offers a nurse discount without a documented nurse message; Wip, Mojo, Grinds and Nectr showed no nurse targeting in what was found. What Bolt can borrow is the format fact (no mug, small tin), the schedule-aware subscription mechanics, and the verified-nurse price, not the claims.

### Cited Findings
- **Roon (nurse and night-shift pages).** Titles "Focus Pouches for Night Shift Nurses" and "Caffeine Pouches for 12-Hour Nursing Shifts." Copy includes "Steady focus for 6 to 8 hours," "Sharp focus in minutes," "Clean energy. Calm focus. No crash," "One pouch at 7pm is still working at 2am," "Placed at handover, one pouch reaches the far side of the middle of a twelve," "Ten seconds of your break buys 6 to 8 hours of the shift," "Without nicotine, without jitters, without crashing out after 4 hours," "Built for daily use," ingredients "resist the tolerance caffeine builds," and a guarantee "If you don't feel a real difference in 30 days, you pay nothing" (first order only, once per customer). Each pouch is 80 mg caffeine with L-theanine and other ingredients, 15 pouches per tin. Pricing: from $9.16 a tin (12-tin subscription), $15.00 a tin one-time, "Free U.S. shipping on orders $35+" (header) but "Free shipping on every order" in the subscription block. Skip, pause or cancel. No nurse discount found. Disclaimer: "These statements have not been evaluated by the Food and Drug Administration." — [night-shift nurses](https://www.takeroon.com/pouches/nurses-night-shift-focus), [12-hour nursing shifts](https://www.takeroon.com/pouches/er-nurse-no-drinks-past-the-doors), [night-shift 3am](https://www.takeroon.com/pouches/night-shift-3am), fetched 2026-10-27. Search results also show Roon pages at /pouches/night-shift-focus-pouches and /pouches/stay-awake-work-after-no-sleep (not opened).
- **Ultra.** "We're proud to offer a discount to Military, Nurses, and First Responders"; Energy pouches launched September 2026 with 180 mg caffeine and L-theanine — [Uncrate](https://uncrate.com/ultra-energy-pouches/), fetched 2026-10-27; its funding release is titled "Pouches Minus the Nicotine: Ultra Raises $11 Million to Build a Clean, Non-Addictive Pouch for High Performers" — [Business Wire 2026-01-20](https://www.businesswire.com/news/home/20260120688296/en/Pouches-Minus-the-Nicotine-Ultra-Raises-11-Million-to-Build-a-Clean-Non-Addictive-Pouch-for-High-Performers/) (title only; 403 in the parent notes). Ultra's own site returned HTTP 503.
- **Wip, Mojo, Grinds, Nectr.** No nurse or healthcare discount or nurse page found for Wip, Mojo or Grinds in the search; Wip is associated with trades/construction and Grinds with military (Grinds x BRCC) per the parent notes (`demand_and_segments.md`). Absence of search results is weak evidence. Wip's own site was a domain-for-sale page and Grinds's site returned 503 in the parent run. Nectr: nectr.energy lists packs with Subscribe & Save 35% and free shipping over $50, with no nurse messaging seen — [nectr.energy](https://nectr.energy/), per parent notes.
- Independent evidence: none found testing Roon or pouches in night-shift nurses; one search result is a reference list on energy-drink use among healthcare workers on night shifts — [Acta Biomedica](https://mattioli1885journals.com/index.php/actabiomedica/article/view/15651).

### Inferences
- Off-limits for Bolt: every effect line in Roon's pages (focus, sharp, calm, clean energy, no crash, no jitters, "6 to 8 hours," tolerance, "if you don't feel a difference" guarantee which implies an effect), the sleep-timing advice, and any "high performer" positioning. Also off-limits: use of the 3 a.m. and "stay awake" frames, and any use-guidance that promotes multiple pouches per shift.
- Usable, subject to review: format facts ("no cup, no lid, no free hand" is effect-free but implies on-the-floor use; flag for review), schedule-aware subscription features (skip, pause, change date), a verified-nurse discount, a first-order satisfaction guarantee worded around the order not an outcome (e.g. unopened-tin return; counsel to word).
- The white space is the price-and-dose-transparent lane: Roon's price is $9.16 to $15.00 a tin at 80 mg; Grinds is the only 25 mg comparable at about $0.33 per pouch; there is no nurse-specific 25 mg offer found.

### Gaps
- Wip, Mojo, Grinds, Nectr, NZE, Wild own-site nurse messaging not directly checked (parent run could not read most of these sites). Ultra's discount percent and verifier unknown. Roon's nurse pages were read once; their performance or conversion is unknown.

---

## 6. What cannot be known without tests, and a cheap test plan

### Takeaway
CAC, retention, willingness to pay for 25 mg, taste, hospital acceptance, ad-platform acceptance and wholesale demand are all unknown; none of them can be inferred from competitors. A cheap sequence of fake-door, sample and wholesale-conversation tests can bound them before inventory is bought, but it cannot start until the owner clears the compliance gate and the name is cleared.

### Cited Findings
- (Evidence that it is unknown) No pouch-specific retention or reorder data, no CAC for caffeine pouches or nurse audiences, no co-packer quote, no hospital policy data, no nurse-gift market size, no nurse WTP for 25 mg — sections 1 to 5 above; parent `unit_economics.md` section 4 and section 6 gaps.

### Inferences
Cannot be known without tests (and how it enters the model):
1. CAC for nurses (Meta, TikTok, creators, communities), by channel. Enters as the CAC input.
2. First-order bundle mix and AOV: do nurses choose 1, 3 or 4 tins at the offered ladder? Enters as tins per order.
3. Reorder rate and subscription take-up at 4 / 6 / 8 / 10-week cadences; churn (5 to 12% per month is vendor-blog only).
4. WTP for a 25 mg pouch at $7.99 to $10.99 a tin, against Grinds (about $0.33/pouch) and Nectr/Roon pricing; per-mg price is the weak point.
5. Taste (mint vs one other) and pouch comfort.
6. Healthcare discount lift: does a 10 to 15% verified offer change conversion enough to pay for itself.
7. Hospital cafe and gift-shop interest, order sizes, policy.
8. Ad-platform and payment-processor acceptance for caffeine pouches (policy text not retrieved).
9. Real COGS, shipping weight, adult-signature need.

Cheap test plan (all spend subject to owner approval and the compliance gate; nothing is published or sent by an agent):
- Test 0 (desk, no cost): counsel review of territories and flagged words; trademark search on INCREMENT/HASP; check ad-platform and processor policies; read SheerID and ID.me pricing; ask two or three hospital gift shops or cafes about policy by phone.
- Test 1 (landing page smoke test, $0 to a few hundred dollars): a single claim-free page with the price ladder (e.g. 1 / 3 / 4 tins at $7.99 to $10.99) and an email waitlist or a "notify me" button, with no sale; compare territory headlines 1 to 5 by click-through and signups. Read price-point preference from clicks on bundle size. A fake door that takes money would need counsel; do not take payments for product that does not exist.
- Test 2 (sample/taste, small): send free sample pouches to a small, consenting adult nurse panel (21+ verified) with a taste and packaging-cue survey (flavor, tin look, "does this remind you of a nicotine tin"); no use instructions beyond label text. Counsel first on sampling rules.
- Test 3 (pre-sell to cap risk): limited pre-order of 4-tin bundles at two prices ($7.99 vs $9.99 per tin, split) once COGS and shipping are quoted; measure conversion and cancellations.
- Test 4 (wholesale): approach 3 to 5 hospital gift shops/cafes with a two-line sell sheet (MSRP $8.99, 50% markup assumption) and ask about volume and policy; record margin terms.
- Success criteria set in advance from the model: first-order CAC below the 4-tin first-order break-even ($16.84 at COGS $2.50) is a green light; CAC $25 to $40 needs at least 70 % of buyers on 4-tin bundles and a reorder within the cycle; CAC above $60 means stop or reprice (thresholds come from the table in section 3, not from a source).

### Gaps
- Test costs for sampling, SheerID/ID.me, and a landing-page tool were not priced. Sampling and pre-sale legal rules (including state laws on caffeine pouches, age verification and ads, which the parent CLAUDE.md says are not yet researched) are for counsel.

## For a professional (collected)
- Counsel/label reviewer: every headline direction and flagged word above; whether a daily-maximum or dose-total statement or a sleep-adjacent safety note is allowed; whether a "taste/satisfaction" guarantee is acceptable; recipient age handling for gifts; whether verified-nurse pricing or imagery implies endorsement.
- Counsel: whether any signature or age check on delivery is legally required before paying the $9 to $11 adult-signature fee; sampling rules; ad-platform and processor acceptance.
- Trademark attorney: INCREMENT and HASP clearance (open in the brand report).
- Accountant/broker: COGS, 3PL, product liability for the nurse channel; SheerID/ID.me contract cost.

## Files created
- `/home/user/bolt/research_notes/Overnight women nurses niche research/nurse_economics.py` (rerunnable; all inputs tagged in comments)
- `nurse_cadence.csv`, `nurse_offer_cm.csv`, `nurse_healthcare_discount.csv`, `nurse_payback.csv`, `nurse_wholesale_gift.csv` (same folder)
