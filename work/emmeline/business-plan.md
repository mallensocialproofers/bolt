# Emmeline business plan: SelfNamed taken at face value (draft, 2026-10-27)

Status: draft for the owner. Not legal, tax or insurance advice; nothing here is a clearance. "Face value" means SelfNamed's own page claims are treated as true for planning: no minimum order, made on demand, dropshipped to the customer, Pro plan $29 a month, and the catalogue prices read from the owner's screenshot. Every figure is tagged: **SRC** read from a page or screenshot, **SRC-U** unverified secondary source, **ASM** assumption, **ARITH** derived. Supporting files: `bundle_model.py`, `bundle-model-results.md`, `plan_financials.py` (+ `plan_financials_monthly.csv`, `plan_financials_summary.csv`).

## 1. Verdict in one paragraph
On face-value inputs this is a **small, low-capital subscription skincare business that can work, but only if customer acquisition stays cheap and retention holds**. There is no inventory to buy, so the money at risk is mostly fixed set-up costs (placeholders of about $4,800) plus whatever you spend on ads. In the base case the first 12 months produce roughly $18k to $48k of revenue and a net of about **+$1.6k to +$7.8k**; in the pessimistic case (CAC $60, 70% retention, 15% subscribing) it **loses $5k to $10k**; in the optimistic case it earns about $13k to $38k. Treat that spread as the honest answer: the unit economics are healthy (a pair earns about 61% to 70% of revenue as contribution), but the business is a test of whether you can acquire customers for about $40 or less without health claims. There is no conversion, retention or CAC data for this product and audience.

## 2. The business in brief
- **Brand:** Emmeline (see `brand-plan.md`). Name risk: an existing seller uses EMMELINE SKIN (TikTok @emmelineskin, emmelineskin.com); counsel must assess before any spend.
- **Customer:** adult women, mostly 35 to 60, with a focus on women who work overnight shifts as nurses (about 87% to 89% of RNs are women; NCSBN 2024 median age 50; BLS median RN pay $97,550; subscription fatigue is real: 55% of Americans plan to cut subscriptions, per a NerdWallet survey via local TV; a Nurse.org 2026 survey says about a quarter of nurses say pay barely covers essentials). All SRC-U.
- **Product:** private-label eye cream (hero), face mist (add-on), "The Pair" (starter). Stock SelfNamed formulas, your label and box.
- **Model:** online only (Shopify), eye cream on a subscription every 8 weeks, mist as a one-time add-on.
- **Supplier:** SelfNamed, on-demand, ships to your customer. No inventory.

## 3. Offer and pricing (all prices ASM, anchored to unverified comparables: Kiehl's eye creams $40 and $60, Caudalie Beauty Elixir 100 ml $59, The Inkey List duos $22 to $35)
| Item | Price | Notes |
|---|---|---|
| Eye cream, 15 ml | $48 | Hero. Subscription: 10% off, every 8 weeks, free shipping on renewals |
| Face mist, 100 ml | $32 | Add-on. One 100 ml bottle lasts about 250 days at 0.4 ml a day (ASM), so not a subscription item |
| The Pair (starter) | $72 | About 10% under the $80 sum. Ships free (line at $60) |
| Shipping | $5.95 under $60, free above | ASM. This line is a profit lever: eye cream alone earns about $35.87 because the customer pays shipping |
Do not offer a 15% bundle discount: the model shows the mist adds only $2.45 over eye-only at 15% off, versus $9 to $13 at 0% to 5% (L1, tier B). Use free shipping, a free sample or a gift box as the incentive. Hold the nurse discount idea until counsel decides (the label reviewer rated it Do Not Use for the earlier pouch work).

## 4. Operating model at face value
**What SelfNamed says (own pages, 2026-10-27; vendor claims):** no MOQ ("No MOQs, not now, not ever"); 200+ ready-to-brand formulas; products made in the EU in an ISO 22716:2007 facility; ECOCERT/COSMOS badges; "compliant with FDA regulation standards"; dropship with automatic fulfilment from US and EU facilities, "as little as 3 days"; Shopify, WooCommerce, Squarespace and Wix integration; samples within 7 business days; Free plan $0, Pro $29 a month ($348 a year) with up to 30% off dropship orders and up to 70% off bulk orders of 25+, "free once you reach $13,500 in orders in a year"; Enterprise for custom formulas.
**What the page does not say (ask before you rely on it):** who is the MoCRA responsible person on a dropshipped order; per-unit dropship price; shipping fee; sample price; custom label/box cost; subscription support; refund and defect policy; a named manufacturer; full ingredient lists, safety assessments and stability data; whether the dropship box carries only your brand (the page lists "Not possible to affect delivery times or boxing" as a dropship downside); an older SelfNamed blog lists 12 units per product for white label and 100 to 500 for custom, which conflicts with "no MOQ".
**Stack:** Shopify store; SelfNamed integration; subscriptions via Shopify Subscriptions (reported free, SRC-U) or Recharge ($99 a month plus about 1.49% plus $0.19, SRC-U, conflicts with Recharge's own 1.25%); Shopify Payments or Stripe (2.9% + $0.30, SRC-U); email and SMS tool; customer support inbox.
**Pro plan:** at the displayed prices Pro saves about $6.77 per pair order, $3.66 per eye-only order and $3.11 per mist-only order, so $29 a month breaks even at about **4.3 pair orders a month** (ARITH). Start on Free, upgrade when you reach that, and check whether the pink-badge prices on the catalogue really are the Pro price.
**Fulfilment promise to customers:** advertise a range ("ships in 3 to 7 business days"), never a single optimistic number. The FTC mail-order rule defaults to 30 days if you advertise none and requires consent or a refund for a late order.
**Quality control:** order samples of the eye cream, the mist and one backup; do a patch test on yourself; read the ingredient list (and the colorant, if any); photograph the real product for the website.

## 5. Unit economics (from `bundle_model.py`; tier B = $9.10 eye cream + $8.89 mist, ship $5.50, refunds 3%)
| | Face-value list (tier B) | Pro prices (tier A) |
|---|---|---|
| Eye cream alone, $48 (customer pays $5.95 shipping) | $35.87 contribution | $39.53 |
| Mist alone, $32 | $21.02 | $24.13 |
| The Pair, $72 | $43.96 (61% of revenue) | $50.73 (70%) |
| Blended first order (40% eye / 10% mist / 50% pair) | $38.43 on $61.38 AOV | $43.59 |
| Subscription renewal (eye at 10% off, free shipping) | $24.92 | $28.58 |
Sensitivities (L1 pair at $62 as reference): shipping at $8.40 and 8% refunds lowers the pair from $34.55 to $28.55; an extra $2.00 for custom label/box lowers it by $2.00; moving to full list cost ($13.60 + $12.70) cuts the pair by about $8 to $9. To keep the pair at 60% contribution margin, total COGS must stay at or below about $15.34 at $62 and $19.43 at $74.

## 6. Twelve-month plan (`plan_financials.py`; ASM throughout)
Common assumptions: renewals every 2 months for up to 6 renewals; fixed monthly costs $69 (Shopify $39, tools $30; Shopify Subscriptions reported free) plus $29 Pro in the Pro tier; one-time placeholders (unsourced unless tagged): trademark attorney search $1,500, cosmetics counsel $1,500, samples $150, product liability insurance first year $1,500 (sourced range $700 to $4,500, SRC-U), domain/photography $150. **These legal and insurance numbers are placeholders, not quotes.** Organic customers are assumed to come from community seeding, search and creators.

| Tier | Paid budget | Case | Customers | Revenue | Ad spend | 12-month net | Peak cash need | Cumulative positive |
|---|---|---|---|---|---|---|---|---|
| List (B) | Lean $5k | Pessimistic (CAC $60, 70% retention, 15% subscribe) | 107 | $7,370 | $4,250 | -$5,304 | $5,572 | never |
| List (B) | Lean $5k | Base (CAC $40, 80%, 30%) | 236 | $18,590 | $4,250 | +$1,560 | $4,800 | month 11 |
| List (B) | Lean $5k | Optimistic (CAC $25, 90%, 45%) | 411 | $38,084 | $4,250 | +$13,333 | $4,800 | month 7 |
| List (B) | Growth $20k | Pessimistic | 369 | $24,973 | $20,000 | -$10,105 | $10,105 | never |
| List (B) | Growth $20k | Base | 630 | $48,252 | $20,000 | +$4,112 | $4,800 | month 10 |
| List (B) | Growth $20k | Optimistic | 1,041 | $92,698 | $20,000 | +$30,993 | $4,800 | month 6 |
| Pro (A) | Lean $5k | Base | 236 | $18,590 | $4,250 | +$2,778 | $4,800 | month 10 |
| Pro (A) | Growth $20k | Base | 630 | $48,252 | $20,000 | +$7,827 | $4,800 | month 9 |
(Peak cash of $4,800 is simply the one-time placeholders; the pessimistic cases add ad losses on top.)
**Reading it:** a bigger ad budget does not rescue a bad CAC (pessimistic growth loses more than pessimistic lean). The lean plan caps the loss near $5k to $6k if everything goes wrong. Only scale spend after CAC and retention are measured.

## 7. Go-to-market (organic first; no paid ads until the gates below pass)
1. **Weeks 1 to 3, set-up and proof:** counsel and trademark search; order samples; ask SelfNamed the questions in section 4; build the store; photograph real product.
2. **Weeks 4 to 8, waitlist and pre-sale:** a claim-free landing page and waitlist; a small founding-customer pre-sale; read the rules of each nurse community by hand before posting; adult micro-creators only, with clear FTC disclosure (16 CFR 255), no nurse-as-expert endorsement and no implied clinical authority; search content (ritual, routine, ingredients as plain facts once verified).
3. **Weeks 9 to 12, paid test:** only if the gates pass; start at the lean envelope; Meta rules to respect (18+ for dietary products does not apply to cosmetics, but no personal-attribute or appearance-attack ads; no "look tired" implications).
**Channels not to rely on:** Reddit and Facebook-group promotion without reading rules; Amazon; any ad that names a condition.

## 8. Compliance and legal checklist (questions for counsel, not conclusions)
- **MoCRA:** who is the responsible person (the name on the label is, per the research); facility registration and product listing; the small-business exemption applies under $1,000,000 average annual US cosmetic sales but excludes products that regularly contact the eye mucous membrane, and whether an undereye cream counts is unresolved; serious adverse events reported within 15 business days; safety substantiation records.
- **Cosmetic vs drug:** eye-area claims about dark circles, puffiness, wrinkles, "repair" or "firming" are drug-claim territory; FDA warning letters cite them. The SelfNamed catalogue tags ("Anti-age", "Under-eye fatigue", "Dark spots", "Damaged skin barrier") are not yours to reuse.
- **Ingredients:** eye-area color additives must be specifically approved (21 CFR 70.5); state toxics laws (California AB 2762 and others); ask for the full ingredient list.
- **Subscriptions:** ROSCA clear disclosure, express consent and a simple cancel; the FTC click-to-cancel rule was vacated 2025-07-08 and rulemaking restarted in 2026; California auto-renewal amendments (July 2025, law-firm summaries); New York amended law (November 2025); no annual prepay at the start (chargeback and reserve exposure).
- **Name:** trademark search for EMMELINE in classes 3, 5, 35, 44 including common law; the EMMELINE SKIN seller; EMELINE and ÉMELINE Class 35 retail marks.
- **Sales tax and entity:** accountant. **Insurance:** broker for cosmetics product liability.
- **Endorsements and reviews:** 16 CFR 255 and the Reviews Rule (16 CFR 465).

## 9. Risks and mitigations
| Risk | Why it matters | Mitigation |
|---|---|---|
| Catalogue formula is not exclusive | SelfNamed sells the same stock formulas to others; a $48 price on a $9 catalogue item invites "overpriced" reviews | Make the value brand, packaging and experience, and do not claim exclusive or clinical formulas; consider a price test at $38 to $44; ask about custom (Enterprise) later |
| Claims creep | The catalogue tags and competitor copy are drug claims | Claims dictionary and `label-claims-reviewer` before anything goes live |
| Supplier dependence | One vendor, unknown policies, one-person account | Ask for refund and defect policy; keep a second supplier option (the AliExpress patches as a cheap demand test, not as the main product) |
| Responsible person unclear | The brand carries MoCRA duties | Counsel before launch |
| CAC above about $40 | Base case barely profitable | Organic first; stop-loss at the lean envelope |
| Chargebacks and reserves | Subscription and new store | Clear terms, easy cancel, no annual plan |
| Name collision | EMMELINE SKIN | Counsel; modifiers or a rename if needed |
| Small scale | Base-case profit is a few thousand dollars | Treat it as a test, not a job |

## 10. Ninety-day timeline with gates and kill criteria
| Weeks | Actions | Gate to proceed |
|---|---|---|
| 1 to 2 | Send SelfNamed questions; order samples; trademark attorney and cosmetics counsel; read EMMELINE SKIN site | Counsel finds no blocking issue; SelfNamed answers the responsible-person and per-unit cost questions |
| 3 to 4 | Patch-test samples; confirm ingredients; photograph product; build store; claims dictionary | Samples acceptable; per-unit cost within the model's ceiling (total COGS about $15 to $19 at a $62 to $74 pair) |
| 5 to 8 | Waitlist and pre-sale; seed communities (rules read); creators | At least a stated number of waitlist sign-ups and pre-orders (owner sets; suggest 50 paid pre-orders as a floor) |
| 9 to 12 | Lean paid test ($1,000 to $2,000 first) | First-order contribution exceeds CAC by month 3 of testing, or kill |
**Kill or pause if:** CAC stays above about $40 after $1,500 of tests; refunds exceed 8%; counsel says the name or the formula claims cannot be used; SelfNamed will not name the responsible person or cannot ship in the stated time.

## 11. KPIs to track
First-order contribution and AOV; CAC by channel; subscription take rate; renewal retention per 8-week cycle; refund and chargeback rate; shipping time and cost; review score; cancellation reasons.

## 12. Decisions needed
1. Approve the lean envelope and kill criteria; set a hard cap on paid spend before the gate.
2. Send the SelfNamed question list (draft available; nothing sent).
3. Hire counsel (cosmetics/food-and-drug and trademark); choose whether to register getemmeline.com or emmelineskincare.com yourself.
4. Choose price cells to test (eye $44 to $54, mist $29 to $34, pair $62 to $79) and the free-shipping line.
5. Decide whether to keep the AliExpress eye patches as a cheap demand test.
6. Whether the Delphine caffeine line stays parked.

## For a professional
Cosmetics/food-and-drug counsel (responsible person, eye-area exemption question, claims, labels), trademark attorney (EMMELINE and EMMELINE SKIN), accountant (entity, sales tax on cosmetics and subscriptions), insurance broker (product liability), payment processor (subscription underwriting and reserves).

## 13. Lowering overhead: where the money is actually at risk (added after the owner's question)
Dropship means product, postage and payment fees are paid only when a customer pays, so there is no inventory risk. The model's losses come from three other things (pessimistic lean case, tier B): **one-time placeholders $4,800** (legal, trademark, insurance, samples, set-up), **ad spend $4,250** that did not pay back, and **monthly fixed $828** (Shopify and tools, $69 a month), against only $4,574 of contribution, for a net of -$5,304. Other ways to lose money: refunds and chargebacks (a fully refunded pair order still costs about $25.88: product $17.99, postage $5.50, payment fee about $2.39), supplier price changes, a defective batch replaced at your cost, processor reserves holding your cash, an FDA warning letter or a forced rebrand after a trademark conflict.
**Organic-only (no ads), tier B, with the full $4,800 one-time costs:** pessimistic -$4,084 (36 customers); base +$581 (130 customers, revenue $10,082); optimistic +$7,698 (241 customers). Covering $4,800 of one-time costs takes about 125 first orders (at $38.43 blended first-order contribution); covering about $2,300 (counsel, samples, set-up only) takes about 60.
**How to lower overhead without skipping what protects you (placeholders are not quotes):**
1. **Sequence the spend behind proof.** Before any legal or insurance spend, run the cheap validation: samples ($150 placeholder), a waitlist page, a short survey of adult women in the audience, and a small pre-sale. If it fails you have spent about $300, not $4,800.
2. **Spend on counsel only once the pre-sale clears the gate,** and ask for a scoped, flat-fee review (name search, label, claims dictionary, MoCRA responsible person). Do not publish or ship before it.
3. **Insurance:** get quotes from a broker for a startup cosmetics policy before the first shipment (the sourced range is $700 to $4,500 a year, SRC-U); do not ship an eye-area product uninsured.
4. **No paid ads until CAC is proven** with organic and a few hundred dollars of tests; cap the first test at $1,000 to $1,500.
5. **Stay on SelfNamed Free** until you reach about 4.3 pair orders a month; use the lowest Shopify plan you can; use free tiers of email tools; no Recharge (use Shopify Subscriptions if it is free as reported); no annual prepay; AI imagery at about $0.09 per image rather than a shoot (once the key is set).
6. **Launch one eye cream plus the pair** (not extra SKUs), and test the eye-cream-only price at $44 to $54.
Kill rule unchanged: if CAC stays above about $40 after $1,500 of tests, refunds exceed 8%, or counsel blocks the name or formula, stop.
