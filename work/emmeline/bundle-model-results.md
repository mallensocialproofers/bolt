# Emmeline eye cream + face mist: bundle model results (2026-10-27)

Script: `bundle_model.py` (rerun with `python3 bundle_model.py`; writes `bundle_model_base.csv` and `bundle_model_grid.csv`, 2,916 scenario rows; asserts the waterfall, a hand-checked cell, and re-summed blends). This is a scenario screen, not a forecast and not evidence the business works: there is no supplier quote, no conversion data and no CAC data.

## Input tags
- **SRC** (read from the owner's screenshot of selfnamed.com Face Care, 2026-10-27): 15 ml eye creams $5.08 to $7.19 (pink badge) and $9.10 to $13.60 (black); 100 ml Microbiome Prebiotics Face Mist $5.78 (pink badge) and $8.89 after -30% (was $12.70). **Which price applies to a dropshipped order is UNVERIFIED** (the pink badge may be Pro-plan pricing at $29 a month), so three cost tiers are run: A = $5.44 + $5.78; B = $9.10 + $8.89; C = $13.60 + $12.70.
- **SRC-U** (search snippets, unverified): USPS Ground Advantage under 1 lb commercial $5.50 to $8.40 (1 lb $10.67); Shopify/Stripe 2.9% + $0.30; Recharge $0.19 + 1.49% per renewal; retail comparables: Kiehl's eye creams $40 and $60, Augustinus Bader eye cream $205 to $215, Caudalie Beauty Elixir 100 ml $59 (or $42.86), The Inkey List duos $22 to $35.
- **ASM** (assumptions): retail prices, free-shipping line ($60) and $5.95 shipping charge below it, refund rate 3% or 8%, subscription discount 10%, 8-week cadence, retention per cycle 70/80/90%, subscription take rate 15/30/45%, offer mixes, custom label/box cost ($0 or $2.00 per order; not priced on the page), CAC test points $25/$40/$60.
- **Not on the SelfNamed page** (missing inputs): shipping fee to the customer, dropship fee, sample cost, custom label/box cost, who is the MoCRA responsible person.

## Price ladders tested (all ASM, anchored to the comparables above)
| Ladder | Eye cream | Face mist | Duo ("The Pair") | Duo discount vs singles |
|---|---|---|---|---|
| L1 accessible-luxury | $44 | $29 | $62 | 15% |
| L2 luxury | $54 | $34 | $74 | 16% |
| L3 impulse | $38 | $26 | $52 | 19% |

## Base case results (ship $5.50, label/box included, refunds 3%, offer mix 40% eye-only / 10% mist-only / 50% duo, 80% retention per cycle, 30% subscribe)
CM = contribution per order after product, shipping, payment fees and refunds. Subscription renewal = eye cream only at 10% off, free shipping.

| Ladder | Cost tier | Eye-only CM | Mist-only CM | Duo CM | Blended AOV | Blended 1st-order CM | Renewal CM | 12-month value (= break-even CAC) |
|---|---|---|---|---|---|---|---|---|
| L1 | A | $35.76 | $21.31 | $41.32 | $54.48 | $37.10 | $25.24 | $59.45 |
| L1 | B | $32.10 | $18.20 | $34.55 | $54.48 | $31.94 | $21.58 | $51.05 |
| L1 | C | $27.60 | $14.39 | $26.24 | $54.48 | $25.60 | $17.08 | $40.73 |
| L2 | A | $45.17 | $26.01 | $52.61 | $64.98 | $46.98 | $33.58 | $76.71 |
| L2 | B | $41.51 | $22.90 | $45.84 | $64.98 | $41.82 | $29.92 | $68.31 |
| L2 | C | $37.01 | $19.09 | $37.53 | $64.98 | $35.48 | $25.42 | $57.99 |
| L3 | A | $30.12 | $18.48 | $37.51 | $49.75 | $32.65 | $20.24 | $50.57 |
| L3 | B | $26.46 | $15.37 | $30.74 | $49.75 | $27.49 | $16.58 | $42.17 |
| L3 | C | $21.96 | $11.56 | $22.43 | $49.75 | $21.15 | $12.08 | $31.85 |

## The main finding: a deep bundle discount gives most of the mist's profit away
Cost tier B, shipping $5.50, refunds 3%. "Duo minus eye-only" is the extra contribution the mist adds to an order.

| Eye / mist | Sum | Duo discount | Duo price | Duo CM | Duo CM minus eye-only CM |
|---|---|---|---|---|---|
| $44 / $29 | $73 | 0% | $73 | $44.90 | +$12.80 |
| | | 5% | $69 | $41.14 | +$9.04 |
| | | 10% | $66 | $38.32 | +$6.21 |
| | | 15% | $62 | $34.55 | +$2.45 |
| $54 / $34 | $88 | 0% | $88 | $59.02 | +$17.51 |
| | | 5% | $84 | $55.25 | +$13.74 |
| | | 10% | $79 | $50.55 | +$9.04 |
| | | 15% | $75 | $46.78 | +$5.27 |
| $48 / $32 | $80 | 10% | $72 | $43.96 | +$8.10 |

At 15% off, the $44/$29 pair adds only $2.45 over selling the eye cream alone. Bundling raises revenue per order, not profit, unless the discount stays small or is replaced by a non-price incentive (free shipping over a line, a free sample, a gift box). The 20% row at $58 looks better only because it falls under the $60 line and the customer then pays $5.95 shipping, which is an artifact of the free-shipping rule and would likely cost conversion.

Other findings:
- **Free-shipping line:** with a $60 line, an eye-only order at $44 earns $32.10 because the customer pays $5.95; if the line were $40 and it shipped free, it would earn $26.50. A line above the eye cream price pushes people toward the pair.
- **Offer mix:** moving from singles-led (70/10/20) to bundle-led (20/5/75) raises 12-month value only from $50.31 to $52.36 at L1/B, because the pair's margin is thin at a 15% discount.
- **Cost tier:** moving from tier A to tier C cuts duo CM by about $15 to $16 at L1 and L2. The SelfNamed price you actually pay matters more than the mix.
- **Shipping and refunds (L1/B duo CM):** $34.55 at $5.50 shipping and 3% refunds; $28.55 at $8.40 and 8%; $26.28 at the 1 lb rate $10.67 and 8%.
- **Custom label/box:** an extra $2.00 per order lowers duo CM from $34.55 to $32.55 and 12-month value from $51.05 to $49.05.
- **Cost ceiling:** to keep duo CM at 60% of revenue (ship $5.50, refunds 3%), total COGS for eye cream + mist must be at most $15.34 at a $62 price and $19.43 at $74.

## CAC, payback and subscriptions
- **First-order payback on the duo (L1/B, $34.55 CM):** pays back a $25 CAC on the first order (+$9.55), not a $40 CAC (-$5.45) or $60 (-$25.45).
- **12-month value (break-even CAC), L1/B:** $38.60 to $72.90 depending on retention (70% to 90% per cycle) and subscription take rate (15% to 45%). L2/B is higher ($68.31 at 80% retention and 30% take).
- **Usage arithmetic (ASM):** 15 ml at 0.20 ml/day lasts about 75 days and at 0.30 ml/day about 50 days, so an 8-week cadence is a sensible choice, not a measurement. A 100 ml mist at 0.4 ml/day lasts about 250 days, so the mist is a one-time or twice-a-year item, not a subscription item.
- **No conversion or CAC data exists** for luxury eye-care to women overnight nurses. Vendor blogs gave $40 to $120 for supplement DTC and $25 to $80 for skincare; none is specific to this audience or product.

## What "impulse yet luxury" means for price
Search-snippet comparables put mid-luxury eye cream at about $40 to $60 and ultra-luxury at $205 to $215; a 100 ml mist runs about $43 to $59 at the high end and duos from The Inkey List at $22 to $35. A mist at $26 to $34 is an impulse-range entry item. A pair at $62 to $88 is a considered purchase. No evidence tested which converts better, so price cells should be A/B tested, not assumed.

## Risks and gaps
- All supplier costs come from a screenshot; shipping fee, dropship fee, sample cost, custom label/box cost and the US responsible-person arrangement are unknown.
- The catalog's own tags ("Anti-age", "Under-eye fatigue", "Dark spots", "Damaged skin barrier", "Calming" CBD eye cream) are claims you cannot reuse; the CBD eye cream should be excluded; the mist's "microbiome" framing is a claim risk.
- Stock formulas: you cannot control ingredients; ask for the full ingredient list, safety assessment, stability and preservative-test reports before choosing.
- Luxury positioning on a catalog formula needs honest framing: no claims of exclusive formulation or results.

## For a professional
Accountant: sales tax on cosmetics and subscriptions, entity. Counsel: MoCRA responsible person for a private-label dropship, eye-area labeling, claims review, EMMELINE SKIN collision. Insurance broker: product liability for cosmetics. Processor: subscription underwriting and reserves.

## Decisions needed
1. Which cost tier is real: ask SelfNamed for the dropship per-unit price at 1 and 25 units and the shipping fee.
2. Bundle policy: small discount (0 to 5%) or a non-price incentive instead of 15%.
3. Free-shipping line at about $60.
4. Price cells to test (for example eye $48 to $54, mist $29 to $34, pair $72 to $79).
5. Whether the mist is part of the subscription (it likely is not) or a one-time add-on.
6. A CAC ceiling for any paid test (about $40 on these inputs, unless retention is high).
