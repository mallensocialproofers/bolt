# Night-word brand names for a US adults-only 25 mg caffeine pouch (nurses on overnight work): candidate screen, deep screens, ranked top 3

Checked 2026-10-27. NOT a legal clearance. No name here is "clear" or "safe"; a trademark attorney must run a full search (similarity, translation, design marks, common law, state registers) before any name is adopted. Mirror or snippet data is marked UNVERIFIED. Nothing here is a health, alertness or sleep claim; the "night-shift read" is about what the NAME might imply to a reader, for counsel to judge.

## How the data was obtained

- **USPTO backend (primary source for record data):** `POST https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch` with an Elasticsearch-style wildcard on `wordmark`, as in `/home/user/bolt/research_notes/Bolt replacement brand name research/deep_screen_increment_scruple_caliper.md`. Undocumented; very recent filings may be missing; no design-code, translation or similar-meaning search. For the 15 quick-screen names I ran `word*` and `*word*` and read every hit (counts below). The script printed only live marks in classes 5, 29, 30, 31, 32, 34, 43 for the quick screen (class 35 was added back for the four deep screens).
- **Trademarkia (mirror, UNVERIFIED against USPTO):** `https://www.trademarkia.com/search/trademarks?query=<word>` fetched with curl and a browser User-Agent, every result page (`&page=N`) until empty. Row counts matched the USPTO backend for all deep-screened names.
- **Domains:** Verisign RDAP `https://rdap.verisign.com/com/v1/domain/<name>.com` (200 = registered, 404 = not registered). For-sale check: Afternic page via WebFetch (only midwatch.com returned a price; vespertine.com and gloaming.com Afternic pages returned 404, so "not listed on Afternic" only).
- **Web search collisions:** the search tool is weak for exact brand names and mostly returns generic caffeine-pouch pages (the same weakness as in the earlier note). Findings are mainly from direct fetches of the domains plus a few targeted searches. Absence of search hits is NOT evidence of absence.
- **Not checked / failed:** Instagram, Facebook, X (login walls), WIPO, state registers, Google result pages, Sedo/Atom/GoDaddy for-sale listings, Justia (403 in the earlier note).
- Date for all items: 2026-10-27.

## Candidate table (15 names, quick screen)

"Night-shift read" = how strongly the name by itself suggests overnight use (and so could be read as an alertness claim). Target-class = live/pending marks in classes 5, 29, 30, 31, 32, 34, 43 on the USPTO backend (`word*` and `*word*`, all hits read).

| # | Name | USPTO total hits (alive) | Live/pending marks in target classes (owner, goods) | .com | Night-shift read | Verdict |
|---|---|---|---|---|---|---|
| 1 | VESPER | 189 (81) | Many. VESPER, Pique Life Pte Ltd, 99407867, class 5 "herbal supplements ... botanical elixirs for relaxation" (final action mailed); AURORA & VESPER LLC 99832841 class 5 dietary supplements and drink mixes (suspended); VESPER Innvictis Crop Care 87168974 class 5; ROT FRONT 79102575 class 30 (coffee, tea, cocoa; matched on a translation, UNVERIFIED); VESPER TAVERN class 43 | taken (1996, Tucows) | low-moderate (evening) | Drop: live class 5 supplement marks in the same lane |
| 2 | NOCTURNE | 107 (43) | NOCTURNE, Guittard Chocolate, 85719961, class 30 chocolate (registered); VANTA NOCTURNE 99619705 class 30 coffee (notice of allowance); NOCTURNE class 43 bar; DELIVERANCE NOCTURNE class 34 cigars | taken (1997, to 2036) | moderate-high ("of the night") | Drop: food (coffee, chocolate) and tobacco-class marks |
| 3 | COMPLINE | 10 (4) | None in 5/29/30/31/32/34. COMPLINE, Fossil Records LLC, 86546747, classes 35, 41, 43 (retail store services; wine classes; restaurant services, wine bars); Compline LLC, 78791844 / 78791859 / 87099883, classes 36/35/41/42/9 (workers' compensation data) | taken, in use by Compline LLC (workers' comp site) | moderate (last prayer of the day) | Runner-up: class 43 hit; pronunciation near "compliance" (see below) |
| 4 | EVENSONG | 11 (3) | None in target classes. EVENSONG, Design for a Flying Machine Ltd, 99709246, class 33 wines (filed 2026-03-18, "withdrawn before publication" but flagged alive by the backend); EVENSONG Canyon Philip Dauber 99792515 class 24 bedding (notice of allowance); EVENSONG SPA class 44 | taken (Robert Reese, personal/organist-style site "Evensong.com") | low-moderate (evening service) | Runner-up: religious cue; getevensong.com, evensongco.com, tryevensong.com all registered in 2026 |
| 5 | EVENTIDE | 31 (14) | EVENTIDE BREWING / BREWING EVENTIDE, Eventide Brewing LLC, 87330020 / 87208617, class 32 beer; EVENTIDE OYSTER CO class 43; EVENTIDE (senior living non-profit) 99652776 / 88677437 classes 43/44 | taken (1994) | low-moderate | Drop: class 32 and 43 marks; senior-care cue = medical authority cue |
| 6 | GLOAMING | 5 (3) | None in 5/29/30/31/32/34/43 (see deep screen) | taken (1997, 007Names, parked) | low | Deep screen |
| 7 | LAMPLIGHT | 88 (27) for `lamplight*` | LAMPLIGHTER BREWING CO 86183653 / 86596282 class 32 beer; LAMPLIGHTER 73058610 class 34 pipe tobacco; LAMPLIGHTER 76547334 class 43 hotel/restaurant. (Mark "LAMPLIGHT" alone: none live in target classes in this pass.) | taken (2000, GoDaddy); getlamplight.com, lamplightco.com, trylamplight.com also taken | low | Drop: pipe tobacco and beer marks are one letter away; every common domain taken |
| 8 | NIGHTFALL | 79 (35) | NIGHTFALL, Captain + Stoker LLC, 98673870, class 30 coffee (registered); NIGHTFALL XR, Randy Birdsong, 99850939, class 5 nutritional supplements (non-final action); NIGHTFALL Seriously Delicious 99926447 class 30 candy (new filing); NIGHTFALL class 31 trees | taken | moderate-high | Drop: coffee and supplement marks |
| 9 | DUSK | 352 (173) | Many: DUSK RITUALS class 5 supplements (99833533); FROM DUSK TILL DAWN class 5 dietary supplements (97925567, Apollon Nutrition); DUSK cigars class 34 (87021059); DUSK cafe class 43 (99110030); VUSE DUSK GLOW class 34 e-cigs; others | taken (expires 2026-11-17, Abion AB) | low-moderate | Drop: crowded in supplements, cigars and e-cigarettes |
| 10 | VIGIL | 701 (218; 649 read) | VIGILANTE COFFEE COMPANY class 30 coffee; MIDNIGHT VIGILS BLEND class 30 coffee (Carmelite monks); VIGILANT / VIGILANTE marks in classes 5, 29, 30, 32, 34, 43 | taken | HIGH, and "vigil/vigilance" = alertness | Drop: implied alertness claim plus crowded register |
| 11 | NIGHTJAR | 5 (2) | NIGHTJAR, Nightjar Holdings LLC, 90804908, classes 25, 34, 35 (smoke accessories: herb grinders, cigarette filters, rolling papers) | taken | moderate | Drop: tobacco-accessory registration |
| 12 | MIDWATCH | 4 (0) | None; all four marks dead (see deep screen) | taken, for sale | HIGH | Deep screen |
| 13 | LAMPLIT | 3 (1) | None in target classes; LAMPLIT, Alldio USA, 97034094, class 11 lamps | taken (expires 2026-11-29); lamplitco.com registered today (2026-10-27, Porkbun); other variants free | low | Weak: descriptive adjective, class 11 lighting only; held back as spare |
| 14 | VESPERTINE | 5 (2) | None in target classes (see deep screen) | taken, for sale via a broker | low | Deep screen |
| 15 | SMALL HOURS (phrase) | 0 hits for `small hour*`, `*small hours*`, `*smallhours*` | none | smallhours.com taken (2006), getsmallhours.com, smallhoursco.com, trysmallhours.com, smallhourscoffee.com all taken | HIGH ("small hours" = 1 to 4 a.m.) | Drop: zero marks but domain family taken, and the name reads as an explicit overnight claim |

Names I considered and left out before searching, because they break the brief: SLEEP/REST/DREAM/WAKE/AWAKE words, NIGHT SHIFT (alertness read), MATINS (morning), VIGILIA words, WITCHING HOUR (sounds like a youth/novelty brand), TWILIGHT (famous media franchise, Class 5/30 clutter likely; not searched, UNVERIFIED).

Domain table for all 15 base names (RDAP 2026-10-27): vesper.com (1996, Tucows), nocturne.com (1997, Network Solutions), compline.com (1995, CSC), evensong.com (2003, Network Solutions), eventide.com (1994, Network Solutions), gloaming.com (1997, 007Names), lamplight.com (2000, GoDaddy), nightfall.com (1997, CSC), dusk.com (1998, Abion AB, expires 2026-11-17), vigil.com (2003, CSC), smallhours.com (2006, GoDaddy), nightjar.com (1998, GoDaddy), midwatch.com (2023-04-25, GoDaddy, Afternic nameservers), lamplit.com (2004, GoDaddy), vespertine.com (2003-10-05, NameCheap). All 15 are registered. Source pattern: https://rdap.verisign.com/com/v1/domain/vesper.com.

## Deep screens (best 4: GLOAMING, VESPERTINE, MIDWATCH, COMPLINE/EVENSONG considered, see why below)

I chose GLOAMING, VESPERTINE and MIDWATCH for deep screening because they have the cleanest target-class register, and added EVENSONG as the fourth (COMPLINE was dropped to runner-up because of its class 43 mark, its live owner of compline.com, and the compliance/complain sound-alike). Evensong's deep screen is shorter because the key facts are already in the table.

---

### 1. GLOAMING

**Takeaway:** No live or pending GLOAMING-type mark in classes 5, 29, 30, 31, 32, 34 or 43. The base .com is taken but the pouch and "try" domains are free. Meaning is twilight (dusk or dawn), which suits a calm, adult, shift-change feel without saying "night shift". Main watch-outs are a pending astrology-app mark, a perfume mark with "A GLOAMING NIGHT", and an unknown owner of gloaming.com.

**Trademark** (classes 5, 29, 30, 31, 32, 34, 35, 43)
- Trademarkia "gloaming": 5 results total, all 5 seen (1 page); "gloamin": 5, same set. Live: GLOAMING, Wenzhou Xiyun Textile Products Co., Ltd., 90099007, class 24 quilts, bed covers, bed linen (Registered); GLOAMING, Melissa Asher Morgan, 99872509, classes 9 and 42, astrology/tarot/spiritual-practice app (Pending, published for opposition; filed 2026-06-08); A GLOAMING NIGHT, Coty Beauty Germany GmbH, 79295565, classes 3 and 35, cosmetics, perfumery (Registered). — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=gloaming) (UNVERIFIED mirror)
- USPTO backend: `gloaming*` 5 total, `*gloaming*` 5 total, `gloamin*` 5, `gloming*` 2 (GLOMINGLE class 7, unrelated), `glowming*` 1 (GLOWMINGLE FIZZ class 24, unrelated); all returned and read. 3 alive (the three above). No live or pending mark in 5, 29, 30, 31, 32, 34, 35 or 43. — [USPTO search backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch), site https://tmsearch.uspto.gov/
- Results seen vs total: 5 of 5 on both sources. Phonetic variants run: gloamin, gloming. Not run: "glowming", "gloeming" on Trademarkia; WIPO; design marks; "GLOAMIN'" with apostrophe.

**Domains** (RDAP, 2026-10-27)

| Domain | Status | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| gloaming.com | registered | 1997-09-28 / 2030-09-27 | 007Names, Inc. | Nameservers NS1/NS2.007NAMES.NET; did not load for me (connection failed); no Afternic listing (Afternic URL 404). Owner and price unknown. |
| getgloaming.com | registered | 2026-10-25 / 2027-10-25 | Porkbun | Placeholder "A Brand New Domain!" (registered 2 days ago) |
| gloamingco.com | registered | 2022-09-01 / 2027-09-01 | Squarespace Domains II | did not load |
| gloamingpouches.com | NOT registered (404) | | | |
| trygloaming.com | NOT registered (404) | | | |
| gloamingcoffee.com | registered | 2026-05-11 / 2028-05-11 | NameCheap | did not load |

- Source: https://rdap.verisign.com/com/v1/domain/gloaming.com (same pattern per name).

**Search collisions** (WebSearch, 2026-10-27: "Gloaming caffeine/energy/pouches", "coffee/supplement/sleep drink", "nicotine/vape/tobacco", "brand beverage/tea/gin/candle")
- No caffeine, energy, supplement, coffee, sleep, nicotine or vape brand named Gloaming surfaced. Searches returned only generic caffeine-pouch and sleep-coffee pages (weak evidence). Someone registered gloamingcoffee.com in May 2026 and getgloaming.com two days ago; use unknown.

**Meaning / slang**
- English: twilight, early morning or especially early evening; dusk. From Old English glōmung (twilight), related to "glow". — [Wiktionary](https://en.wiktionary.org/wiki/gloaming)
- Urban Dictionary (thumbs counts returned 0, prevalence unknown): twilight (Brigadoon song); a crude sexual act (one entry); "gloating and beaming"; "gloomy" adverb; "good, brilliant". — [UD API](https://api.urbandictionary.com/v0/define?term=gloaming)
- Other languages: no dictionary check beyond Wiktionary; it is an English/Scots poetic word. Slang in other languages: not found / not checked.

**Handles**
- YouTube @gloaming: 404; @gloamingco: 404; @getgloaming: 404. TikTok @gloaming: statusCode 10222 with followerCount 0 (an account appears to exist, restricted or private, UNVERIFIED meaning of code); @gloamingco, @getgloaming: 10221 (not found). Instagram/Facebook/X: NOT CHECKED.

**Night-shift read:** LOW-to-MODERATE. It names the light between day and night (and Wiktionary lists early morning too), so it fits a shift change without saying "night shift" or "alert". Nothing in the word implies energy or wakefulness.

**Fit:** Adult and calm: an old poetic word, no youth hook, nothing candy or slang. Dose-transparent: easy to print "25 mg caffeine per pouch" under it. Nicotine look-alike risk is low (soft G-L, no hard consonant stops, two syllables). Implied-claim risk is low; copy must not slide into "carry you through the dark" or similar. Pronunciation is clear (GLOH-ming). Risks: a pending astrology/tarot app mark (different field, but "spiritual" overlap with a night-time brand story, counsel to judge), Coty's "A GLOAMING NIGHT" perfume mark, an unknown owner of gloaming.com, and the Scots/poetic word may feel precious to some buyers.

---

### 2. VESPERTINE

**Takeaway:** Cleanest register of the four: only a class 25 belt/scarf mark and a class 35/42 marketing-agency mark are live, nothing in 5/29/30/31/32/34/43; every pouch/co/get/try/coffee domain variant is free. But vespertine.com is a broker-held asset (price unknown), and a famous two-Michelin-star Culver City restaurant called Vespertine exists (unregistered use in food), plus the final syllable can be heard as "teen".

**Trademark**
- Trademarkia "vespertine": 5 results total, all 5 seen. Live: VESPERTINE, Sarah Canner, 85459463, class 25 belts, sashes, scarves, vests (Registered); VESPERTINE AGENCY, Jason Hall, 97155340, classes 35 and 42, advertising and brand consulting (Registered). Others dead. — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=vespertine) (UNVERIFIED mirror)
- USPTO backend: `vespertine*` 5, `*vespertine*` 5, `vespertin*` 7 total (adds VESPERTINO, Northstar Brands LLC, 86768902, class 33 distilled spirits, Section 8 & 15 accepted), `vesperteen*` 0. All read. No live or pending mark in 5, 29, 30, 31, 32, 34, 43. — [USPTO search backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)
- Neighbour: the shorter VESPER has live class 5 supplement marks (Pique Life 99407867 "botanical elixirs for relaxation"; Aurora & Vesper LLC 99832841 supplements and drink mixes) and a class 30 ROT FRONT mark that matched it; an examiner or opposer might treat VESPERTINE as close to VESPER. For counsel.
- Results seen vs total: 5 of 5, 5 of 5, 7 of 7.

**Domains** (RDAP, 2026-10-27)

| Domain | Status | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| vespertine.com | registered | 2003-10-05 / 2027-10-05 | NameCheap | Nameservers SAWSELLS.COM; the site redirects (HTTP 303) to saw.com/upgrade, a domain-sales service; price not visible (saw.com page returned 403 to my fetch). No Afternic listing (404). |
| getvespertine.com | NOT registered (404) | | | |
| vespertineco.com | NOT registered (404) | | | |
| vespertinepouches.com | NOT registered (404) | | | |
| tryvespertine.com | NOT registered (404) | | | |
| vespertinecoffee.com | NOT registered (404) | | | |

**Search collisions**
- Vespertine (restaurant), Culver City, chef Jordan Kahn, opened 2017, two Michelin stars, closed March 2020, reopened April 2024; a sensory tasting-menu restaurant. Wikipedia, press. — [Wikipedia](https://en.wikipedia.org/wiki/Vespertine_(restaurant)), [Hollywood Reporter](https://www.hollywoodreporter.com/lifestyle/lifestyle-news/vespertine-restaurant-reopens-los-angeles-1235858446/). No USPTO class 43 VESPERTINE registration appeared, so any restaurant rights would be common-law (counsel to judge).
- A Björk album named Vespertine exists (general knowledge, not sourced here, UNVERIFIED); Urban Dictionary mentions an album entry.
- No caffeine, energy, supplement, coffee, sleep, nicotine or vape brand named Vespertine found via search (weak search; results were generic).

**Meaning / slang**
- English adjective, poetic: of or related to the evening; (zoology) active at dusk; (botany) opening in the evening. From Latin vespertīnus. — [Wiktionary](https://en.wiktionary.org/wiki/vespertine)
- Urban Dictionary: botany sense; a late-afternoon meal; an album; one crude entry ("nipple"); a TikTok-user insult. Thumbs counts 0. — [UD API](https://api.urbandictionary.com/v0/define?term=vespertine)
- Other languages: related Romance forms (Spanish/Portuguese/Italian "vespertino") are not verified here (Wiktionary lookup returned nothing for me); not found / not checked.

**Handles**
- YouTube @vespertine: EXISTS (200). @vespertineco, @getvespertine: 404. TikTok @vespertine: EXISTS (statusCode 0, followerCount 2017); @vespertineco: EXISTS (18 followers); @getvespertine: not found. Instagram/Facebook/X: NOT CHECKED. The base handle is taken on two platforms, so a modifier handle would be needed.

**Night-shift read:** MODERATE-LOW. Evening/dusk, not specifically overnight, so it does not claim wakefulness. It reads as upscale and nocturnal-botanical.

**Fit:** Adult, calm and premium; nothing about candy or slang; low nicotine look-alike risk (soft sibilants, four syllables). Dose transparency is easy. Risks: two pronunciations (VES-per-teen vs VES-per-tine), and the "teen" sound can look unfortunate on an adults-only product, to be tested with a pronunciation panel; length (four syllables); a famous restaurant of the same name; the broker-held .com. Implied-claim risk is low.

---

### 3. MIDWATCH

**Takeaway:** No live or pending MIDWATCH mark in any class (all four are dead). Best domain situation of the four for modifiers (get, co, pouches, try all free), and the strongest night-shift fit. But the name's pull is also its risk: "watch" suggests staying alert, a nautical midnight-to-4 a.m. watch word, and midwatchcoffee.com was registered in March 2026 with a "Launching Soon" page.

**Trademark**
- Trademarkia "midwatch": 4 results total, all 4 seen. All Dead: MIDWATCH, Tinder Box International, 73084780, class 34 smoking tobacco (cancelled, Section 8; 1983 registration); MIDWATCH BREWING CO. (Sabato, Cindy 97012842 and Sabato, George Edward 87825501), class 43 bar and taproom services featuring beer (both abandoned, no statement of use filed); MIDWATCH SECURITY LLC, 86642471, class 45 security guard services (cancelled; the 2026-08-28 date on Trademarkia). — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=midwatch) (UNVERIFIED mirror)
- USPTO backend: `midwatch*` 4, `*midwatch*` 4, `*midwatch` 4, `midwatc*` 4, `mid watch*` 0, `*midwach*` 0; all read; alive = 0. — [USPTO search backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)
- Results seen vs total: 4 of 4 on every query.
- Common-law: the Sabatos' "Midwatch Brewing Co." filings (2018, 2021) suggest a beer/taproom business may exist or have existed; I found only trademark records, no brewery site (search "Midwatch Brewing Co. brewery" returned only Justia owner pages). Whether it operates is UNVERIFIED. The expired tobacco and security marks do not prove nobody uses the name.

**Domains** (RDAP, 2026-10-27)

| Domain | Status | Created / expires | Registrar | What is there |
|---|---|---|---|---|
| midwatch.com | registered | 2023-04-25 / 2027-04-25 | GoDaddy | Afternic nameservers, parked; **Afternic listing "Buy now" $17,995 USD** or make an offer (WebFetch of https://www.afternic.com/domain/midwatch.com, read 2026-10-27) |
| getmidwatch.com | NOT registered (404) | | | |
| midwatchco.com | NOT registered (404) | | | |
| midwatchpouches.com | NOT registered (404) | | | |
| trymidwatch.com | NOT registered (404) | | | |
| midwatchcoffee.com | registered | 2026-03-26 / 2029-03-26 | GoDaddy | Live "Launching Soon" page with a contact and email sign-up form; owner not shown. A coffee-adjacent plan under the same name by an unknown party. |

**Search collisions**
- No caffeine, energy, pouch, supplement, sleep, nicotine or vape brand named Midwatch surfaced (three searches; generic results; weak evidence). Direct fetch found midwatchcoffee.com (above).

**Meaning / slang**
- English: (nautical) a watch kept from midnight until 4 a.m. — [Wiktionary](https://en.wiktionary.org/wiki/midwatch)
- Urban Dictionary: no entry (0 results). Other languages: not checked. "Mid" is also modern slang for "mediocre" (general knowledge, UNVERIFIED), which a young-skewing reader could hear in the first syllable.

**Handles**
- YouTube @midwatch: EXISTS (200); @midwatchco, @getmidwatch: 404. TikTok @midwatch: EXISTS (859 followers); @midwatchco, @getmidwatch: not found. Instagram/Facebook/X: NOT CHECKED.

**Night-shift read:** HIGH, and I say so plainly. "Midwatch" is literally the midnight-to-4 a.m. shift, which the nurse research flagged as a likely implied-alertness problem; "watch" also carries "stay vigilant". The owner may still choose it; counsel should judge whether the name alone implies a performance claim, and copy must never pair it with "stay sharp" style lines.

**Fit:** Calm, adult, no slang, no candy; no nicotine-pouch sound (soft M, two syllables, but the hard "-watch" ending is crisper than the others). Dose transparency: fits "25 mg per pouch, count your pouches" tone. Youth appeal: low (nautical/adult), apart from the "mid" slang echo. Risks: strongest implied-claim reading of the four; `.com` costs $17,995 or use a modifier; an unknown party holds midwatchcoffee.com; the 2021 brewery filings.

---

### 4. EVENSONG

**Takeaway:** No live mark in target classes; the register is quiet (a pending wine mark flagged alive despite "withdrawn", a bedding mark, a day spa). But four domain variants were registered in 2026, which hints at recent interest by others, and the word is an Anglican church service.

**Trademark**
- Trademarkia "evensong": 11 results total, all 11 seen (2 pages). Live/pending: EVENSONG, Design for a Flying Machine Limited, 99709246, class 33 wines (filed 2026-03-18; status "withdrawn before publication", yet flagged alive by the USPTO backend; treat as UNVERIFIED); EVENSONG, Canyon Philip Dauber, 99792515, class 24 bed sheets, quilts (notice of allowance, filed 2026-04-28); EVENSONG SPA, South Street Partners, 78880791, class 44 health spa services (Registered and renewed). — [Trademarkia](https://www.trademarkia.com/search/trademarks?query=evensong) (UNVERIFIED mirror)
- USPTO backend: `evensong*` 11, `*evensong*` 11, 3 alive; none in target classes. — [USPTO search backend](https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch)
- Results seen vs total: 11 of 11.

**Domains** (RDAP, 2026-10-27): evensong.com registered 2003-09-20 (Network Solutions), in use as a personal site for Robert Reese, with Evensong verse text on the page (https://evensong.com/); getevensong.com registered 2026-07-14 (GoDaddy); evensongco.com registered 2026-05-23 (Cloudflare); tryevensong.com registered 2026-03-18 (NameCheap); evensongpouches.com and evensongcoffee.com NOT registered (404). None of the registered modifiers loaded content for me except evensong.com.

**Search collisions:** not searched individually beyond the quick screen (generic results only). **Meaning:** an Anglican/Episcopal evening service, also a name for vespers; from Old English ǣfensang. — [Wiktionary](https://en.wiktionary.org/wiki/evensong). Urban Dictionary entries are personal-name and crude/cheater-tag entries (4 entries, thumbs 0) — [UD API](https://api.urbandictionary.com/v0/define?term=evensong). **Handles:** not checked. **Night-shift read:** LOW-MODERATE (evening, not overnight). **Fit:** calm, adult, no slang; religious cue (counsel and marketing to decide if that is acceptable for a caffeine product; it may also read as "wellness/peace"); the 2026 domain registrations by others make modifiers scarce.

---

### Runner-up note: COMPLINE
Not deep-screened. Facts above: Fossil Records LLC holds a live COMPLINE registration (86546747) covering retail store services, wine education and restaurant services/wine bars (class 43); Compline LLC holds three live registrations and the in-use compline.com (workers' compensation data, https://compline.com/); getcompline.com was registered 2026-10-26 (Porkbun). Urban Dictionary entries include "completely fine" and "whines and complains" (thumbs 0). Phonetic risk: "COMP-lin" sounds like "compliance"/"complain". Variants complineco.com, complinepouches.com, trycompline.com, complinecoffee.com were not registered (404). Night-shift read: moderate (the last canonical hour before bed).

## Ranked top 3 (for sending to a trademark attorney)

1. **GLOAMING.** Nothing live in classes 5/29/30/31/32/34/43; softest, most adult, lowest implied-claim risk; the "twilight" meaning covers both dusk and dawn and so suits shift change. Open: pouch and try domains; blockers to check: who owns gloaming.com, the pending astrology-app mark, Coty's "A GLOAMING NIGHT". Night-shift read: low-moderate.
2. **VESPERTINE.** Quietest register and every modifier domain free, premium evening feel. Cautions: the famous Culver City restaurant of the same name (common-law), closeness to VESPER (live class 5 supplement marks), the "-teen" ending, base .com on a broker's list, base handles taken. Night-shift read: moderate-low.
3. **MIDWATCH.** No live mark anywhere and modifier domains free, and it is the clearest "night-shift" name for nurses. Ranked third because it carries the highest implied-alertness risk of the three, midwatchcoffee.com was registered in March 2026 by an unknown party, and midwatch.com is $17,995. If the owner wants the overnight-worker connection explicit, this is the one; if not, the first two are safer on the claims rule.

Runners-up: EVENSONG, COMPLINE. Dropped for same-lane marks: VESPER (class 5), NIGHTFALL (class 30 coffee, class 5), NOCTURNE (class 30), DUSK, VIGIL, EVENTIDE, LAMPLIGHT, NIGHTJAR.

## For a professional (trademark attorney, plus counsel on claims)
- Run full searches on GLOAMING, VESPERTINE and MIDWATCH: similarity (VESPER, GLOAMING/GLOMING, MIDWATCH), translation, design marks, common-law and state registers.
- Ask counsel whether the name MIDWATCH, standing alone, could be read as an implied alertness claim for a caffeine product, and whether a night-themed brand story for nurses is itself an implied performance claim.
- Check the common-law status of the Vespertine restaurant, Midwatch Brewing Co., the owner of midwatchcoffee.com, and the owner of gloaming.com.
- Review the "teen" pronunciation of VESPERTINE against the adults-only and no-minor-appeal rule.

## Gaps
- Instagram, Facebook, X handles; WIPO; state registers; Google exact-phrase searches; who owns gloaming.com, midwatchcoffee.com, getgloaming.com; vespertine.com price; whether Midwatch Brewing Co. operates; Romance-language meanings of "vespertino"; Urban Dictionary prevalence (thumbs counts returned 0).
- Quick-screen names (not deep-screened) have no web-collision or slang check beyond the register and domains.
- No search hit for a caffeine, nicotine or supplement brand under any of the four deep-screened names, but the search tool is weak for exact brand names, so this is "nothing found by these tools", not "nothing exists".
