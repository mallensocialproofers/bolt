# Nightwell alternatives: MOON, STARS, SKY and QUIET PLACES territory

Checked 2026-10-27. NOT a legal clearance. No name here is "clear" or "safe". A trademark attorney must run a full search (similarity, translation, design marks, common law, state registers) before any name is adopted. Mirror and snippet data are marked UNVERIFIED. "Not checked" means a wall or error stopped the check.

## Candidate table, trademark and domain quick screen, then deep screens, ranked top 3

### Takeaway
Of 17 names screened, EVENFALL has the cleanest food/supplement/beverage/tobacco picture with a clear night-time reading, NORTHFALL has no USPTO marks at all but almost no night-shift meaning, and GLOAMING has the strongest night feel but sits next to live GLOAM (smokeless tobacco) and GLOAMM (coffee) marks. PERIGEE was dropped because PERIGEA (energy shots) is live in Class 32. Nothing is cleared.

### How the data was obtained
- USPTO trademark search backend: `POST https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch` (Elasticsearch-style `wildcard` on `wordmark`, 100 per page), the same undocumented route described in `/home/user/bolt/research_notes/Bolt replacement brand name research/deep_screen_increment_scruple_caliper.md`. Primary-source records; recent filings may be missing; no design-code or similar-meaning search. Source: https://tmsearch.uspto.gov/ (checked 2026-10-27).
- Quick screen filter: live/pending marks whose wordmark contains the word at a word start, in classes 5, 29, 30, 31, 32, 34, 35, 43. "Total" is the number of hits the backend reported for `*word*`; where the total exceeded 1,000 only the first 1,000 were read (noted).
- Trademarkia pages (https://www.trademarkia.com/search/trademarks?query=WORD) loaded with a browser User-Agent (HTTP 200) for all 15 core words, but the page carries no parseable result count in the server HTML and I did not page through them. Trademarkia was therefore NOT used as a count source in this note. Not checked: Trademarkia pages 2+, Justia, WIPO, state registers.
- Domains: Verisign RDAP https://rdap.verisign.com/com/v1/domain/NAME.com (200 = registered, 404 = not registered). Page content fetched with curl where it loaded. Several 2026-registered domains did not load from this environment ("did not load").
- Web search (WebSearch tool, US-only) was weak: for every exact-brand query it returned generic caffeine-pouch or sleep pages and no brand named the candidate. Treat "no collision found" as weak evidence only.
- Firecrawl was not used (out of credits).

### Candidate table (15 core + 2 surname/place-style extras)

Night-shift implication scale: Strong / Moderate / Weak / None (honest read of how much the word alone suggests working nights).

| # | Name | Meaning | Night-shift implication | Live/pending marks in classes 5/29/30/31/32/34/35/43 (USPTO backend) | .com state (name / get / co / pouches / try / coffee) | Verdict |
|---|---|---|---|---|---|---|
| 1 | EVENFALL | dusk, twilight (Wiktionary) | Moderate: evening, the start of a night shift, not sleep or alertness | 3 hits total; none in target classes live (EVENFALL beer Class 32 abandoned; live EVENFALL Class 24 bedding) | evenfall.com reg 1997 (musician page); getevenfall.com reg 2026-06-29; tryevenfall.com reg 2026-04-15; co/pouches/coffee not reg | DEEP SCREEN |
| 2 | GLOAMING | dusk, twilight (Wiktionary) | Strong: reads as the hour between day and night | 5 hits; none live in target classes, but neighbours GLOAM (Class 34 smokeless tobacco) and GLOAMM (Class 30 coffee) | gloaming.com reg 1997; getgloaming.com reg 2026-10-25 (two days ago); gloamingco.com reg 2022; gloamingcoffee.com reg 2026-05-11; pouches/try not reg | DEEP SCREEN |
| 3 | NORTHFALL | invented compound (not in Wiktionary) | None/Weak: no night meaning on its own | 0 hits for `northfal*`, `norfall*` | northfall.com reg 2006 (domain investment company); the other five not reg | DEEP SCREEN |
| 4 | GIBBOUS | moon phase, more than half lit | Moderate (moon) | 3 hits; none live in target classes (CAMP GIBBOUS Class 41, GIBBOUS NIMBUS Class 20) | gibbous.com reg 2001 (consulting firm); getgibbous.com reg 2026-07-01 (live moon-phase iPhone app); co/pouches/try/coffee not reg | DEEP SCREEN (live moon app and crude slang) |
| 5 | PERIGEE | moon's closest point to Earth | Weak | 32 hits; live in target classes: PERIGEE Class 35 industrial adhesives distributor only. BUT PERIGEA (Murphy Oil USA, 99123400, Class 32 energy shots, bottled water) is live | perigee.com reg 1995 (hosting page); getperigee.com reg 2020 (AI tools page); the rest not reg | DROPPED: PERIGEA energy shots one letter away |
| 6 | VESPER | evening star / evening prayer | Moderate-Strong | 192 hits; live VESPER Class 5 herbal elixirs "for relaxation" (Pique Life, 99407867, final action stage) and AURORA & VESPER Class 5 supplements (99832841, suspended) | not run beyond quick RDAP | DROPPED: crowded, relaxation goods in Class 5 |
| 7 | NOCTURNE | night piece | Strong | 107 hits; live NOCTURNE Class 30 chocolate (Guittard), Class 43 restaurant/bar, VANTA NOCTURNE Class 30 coffee (notice of allowance), DELIVERANCE NOCTURNE cigars Class 34 | not run | DROPPED: crowded in food, coffee, cigars |
| 8 | SOLSTICE | longest/shortest day | Weak | 402 hits; live SOLSTICE Class 30 tortilla chips, Class 43, Class 35, SOLSTICE TEA TRADERS Class 30, SOLSTICE lager Class 32, others | not run | DROPPED: crowded |
| 9 | MERIDIAN | noon line | None | 1,087 hits (first 1,000 read); live MERIDIAN TEA Class 30, MERIDIAN BIOSCIENCE Class 5, many Class 35 | not run | DROPPED: crowded |
| 10 | CAPELLA | star | Weak | 174 hits; live CAPELLA Class 30/32 flavorings (Capella Flavors), Class 31 blueberries, hotel Classes 35/43 | not run | DROPPED: Class 30/32 flavorings mark |
| 11 | NEAP | lowest tide | Weak | 1,604 hits; live NEAP Class 5 protein dietary supplements (Neap Foods, 98843705, Registered) | not run | DROPPED: exact mark in Class 5 |
| 12 | SYZYGY | sun, moon and Earth aligned | Weak | 70 hits; live SYZYGY Class 30 coffee (90706704) | not run | DROPPED: exact mark for coffee |
| 13 | MIZAR | star in the Plough | Weak | 42 hits; MIZARU Class 5 dietary supplements (79274365, Registered) is the only target-class hit; no exact MIZAR | mizar.com, getmizar, trymizar, mizarcoffee all reg; mizarco, mizarpouches not reg | Reserve; not deep screened (domains taken, MIZARU in Class 5) |
| 14 | ORRERY | model of the solar system | Weak | 2 hits total; none live in target classes | orrery.com reg 2004; getorrery.com, orreryco.com (software/AI firm), tryorrery.com reg 2026 | Reserve; weak night meaning, co/try/get taken |
| 15 | SLACK TIDE (as SLACKTIDE) | the still point between tides | Weak | 6 hits for `*slacktide*`; not read in detail | slacktide.com registered | Not deep screened; "slack" may suggest relaxing, UNVERIFIED reading |
| 16 | ASHCOMBE (surname/place style) | invented place-like name | None | 1 hit: ASHCOMBE Class 16 boxes (GR Vault LLC, 50005865, approved for publication) | ashcombe.com reg | Reserve; no night meaning |
| 17 | LOWMOOR (place style) | place name | None | 2 hits, both dead (Class 6) | lowmoor.com reg | Reserve; no night meaning |

Source for all rows: USPTO backend https://tmsearch.uspto.gov/ and Verisign RDAP, checked 2026-10-27. Not all RDAP states were run for rows 6 to 12 and 15 to 17 because they were dropped on trademark grounds (marked "not run").

Hard-constraint check done by reading the words: none of the 17 contains well, care, rx, vital, rest, sleep, calm, awake, alert, boost, wake, dream, charge or power, none sounds like Zyn/Velo/On!, and none is a cute animal. None is on the existing-pouch list. Note GLOAMING and EVENFALL imply a time of day, which is a time cue and not a benefit, but see the implied-claim comments below.

---

## EVENFALL (deep screen)

### Takeaway
No live or pending EVENFALL mark exists in the food, supplement, beverage or tobacco classes on the USPTO backend (3 hits total: an abandoned Class 32 beer filing, a live Class 24 bedding mark, a cancelled Mattel doll mark). A live EVENFLOW WORLDWIDE (Class 30 coffee) is a sound-and-look neighbour for counsel. The exact .com is a long-held musician's site; getevenfall.com and tryevenfall.com were registered this year by unknown parties.

### Cited Findings
**Trademark**
- `evenfall*` and `*evenfall*`: 3 hits total, all 3 read. EVENFALL, FGBC, LLC (Mississippi), 90152346, Class 32 beer, ABANDONED - no statement of use filed. EVENFALL, Melissa Susan Miller (individual, USA), 90486950, Class 24 bed blankets, covers, linen, bed sheets, bedding, REGISTERED. AERY EVENFALL, Mattel, 86507941, Class 28 dolls, CANCELLED. — [USPTO backend](https://tmsearch.uspto.gov/)
- Variants: `evenfal*` 3 hits (same set); `evenfl*` 73 hits (all read). Live in target classes among those: EVENFLOW WORLDWIDE (Evenflow Worldwide, LLC, 97215200, Classes 30 and 35, goods "Coffee", REGISTERED) and EVENFLO (Evenflo Company Holdings, 97669939, Class 5 nursing pads, REGISTERED). EVENFLO also appears in web search as a baby-products brand. — [USPTO backend](https://tmsearch.uspto.gov/)
- Common-law use not searched; Trademarkia total not captured (see method).

**Domains (RDAP, checked 2026-10-27)**
| Domain | State | Created / expires | Content |
|---|---|---|---|
| evenfall.com | registered | 1997-11-10 / 2027-11-09 | Page "Welcome", lists CDs (Telomere, Supergiant, Lux Primordia, Zoetosis, Astral Currents; Kunaki). A musician's site. For-sale status not found. — [RDAP](https://rdap.verisign.com/com/v1/domain/evenfall.com), [site](https://evenfall.com) |
| getevenfall.com | registered | 2026-06-29 / 2027-06-29 | Did not load; owner unknown |
| tryevenfall.com | registered | 2026-04-15 / 2027-04-15 | Did not load; owner unknown |
| evenfallco.com, evenfallpouches.com, evenfallcoffee.com | NOT registered (404) | | |

**Search collisions** (WebSearch, 2026-10-27: "Evenfall caffeine pouches", "Evenfall coffee OR supplement OR sleep OR nicotine brand", "Evenfall brand company products")
- No brand called Evenfall in food, drink, supplement, sleep, caffeine, nicotine or vape found. Results were generic or showed lookalikes (Evenflo baby products and pigments). Weak evidence. — e.g. [generic search result](https://tobaccoinsider.com/caffeine-pouches/)

**Meaning**
- Wiktionary: noun, "dusk, twilight". — [Wiktionary](https://en.wiktionary.org/wiki/evenfall)
- Urban Dictionary: one entry, "kind of like an oddball, but much smarter", 0 thumbs. — [UD API](https://api.urbandictionary.com/v0/define?term=evenfall)
- Other languages: not found / not checked.

**Handles (2026-10-27)**
- YouTube @evenfall EXISTS (HTTP 200, content not inspected); @getevenfall, @evenfallco: 404. TikTok @evenfall exists (page data: 45 followers, statusCode 10222, probably private or restricted, UNVERIFIED); @getevenfall, @evenfallco not found (10221). Instagram, Facebook, X: not checked (login walls).

### Inferences
- The register looks open in the target classes for the exact word, but the EVENFLOW coffee mark and the Class 24 bedding mark are the two things a lawyer will ask about; bedding is also a sleep-adjacent field.
- Two "get/try" domains registered in 2026 suggest someone else has recently considered the name, UNVERIFIED.

### Gaps
- Trademarkia counts, WIPO, state registers, Instagram/Facebook/X, who owns getevenfall.com / tryevenfall.com, evenfall.com sale price.

### Fit (one paragraph)
EVENFALL names the hour when daylight ends, which fits a product used by people starting an overnight shift without saying "sleep", "rest" or "alert". Night-shift implication: moderate; a general reader may also think of ordinary evening use. It is adult and quiet, and "25 mg" can sit beside it on the label. Nicotine-pouch look-alike risk is low (soft sounds, three syllables). Youth appeal is low, though the fantasy-game ring of the word (it appears in game titles, UNVERIFIED) is worth a counsel check. Implied-claim risk: low from the word; "fall" could be misread as "fall asleep", so tagline copy must avoid any bedtime idea. Possible conflict with the evening-use caffeine messaging is a lawyer question: an evening-use pouch is not a safety claim anyone should make.

---

## GLOAMING (deep screen)

### Takeaway
Strongest night-time feel of the set, but the register has near neighbours GLOAM (Class 34 smokeless tobacco, live) and GLOAMM (Class 30 coffee, live), both filed by Chinese applicants, and getgloaming.com was registered two days ago (2026-10-25). No exact GLOAMING mark is live in Classes 5/29/30/31/32/34/35/43.

### Cited Findings
**Trademark**
- `gloaming*`: 5 hits total, all read. Live GLOAMING: Wenzhou Xiyun Textile Products Co., Ltd., 90099007, Class 24 quilts, bed covers, bed linen, REGISTERED; GLOAMING, Melissa Asher Morgan (individual, USA), 99872509, Classes 9 and 42 astrology/divination mobile app, PUBLISHED FOR OPPOSITION; A GLOAMING NIGHT, Coty Beauty Germany, 79295565, Classes 3 and 35 cosmetics, REGISTERED. Dead: two Avon GLOAMING marks (Class 3, expired). — [USPTO backend](https://tmsearch.uspto.gov/)
- `gloam*`: 18 hits total, all read. Live target-class neighbours: GLOAM, Shenzhen SKE Technology Co., Ltd., 99509175, Class 34 "Smokeless tobacco; cigarettes containing tobacco substitutes", REGISTERED; GLOAMM, Xia Yu (China), 99427156, Class 30 "Candy; tea bags; coffee and tea; coffee based beverages; ice creams ...", REGISTERED. Other GLOAM- marks are in Classes 3, 9, 11, 24, 25, 28, 42 (GLOAM Class 3 cosmetics, Emeis Cosmetics; GLOAM Class 42, Roberto Febus). — [USPTO backend](https://tmsearch.uspto.gov/)
- `gloamin*` 5 hits (same set).

**Domains (RDAP, 2026-10-27)**
| Domain | State | Created / expires | Content |
|---|---|---|---|
| gloaming.com | registered | 1997-09-28 / 2030-09-27 | Did not load; owner/for-sale unknown |
| getgloaming.com | registered | 2026-10-25 / 2027-10-25 | Did not load (binary/garbled response); registered 2 days ago |
| gloamingco.com | registered | 2022-09-01 / 2027-09-01 | Did not load |
| gloamingcoffee.com | registered | 2026-05-11 / 2028-05-11 | Did not load; two-year registration, owner unknown |
| gloamingpouches.com, trygloaming.com | NOT registered (404) | | |
Source: https://rdap.verisign.com/com/v1/domain/gloaming.com (same pattern for each).

**Search collisions** (WebSearch 2026-10-27: "Gloaming caffeine pouches", "Gloaming coffee OR energy drink OR supplement OR sleep brand", "Gloaming nicotine OR vape OR tobacco", `"Gloaming" brand drink OR tea OR beer OR gin company`)
- One alcohol item: "The Gloaming" imperial rye wine by Solaris Beer & Blending on Untappd. — [Untappd](https://untappd.com/b/solaris-beer-and-blending-the-gloaming/6200492)
- No Gloaming brand found in caffeine, energy, supplement, coffee, sleep, nicotine or vape. The nicotine query returned only unrelated "glo" heated-tobacco pages. Weak evidence.
- General knowledge, not source-checked here: "The Gloaming" is also the name of a music group and a Scottish/Irish literary term, UNVERIFIED.

**Meaning**
- Wiktionary: noun "twilight, as at early morning or (especially) early evening; dusk"; also present participle of "gloam". — [Wiktionary](https://en.wiktionary.org/wiki/gloaming)
- Urban Dictionary (10 entries, all 0 thumbs): twilight, from the musical Brigadoon; one crude sexual entry (glow-stick act); other entries are jokes (gloating plus beaming; "gloomy" adverb). — [UD API](https://api.urbandictionary.com/v0/define?term=gloaming)
- Other languages: not found / not checked.

**Handles (2026-10-27)**
- YouTube @gloaming: 404; @getgloaming, @gloamingco: 404. TikTok @gloaming exists (0 followers, statusCode 10222, UNVERIFIED meaning); @getgloaming, @gloamingco not found. Instagram, Facebook, X: not checked.

### Inferences
- GLOAM (smokeless tobacco) plus GLOAMING (nicotine-free pouch) is the single most important question for counsel: same pouch format, one letter group apart, and our brand rules say it must not read as nicotine.
- The fresh get/co/coffee domains suggest others are exploring the word, UNVERIFIED.

### Gaps
- Trademarkia, WIPO, state registers, Instagram/Facebook/X, domain owners, whether gloaming.com is for sale.

### Fit (one paragraph)
GLOAMING is the most evocative of the night: dusk, soft, adult, slightly literary. Night-shift implication: strong, since it is the hour before the shift. It is easy to remember and does not name any effect. Nicotine look-alike risk comes from the neighbouring GLOAM smokeless tobacco mark, not from the sound. Youth appeal: low, though fantasy-leaning readers may like it (UNVERIFIED). Implied-claim risk: low from the word; "gloam" is close to "gloom" and "glow", so avoid any "glow" or mood wording in copy. The crude UD entry is low-evidence.

---

## NORTHFALL (deep screen)

### Takeaway
Zero USPTO hits for NORTHFALL and the obvious phonetic variants, and no brand found in web search, but the word carries almost no night-shift meaning and northfall.com belongs to a domain-investment firm. Bare handles are taken on YouTube and TikTok.

### Cited Findings
**Trademark**
- `*northfall*`, `northfal*`, `norfall*`: 0 hits each on the USPTO backend. — [USPTO backend](https://tmsearch.uspto.gov/)
- Not searched: NORTH FALL as two words, NORTHFALLS, other spellings (Trademarkia, WIPO, state registers not checked).

**Domains (RDAP, 2026-10-27)**
| Domain | State | Created / expires | Content |
|---|---|---|---|
| northfall.com | registered | 2006-09-01 / 2027-09-01 | Heavy Lifting LLC, "private investment company focused on digital assets ... 100% UDRP Defense Success Rate". Page does not list a price. A domain holder: expect an offer-based price, UNVERIFIED. — [site](https://northfall.com) |
| getnorthfall.com, northfallco.com, trynorthfall.com, northfallcoffee.com, northfallpouches.com | NOT registered (404) | | |
Source: https://rdap.verisign.com/com/v1/domain/northfall.com

**Search collisions** (WebSearch "Northfall caffeine OR energy OR coffee OR supplement OR nicotine", 2026-10-27)
- Nothing named Northfall found in caffeine, energy, supplement, coffee, nicotine or vape. Results were generic caffeine-pouch and nicotine-pouch pages. Weak evidence.

**Meaning**
- Wiktionary: not found. — [Wiktionary](https://en.wiktionary.org/wiki/northfall)
- Urban Dictionary: 10 entries, all 0 thumbs; mostly a school (Northville/Northfall prep school), two crude entries ("a massive hole" and a slur-laden school description). — [UD API](https://api.urbandictionary.com/v0/define?term=northfall)
- A school-name association is likely in the US; other languages: not checked.

**Handles (2026-10-27)**
- YouTube @northfall EXISTS (HTTP 200, not inspected); @getnorthfall, @northfallco: 404. TikTok @northfall exists (35 followers, statusCode 0); @getnorthfall, @northfallco not found. Instagram, Facebook, X: not checked.

### Inferences
- The empty register is the main advantage, and may only reflect that the word is invented and rarely used.
- "Fall" in the name can be misread as "falling asleep"; the compass word gives no night meaning on its own.

### Gaps
- Trademarkia, WIPO, state registers, other spellings, Instagram/Facebook/X, price of northfall.com, any game/fantasy brand using Northfall (web search too weak to rule out).

### Fit (one paragraph)
NORTHFALL is calm, sparse and adult, with a cold-north feel, and it avoids every banned benefit word. Night-shift implication: none to weak, so it would need packaging and copy to carry the night link (and any such copy must avoid sleep or alertness claims). Nicotine look-alike risk: low. Youth appeal: low-to-moderate, since the word reads like a fantasy-game place name (UNVERIFIED). Dose transparency is neutral. Implied-claim risk: none from the word, with the "fall" ambiguity noted.

---

## GIBBOUS (deep screen)

### Takeaway
No live or pending GIBBOUS mark in the target classes, but a live moon-phase iPhone app named Gibbous owns getgibbous.com, the word is a consulting firm's .com, and Urban Dictionary has crude and drug-slang meanings. Weak fit and awkward sound.

### Cited Findings
**Trademark**
- `gibbous*`: 3 hits total, all read. CAMP GIBBOUS EST. 2017, Sickle Cell Disease Foundation, 88904166, Class 41, live; GIBBOUS NIMBUS, Fundamatter Products Pte Ltd, 90231890, Class 20 shelves, live; THE GIBBOUS MOON, Daniel G. Marcus, 88185817, Class 9, cancelled. None in target classes. — [USPTO backend](https://tmsearch.uspto.gov/)
- `gibb*` 285 hits read: GIBBLE'S (Class 29/30 chips, Pennsylvania) is live and a different word. `gibous*` 0 hits.

**Domains (RDAP, 2026-10-27)**
- gibbous.com: registered 2001-08-28, expires 2035-08-28; "Gibbous LLC 2026", a strategy and operations consulting firm. — [site](https://gibbous.com)
- getgibbous.com: registered 2026-07-01; page title "Gibbous: Moon Phase & Widget", an iPhone/iPad/Apple Watch app showing moon phase, moonrise and full-moon alerts. — [site](https://getgibbous.com)
- gibbousco.com, gibbouspouches.com, trygibbous.com, gibbouscoffee.com: NOT registered (404).

**Search collisions**: WebSearch "Gibbous caffeine OR energy OR supplement OR coffee brand" returned no Gibbous brand (results were Wip, Starbucks BAYA, etc.). Weak evidence. The moon-phase app above is the one live use found.

**Meaning**
- Wiktionary: not found via the API (the word is standard English: more than half lit, as a moon). Urban Dictionary: 10 entries, 0 thumbs; the first is a crude sexual one (penis state); others: moon phase, "high on weed" euphemism, a Newcastle slang meaning cool/fun. — [UD API](https://api.urbandictionary.com/v0/define?term=gibbous)
- The standard English adjective also means humped or hunchbacked (general knowledge, not source-checked), UNVERIFIED.

**Handles**: YouTube @gibbous EXISTS (200); @getgibbous, @gibbousco 404. TikTok @gibbous exists (0 followers, statusCode 0); others not found. Instagram, Facebook, X: not checked.

### Inferences
- The slang entries (crude, weed) plus the "humped" sense are tone risks, and the moon app is a live same-word brand, albeit in a different field.

### Gaps
- Trademarkia, WIPO, state registers, app owner identity, Instagram/Facebook/X.

### Fit (one paragraph)
GIBBOUS carries a moon image but sounds harsh and technical, not calm. Night-shift implication: moderate (moon), though "more than half" has no meaning for a customer. Nicotine look-alike risk low; youth appeal low; implied-claim risk none. The slang and the app make it the weakest of the four.

---

## Ranked top 3 (for a trademark attorney to look at first)

1. **EVENFALL.** Cleanest target-class register of the names with a real night link; moderate night-shift implication; main questions are EVENFLOW (Class 30 coffee), the Class 24 EVENFALL bedding mark, and the unknown owners of getevenfall.com and tryevenfall.com. Handle @evenfall exists on YouTube and TikTok.
2. **NORTHFALL.** Zero USPTO hits, free modifier domains, but almost no night meaning and the exact .com is held by a domain investor. Choose this if a clean register matters more than the night link.
3. **GLOAMING.** Best night feel, but the live GLOAM (Class 34 smokeless tobacco) and GLOAMM (Class 30 coffee) marks, a domain registered two days ago, and a pouch product beside a tobacco-class neighbour make it the riskiest. Choose this only if counsel is comfortable with the GLOAM mark.

Dropped on search evidence: PERIGEE (PERIGEA energy shots), VESPER, NOCTURNE, SOLSTICE, MERIDIAN, CAPELLA, NEAP, SYZYGY. GIBBOUS ranked below the three.

### For a professional (trademark attorney)
- Full clearance search on EVENFALL first: EVENFLOW (Class 30 coffee), EVENFLO (Class 5 nursing pads), EVENFALL (Class 24 bedding), and the abandoned Class 32 beer filing.
- If GLOAMING stays: GLOAM (Class 34 smokeless tobacco, Shenzhen SKE) and GLOAMM (Class 30) likelihood of confusion, and whether a nicotine-class neighbour affects our "no nicotine look-alike" rule.
- Check that NORTHFALL has no unregistered or foreign use, and the price of northfall.com.
- Any tagline using time-of-day wording must be reviewed for implied sleep, alertness or shift-work claims, and for the 12 pouches = 300 mg labelling question in `CLAUDE.md`.

### Not done
- WIPO, state registers, OpenCorporates, Trademarkia counts, Instagram/Facebook/X, for-sale prices (Afternic/Sedo not queried in this pass), non-English slang.
