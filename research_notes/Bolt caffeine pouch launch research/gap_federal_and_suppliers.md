# Gap-fill: US federal labeling/manufacturing rules for an oral caffeine pouch, and public-record checks on contract makers

Date checked for every item: 2026-10-27 (eCFR items fetched from the eCFR versioner snapshot dated 2026-10-20 unless noted). Research only. Nothing here concludes that any practice is legal, compliant or safe. Tools: WebSearch/WebFetch (Firecrawl out of credits). Items I could not read from a primary page are marked UNVERIFIED. "Cornell LII" pages are a mirror of the U.S. Code, not a government site; flagged where used. WebFetch answers come from a small model summarizing the page, so quotes are as returned and should be spot-checked by counsel against the cited URL.

Housekeeping note: the project CLAUDE.md says deliverables go in work/<agent>/. This file is saved at the path the assignment named, and work/decisions.md was NOT edited, as instructed. Findings that probably change a decision are listed at the end ("Candidates for decisions.md") for the owner/coordinator to add.

---

## 1. 21 CFR Part 111 (dietary supplement cGMP) for a contract-made product

### Takeaway
Part 111 applies to anyone who manufactures, packages, labels or holds a dietary supplement, including a product made by one firm and packaged/labeled by another. Part 111 requires identity testing of dietary-ingredient components and verification that each finished batch meets identity, purity, strength and composition specifications. The text I retrieved does not assign brand-owner vs. manufacturer duties in contract arrangements; I could not retrieve the FDA guidance that does (404). This whole section only matters if the product is a "dietary supplement" at all (see section 4).

### Cited Findings
- Scope, 21 CFR 111.1(a): a person is subject to Part 111 if they "manufacture, package, label, or hold" a dietary supplement, including one "you manufacture but that is packaged or labeled by another person," and imports. Retail establishments holding product solely for direct sale to individual consumers are exempt from the holding requirements only; warehouses/storage serving retailers or that sell directly to consumers are not "retail establishments." The retrieved section does not use the term "contract manufacturer" — [eCFR 21 CFR 111.1](https://www.ecfr.gov/api/versioner/v1/full/2026-10-20/title-21.xml?part=111&section=111.1) (2026-10-27)
- 21 CFR 111.75(a)(1)(i): must "conduct at least one appropriate test or examination to verify the identity of any component that is a dietary ingredient" (unless FDA grants an exemption petition); 111.75(a)(2): other components' identity/specs verified by own testing or by reliance on a qualifying supplier certificate of analysis — [eCFR 21 CFR 111.75](https://www.ecfr.gov/api/versioner/v1/full/2026-10-20/title-21.xml?part=111&section=111.75) (2026-10-27)
- 21 CFR 111.75(c): must "verify that your finished batch of the dietary supplement meets product specifications" (statistically sound sample or every batch); specifications for identity, purity, strength and composition must be selected and tested; documented basis must be reviewed and approved by quality control personnel; 111.75(h): tests must be "appropriate, scientifically valid methods" — same eCFR link (2026-10-27)
- Caffeine is a dietary-ingredient-type component only if the product is a supplement; for a caffeine pouch, "strength" (mg caffeine per pouch) would be the specification FDA's Part 111 batch testing targets. This is my reading of 111.75(c), not an FDA statement about pouches.

### Inferences
- If a brand owner's name is on the label, the brand is the "responsible person" for adverse events (section 2) and is a person who "labels" or has product "manufactured... by another" for scope purposes. Whether the brand owner has independent Part 111 release/quality-unit obligations when a contractor does all steps is a legal-interpretation point not resolved by the text I read.
- A candidate maker that says only "GMP certified" (Global Snus, Daily Manufacturing site) has not said it complies with Part 111 specifically.

### Gaps
- FDA's Part 111 Small Entity Compliance Guide URL I tried returned 404; FDA's 2007 final-rule preamble discussion (who is responsible when operations are contracted out) was not retrieved. Counsel should read it.
- Other Part 111 subparts (quality control unit 111.65-111.140, master manufacturing record, complaint handling 111.553, recordkeeping 111.605-111.610) were not fetched.

---

## 2. Adverse event reporting and required label statements

### Takeaway
For supplements, the person whose name is on the label is the "responsible person" who must receive and report serious adverse events within 15 business days and keep records 6 years; the label must carry a domestic address or phone. The user's cited "21 CFR 101.11" does not appear to be the right cite for supplement AE/label content (101.11 is not a supplement provision in my understanding; I did not fetch it) — the AE/address rules are in FD&C Act 761 (21 U.S.C. 379aa-1) and 403(y) (21 U.S.C. 343(y)). Supplement Facts is 21 CFR 101.36.

### Cited Findings
- 21 U.S.C. 379aa-1 (FD&C Act 761): the "responsible person" is the manufacturer, packer or distributor whose name appears on the label under 343(e)(1); serious adverse event report due to FDA no later than 15 business days after receipt; new medical information within 1 year also due within 15 business days; records kept 6 years and open to inspection; a retailer-distributor may by agreement authorize the manufacturer/packer to submit the reports — [Cornell LII 21 USC 379aa-1](https://www.law.cornell.edu/uscode/text/21/379aa-1) (mirror; 2026-10-27; verify on uscode.house.gov)
- 21 U.S.C. 343(y): supplement label must include "a domestic address or domestic phone number through which the responsible person" may receive a serious adverse event report — [Cornell LII 21 USC 343](https://www.law.cornell.edu/uscode/text/21/343) (2026-10-27; paraphrase returned by tool, exact subsection text not displayed)
- 21 U.S.C. 343(e)(1): label of packaged food must show "the name and place of business of the manufacturer, packer, or distributor" — same LII link (2026-10-27)
- 21 U.S.C. 343(s)(2): supplement misbranded if label fails to list each 321(ff) ingredient with quantity, or fails to identify the product using the term "dietary supplement" — same LII link (2026-10-27)
- 21 U.S.C. 343(w): major food allergen labeling via "Contains [source]" after the ingredient list or parenthetical in the ingredient list; definition of major food allergen sits in 321(qq) (not retrieved) — same LII link (2026-10-27). The FASTER Act (sesame as ninth allergen) text and effective date were NOT fetched: UNVERIFIED here.
- 21 CFR 101.36 Supplement Facts format and caffeine's "Daily Value not established" handling: see earlier note — [federal_regulation.md section 3](federal_regulation.md) (sibling file; underlying eCFR link in that file)
- 21 CFR 101.93(c)(1): structure/function claims require disclaimer: "This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease."; 101.93(a): notify FDA Office of Dietary Supplement Programs within 30 days of first marketing a product with such a statement, with firm name/address, statement text, product name; signed certification of substantiation — [eCFR 21 CFR 101.93](https://www.ecfr.gov/api/versioner/v1/full/2026-10-20/title-21.xml?part=101&section=101.93) (2026-10-27)

### Inferences
- Bolt's CLAUDE.md bars health/performance claims; if no structure/function claim is made, 101.93 notification may not be triggered, but this is a counsel question (what counts as a structure/function claim for "energy" wording).
- The label of a product made by a contractor but branded Bolt makes Bolt the AE "responsible person" unless the label names the manufacturer/packer instead (statute text above), so Bolt would need an AE intake process (domestic phone/address, 6-year records).

### Gaps
- 21 CFR 101.3 statement of identity, 101.5 name/place details, 101.105 net quantity, 101.4 ingredient listing: not fetched.
- FASTER Act text and effective dates; allergen status of the likely pouch components: not fetched.
- Whether a "dietary supplement" label statement is accurate for a non-swallowed pouch (section 4).

---

## 3. Caffeine: NDI notification and GRAS

### Takeaway
GRAS: the only caffeine listing I found in the CFR is 21 CFR 182.1180, which is limited to cola-type beverages. I found no FDA GRAS listing or notice covering caffeine in pouches. NDI: the FDA page I tried 404'd, so I have no primary text on whether caffeine counts as an old dietary ingredient.

### Cited Findings
- 21 CFR 182.1180 "Caffeine": GRAS "when used in cola-type beverages" at a tolerance of 0.02 percent, in accordance with good manufacturing practice — [eCFR 21 CFR 182.1180](https://www.ecfr.gov/api/versioner/v1/full/2026-10-20/title-21.xml?part=182&section=182.1180) (2026-10-27)
- 2010 FDA position on caffeinated alcoholic beverages (caffeine not GRAS in that use) and a 2012 FDA Law Blog post on a caffeinated "breathable" product marketed as a supplement surfaced in search — [FDA Law Blog 2012](https://www.thefdalawblog.com/2012/02/breathable-food-comes-under-scrutiny/) — secondary; content not opened; UNVERIFIED

### Inferences
- If a pouch is treated as a conventional food rather than a supplement, 182.1180's cola-only listing suggests added caffeine in other foods would need a separate GRAS/food-additive basis. That is my reading, flagged for counsel — not an FDA statement about pouches.

### Gaps
- NDI: FDA NDI page returned 404; no primary source on caffeine as pre-October-1994 dietary ingredient or on any NDI notification for caffeine. UNVERIFIED.
- No FDA letter/Q&A specific to caffeine pouches found (searched again 2026-10-27; only the same secondary pages as in the earlier note).

---

## 4. Supplement vs. conventional food: the "form" question

### Takeaway
The statutory definition has two hooks relevant to a pouch: "intended for ingestion in a form described in" 21 USC 350(c)(1)(B)(i), and "not represented for use as a conventional food." Whether a pouch held in the mouth and not swallowed satisfies "ingestion" is contested by secondary sources; I found no FDA statement resolving it.

### Cited Findings
- 21 USC 321(ff): dietary supplement must be "other than tobacco," "intended to supplement the diet," contain a listed dietary ingredient (vitamin, mineral, amino acid, herb/botanical, "dietary substance... by increasing the total dietary intake," or concentrate/metabolite/constituent/extract/combination), be "intended for ingestion in a form described in section 350(c)(1)(B)(i)" (or comply with 350(c)(1)(B)(ii)), "is not represented for use as a conventional food or as a sole item of a meal or the diet," and be "labeled as a dietary supplement" — [Cornell LII 21 USC 321](https://www.law.cornell.edu/uscode/text/21/321) (mirror; 2026-10-27). The text of 350(c)(1)(B)(i) (tablet, capsule, powder, softgel, gelcap, liquid-drop forms) was not retrieved.
- A certification-industry blog argues non-swallowed pouches likely do not qualify as dietary supplements under DSHEA; other pages say pouches are "classified as dietary supplements"; no FDA statement found by search — [BSCG blog](https://www.bscg.org/blogs/single/energy-pouches-safety-ingredients-and-compliance-risk) (secondary; the earlier note found the fetched page did not contain this analysis, so UNVERIFIED), [Tobacco Insider Q&A](https://tobaccoinsider.com/caffeine-pouches-questions-and-answers/) (trade site, not FDA)
- Also see [federal_regulation.md sections 1-2](federal_regulation.md) for FDA's 2018 highly-concentrated-caffeine guidance and the June 2026 draft caffeine-labeling guidance agenda item.

### Inferences
- Classification drives everything downstream (Part 111 vs 21 CFR 117 food cGMP; Supplement Facts vs Nutrition Facts; GRAS/additive status; AE reporting). It is the single largest open question for counsel.

### Gaps
- No FDA letter, Q&A or warning letter on oral (non-swallowed) pouch products as supplements vs. foods found. FDA warning-letter database was not queried directly (not queryable via the tools).
- 350(c)(1)(B)(i) text; FDA's treatment of lozenges/gum (which are held in mouth) as supplement forms: not researched.

---

## 5. FTC: Endorsement Guides, ROSCA, health-claim guidance; H.R. 2511

### Takeaway
16 CFR 255 (revised July 2023) puts liability on the advertiser for misleading endorsements and undisclosed material connections; ROSCA (15 USC 8403) imposes three online negative-option requirements. H.R. 2511 shows as referred to House Energy and Commerce on March 31, 2025, with no confirmed movement; I could not open congress.gov (403).

### Cited Findings
- 16 CFR Part 255, issued at 88 FR 48102 (July 26, 2023): 255.1 advertisers can be liable for misleading endorsements or undisclosed material connections and should guide/monitor endorsers; 255.2 consumer endorsements about performance are claims the advertiser must substantiate and are not competent scientific evidence; typical-results rule ("should clearly and conspicuously disclose the generally expected performance in the depicted circumstances"), "results not typical" generally insufficient; 255.5 material connections (payment, free or discounted product, family/business ties) must be clearly and conspicuously disclosed; 255.6 practices fine for adults may draw scrutiny if directed at children — [eCFR 16 CFR 255](https://www.ecfr.gov/api/versioner/v1/full/2026-10-20/title-16.xml?part=255) (2026-10-27)
- ROSCA, 15 USC 8403: unlawful to charge for goods/services sold online through a negative option feature unless the seller (1) "clearly and conspicuously discloses all material terms" before collecting billing information, (2) obtains express informed consent before charging, and (3) provides "simple mechanisms for a consumer to stop recurring charges"; FTC enforcement is in 8404 — [Cornell LII 15 USC 8403](https://www.law.cornell.edu/uscode/text/15/8403) (mirror; 2026-10-27). 8402 and 8404 text not read.
- FTC health-products guidance, Reviews Rule (16 CFR 465) and negative option rulemaking status: see [federal_regulation.md section 4](federal_regulation.md) (FTC pages cited there).
- H.R. 2511, Sarah Katz Caffeine Safety Act, 119th Congress: Congress.gov bill page (per search result) shows "03/31/2025 Referred to the House Committee on Energy and Commerce"; GovTrack (data dated Dec 27, 2025) shows Introduced, 14 cosponsors (13 D, 1 R), 2% chance of enactment; a congress.gov-hosted page snippet with floor-vote tallies (413-0, 414-7) and different dates looks like a different bill or scraping artifact and should not be relied on — [Congress.gov H.R.2511](https://www.congress.gov/bill/119th-congress/house-bill/2511), [Actions](https://www.congress.gov/bill/119th-congress/house-bill/2511/actions), [GovTrack](https://www.govtrack.us/congress/bills/119/hr2511) (search summaries only; direct fetch of congress.gov returned 403 on 2026-10-27). A "Committee Meetings: 04/29/26" entry was mentioned in the search summary and not confirmed.

### Inferences
- Any influencer program (Bolt's own CLAUDE.md contemplates content) needs a disclosure and monitoring process under 255.1/255.5.
- Status of H.R. 2511 should be treated as "referred to committee, unconfirmed beyond that" until someone reads the Actions tab in a browser.

### Gaps
- Congress.gov actions tab not read directly; bill text/definitions (whether it reaches pouches) not read.
- ROSCA 8402/8404 and FTC penalty amounts not read.

---

## 6. Child-resistant packaging (Poison Prevention Packaging Act / CPSC)

### Takeaway
Caffeine is not in the CPSC's list of substances requiring special packaging at 16 CFR 1700.14(a) as retrieved; the only dietary-supplement entry is for iron-containing supplements (250 mg or more elemental iron). No PPPA requirement for caffeine pouches found. This is not a conclusion that none applies.

### Cited Findings
- 16 CFR 1700.14(a) lists 33 numbered categories (aspirin, acetaminophen, prescription drugs, iron-containing drugs, "dietary supplements... that contain an equivalent of 250 mg or more of elemental iron," ibuprofen, naproxen, lidocaine, mouthwash, and others); the word "caffeine" does not appear in the retrieved text — [eCFR 16 CFR 1700.14](https://www.ecfr.gov/api/versioner/v1/full/2026-10-20/title-16.xml?part=1700&section=1700.14) (2026-10-27; the retrieved summary lists 33 items; exact numbering vs. paragraph lettering should be checked)
- Test standard: child-resistance test at 16 CFR 1700.20 (80%+ child effectiveness; 90%+ senior-adult test) per a CPSC presentation cited in search results — [eCFR Part 1700](https://www.ecfr.gov/current/title-16/chapter-II/subchapter-E/part-1700) (search result only; 2026-10-27)
- Vendor/industry material on child-resistant tins for nicotine pouches is in [sourcing.md section 3](sourcing.md).

### Inferences
- Because the CPSC list is substance-specific and caffeine is absent, CR packaging for Bolt would be voluntary unless CPSC amends the list, FDA acts, or a state rule requires it (state laws are out of scope here). Voluntary CR is a business/risk decision for the owner and counsel.

### Gaps
- CPSC rulemaking activity on caffeine (any petition or ANPR) not searched. State CR rules not researched.

---

## 7. Public-record checks on named contract makers

### Takeaway
Most important new finding: FDA's Center for Tobacco Products issued a warning letter (April 21, 2026) to Daily Manufacturing Solutions Inc. for manufacturing and offering nicotine pouches without marketing authorization. The letter concerns nicotine, not caffeine, but it is a direct public-record hit on a named caffeine-pouch candidate that also makes nicotine pouches. FDA food-facility-registration and NSF directory lookups and the Virginia SCC search were not possible with these tools, so no candidate's registration or certification is verified.

### Cited Findings
**Daily Manufacturing Solutions Inc. (Daily Manufacturing; "dlymfg")**
- FDA warning letter ER2601477, April 21, 2026, from FDA Center for Tobacco Products (Office of Compliance and Enforcement) to Daily Manufacturing Solutions Inc., 9119 Milliken Avenue, Rancho Cucamonga, CA 91730 (copied to Puck LLC, Tuscaloosa AL). Product named: PUCK COOL MINT 6MG nicotine pouch. FDA says the firm "manufacture[s] and offer[s] for sale or distribution" nicotine pouch products lacking a marketing authorization order; classifies as adulterated (FD&C 902(6)(A)) and misbranded (903(a)(6)); 15 working days to respond; warns of possible civil money penalties, seizure, injunction — [FDA warning letter](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/daily-manufacturing-solutions-inc-728255-04212026) (2026-10-27). Whether the firm responded or the letter was closed out: not found.
- Own site: 9119 Milliken Ave, Rancho Cucamonga, CA 91730 and 7801 Cherry Ave, Fontana, CA 92336; phone 888-222-1575; co-packing, private label, contract manufacturing, 3PL, formulation; claims "FDA Registered Facility" and "GMP Certified" (page does not mention cGMP or NSF); caffeine, nicotine and nootropic pouches; caffeine pouches described as tobacco-free in 50-150 mg strengths; 100+ flavors; MOQ 25,000 cans with 5,000 cans per flavor; capacity 200,000 cans/day; lead time "as low as 6 weeks" — [dlymfg.com](https://dlymfg.com) (2026-10-27; animation counters on the page showed 0, tool used surrounding text; the first published MOQ/lead time found for any candidate, self-reported). Note: 25 mg is below the strengths listed on its site; fill feasibility unconfirmed.
- Thomasnet profile: Rancho Cucamonga CA; "Thomas Verified"; lists FDA Food Facility Registration (certificate dated 12-20-24), GMP/cGMP, ISO 9001:2015, organic certification; founded 2015 per business details but also "over 20 years of experience" (internal inconsistency); claims 200,000+ oral pouch units/day, 40,000 sq ft; press item gives a 1615 Yeager Ave, La Verne address — [Thomasnet](https://www.thomasnet.com/company/daily-manufacturing-solutions-inc-30869349/profile) (2026-10-27). Registration number not shown, so the FDA registration is UNVERIFIED. The earlier note (sourcing.md) located the firm only as La Verne via ZoomInfo; addresses in sources conflict (La Verne / Rancho Cucamonga / Fontana; one directory also lists Rockwell NC) — [ZoomInfo](https://www.zoominfo.com/c/daily-manufacturing/546700659)

**JD Quality Pouches LLC**
- Own site (re-read 2026-10-27): "Richmond, VA"-based; 2050 Val Park Drive, Oilville, VA 23129; phone 646-696-1932; hours 9-5 EST; claims "NSF Certified, USDA Certified Organic, State of VA Food Manufacturing License, HAACP Certified"; turn-key formulation, blending, pouching, canning; white/private label, short runs, long-term supply, "incubation"; caffeine and CBD pouches; MOQ not stated; cGMP/FDA registration not mentioned — [jdqualitypouches.com](https://jdqualitypouches.com)
- Wonnda directory lists it in Oilville VA, no certifications named — [Wonnda](https://wonnda.com/suppliers/jd-quality-pouches-llc/). No Virginia State Corporation Commission record found via search; SCC and VDACS lookups not performed (no state-registry access via tools). No FDA warning letter or recall surfaced for the name in a combined search — [search 2026-10-27]; absence is not clearance.

**Global Snus (Vilnius, Lithuania), Luna Corporate (Poland), House of Pouches (Denmark)**
- Combined warning-letter/recall search returned no hit naming Global Snus or Luna Corporate (hits were for unrelated snus retailers: snusguys.com letter May 19, 2026; snusme.com Apr 2025; snusport.com 2025) — [FDA snusguys.com letter](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/snusguyscom-730124-05192026) (search result only; not opened). Note Global Snus's name is similar to those retailers' category; no letter naming Global Snus itself was seen. FDA import alerts: not checked.
- House of Pouches: Wonnda (German page) describes a Denmark-based maker of tobacco-free, caffeine-containing and cannabinoid-containing oral pouches, private label program, sells to Europe and North America; no MOQ, certifications or own site found — [Wonnda](https://wonnda.com/de/lieferanten/house-of-pouches/) (directory only). Own-site read not achieved (no site surfaced).
- Global Snus and Luna Corporate own sites were NOT re-read in this pass; see [sourcing.md section 1](sourcing.md) for earlier reads.

### Inferences
- The Daily Manufacturing letter is about tobacco-product authorization, not caffeine, but a candidate with an open FDA enforcement letter and a nicotine line raises questions for counsel about commingled lines (cross-contamination with nicotine) and about reputational/supply continuity; whether Bolt can accept a maker that also produces nicotine pouches is an owner decision.
- Daily Manufacturing's published MOQ (25,000 cans) is the only published MOQ found for any candidate; it is self-reported.

### Gaps
- FDA Food Facility Registration lookup (no public query via tools), NSF live directory search (search returned the NSF Dietary listing pages, not a company search result), Virginia SCC and VDACS, state licenses, FDA import alerts, FDA recall/enforcement reports database queries: not performed. Counsel/ops should run these in a browser.
- Whether Daily Manufacturing answered/closed the April 2026 FDA letter.

---

## 8. Additional US makers who could pouch (target: 8-10 candidates total)

### Takeaway
I could not reach 8-10. Total published candidates with some evidence for caffeine/functional pouches: 5 from sourcing.md (JD Quality, Daily Manufacturing, Global Snus, Luna Corporate, House of Pouches), plus 2 weak leads below that are not pouch makers. Exhibitor lists and trade directories surfaced almost nothing new.

### Cited Findings
- HTT Packaging & Design (Huntington Beach, CA): described as a private-label contractor for sachets and stick packs and "state, NSF organic, and SQF-certified" per a California manufacturers profile; not a pouch maker — [CMTC Made in California](https://www.cmtc.com/made-in-california-profile/htt-packaging-design) (search snippet; not opened; certifications UNVERIFIED)
- Gumtech (nutraceutical gum maker) appears in a trade case study; gum not pouches; current status unverified — [ProFood World](https://www.profoodworld.com/industry/beverage/article/13328516/insourcing-revitalizes-gumtech) (snippet only)
- An unnamed "North American contract manufacturer" focused on "bulk liquid and modern oral buccal delivery pouch manufacturing" in a Newsfile press release; company name not displayed in results; link redirected earlier and gave empty content — [Newsfile](https://www.newsfilecorp.com/redirect/k4OYH7xq) — unusable until the name is found
- Generic supplement contract manufacturers on Thomasnet (ABS Corporation — tableting/encapsulation; GMP Laboratories of America — tablets, capsules, powder blends): no pouch or lozenge evidence — [Thomasnet ABS](https://www.thomasnet.com/company/abs-corporation-10075931/catalog/item/17610-1001-1001), [Thomasnet GMP Labs](https://www.thomasnet.com/company/gmp-laboratories-of-america-inc-10111057/catalog/item/15823-1003-1003) (snippets)
- No lozenge-specific or gum-specific co-packer with a pouch line found. Natural Products Expo, Vitafoods and NACS exhibitor lists were not retrieved by search.
- Competitor Roon states its pouches are made in an NSF-certified, FDA-registered, cGMP facility, maker not named (brand claim) — [Roon](https://www.takeroon.com/pouches/where-its-made-and-who-tested-it)

### Inferences
- The US caffeine-pouch contract pool visible in public sources is small; the unnamed plants behind Roon, Mojo and others are likely reachable only by asking the brands or searching trade shows in person.

### Gaps
- Exhibitor lists (NACS, Natural Products Expo, SupplySide, TPE), LinkedIn, MFG.com, FDA registration-by-product-code searches: not done.

---

## Candidates for decisions.md (NOT written; owner/coordinator to add)
- 2026-10-27 | gap-fill research | FDA CTP warning letter ER2601477 (Apr 21, 2026) to Daily Manufacturing Solutions Inc. for unauthorized nicotine pouches | Owner decides whether a maker that also runs nicotine lines is acceptable and whether to ask counsel about line segregation.
- 2026-10-27 | gap-fill research | Caffeine GRAS listing in CFR is cola-type beverages only (21 CFR 182.1180); supplement-vs-food status of a non-swallowed pouch is unresolved | Owner/counsel decide classification path before any inventory spend.
- 2026-10-27 | gap-fill research | CPSC list at 16 CFR 1700.14 does not include caffeine | Owner decides whether to use voluntary child-resistant tins.

## For a professional (questions for counsel)
1. Is an oral pouch held in the mouth and not swallowed "intended for ingestion" under 21 USC 321(ff)(2)(A), and is a pouch a form within 350(c)(1)(B)? If not a supplement, what is the food-additive/GRAS basis for added caffeine beyond 21 CFR 182.1180?
2. If a supplement: Bolt's duties as label "responsible person" (AE intake, 15-business-day reports, 6-year records, domestic phone/address on label); whether Bolt must itself verify the contractor's Part 111 compliance and release testing (strength per pouch).
3. Do the FASTER Act and 321(qq) allergen rules affect the intended flavors/fleece/fillers? Does "Contains" statement apply?
4. Any "energy/focus" wording: is it a structure/function claim triggering 101.93 notification and disclaimer?
5. Subscription offer: ROSCA 15 USC 8403 flow design; influencer/affiliate program under 16 CFR 255.
6. Contract terms: quality agreement, recall/insurance, and exclusion of nicotine cross-contact; due diligence on any maker with an FDA warning letter.
7. Should Bolt voluntarily use child-resistant packaging given no PPPA entry for caffeine?
8. Monitor H.R. 2511 (Actions tab), FDA draft caffeine-labeling guidance, FTC negative-option rulemaking.

## Overall gaps (not performed)
FDA FFR lookup; NSF live company search; Virginia SCC/VDACS; FDA import alerts and recall database; FDA NDI primary page (404); Part 111 FDA guidance on contract responsibility (404); FASTER Act text; congress.gov direct read (403); Global Snus/Luna/House of Pouches own sites re-read; trade-show exhibitor lists.
