# Deep screen: INCREMENT, SCRUPLE, CALIPER (US adults-only 25 mg caffeine pouch)

Checked 2026-10-27. NOT a legal clearance. No name here is "clear" or "safe". A trademark attorney must run a full search (including common-law use, state registers and design marks) before any name is adopted. Every item below was checked on 2026-10-27 unless it says otherwise. Mirror or snippet data is marked UNVERIFIED.

## How the trademark data was obtained (and what failed)

- **Primary-source route that worked:** the JSON backend behind the USPTO trademark search site, `POST https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch` (the site is https://tmsearch.uspto.gov/). It returned USPTO's own records (wordmark, owner, status, goods, classes). I queried wildcard and match on `wordmark` and read every returned hit. It is an undocumented endpoint behind the public search page, and records filed in the last days or weeks may not be loaded yet. It is not a clearance search (no design-code, translation or similar-meaning search).
- **Trademarkia (mirror, UNVERIFIED against USPTO):** I fetched every results page with `?query=<word>&page=N` (server-rendered). Pages repeat some rows, so "rows seen" can exceed "unique marks".
- **Failed or unusable:** Justia (HTTP 403 on every URL form tried: `/search?q=`, `/search/<word>`, record pages); `tsdr.uspto.gov` and `tsdrapi.uspto.gov` (401 / app shell, no data); WIPO Global Brand Database (returns a JavaScript/altcha challenge page, no data); OpenCorporates (reCAPTCHA wall, API needs a token); Sedo (page temporarily unavailable); Atom (403); GoDaddy (403). State registries and Google were not run. The earlier pass in `names_measure_dose.md` saw Trademarkia page 1 only.
- A web-search tool was also used. It was weak on exact brand queries: it returned mostly generic pages.

---

## INCREMENT

### Takeaway
Cleanest of the three in the register: all 13 Trademarkia results and 76 USPTO wildcard hits show no live or pending mark in classes 5, 29, 30, 31, 32, 34 or 43 for INCREMENT or the variants searched. The live INCREMENT mark is Stripe's, in classes 16/41 (a developer magazine that has wound down). The modifier domain incrementcoffee.com was registered in January 2026 by an unknown party and shows a "Coming Soon" page, and incrementco.com / incrementpouches.com are unregistered.

### Cited Findings

**Trademark (classes 5, 29, 30, 31, 32, 34, 35, 43)**
- Trademarkia exact "increment": 13 results total, all 13 seen (page 1 = 10, page 2 = 3). No class 5/29/30/31/32/34/43 marks. Live: INCREMENT, Stripe LLC, serial 88100994, class 16 magazines on software engineering + class 41, Registered. Dead: INCREMENT CO. (Walsh, Matthew, 87077509, class 41 modelling/photography, Abandoned), INCREMENT (Silota R&D, 98156230, classes 9/42, Abandoned), plus dead class 35/36/9 compound marks. — [Trademarkia p1](https://www.trademarkia.com/search/trademarks?query=increment), [p2](https://www.trademarkia.com/search/trademarks?query=increment&page=2) (UNVERIFIED mirror)
- Trademarkia "incrementum" 7/7 seen; "increments" 6/6 seen. No target-class marks. Live ones: INCREMENTUM DIGITAL (Incrementum Digital, LLC, 90775164, class 35 marketing), INCREMENTUM EPULUM, LLC (Giovanni Delocana, 99428003, class 35 restaurant franchising consulting), INCREMENTS (Increments Ltd, Canada, 79354870, classes 14/18/25 jewelry, bags, clothing), SELECT INCREMENTS (class 9 car audio). — [incrementum](https://www.trademarkia.com/search/trademarks?query=incrementum), [increments](https://www.trademarkia.com/search/trademarks?query=increments) (UNVERIFIED mirror)
- USPTO backend, wildcard `increment*`: 74 total hits, `*increment*`: 76 total, `incrementum*`: 7 total; all returned and read (76 unique marks, 19 alive). Alive marks in target classes 5/29/30/31/32/34/35/43: only class 35 consulting/marketing marks (INCREMENTAL SHIFT 88900949; INCREMENTOR, Increment Mentoring Group LLC, 88586415; INCREMENTUM DIGITAL; INCREMENTUM EPULUM) and VRUDHI (New India Bazar, 88221173, classes 29/30 oils, rice, flour, spices; it matched the search, so I believe it is indexed by a translation of "increment", UNVERIFIED reason; not a similar-looking mark). No live or pending INCREMENT-formative mark in 5, 29, 30, 31, 32, 34 or 43. Other live marks: IF INCREMENTAL FITNESS (class 41, 87332586), MULTI INCREMENT (class 41, 76656668), INCREMENTAL (classes 28, 42, 44/42 owners differ). — [USPTO search backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), site https://tmsearch.uspto.gov/
- Not searched: phonetic spellings such as "INKREMENT". Trademarkia returned the same set for exact "increment"; I did not run other spellings on the USPTO backend.

**Domains (Verisign RDAP, https://rdap.verisign.com/com/v1/domain/NAME.com; HTTP 200 = registered, 404 = not registered)**

| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| increment.com | registered | 1999-03-19 / 2028-03-19 | SafeNames Ltd | In use. Title "Increment: Planning...". Stripe's developer magazine; its last issue's editor letter says it is the final quarterly issue, back issues remain readable. [site](https://increment.com/), [about](https://increment.com/about/), [letter](https://increment.com/planning/letter-from-the-editor/). No Afternic listing found (Afternic URL redirected, HTTP 307). |
| getincrement.com | registered | 2024-03-21 / 2027-03-21 | NameCheap | Did not load (connection failed). No sale listing found. |
| incrementco.com | NOT registered (404) | n/a | n/a | n/a |
| incrementpouches.com | NOT registered (404) | n/a | n/a | n/a |
| incrementcoffee.com | registered | 2026-01-02 / 2027-01-02 | Squarespace Domains | Page says "Coming Soon ... under construction". Owner unknown (RDAP privacy). Registered about 10 months ago. |
| tryincrement.com | registered | 2024-05-08 / 2027-05-08 | NameCheap | Did not load. |
| incrementlabs.com | registered | 2018-11-19 / 2026-11-19 (expires in about 3 weeks) | Squarespace Domains II | Did not load. Expiry date is a possible but unreliable chance to acquire. |

- RDAP source for all rows: https://rdap.verisign.com/com/v1/domain/increment.com (and the same pattern for each name). For-sale check covered Afternic only (https://www.afternic.com/domain/increment.com etc.); Sedo, Atom, GoDaddy were blocked, so "not listed" is UNVERIFIED.

**Search collisions** (web search, 2026-10-27, queries "Increment caffeine", "Increment pouches", "Increment energy drink", "Increment supplement brand", "Increment coffee", "Increment vape nicotine", plus a combined OR query)
- No brand named Increment in caffeine, energy, supplement, coffee, nicotine or vape found. "Increment pouches" returns tactical MOLLE gear pouches (a different product). — e.g. [a tactical pouch listing](https://ibspot.com/products/wynex-tactical-increment-molle-pouch-vertical-edc-utility-pouches-sling-bag-military-multi-purpose-large-capacity-with-shoulder-strap-waterproof-attachment-modular-design-black-upgraded-2-packs)
- Weak evidence only: the search tool returned generic pages for exact-brand queries.

**Meaning / slang**
- Urban Dictionary "increment": top entries are "The Increment", a UK special-forces unit claim; "slippery slope into unethical behavior"; "achieving great things in many small steps". One plural-form entry ("increments") is a crude sexual one. UD thumbs counts were returned as 0, so popularity is unknown. — [UD API](https://api.urbandictionary.com/v0/define?term=increment), [increments](https://api.urbandictionary.com/v0/define?term=increments)
- English meaning: an amount of increase, or "to increase in steps"; also the time added to a chess clock. No slang label. — [Wiktionary](https://en.wiktionary.org/wiki/increment)
- Translations (Wiktionary): German Erhöhung / Zunahme / Zuwachs / Inkrement; Russian прирост / инкремент; verb forms Spanish incrementar, French incrémenter, Italian incrementare. — [Wiktionary](https://en.wiktionary.org/wiki/increment)
- Portuguese, Hindi, Mandarin, Arabic translations: not found on the page. Slang or taboo senses in the nine languages: not found / not checked beyond the dictionary pages.

**Handles** (checked 2026-10-27)
- YouTube `@increment`, `@getincrement`, `@incrementco`, `@incrementpouches`: all HTTP 404 "Not Found" (not existing). — [example](https://www.youtube.com/@increment)
- TikTok: `@increment` EXISTS (page data: uniqueId "increment", nickname "aw", followerCount 13). `@getincrement`, `@incrementco`, `@incrementpouches`: statusCode 10221 (not found; a nonsense control handle returned the same code). — [example](https://www.tiktok.com/@increment)
- Instagram: 429 / login wall = NOT CHECKED. Facebook: redirect / login wall = NOT CHECKED. X: returned a generic 200 app shell that cannot distinguish accounts = NOT CHECKED.

### Inferences
- With no live or pending INCREMENT mark in the food, supplement, beverage or tobacco classes in the USPTO backend, the first-pass picture is the best of the three. A search for similar-sounding or similar-meaning marks, and for unregistered use, is still needed.
- Stripe's INCREMENT is a different field (software magazine, classes 16/41), and the magazine has ended, but Stripe still holds the live registration and the domain.
- incrementcoffee.com being taken in January 2026 by an unknown party is a signal that someone else has thought of this name for coffee; it is probably a squatter or hobby project, but that is unverified.

### Gaps
- Phonetic spellings on the USPTO backend; WIPO; state registers; Google exact-phrase results; Instagram/Facebook/X handles; who owns incrementcoffee.com; whether getincrement.com / tryincrement.com / incrementlabs.com are in use.
- Pronunciation or slang in the nine languages beyond dictionary translations.

### Fit (one paragraph)
INCREMENT reads as adult, calm and numeric: "one more small step" matches a low 25 mg pouch where the user chooses how many to take, and it supports dose transparency (print "25 mg per pouch" next to it). It has no obvious youth appeal and is unlikely to be mistaken for nicotine-pouch branding, though the plain one-word name sits stylistically near existing nicotine-pouch names, so pack design must keep the "caffeine, no nicotine" statement prominent. The implied-claim risk is mild but real: "increment" can suggest a stepwise boost or building up, so copy must avoid "boost your energy step by step" style claims and anything on cumulative effect; a lawyer should review taglines. It is abstract and weak as an image, and the abstract word is harder to protect if the register shows crowded "INCREMENTAL" marks in other fields.

---

## SCRUPLE

### Takeaway
SCRUPLE has the most serious positioning conflict found: scruplelabs.com is a live 2026 pre-order page for a product also called SCRUPLE: a dose-math, weight-based L-theanine "focus base" sold in pouches that pairs with caffeine, with "dose transparency" as its whole pitch. No registered SCRUPLE mark exists in food or supplement classes yet (only class 9 software marks and a different SCRUPLES salon family), but this is a live, apparently recent, direct competitor in the same concept space, and scruple.com is a $44,999 listing. The word also carries crude and drug slang meanings.

### Cited Findings

**Trademark**
- Trademarkia exact "scruple": 39 results, all 4 pages fetched (10 + 10 + 10 + 9 = 39 rows; a couple of rows repeat across pages so a few marks may be unseen). Live/pending SCRUPLE (singular) marks: SCRUPLE, Aquanomous LLC, serial 99612095, class 9 downloadable computer programs for recording AI [text truncated], Registered; SCRUPLE. (with design) Scruple LLC, Danville, Indiana, serial 99921813, class 9 downloadable mobile apps for social networking, filed 2026-07-04, status "new application, not assigned to examiner". Dead: SCRUPLE SERIES (TTOB Enterprises, class 28 stuffed toys, abandoned 1989). — [Trademarkia p1](https://www.trademarkia.com/search/trademarks?query=scruple), [p2](https://www.trademarkia.com/search/trademarks?query=scruple&page=2), [p3](https://www.trademarkia.com/search/trademarks?query=scruple&page=3), [p4](https://www.trademarkia.com/search/trademarks?query=scruple&page=4) (UNVERIFIED mirror)
- SCRUPLES variants: Trademarkia "scruples" 36 results (page 1 seen = 10; family is the same as above). Live SCRUPLES marks are Scruples Professional Salon Products, Inc. (classes 3, 8, 11: hair care, tools, dryers; many registrations, some dating from 1989), Stand Up Apparel, LLC (97559864, 97659748: class 35 online retail of fanny packs, magnets, clothing + class 25), High Game Enterprizes Inc. (97365010, class 28 board games). "scrupul": 2 results, both dead (SCRUPULOES class 25; SCRUPULOUS class 2). "skruple", "scrupel": 0 results. — [scruples](https://www.trademarkia.com/search/trademarks?query=scruples), [scrupul](https://www.trademarkia.com/search/trademarks?query=scrupul) (UNVERIFIED mirror)
- USPTO backend: `scrup*` 47 hits, `scrupl*` 39, `*scruple*` 39, `skrup*` 0, `scrupel*` 0; all returned and read (47 unique marks, 18 alive). Alive marks in classes 5/29/30/31/32/34/35/43: only the two Stand Up Apparel SCRUPLES marks (class 35 online retail of fanny packs, magnets and clothing; class 25). Nothing in 5, 29, 30, 31, 32, 34 or 43. Other live: SCRUPLES (Scruples Professional Salon Products) classes 3/8/11, SCRUPLES board games class 28, SCRUPPER (class 10 massage devices), SCRUPS (class 10/25), BOSTON BADATZ (Kosher certification, matched on a translation, UNVERIFIED), MIGALA (class 33 wine, matched on a translation, UNVERIFIED). — [USPTO search backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)
- The applicant Scruple LLC (Indiana) is a social-app filer; the gap between that and scruplelabs.com is unknown (no link found).

**Domains**

| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| scruple.com | registered | 2002-02-21 / 2027-02-21 | GoDaddy | Parked via namefind.com nameservers (page redirects to /lander, blank). **Afternic listing: "Buy it now for $44,999.00" or make an offer** — [Afternic](https://www.afternic.com/domain/scruple.com) (read 2026-10-27) |
| getscruple.com | registered | 2026-10-04 / 2027-10-04 | Name.com | Live page titled "Scruple": "We help independent pharmacies find the money they're losing. Private for now. Enter the passcode." (a pharmacy software start-up, registered 23 days ago) |
| scrupleco.com | NOT registered (404) | | | |
| scruplepouches.com | NOT registered (404) | | | |
| scruplecoffee.com | NOT registered (404) | | | |
| tryscruple.com | NOT registered (404) | | | |
| scruplelabs.com | registered | 2026-08-31 / 2027-08-31 | GoDaddy (Vercel DNS) | **Live product site, see Search collisions below** |

- RDAP: https://rdap.verisign.com/com/v1/domain/scruple.com (same pattern for each).

**Search collisions**
- **scruplelabs.com (read in full 2026-10-27):** page title "SCRUPLE — Focus Base, and the dose math for your body weight". It takes pre-orders for a "founding batch, 300 pouches" at a "$45 founding price" with a $25 deposit (Stripe receipt mentioned). The product is described as a caffeine-free focus base with 190 mg L-theanine per 5.50 g serving, mixed into 350 mL water; the user adds their own caffeine at 2.0 mg/kg and the page runs a body-weight dose calculator. Its pitch is "Your dose is not a serving suggestion", "Measured, not marketed", with caffeine ceiling language (cites FDA 400 mg/day). No company name, address or social links found in the page source. Domain registered 2026-08-31. — [scruplelabs.com](https://scruplelabs.com/)
- Web search for "Scruple caffeine / pouches / energy / coffee / vape nicotine / supplement" returned nothing about any Scruple brand (the search tool did not index scruplelabs.com; a direct query for it also returned only generic L-theanine pages). So the live collision above was found only by fetching the domain. — [example search](https://en.wikipedia.org/wiki/Scruple_(unit))
- No nicotine, vape or coffee brand named Scruple found (weak search).

**Meaning / slang**
- English: (1) hesitation from difficulty of knowing what is right, a moral qualm; (2) apothecary unit of 20 grains, about 1.3 g, symbol ℈; (3) obsolete: a very small quantity. No slang label in the dictionary entry. — [Wiktionary](https://en.wiktionary.org/wiki/scruple)
- **"No scruples" double meaning:** the common idiom is "to have no scruples" / "unscrupulous" = lacking a conscience, behaving unethically. Used as a brand it invites the line "no scruples" in reviews, jokes and ads, and for a stimulant could read as ironic. The same word's moral sense ("scruple" = ethics) can also read as upright. Net: both readings are easy to find in English, and the negative one is the reflex. The idiom claim is general English usage and the dictionary sense above; I did not find a source on how consumers read the name in a product context.
- **Urban Dictionary** (UD API, thumbs counts returned as 0 so prevalence is unknown): "scruple": doubt/hesitation; **testicle(s)/scrotum slang**; a rash; an undesirable person; "can mean whatever you want, originating from free Rizlas with Amber Leaf" (rolling-paper/tobacco reference). "scruples": morals or conscience; **"the small amount of weed left over after you clean it and pack a bowl or roll a joint"** (drug slang); testicles; a made-up STD. — [UD scruple](https://api.urbandictionary.com/v0/define?term=scruple), [UD scruples](https://api.urbandictionary.com/v0/define?term=scruples)
- Translations of the moral sense (Wiktionary): French scrupule, German Skrupel, Portuguese escrúpulo, Spanish escrúpulo; unit sense: Spanish escrúpulo, Portuguese escrópulo. Italian, Hindi, Mandarin, Arabic, Russian: not found on the page (Russian appears only under a verb sense). Slang in those languages: not found / not checked. — [Wiktionary](https://en.wiktionary.org/wiki/scruple)

**Handles**
- YouTube `@scruple`: EXISTS (HTTP 200, page title "Scruple - YouTube"; content not inspected). `@getscruple`, `@scrupleco`, `@scruplepouches`: 404 (not existing). — [example](https://www.youtube.com/@scruple)
- TikTok: `@scruple` EXISTS (uniqueId "scruple", followerCount 2). `@getscruple`, `@scrupleco`, `@scruplepouches`: statusCode 10221 (not found). — [example](https://www.tiktok.com/@scruple)
- Instagram (429 login wall), Facebook (login redirect), X (generic 200 shell): NOT CHECKED.

### Inferences
- The scruplelabs.com page is the single most important finding in this whole screen: same word, same dose-transparency message, pouches, caffeine-adjacent, and recent (domain registered 2026-08-31). Even without a registered mark it gives the owner of that site a common-law and priority argument, and it would confuse buyers. A US attorney should judge the actual risk; I cannot.
- The negative "no scruples" reading, the drug slang entry and the testicle slang would be a recurring joke for a product people put in their mouth.
- Buying scruple.com at the listed price is not realistic for this project; modifier domains are open.

### Gaps
- Who operates scruplelabs.com (not named on the page); whether they filed or plan to file a trademark (the USPTO backend showed no such filing as of today, but new filings lag); Instagram/Facebook/X; WIPO and state registers; ownership of the YouTube/TikTok @scruple accounts.
- Slang in Hindi, Mandarin, Arabic, Russian, Italian: not found.

### Fit (one paragraph)
SCRUPLE ties directly to dose (the apothecary unit) and to conscience, which could suit an honest, label-everything, dose-transparent brand, and it is distinctive. But the live scruplelabs.com product already owns that exact story in 2026, the "no scruples" reading is the first joke anyone will make, and the slang (testicles, leftover weed) is poor for a calm adult product, so the name carries confusion, reputation and tone risk at once. Nicotine-pouch look-alike risk is low from the word itself. Youth appeal is low; the weed slang is an adult-only association and not a youth hook, but it is still the wrong signal. Implied claims: the word itself makes none, but "conscience" could slide into "guilt-free" claims, which would need review.

---

## CALIPER

### Takeaway
CALIPER has no live or pending mark in the food, supplement, beverage or tobacco classes, but it has a recent consumer brand in the same lane: Caliper CBD / Caliper Swiftsticks (dissolvable CBD powder packets, 21+, Circle K distribution in 2020), whose live site says "Caliper is a trademark of Caliper Foods" and "© 2026 Caliper Holdings". Its CALIPER trademark applications in classes 1, 5 and 32 (hemp supplements and beverage powders) were all abandoned in January 2024, which Trademarkia missed because of its 84-row cap. Caliper Corporation holds long-standing live registrations in unrelated classes (HR testing, mapping software) and caliperco.com is taken.

### Cited Findings

**Trademark**
- Trademarkia exact "caliper": 84 results, all 9 pages fetched (8 pages of 10 + 4 = 84 rows; 81 unique serial numbers because rows repeat across pages, so about 3 results unseen). Live CALIPER marks: Talogy, Inc. (73574191 class 16 personnel assessment tests; 73632114 classes 35/42; CALIPER ANALYTICS), Caliper Corporation (74501386 classes 35/42 marketing research consulting; 76094414 class 9 mapping software), Tegra118 Wealth Solutions (78367415 class 9), Caliper Life Sciences (75539199 class 9/42), Redox Bio-Nutrients (77441197 class 1 plant nutrients), CALIPER COSMETICS (Anderson, 88878051 class 44 tattooing/laser services), CUPID CALIPER (Cupid Lift, 98528321 class 10, pending), Caliper App LLC (99872829 class 9, filed 2026-06-08, pending, "non-final action"), plus CALIPERAY, CALIPERD, brake-caliper compounds (class 12), MGP CALIPER COVERS, PHOENIX CALIPER (class 37), HIGH CALIPER (class 22). Dead: CALIPER IP, INC. 88341712 (class 5) and NEXTEVO, INC. 88341707 (class 1), both Abandoned 2024-01-01; CALIPER HUBBARD FEEDS (class 31 animal feed, cancelled 2009). — [p1](https://www.trademarkia.com/search/trademarks?query=caliper) ... [p9](https://www.trademarkia.com/search/trademarks?query=caliper&page=9) (UNVERIFIED mirror)
- "calliper" and "caliperz": 0 results. — [calliper](https://www.trademarkia.com/search/trademarks?query=calliper)
- USPTO backend: `calip*` 176 total hits (all fetched with from=0 and from=100), `*caliper*` 105 total (fetched), `callip*` 19, `kalip*` 37, `calliper*` 0; 245 unique marks read in total across the caliper-spelling and caliber-spelling sets. **New vs Trademarkia:** CALIPER, Caliper IP, Inc., serial 88341754, **class 32** (powders and liquid concentrates for making hemp-infused soft drinks, tea-flavoured beverages, energy drinks), filed 2019-03-15, Abandoned 2024-01-01 "no statement of use filed". Also 88341712 class 5 (vitamin and mineral supplements, hemp-containing, drink mixes, herbal supplements), same filer and fate. Related owner filings by Caliper IP: MAKE AGEING SUCK LESS (class 5 powdered nutritional supplement drink mix 88651332; class 32 powders for beverages, coffee and tea 88653153; class 35 online retail of supplements 88651881; classes 3/16/41), all Abandoned. NEXTEVO, INC. (the other applicant) has a live NEXTEVO class 3 registration and abandoned vitamin-supplement filings. — [USPTO search backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)
- Alive CALIPER marks in target classes (5/29/30/31/32/34/35/43) on the USPTO backend: only class 35 (Caliper Corporation 74501386; Talogy 73632114; CALIPER ANALYTICS 86395901). No live or pending CALIPER in 5, 29, 30, 31, 32, 34, 43. Also live: CALIPER (French SAS, Madrid, 79384103, classes 7/9/42, status "report completed, suspension check").
- **Phonetic neighbours (incomplete):** `caliber*` returned 668 total, `calibre*` 138, `calibr*` 587, but the tool returned only the first 100 per query, so only 276 unique marks were read and the list below is NOT complete. Alive in target classes among those: CALIBER (Boehringer Ingelheim, 88211088 and 75587157, class 5 veterinary vaccines; Dukal, 77572223, class 5 bandages), CALIBR (iKrusher, Inc., 90054568, **class 34 electric cigarettes**), CALIBRÈ (Calibre Coffee, Illinois, 99574748, **class 43 coffee shop services**, "suspension letter mailed" = pending), CHOCOLATS DU CALIBRESSAN (classes 30/35), CALIBER / CALIBRE class 35 marks (Everest.com, MCH Management, CALIBRE Systems). Plus KALIPSO (Kaluch Global Trading, 99862833, class 32 beer, non-final action), CALIPPO (class 30 ice cream), KALIPAI (classes 29/30 snacks). Whether any of these is "similar enough" to CALIPER is for counsel.
- Common-law brand: **Caliper CBD / Caliper Swiftsticks** (see Search collisions).

**Domains**

| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| caliper.com | registered | 1992-10-02 / 2029-10-01 | GoDaddy | In use: "Maptitude GIS & Mapping Software, TransCAD ... Caliper" (Caliper Corporation). [site](https://www.caliper.com/). Not listed on Afternic (307 redirect). |
| getcaliper.com | registered | 2017-01-16 / 2027-01-16 | GoDaddy (Afternic NS) | Parked; **Afternic "Buy it now for $1,988.00"** — [Afternic](https://www.afternic.com/domain/getcaliper.com) (read 2026-10-27) |
| caliperco.com | registered | 2021-02-17 / 2027-02-17 | WebNic.cc | Did not load; nameservers arvancdn.ir; YouTube channel "CaliperCO" page og:description "www.veliira.com"; TikTok @caliperco 149 followers (unrelated apparent third party, UNVERIFIED) |
| caliperpouches.com | NOT registered (404) | | | |
| calipercoffee.com | NOT registered (404) | | | |
| trycaliper.com | registered | 2019-03-12 / 2029-03-12 | Tucows (Cloudflare DNS) | **Live shop: "Buy CBD Powder ... | Caliper CBD | NextEvo - TryCaliper"** |
| caliperlabs.com | registered | 2024-11-20 / 2027-11-20 | NameCheap | Did not load |

- RDAP: https://rdap.verisign.com/com/v1/domain/caliper.com (same pattern).

**Search collisions**
- **Caliper CBD (trycaliper.com), read 2026-10-27:** sells flavourless dissolvable CBD powder in 20 mg packets and "Caliper Swiftsticks"; footer: "Caliper is a trademark of Caliper Foods. © 2026 Caliper Holdings", "not for use by or sale to persons under the age of 21", "manufactured in Commerce City, CO". It uses claims language ("Ease Everyday Aches", "Snooze Easier", "Stress Less") that is not acceptable for Bolt, which only shows what that brand does. — [trycaliper.com](https://trycaliper.com/)
- Trade press: "Caliper Launches Dissolvable CBD Powders in Circle K Texas Region" (BevNet, 2020) and "Caliper Foods creates a water-soluble flavored CBD powder" (Packaging Strategies); a Nosh brand page says Caliper Holdings was moving to a licensing business model (page 403 for direct fetch, so the detail is from the search-result snippet, UNVERIFIED). — [BevNet](https://www.bevnet.com/news/supplier-news/2020/caliper-launches-dissolvable-cbd-powders-in-circle-k-texas-region/), [Packaging Strategies](https://www.packagingstrategies.com/articles/102487-caliper-foods-creates-a-water-soluble-flavored-cbd-powder), [Nosh](https://www.nosh.com/brands/caliper-cbd)
- Web search "Caliper caffeine / pouches / energy / coffee / vape nicotine": no caffeine, nicotine or vape brand named Caliper found; "Caliper pouches" returns tool pouches (McMaster-Carr, Starrett). "Caliper supplement brand" surfaced Justia pages for Caliper IP, Inc. trademarks (those are the abandoned filings above). — [McMaster-Carr](https://www.mcmaster.com/products/caliper-pouches/), [Justia owner page, via search snippet only](https://trademarks.justia.com/owners/caliper-ip-inc-4237101)

**Meaning / slang**
- English: a measuring instrument for small distances; the part of a disc brake that holds the pads; (UK) a metal orthopaedic leg support. No slang label. — [Wiktionary caliper](https://en.wiktionary.org/wiki/caliper), [calipers](https://en.wiktionary.org/wiki/calipers)
- **Urban Dictionary** (thumbs returned as 0): "caliper": a tool to measure depth and width of an anatomical part (crude sexual); "calipers": a system for judging whether a woman's bottom is in a size range (crude); "to meet up and smash". These are crude, low-evidence entries. — [UD caliper](https://api.urbandictionary.com/v0/define?term=caliper), [UD calipers](https://api.urbandictionary.com/v0/define?term=calipers)
- Skinfold calipers are a body-fat measuring tool (general knowledge, no source fetched), so a body-composition association is plausible and would conflict with "no weight-loss claims" if copy leans on it.
- Translations (Wiktionary): measuring device: Spanish calibre, French compas d'épaisseur / pied à coulisse, German Messschieber / Stangenzirkel, Portuguese paquímetro, Mandarin 卡尺 (kǎchǐ), Russian штангенциркуль; brake part: Spanish cáliper / mordaza, French étrier, German Bremssattel, Portuguese pinça, Russian суппорт. Italian, Hindi, Arabic: not found. Sound-alike hazard: Spanish "calibre" (their word for calipers and for "caliber"). — [Wiktionary caliper](https://en.wiktionary.org/wiki/caliper), [calipers](https://en.wiktionary.org/wiki/calipers)

**Handles**
- YouTube: `@caliper` EXISTS (HTTP 200, title "caliper - YouTube"); `@caliperco` EXISTS (title "CaliperCO - YouTube"); `@getcaliper`, `@caliperpouches`: 404. — [example](https://www.youtube.com/@caliper)
- TikTok: `@caliper` returns statusCode 10222 with uniqueId "caliper" and followerCount 2 (an account exists; 10222 appears to mean private/restricted, UNVERIFIED); `@caliperco` EXISTS (149 followers); `@getcaliper`, `@caliperpouches`: not found (10221). — [example](https://www.tiktok.com/@caliper)
- Instagram, Facebook, X: NOT CHECKED (login walls / generic shell).

### Inferences
- Registered-mark picture is moderate: no CALIPER in 5/29/30/31/32/34/43, but a recent same-aisle brand (powdered CBD packets, with the 21+ adult positioning) that claims the mark by use and let its applications lapse. Whether that is abandonment of the name or only of the filings is a legal question for counsel.
- The phonetic neighbours (CALIBR in class 34 e-cigarettes, CALIBRE coffee shop in class 43) are different words by one consonant; an examiner or opposer might or might not treat them as similar.
- getcaliper.com ($1,988) is an actual purchasable asset if the name were chosen; caliperco.com is not.

### Gaps
- Instagram/Facebook/X; who currently owns Caliper CBD; whether the licensing model means CALIPER is sold or licensed to others; WIPO and state registers; the 3 unseen Trademarkia rows and the unread remainder of the caliber/calibre/calibr USPTO result sets; Italian, Hindi, Arabic translations; slang in languages other than English.

### Fit (one paragraph)
CALIPER suggests precision and measurement, a clean fit for a "25 mg, measured" product, and it is easy to say and spell. The risks are: a live brand in a neighbouring edible/supplement format with a claimed trademark; an industrial or brake-part feel; a body-measurement ("skinfold caliper") reading that could drift towards weight or body claims; and crude Urban Dictionary entries (low evidence). Nicotine-pouch look-alike risk is low from the word. Youth appeal is low. The implied-claim risk is the "precision / exact dosing" idea, which is acceptable only if the mg per pouch is printed and nothing implies guaranteed effect.

---

## Closing ranking of the three (for choosing which to send to a trademark attorney)

1. **INCREMENT** (best of the three). No live or pending INCREMENT-type mark in classes 5, 29, 30, 31, 32, 34, 43 on the USPTO backend (all 74-76 hits read); live INCREMENT is Stripe's class 16/41 magazine, which has ended. incrementco.com and incrementpouches.com are unregistered; incrementcoffee.com was registered by an unknown party in January 2026 (placeholder page). TikTok @increment exists (13 followers). No Increment caffeine, nicotine or supplement brand in web search (weak). The best fit with the dose-step idea. Still needs a full attorney search; the abstract word will be weaker as a mark.
2. **CALIPER**. Good meaning, but a live CBD powder-packet brand with a stated trademark (Caliper Foods / Caliper Holdings) sits in the same aisle, its hemp-supplement and drink-powder applications (classes 5, 32) lapsed in 2024, Caliper Corporation holds old live registrations in classes 35/42 (HR and marketing research), caliperco.com and @caliperco are taken, and the body-measurement reading could pull copy towards body claims. Attorney should judge the common-law risk before it is used.
3. **SCRUPLE** (weakest). A live 2026 pre-order product named SCRUPLE at scruplelabs.com is built on the same "dose math, measured not marketed" idea and sells pouches that go with caffeine; scruple.com is listed at $44,999; there is a pending class 9 SCRUPLE mark (Scruple LLC, filed 2026-07-04) and a registered class 9 SCRUPLE (Aquanomous LLC); the "no scruples" reading and crude/drug slang are extra tone risks. Not recommended to send forward unless the owner wants the attorney to assess the scruplelabs.com conflict specifically.

Because INCREMENT is the only one with no direct same-lane brand found, it is the suggested first candidate, with the caveat that the evidence is "nothing found by these tools", not "nothing exists".

### For a professional (trademark attorney)
- Run a full search (similarity, translation and design marks; unregistered use; state registers) on INCREMENT first; ask about INCREMENTUM/INCREMENTAL as possible citations and Stripe's INCREMENT class 16/41 registration.
- If CALIPER stays in play: status of the CALIPER mark claimed by Caliper Foods / Caliper Holdings, and whether the lapsed 2019 filings affect priority.
- If SCRUPLE stays in play: priority and likelihood of confusion with scruplelabs.com.
- Review whether a one-word name next to caffeine pouches risks confusion with nicotine-pouch look-alikes, and review any tagline for implied claims.

### Verification still owed (not done)
- Instagram, Facebook, X handles for all three names (login walls); WIPO; state registries; OpenCorporates; Google result pages; Sedo/Atom/Dan for-sale status; whether TikTok/YouTube accounts above are active or dormant.
