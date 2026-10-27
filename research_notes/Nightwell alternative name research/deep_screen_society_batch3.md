# Deep screen, batch 3: ISADORA, ROSALIND, MARGAUX, ANOUK, EDIE, MABEL (US adults-only 25 mg caffeine pouch; "<Name> Society / Club / Supply / Tins")

Checked 2026-10-27. NOT a legal clearance. No name here is "clear" or "safe". A trademark attorney must run a full search (similarity, translation, design marks, common-law use, state registers) before any name is adopted. Mirror or snippet data is marked UNVERIFIED. Pronunciation and "reads young / old-fashioned" judgments are my own reading, not sourced.

## How the data was obtained, and its limits

### Takeaway
USPTO's own search backend was used for trademark status (authoritative field `alive`, owner, goods). Trademarkia was fetched page by page for counts, but its status label could not be trusted in my parse (it tagged abandoned and cancelled marks as live), so every "live/pending" statement below comes from the USPTO backend, not Trademarkia.

### Cited Findings
- USPTO backend `POST https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch` (the endpoint behind https://tmsearch.uspto.gov/), wildcard queries on `wordmark`, every page read (100 per page). Undocumented; recent filings may be missing. Hit totals (wildcard) per name: ISADORA `isadora*` 57, `*isadora*` 60, `isidora*` 1, `izadora*` 1, `isadorra*` 0 (62 unique read). ROSALIND `rosalind*` 50, `*rosalind*` 50, `rosalyn*` 16, `rosalin*` 72, `rosaline*` 8 (88 unique). MARGAUX `margaux*` 65, `margeaux*` 7, `margo*` 243, `*margo` 153, `margot*` 87, `margaud*` 0 (352 unique). ANOUK `anouk*` 12, `*anouk*` 35, `anook*` 6, `anouck*` 2, `anuk*` 20, `anouc*` 6 (67 unique). EDIE `edie` 98, `edie*` 122, `*edie` 189, `eddie*` 824, `edy` 28, `eddy` 331 (1,286 unique; Eddie/Eddy are mostly unrelated surnames and are context only). MABEL `mabel*` 150, `*mabel*` 212, `mabelle*` 5, `*mabelle*` 15, `mabell*` 9, `mable*` 53 (265 unique). — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)
- Trademarkia (mirror, UNVERIFIED) every results page fetched with a browser User-Agent: counts "results / pages / rows seen": isadora 57 / 6 / 56; isidora 1; isadorah 0; rosalind 49 / 5 / 49; rosalyn 16; rosalynd 0; rosaline 8; margaux 64 / 7 / 64; margo 101 / 11; margot 67; anouk 10 / 1 / 10; anook 4; edie 84 / 9 / 84; edy 15; eddie 627 / 63 / 627; mabel 91 / 10 / 91; mabelle 5; mable 34. Example URLs: https://www.trademarkia.com/search/trademarks?query=isadora , `&page=2` ... `&page=6`; same pattern for each term. Cross-check: every Trademarkia serial for isadora, rosalind, margaux, anouk and mabel was also in my USPTO pulls (0 missing); for the Edie set 64 Eddie-surname marks were not (none relevant: e.g. EDDIE G'S COOKIES 88298561 and 98504181, class 30, are cookies by a person named Eddie).
- Phrase forms ("<name> society", "<name> club", "<name> supply", "<name> tins"): Trademarkia treats the query as OR across words (e.g. "anouk society" = 9,293 results, "anouk club" = 30,000), so the totals are meaningless. I read pages in order until a page had no row containing the name (2 to 5 pages each). Only marks already found by the single-name searches appeared; no mark containing the name plus society, club, supply or tins in any class was found for any of the six names. The joined forms (e.g. "isadorasociety") return 0 results for all six names. — e.g. [anouk society p1](https://www.trademarkia.com/search/trademarks?query=anouk%20society), [isadorasociety](https://www.trademarkia.com/search/trademarks?query=isadorasociety)
- Not run: Justia, WIPO, state registers, TSDR (blocked or login walls in the earlier pass per the prior note). Web search was weak on exact-brand queries (it often returned generic caffeine-pouch pages), so "no brand found" below is weak evidence. — prior method note: /home/user/bolt/research_notes/Bolt replacement brand name research/deep_screen_increment_scruple_caliper.md
- Domain method: Verisign RDAP, https://rdap.verisign.com/com/v1/domain/NAME.com (200 = registered, 404 = not registered in .com; a registrar may still hold or reserve it). Prior pass found the phrase .coms mostly free — [dotcom_first_search.md](/home/user/bolt/research_notes/Nightwell%20alternative%20name%20research/dotcom_first_search.md). Handles: YouTube `@handle` HTTP status and TikTok page `statusCode` (0 = exists, 10221 = not found, 10222 = restricted/private, 209002 = unclear); Instagram, Facebook, X = NOT CHECKED (login walls).

### Inferences
- The USPTO backend is the better source for status; Trademarkia is only a cross-check for coverage.

### Gaps
- Phonetic and similar-meaning searches beyond the spellings above; design marks; WIPO; state registers; common-law use. All for the attorney.

---

## ISADORA

### Takeaway
ISADORA has seven live registrations for the exact word in food classes 29 and 30 (Mexican beans, rice, soups; owner Productos Verde Valle, Mexico) plus a live ISADORA HOTEL in class 43, and IsaDora is a Swedish women's cosmetics brand that owns isadora.com and sells in the US. The phrase .coms are free, but the exact word is already a food brand, and the name carries an "is adorable" pun that reads cute.

### Cited Findings
**Trademark (live or pending, classes 5/29/30/31/32/34/35/43; USPTO backend, 62 unique marks read of 57/60 hits; Trademarkia 56 of 57 rows seen)**
- ISADORA, Productos Verde Valle, S.A. de C.V. (Mexico), class 29 processed beans: serials 77975874 (registered and renewed), 87133186 (Sec. 8 and 15 accepted: processed and refried beans); 90979904 (beans, shredded beef, chicken in mole sauce); 98078995 (design plus words, prepared meat and dishes, barbacoa); 99039761 (soups, processed lentils). Class 30: 90851275 (Mexican-style rice), 99039779 (rice, prepared rice side dishes). All status Registered. — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [Trademarkia](https://www.trademarkia.com/search/trademarks?query=isadora)
- ISADORA HOTEL, South Florida United Investments, LLC, 99363726, class 43 hotel accommodation, "first extension granted" (pending). — USPTO backend
- No live or pending ISADORA mark in classes 5, 31, 32, 34 or 35 (Blue Star Group ISADORA 98711496 and Castelli ISADORA 85141899, both class 35 retail, are abandoned or cancelled). — USPTO backend
- Context, classes 3/25/33: ISADORA, Invima AG, 78099038, class 3 (cleaning/body-care preparations; also 16, 18, 21), registered and renewed; ISADORA, Isadora AB (Sweden), 79458289, class 3, new application (79-series serial, which normally indicates an international Madrid filing; inference); ISADORA, Novus, Inc., 74342365, class 25; ISADORA PACCINI 75435832 class 25; IZZIE ISADORA, Sonoma Bespoke LLC, 87519249, class 33 wine, Sec. 8 and 15 accepted. — USPTO backend
- Phrase forms: no "ISADORA SOCIETY / CLUB / SUPPLY / TINS" mark. Variant spellings: ISIDORA GROUP LLC (98777312, class 14 jewelry) only; "izadora" 1 hit not in target classes.

**Domains (RDAP, 2026-10-27)** — [RDAP template](https://rdap.verisign.com/com/v1/domain/isadora.com)
| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| isadora.com | registered | 1997-06-27 / 2027-06-26 | Abion AB | In use: page title "IsaDora | Start page" (Swedish cosmetics brand; [about us](https://www.isadora.com/about-us)). |
| isadorasociety.com, isadoraclub.com, isadorasupply.com, isadoratins.com, isadorapouches.com, tryisadora.com | NOT registered (404) | | | |
| getisadora.com | registered | 2026-04-08 / 2027-04-08 | Wix.com | Wix "ConnectYourDomain Error" (HTTP 404), unused placeholder; owner unknown |
- For-sale status of isadora.com: not checked (live site of the cosmetics brand).

**Search collisions**
- IsaDora cosmetics: Swedish make-up brand founded 1983, Malmo; entered the US in 2017 via Walgreens.com; says it sells in over 40 countries; fragrance-free, vegan-friendly marketing claims are self-reported. — [Wikipedia](https://en.wikipedia.org/wiki/IsaDora_cosmetics), [Drug Store News](https://drugstorenews.com/beauty/swedish-beauty-brand-isadora-enters-us-market-walgreenscom), [company about page](https://www.isadora.com/about-us). Parent "Invima" link to "Isadora AB" unconfirmed in sources.
- Searches "Isadora caffeine/pouches/coffee/energy", "Isadora nicotine/vape/supplement": no caffeine, coffee, energy, nicotine, vape or supplement brand called Isadora found (weak search tool). "Isadora Society": no brand; results are the Isadora Duncan dance world (Isadorables, Isadora Duncan Dance Foundation). — [Isadorables](https://en.wikipedia.org/wiki/Isadorables), [Isadora Duncan Dance Foundation](https://www.idealist.org/en/nonprofit/5024c8a13db04feda18916d13813e297-isadora-duncan-dance-foundation-new-york)
- Oddity: ISADORA DUNKING COFFEE! DANCE TO THE LAST DROP, D'Excelsior Productions LLC, 98159422, class 21 (not a target class; coffee-themed kitchenware). — Trademarkia

**Meaning / slang / fame**
- Female given name, from Ancient Greek (variant of Isidora, "gift of Isis" in the Portuguese entry). — [Wiktionary](https://en.wiktionary.org/wiki/Isadora)
- Urban Dictionary: 10 entries, all about a girl named Isadora (cute, sweet, "all the guys want a piece of her"); one entry reads the name as "she is adorable". No crude entry seen in the first six. — [UD API](https://api.urbandictionary.com/v0/define?term=isadora)
- Famous person: Isadora Duncan (modern dancer), plus the "Isadorables" dance group. — [Wikipedia](https://en.wikipedia.org/wiki/Isadorables)

**Handles**: YouTube `@isadora` exists (HTTP 200); `@isadoraclub` exists (200); `@isadorasociety`, `@isadorasupply` 404. TikTok `@isadora` exists (1,952 followers), `@isadoraclub` exists (20 followers), `@isadorasociety`, `@isadorasupply` not found. Instagram, Facebook, X NOT CHECKED. — e.g. [YouTube](https://www.youtube.com/@isadora), [TikTok](https://www.tiktok.com/@isadora)

### Inferences
- Fit: Feminine, long-form, elegant and easy to say (iz-uh-DOR-uh), with no sleep, energy or medical cue and no nicotine-pouch look-alike (it sounds nothing like Lucy, Fre, Zyn, Velo, ALP, Killa, Rogue, Sesh+, Nectr, Roon, Wip, Mojo, Ultra, Grinds, NZE, Plopii or Doseology; the only shared pattern is "girl's name", as with Lucy, which "Society" or "Club" helps separate). The "is adorable" pun and strong girl-name feel risk a cute or young read that the owner wants to avoid, and Isadora Duncan adds an art/dance flavour, not a hospital one. Selling-wise it is distinctive and memorable. The main weaknesses are registry and market: seven live ISADORA food registrations in classes 29/30 and a known women's beauty brand with the exact .com; whether either blocks a caffeine pouch is for counsel. Implied-claim risk is low.

### Gaps
- Whether Productos Verde Valle's food marks or IsaDora's class 3 marks would be asserted against a pouch brand; Instagram/Facebook/X; whether the cosmetics brand sells anything ingestible.

---

## ROSALIND

### Takeaway
No live ROSALIND mark in classes 5, 30, 32, 34 or 35; live ones sit in rose plants (class 31) and near-variants in snacks and cheese (ROSALINDA'S, ROSALINA). Phrase .coms are all free and "Rosalind Club" is a real historic women's club name. Main cautions are the science and medical associations (Rosalind Franklin, Rosalind Franklin University of Medicine and Science) and an old-fashioned feel.

### Cited Findings
**Trademark (USPTO backend 88 unique marks read; Trademarkia rosalind 49 of 49 rows seen)**
- Live in target classes: ROSALIND, David Austin Roses Limited, 77343510, class 31 live rose plants (registered and renewed); HEAVENLY ROSALIND 75839855 (same owner, class 31; seen on Trademarkia, status UNVERIFIED); ROSALINA, Cheese Land, Inc., 86089337, class 29 cheese; ROSALINA, Knaap Licenties B.V., 86910016, class 31; ROSALINDA, Flowerwood Nursery, 74549015, class 31; ROSALINDA'S, Snak King Corp, 77252436, classes 29/30 and ROSALINDA'S ... CANTINA STYLE, Snak-King LLC, 97359505, class 30 tortilla chips; ROSALINE' (Culinary Lab Partners, LLC, 87776033, class 43 restaurant and bar); ROSALYN THE TASTE OF NATURE (Atlantic Golden Age Holding Inc., 98754607, class 29 sea cucumbers); ROSALYNN CARTER BUTTERFLY TRAIL (class 31 seeds among others); ROSALYNN DANIELS (Brown Hands Media, 97426482, classes 35/41/43); ROSALIND WHEELER (Wayfair, 87234635, includes class 35). — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [Trademarkia](https://www.trademarkia.com/search/trademarks?query=rosalind)
- Not live (checked): ROSALIND 77029764 wine (cancelled), ROSALIND Mattel doll (abandoned), ROSALINDA class 34 e-cigarette cartridges, Gonzalez Rubio, 97727454 (abandoned), ROSALIND Cotinga Pharmaceuticals software (abandoned). — USPTO backend
- Other live ROSALIND marks, not target classes: ROSALIND, OnRamp Bioinformatics, 87705172, classes 9/42 (genomic software platform); ROSALIND AI, DNA Labs International, 99659054, class 42; ROSALIND, Guangzhou Shida, 97260795, class 3; many ROSALIND FRANKLIN UNIVERSITY OF MEDICINE AND SCIENCE marks (education and health services). — USPTO backend, [Trademarkia](https://www.trademarkia.com/search/trademarks?query=rosalind)
- Variants rosalyn (16 results), rosalynd (0), rosaline (8): nothing else in target classes. Phrase forms: no ROSALIND SOCIETY / CLUB / SUPPLY / TINS mark.

**Domains (RDAP)**
| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| rosalind.com | registered | 2001-10-03 / 2028-10-03 | GoDaddy | Parked, redirects to /lander (Afternic nameservers); price not retrievable (GoDaddy sale page returned 403) |
| getrosalind.com | registered | 2026-04-16 / 2027-04-16 | Spaceship | Parked; Afternic page: "Buy it now for $1,500.00" or make an offer (read via fetch tool, 2026-10-27) — [Afternic](https://www.afternic.com/domain/getrosalind.com) |
| rosalindsociety.com, rosalindclub.com, rosalindsupply.com, rosalindtins.com, rosalindpouches.com, tryrosalind.com | NOT registered (404) | | | |

**Search collisions**
- "Rosalind Club": the Rosalind Club of Orlando, Florida, a women's club founded 1894, named for the Shakespeare character. A historic women's social club, not a commercial brand. — [Orlando Memory](https://orlandomemory.org/organizations/the-rosalind-club/), [VoiceMap](https://voicemap.me/tour/orlando/beyond-the-theme-parks-orlando-s-historical-highlights/sites/rosalind-club)
- Searches "Rosalind caffeine/pouches/coffee/energy/supplement" and "Rosalind nicotine/vape/cannabis": no brand found (weak search).

**Meaning / slang / fame**
- Female given name of Germanic origin; character in Shakespeare's As You Like It; a moon of Uranus. — [Wiktionary](https://en.wiktionary.org/wiki/Rosalind)
- Urban Dictionary: 10 entries; mostly a positive girl description; one reads "Veluptious. Very Curvy." and one "Annoying tan girl". — [UD API](https://api.urbandictionary.com/v0/define?term=rosalind)
- Famous associations: Rosalind Franklin (scientist) is implied by the many live ROSALIND FRANKLIN UNIVERSITY OF MEDICINE AND SCIENCE marks; a ROSALIND RUSSELL class 14 mark (86889767) appears in Trademarkia, status UNVERIFIED (not confirmed on the USPTO pull).

**Handles**: YouTube `@rosalind`, `@rosalindclub`, `@rosalindsociety`, `@rosalindsupply` all 404. TikTok `@rosalind` exists (58 followers); the other three not found. Instagram, Facebook, X NOT CHECKED.

### Inferences
- Fit: Sounds adult, literary and elegant (ROZ-uh-lind), clearly feminine, not cute and not a candy or teen word, and easy to sell as a "Rosalind Club" membership-style brand; there is a real women's club by that name, which supports the "club" idea but could also cause a local-name conflict. Nicotine look-alike risk is low; the "Ro-" start is only loosely near Roon and Rogue. Medical cue risk is the one to weigh: the name evokes Rosalind Franklin and a medical university, which brushes the owner's "no hospital or medical authority cue" rule, though it is a given name used in everyday life. It may read slightly old-fashioned. Implied-claim risk is low.

### Gaps
- Whether ROSALINDA'S (snacks) or David Austin's ROSALIND (roses) would be raised against a pouch brand; rosalind.com price; Instagram/Facebook/X.

---

## MARGAUX

### Takeaway
MARGAUX is the name most tied to alcohol: Chateau Margaux (Bordeaux wine) holds many live class 33 marks, and MADEMOISELLE DE MARGAUX (chocolate and coffee, class 30) is live. The owner's no-alcohol cue rule and the hard-to-say pronunciation count against it, and margauxsociety.com was registered in January 2026, though margauxclub.com is free.

### Cited Findings
**Trademark (USPTO backend 352 unique marks read incl. Margo/Margot; Trademarkia margaux 64 of 64 rows seen, margo 101, margot 67)**
- Live in target classes, MARGAUX family: MADEMOISELLE DE MARGAUX, 78584193, class 30 (cocoa, chocolate, coffee, pastries, confectionery), registered and renewed; MARGEAUX'S GOURMET SEASONINGS INC, Margaret I. Johnson, 98426290, class 30; MAISON MARGAUX, Good Food Is A Right LLC, 97551118, classes 36/41/43; MARGAUX AGENCY, 90630055, class 35; MARGAUX THE AGENCY (Margaux Models, LLC), 90125811, class 35. — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [Trademarkia](https://www.trademarkia.com/search/trademarks?query=margaux)
- Live in target classes, sound-alike MARGO/MARGOT: MARGO, Antya Waegemann, 90740086, class 5 (sexual-assault evidence collection kits); MARGO'S BARK, Margo's Bark Soda Co., LLC, 77676297, class 32 (energy drinks, soft drinks, water; registered and renewed); MARGOT'S MORSELS, 88834261, class 30; DEAR MARGO (Easy Greek) 99233055 and 99276793, class 43; MARGOT 97122029 and 97361642, class 43; MARGOT ELENA 97547065, class 35; LOVE, MARGOT 88879844, class 35; MARGO SUPPLIES (Ropes, Inc.) 90716411, class 35; MARGOTE (Jean-Marc Brocard, France) 79345595, classes 33/35; MARGOT92 90038800, classes 25/35; VIVI ET MARGOT 90695682, class 35; TIPICOS MARGOTH 99289603, class 43. (24 live rows in the family in target classes; the full list is in my scratch output, available on request.) — USPTO backend
- Live, wine class 33 (context): CHATEAU MARGAUX marks (SOCIETE CIVILE AGRICOLE CHATEAU MARGAUX, 79236950, 71348563 via Societe Civile et Immobiliere, 73571843, 73560209, 72446094) plus LE MARGAUX DU CHATEAU DE MALLERET 79295944, DOMAINE DE L'ILE MARGAUX 98423858, MARGAUX DE BRANE HENRI LURTON 99876088 (new application), CHATEAU LABEGORCE MARGAUX, CHATEAU DAUZAC MARGAUX. — USPTO backend
- Live, class 25/21/11 (context): MARGAUX, Margaux New York, LLC, 86459646, class 25 footwear; MARGAUX, Margaux New York, Inc., 99637780, class 25 (published for opposition); MARGAUX, Monroe Hair Care LLC, 77404054, class 21 hair brushes; MARGAUX, Kohler Co., 78749102, classes 11/6/21. — USPTO backend
- No live or pending MARGAUX SOCIETY / CLUB / SUPPLY / TINS mark; no mark in classes 5, 31, 32 or 34 for the exact word MARGAUX.

**Domains (RDAP)**
| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| margaux.com | registered | 1996-07-30 / 2030-07-29 | Tucows | "Reserved Web Site Address" page: "Looking for Cafe Margaux Restaurant in Cocoa? You want Cafemargaux.com" |
| margauxsociety.com | registered | 2026-01-13 / 2029-01-13 | GoDaddy (Squarespace DNS) | Squarespace "Website Expired" page; owner unknown |
| margauxclub.com, margauxsupply.com, margauxtins.com, margauxpouches.com, getmargaux.com, trymargaux.com | NOT registered (404) | | | |

**Search collisions**
- "Margaux Club" / "Margaux Society": no club brand; results are Margaux wine, The Wine Society's Margaux bottlings, and Mademoiselle de Margaux chocolatier (founded 1969, Margaux, France). — [Moodie Davitt](https://moodiedavittreport.com/mademoiselle-de-margaux-pairs-chocolate-with-fine-wines-spirits), [Justia owner page, search snippet](https://trademark.justia.com/owners/societe-civile-agricole-chateau-margaux-15484)
- "Margaux caffeine/pouches/coffee/energy/nicotine": no brand found (weak search). Women's brand: Margaux New York shoes (USPTO class 25 marks above).

**Meaning / slang / fame**
- Female given name from French; coordinate with Margo, Margot. — [Wiktionary](https://en.wiktionary.org/wiki/Margaux)
- Urban Dictionary: 10 entries; mostly a positive girl description; one plural entry reads "any number of sexy French females ... petite brunette". — [UD API](https://api.urbandictionary.com/v0/define?term=margaux)
- Fame: Chateau Margaux, a Bordeaux Premier Grand Cru (wine appellation and estate), the dominant meaning of the word for wine-aware US readers. — [Justia owner page via search](https://trademark.justia.com/owners/societe-civile-agricole-chateau-margaux-15484)

**Handles**: YouTube `@margaux`, `@margauxclub`, `@margauxsociety`, `@margauxsupply` all 404. TikTok `@margaux` exists (68 followers); `@margauxsupply` restricted (9 followers); `@margauxclub` returned code 209002 (unclear); `@margauxsociety` not found. Instagram, Facebook, X NOT CHECKED.

### Inferences
- Fit: Elegant and unmistakably feminine, and "Margaux Club" has a refined ring, but US speakers may stumble (mar-GOH, silent x) and many will read it as the wine, which breaks the no-alcohol-cue rule and could suggest a wine or cocktail club rather than a caffeine pouch. Not cute or young. No sleep, energy or medical cue. Nicotine look-alike risk is low in sound, though "Margo" sits near Mojo in rhythm only. Selling-wise it reads upscale but not simple. The margauxsociety.com registration in January 2026 suggests someone else considered the same pairing; owner unknown. Implied-claim risk is low.

### Gaps
- Who owns margauxsociety.com; whether wine fame would be asserted in class 5/30 (counsel); Instagram/Facebook/X.

---

## ANOUK

### Takeaway
ANOUK has the cleanest register of the six: no live or pending ANOUK mark in any of classes 5, 29, 30, 31, 32, 34, 35 or 43, and every phrase .com (anouksociety, anoukclub, anouksupply, anouktins, anoukpouches, getanouk, tryanouk) is unregistered. Its weaknesses are US pronunciation and several existing women's fashion businesses using the name abroad.

### Cited Findings
**Trademark (USPTO backend 67 unique marks read; Trademarkia anouk 10 of 10, anook 4 of 4 rows seen)**
- Live ANOUK-formative marks (all outside target classes): ANOUK MASSON KRANTZ, AMK Entertainment LLC, 98421409 and 98421416, class 16; ANOUKPC, Circle One Trade Co., 99341220, class 28. Live non-ANOUK matches from the wildcard (not similar marks): SIHANOUKVILLE, Tran's Family, 98191276, class 30 rice; MARTIROS MANOUKIAN, 99664018, classes 16/35/41 (notice of allowance); HANOUKALEE 99713573 class 20. — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [Trademarkia](https://www.trademarkia.com/search/trademarks?query=anouk)
- Dead ANOUK marks: ANOUK, Dino Music B.V. (classes 9, 41), ANOUK, Antonio Puig, S.A. (class 3, cancelled), ANOUK & CO. (class 35, cancelled), HOUSE OF ANOUK (class 18, abandoned), ANOUK, Alessandro Gabrielli (class 28), others. — USPTO backend
- Phonetic: ANOOK, The Dannon Company, 77086952 (class 29) and 77084728 (class 32), both cancelled or abandoned; ANOOK ATHLETICS (class 25, cancelled); ANOUCK / ANOUCK LEPERE (jewelry, abandoned). No live ANOOK or ANOUCK mark in target classes. — USPTO backend
- No ANOUK SOCIETY / CLUB / SUPPLY / TINS mark.

**Domains (RDAP)**
| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| anouk.com | registered | 1999-09-29 / 2027-09-29 | Tucows | Did not load (connection failed; fetch tool returned HTTP 503). Nameservers argewebhosting (Dutch host, inference only). Not checked further. |
| anouksociety.com, anoukclub.com, anouksupply.com, anouktins.com, anoukpouches.com, getanouk.com, tryanouk.com | NOT registered (404) | | | |

**Search collisions**
- Existing women's fashion brands named Anouk (all outside the pouch aisle): Anouk SA, a Swiss multi-brand women's fashion retailer (49 stores, women 30 to 50, majority bought by Imperial Spa in 2020); Anouk, an Indian women's ethnic-wear label owned by Myntra; Empreinte "Anouk" lingerie collection; Anouki (Georgia). — [PwC](https://www.pwc.ch/en/services/deals/deal-alert/anouk-sa-sold-to-imperial-spa.html), [FashionUnited](https://fashionunited.com/news/business/italian-fast-fashion-group-imperial-acquires-majority-stake-in-swiss-retailer-anouk/2020051233513), [Kyoorius awards](https://awards.kyoorius.com/2016/creative/anouk-bold-is-beautiful-digital-branded-film-content-and-entertainment.html), [Lingerie Briefs](https://lingeriebriefs.com/?p=88396)
- "Anouk Club" / "Anouk Society": no brand found. "Anouk caffeine/energy/nicotine/vape": no brand found (weak search).

**Meaning / slang / fame**
- Dutch given name, from French, popularised by actress Anouk Aimee, who took it after a 1947 film role; possibly a diminutive of Anne. — [Wiktionary](https://en.wiktionary.org/wiki/Anouk)
- Urban Dictionary: 10 entries, all positive descriptions of a girl (one says it "means ice bear", unverified). — [UD API](https://api.urbandictionary.com/v0/define?term=anouk)

**Handles**: YouTube `@anouk` exists (HTTP 200); `@anoukclub`, `@anouksociety`, `@anouksupply` 404. TikTok `@anouk` exists (31,200 followers); `@anoukclub`, `@anouksociety`, `@anouksupply` not found. Instagram, Facebook, X NOT CHECKED.

### Inferences
- Fit: Feminine, short, chic and clearly adult, with no candy, sleep, energy or medical cue; "Anouk Club" and "Anouk Society" both read as a boutique membership brand. It is the least likely of the six to be mistaken for a nicotine pouch (it sounds like none of Lucy, Fre, Zyn, Velo, ALP, Killa, Rogue, Sesh+, Nectr, Roon, Wip, Mojo, Ultra, Grinds, NZE, Plopii or Doseology). The risk is selling and speaking: many US speakers will say it differently (uh-NOOK vs ANN-ook, my reading) and may think "nook", and it needs a one-line audio hint on packaging; the odd spelling is harder to type from memory, so a misspelled domain/search could leak traffic. Existing fashion retailers named Anouk (Swiss, Indian) could matter if the brand sells apparel or merch in the US; for pouches the register is open as far as these tools show. Implied-claim risk is low.

### Gaps
- Content of anouk.com (not loaded) and whether it is for sale; Instagram/Facebook/X; WIPO and state registers; whether Myntra's Anouk or Anouk SA hold US applications not yet loaded in the backend.

---

## EDIE

### Takeaway
No live exact EDIE mark in classes 5, 29, 30, 31, 32, 34 or 35, and the phrase .coms are free, but the best-known Edie brand is Edie Parker, a luxury women's lifestyle label that sells lighters, pipes and oral-vaporizer accessories (live class 34 registration) and THC gummies: exactly the smoking-adjacent association this project must avoid. The name also reads old-fashioned cute.

### Cited Findings
**Trademark (USPTO backend; the `edie` token query returned 98 and `edie*` 122, `*edie` 189; Trademarkia edie 84 of 84 rows seen, edy 15, eddie 627 of 627)**
- Live in target classes (EDIE / EDY word, not Eddie surnames): LITTLE EDIE, Eva Marie Beale, 98034397, class 34 ashtrays (third extension granted); LITTLE EDIE VINTAGE 97916014, class 35; EDIE PARKER, Edie Parker LLC, 87597132, classes 14/21/35 (online retail of handbags and jewelry); FLOWER BY EDIE PARKER, Edie Parker LLC, 88627573, registered, includes **class 34: oral vaporizers for smoking purposes, water pipes, matches, cigarette paper, lighters, rolling trays, tobacco grinders and jars**; other Edie Parker filings: EDIE PARKER 77969395 (class 18 handbags), 86663611 (class 21), FLOWER BY EDIE PARKER 99735734 (class 14, published), 99735809 (class 4), 99735860 (class 3), EDIE PARKER FLOWER 99735569, 99735590, 99735654 (non-final action or published); EDIE'S OPTICS 98599232 and EDIE'S EYEWEAR 98613271 (Lorber Lenses, classes 9/35); EST D 2020 EDIE'S ALL DAY CAFE & BAR, Mag Hospitality, 90226426, class 43; HELLO EDIE 90863270 (jewelry, class 14/35); OLIVE & EDIE (DSW, 25/35); EDY'S (ice cream, Nestle, classes 30: 78565992, 74517999, 90124284, 99524863 notice of allowance); EDY'S GROCER, 90770396, classes 29/35/43. — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [Trademarkia](https://www.trademarkia.com/search/trademarks?query=edie)
- Live exact EDIE marks are in classes 9 and 42 only (EDIE, NovAtel Inc., 90693190; EDIE, Collective Medical Technologies, 85896218; EDIE, 9546-2966 Quebec Inc., 99453387). — USPTO backend
- Eddie/Eddy variants live in target classes are mostly surnames in food and drink (e.g. EDDIE MAE'S GOOD LEMONADE 99317398 class 32; EDDY OUT beer; EASY EDDY / WILD EDDY / ZERO EDDY, Big Grove, class 32 beer and non-alcoholic beer; EDDIE O'CLARE'S and EASY EDDIE'S, class 34 cigars; EDDY LEPP 50099731, class 34 pipes and oral vaporizers); context only. — USPTO backend
- No EDIE SOCIETY / CLUB / SUPPLY / TINS mark.

**Domains (RDAP)**
| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| edie.com | registered | 1996-04-17 / 2029-04-18 | Network Solutions | Fetch returned only a cookie/privacy banner; content UNVERIFIED |
| getedie.com | registered | 2024-11-06 / 2027-11-06 | Cloudflare | Vercel "DEPLOYMENT_NOT_FOUND" (dead project) |
| tryedie.com | registered | 2025-08-21 / 2027-08-21 | Cloudflare | Did not load |
| ediesociety.com, edieclub.com, ediesupply.com, edietins.com, ediepouches.com | NOT registered (404) | | | |

**Search collisions**
- Edie Parker: New York luxury lifestyle brand, founded 2010 by Brett Heyman (ex-Gucci PR), named for her daughter Edie, known for acrylic clutches; 2019 launch of Flower by Edie Parker (cannabis accessories, lighters, pipes) and THC gummies sold in Colorado dispensaries. — [The Quality Edit](https://www.thequalityedit.com/articles/brett-heyman-edie-parker-interview), [GreenState](https://www.greenstate.com/lifestyle/flower-by-edie-parker/), [SSENSE smoking accessories](https://www.ssense.com/en-au/everything-else/designers/edie-parker/smoking-accessories), [Element Vape listing](https://www.elementvape.com/edie-parker)
- "Edie Society" / "Edie Club": no brand; results are all Edie Parker. "Edie caffeine/energy/nicotine pouch": no brand found (weak search).

**Meaning / slang / fame**
- Female given name, diminutive of Edith, described in a Wiktionary quotation as an "old fashioned" name. — [Wiktionary](https://en.wiktionary.org/wiki/Edie)
- Urban Dictionary: 10 entries; mostly positive girl descriptions; one reads "Crude speaking; vulgar; awesome". — [UD API](https://api.urbandictionary.com/v0/define?term=edie)
- Famous associations (from USPTO records and general knowledge, not sourced here): Little Edie (Grey Gardens) shows in the live LITTLE EDIE marks.

**Handles**: YouTube `@edie` exists (200); `@ediesociety`, `@edieclub`, `@ediesupply` 404. TikTok `@edie` exists (47 followers), `@edieclub` exists (41 followers); `@ediesociety`, `@ediesupply` not found. Instagram, Facebook, X NOT CHECKED.

### Inferences
- Fit: Short, warm, easy to say (EE-dee) and easy to spell, so it would sell well, but it is the most likely of the six to read as "old-fashioned cute" (the owner's flag), and a nursing audience may hear a pet name. The decisive issue is Edie Parker: a women's luxury lifestyle brand that already uses EDIE in class 34 smoking goods and cannabis edibles, which makes an "Edie Club" pouch brand look like a smoking-accessory or cannabis extension and adds a nicotine/cannabis adjacency that conflicts with the no-nicotine-look-alike rule. It also invites a likelihood-of-confusion question for counsel (EDIE PARKER and FLOWER BY EDIE PARKER are the nearest marks). Implied-claim risk is low.

### Gaps
- What edie.com hosts; whether Edie Parker would object; Instagram/Facebook/X.

---

## MABEL

### Takeaway
MABEL has the most crowded, same-aisle register: MABEL'S (Highgate Investment Corp., Florida) is registered in classes 29/30/32 including soft-drink concentrates, MABEL is a registered cookie brand (class 30, CIPA, a leading Brazilian biscuit brand now owned by Camil), and MABEL is registered for acne medications in class 5. It also reads old-fashioned cute, and getmabel.com is a healthcare software company.

### Cited Findings
**Trademark (USPTO backend 265 unique marks read; Trademarkia mabel 91 of 91, mabelle 5, mable 34 rows seen)**
- Live in target classes: MABEL'S, Highgate Investment Corp. (Florida), 98465873, registered 2024-12-31: class 32 concentrates used in the preparation of soft drinks, class 29 peanut butter, jams, jellies, class 30 sauces and seasonings; MABEL, CIPA Industrial de Produtos Alimentares Ltda., 86458049, class 30 cookies, crackers, biscuits (Sec. 8 and 15 accepted); MABEL, Mabel Beauty Center, LLC, 90154469, class 5 acne medications and class 10 LED masks, registered; WOMABEL, Futurex, Inc., 97793571, class 5 dietary supplements (registered; differs by prefix, counsel to judge); AMABELZ, Lupin Limited, 87100819, class 5 oral contraceptives; BLUE MABEL, Blue Mabel, LLC, 88806002, class 43 restaurant; MABLE, Foundry Market, 88519207, class 35 online wholesale; MABEL & SCOUT 50020226 (class 35, new application); MAD MABEL 50023512 (classes 35/43, new application); MABEL OF MARBLEHEAD 50160704 (classes 9/35/41/43, new application); MAC & MABEL 97764293 (class 35); MABELY Q 90650360 (35/41); THEO & MABEL 90125068 and 90125071 (class 31 pet food); MABLE'S SMOKEHOUSE & BANQUET HALL 86620626 (class 43); MAX & MABLE ... 88789654 (class 35 beauty products); TOMABELLA 73751703 (29/30). — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [Trademarkia](https://www.trademarkia.com/search/trademarks?query=mabel)
- Context, classes 3/25: MABEL MARSEILLE 97782416 (class 3); MAGNUS & MABEL 88867413, MABEL AND HONEY 87190295 (Carousel Brands), MABEL MARIE 50151990, MABEL & COAST 50051362 (class 25 apparel); MABLE, Mable Inc., 99078884 (class 25). Other exact MABEL registrations: class 20 furniture (Kimball), class 28 dolls (Maison Battat), classes 35/42 software (BYOD, LLC). — USPTO backend
- No MABEL SOCIETY / CLUB / SUPPLY / TINS mark.

**Domains (RDAP)**
| Domain | RDAP | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| mabel.com | registered | 2001-11-05 / 2027-11-05 | Network Solutions | Did not load (HTTP 503 via fetch tool); not checked |
| mabelsupply.com | registered | 2020-09-20 / 2027-09-20 | GoDaddy | Parked, redirects to /lander; no price found (Afternic page returned 404) |
| getmabel.com | registered | 2020-05-28 / 2027-05-28 | Squarespace Domains II | In use: "Voluntary Alignment Software for ACO REACH & LEAD | Mabel" (healthcare software for accountable care organizations and CMS programs) — [site](https://getmabel.com/) |
| trymabel.com | registered | 2025-09-20 / 2027-09-20 | Spaceship | Parked; Afternic "Buy it now for $3,495.00" or make an offer (2026-10-27) — [Afternic](https://www.afternic.com/domain/trymabel.com) |
| mabelsociety.com, mabelclub.com, mabeltins.com, mabelpouches.com | NOT registered (404) | | | |

**Search collisions**
- Mabel cookies (Brazil): Camil bought the Mabel biscuit business from PepsiCo in August 2022 (also Mirabel, Doce Vida, Elbi's, Pavesino); Mabel is described as a leader in donut-style biscuits in Brazil. — [InvestNews](https://investnews.com.br/negocios/camil-compra-marca-de-biscoitos-mabel-e-recebe-aval-para-uso-da-toddy/amp/), [Money Times](https://www.moneytimes.com.br/camil-caml3-adquire-mabel-e-agrega-segmento-de-biscoitos-ao-portfolio/)
- Women's lifestyle brands: Mabel's Labels (Canadian, personal-belongings labels for children), Mabel Love Co (women's fashion), Mabel Magalhaes (Brazilian luxury fashion). — [CB Insights](https://www.cbinsights.com/company/mabels-labels-inc), [Thingtesting](https://thingtesting.com/brands/mabel-love-co), [Fashion Model Directory](https://fashionmodeldirectory.com/brands/mabel-magalhaes)
- "Mabel coffee/energy drink/pouches": no coffee, energy or pouch brand named Mabel found (weak search).

**Meaning / slang / fame**
- Female given name, clipped from Amabel, from Latin amabilis ("lovable"). — [Wiktionary](https://en.wiktionary.org/wiki/Mabel)
- Urban Dictionary: 10 entries; mostly positive; at least one sexual entry ("great in bed", "pornstar") and a "means beautiful in french" claim. — [UD API](https://api.urbandictionary.com/v0/define?term=mabel)
- Famous: Mabel Hubbard Bell (wife of Alexander Graham Bell) appears in search results. — [Infinite Women](https://www.infinite-women.com/women/mabel-hubbard-bell/); the TikTok `@mabel` account has about 1.3 million followers (likely the singer; UNVERIFIED).

**Handles**: YouTube `@mabel`, `@mabelclub`, `@mabelsociety`, `@mabelsupply` all 404. TikTok `@mabel` exists (1.3 million followers), `@mabelclub` exists (54), `@mabelsupply` exists (25); `@mabelsociety` not found. Instagram, Facebook, X NOT CHECKED.

### Inferences
- Fit: Easy to say and spell, feminine and warm, but it skews old-fashioned cute (the owner's flag), is a cartoon-sounding name to some US ears, and "lovable" is the dictionary root. Register is the most crowded of the six in the same aisle: a soft-drink concentrate registration (MABEL'S, class 32), a cookie brand (class 30) and an acne-medication registration (class 5), so a clash on food, beverage and health goods is plausible; counsel would need to decide. A healthcare-software company (getmabel.com) adds a medical-authority cue. Nicotine look-alike risk is low in sound. Implied-claim risk is low, but the class 5 acne-medication mark makes any health-adjacent copy riskier.

### Gaps
- What mabel.com hosts; mabelsupply.com price; Instagram/Facebook/X.

---

## Closing ranking (for choosing which to send to a trademark attorney)

### Takeaway
Order by register cleanliness first, then collisions and tone: 1 ANOUK, 2 ROSALIND, 3 ISADORA, 4 MARGAUX, 5 EDIE, 6 MABEL. Nothing here is cleared; the order only shows which names look less crowded in these tools.

### Cited Findings
1. **ANOUK**: no live or pending ANOUK, ANOOK or ANOUCK mark in classes 5/29/30/31/32/34/35/43; all seven phrase and get/try .coms unregistered; no food, caffeine, nicotine or supplement brand found. Cost: US pronunciation, anouk.com taken and unverified, women's fashion retailers named Anouk in Switzerland and India. — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [RDAP](https://rdap.verisign.com/com/v1/domain/anouksociety.com)
2. **ROSALIND**: live marks only in roses (class 31) and near-variants in snacks and cheese; rosalindsociety, rosalindclub, rosalindsupply and rosalindtins are unregistered; real historic "Rosalind Club" for women. Cost: Rosalind Franklin / medical-university and genomics-software associations (medical-cue rule), old-fashioned feel. — [Orlando Memory](https://orlandomemory.org/organizations/the-rosalind-club/), [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)
3. **ISADORA**: seven live exact ISADORA food registrations (classes 29/30), a US-sold Swedish women's cosmetics brand with the exact .com, "is adorable" cute reading; phrase .coms free. — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [IsaDora](https://www.isadora.com/about-us)
4. **MARGAUX**: Chateau Margaux wine (many live class 33 marks) breaks the alcohol-cue rule; MADEMOISELLE DE MARGAUX chocolate and coffee (class 30) live; margauxsociety.com registered January 2026; hard to pronounce. — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), [RDAP](https://rdap.verisign.com/com/v1/domain/margauxsociety.com)
5. **EDIE**: no live exact EDIE in food or pouch classes, but Edie Parker's live class 34 smoking/vaporizer goods and cannabis products create nicotine-adjacent association; old-fashioned cute. — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=edie), [GreenState](https://www.greenstate.com/lifestyle/flower-by-edie-parker/)
6. **MABEL**: live MABEL'S (class 32 soft-drink concentrates plus 29/30), MABEL cookies (class 30), MABEL acne medication (class 5), healthcare-software company on getmabel.com, cute/old-fashioned skew; mabelsupply.com, getmabel.com, trymabel.com taken (only mabelsociety/mabelclub free). — [USPTO backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)

### Inferences
- Rank 1 vs 2 is close: ANOUK wins on the register, ROSALIND on pronounceability and "club" heritage. If the owner weighs "easy to say" above a clean register, ROSALIND should go first.
- For the preferred form: all four phrase .coms are unregistered for ANOUK, ROSALIND and ISADORA (isadoraclub, isadorasociety, isadorasupply, isadoratins). For MARGAUX only margauxclub, margauxsupply, margauxtins are free; for EDIE all four are free; for MABEL only mabelsociety, mabelclub, mabeltins are free.
- None of the six sounds like the listed nicotine or caffeine pouch brands; the shared feature with Lucy is only that it is a girl's name, so the separate word (Society, Club) matters.

### Gaps
- No Instagram, Facebook, X or state-register checks; no similar-meaning or design-mark search; web search tool was weak on exact brand queries.

### For a professional (trademark attorney)
- Run a full search on ANOUK and ROSALIND first (similarity, translation, design marks, common law, state registers), and ask about: ANOUK in apparel abroad (Anouk SA, Myntra Anouk) if merchandise is planned; ROSALIND/ROSALINDA'S/ROSALINA in classes 29/30/31; the Rosalind Franklin University marks.
- If ISADORA stays in play: the seven ISADORA food registrations (Productos Verde Valle) and IsaDora cosmetics (Invima AG, Isadora AB).
- If EDIE stays in play: FLOWER BY EDIE PARKER class 34 and the EDIE PARKER family. If MABEL: MABEL'S class 32, MABEL class 30 and class 5. If MARGAUX: Chateau Margaux class 33 family and MADEMOISELLE DE MARGAUX class 30.
- Review any "Society" or "Club" membership language and any dosing copy for implied claims; the brand must stay free of health, sleep, alertness and nicotine-replacement cues.

### Verification still owed (not done)
- Instagram, Facebook, X handles; WIPO; state registers; Google exact-phrase results; content of anouk.com, mabel.com, edie.com; ownership of margauxsociety.com and the parked domains; prices for rosalind.com and mabelsupply.com.
