# Nightwell alternatives: LIGHT, LAMP and WATCH imagery (US adults-only 25 mg caffeine pouch, women working overnight)

Checked 2026-10-27. NOT a legal clearance. No name here is "clear" or "safe". A trademark attorney must run a full search (similarity, translation, design marks, state registers, unregistered use) before any name is adopted. Mirror and snippet data is marked UNVERIFIED. Nothing was invented; where a check was not run it says "not checked".

## How the data was obtained (and limits)

- **USPTO backend (primary-source route, undocumented):** `POST https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch` (site https://tmsearch.uspto.gov/), method per `deep_screen_increment_scruple_caliper.md`. Body used: `{"query":{"bool":{"must":[{"wildcard":{"wordmark":"name*"}}]}},"size":100,"from":N}` for `name*` and `*name*`, and `match_phrase` for two-word forms ("harbor light"). Wildcards with a space do NOT work (return 0); `match_phrase` does. Results were filtered to live marks in classes 5, 29, 30, 31, 32, 34, 35, 43 (class 43 and 35 included per brief). Recent filings may be missing from this index. It does not do similar-sound or similar-meaning searches.
- **Trademarkia (mirror, UNVERIFIED):** `https://www.trademarkia.com/search/trademarks?query=<word>`, browser User-Agent. Run only for the four deep-screen names plus harborlight; exact-word counts below.
- **RDAP:** `https://rdap.verisign.com/com/v1/domain/<name>.com` (200 = registered, 404 = not registered). Afternic pages are templated and do not show a price to curl; price = "not determined" for every domain.
- **Web search tool** was weak for exact-brand queries (returns generic caffeine-pouch SEO pages); absence of results is weak evidence only.
- **Not run:** Instagram/Facebook/X handles (login wall, NOT CHECKED), WIPO, state registers, Google result pages, Urban Dictionary for the rejected names Lamplighter, Lamplit, Porchlight, Taper, Pharos, Vesper, Harborlight, Lampwick (not checked). Wiktionary API failed; HTML pages were read directly where noted.

---

## 1. Fifteen candidates, quick screen

Night-shift implication = honest read of how strongly the name signals overnight use (Strong / Moderate / Weak). USPTO column = live/pending marks in target classes for the exact word or its direct compounds, with total hits read.

| # | Name | USPTO backend (live/pending, target classes) | Domains (.com RDAP) | Night-shift read | Verdict |
|---|---|---|---|---|---|
| 1 | **RUSHLIGHT** | 2 hits total, all read. None in target classes (RUSHLIGHT pending class 9 radar, C Speed LLC, 50067311; RUSHLIGHT class 11 abandoned). | rushlight.com taken ("Coming Soon" page); get/co/pouches/try/coffee all NOT registered | Strong (historic cheap night candle; Dickens: "night-light") | DEEP SCREEN. Caveat: "rush" can read as energy rush |
| 2 | **LOWLAMP** | 1 hit (FLOWLAMP, class 11, unrelated). Zero LOWLAMP. | lowlamp.com taken (IONOS, blank page); all 5 variants NOT registered | Strong (low light at night) | DEEP SCREEN |
| 3 | **STREETLAMP** | 5 hits, all read. STREETLAMP + STREETLAMP STUDIO pending classes 9/41/42 (Lemon Inc.); STREETLAMP BAKERY class 30 abandoned (88365010). None live in target classes. | streetlamp.com taken (HTTP 502); 5 variants NOT registered | Strong | DEEP SCREEN |
| 4 | **WICKLIGHT** | 0 hits (WICKLITE x2 live, non-target). | wicklight.com taken (2008); 5 variants NOT registered | Moderate | DEEP SCREEN (weakest; see slang and smoking-adjacent collision) |
| 5 | Cresset | 28 hits read. Live in target classes: only CRESSET CARES (35/36 charity/finance). Large class 36 family (Cresset Capital). | cresset.com taken (Cresset Chemical); cressetco.com expires 2026-11-16 (GoDaddy); others free | Weak (obscure word for a beacon fire-basket) | Parked: obscure, owned by a finance brand in classes 35/36 |
| 6 | Lamplighter | 88 hits. **LAMPLIGHTER pipe tobacco class 34 live (Tinder Box, 73058610)**; LAMPLIGHTER BREWING class 32 beer live; LAMPLIGHTER hotel/restaurant class 43 live. | taken; lamplightercoffee.com registered | Strong | REJECT: tobacco and beer marks live |
| 7 | Lamplit | 3 hits, 1 alive, none target. | lamplit.com (exp 2026-11-29); **lamplitco.com registered today 2026-10-27**; others free | Strong | Parked: unconfirmed; fresh registration of a variant is a signal. Not deep-screened |
| 8 | Porchlight | 61 hits. PORCHLIGHT cigars class 34 pending (Brolo Cigar Co., 99939662); PORCHLIGHT beer class 32 (Big Rock); PORCHLIGHT restaurant class 43 (USHG); PORCH LIGHT COFFEE AND CREAMERY class 30 pending (50074063). | 5 of 6 domains taken | Strong | REJECT: cigar, beer, coffee marks |
| 9 | Taper | 407/511 hits. TAPERANCE class 5 analgesic (97754267); TAPERED TASTE class 30 coffee. | taper.com + 3 variants taken | Weak | REJECT on meaning: "taper" = reducing a drug or nicotine dose (implied quit/dose claim) |
| 10 | Pharos | 95/114 hits. **PHAROS class 5 pet dietary supplements (Pharos Animal Health, 88890753)**; EGYPTIAN PHAROS class 34 tobacco; PHAROS class 35, 43 (pending). | 5 of 6 taken | Moderate (lighthouse) | REJECT: class 5 supplement mark, tobacco mark |
| 11 | Vesper | 189/192 hits. **VESPER class 5 herbal relaxation elixirs (Pique Life, 99407867)**; **AURORA & VESPER class 5 supplements/drink mixes (99832841)**; VESPER insecticide class 5. | all 6 taken | Moderate (evening) | REJECT: class 5 supplements, and relaxation-claim zone |
| 12 | Sconce | 49 hits, 13 alive, none target. | sconce.com redirects to PDSVISION ("Sconce Solutions Inc is now PDSVISION"); 5 variants free | Weak-Moderate (candle wall holder) | Parked: awkward sound; UD senses include UK university drinking forfeit and a slur |
| 13 | Harborlight | 12 hits for single word, none live in target classes (HARBORLIGHT cookies class 30 abandoned 2005). But phrase form: **HARBOR LIGHT COFFEE class 30/39 live (Mauro Pennisi, 76678120)**; **HARBOR LIGHT HOSPICE class 44 live (Hospice of America, 77072465/77072476)**; HARBOR LIGHT Salvation Army class 42 live. Trademarkia 9 results. | getharborlight.com registered 2026-10-12 with a live app site; harborlightco.com, tryharborlight.com parked 2026 | Moderate-Strong | REJECT: hospice (medical/end-of-life cue), coffee, recent third-party use |
| 14 | Glim | 626/717 hits (600 of each read; 26/117 unread). No exact GLIM in target classes seen; GLIMMER BOMB (beverage powders, class 30/32, 97519253) and GLIMMER alcohol-free wine (class 32) are near. | glim.com (HTTP 436), getglim, glimco, tryglim, glimcoffee all taken | Moderate | REJECT: beverage-powder neighbours, short word crowded online, spark/glimmer cliché |
| 15 | Lampwick | 0 hits. | lampwick.com taken (2004); 5 variants free | Strong | REJECT: Lampwick is the troublemaking boy in Pinocchio (general knowledge, UNVERIFIED by search): cartoon and youth association |

Source for all USPTO columns: https://tmsearch.uspto.gov/ backend (queried 2026-10-27). Source for all domain columns: https://rdap.verisign.com/com/v1/domain/ (2026-10-27).

---

## 2. Deep screens (best four)

### RUSHLIGHT

**Trademark.** USPTO backend `rushlight*` and `*rushlight*`: 2 hits each, same 2 marks, both read (https://tmsearch.uspto.gov/). RUSHLIGHT, C Speed, LLC, serial 50067311, class 9 electronic surveillance apparatus (radar), new application not yet examined; RUSHLIGHT, Gaijin-Works LLC, 90339972, class 11 UV sanitizing light box, abandoned. Variants `rushlite*` and `rushlit*`: 2 hits, 0 alive. Phrase "rush light": 0. Trademarkia exact "rushlight": 2 results, both seen (https://www.trademarkia.com/search/trademarks?query=rushlight, UNVERIFIED mirror). No live or pending mark in 5, 29, 30, 31, 32, 34, 35, 43. Not covered: similar-sounding forms such as "RUSH" family marks in classes 5/30/32 (RUSH is a common energy-style word; not searched).

**Domains** (https://rdap.verisign.com/com/v1/domain/rushlight.com etc.):
| Domain | Status |
|---|---|
| rushlight.com | registered 2005-06-08, exp 2027-06-08, GoDaddy; page "rushlight.com - Coming Soon" (read 2026-10-27); Afternic page is a templated listing, price not determined |
| getrushlight.com, rushlightco.com, rushlightpouches.com, tryrushlight.com, rushlightcoffee.com | NOT registered (404) |

**Search collisions.** Web searches "Rushlight caffeine OR pouches OR energy OR supplement brand" and "Rushlight brand coffee OR tea OR supplement OR vape OR drink": no Rushlight brand found in food, drink, supplement, sleep, caffeine, nicotine or vape (weak tool; generic caffeine pouch pages returned). Searches for "sleep" and "nicotine" variants individually were not run.

**Meaning/slang.** Wiktionary: "(historical) A type of inexpensive candle formed by soaking the dried pith of the rush plant in fat or grease"; quotations include Dickens, Great Expectations ("a night-light ... the good old constitutional rushlight") — https://en.wiktionary.org/wiki/rushlight. Urban Dictionary (2 entries): a paranoia-about-lights sense, and a pet-rat-owner sense; no sexual or drug slang found — https://api.urbandictionary.com/v0/define?term=rushlight. Other languages: not checked.

**Handles.** YouTube @rushlight: HTTP 404 (not existing). TikTok @rushlight: EXISTS (nickname in Cyrillic, status 0; activity not inspected). Instagram/Facebook/X: NOT CHECKED.

**Fit.** Calm, quiet and adult, a candle for people up at night, with literary weight and no link to nicotine brands (two syllables, soft endings, nothing like ZYN/VELO/On!). Night-shift implication: strong, but understated. Dose transparency: "25 mg" prints cleanly beside it. Youth appeal: low. Implied-claim risk: the first syllable "rush" can read as an energy/caffeine rush, which brushes against the rule on implied energy claims; counsel should judge, and copy must never lean on "rush". Adult-only 21+ fits.

### LOWLAMP

**Trademark.** USPTO backend `lowlamp*`: 0; `*lowlamp*`: 1 (FLOWLAMP, Shenzhen Furuo Photo-Electric, 88279005, class 11 lighting, live). Variants `lowlamps*`, `lolamp*`: 0 and 1 dead. Phrase "low lamp": 0. Trademarkia exact "lowlamp": 0 results (https://www.trademarkia.com/search/trademarks?query=lowlamp, UNVERIFIED). No live or pending marks in any target class. Not covered: phonetic variants like "LOWLAMPE", "LOW-LAMP" as two words in design marks.

**Domains.**
| Domain | Status |
|---|---|
| lowlamp.com | registered 2016-09-09, exp 2027-09-09, IONOS; page shows only "index" (blank); Afternic page templated, price not determined |
| getlowlamp.com, lowlampco.com, lowlamppouches.com, trylowlamp.com, lowlampcoffee.com | NOT registered (404) |

**Search collisions.** Web search `"Lowlamp" OR "Low Lamp" caffeine OR coffee OR supplement OR sleep brand`: no brand named Lowlamp found; returned unrelated low-caffeine/sleep brands (Buzz Lite, ThinkNOO, Clevr). Not run: separate pouches, energy, nicotine queries.

**Meaning/slang.** Not a dictionary word: Wiktionary "lowlamp" and "low_lamp" pages do not exist (HTTP 404, https://en.wiktionary.org/wiki/lowlamp). Urban Dictionary "lowlamp" (4 entries, thumbs unknown): "Laughing Out Load" style joke; an online-game term for a person who skips events; "to calm down, or chill" (low + lam); and a "scary/creepy/pedophilic person" entry — all low-evidence, but the last is an unpleasant association — https://api.urbandictionary.com/v0/define?term=lowlamp. Other languages: not checked.

**Handles.** YouTube @lowlamp: EXISTS (HTTP 200, not inspected). TikTok @lowlamp: account exists, status 10222 (restricted/private, UNVERIFIED meaning). Instagram/Facebook/X: NOT CHECKED.

**Fit.** The coined compound is clean in the register and carries "low light" (dim break-room, quiet hours) plus "low dose" for a deliberately low 25 mg product. Night-shift implication: strong. Nicotine look-alike: low (two-word soft compound, not hard-consonant). Youth appeal: low. Implied-claim risk: "low" is factual for 25 mg but must not become "low-jitter" or calming copy; no sleep or calm claim in the name itself. Weaknesses: a made-up pairing that is awkward to say ("low-lamp"), slightly clunky, and the UD entries.

### STREETLAMP

**Trademark.** USPTO backend `streetlamp*` and `*streetlamp*`: 5 hits each, same marks, all read. Live/pending: STREETLAMP (99784457) and STREETLAMP STUDIO (99784456), Lemon Inc. (Cayman Islands), classes 9/41/42 games and software, status suspension letter mailed; MAISON FAROLA (Farola Flowers, class 44, matched on a translation, UNVERIFIED reason). Dead: STREETLAMP BAKERY (88365010, class 30 baked goods, abandoned, no statement of use); UNDER THE STREETLAMP (class 41, cancelled). Variants: `streetlamps*`: 0; `streetlite*`: 6 hits, 1 alive non-target. Compound spelling "STREETLIGHT" (different word): 41 hits, with **STREETLIGHT class 30 coffee, Streetlight Coffee and Skate LLC (50161220, new application)** and **STREETLIGHTS COFFEE class 30 (Lisa Wynn, 99668098, notice of allowance)** — a near-neighbour that matters because a buyer may confuse lamp/light. Phrase "street lamp": 4 hits, 0 alive. Trademarkia exact "streetlamp": 4 results, all seen (UNVERIFIED mirror). No live STREETLAMP in 5, 29, 30, 31, 32, 34, 35, 43.

**Domains.**
| Domain | Status |
|---|---|
| streetlamp.com | registered 1996-04-23, exp 2032-04-24, Network Solutions; site returned HTTP 502 on 2026-10-27; Afternic templated, price not determined |
| getstreetlamp.com, streetlampco.com, streetlamppouches.com, trystreetlamp.com, streetlampcoffee.com | NOT registered (404) |

**Search collisions.** Web searches "Streetlamp caffeine OR pouches OR energy drink OR supplement brand" and `"Streetlamp" drink OR coffee OR "energy" OR nicotine brand USA`: no Streetlamp brand in food, drink, supplement, caffeine, nicotine or vape found (weak). Closest: Street Lights beer (Brighter Days Brewing, different name) — https://untappd.com/b/brighter-days-brewing-company-street-lights/6274494.

**Meaning/slang.** Wiktionary: "Alternative form of street lamp" — https://en.wiktionary.org/wiki/streetlamp. Urban Dictionary (6 entries): a person-name/"gentleman" entry, a slang for a crude word, a "connecting in harmony" entry, and a street pick-up-artist sense ("talk to and pick-up women ... on the bus") — https://api.urbandictionary.com/v0/define?term=streetlamp. "Under the streetlamp" also evokes street solicitation to some readers (general association, UNVERIFIED, no source).

**Handles.** YouTube @streetlamp: 404 (not existing). TikTok @streetlamp: EXISTS (status 0, not inspected). Instagram/Facebook/X: NOT CHECKED.

**Fit.** Night-shift implication: strong and very visual (the lamp you drive home under). Calm adult feel, and an urban/working-night mood that fits shift workers rather than students. Nicotine look-alike: low. Youth appeal: low. Implied claim: none in the word. Weaknesses: a plain common noun (weaker mark, more descriptive-feeling), it is close to STREETLIGHT coffee marks, "street" tone is less feminine/soft than the brief, and the street-solicitation association.

### WICKLIGHT

**Trademark.** USPTO backend `wicklight*` and `*wicklight*`: 0 hits. Variants `wicklite*` and `wicklit*`: 2 alive each, none in target classes. Trademarkia: not run. No live or pending marks found in target classes. Zero hits means no precedence found, not clearance.

**Domains.**
| Domain | Status |
|---|---|
| wicklight.com | registered 2008-08-05, exp 2027-08-05, TurnCommerce; content not fetched (HTTP 429 on Wiktionary only; domain page not inspected) |
| getwicklight.com, wicklightco.com, wicklightpouches.com, trywicklight.com, wicklightcoffee.com | NOT registered (404) |

**Search collisions.** Web search `"Wicklight" brand candle OR supplement OR drink OR vape`: no Wicklight supplement, drink or vape brand. Found: "The Wick" portable LED candle lantern (Graypants, sold by the Getty Museum shop) — https://shop.getty.edu/products/portable-wick-light; and "Wick Light", a hemp wick sold with a BIC mini lighter in a 2017 High Times lighter roundup — https://hightimes.com/products/best-lighters-2017/2/ (a smoking-accessory association, which is the wrong signal for a nicotine-adjacent screen).

**Meaning/slang.** Not a dictionary word; Wiktionary page not read (HTTP 429). Urban Dictionary (6 entries): a bird species, a crude entry about taping a flashlight to the body, and other sexual entries — https://api.urbandictionary.com/v0/define?term=wicklight. Other languages: not checked.

**Handles.** YouTube @wicklight: EXISTS (HTTP 200, not inspected). TikTok @wicklight: EXISTS (nickname "BETTER PFP SOON xD", status 0). Instagram/Facebook/X: NOT CHECKED.

**Fit.** Candle imagery, quiet and adult. Night-shift implication: moderate. Nicotine look-alike: low from the word, but the "Wick Light" hemp lighter product ties it to smoking. Youth appeal: the crude UD entries are the only concern. Implied claim: none. Weaker than the other three.

---

## 3. Ranked top 3 (for the owner to send to a trademark attorney)

Ranking basis: cleanest registers in target classes, no collision with a food/supplement/tobacco/nicotine brand found, fit with the brief, and fewest implied-claim and slang problems. Evidence is "nothing found by these tools", not "nothing exists".

1. **RUSHLIGHT.** Best brand feel and strongest night-shift heritage (the old night-light candle). Register: no live mark in the target classes, two hits in total. All five modifier domains (get/co/pouches/try/coffee) are open. Risk to flag: "rush" reads as an energy rush, so counsel must judge it against the no-implied-energy rule; also rushlight.com is taken and TikTok @rushlight exists.
2. **LOWLAMP.** Zero marks anywhere near, all five modifier domains open, and the "low" suggests a low, honest 25 mg. Risks: a coined word, awkward to say, thin web footprint (neither good nor bad), a few unpleasant low-evidence UD entries, YouTube @lowlamp exists.
3. **STREETLAMP.** Clean in target classes (pending Lemon Inc. marks are games/software, 9/41/42), all five modifier domains open, very strong night imagery. Risks: a plain common noun (weaker mark), STREETLIGHT coffee marks are pending/allowed in class 30, a street-pickup slang sense, streetlamp.com is held.

Not recommended: Wicklight (smoking-accessory "Wick Light" product, crude slang), and the ten rejected names above.

None of the three has been checked for similar-sounding marks beyond the spellings listed, and Instagram/Facebook/X handles are NOT CHECKED for all of them.

### For a professional (trademark attorney)
- Full clearance search on RUSHLIGHT first; ask specifically about RUSH-formative marks in classes 5/30/32 and about RUSHLIGHT (C Speed LLC, class 9, serial 50067311).
- LOWLAMP: search for LOW-formative and LAMP-formative marks in classes 5/30/32/34 and the coined-compound strength.
- STREETLAMP: likelihood of confusion with STREETLIGHT coffee marks (50161220, 99668098) and the Lemon Inc. STREETLAMP filings.
- Review all three names and any tagline for implied energy, alertness or night-shift claims, and for nicotine-pouch look-alike risk.

### Verification still owed (not done)
- Instagram, Facebook, X handles; WIPO; state registers; Google results; who owns rushlight.com, lowlamp.com, streetlamp.com and any asking price (Afternic prices not visible); content of wicklight.com and the TikTok/YouTube accounts above; Urban Dictionary and Wiktionary for the ten non-deep names where marked "not checked"; other-language meanings for all four deep names.
