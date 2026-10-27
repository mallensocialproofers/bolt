# Deep screen: DOSEO, ALVANE, FORENOON, ELEVENSES (US adults-only 25 mg caffeine pouch)

Checked 2026-10-27. NOT a legal clearance; no name is "clear" or "safe". Everything below is for an attorney to verify.

**Method and what failed (read first)**
- Trademarkia search pages (curl, `https://www.trademarkia.com/search/trademarks?query=<term>`) DID return full server-rendered result lists this time, including a "N Trademarks found" count and "End of search results / Page 1 of 1". Every query below was complete on page 1; `&page=2` returned "0 results". So I saw ALL results Trademarkia holds for each exact term and variant. This is still a third-party mirror of USPTO data, so it is UNVERIFIED against USPTO. Trademarkia's query is word-based and does not do fuzzy/phonetic matching, so phonetic variants were searched one by one.
- Failed: Justia (HTTP 403, 2026-10-27); USPTO tmsearch.uspto.gov and tsdr.uspto.gov (HTTP 200 but JavaScript shells with no results, not usable via curl); OpenCorporates (reCAPTCHA "Checking your browser"); trademarkdir.com (connection failed); WIPO Global Brand Database (JS app, not queried). State registries not checked. No Google; WebSearch tool only (US-only index, weak for tiny brands).
- Social handles: curl returned 302 login walls (Instagram, Facebook), 200 for every TikTok handle including nonsense, and 200/404 on X/YouTube that I cannot trust without a rendered page. All handles = NOT CHECKED. Do not use my status codes.
- Foreign-language meanings: Wiktionary checks for es/fr/de/pt/it/hi/zh/ar/ru returned 404 (no entry) for doseo and alvane (zh doseo and hi alvane returned 429 = not checked). Absence of a Wiktionary entry is NOT proof of no meaning. Everything else in those languages = "not found / not sourced".

---

## 1. DOSEO

### Takeaway
Zero Trademarkia hits for DOSEO and its spelling variants (DOSEIO, DOSEOS = 0; DOSIO = 1 wine mark), but DOSED has live Class 5 and Class 30 marks and a pending Class 5 pharma application, and DOCEO has several live marks in unrelated services. doseo.com is held until 2032 and its site did not load.

### Cited Findings
**Trademark (Trademarkia, all pages, UNVERIFIED mirror)**
- DOSEO: 0 results of 0 total. DOSEIO: 0 of 0. DOSEOS: 0 of 0. — [Trademarkia doseo](https://www.trademarkia.com/search/trademarks?query=doseo), [doseio](https://www.trademarkia.com/search/trademarks?query=doseio), [doseos](https://www.trademarkia.com/search/trademarks?query=doseos), 2026-10-27
- DOSIO: 1 of 1. Live/Registered, Class 33 alcoholic beverages except beer, Societa Agricola Dosio Vigneti S.r.l., serial 86176992, registered 31 Aug 2024. — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=dosio), 2026-10-27
- DOCEO: 5 of 5. Live/Registered: Altruist Advisors LLC (Cl. 35/36 accounting/financial planning, 90015649); Doceo Arts LLC (DOCEO ARTS, Cl. 41, 90069762); Doceo Office Solutions LLC (Cl. 35 office equipment retail, 78524502, renewal date 23 Nov 2026); HTM Global LLC (DOCEO CONDOCEO AUCTORO, Cl. 41, 97350595). Dead: KTKSTS LLC (Cl. 42, abandoned 30 Jun 2025). None in classes 5/29/30/31/32/34. — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=doceo), 2026-10-27
- DOSED (the owner you asked about): 20 results, all on one page. Relevant ones: (a) DOSED, Dosed LLC, Cl. 30 "Tea; tea extracts; tea-based beverages; instant teas; tea bags", two registrations, 88813501 and 88813490, registered 4 May 2021, Live/Registered; (b) DOSED, Pilates Club LLC, Cl. 5 "Dietary supplements for human consumption", 90897895, Live/Registered since 19 Aug 2026; (c) DOSED, Dosed IP LLC, Cl. 5/35 "Pharmaceutical preparations for use in treating nausea, fatigue, anxie..." (truncated), 99538564, Live/Pending (status date 21 Aug 2026); (d) PERFECTLY DOSED, Natuur Brands Inc., Cl. 35 cannabis-infused food information, Live/Registered; (e) DOSED, Koznarsky, Cl. 5 powdered supplement drink mix, status "Indifferent" (14 Jul 2021); (f) Dead: Dosed Management Cl. 43 cafe (abandoned 9 Jul 2026), Dosed Co. Cl. 3/35, Poni Cosmetics Cl. 3/21, Mod Beverage Cl. 32/33. I saw 20 of 20 but only part of the 20 is reproduced here. — [Trademarkia dosed](https://www.trademarkia.com/search/trademarks?query=dosed), 2026-10-27
- Correction to earlier notes: Dosed LLC's goods are tea (Class 30), not Class 29, and I found no Class 29 DOSED mark.
- How close is DOSED to DOSEO: DOSEO adds one letter pair ("-eo") to the same root; both read as "dose". Same root plus overlapping Class 5 supplements and Class 30 tea/beverage = a real attorney question (my inference, not a finding).
- Phonetic variants not found on Trademarkia: DOSEIO, DOSEOS (0 each). Not searched: "Doceo" was searched above; "DOSEYO", "DOSIO" done.
- Other mirrors: Justia 403, USPTO/TSDR/OpenCorporates unusable (see method). WIPO not queried. Nothing else confirmed.

**Domains (Verisign RDAP, 2026-10-27, `rdap.verisign.com/com/v1/domain/<d>`)**
- doseo.com registered 2007-02-25, expires 2032-02-25, last changed 2026-10-12, status "client transfer prohibited". — [RDAP](https://rdap.verisign.com/com/v1/domain/doseo.com)
- getdoseo.com, doseoco.com, doseopouches.com, doseocoffee.com, trydoseo.com, doseolabs.com: all 404 (unregistered). — RDAP, same pattern
- doseo.com content: curl http redirected to https and then failed to connect; WebFetch returned HTTP 503. Parked/for-sale/in-use: NOT DETERMINED. No Sedo/Afternic/Dan listing checked successfully (Afternic URL for doseo.com not fetched). No price found.

**Search (WebSearch, 2026-10-27)**
- "Doseo caffeine", "Doseo supplement brand", "Doseo vape OR nicotine OR pharma": no brand named Doseo returned; nearest were Dose (dosedaily.co wellness shots, reported by Reuters via Athletech as exploring a $1B sale) and Dose & Co (collagen). — [Athletech](https://athletechnews.com/us-wellness-shot-brand-dose-explores-sale-sources-say/), [Provenance](https://www.provenance.org/brands/dose-co)
- Not run: "doseo pouches", "doseo energy", "doseo coffee" as separate queries (budget). The three runs above were generic-weak (search tool does not index tiny brands well).

**Meaning/slang**
- Latin "doceo" = "to teach" (Wiktionary etymology block, id=teach). — [Wiktionary doceo](https://en.wiktionary.org/wiki/doceo). Pharma-sounding read is my assessment: "dose" + "-eo" reads like a drug/dosing brand.
- Urban Dictionary API for "doseo": no entry for the exact term; neighbours only (e.g. "Dos Dose", "doseface" Irish slang for a pain, "Small Doses"). — [UD API](https://api.urbandictionary.com/v0/define?term=doseo)
- Spanish "doseo" not sourced (no Wiktionary entry found; es "dosear/dosificar" is related to dosing but I could not source "doseo"). French, German, Portuguese, Italian, Hindi, Mandarin, Arabic, Russian: not found.

**Handles:** all NOT CHECKED.

**Fit (my assessment)** — Strongest conceptual match to a "dose-transparent" 25 mg brand: the word says "dose" in plain sight. That is also the problem: it reads as pharma/clinical (a measured dose, not a pleasure), which can sit oddly with "calm" and risks implying a therapeutic or medicinal claim. It does not resemble Zyn/Velo-style nicotine pouch names and has no youth-slang pull. Implied-claim risk is moderate (dosing = effect). The DOSED family (live Cl. 5 supplements, live Cl. 30 tea, pending Cl. 5 pharma) is the main trademark question.

### Gaps
- doseo.com content/for-sale/price; USPTO and WIPO confirmation; state registries; separate "pouches/energy/coffee" searches; foreign meanings; handles.

---

## 2. ALVANE

### Takeaway
No ALVANE or close variants on Trademarkia; AVELAINE (pending Class 5 supplement) is visually similar but not identical. Concerning facts: alvane.com is held to 2027-04-04, and someone registered tryalvane.com on 2026-07-25 and is running a Shopify "opening soon" store named "Alvane" with GBP currency.

### Cited Findings
**Trademark (Trademarkia, UNVERIFIED mirror)**
- ALVANE: 0 of 0. ALVANES: 0 of 0. ALVAIN: 0 of 0. ALVEEN: 0 of 0. — [alvane](https://www.trademarkia.com/search/trademarks?query=alvane), [alvain](https://www.trademarkia.com/search/trademarks?query=alvain), [alveen](https://www.trademarkia.com/search/trademarks?query=alveen), 2026-10-27
- ALVAN: 3 of 3. ALVAN, S.C.A.M.I. S.n.c., Cl. 7/8 reamers/hand tools, Live/Registered (status 10 Feb 2026); THE ALVAN AZINNA CHIBUZO IKOKU FOUNDATION, Cl. 35 charitable services, Live/Registered; ALVAN CLARK & SONS, Cl. 9/25, Dead/Abandoned 1993. None in food/supplement classes. — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=alvan), 2026-10-27
- AVELAINE: 1 of 1. SHUOYANG TRADING CO., LIMITED, serial 50003216, filed 20 Jul 2026, Live/Pending (status 14 Oct 2026), Class 5 "Cod liver oil; Dietary supplements for pets; Gummy vitamins; Health fo..." (truncated). — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=avelaine), 2026-10-27. Closeness to ALVANE: shares A-_-_-AINE/ANE ending and 3 of 6 letters in sequence; sound differs (al-VANE vs AV-uh-LANE). My inference: a conflict examiner would be unlikely to treat it as identical, but it is in the same Class 5 supplements space so attorney should assess.
- ALVANSO (pending, skin/hair care) seen in earlier notes via Justia snippet; not re-verified. Other mirrors: see method.

**Domains (RDAP, 2026-10-27)**
- alvane.com registered 2017-04-04, expires 2027-04-04, last changed 2026-09-24, "client transfer prohibited". — [RDAP](https://rdap.verisign.com/com/v1/domain/alvane.com). Content: curl connect failed; WebFetch 503 (nginx server header seen on http). Status unknown; no price.
- tryalvane.com REGISTERED 2026-07-25 (expires 2027-07-25). Page title "Alvane", Shopify password page "Opening soon. Be the first to know when we launch", store currency GBP. — [RDAP](https://rdap.verisign.com/com/v1/domain/tryalvane.com), [tryalvane.com](https://tryalvane.com/password), 2026-10-27. Products unknown. Indicates a third party may be launching an "Alvane" brand (UK-linked from currency) — UNVERIFIED, could be the same person as the alvane.com registrant or unrelated.
- getalvane.com, alvaneco.com, alvanepouches.com, alvanecoffee.com, alvanelabs.com: 404 (unregistered). — RDAP

**Search (WebSearch, 2026-10-27):** "Alvane caffeine pouches energy", "Alvane supplement brand", "Alvane nicotine vape pouches": no Alvane brand found. Near-names: Alvityl (French vitamins), Alvine Tonic (Indian tonic, "stimulant and energizer"), Alaven. — [1mg Alvine Tonic](https://jupiter.1mg.com/otc/allen-laboratories-alvine-tonic-otc979517), [Redcare Alvityl](https://www.redcare-pharmacie.fr/hygiene-et-sante/F00591780/alvityl-vitalite.htm). Not run: "alvane coffee".

**Meaning/slang:** Wiktionary has an entry "alvane" as an inflected form (definite plural) of Norwegian Nynorsk "alv" (elf), so it reads as "the elves" in Nynorsk. — [Wiktionary alvane](https://en.wiktionary.org/wiki/alvane). Urban Dictionary: no entry (neighbours only: Albane, Aljane). Other languages: not found.

**Handles:** NOT CHECKED.

**Fit (my assessment)** — Soft, vowel-led, calm; nothing in the word says caffeine, nicotine, or a medicine, which keeps implied-claim risk low. "-ane" is a chemistry/pharma-feeling ending, but weaker than "-eo". Low youth appeal; not a Zyn/Velo look-alike. Weakness: the name carries no dose signal, and the live tryalvane.com "Alvane" store plus AVELAINE (Class 5) make the identical-name and nearest-neighbour questions urgent to resolve.

### Gaps
- Who owns alvane.com and what tryalvane.com sells; USPTO/WIPO; foreign meanings; handles; "alvane coffee" search.

---

## 3. FORENOON

### Takeaway
The cleanest trademark picture of the four (1 total mark, dead), but no coined distinctiveness (a plain dictionary word for morning) and forenoon.com is held with registry-lock statuses to 2027-03-23 on a parked lander with no readable price.

### Cited Findings
**Trademark (Trademarkia, UNVERIFIED mirror)**
- FORENOON: 1 of 1 total. FORENOON TIMES, Juan Ontiveros Toro, serial 98592108, filed 9 Jun 2024, Dead/Abandoned 10 Nov 2025, Class 21 barbecue utensils. — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=forenoon), 2026-10-27. Page 2 = 0 results.
- FORENOONS: 0 of 0. — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=forenoons). "fore-noon"/"fore noon" returned a 16,640-result phrase search (matches "fore" or "noon" generally), not meaningful; not read. Not searched: FORNOON, FORENUN.
- Live or pending marks in classes 5/29/30/31/32/34/35/43: none seen.

**Domains (RDAP, 2026-10-27)**
- forenoon.com registered 2005-03-23, expires 2027-03-23, last changed 2026-03-03, statuses client delete/renew/transfer/update prohibited. — [RDAP](https://rdap.verisign.com/com/v1/domain/forenoon.com)
- Content: http(s) returns a 114-byte page that redirects by JavaScript to `/lander`; the lander body was empty to curl and WebFetch. Parked-lander pattern (same stub as elevenses.com's) but broker, price, or use: NOT DETERMINED.
- getforenoon.com, forenoonco.com, forenoonpouches.com, forenooncoffee.com, tryforenoon.com, forenoonlabs.com: 404 (unregistered). — RDAP

**Search (WebSearch, 2026-10-27):** "Forenoon caffeine pouches energy", "Forenoon coffee brand", "Forenoon vape nicotine pouches brand": no Forenoon brand returned. Not run: supplement-only query. Weak evidence (tool misses small brands).

**Meaning/slang:** English: the morning, sunrise to noon; Shakespeare quote in Wiktionary. — [Wiktionary](https://en.wiktionary.org/wiki/forenoon). Urban Dictionary: one entry, "before noon which equals morning" (2022). — [UD API](https://api.urbandictionary.com/v0/define?term=forenoon). Archaic/formal; I found no slang. Other languages: not found.

**Handles:** NOT CHECKED.

**Fit (my assessment)** — Calm, adult, and time-of-day specific; no youth cue, no nicotine-pouch cue, no pharma cue. Descriptive/suggestive in a "morning" way: weak as a trademark (many users could say "forenoon") and can imply morning-only use or a "wake up" effect (mild implied-claim risk). Reads old-fashioned and a bit literary; pronunciation (FOR-noon) is easy.

### Gaps
- What forenoon.com is and its price; USPTO/WIPO; foreign meanings; handles; phonetic variants beyond FORENOONS.

---

## 4. ELEVENSES

### Takeaway
Real, live, and busy: ELEVENSES is registered in Class 25 and a live ELEVENSES FRESH TABLE & BAR in Class 43; a Tampa bakery/coffee shop is operating as "Elevenses" (elevensesco.com); the bare .com is listed at $9,000 buy-now (single source). Highest adjacency to coffee, cafe and bakery uses, so it is the highest conflict risk for a coffee-like pouch.

### Cited Findings
**Trademark (Trademarkia, all 7 of 7 seen, UNVERIFIED mirror)**
- ELEVENSES, Urban Outfitters Wholesale Inc., 78805494, Live/Registered since 9 Feb 2017, Class 25 women's clothing (renewal date 14 Dec 2026).
- ELEVENSES FRESH TABLE & BAR, FHE LLC, 97797880, Live/Registered since 9 Apr 2024 (to 9 Apr 2030), Class 43 bar and restaurant services.
- Dead: Elevenses LLC Cl. 43 (98323996, abandoned 12 Feb 2025); Sweet Concepts LLC Cl. 30 bakery (86425713, cancelled 19 Aug 2022); Seven Happiness LLC Cl. 43 (abandoned 2013); W.S. Thomas Pty Cl. 33 spirits (abandoned 2007); a Chinese filer Cl. 9 phone accessories (cancelled 13 Oct 2026).
- — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=elevenses), 2026-10-27. 7 of 7; page 2 = 0. ELEVENSIES, ELEVENES, ELEVENSIS: 0 each. — [elevensies](https://www.trademarkia.com/search/trademarks?query=elevensies)
- No live mark in classes 5/29/30/31/32/34/35 seen. Class 30 and Class 43 have prior filings by bakery/cafe owners (now dead for 30), so those spaces have a history of this exact name. Other mirrors: see method.

**Domains (RDAP, 2026-10-27)**
- elevenses.com registered 2000-03-22, expires 2035-03-22, last changed 2025-07-18. — [RDAP](https://rdap.verisign.com/com/v1/domain/elevenses.com). It redirects (JS stub to `/lander`) to a GoDaddy for-sale page (`forsale.godaddy.com/forsale/elevenses.com`, HTTP 403 to curl and WebFetch). WebFetch of Afternic's listing page reports "Buy now $9,000 USD" with "make an offer". — [Afternic](https://www.afternic.com/domain/elevenses.com), 2026-10-27. This price comes from a single WebFetch summary, UNVERIFIED; confirm on the listing.
- elevensesco.com registered 2020-12-09, expires 2026-12-09 (in 43 days), in use: "Elevenses | bakery | 1001 East Columbus Drive, Tampa, FL" with specialty coffee, cakes, and Toast ordering. — [elevensesco.com](https://www.elevensesco.com/), [Toast](https://www.toasttab.com/local/order/elevensesco), 2026-10-27
- getelevenses.com, elevensespouches.com, elevensescoffee.com, tryelevenses.com, elevenseslabs.com: 404 (unregistered). — RDAP

**Search (WebSearch, 2026-10-27):** "Elevenses caffeine pouches energy", "Elevenses coffee brand supplement", "Elevenses vape nicotine brand": no caffeine, supplement, or nicotine brand called Elevenses. Found the Tampa cafe, an unrelated "elevens.coffee" Nespresso-capsule Shopify seller (different name), and Rare Tea Company's Elevenses Gift Set (earlier notes). — [Toast](https://www.toasttab.com/local/order/elevensesco), [StoreCensus elevens.coffee](https://api.storecensus.com/stores/elevens.coffee)

**Meaning/slang/recognition**
- British informal: a short mid-morning break at about 11 for a drink or snack. — [Wiktionary](https://en.wiktionary.org/wiki/elevenses). Dictionary.com notes American usage historically referred to a pre-noon whiskey break (via search summary; page not opened). — [Dictionary.com](https://www.dictionary.com/e/eleven/) UNVERIFIED snippet.
- Urban Dictionary: mixed; top sense is the tea-and-biscuit break, others: tyre-spin marks, vending-machine snack. — [UD API](https://api.urbandictionary.com/v0/define?term=elevenses). Nothing sexual or drug-related in the first 4 entries I read.
- US recognition: I found NO US survey or search-trend data. Only a UK survey (72% snack around 11 am) and a blog claiming many Americans know it from Pippin in the Lord of the Rings film (anecdotal). — [Michigan Public](https://www.michiganpublic.org/2015-06-30/high-tea-afternoon-tea-elevenses-english-tea-times-for-dummies). Google Trends not accessible here: GAP.
- Other languages: not found.

**Handles:** NOT CHECKED.

**Fit (my assessment)** — The most charming and ritual-forward of the four: a named pause with a drink fits "calm, adult". But it is British, may be unfamiliar to many US adults, hard to spell, and the "-ses" plural sounds whimsical. Implied-claim risk is low (a break, not an effect). No youth or nicotine-pouch cue. Real-world cafe, bakery and clothing owners use the exact word, so confusion and crowding risks are the biggest here, and the $9,000 .com is the only owner-priced domain of the four.

### Gaps
- Confirm $9,000 on the Afternic listing; USPTO/WIPO; US familiarity data; foreign meanings; handles.

---

## 5. Closing ranking of the four (judgement, not clearance)

1. **FORENOON** — only one dead mark; no brand found in any category; clean modifier domains; weak but acceptable calm/adult fit. Cons: descriptive (weak mark), forenoon.com owner unknown.
2. **ALVANE** — no exact marks, calm and neutral, no claim risk. Cons: tryalvane.com "Alvane" store launching in the past 3 months, alvane.com unknown holder, AVELAINE in Class 5 pending, no dose or ritual signal.
3. **DOSEO** — best dose-transparency story, no exact mark. Cons: DOSED live Class 5 and Class 30 plus pending Class 5 pharma on the same root, pharma-sounding, doseo.com held to 2032.
4. **ELEVENSES** — best ritual story and an owner-priced .com ($9,000, unverified). Cons: exact live marks in Class 25 and 43, an operating Tampa coffee/bakery under the name (elevensesco.com), US recognition unproven, hardest to spell.

For the attorney: ask for a full USPTO knockout in classes 5/29/30/31/32/34/35/43 for all four with phonetic variants, and identity checks on tryalvane.com (Alvane), the DOSED family (Dosed LLC, Pilates Club LLC, Dosed IP LLC), and the Elevenses Cl. 43 and Tampa owners.
