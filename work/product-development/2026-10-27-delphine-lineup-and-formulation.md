# Delphine: product lineup and formulation briefs (25 mg caffeine per pouch)

Date: 2026-10-27. Agent: product-development. Status: DRAFT for the owner. Nothing here is sent, ordered or published.

Scope and rules applied
- Brand: DELPHINE (owner's choice, 2026-10-27; NOT trademark-cleared; see CLAUDE.md). Product names below are working names only.
- One strength: 25 mg caffeine per pouch. The four products differ only in flavor, pouch format and tins per pack.
- Segment (owner's decision, 2026-10-27): women who work overnight shifts (nurses). Adults only; age treated as 21+ because the minimum age is not yet recorded in `work/decisions.md`.
- Copy and product names carry no health, alertness, sleep or performance meaning, no nicotine-replacement meaning, and nothing that appeals to minors.
- Evidence: this file reuses the existing research notes and did not re-run the research. I ran no new web searches. Source pages were last checked 2026-10-27 in those notes. Items the notes could not confirm from a primary source are marked UNVERIFIED.
- Tags: SRC = in an existing note with a URL. ASM = my assumption or scenario, not a fact. UNVERIFIED = not confirmed from a primary source.
- Nothing here says any practice is legal, compliant or safe. Legal questions are collected under "For a professional".
- No spend on inventory, branding or ads is recommended until the owner records that the compliance gate is cleared in `work/decisions.md` (it is NOT cleared as of today).

---

## 1. Lineup table

All products: 25 mg caffeine per pouch, 20 pouches per tin (ASM, see section 2), so 500 mg caffeine per tin. Caffeine per day is plain multiplication (25 mg x pouches) and counts pouches only. Coffee, tea, soda, energy drinks and other products add to it.

| # | Working product name | Flavor (plain descriptor) | Pouch format | Pouches per tin | Tins per pack | Caffeine per tin | 4 / day | 8 / day | 12 / day |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Delphine Lemon, Slim, 4-tin pack | Lemon (citrus peel) | Slim | 20 | 4 | 500 mg | 100 mg | 200 mg | 300 mg |
| 2 | Delphine Ginger, Slim, 3-tin pack | Ginger | Slim | 20 | 3 | 500 mg | 100 mg | 200 mg | 300 mg |
| 3 | Delphine Black Tea, Regular, 4-tin pack | Black tea (flavor only, no tea extract) | Regular | 20 | 4 | 500 mg | 100 mg | 200 mg | 300 mg |
| 4 | Delphine Spearmint, Regular, 3-tin pack (OPTIONAL, see note) | Spearmint | Regular | 20 | 3 | 500 mg | 100 mg | 200 mg | 300 mg |

Per-shift scenarios (12-hour shift; arithmetic only, NOT a use recommendation; pouches per shift are the modelling variable from the nurse economics note):

| Pouches on one 12-hour shift | Caffeine from pouches | Share of FDA 400 mg/day figure | Tins per month at 13 shifts/month (ASM from nurse note) |
|---|---|---|---|
| 3 | 75 mg | 18.8% | 1.95 |
| 5 | 125 mg | 31.3% | 3.25 |
| 8 | 200 mg | 50% | 5.20 |

Daily-total reference table for the label (my arithmetic):

| Pouches in a day | Caffeine from pouches | Share of 400 mg | Left under 400 mg for all other caffeine |
|---|---|---|---|
| 4 | 100 mg | 25% | 300 mg |
| 8 | 200 mg | 50% | 200 mg |
| 12 | 300 mg | 75% | 100 mg |
| 16 | 400 mg | 100% | 0 mg |

Pack-level caffeine (ASM pack sizes): 3 tins = 60 pouches = 1,500 mg; 4 tins = 80 pouches = 2,000 mg. The pack total is not a serving figure and is not recommended for the label.

Notes on the lineup
- Why these flavors. Flavors are plain descriptors (citrus, root, tea, herb). Not used: dessert, candy, fruit-punch, cola, alcohol or "ice/cool" names. Mint and wintergreen are the default flavor family of nicotine pouches, so Delphine leads with non-mint flavors. Product 4 (Spearmint) is optional and is a test of the look-alike question; drop it if counsel or the nurse panel reads it as a nicotine-pouch cue. (ASM; no evidence either way.)
- Why "Slim" and "Regular". These are format labels only. Pouch dimensions and fill weight are NOT known; the manufacturer should propose them (section 4). Competitor pouch sizes were not captured in the existing notes (gap).
- Why no cooling agents. Mouth tingle and irritation recur as a complaint theme for Nectr, NZE and Mojo (SRC: competitors_and_dose.md section 3, gap_competitors_trademark.md section 2; second-hand, UNVERIFIED). The briefs below ask for no added cooling or "heat" agents. Ginger is the main irritation risk and is a test item.
- Flavor-name caution. "Black Tea" names a taste. The product must not add tea extract or any other caffeine-bearing ingredient (see exclusions), or the 25 mg figure would be wrong.

---

## 2. Recommended tin size and bundle structure (ASSUMPTIONS, not decisions)

Source for the economics: `/home/user/bolt/research_notes/Overnight women nurses niche research/economics_offer_positioning.md` and `nurse_economics.py` (inherited model, COGS $2.50 per tin, shipping cost $5.50, pick-pack $2.50, all ASM; no co-packer quote exists).

| Item | Recommendation | Basis | Status |
|---|---|---|---|
| Pouches per tin | 20 | Keeps tins per month near 2 to 3 for light use and spreads shipping and pick-pack over more pouches. Competitors use 15 to 20 (SRC). | ASM; ask makers to quote 15 and 20 |
| Caffeine per tin | 500 mg | 20 x 25 mg | arithmetic |
| First-order default | 4-tin pack | At free shipping and $7.99 per tin, first-order CM1 is +$12.09; a 1-tin order is -$2.25 and a 2-tin order only +$2.85 (SRC: nurse note section 2). | ASM |
| Smaller option | 3-tin pack | CM1 +$7.00 at free shipping; positive even in the worst case run (+$1.50). | ASM |
| Not recommended | 1-tin and 2-tin free-shipping orders; 5-tin bundle | 5 tins at $7.49 earns less CM1 than 4 tins, and at 3 pouches per shift a 5-tin pack lasts about 11 weeks, which delays reorders. | ASM |
| Illustrative price ladder (nurse note "Ladder A") | 3 tins $23.97; 4 tins $31.96 ($7.99 per tin, $0.40 per pouch) | Competitor anchor: Grinds 25 mg about $0.33 per pouch (SRC, UNVERIFIED count and price). | ASM, price not a decision |
| Free-shipping line | About $30, just above a 3-tin order | Nudges buyers to 4 tins. | ASM, untested |
| Subscription | Every 6 to 8 weeks with skip, pause and change date | 4 tins last about 8.8 weeks at 3 per shift, 5.3 at 5, 3.3 at 8 (13 shifts a month). | ASM |
| Verified-healthcare discount | First order only, 10 to 15%, replaces (does not stack on) the subscription discount | At 15% a 4-tin first order still returns $12.28 CM1. | ASM; discount vendor fees unknown |

Product-mix suggestion (ASM): launch with Products 1 and 2 (non-mint, slim) and add 3 and 4 only if the sample panel supports them. All four share one formulation base so the minimum order is not split four ways more than needed. The only published minimum order found is Daily Manufacturing's 25,000 cans (5,000 per flavor), self-reported, from a maker that is under an FDA tobacco warning letter (SRC: gap_federal_and_suppliers.md section 7; see decisions.md). Four flavors at 5,000 tins each would be 20,000 tins; this is a reference point, not a quote.

Caveats
- Per 100 mg, a 25 mg pouch costs more than a 100 to 200 mg pouch (SRC: gap_competitors_trademark.md section 1: Grinds 25 mg about $1.32 per 100 mg; Wip 200 mg about $0.28). Price is the weak point of a low-dose product. Do not respond by encouraging more pouches per day.
- Nectr price conflict, not resolved: nectr.energy lists $29.99 to $39.99 per pack with 20 pouches per tin (earlier note), while Roon's table lists $9.99 to $10.99 per tin (competitor source). The first figure appears to be a multi-tin pack and the second a single tin (owner's reading); neither is confirmed. Do not put either in a model without a live check.
- Real cost of goods, tin weight, adult-signature requirement and shipping cost are unknown.

---

## 3. Shared specification (applies to all four products)

Fixed by the owner
- Caffeine: 25 mg per pouch. No other strength, no "extra" line.
- Adults only. 21+ used until the age policy is recorded.

Caffeine source (to confirm with maker)
- Caffeine anhydrous, USP or FCC grade, synthetic or natural per maker. Supplier COA, identity and purity per lot. Country of origin. (No verified bulk supplier is named in the notes; sourcing.md section 3 gap.)
- The caffeine in each pouch must come only from this ingredient. Declared strength is the sum, so every other ingredient must be confirmed free of added caffeine.

Ingredients and materials to AVOID unless counsel and the owner approve (each is a question for the maker or a lawyer, not a ruling)
- Other caffeine-bearing or caffeine-adjacent ingredients: guarana, green tea or green coffee extract, yerba mate, kola, taurine, paraxanthine, theacrine, methylliberine. Reason: they add unquantified or second stimulants and break the single-number 25 mg declaration.
- L-theanine, B vitamins, citicoline, Alpha-GPC, adaptogens, "nootropics", melatonin. Reason: these are how competitors make effect claims (Nectr, Ultra, Roon, Mojo; SRC). They would invite substantiation and claim questions, and some (melatonin) tie directly to sleep.
- Nicotine, tobacco-derived material, or any ingredient processed on a line that has run nicotine without a documented cleaning and segregation protocol. Ask for a nicotine non-detect result per lot (see section 5).
- Cooling or "tingle" agents added for sensation, and added "heat" agents.
- Xylitol and other polyols: xylitol is used by Wild Pouches (SRC). I flag it to confirm for two reasons: gastrointestinal effects of polyols at repeated use (UNVERIFIED) and the commonly cited toxicity of xylitol to dogs (UNVERIFIED here, general knowledge). Ask the maker to quote without it.
- Artificial colors, titanium dioxide, glitter, bright coloring of pouches or tins (minor-appeal and look-alike risk).
- Sugar (dental exposure with repeated daily holds; ASM).

Pouch material (questions for the maker)
- Food-grade non-woven plant-fiber (cellulose) pouch material is the working assumption (Wonnda copy mentions "food-safe fleece/nonwoven materials", SRC sourcing.md). Maker to name the material, supplier, food-contact documentation, seal method, and whether any binder, dye or optical brightener is used.
- Pouch dimensions, fill weight (mg), moisture level (dry vs moist) and whether the pouch breaks down or leaves fibre in the mouth: maker to propose. "Slim" and "Regular" are targets set by Delphine's pouch-size comparison to be agreed after samples; I have no dimension data and have not invented any.
- Content per pouch must be within the tolerance in section 5 for every pouch size.

Allergens (all products)
- Design target: no major food allergen as an ingredient. Maker to confirm in writing the major allergens handled in the facility and on the line (the nine US major allergens including sesame; the FASTER Act text and effective date were not fetched in the notes, UNVERIFIED), the carrier of every flavor (maltodextrin, starch, oils), and cross-contact controls.
- Starch, maltodextrin and MCT-type oils appear in competitor ingredient lists (Wild Pouches; SRC). Sources (wheat, corn, coconut) must be named.
- Allergen statement format ("Contains ...") is for counsel.

Packaging (all products) options for the maker to quote
- Tin A: plastic (e.g. polypropylene) tin with standard snap lid, 20 pouches, printed label or sleeve.
- Tin B: same tin with a child-resistant (CR) lid. Ask for the CR certification test report (16 CFR 1700.20 child-resistance protocol is the usual standard; the notes only have a search result for it, UNVERIFIED).
- Tin C: metal tin, if the maker supplies it (cost unknown).
- Tin look: avoid the matte-black or saturated round tin, bold strength band, and mint-green or ice-blue coding that read as nicotine-pouch tins (SRC: nurse note section 4). Pocket-size, flat, warm paper-white or soft earth-tone label; no nurse icons, medical symbols or scrubs imagery.
- Tamper-evident seal (foil or shrink band).
- Pouch separation: liner or inner sleeve so pouches do not dry out or stick (maker to advise).
- Shipping case, pack labelling and a lot code on every tin and outer carton.

Is child-resistant packaging advisable? (my view, for the owner and counsel to decide)
- The CPSC special-packaging list at 16 CFR 1700.14(a) as retrieved does not mention caffeine; the only supplement entry is for iron (SRC: gap_federal_and_suppliers.md section 6). That is not a conclusion that no rule applies (counsel to confirm; state rules were not researched).
- Advisable on a voluntary basis, in my view, for these reasons: one tin holds 500 mg of caffeine (20 x 25 mg), the format is a small tin that looks like a nicotine-pouch tin and may be attractive to children, and schools are already banning these pouches (SRC: AP/Fortune 2026-10-22 in the notes). Trade-offs: higher unit cost (unknown), harder opening for gloved or tired hands, and a voluntary CR claim may need substantiation (a lawyer question). Ask the maker for both quotes (Tin A and B) before deciding.

Shelf life
- Not known. Ask the maker for stability data (caffeine assay and microbial over time, at room temperature and under accelerated conditions) and propose a "best by" period from that data. I have not assumed a number. Storage statement ("store in a cool, dry place" or similar) is for the maker and counsel.

Label caffeine declaration (all products; for counsel to approve)
- Front of tin: "25 mg caffeine per pouch".
- Back or side: "Contains caffeine." Pouches per tin and total caffeine per tin: "20 pouches, 500 mg caffeine per tin" (arithmetic; counsel to say whether the per-tin figure should appear).

---

## 4. Formulation briefs (one per product, for a manufacturer to quote against)

Common to all four: quote by RFQ at two pouch weights and two pouch sizes (Slim, Regular), fill 20 pouches per tin, with an alternative quote at 15. Percentages and fill weights are for the maker to propose; this brief fixes only the caffeine amount and the permitted ingredient classes. "Ingredient" lines below are proposed classes to confirm, not final formulas.

### Product 1: Delphine Lemon, Slim, 20 per tin, 4-tin pack

| Item | Brief |
|---|---|
| Label caffeine claim | "25 mg caffeine per pouch" (for counsel to approve) |
| Caffeine | Caffeine anhydrous, 25 mg per pouch, target within tolerance in section 5 |
| Filler / carrier | Microcrystalline cellulose (MCC) or equivalent plant-fiber filler (named in Wild Pouches' list; SRC) |
| Moisture / texture | Purified water; humectant (e.g. glycerin; maker to confirm); no oil unless the maker needs it, and then source named |
| pH / salt | Optional food-grade sodium bicarbonate and salt (both appear in Wild Pouches' list; SRC); maker to say what each does and the amount |
| Flavor system | Natural lemon (citrus) flavor, no added cooling agent; maker to name the flavor supplier, carrier and allergen status |
| Sweetener | One sweetener only, chosen with counsel's advice; options to quote: steviol glycosides or sucralose; no xylitol |
| Colorant | None |
| Pouch | Slim non-woven plant-fiber pouch (maker to specify) |
| Packaging | Tin A and B quotes, 20 per tin, 4 tins per pack |
| Allergens | None intended; written confirmation required |

### Product 2: Delphine Ginger, Slim, 20 per tin, 3-tin pack

| Item | Brief |
|---|---|
| Label caffeine claim | "25 mg caffeine per pouch" (for counsel to approve) |
| Caffeine | Caffeine anhydrous, 25 mg per pouch |
| Filler / carrier | MCC or equivalent |
| Moisture / texture | Purified water; humectant (maker to confirm) |
| pH / salt | As Product 1 |
| Flavor system | Natural ginger flavor, no added "heat" or cooling agent. Do not use ginger root powder or extract if the maker cannot document that the pouch stays free of extra active compounds; flavor concentrate preferred. Irritation test: ask the maker whether ginger flavor increases tingle; include in the sample panel |
| Sweetener | As Product 1 |
| Colorant | None |
| Pouch | Slim non-woven plant-fiber pouch |
| Packaging | As Product 1, 3 tins per pack |
| Allergens | None intended; written confirmation required |

### Product 3: Delphine Black Tea, Regular, 20 per tin, 4-tin pack

| Item | Brief |
|---|---|
| Label caffeine claim | "25 mg caffeine per pouch" (for counsel to approve) |
| Caffeine | Caffeine anhydrous, 25 mg per pouch. Flavor must be a tea-type flavor with NO tea extract or tea leaf; maker to certify the flavor adds no caffeine, or give the measured caffeine contribution so the assay target can be set (this is the main risk on this product) |
| Filler / carrier | MCC or equivalent |
| Moisture / texture | Purified water; humectant |
| pH / salt | As Product 1 |
| Flavor system | Natural black-tea-type flavor, no cooling agent |
| Sweetener | As Product 1 |
| Colorant | None (tea flavor must not color the pouch) |
| Pouch | Regular non-woven plant-fiber pouch |
| Packaging | As Product 1, 4 tins per pack |
| Allergens | None intended; written confirmation required |

### Product 4: Delphine Spearmint, Regular, 20 per tin, 3-tin pack (OPTIONAL)

| Item | Brief |
|---|---|
| Label caffeine claim | "25 mg caffeine per pouch" (for counsel to approve) |
| Caffeine | Caffeine anhydrous, 25 mg per pouch |
| Filler / carrier | MCC or equivalent |
| Moisture / texture | Purified water; humectant |
| pH / salt | As Product 1 |
| Flavor system | Natural spearmint flavor only; NO menthol/cooling-agent boost, no "ice" or "extreme" variants. Nicotine-pouch look-alike risk: counsel and the nurse panel decide whether to launch it |
| Sweetener | As Product 1 |
| Colorant | None |
| Pouch | Regular non-woven plant-fiber pouch |
| Packaging | As Product 1, 3 tins per pack. Tin art must avoid the mint-green / ice-blue coding that marks nicotine tins |
| Allergens | None intended; written confirmation required |

---

## 5. Tests to require (questions for the manufacturer; tolerances are ASSUMPTIONS for counsel and QA to set)

| Test | What to ask | Notes |
|---|---|---|
| Caffeine assay per pouch | Validated method (HPLC or equivalent), on individual pouches, every lot, results on the COA | Proposed starting tolerance: 90 to 110% of label (22.5 to 27.5 mg per pouch) as an average, with a stated per-pouch range and a uniformity limit. ASM only: because 12 pouches is 300 mg, the upper limit matters more than the lower one. QA and counsel set the real number. |
| Content uniformity | Number of pouches tested per lot, spread across the run (start, middle, end) | Maker to state sample size and limits |
| Identity of caffeine (raw material) | COA for each caffeine lot plus identity test in house (21 CFR 111.75 expects it if the product is a supplement; SRC) | Applies only if supplement route; see classification question |
| Release of caffeine in use | Optional: caffeine released into artificial saliva after a stated hold time | Label declares content per pouch, not delivered dose. Delivered dose is unknown (no pouch PK study; SRC competitors_and_dose.md section 4). Do not make an absorption or onset claim. |
| Microbial | Total aerobic count, yeast and mold, E. coli, Salmonella, S. aureus (organism list and limits per maker's spec) | Counsel and QA to confirm limits against the applicable standard |
| Heavy metals | Lead, arsenic, cadmium, mercury (ICP-MS) on finished lot | Ask whether California Prop 65 warning is needed (lawyer) |
| Nicotine non-detect | Screen each lot for nicotine | Only needed if the maker runs nicotine on shared equipment; ask for cleaning validation |
| Allergen | Written program; testing for any allergen that shares the line | |
| Water activity, pH, moisture | Per lot | Needed for stability and microbial control |
| Stability | Real-time and accelerated, caffeine assay and microbial at set intervals | Sets shelf life |
| Packaging integrity | Seal, leak, tin closure, CR test report if Tin B | |
| COA per lot | Released to Delphine before shipment; retain samples | |
| Third-party verification | Ask about NSF, USP or similar programs and cost | Competitors only claim "third party tested" or "GMP" (SRC); none verified |

Other maker questions: FDA facility registration number; cGMP standard actually followed (21 CFR 111 vs 117; "GMP certified" alone does not say); recall history; insurance; MOQ and lead time; who owns tin inventory; ability to fill exactly 25 mg (Daily Manufacturing lists 50 to 150 mg only; SRC gap_federal_and_suppliers.md).

---

## 6. Recommended label statements (ALL FOR COUNSEL TO APPROVE)

None of this wording is final. Each line may need to change if the product is a conventional food rather than a dietary supplement (Supplement Facts vs Nutrition Facts, see "For a professional").

1. Caffeine declaration (front, large): "25 mg caffeine per pouch" (for counsel to approve)
2. Adults only: "Adults 21+ only." (21+ is a placeholder until the owner records the age policy; for counsel to approve)
3. Serving statement: "Serving size: 1 pouch (25 mg caffeine). Servings per container: 20." (for counsel to approve)
4. Daily-total statement (draft; the cap number is the owner's and counsel's decision, not mine): "Count your caffeine. Each pouch has 25 mg. 4 pouches = 100 mg. 8 pouches = 200 mg. 12 pouches = 300 mg. Caffeine from coffee, tea, soda, energy drinks and other products adds to your total. Do not use more than [NUMBER SET BY COUNSEL] pouches in a day." (for counsel to approve)
   - Reference: FDA has cited 400 mg a day as an amount not generally associated with negative effects in most healthy adults (SRC: https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much, checked 2026-10-27 in the notes; counsel and regulatory agent have not yet confirmed it as the label reference). 16 pouches = 400 mg from pouches alone, leaving no room for other caffeine; a statement naming a cap at or near 16 would not account for coffee or tea. Whether to state any number, and which, is for counsel. I do not recommend printing "up to 16".
5. Sensitivity and conditions: "Caffeine affects people differently. If you are pregnant, trying to become pregnant or breastfeeding, take medication, or have a medical condition, ask your health care provider before use." (for counsel to approve). Specific pregnancy and lactation mg figures (about 200 mg and about 300 mg per day from secondary sources) are UNVERIFIED and are not used. Note for the owner: 8 pouches is 200 mg from pouches alone, which equals the pregnancy figure the research cites, so this line matters for a female customer base.
6. Children: "Not for children. Keep out of reach of children." (for counsel to approve)
7. Use instruction: "Place one pouch in the mouth. Do not swallow or chew the pouch. Dispose of used pouches." Whether to name a position in the mouth, and whether the instruction itself looks like a nicotine pouch instruction, is for counsel (for counsel to approve).
8. Ingredient list in descending order and allergen statement per counsel (for counsel to approve).
9. Factual "Contains no nicotine or tobacco." Optional. It invites nicotine comparison, so counsel decides (for counsel to approve).
10. Responsible-person line: name and place of business, plus a domestic address or phone for adverse-event reports (21 U.S.C. 343(e)(1) and 343(y); SRC gap_federal_and_suppliers.md section 2; for counsel to approve). Delphine's legal entity and address are not recorded; the owner must supply them.
11. Lot code and best-by on every tin.

Do not print or publish: "energy", "focus", "alert", "awake", "stay up", "all night", "recharge", "fuel", "boost", "no crash", "no jitters", "natural energy", "safe", "unlimited", "as many as you need", any sleep-timing advice (counsel may add a safety line; I did not draft one because the rules bar sleep claims), any nurse-as-endorser, scrub or medical imagery, and any quit-smoking or "alternative to" wording.

---

## 7. Competitor teardown

All rows are from the existing notes, checked 2026-10-27 in those notes. Most brand-site figures were read through a page summarizer and need re-checking on the live page. Weak sources are flagged.

| Brand | Caffeine per pouch | Pouches per tin | Price | Ingredients (as recorded) | Flavors | Review themes | URLs and status |
|---|---|---|---|---|---|---|---|
| Grinds (closest 25 mg analogue) | 25 mg in Wintergreen, Spearmint, Caramel, Cinnamon Roll; 50 mg Double Mocha and Root Beer (Amazon summary) | Conflicts: 15 (Walmart), 18 (Roon, Amazon), 20 (Kill the Can) | About $5.95 per tin, about $0.33 per pouch at 18 (Roon) | Coffee; one listing adds guarana, taurine, B vitamins | 30+ flavors (Roon) | Flavor fade (2 to 10 minutes per one Reddit user, second-hand); varies dry to moist | https://www.walmart.com/ip/Grinds-Coffee-Pouches-1-Can-of-Wintergreen-Tobacco-Nicotine-Free-25-mg-of-Caffeine/740930074 ; https://www.amazon.com/GRINDS-Coffee-Pouches-Caramel-Flavors/dp/B0GR9YJ4JD ; https://www.takeroon.com/blog/best-caffeine-pouches-ranked ; https://www.killthecan.org/?p=895 . UNVERIFIED: own site returned 503 |
| Nectr | 50 mg (Energy, Focus); a reported 30 mg product is not supported | 20 (nectr.energy via earlier note); count not published in Roon table | Conflict: $29.99 to $39.99 per pack (nectr.energy) vs $9.99 to $10.99 per tin (Roon). Likely multi-tin pack vs single tin, not reconciled | Focus adds 320 mg nootropic blend (Alpha-GPC, L-theanine, L-tyrosine, Huperzine A); Energy adds B vitamins | Wintergreen, Watermelon, Mango, Fresh Mint, Black Cherry, Cinnamon, Jalapeno Lime | Lip burn complaint (second-hand); warning "do not exceed 400 mg daily from all sources (about 8 pouches)" | https://nectr.energy/ ; https://www.takeroon.com/blog/best-caffeine-pouches-ranked . Price UNVERIFIED |
| Roon | 80 mg | 15 | About $9.16 per tin on a 12-tin plan, $15.00 one-time (nurse pages) | Caffeine, L-theanine 60 mg, methylliberine 25 mg, theacrine 5 mg | Cool Mint and others | Only nurse-specific competitor; effect-claim copy (off limits for Delphine) | https://www.takeroon.com/blog/best-nicotine-free-energy-pouches-2026 ; https://www.takeroon.com/pouches/nurses-night-shift-focus . Competitor-authored |
| Wip | 100 or 200 mg | 15 | $0.44 to $0.56 per pouch by pack; $5.99 launch MSRP | B vitamins, chromium, L-theanine (amount undisclosed) | Not captured | "Smooth and steady"; one incentivized review; no third-party certification (AOL) | https://insider.fitt.co/press-release/wip-energy-pouches-now-available-in-over-330-walmart-fuel-centers-nationwide/ ; https://thingtesting.com/brands/wip/reviews |
| Mojo | 50 or 100 mg | 15 | About $0.37 to $0.60 per pouch | L-theanine, N-acetyl-L-tyrosine, ginseng, yerba mate, eleuthero, rhodiola, B vitamins | Not captured | Mixed: artificial taste and tingle vs praised taste | https://jefferyshome.com/mojo-energy-pouches-review/ ; Roon pages above. Competitor source |
| Ultra | 180 mg (Energy, launched Sept 2026 per Uncrate) | 15 (Focus) | Focus $16.00 per can; nurse discount, percent unknown | Energy: L-theanine, B3/B6/B12, C, E; Focus and Sleep lines differ | Wintergreen, Sweet Mint, Black Cherry | Subscription cancellation complaints (second-hand) | https://takeultra.com/ ; https://uncrate.com/ultra-energy-pouches/ ; https://www.businesswire.com/news/home/20260120688296/en/Pouches-Minus-the-Nicotine-Ultra-Raises-11-Million-to-Build-a-Clean-Non-Addictive-Pouch-for-High-Performers/ |
| Wild Pouches | 60 or 120 mg | Not shown | Not shown | MCC, caffeine, maltodextrin, natural flavors, MCT oil, glycerin, xylitol, stevia, sucralose, starch, baking soda, inulin, salt | Citrus Ice, Caramel Iced Coffee, Watermelon Grape, Ice Peppermint, Raspberry Lemon Heat, Wintergreen | Inconsistent duration claims on site | https://wild-pouches.com/ . Closest published ingredient list for a plain-caffeine pouch |
| NZE | 50 mg | 15 | $34.99 per 5-pack (about $7.00 per tin) | Not captured | Lemon Cherry | Praised taste; canker sore complaint (second-hand) | Roon pages above. UNVERIFIED |
| BUM Energy | 30 mg | Not captured | $8.99 per can, $34.99 for 5 | 125 mg Cognizin citicoline | Not captured | n/a | https://www.takeroon.com/blog/best-caffeine-pouches-ranked . UNVERIFIED |
| boltpouches.com | 50 to 200 mg | 20 | From AED 29 | Caffeine, L-theanine, B6, B12, natural flavour, plant fibre | 13 flavors including bubble gum, cola, cherry | UAE-oriented; name collision with the dropped "Bolt" name, not Delphine | https://boltpouches.com . Included for completeness only |

Teardown findings
- Grinds already sells a 25 mg pouch. "First 25 mg pouch" is not a safe statement for Delphine (SRC: gap_competitors_trademark.md). The differentiators available without claims are plain caffeine only, a single printed number, a published ladder, non-mint flavors, and a flat pocket tin.
- Competitor flavor lists lean to mint, wintergreen, cherry, watermelon and dessert flavors. Delphine's non-mint, non-dessert set is a deliberate gap and a guard against minor appeal and nicotine look-alike.
- Competitor ingredients stack nootropics or vitamins to support effect claims. Delphine's plain set is not a claim-free guarantee; counsel still reviews it.
- Gaps: gum, mint, strip and chew competitors were not covered. Pouch dimensions and moisture were not captured. No first-hand review text was retrieved.

---

## 8. The three biggest open questions for the owner

1. Do you commission counsel's view on the regulatory category (dietary supplement vs conventional food) before any maker is contacted? It decides the label panel, cGMP standard, the testing a maker must do, whether the 25 mg declaration is a Supplement Facts line or an ingredient-list line, and who must receive adverse-event reports. No FDA statement exists (SRC: gap_federal_and_suppliers.md section 4). Without it, the formulation briefs cannot be finalized.
2. What is your risk posture on voluntary protections: a stated daily-pouch cap on the tin, a pregnancy and lactation caution, and child-resistant tins? Each costs conversion or unit cost. The research does not require any of them, but 500 mg per tin, a female customer base and school-ban attention in the news (October 2026) point to using all three. This also fixes the age policy (18+ or 21+).
3. Are you willing to launch with a plain, non-mint line at roughly $7.99 per tin (illustrative) in 4-tin and 3-tin packs without a real cost quote, against Grinds at about $0.33 per pouch? COGS, MOQ and tin size (20 vs 15) are all unquoted. If the quote lands above about $2.50 per tin (my model assumption), the 3-tin and 4-tin floor needs a higher price. Also tell me whether Product 4 (Spearmint) stays on the list.

---

## 9. For a professional

For counsel (food and drug, advertising)
- Classification. Is a pouch held in the mouth and not swallowed "intended for ingestion" under 21 U.S.C. 321(ff)? If not a supplement, what is the basis for added caffeine given that 21 CFR 182.1180 covers only cola-type beverages? (SRC: gap_federal_and_suppliers.md sections 3 and 4.)
- Label framework. Supplement Facts (21 CFR 101.36) vs Nutrition Facts; caffeine as an ingredient with "Daily Value not established" if supplement; where the per-pouch figure goes; serving definition (one pouch).
- Daily-total statement. Which daily cap wording is acceptable, whether naming a number could itself imply a benefit or sleep effect, and whether FDA's 400 mg figure should be cited on the label. Confirm that the 400 mg figure is right to use.
- Safety line. Whether a sleep-timing or bedtime safety note is permitted when marketing rules bar sleep claims.
- Pregnancy and lactation. Approve wording in section 6, item 5. Figures of about 200 mg (pregnancy) and about 300 mg (lactation) are UNVERIFIED secondary numbers; confirm against ACOG and the current Dietary Guidelines before using any.
- Age. 21+ or 18+; checkout age verification; adult-signature delivery (is it required, given the $9 to $11 fee).
- Nicotine look-alike. Do the flavor names, format (small tin and pouch), and use instruction look like nicotine pouch products? Does "Contains no nicotine or tobacco" help or hurt?
- School and state laws. State laws and the school-ban trend were not researched; some places treat caffeine pouches as simulated tobacco (SRC: AP/Fortune).
- Adverse events. Responsible-person duties, 15-business-day reporting, 6-year records, domestic address or phone on the label.
- Allergen labeling (FASTER Act sesame, 321(qq)), Prop 65, and whether a "dietary supplement" statement is needed.
- Child-resistant packaging. Is it required or advisable; can Delphine say "child-resistant" on the tin; does voluntary CR change liability?
- Contract terms. Quality agreement, recall, insurance, exclusion of nicotine cross-contact, and due diligence on any maker with an FDA warning letter (Daily Manufacturing Solutions, Apr 21 2026, nicotine pouches; SRC).
- Names. Clearance of DELPHINE with a trademark attorney; neighbors DELPHINOL (Class 5), DELFINA and SANTA DELFINA (SRC: CLAUDE.md). Product names are working names only.

For the manufacturer and an independent lab (questions)
- All items in sections 3 and 5: caffeine source and COA, pouch material, fill weight, tolerance and uniformity, per-lot microbial, heavy metals, nicotine non-detect, allergen program, stability and best-by, CR tin options, MOQ, lead time, facility registration and cGMP standard.

For an accountant or insurance broker
- Product liability cover for a caffeine product sold to a nurse audience; real COGS and 3PL fees to replace the $2.50 and $5.50 assumptions.

---

## Decisions needed (for the coordinator to log; I did not edit decisions.md)

1. 2026-10-27 | product-development | Draft Delphine lineup: 4 working products (Lemon Slim 4-pack, Ginger Slim 3-pack, Black Tea Regular 4-pack, optional Spearmint Regular 3-pack), all 25 mg, 20 pouches per tin (500 mg per tin) | Owner to approve, cut or change the flavors; decide whether to keep Spearmint (nicotine look-alike risk).
2. 2026-10-27 | product-development | Tin size 20 and 3- to 4-tin first-order floor are assumptions based on an unquoted COGS of $2.50 | Obtain real maker quotes at 15 and 20 per tin before fixing tin size, bundles or price.
3. 2026-10-27 | product-development | Label drafts (caffeine per pouch, serving, daily total, pregnancy and lactation caution, 21+) need counsel; 16 pouches = 400 mg, 8 = 200 mg (equals the UNVERIFIED pregnancy figure) | Owner and counsel to pick the daily-cap wording and age policy; record the age policy in decisions.md.
4. 2026-10-27 | product-development | Child-resistant tins are not required by any rule found (CPSC list silent on caffeine) but one tin holds 500 mg | Owner to decide voluntary CR tins after cost quotes; counsel to confirm.
5. 2026-10-27 | product-development | Supplement-vs-food classification still unresolved; it controls label panel, cGMP and test scope | Counsel written view before any RFQ goes out.
6. 2026-10-27 | product-development | Ingredient exclusions proposed (no nootropics, vitamins, extra caffeine sources, cooling agents, xylitol, colorants) | Owner to approve the exclusion list so makers quote the same plain spec.
