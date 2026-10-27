# Delphine: contract maker and co-packer shortlist, comparison and RFQ drafts

Date: 2026-10-27 (every "checked" date below is 2026-10-27). Agent: sourcing. Nothing was sent, called, signed or paid for. Age policy not yet recorded in `work/decisions.md`, so 21+ is assumed. Compliance gate NOT cleared, so this file recommends conversations and quotes only, not inventory or deposits.

## Labeled assumptions (NOT decisions)

- ASSUMPTION: 20 pouches per tin.
- ASSUMPTION: first production run roughly 5,000 to 25,000 tins, asked of suppliers as a range. Daily Manufacturing's self-reported minimum is 25,000 cans with 5,000 per flavor (UNVERIFIED, own site).
- ASSUMPTION: 3 to 4 flavors.
- 25 mg caffeine per pouch is settled (decisions.md). 25 mg x 20 = 0.5 g caffeine per tin (my arithmetic).

## What I could and could not check (read this first)

- Tools this run: WebSearch and WebFetch only. No Bash or curl was available, so openFDA (api.fda.gov) calls were attempted through WebFetch and returned HTTP 404 both times (food/enforcement endpoint). openFDA recall/enforcement, FDA Food Facility Registration, NSF live directory (HTTP 403 via WebFetch), Virginia SCC and VDACS, and FDA import alerts were NOT checked for any candidate. Every "FDA registered", "NSF", "cGMP" claim below is therefore UNVERIFIED.
- One primary record was re-read: the FDA CTP warning letter to Daily Manufacturing Solutions (confirmed below).
- Earlier work was not repeated: see `/home/user/bolt/research_notes/Bolt caffeine pouch launch research/sourcing.md` and `gap_federal_and_suppliers.md` for JD Quality, Global Snus, Luna, House of Pouches baseline reads.
- No candidate publishes price per tin, and none publishes a caffeine assay tolerance at 25 mg. Both are "not published" throughout.

## 1. Recommendation (one paragraph)

After the compliance gate is cleared by the owner (and counsel has said which regulatory category a non-swallowed pouch falls in), request quotes first from (1) JD Quality Pouches LLC (US, Virginia, offers formulation-to-canning and says short runs; it names NSF and a Virginia food license but no cGMP or FDA registration, so ask for all certificates before any other step), (2) Daily Manufacturing Solutions (US, California, the only candidate with a published MOQ, lead time and capacity, and a Thomasnet-listed FDA registration dated 12-20-24, but it holds an April 2026 FDA tobacco warning letter for nicotine pouches, so ask hard questions about nicotine line segregation and whether it is a sound counterparty), and (3) a US stick-pack maker that claims NSF-audited cGMP, Pharmatech Labs (Utah), as a format fallback in case counsel concludes a swallowed supplement format is easier to place, or if the two pouch makers fail diligence. Overseas makers (Lithuania, Poland, Denmark, Sweden) come second because duties, foreign-facility registration and longer freight are unresearched. This ranking is judgment from thin, mostly self-reported evidence; it is not a verification of any firm.

## 2. Candidate table

Ranking by estimated landed cost per tin is NOT possible: no candidate publishes a price. Order below is by evidence quality (best first), not cost. Landed-cost column is "not published" for all; see section 7 for assumption ranges.

| # | Company | Location | Type | MOQ / lead time (self-reported) | Price/tin at 3 volumes | Claimed standards (all UNVERIFIED unless noted) | Source (checked 2026-10-27) |
|---|---|---|---|---|---|---|---|
| 1 | Daily Manufacturing Solutions Inc. (dlymfg) | Rancho Cucamonga, CA (9119 Milliken Ave); also listed Fontana and La Verne | US pouch co-packer, caffeine + nicotine + nootropic | 25,000 cans; 5,000/flavor; ~6 weeks; 200,000 cans/day claimed | Not published | "FDA registered", "GMP certified"; Thomasnet: FDA FFR cert dated 12-20-24, ISO 9001:2015, cGMP; own blog headline claims "CGMP + NSF" but gives no standard, certificate number or date; a web search found NSF listings only for other firms | [dlymfg.com](https://dlymfg.com), [co-manufacturers profile](https://www.comanufacturers.com/manufacturers/daily-manufacturing), [Thomasnet](https://www.thomasnet.com/company/daily-manufacturing-solutions-inc-30869349/profile), [NSF blog page](https://dlymfg.com/blog/how-caffeine-pouches-work-what-brands-need-to-know/) |
| 2 | JD Quality Pouches LLC | 2050 Val Park Dr, Oilville VA 23129 | US private label / contract, caffeine and CBD pouches | Not stated; "short runs to long-term" | Not published | "NSF Certified, USDA Organic, VA Food Manufacturing License, HAACP"; no cGMP or FDA registration number; no certificate numbers | [jdqualitypouches.com](https://jdqualitypouches.com), [Wonnda](https://wonnda.com/suppliers/jd-quality-pouches-llc/) |
| 3 | PouchWorx | USA (city not found) | Named only in a competitor-seller roundup | Not stated | Not published | "FDA-registered, cGMP-compliant" per roundup | [BAE Vapor roundup](https://baevapor.com/caffeine-pouch-manufacturers-usa/) (seller's own marketing). Search for the company name returned nothing; existence not confirmed |
| 4 | Pharmatech Labs | Lindon, UT | US supplement contract maker, stick packs; NOT a pouch maker | Not checked | Not published | "FDA and NSF certified, cGMP" per search snippet | [Wonnda](https://wonnda.com/suppliers/pharmatech-labs/) (directory) |
| 5 | Jelsert | North America (site) | US stick-pack producer | Not checked | Not published | "NSF Certified Manufacturer (GMP Registered for Functional Foods and Sports Nutrition)" per own snippet | [jelsert.com](https://jelsert.com/pages/capabilities) (snippet only) |
| 6 | Superior Supplement Manufacturing | US (not checked) | Supplement contract maker incl. stick packs and sachets | Not checked | Not published | "FDA and cGMP certified facilities audited by third parties incl. NSF" per snippet | [superiorsupplementmfg.com](https://www.superiorsupplementmfg.com/) (snippet only) |
| 7 | Global Snus | Vilnius, Lithuania | EU pouch maker; Ignite caffeine line | Not stated | Not published | "GMP certified" (type unnamed) | [globalsnus.com](https://globalsnus.com) (earlier read) |
| 8 | Luna Corporate | Suchy Las, Poland | EU pouch maker; Cafero caffeine | Not stated | Not published | None named | [lunacorporate.com](https://lunacorporate.com) (earlier read) |
| 9 | House of Pouches ApS | Denmark | Tobacco-free pouches; BLOW and POKE lines on Danish register | "4 weeks from approval" per directory | Not published | None found | [Wonnda](https://wonnda.com/de/lieferanten/house-of-pouches/); [Danish SIK register](https://www.sik.dk/en/registre/list_of_registered_tobacco_surrogates?page=9) (confirms ApS registered products; not caffeine) |
| 10 | Microzero AB | Hildedalsgatan 172, Gothenburg, Sweden | White-label nicotine-free pouch producer (Zeronito) | Not found | Not published | None found; 4 to 19 employees (sources conflict) | [funnelfeedr](https://funnelfeedr.com/sv/company/se/microzero-ab-5592288889), [Northerner retailer](https://www.northerner.com/at/zeronito/zeronito-liquorice-original-nicotine-free-pouches) |
| 11 | Fertin Pharma | Denmark | Gum / lozenge CDMO; Energy Gum 50 and 100 mg | Not found | Not published | Certificates listed but unnamed on CPHI | [CPHI](https://www.cphi-online.com/product/energy-gum-100-2/) via search (page 403 on fetch) |
| 12 | Smitify Group Ltd (OEMNicotine.com / caffeinepouchmanufacturer.com) | Hong Kong office; production "support" Sweden, Indonesia, China | Broker-like; 50M+ pouches/month claimed | Not stated | Not published | "FDA-registered, GMP, ISO 9001, CE"; no registration number; certificates shown as images | [site page](https://caffeinepouchmanufacturer.com/pages/fda-registered-and-gmp-certified-manufacturer) |
| 13 | BAE Vapor | Shenzhen, China | Vape/pouch OEM; publisher of the roundup that ranks itself first | Not stated | Not published | None stated | [baevapor.com](https://baevapor.com/caffeine-pouch-manufacturers-usa/) |

Names that appeared in secondary sources and could NOT be found: AmeriPouch (USA), Patriot Pouches (Las Cruces NM), Nicopack (Poland). Treat as nonexistent until a primary page is found. HTT Packaging & Design (CA, stick packs, "NSF organic and SQF") remains a weak stick-pack lead from the earlier note ([CMTC](https://www.cmtc.com/made-in-california-profile/htt-packaging-design)). Gumtech (gum) status unverified.

## 3. Primary-record checks performed

| Item | Result |
|---|---|
| FDA warning letter to Daily Manufacturing Solutions Inc. | Confirmed on fda.gov: Center for Tobacco Products, April 21, 2026, product "PUCK COOL MINT 6MG" nicotine pouch; no marketing authorization order; adulterated (FD&C 902(6)(A)) and misbranded (903(a)(6)). Caffeine and dietary supplement not mentioned. Close-out/response not found. [FDA letter](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/daily-manufacturing-solutions-inc-728255-04212026) |
| openFDA recalls/enforcement (api.fda.gov) | Not reachable (HTTP 404 via WebFetch). Not checked for any candidate. |
| FDA Food Facility Registration | Not reachable. Only Thomasnet's "certificate dated 12-20-24" for Daily, number not shown. |
| NSF directory | HTTP 403. A web search found no NSF listing for Daily Manufacturing (listings found were other firms). JD Quality's "NSF Certified" not checked. Note: NSF certifies the facility's program, not the product (competitor Roon's own explainer). |
| Virginia SCC / VDACS | Searches returned no record for JD Quality; SCC search tool itself not queried. No independent web trace of JD Quality beyond Wonnda and its own site (its site header reads "Dan Victor, Just another WordPress site"; builder credit "Kyle Weidner"; no owner named). |
| Daily Manufacturing identity | Conflicts: founded 2019 vs "over 20 years"; revenue under $5M (ZoomInfo) vs $10M-$50M (co-manufacturers page); sq ft 40,000 vs 45,000; multiple addresses. Treat all as self-reported. |
| Smitify (OEMNicotine) | Registration number 77346730 shown on its page for a Hong Kong company; not checked against the HK registry. |

## 4. Red flags and five call questions per supplier

Common flags for all: price, tolerance and COA practice not published; certificates asserted without numbers. Common core (ask every one): what is your assay tolerance at 25 mg per pouch and how is it tested; can I see a COA for a comparable lot; is nicotine ever run on this line or in this building; what is your MOQ per flavor; who is the responsible person for adverse events.

**1. Daily Manufacturing.** Flags: FDA CTP warning letter (nicotine, Apr 2026); runs nicotine pouches in the same business, line sharing unknown; NSF claim without scope or number; contradictory company facts; caffeine strengths listed 50-150 mg only. Questions: (1) Is caffeine filled on a dedicated line or room with documented changeover and nicotine-residue testing? (2) What is the status of the April 2026 FDA letter and has it affected operations? (3) Show the NSF certificate (standard, number, scope, date) and your FDA registration number. (4) Can you hold 25 mg per pouch and what is your content-uniformity data? (5) Price per tin at 5k, 15k and 25k tins, setup fees, and sample cost.

**2. JD Quality.** Flags: no FDA registration or cGMP stated; phone area code 646 and Richmond/Oilville wording mismatch; no owner named; no independent trace found; "HAACP" misspelling on a certification claim. Questions: (1) Who owns the company, and can I visit? (2) Provide NSF certificate, VA license and FDA registration numbers. (3) Do you make any nicotine product here? (4) Who tests caffeine per pouch, by what method, how often? (5) Who supplies tins and fleece, and what is the sample policy?

**3. PouchWorx.** Flags: appears only in a competitor's marketing roundup; no site found. Questions: (1) Legal entity, address and website? (2) FDA registration number? (3) Nicotine on site? (4) Caffeine assay method and tolerance at 25 mg? (5) MOQ, lead time, price per tin?

**4. Pharmatech Labs (stick pack).** Flags: not a pouch maker; format change alters the product; NSF claim from directory snippet. Questions: (1) Do you run caffeine at 25 mg per serving and what assay tolerance? (2) NSF certificate and scope (NSF/ANSI 173?) (3) MOQ and price per 20 sticks? (4) Allergen control and shared-line policy? (5) Private-label artwork and COA per lot?

**5. Jelsert.** Flags: snippet-only; not pouch. Questions: (1) Current NSF listing (GMP Registered) number? (2) Caffeine experience and tolerance at 25 mg? (3) MOQ per flavor? (4) Tins or alternative packaging? (5) Responsible person and recall insurance?

**6. Superior Supplement Manufacturing.** Flags: snippet-only; pouch capability unknown. Questions: (1) Do you do oral pouches or only stick packs/sachets? (2) Third-party audit reports (who audits)? (3) COA practice per lot? (4) MOQ and price? (5) Product liability and recall coverage?

**7. Global Snus.** Flags: "GMP" not equal to 21 CFR 111; EU facility, so FDA foreign facility registration and import clearance questions; tobacco-sector orientation; no price or MOQ. Questions: (1) Which GMP standard, who audits, certificate copy? (2) Nicotine on the same line? (3) Experience exporting to the US and FDA registration number? (4) 25 mg tolerance and assay? (5) Incoterms, duties, freight per pallet?

**8. Luna Corporate.** Flags: no certifications named; own nicotine and energy brands (competitor risk and line-sharing); Polish-language site. Questions: (1) Certificates (ISO 22000, IFS, other)? (2) Do you make nicotine pouches in the same facility? (3) Will you sign an exclusivity/confidentiality agreement given your own Cafero brand? (4) Tolerance at 25 mg? (5) US export experience and landed-cost basis?

**9. House of Pouches.** Flags: no own website found; "4-week lead time" is directory-only; Danish market regulating caffeine sachets (draft order Feb 2026, [NutraIngredients](https://www.nutraingredients.com/Article/2026/02/12/authorities-play-catch-up-on-caffeine-energy-pouch-regulation)) which may affect their business. Questions: (1) Legal entity, site, facility address? (2) Certificates and registration numbers? (3) Which products share the line (BLOW/POKE are listed on the Danish tobacco-surrogate register)? (4) 25 mg tolerance, assay lab? (5) MOQ, price, samples?

**10. Microzero AB.** Flags: tiny (4-19 staff, sources conflict); no site found; caffeine capability not shown. Questions: (1) Do you make caffeine pouches? (2) Capacity and quality certificates? (3) Nicotine or tobacco on site? (4) Assay and tolerance? (5) MOQ, freight to US, FDA registration?

**11. Fertin Pharma.** Flags: gum/lozenge, not pouch; caffeine strengths 50 and 100 mg listed; MOQs likely large (UNVERIFIED); caffeine gum history (Wrigley paused Alert gum in 2013 after FDA concern, [FoodNavigator](https://www.foodnavigator-usa.com/Article/2013/05/20/Wrigley-halts-production-of-caffeine-gums-on-FDA-concerns)). Questions: (1) Can you make 25 mg gum or lozenge? (2) FDA registration, cGMP/Part 111 status? (3) MOQ and price? (4) US customers for private label? (5) Assay tolerance?

**12. Smitify / OEMNicotine / caffeinepouchmanufacturer.com.** Flags: Hong Kong office with production "support" in three countries (trading-company pattern); certificates as images with no numbers; no nicotine segregation described though same group runs a nicotine-pouch site; no MOQ. Questions: (1) Which factory makes my product, address, and may I audit? (2) FDA registration number of that factory? (3) Nicotine segregation? (4) COA per lot and independent lab? (5) Payment terms and who bears loss in transit? Recommendation: do not proceed without a named factory.

**13. BAE Vapor.** Flags: self-ranked first in its own roundup; vape orientation; no certifications. Questions: same as 12. Low priority.

## 5. Ingredient and packaging inputs (leads, not verified)

| Input | Lead | Evidence | Notes |
|---|---|---|---|
| Caffeine anhydrous USP/FCC | Lab Alley (US reseller), Xenex Labs (20 kg listed at $0.05/g per search; earlier note found it marked unavailable), Sigma-Aldrich food-grade W222455 (bulk by request), an Indian maker via Globallinker (50 kg MOQ) | [Lab Alley](https://laballey.com/products/caffeine-usp), [Xenex](https://www.xenexlabs.com/products/caffeine-anhydrous-powder-fcc-usp), [Sigma](https://www.sigmaaldrich.com/US/en/product/sial/c7731), [Globallinker](https://www.globallinker.com/products/caffine-powder-7791798) | Most co-packers source their own; ask who and ask for origin on the COA (Lab Alley sample COAs show both US and China lots). Active cost is small: 0.5 g per tin. |
| Pouch fleece / nonwoven | Nonwovenn (Somerset UK), TENOWO GmbH (Germany) | [Textile World](https://www.textileworld.com/?p=101876), [UniBo listing](https://adu.unibo.it/pack/en/actors/tenowo) | Viscose-based; no food-contact documents, price or MOQ seen. Release behavior may differ without nicotine. |
| Sweeteners | Not sourced; pouch studies report sucralose and acesulfame-K use | [Roon guide](https://www.takeroon.com/guides/what-is-actually-in-a-focus-pouch) (competitor) | Biostevera (earlier note) is a stevia lead. Ask the co-packer. |
| Flavor and bitter masking | Comax Flavors lists caffeine maskers; major houses not checked | [NutritionInsight](https://nutritioninsight.com/news/comax-flavors-unveils-caffeine-maskers-and-bitter-blockers-for-nootropics.html) | Flavors must avoid candy/minor appeal (project rule 4). |
| Rectangular tins | Berlin Packaging (rectangular slip-cover and child-resistant items; origin not checked); Promotional Product Inc (US-made CR hinged tin, 150 minimum, joint/edible format); China factories on made-in-china.com | [Berlin](https://www.berlinpackaging.com/rectangular-slip-cover-tins), [PPI](https://www.promotionalproductinc.com/child-resistant-joint-edible-hinged-tin-box-with-see-through-window) | CR is voluntary on current findings (16 CFR 1700.14 lacks caffeine, per earlier note); CPSC's maker list is dated 2010 ([CPSC](https://www.cpsc.gov/Regulations-Laws--Standards/Statutes/Poison-Prevention-Packaging-Act/Manufacturers-of-Child-Resistant-Senior-Friendly-Packaging)). Tin price not published. |

## 6. Request-for-quote DRAFT (do not send)

Subject: RFQ - private-label nicotine-free oral caffeine pouches, 25 mg per pouch

Hello [Name],

We are an early-stage US brand evaluating contract makers for a nicotine-free, tobacco-free oral caffeine pouch, 25 mg caffeine per pouch, for adult consumers. We are at the information-gathering stage and have not committed to a supplier. Please send what you can on the points below.

Working assumptions, subject to change: 20 pouches per tin; 3 to 4 flavors; first run of roughly 5,000 to 25,000 tins in total (please tell us your minimum per flavor and per run).

1. Pricing: price per tin at 5,000, 15,000 and 25,000 tins; one-time setup, tooling and artwork fees; tin, lid and label cost shown separately; payment terms and deposit.
2. Lead time for first run and for repeat runs; MOQ per flavor.
3. Caffeine assay: method (e.g., HPLC), who performs it (in-house or named third-party lab), frequency (per lot or per sample plan), and the tolerance you hold on 25 mg per pouch. Please share content-uniformity data if available.
4. Certificate of analysis for every lot, including identity, assay, microbial and heavy metals.
5. Facility: address, FDA food facility registration number, and whether you manufacture to 21 CFR Part 111 (dietary supplement cGMP) and/or Part 117; copies of third-party audit certificates (certifier, number, scope, expiry).
6. Nicotine-free line segregation: do you manufacture nicotine or tobacco products at this site? If so, describe dedicated rooms/lines, changeover cleaning, and any testing for nicotine carryover. Have you received any FDA warning letter, Form 483 or recall in the last five years?
7. Allergen control program and allergen statement for the fleece, sweeteners and flavors.
8. Materials: pouch fleece material and supplier, caffeine source and grade (USP/FCC) and origin, sweeteners, flavor supplier.
9. Packaging: tin options (rectangular, child-resistant), label and printing capability, artwork specifications and who owns tin inventory.
10. Samples: what is available, cost, and timing; whether sample cost is credited against an order.
11. Private-label terms: confidentiality, formulation ownership, exclusivity, and what artwork or regulatory text you require from us.
12. Adverse events and recalls: who acts as the responsible person for adverse event reports, how complaints reach us, and your recall procedure and insurance (product liability and recall limits).
13. Two references from comparable private-label customers if possible.

We may later ask for a quality agreement. Thank you; happy to arrange a call.

[Name, Delphine, phone]

### Short personalized follow-ups (drafts; edit before use)

- Daily Manufacturing: "Thank you for the published 25,000-can minimum. Beyond the RFQ, could you tell us how caffeine production is separated from your nicotine pouch work, and whether the NSF certification on your blog covers the caffeine filling line (certificate number and scope)? We also noticed FDA's April 2026 letter and would like your account of its status."
- JD Quality: "Your site lists NSF, a Virginia food manufacturing license and HACCP. Could you send the certificate numbers and your FDA food facility registration number, and tell us who owns and operates the facility? We would also like a short video visit if possible."
- PouchWorx: "We saw PouchWorx described as a US FDA-registered maker but could not find a website. Could you confirm your legal entity, address and registration number?"
- Pharmatech Labs / Jelsert / Superior: "We are mainly evaluating oral pouches but are open to a stick-pack format. Can you run 25 mg caffeine per serving, and what assay tolerance and NSF scope apply?"
- Global Snus / Luna / House of Pouches / Microzero: "Please also confirm FDA foreign facility registration status, US export experience, Incoterms, and who bears import duties and customs clearance."
- Fertin: "Do you supply private label 25 mg caffeine gum or lozenge to US customers in small runs? Please include MOQ and cGMP/registration status."
- Smitify / BAE Vapor: "Before any quote, please name the factory that would make our product, its address, and the FDA registration number for that factory."

## 7. Cost assumptions (all ASSUMPTION unless sourced)

- Co-packer price per tin: NOT PUBLISHED by any candidate. The only published-ish figures are an unreliable China agent blog (earlier note). No number used here as fact.
- Scenario COGS per 20-pouch tin used in the existing model: $1.50 / $2.50 / $3.50 (ASSUMPTION from `unit_economics.md`, no source).
- Caffeine active cost per tin: 0.5 g x $0.05/g = $0.025 (Xenex listing, availability unconfirmed); 0.5 g x $455/kg = $0.23 (Sigma lab reagent, upper bound).
- Overseas landed cost: duties, freight, FDA prior notice and broker fees NOT researched. Add as unknown. Not computed.
- Inventory exposure at the scenario range: 5,000 tins x $1.50 to $3.50 = $7,500 to $17,500; 25,000 tins x $1.50 to $3.50 = $37,500 to $87,500 (my arithmetic on ASSUMPTION costs; not a quote).
- Child-resistant tin premium: not published.

### Cost figures for finance (paste-ready)

| Item | Value | Basis | Status |
|---|---|---|---|
| Pouches per tin | 20 | Owner placeholder | ASSUMPTION |
| Run size to quote | 5,000 / 15,000 / 25,000 tins | Owner placeholder; Daily MOQ 25,000 | ASSUMPTION |
| Co-packer price per tin | not published | No candidate publishes | UNKNOWN, RFQ needed |
| Scenario COGS per tin | $1.50 / $2.50 / $3.50 | Prior model | ASSUMPTION |
| Caffeine per tin | $0.025 to $0.23 | 0.5 g at $0.05/g to $455/kg | Computed; supplier prices UNVERIFIED |
| Tin and lid | not published | | UNKNOWN |
| Fleece | not published | | UNKNOWN |
| Flavor, sweetener | not published | | UNKNOWN |
| Setup, tooling, artwork | not published | | UNKNOWN |
| Sample cost | not published | | UNKNOWN |
| Lead time (Daily) | about 6 weeks | Own site | Self-reported |
| Lead time (House of Pouches) | 4 weeks | Directory | UNVERIFIED |
| Overseas duties and freight | not researched | | UNKNOWN |
| Product liability insurance | $700 to $4,500/yr | Broker blogs in prior note | UNVERIFIED |

## 8. For a professional

Counsel (FDA / food and supplements):
- Which category applies to a non-swallowed pouch (dietary supplement vs conventional food), because it decides Part 111 vs Part 117, label format, and whether swallowed formats (stick pack, gum, lozenge) are cleaner. Do not commit to a supplier before this is answered.
- Supply agreement and quality agreement: who is responsible for specifications, release testing, batch records, retained samples, COA acceptance, and recall cost; right to audit; right to refuse lots; specification at 25 mg with a stated tolerance and consequence for failure.
- Nicotine segregation: contractual warranty and audit rights; whether sharing a facility with a company that has an FDA tobacco warning letter is acceptable, and whether to require a dedicated line. Cross-contact liability.
- Adverse event responsibility: who is the "responsible person" under the label (the name on the label), intake process, and who may submit reports on whose behalf.
- Intellectual property: formulation ownership, flavor exclusivity, non-compete if the maker has its own caffeine brand (Luna), confidentiality, artwork/trademark license while DELPHINE is uncleared.
- Import: for overseas makers, foreign facility registration, prior notice, importer-of-record duties, and tariff classification (customs broker).
- Child-resistant packaging: advisable or required; testing standard and who certifies.

Insurance broker:
- Product liability limits suitable for a caffeine product, recall and contamination coverage, whether the co-packer's policy names Delphine as additional insured, vendor's endorsement, coverage for a supplement-vs-food classification dispute, and whether insurers require NSF/Part 111 evidence.

Accountant:
- Deposit and inventory risk at 5,000 to 25,000 tins, payment terms, tariff treatment, landed-cost accounting.

## 9. Decisions needed (for the coordinator to log; I did not edit decisions.md)

1. Owner to confirm or replace the placeholders: 20 pouches per tin, 5,000 to 25,000 tin first run, 3 to 4 flavors, so RFQs can be sent after the gate.
2. Owner to decide whether a maker that also produces nicotine pouches (Daily Manufacturing, and probably Global Snus, Luna, House of Pouches, Microzero, Smitify) is acceptable, and whether to require a dedicated nicotine-free line.
3. Owner to approve a browser-based verification pass (a human, since tools here could not reach them): FDA Food Facility Registration, openFDA/FDA recall and warning letter search, NSF certified-company search, Virginia SCC and VDACS, Hong Kong registry for Smitify.
4. Owner to decide whether to also quote a swallowed format (stick pack, gum, lozenge) pending counsel's classification answer.
5. Owner to approve sending the RFQ draft (section 6) only after the compliance gate is cleared and the DELPHINE name is with a trademark attorney.
6. Owner to decide whether child-resistant tins are required by Delphine's own policy (voluntary on current findings, counsel to confirm).
