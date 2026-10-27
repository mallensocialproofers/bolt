# Delphine 25 mg caffeine pouch: cost model, break-even, cash and usage scenarios (2026-10-27)

Agent: finance. Status: MODEL ONLY. There are no supplier quotes, no supplier terms and no owner-approved prices, so every cost below is a labeled scenario, not a quote. Brand is Delphine (not trademark-cleared). Minimum age is not recorded in `work/decisions.md`; treated as 21+. The compliance gate is not cleared, so nothing here recommends inventory, branding or ad spend.

Files: this note, `/home/user/bolt/work/finance/2026-10-27-delphine-cost-model.csv` (long format: section, row, column, value; 1,214 rows) and `/home/user/bolt/work/finance/2026-10-27-delphine-cost-model.py` (rerun it to regenerate the CSV and all tables; 48 internal checks assert on every run).

## 1. Summary

Three numbers matter most. (1) A 4-tin first order at the ladder-A price of $7.99 a tin earns about $12.09 of contribution (COGS $2.50, shipping $5.50, free shipping), while a 1-tin order loses $2.25 and a $10 adult-signature fee cuts the 4-tin order to $2.09 and turns a 3-tin order negative (-$3.00). (2) A customer on the 3-pouches-per-shift scenario, buying 4-tin bundles with a 15% subscription discount and 8% monthly churn, returns about $35.58 of contribution in 12 months: enough to repay a $25 CAC, not a $40 CAC, and only if COGS stays under about $3.14 a tin. (3) Cash is driven by the unquoted supplier terms: one 25,000-tin PO (the only published MOQ, Daily Manufacturing, self-reported and unverified) costs $37,500 to $87,500 at scenario COGS of $1.50 to $3.50, and the modelled peak cash need is about $55k at $2.50 COGS, against roughly $5k to $13k for an illustrative 5,000-tin run at 1,500 tins a month. COGS, shipping weight, the signature rule and CAC are all unknown, so this is a screen that shows where the thresholds sit, not evidence that the business works. Usage rows are scenarios, not forecasts, and not a customer-facing goal.

## 2. Inputs and assumptions (status tags)

Tags: SRC = sourced, file cited. SRC-U = sourced but UNVERIFIED (vendor blog or secondary page). ASM = placeholder scenario, no source. OWNER = owner must supply. Nothing is currently tagged "owner supplied", because the owner has supplied only the price scenarios, the three usage levels and the brand.

| Input | Value used | Status | File |
|---|---|---|---|
| Retail price scenarios | $8.99, $9.99, $10.99 per tin | Owner scenarios in the brief; anchors Bucked Up $8.99, Nectr $10.99 (SRC-U) | `research_notes/Caffeine pouch niche selection research/unit_economics.md` s1 |
| Bundle ladder A | 1 tin $8.99, 2 $8.49, 3 $7.99, 4 $7.99, 5 $7.49 | ASM, anchored to multipack per-tin prices $7.50 to $8.25 | `research_notes/Overnight women nurses niche research/nurse_economics.py` |
| Pouches per tin | 20 | ASM (competitors 15/18/20) | unit_economics.py |
| COGS per tin | $1.50 / $2.50 / $3.50 | ASM. No published COGS; only a self-contradicting FOB hint $0.78 to $2.60, unit undefined | `Bolt caffeine pouch launch research/sourcing.md` s4; unit_economics.md s3 |
| Card fee | 2.9% + $0.30 | SRC | unit_economics.md s3 (stripe.com/pricing, shopify.com/pricing, checked 2026-10-27) |
| Dispute fee | $15 | SRC | same |
| Shipping cost per order | $5.50 or $8.00, flat across 1 to 5 tins | SRC-U ($5.50 USPS commercial pre 2026-07-12; $7.90 retail zone 1 after). Flat is optimistic: tin weight unknown | unit_economics.md s3 |
| Pick-pack and mailer | $2.50 per order | ASM | unit_economics.py |
| Refunds + chargebacks | 2% of revenue | ASM, no benchmark | unit_economics.py |
| Adult signature | $10 per parcel | SRC-U ($9 to $11); whether required is unknown | unit_economics.md s3 |
| Subscription discount | 15% | SRC-U (Wip via Roon) | unit_economics.md s1 |
| Monthly churn | 8% (5% to 12% range) | SRC-U vendor blogs | unit_economics.md s4 |
| Nurse shift pattern | 3 shifts a week (13.0 a month) | ASM (Elite Learning, UNVERIFIED) | `Overnight women nurses niche research/economics_offer_positioning.md` s1 |
| Wholesale discount off retail | 33.3% / 40% / 50% | OWNER (missing); 33.3% = 50% retailer markup (Clarivate consultant, UNVERIFIED), 50% = keystone | economics_offer_positioning.md s2 |
| Wholesale freight | $0.25 per tin | ASM | nurse_economics.py |
| Product liability insurance | $700 to $4,500 a year | SRC-U broker blogs (Assureful, Insurance Canopy) | unit_economics.md s3 |
| Age-verification app | $24 to $360 a year ($2 to $29.99 a month) | SRC-U app listing prices; no app chosen | `Overnight women nurses niche research/workplace_regulatory_claims.md` l.119 |
| Supplier lead time | 2 months | ASM, from Daily Manufacturing "about 6 weeks" (self-reported, UNVERIFIED), transit not included | `Bolt caffeine pouch launch research/gap_federal_and_suppliers.md` |
| PO size | 25,000 tins; 5,000 tins | 25,000 = Daily Manufacturing self-reported MOQ, UNVERIFIED and from a maker with an FDA CTP warning letter on nicotine pouches (see decisions.md); 5,000 is an ASM illustration | same |
| Deposit share | 30% / 50% / 100% | ASM. No supplier terms exist | none |
| Tins sold per month | 500 / 1,500 / 3,000 | ASM. No demand data | none |

### Missing inputs (owner or supplier must provide; none were invented)

1. Supplier quote per tin with components (fleece, filler, flavor, caffeine, tin, lid, label, labor, testing), price breaks, MOQ per SKU and per flavor, tooling and setup, sample policy.
2. Supplier payment terms: deposit %, balance timing, lead time for first and repeat runs, who pays inbound freight.
3. Shipping: tin weight and packed weight, 3PL rate card (pick-pack, storage, receiving), carrier rates for 1 to 4 tins, whether adult signature is required (counsel).
4. Owner's wholesale discount off retail, wholesale payment terms, minimum wholesale order, whether wholesale goes through a marketplace such as Faire.
5. Shopify plan fee, store theme and app costs; chosen age-verification app and its price.
6. Legal estimates: trademark clearance and filing for Delphine, regulatory counsel, label review; accountant fees; testing/COA; packaging design. No sourced figure exists for any of these.
7. Insurance quotes (product liability and recall) from a broker; processor underwriting result and any reserve or higher rate.
8. Conversion rate, real CAC, first-order tin mix, subscription take-rate, real churn, real refund rate. Processor payout timing.
9. Owner decisions: final retail price ladder, shipping threshold, healthcare-discount percentage, minimum age.

## 3. Tables (all produced by the script; formulas shown under each)

Core formula: contribution = AOV - tins x COGS - (2.9% x AOV + $0.30) - 2% x AOV - shipping - pick-pack - adult signature. Gross margin = (price - COGS) / price. Gross margin is before fees, shipping and pick-pack; contribution is after them and before CAC and fixed costs.

**1a. COGS components (every component listed; only the active is derivable)**

| Component | Per tin | Per pouch (20/tin) | Status |
|---|---|---|---|
| Caffeine active (25 mg x 20 = 0.5 g/tin at $455/kg reagent price) | $0.23 | $0.01 | SRC arithmetic, upper bound (reagent, not bulk food grade) |
| Fleece/pouch material, filler, sweetener, flavor | MISSING | MISSING | needs supplier quote |
| Tin, lid, label, insert, case packing | MISSING | MISSING | needs supplier quote |
| Labor, machine time, QC/testing, supplier margin | MISSING | MISSING | needs supplier quote |
| Inbound freight, duties (if imported), tooling/setup | MISSING | MISSING | needs supplier quote |
| Landed COGS scenario (all components combined) | $1.50 | $0.07 | ASM placeholder, not a quote (scenario $1.50) |
| Landed COGS scenario (all components combined) | $2.50 | $0.12 | ASM placeholder, not a quote (scenario $2.50) |
| Landed COGS scenario (all components combined) | $3.50 | $0.17 | ASM placeholder, not a quote (scenario $3.50) |


**1b. Fully loaded cost per order, per tin and per pouch (free shipping, ladder A prices, no CAC, no adult signature)**

Formula: contribution = AOV - tins x COGS - (2.9% x AOV + 0.30) - 2% x AOV - shipping - pick-pack. Cost per tin = total cost / tins; per pouch = per tin / 20.

| Order | COGS/tin (ASM) | Ship cost (SRC-U) | AOV | COGS | Card fee 2.9%+$0.30 | Refund 2% (ASM) | Shipping | Pick-pack $2.50 (ASM) | Total cost | Cost per tin | Cost per pouch | Contribution |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 tin(s) @ $8.99 | $1.50 | $5.50 | $8.99 | $1.50 | $0.56 | $0.18 | $5.50 | $2.50 | $10.24 | $10.24 | $0.51 | -$1.25 |
| 1 tin(s) @ $8.99 | $1.50 | $8.00 | $8.99 | $1.50 | $0.56 | $0.18 | $8.00 | $2.50 | $12.74 | $12.74 | $0.64 | -$3.75 |
| 1 tin(s) @ $8.99 | $2.50 | $5.50 | $8.99 | $2.50 | $0.56 | $0.18 | $5.50 | $2.50 | $11.24 | $11.24 | $0.56 | -$2.25 |
| 1 tin(s) @ $8.99 | $2.50 | $8.00 | $8.99 | $2.50 | $0.56 | $0.18 | $8.00 | $2.50 | $13.74 | $13.74 | $0.69 | -$4.75 |
| 1 tin(s) @ $8.99 | $3.50 | $5.50 | $8.99 | $3.50 | $0.56 | $0.18 | $5.50 | $2.50 | $12.24 | $12.24 | $0.61 | -$3.25 |
| 1 tin(s) @ $8.99 | $3.50 | $8.00 | $8.99 | $3.50 | $0.56 | $0.18 | $8.00 | $2.50 | $14.74 | $14.74 | $0.74 | -$5.75 |
| 3 tin(s) @ $7.99 | $1.50 | $5.50 | $23.97 | $4.50 | $1.00 | $0.48 | $5.50 | $2.50 | $13.97 | $4.66 | $0.23 | $10.00 |
| 3 tin(s) @ $7.99 | $1.50 | $8.00 | $23.97 | $4.50 | $1.00 | $0.48 | $8.00 | $2.50 | $16.47 | $5.49 | $0.27 | $7.50 |
| 3 tin(s) @ $7.99 | $2.50 | $5.50 | $23.97 | $7.50 | $1.00 | $0.48 | $5.50 | $2.50 | $16.97 | $5.66 | $0.28 | $7.00 |
| 3 tin(s) @ $7.99 | $2.50 | $8.00 | $23.97 | $7.50 | $1.00 | $0.48 | $8.00 | $2.50 | $19.47 | $6.49 | $0.32 | $4.50 |
| 3 tin(s) @ $7.99 | $3.50 | $5.50 | $23.97 | $10.50 | $1.00 | $0.48 | $5.50 | $2.50 | $19.97 | $6.66 | $0.33 | $4.00 |
| 3 tin(s) @ $7.99 | $3.50 | $8.00 | $23.97 | $10.50 | $1.00 | $0.48 | $8.00 | $2.50 | $22.47 | $7.49 | $0.37 | $1.50 |
| 4 tin(s) @ $7.99 | $1.50 | $5.50 | $31.96 | $6.00 | $1.23 | $0.64 | $5.50 | $2.50 | $15.87 | $3.97 | $0.20 | $16.09 |
| 4 tin(s) @ $7.99 | $1.50 | $8.00 | $31.96 | $6.00 | $1.23 | $0.64 | $8.00 | $2.50 | $18.37 | $4.59 | $0.23 | $13.59 |
| 4 tin(s) @ $7.99 | $2.50 | $5.50 | $31.96 | $10.00 | $1.23 | $0.64 | $5.50 | $2.50 | $19.87 | $4.97 | $0.25 | $12.09 |
| 4 tin(s) @ $7.99 | $2.50 | $8.00 | $31.96 | $10.00 | $1.23 | $0.64 | $8.00 | $2.50 | $22.37 | $5.59 | $0.28 | $9.59 |
| 4 tin(s) @ $7.99 | $3.50 | $5.50 | $31.96 | $14.00 | $1.23 | $0.64 | $5.50 | $2.50 | $23.87 | $5.97 | $0.30 | $8.09 |
| 4 tin(s) @ $7.99 | $3.50 | $8.00 | $31.96 | $14.00 | $1.23 | $0.64 | $8.00 | $2.50 | $26.37 | $6.59 | $0.33 | $5.59 |


**2a. Product gross margin per tin at three retail prices (price - COGS; before fees, shipping, pick-pack)**

| Retail price/tin | COGS/tin (ASM) | Gross profit/tin | Gross margin % | Gross profit/pouch |
|---|---|---|---|---|
| $8.99 | $1.50 | $7.49 | 83.3% | $0.37 |
| $8.99 | $2.50 | $6.49 | 72.2% | $0.32 |
| $8.99 | $3.50 | $5.49 | 61.1% | $0.27 |
| $9.99 | $1.50 | $8.49 | 85.0% | $0.42 |
| $9.99 | $2.50 | $7.49 | 75.0% | $0.37 |
| $9.99 | $3.50 | $6.49 | 65.0% | $0.32 |
| $10.99 | $1.50 | $9.49 | 86.4% | $0.47 |
| $10.99 | $2.50 | $8.49 | 77.3% | $0.42 |
| $10.99 | $3.50 | $7.49 | 68.2% | $0.37 |


**2b. DTC contribution at three flat retail prices (COGS $2.50 ASM, free shipping, 2% refunds, $2.50 pick-pack, no CAC)**

| Retail price/tin | Tins in order | Ship cost | AOV | Contribution/order | Contribution % of AOV | Contribution/tin |
|---|---|---|---|---|---|---|
| $8.99 | 1 | $5.50 | $8.99 | -$2.25 | -25.0% | -$2.25 |
| $8.99 | 1 | $8.00 | $8.99 | -$4.75 | -52.8% | -$4.75 |
| $8.99 | 3 | $5.50 | $26.97 | $9.85 | 36.5% | $3.28 |
| $8.99 | 3 | $8.00 | $26.97 | $7.35 | 27.2% | $2.45 |
| $8.99 | 4 | $5.50 | $35.96 | $15.90 | 44.2% | $3.97 |
| $8.99 | 4 | $8.00 | $35.96 | $13.40 | 37.3% | $3.35 |
| $9.99 | 1 | $5.50 | $9.99 | -$1.30 | -13.0% | -$1.30 |
| $9.99 | 1 | $8.00 | $9.99 | -$3.80 | -38.0% | -$3.80 |
| $9.99 | 3 | $5.50 | $29.97 | $12.70 | 42.4% | $4.23 |
| $9.99 | 3 | $8.00 | $29.97 | $10.20 | 34.0% | $3.40 |
| $9.99 | 4 | $5.50 | $39.96 | $19.70 | 49.3% | $4.93 |
| $9.99 | 4 | $8.00 | $39.96 | $17.20 | 43.0% | $4.30 |
| $10.99 | 1 | $5.50 | $10.99 | -$0.35 | -3.2% | -$0.35 |
| $10.99 | 1 | $8.00 | $10.99 | -$2.85 | -25.9% | -$2.85 |
| $10.99 | 3 | $5.50 | $32.97 | $15.55 | 47.2% | $5.18 |
| $10.99 | 3 | $8.00 | $32.97 | $13.05 | 39.6% | $4.35 |
| $10.99 | 4 | $5.50 | $43.96 | $23.51 | 53.5% | $5.88 |
| $10.99 | 4 | $8.00 | $43.96 | $21.01 | 47.8% | $5.25 |


**2c. Subscription reorder (4 tins, 15% subscription discount SRC-U, ship $5.50) contribution**

| Retail price/tin | COGS/tin | AOV after discount | Contribution | % of AOV |
|---|---|---|---|---|
| $8.99 | $1.50 | $30.57 | $14.77 | 48.3% |
| $8.99 | $2.50 | $30.57 | $10.77 | 35.2% |
| $8.99 | $3.50 | $30.57 | $6.77 | 22.1% |
| $9.99 | $1.50 | $33.97 | $18.00 | 53.0% |
| $9.99 | $2.50 | $33.97 | $14.00 | 41.2% |
| $9.99 | $3.50 | $33.97 | $10.00 | 29.4% |
| $10.99 | $1.50 | $37.37 | $21.24 | 56.8% |
| $10.99 | $2.50 | $37.37 | $17.24 | 46.1% |
| $10.99 | $3.50 | $37.37 | $13.24 | 35.4% |


**2d. Wholesale margin per tin (owner's wholesale discount is MISSING; three scenarios; freight $0.25/tin ASM; no card fee, no CAC; payment terms unknown)**

| Retail price/tin | Discount off retail | Wholesale net/tin | COGS/tin | Contribution/tin | % of wholesale net |
|---|---|---|---|---|---|
| $8.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $5.99 | $1.50 | $4.24 | 70.8% |
| $8.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $5.99 | $2.50 | $3.24 | 54.1% |
| $8.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $5.99 | $3.50 | $2.24 | 37.4% |
| $8.99 | 40% off retail (ASM) | $5.39 | $1.50 | $3.64 | 67.6% |
| $8.99 | 40% off retail (ASM) | $5.39 | $2.50 | $2.64 | 49.0% |
| $8.99 | 40% off retail (ASM) | $5.39 | $3.50 | $1.64 | 30.5% |
| $8.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $4.50 | $1.50 | $2.75 | 61.1% |
| $8.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $4.50 | $2.50 | $1.75 | 38.8% |
| $8.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $4.50 | $3.50 | $0.75 | 16.6% |
| $9.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $6.66 | $1.50 | $4.91 | 73.7% |
| $9.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $6.66 | $2.50 | $3.91 | 58.7% |
| $9.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $6.66 | $3.50 | $2.91 | 43.7% |
| $9.99 | 40% off retail (ASM) | $5.99 | $1.50 | $4.24 | 70.8% |
| $9.99 | 40% off retail (ASM) | $5.99 | $2.50 | $3.24 | 54.1% |
| $9.99 | 40% off retail (ASM) | $5.99 | $3.50 | $2.24 | 37.4% |
| $9.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $5.00 | $1.50 | $3.25 | 65.0% |
| $9.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $5.00 | $2.50 | $2.25 | 44.9% |
| $9.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $5.00 | $3.50 | $1.25 | 24.9% |
| $10.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $7.33 | $1.50 | $5.58 | 76.1% |
| $10.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $7.33 | $2.50 | $4.58 | 62.5% |
| $10.99 | 33.3% off retail (=50% retailer markup on cost; Clarivate consultant, UNVERIFIED) | $7.33 | $3.50 | $3.58 | 48.8% |
| $10.99 | 40% off retail (ASM) | $6.59 | $1.50 | $4.84 | 73.5% |
| $10.99 | 40% off retail (ASM) | $6.59 | $2.50 | $3.84 | 58.3% |
| $10.99 | 40% off retail (ASM) | $6.59 | $3.50 | $2.84 | 43.1% |
| $10.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $5.50 | $1.50 | $3.75 | 68.2% |
| $10.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $5.50 | $2.50 | $2.75 | 50.0% |
| $10.99 | 50% off retail (=keystone 100% markup; common, UNVERIFIED) | $5.50 | $3.50 | $1.75 | 31.8% |


**2e. Re-verification of carried-forward conclusions (ladder A, COGS $2.50, ship $5.50 unless stated)**

Check: the threshold and adult-signature columns reproduce `nurse_offer_cm.csv` row by row (asserted in the script). Result: 1 tin loses $2.25 under free shipping, 3-4 tins is the floor, and a $10 adult-signature fee turns 1-3 tin free-shipping orders negative.

| Tins | Price/tin | CM free ship | CM worst case (COGS 3.50, ship 8.00) | CM free ship + $10 adult sig | CM with $4.99 ship fee under $35 | Same + $10 adult sig | Positive (free ship)? |
|---|---|---|---|---|---|---|---|
| 1 | $8.99 | -$2.25 | -$5.75 | -$12.25 | $2.49 | -$7.51 | NO |
| 2 | $8.49 | $2.85 | -$1.65 | -$7.15 | $7.59 | -$2.41 | yes |
| 3 | $7.99 | $7.00 | $1.50 | -$3.00 | $11.74 | $1.74 | yes |
| 4 | $7.99 | $12.09 | $5.59 | $2.09 | $16.84 | $6.84 | yes |
| 5 | $7.49 | $14.81 | $7.31 | $4.81 | $14.81 | $4.81 | yes |


**2f. Healthcare discount: replace vs stack with the 15% subscription discount**

Result: stacking 15% + 15% takes the 4-tin reorder from $12.28 to $8.41, so the healthcare discount should replace, not stack.

| Tins | Healthcare discount | First-order CM | Reorder CM (replace: larger of the two) | Reorder CM (stacked) | CM lost by stacking |
|---|---|---|---|---|---|
| 3 | 10.0% | $9.46 | $8.32 | $6.38 | $1.94 |
| 3 | 15.0% | $8.32 | $8.32 | $5.42 | $2.91 |
| 3 | 20.0% | $7.18 | $7.18 | $4.45 | $2.74 |
| 4 | 10.0% | $13.80 | $12.28 | $9.70 | $2.58 |
| 4 | 15.0% | $12.28 | $12.28 | $8.41 | $3.88 |
| 4 | 20.0% | $10.76 | $10.76 | $7.11 | $3.65 |


**3a. Fixed costs (placeholders; MISSING items are not modelled)**

| Fixed cost | Low | High | Source / status |
|---|---|---|---|
| Product liability insurance (annual) | $700.00 | $4,500.00 | SRC-U broker blogs: unit_economics.md s3 (Assureful, Insurance Canopy) |
| Age-verification Shopify app (annual) | $24.00 | $359.88 | SRC-U app listing prices, $2/mo to $29.99/mo: workplace_regulatory_claims.md l.119; vendor choice not made |
| Shopify plan / store software (annual) | MISSING | MISSING | plan fee not recorded in any research file; owner to supply |
| Trademark clearance + filing, legal/label review (one-time) | MISSING | MISSING | no sourced figure; attorney quote needed |
| Regulatory counsel, accountant, bookkeeping | MISSING | MISSING | no sourced figure |
| Product testing / COA, label design, tin tooling, photography | MISSING | MISSING | no sourced figure; supplier quote |
| Sourced subtotal (annual) | $724.00 | $4,859.88 | lower bound only; true fixed costs are higher |


**3b. Break-even units and revenue (COGS $2.50 ASM; DTC = 4-tin free-ship order, ship $5.50, before CAC; wholesale = 50% off retail)**

Formulas: break-even tins = fixed costs / contribution per tin; break-even revenue = tins x revenue per tin (retail price for DTC, 50% of retail for wholesale). Checked by multiplying back.

| Retail price/tin | Fixed-cost case | Fixed costs | DTC contribution/tin | DTC break-even tins | DTC break-even revenue | Wholesale contribution/tin | Wholesale break-even tins | Wholesale break-even revenue |
|---|---|---|---|---|---|---|---|---|
| $8.99 | sourced subtotal, low | $724.00 | $3.97 | 182 | $1,637.63 | $1.75 | 415 | $1,864.97 |
| $8.99 | sourced subtotal, high | $4,859.88 | $3.97 | 1,223 | $10,992.69 | $1.75 | 2,785 | $12,518.72 |
| $8.99 | per extra $1,000 of MISSING fixed costs | $1,000.00 | $3.97 | 252 | $2,261.93 | $1.75 | 573 | $2,575.93 |
| $9.99 | sourced subtotal, low | $724.00 | $4.93 | 147 | $1,468.43 | $2.25 | 322 | $1,610.86 |
| $9.99 | sourced subtotal, high | $4,859.88 | $4.93 | 987 | $9,856.93 | $2.25 | 2,165 | $10,812.96 |
| $9.99 | per extra $1,000 of MISSING fixed costs | $1,000.00 | $4.93 | 203 | $2,028.22 | $2.25 | 445 | $2,224.94 |
| $10.99 | sourced subtotal, low | $724.00 | $5.88 | 123 | $1,354.00 | $2.75 | 264 | $1,449.32 |
| $10.99 | sourced subtotal, high | $4,859.88 | $5.88 | 827 | $9,088.77 | $2.75 | 1,770 | $9,728.61 |
| $10.99 | per extra $1,000 of MISSING fixed costs | $1,000.00 | $5.88 | 170 | $1,870.16 | $2.75 | 364 | $2,001.82 |


**3c. First-order contribution after CAC (4 tins, COGS $2.50, ship $5.50). CAC values are report thresholds, not data**

| Retail price/tin | CAC | First-order contribution | After CAC | Break-even on low sourced fixed costs |
|---|---|---|---|---|
| $8.99 | $25.00 | $15.90 | -$9.10 | n/a (never positive on first order) |
| $8.99 | $40.00 | $15.90 | -$24.10 | n/a (never positive on first order) |
| $9.99 | $25.00 | $19.70 | -$5.30 | n/a (never positive on first order) |
| $9.99 | $40.00 | $19.70 | -$20.30 | n/a (never positive on first order) |
| $10.99 | $25.00 | $23.51 | -$1.49 | n/a (never positive on first order) |
| $10.99 | $40.00 | $23.51 | -$16.49 | n/a (never positive on first order) |


**4a. Peak funding need for the first three POs (COGS $2.50 ASM; lead time 2 months ASM; reorder when stock = lead-time demand; DTC only; excludes marketing, MISSING fixed costs, inventory not sold)**

No supplier terms exist: deposit %, balance timing, lead time, MOQ and payout timing are all scenarios. Net receipt per tin is the 4-tin ladder-A contribution plus COGS ($7.99 tin, ship $5.50), so shipping, fees, refunds and pick-pack are paid out of each sale. Marketing is excluded: at a $25 CAC (report threshold) every 100 new customers needs $2,500 cash before any reorder revenue.

| PO size | Deposit at order | Tins sold/month (ASM) | One PO at COGS | Peak cumulative cash need | Peak occurs | PO timing (placed -> arrives) |
|---|---|---|---|---|---|---|
| 5,000 tins (ASM, illustrative small run) | 30% | 500 | $12,500.00 | $10,462.25 | month 2 | PO1: m0->m2; PO2: m10->m12; PO3: m20->m22 |
| 5,000 tins (ASM, illustrative small run) | 30% | 1,500 | $12,500.00 | $4,938.76 | month 2 | PO1: m0->m2; PO2: m4->m6; PO3: m8->m10 |
| 5,000 tins (ASM, illustrative small run) | 30% | 3,000 | $12,500.00 | $8,224.00 | month 1 | PO1: m0->m2; PO2: m1->m3; PO3: m4->m6 |
| 5,000 tins (ASM, illustrative small run) | 50% | 500 | $12,500.00 | $10,462.25 | month 2 | PO1: m0->m2; PO2: m10->m12; PO3: m20->m22 |
| 5,000 tins (ASM, illustrative small run) | 50% | 1,500 | $12,500.00 | $6,974.00 | month 0 | PO1: m0->m2; PO2: m4->m6; PO3: m8->m10 |
| 5,000 tins (ASM, illustrative small run) | 50% | 3,000 | $12,500.00 | $13,224.00 | month 1 | PO1: m0->m2; PO2: m1->m3; PO3: m4->m6 |
| 5,000 tins (ASM, illustrative small run) | 100% | 500 | $12,500.00 | $13,224.00 | month 0 | PO1: m0->m2; PO2: m10->m12; PO3: m20->m22 |
| 5,000 tins (ASM, illustrative small run) | 100% | 1,500 | $12,500.00 | $13,224.00 | month 0 | PO1: m0->m2; PO2: m4->m6; PO3: m8->m10 |
| 5,000 tins (ASM, illustrative small run) | 100% | 3,000 | $12,500.00 | $25,724.00 | month 1 | PO1: m0->m2; PO2: m1->m3; PO3: m4->m6 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 30% | 500 | $62,500.00 | $60,462.25 | month 2 | PO1: m0->m2; PO2: m50->m52; PO3: m100->m102 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 30% | 1,500 | $62,500.00 | $54,938.76 | month 2 | PO1: m0->m2; PO2: m17->m19; PO3: m34->m36 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 30% | 3,000 | $62,500.00 | $46,653.53 | month 2 | PO1: m0->m2; PO2: m9->m11; PO3: m18->m20 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 50% | 500 | $62,500.00 | $60,462.26 | month 2 | PO1: m0->m2; PO2: m50->m52; PO3: m100->m102 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 50% | 1,500 | $62,500.00 | $54,938.76 | month 2 | PO1: m0->m2; PO2: m17->m19; PO3: m34->m36 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 50% | 3,000 | $62,500.00 | $46,653.53 | month 2 | PO1: m0->m2; PO2: m9->m11; PO3: m18->m20 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 100% | 500 | $62,500.00 | $63,224.00 | month 0 | PO1: m0->m2; PO2: m50->m52; PO3: m100->m102 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 100% | 1,500 | $62,500.00 | $63,224.00 | month 0 | PO1: m0->m2; PO2: m17->m19; PO3: m34->m36 |
| 25,000 tins (Daily Mfg self-reported MOQ, UNVERIFIED) | 100% | 3,000 | $62,500.00 | $63,224.00 | month 0 | PO1: m0->m2; PO2: m9->m11; PO3: m18->m20 |


**4b. COGS sensitivity of peak cash need (25,000-tin PO, 50% deposit, 1,500 tins/month)**

| COGS/tin (ASM) | One 25,000-tin PO | Peak cash need | Peak occurs |
|---|---|---|---|
| $1.50 | $37,500.00 | $29,938.76 | month 2 |
| $2.50 | $62,500.00 | $54,938.76 | month 2 |
| $3.50 | $87,500.00 | $79,938.76 | month 2 |


**4c. Monthly cash, central scenario (25,000 tins, 50% deposit, COGS $2.50, 1,500 tins/month, 2-month lead). Negative = cumulative cash below start**

| Month | Events | Cash out | Cash in (sales) | Cumulative cash | Tins on hand |
|---|---|---|---|---|---|
| 0 | PO1 placed, deposit paid | $31,250.00 | $0.00 | -$31,974.00 | 0 |
| 2 | PO1 arrives, balance paid | $31,250.00 | $8,285.24 | -$54,938.76 | 23,500 |
| 6 |  | $0.00 | $8,285.24 | -$21,797.82 | 17,500 |
| 12 |  | $0.00 | $8,285.24 | $27,913.59 | 8,500 |
| 17 | PO2 placed, deposit paid | $31,250.00 | $8,285.24 | $38,089.76 | 1,000 |
| 18 |  | $0.00 | $5,523.49 | $43,613.25 | 0 |
| 19 | PO2 arrives, balance paid | $31,250.00 | $8,285.24 | $20,648.49 | 23,500 |
| 24 |  | $0.00 | $8,285.24 | $62,074.66 | 16,000 |
| 30 |  | $0.00 | $8,285.24 | $111,786.07 | 7,000 |
| 34 | PO3 placed, deposit paid | $31,250.00 | $8,285.24 | $113,677.01 | 1,000 |
| 36 | PO3 arrives, balance paid | $31,250.00 | $8,285.24 | $96,235.74 | 23,500 |
| 42 |  | $0.00 | $8,285.24 | $145,947.15 | 14,500 |
| 48 |  | $0.00 | $8,285.24 | $195,658.55 | 5,500 |
| 52 |  | $0.00 | $5,523.49 | $226,037.75 | 0 |

Gap between first supplier payment and first revenue in this scenario: month 0 deposit to month 2 receipt of stock, then sales; about 6 weeks per Daily Manufacturing's self-reported lead time (UNVERIFIED) plus MISSING transit, label/artwork and compliance holds. Payout timing from the processor is MISSING (not recorded in sources).


**5a. SCENARIO, NOT A FORECAST: nurse pattern, 3 shifts/week = 13.0 shifts/month, pouches only on shift days (ASM)**

Formulas: pouches/month = per-shift x 13.0; tins/month = pouches/20; days between orders = tins in bundle x 20 / pouches per month x 30; revenue/month = tins/month x $7.99 x 0.85. Churn 8%/month (SRC-U), survival (1-0.08)^completed months. Reorder cadence is where unit counts and cash come from, not a target for customers. Usage is the customer's own choice; Delphine copy must not promote it.

| Pouches per 12-h shift | Pouches/month | Tins/month | A 20-pouch tin lasts | Reorder cadence: 3-tin / 4-tin bundle | Subscriber revenue/month (15% sub disc.) | Contribution/month | Expected 12-month revenue (8% monthly churn, 4-tin bundle) | Expected 12-month contribution |
|---|---|---|---|---|---|---|---|---|
| 3 per shift (75 mg per shift) | 39 | 1.95 | 6.7 shifts = 16 calendar days | 46 / 62 days | $13.24 | $3.67 | $116.63 | $35.58 |
| 5 per shift (125 mg per shift) | 65 | 3.25 | 4.0 shifts = 9 calendar days | 28 / 37 days | $22.07 | $6.12 | $189.81 | $55.88 |
| 8 per shift (200 mg per shift) | 104 | 5.20 | 2.5 shifts = 6 calendar days | 17 / 23 days | $35.32 | $9.80 | $297.14 | $85.64 |


**5b. SCENARIO, NOT A FORECAST: same levels as pouches per calendar day (every day), for contrast**

400 mg/day comes from the trade explainer in CLAUDE.md (tobaccoinsider.com, not FDA); counsel decides how daily totals are shown. Higher usage means faster revenue only mechanically; none of these is a goal, a target or customer-facing copy.

| Pouches per day | Pouches/month | Tins/month | A tin lasts | 4-tin bundle lasts | Subscriber revenue/month | Share of the 400 mg/day FDA reference figure |
|---|---|---|---|---|---|---|
| 3 per calendar day (75 mg/day) | 90 | 4.50 | 6.7 days | 27 days | $30.56 | 18.8% |
| 5 per calendar day (125 mg/day) | 150 | 7.50 | 4.0 days | 16 days | $50.94 | 31.2% |
| 8 per calendar day (200 mg/day) | 240 | 12.00 | 2.5 days | 10 days | $81.50 | 50.0% |


**6a. Sensitivity of 4-tin first-order contribution (ladder A $7.99/tin, COGS $2.50, ship $5.50, free shipping; base = $12.09 on $31.96 AOV)**

Each variable moved alone by -20%, -10%, +10%, +20%. Positive change in price improves contribution; positive change in the others reduces it.

| Variable | Change | Contribution | Change vs base | Contribution % of AOV |
|---|---|---|---|---|
| Supplier price (COGS/tin) | -20% | $14.09 | $2.00 | 44.1% |
| Supplier price (COGS/tin) | -10% | $13.09 | $1.00 | 41.0% |
| Supplier price (COGS/tin) | +10% | $11.09 | -$1.00 | 34.7% |
| Supplier price (COGS/tin) | +20% | $10.09 | -$2.00 | 31.6% |
| Shipping cost | -20% | $13.19 | $1.10 | 41.3% |
| Shipping cost | -10% | $12.64 | $0.55 | 39.6% |
| Shipping cost | +10% | $11.54 | -$0.55 | 36.1% |
| Shipping cost | +20% | $10.99 | -$1.10 | 34.4% |
| Processor fees (2.9% and $0.30 scaled together) | -20% | $12.34 | $0.25 | 38.6% |
| Processor fees (2.9% and $0.30 scaled together) | -10% | $12.22 | $0.12 | 38.2% |
| Processor fees (2.9% and $0.30 scaled together) | +10% | $11.97 | -$0.12 | 37.5% |
| Processor fees (2.9% and $0.30 scaled together) | +20% | $11.85 | -$0.25 | 37.1% |
| Returns/refunds rate (2% scaled) | -20% | $12.22 | $0.13 | 38.2% |
| Returns/refunds rate (2% scaled) | -10% | $12.16 | $0.06 | 38.0% |
| Returns/refunds rate (2% scaled) | +10% | $12.03 | -$0.06 | 37.6% |
| Returns/refunds rate (2% scaled) | +20% | $11.97 | -$0.13 | 37.4% |
| Pick-pack (ASM) | -20% | $12.59 | $0.50 | 39.4% |
| Pick-pack (ASM) | -10% | $12.34 | $0.25 | 38.6% |
| Pick-pack (ASM) | +10% | $11.84 | -$0.25 | 37.1% |
| Pick-pack (ASM) | +20% | $11.59 | -$0.50 | 36.3% |
| Retail price/tin | -20% | $6.02 | -$6.08 | 23.5% |
| Retail price/tin | -10% | $9.05 | -$3.04 | 31.5% |
| Retail price/tin | +10% | $15.13 | $3.04 | 43.0% |
| Retail price/tin | +20% | $18.17 | $6.08 | 47.4% |


**6b. Returns rate beyond +/-20% (the 2% base has no benchmark behind it; +/-20% of 2% is only 0.4 points)**

A single lost dispute also costs the $15 Stripe dispute fee (SRC) on top of the order value.

| Refund + chargeback rate of revenue | Contribution | Change vs base |
|---|---|---|
| 1.0% | $12.41 | $0.32 |
| 2.0% | $12.09 | $0.00 |
| 4.0% | $11.45 | -$0.64 |
| 5.0% | $11.14 | -$0.96 |
| 10.0% | $9.54 | -$2.56 |


**7. Assumptions ranked by how much they move 4-tin first-order contribution (largest swing first)**

| Rank | Assumption and range tested | Swing in contribution | Relative to base ($12.09) | Input status |
|---|---|---|---|---|
| 1 | Tins per order: 1 tin vs 4 tins (free shipping) | $14.34 | 119% of base contribution | ASM mix, no data |
| 2 | Adult signature on/off ($10) | $10.00 | 83% of base contribution | SRC-U fee; legal need unknown |
| 3 | Supplier price: COGS $1.50 to $3.50 per tin | $8.00 | 66% of base contribution | ASM, no quote |
| 4 | Retail price per tin +/-10% ($7.99 base) | $6.08 | 50% of base contribution | ASM ladder |
| 5 | Shipping cost $5.50 vs $8.00 | $2.50 | 21% of base contribution | SRC-U |
| 6 | Pick-pack/3PL $1.50 to $3.50 (+/-$1) | $2.00 | 17% of base contribution | ASM |
| 7 | Refund rate 0% to 5% | $1.60 | 13% of base contribution | ASM |
| 8 | Processor fees +/-20% | $0.49 | 4% of base contribution | SRC |


**7b. Same ranking restricted to uniform +/-20% moves**

| Rank | Variable | Swing (-20% to +20%) | Change at -20% | Change at +20% |
|---|---|---|---|---|
| 1 | Retail price/tin | $12.16 | -$6.08 | $6.08 |
| 2 | Supplier price (COGS/tin) | $4.00 | $2.00 | -$2.00 |
| 3 | Shipping cost | $2.20 | $1.10 | -$1.10 |
| 4 | Pick-pack (ASM) | $1.00 | $0.50 | -$0.50 |
| 5 | Processor fees (2.9% and $0.30 scaled together) | $0.49 | $0.25 | -$0.25 |
| 6 | Returns/refunds rate (2% scaled) | $0.26 | $0.13 | -$0.13 |


**8. Go/no-go: what must be true**

This is a model screen, not an approval. Nothing here clears the compliance gate in CLAUDE.md.

| Condition | Modelled result | Threshold / what it needs | Status |
|---|---|---|---|
| Blended first-order contribution is positive with 70% of orders at 3-4 tins and 30% at 1 tin | mix contribution at COGS $2.50 = $6.01 | max COGS/tin = $4.68 | PASS at ASM inputs |
| The same mix with 50% of orders at 1 tin | $3.65 | max COGS/tin = $4.12 | PASS |
| COGS near $2.50 per tin (report threshold) | needs supplier quote | 4-tin order breaks even on CM at COGS $5.52; first-order contribution never reaches a $25 CAC (even $0 COGS gives $22.09) | UNKNOWN until quote |
| 12-month contribution per customer covers a $25 CAC (4-tin bundle, 3 pouches/shift scenario, 8% churn) | $35.58 at COGS $2.50 | max COGS/tin = $3.14 | PASS at ASM inputs |
| Same at a $40 CAC | $35.58 | max COGS/tin = $2.23 | FAIL (needs higher usage or price; usage is not a lever to promote) |
| Shipping near $5.50 per order | SRC-U pre 2026-07-12; retail zone 1 is $7.90 | 4-tin CM at ship $8.00 = $9.59; 3-tin = $4.50 | UNKNOWN until 3PL quote and tin weight |
| No adult signature on delivery | 4-tin CM with $10 signature = $2.09; 3-tin = -$3.00 | needs counsel: is a signature required? | OPEN (counsel) |
| Healthcare discount replaces, never stacks | 4-tin reorder $12.28 replaced vs $8.41 stacked (incl. $4.99 customer shipping under $35) | policy decision | OWNER DECISION |
| Disputes stay under card-network thresholds (Visa monitoring reported 0.9% to 1.5%, conflicting) | each dispute costs $15 plus the order | processor underwriting must accept the category | UNKNOWN |
| Counsel clearances: trademark (Delphine), regulatory category, label, age policy, adult-signature, state laws | none recorded in decisions.md | gate | NOT CLEARED: no inventory spend |
| Supplier terms: MOQ, deposit, lead time, price breaks | none exist | one 25,000-tin PO is $37,500.00 to $87,500.00 at scenario COGS | UNKNOWN until RFQ (not sent) |


Self-checks passed (asserted in script): unit cost waterfall 1t cogs1.5 ship5.5; unit cost waterfall 1t cogs1.5 ship8.0; unit cost waterfall 1t cogs2.5 ship5.5; unit cost waterfall 1t cogs2.5 ship8.0; unit cost waterfall 1t cogs3.5 ship5.5; unit cost waterfall 1t cogs3.5 ship8.0; ... total 48 checks, all within tolerance.

## 4. Assumptions that matter most (ranked by movement in 4-tin first-order contribution)

See table 7 above. In order: (1) first-order tin mix (1 tin vs 4 tins moves contribution by $14.34, more than the whole 4-tin contribution); (2) whether an adult signature is required ($10); (3) supplier price ($8.00 across $1.50 to $3.50; $4.00 for +/-20%); (4) retail price per tin ($6.08 for +/-10%); (5) shipping cost and tin weight ($2.50 between $5.50 and $8.00); (6) 3PL pick-pack; (7) refund rate; (8) processor fees. Processor fees and the 2% refund rate barely move margin at +/-20% (about $0.25 and $0.13 each way); the risk in returns is a chargeback ratio that threatens the merchant account, not the margin arithmetic. Four of the top five are ASM or SRC-U inputs with no quote behind them.

## 5. For a professional

Accountant:
- Entity choice (LLC vs S corp or other), owner pay, and when to form it relative to the first supplier deposit, trademark filing and insurance application.
- Sales tax on dietary supplements and on food or "candy"-type goods by state (taxability may depend on whether a pouch is classed as a supplement or conventional food, which is itself an open question for counsel), economic nexus thresholds for a Shopify seller, whether Shopify tax tools suffice, and wholesale resale-certificate handling.
- Inventory costing (landed cost, deposits as prepaid inventory), treatment of the trademark and legal costs, and cash-basis vs accrual.
- Whether the healthcare discount, gift bundles and sampling have tax or deductibility implications.
- Which of the placeholders in section 3a to replace first with real quotes.

Insurance broker:
- Product liability limits and cost for an ingestible oral caffeine pouch; the $700 to $4,500 range is from broker blogs only. Whether the carrier will cover a nicotine-look-alike product and sales to a workplace audience; recall/contamination cover; whether the co-packer's own cover and vendor-endorsement can be used; claims-made vs occurrence; wholesale buyers' requirements for certificates of insurance.

Payment processor underwriting:
- Whether Shopify Payments, Stripe or another processor accepts caffeine pouches (the research found a case of a zero-nicotine vape seller losing Shopify Payments and Stripe; not conclusive for caffeine). Reserves, rates above 2.9% + $0.30, adult-signature or age-verification expectations, chargeback thresholds (Visa 0.9% to 1.5% reported, conflicting), and what happens to payouts if the category is flagged.

Also for counsel (feeds the model): whether adult signature on delivery is required; regulatory category (supplement vs conventional food); the Daily Manufacturing warning-letter question.

## 6. Decisions needed

1. Choose a supplier-quote path: approve sending the draft RFQ (not sent) after the compliance gate, asking for per-tin component costs, MOQ, deposit, lead time and price breaks. Until then COGS stays a $1.50 to $3.50 placeholder.
2. Set the first-order bundle floor and free-shipping line (model: 3 to 4 tins, 1 tin loses $2.25 under free shipping) and the retail price per tin ($8.99, $9.99 or $10.99 scenarios).
3. Set the wholesale discount off retail (model: 33.3%, 40% or 50%; at 50% off $8.99 and COGS $2.50 the brand keeps $1.75 a tin).
4. Confirm the healthcare discount replaces, and does not stack with, the 15% subscription discount (stacking cuts the 4-tin reorder from $12.28 to $8.41).
5. Counsel to say whether adult signature on delivery is required (it takes $10 off every parcel).
6. Provide or approve the missing fixed-cost inputs: Shopify plan, age-verification app, trademark and legal estimates, insurance quotes.
7. Set a spending limit for the first PO and confirm no deposit before the compliance gate is cleared (a 25,000-tin PO is $37,500 to $87,500 at scenario COGS).
8. Treat CAC around $25 as a hard ceiling for any paid test (12-month contribution per customer is about $35.58 in the lowest-use scenario; $40 CAC fails).
