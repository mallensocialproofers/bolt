# Deep screen: HASP, FERRULE, RIVET (caffeine pouch brand name shortlist)

NOT A LEGAL CLEARANCE. No name here is cleared or safe. All checks dated 2026-10-27 (today) unless stated. Trademarkia is a third-party mirror of USPTO data: every trademark line below is UNVERIFIED against USPTO. This pass finishes the page-1-only gap in `names_objects_materials.md`.

## Method and what failed
- Trademarkia (curl, all result pages; URL pattern `https://www.trademarkia.com/search/trademarks?query=<q>&page=<n>`): worked. Pages parsed by script; the class filter URL form was not found, so I filtered by class myself from the records.
- Justia (curl and WebFetch): HTTP 403. USPTO tmsearch.uspto.gov: returns a JavaScript shell only, no usable data. tsdr.uspto.gov: no connection. USPTO TSDR API (tsdrapi.uspto.gov): 401 (needs a key). WIPO Global Brand Database (branddb.wipo.int): JavaScript shell only. TMview: JavaScript shell only. OpenCorporates API: 401. So no second trademark source could be read directly. One WebSearch snippet quoted a Justia page for the Rivet Global filing (see RIVET), which is a snippet only (UNVERIFIED) and conflicts with Trademarkia on status.
- Google is not available; WebSearch (standard mode) returned mostly generic pages, so "no brand found" is weak evidence only.
- Instagram returned 429 for every handle (not checked). TikTok and Facebook returned generic or inconsistent pages (not checked). YouTube and X returned distinguishable results (see each section).
- Atom returned a Cloudflare challenge (403); Sedo returned 503; Dan redirected to Afternic. Afternic worked for two domains only.
- Class scope: I recorded live/pending marks in classes 5, 29, 30, 31, 32, 34, 35, 43 (and noted 33 for RIVET because Iron Hill Brewery holds RIVET there).

---

## 1. HASP

### Trademark
**Takeaway:** On Trademarkia, no live or pending HASP mark was seen in classes 5, 29, 30, 31, 32, 34 or 43. Only one live/pending exact HASP mark exists (Class 9/45 app). Everything else is dead or unrelated.

**Cited findings**
- Query "hasp": 16 results total, 16 seen (pages 1 and 2 of 2). Live exact marks: HASP, Travex LLC, serial 50017413, Live/Pending, filed 28 Jul 2026, Class 9 and 45, downloadable social networking apps. SECUR-HASP II, E. J. Brooks Company, serial 73594866, Live/Registered, Class 20 plastic security seals. The other 14 are Dead (Class 6, 7, 9, 42: Webster Engineering, SafeNet, MTI MicroFuel, Capintec, Aladdin Knowledge Systems, Lawman Armor, Pressure Technologies, Security Enhancement Systems, Micro-Integration). UNVERIFIED mirror. [Trademarkia hasp p1](https://www.trademarkia.com/search/trademarks?query=hasp&page=1), [p2](https://www.trademarkia.com/search/trademarks?query=hasp&page=2), checked 2026-10-27.
- Query "hasp*": 34 results total, 4 pages, all 4 fetched and parsed (34 records). Live marks beyond the above are compound or different words in unrelated classes: HASPORT (Class 12), HASPOOLS (Class 35 retail pool supplies, Live/Registered, Jeremy Hasbrouck, serial 98791910), HASPET (21), HASPEL x2 (25, clothing), HASPSSO (11), HASPLAY (28), HASPINH (21), HASPRONY (25, Live/Pending). One dead HASPIZZA (Class 30/43, Dead/Abandoned 24 Feb 2025). No class 5, 29, 31, 32, 34 hit. UNVERIFIED mirror. [Trademarkia hasp*](https://www.trademarkia.com/search/trademarks?query=hasp%2A&page=1) pages 1-4, checked 2026-10-27.
- Variants "haspe", "haspd", "hasps": 0 results each. UNVERIFIED mirror. e.g. [haspe](https://www.trademarkia.com/search/trademarks?query=haspe), checked 2026-10-27.
- The Travex HASP app: a WebSearch for the app/company found nothing, so the owner and use are unidentified. [search](https://www.g2.com/sellers/travex) (unrelated Travex AI travel result only), checked 2026-10-27.

**Inferences:** Class 9/45 HASP (Travex) is the closest live exact mark; it is a different field, but an attorney should judge whether an app owner objects to a consumer brand called HASP. Compound marks are far from caffeine goods.
**Gaps:** USPTO, Justia, WIPO and state registries could not be read. Common-law (unregistered) use not searchable here. Foreign marks not checked.

### Domains
**Takeaway:** hasp.com is registered since 1994 and is a Sedo parking page; no price seen. gethasp.com and hasplabs.com are registered and in use by others. haspco, hasppouches, haspcoffee, tryhasp are unregistered per RDAP.

**Cited findings** (RDAP: `https://rdap.verisign.com/com/v1/domain/<d>.com`, checked 2026-10-27)
- hasp.com: registered 1994-07-08, expires 2027-01-02, last changed 2025-12-28, nameservers NS1/NS2.DTNT.INFO. [RDAP](https://rdap.verisign.com/com/v1/domain/hasp.com). Fetching `http://hasp.com` returns a page whose script loads `sedoparking.com/frmpark/<host>/dtnt/park.js`, i.e. a Sedo parking page (HTTPS and www would not connect; WebFetch got 503). No price visible. Sedo details page returned 503, Afternic returned 404 for hasp.com, Atom was blocked. Price: not found.
- gethasp.com: registered 2026-04-13; site title "hasp · model 01 · spec sheet", a local secret broker for AI agents (software). [site](https://gethasp.com/).
- hasplabs.com: registered 2026-04-15; "HASP Labs", small-business web and app development. [site](https://hasplabs.com/).
- haspco.com, hasppouches.com, haspcoffee.com, tryhasp.com: RDAP 404 (not registered). Not confirmed by web fetch.

**Inferences:** Two newly registered gethasp.com and hasplabs.com (April 2026) show other parties already building brands on HASP in software; relevant to confusion and search clutter.
**Gaps:** hasp.com asking price/broker not found.

### Search collisions
**Takeaway:** No caffeine, pouch, energy, supplement, coffee, vape or nicotine brand called Hasp surfaced.

**Cited findings** (WebSearch standard mode, 2026-10-27; queries: hasp caffeine, hasp pouches, hasp energy drink, hasp supplement brand, hasp coffee, hasp vape, hasp nicotine)
- Results were generic (hardware hasps, a vending-machine "Cigarette Top Hasp Set", lock pouches, "Hap Coffee" Hong Kong, French supplement "HSP Recup"). No brand in food/drink/supplement/caffeine/nicotine/vape found. e.g. [Master Lock hasp page](https://masterlock.com/products/product/731), [Capital Vending cigarette-top hasp](https://www.capitalvending.com/national-vendors-cigarette-top-hasp-set).
- Software/tech uses seen: gethasp.com, hasplabs.com (above), plus the older HASP software-dongle trademarks (SafeNet, Aladdin; Dead) on Trademarkia.

**Gaps:** WebSearch is weak for exact brand lookups; absence is not evidence of absence. Retail/Amazon/Shopify not searched.

### Meaning / slang
**Takeaway:** Core meaning is a hinged clasp for a padlock. Urban Dictionary has one crude acronym entry. Not a known drug/nicotine/youth slang term from what I could source.

**Cited findings**
- Urban Dictionary: one visible definition, a vulgar acronym insult (about a hairy rear and a small penis), submitted 20 Feb 2008, 0 votes up/down; the page has a "Load more" link so further entries may exist and were not seen. [UD hasp](https://www.urbandictionary.com/define.php?term=hasp), 2026-10-27.
- Wiktionary: English noun = clasp fastened by padlock/pin, spindle for winding yarn, measure of linen thread, scarifier; no slang listed. Irish "hasp" = h-prothesized form of "asp". Swedish "hasp" = hasp/latch. [Wiktionary hasp](https://en.wiktionary.org/wiki/hasp), 2026-10-27.
- Translations of the English noun (not the string's meaning in those languages): Spanish aspa; French loquet; Italian fermaglio; Hindi कुंडी / सिटकिनी; Mandarin 搭扣. German, Portuguese, Arabic, Russian translations not listed on the page.
- Whether the string "hasp" means something in Spanish, French, German, Portuguese, Italian, Hindi, Mandarin, Arabic or Russian: not found beyond the above. Spanish "aspa" is a different word.

**Inferences:** English speakers may hear "hasp" near "gasp", "asp" or "hash"; my judgement, not sourced.

### Handles (2026-10-27)
**Cited findings** (HTTP status/title via curl)
- YouTube: @hasp exists (title "はすP - YouTube", a Japanese-named channel, unrelated); @gethasp, @haspco, @hasppouches: 404 (appear unregistered). [youtube.com/@hasp](https://www.youtube.com/@hasp).
- X: @hasp exists (page title "hasp (@hasp) / X"); @haspco exists ("john christie"); @gethasp, @haspouches, @hasppouches: "User Profile Not Found". [x.com/hasp](https://x.com/hasp).
- Instagram: 429 for all, not checked. TikTok: generic page, not checked. Facebook: generic/inconsistent, not checked.
- Note: "haspouches" in the raw probe was a typo for hasppouches; ignore it.

### Fit
HASP is a short, firm, one-syllable word that suggests closing a tin lid, which fits a calm, adult, small-dose pouch tin, and it is far from beverage or energy cliches (no lightning, no "boost"). It is blunt rather than warm, and it can be misheard as "gasp" or "hash", the latter an unhelpful drug association; the crude Urban Dictionary acronym is obscure but exists. Nicotine-pouch look-alike risk is moderate: nicotine pouch brands use short hard names (ZYN, VELO, on!) so a short hard word on a round tin sits in that visual neighbourhood, a risk driven more by packaging than name. Youth appeal is low (no cartoon, candy or slang cue). Implied-claim risk is low: it implies security/closure, not energy, performance or health. The main practical issues are the Travex HASP app mark, the lost .com, and software brands already using HASP.

---

## 2. FERRULE

### Trademark
**Takeaway:** No live or pending FERRULE mark in the food, supplement, tobacco or caffeine classes was seen. Two live exact FERRULE marks are in Class 16/35 and 37/42; one dead FERRULE Class 35 wholesale mark.

**Cited findings**
- Query "ferrule": 22 results total, 22 seen (3 pages). Live: FERRULE, Makers Cabinet Ltd, serial 90557076, Live/Registered 30 Aug 2022, Class 16 and 35 (paper, stationery boxes; Class 35 services not fully visible, truncated). FERRULE, Coldiron Technology Group LLC, serial 50070879, Live/Pending filed 25 Aug 2026, Class 37 and 42 IT support. FERRULE MATE, Seikoh Giken, Class 9. FERRULE BLASTER, Adam Abrams, Class 8 (hand tools). FERRULESDIRECT, Miromar LLC, Live/Pending, Class 8/9. Dead: Class 6, 10, 13, 15, 22, 28 (golf/archery/fishing), Class 2, plus FERRULE MASTER Tobek Class 35 wholesale of ferrules (Dead/Cancelled 2009) and CONTROLLED FERRULE DRIVE Hoke Class 35 (Dead/Abandoned). No class 5, 29, 30, 31, 32, 34, 43. UNVERIFIED mirror. [p1](https://www.trademarkia.com/search/trademarks?query=ferrule&page=1), [p2](https://www.trademarkia.com/search/trademarks?query=ferrule&page=2), [p3](https://www.trademarkia.com/search/trademarks?query=ferrule&page=3), 2026-10-27.
- Query "ferrule*": 13 results, page 1 of 2 seen (10); page 2 not fetched; it is a superset of the above plus compounds. 
- Variants "ferule", "ferrel", "ferul": 0 results each; "ferrules": 1 result (Class 8/9). UNVERIFIED. [ferule](https://www.trademarkia.com/search/trademarks?query=ferule), 2026-10-27.

**Inferences:** The Makers Cabinet Class 35 listing should be read in full by an attorney if the brand will sell online (Class 35 retail). The "ferule" spelling returned nothing, but the word is commonly misspelled, so misspelling risk matters.
**Gaps:** same unreachable sources as above; Class 35 detail for Makers Cabinet truncated.

### Domains
**Takeaway:** ferrule.com is a parked page ("may be for sale", no price); getferrule, tryferrule and ferrulelabs are registered in 2026 by others and in use; ferruleco, ferrulepouches, ferrulecoffee unregistered.

**Cited findings** (RDAP, 2026-10-27)
- ferrule.com: registered 2004-10-24, expires 2027-10-24, last changed 2026-10-10, nameservers AboveDomains. [RDAP](https://rdap.verisign.com/com/v1/domain/ferrule.com). WebFetch: parked page with text "This domain may be for sale"; no price or broker shown. [ferrule.com](https://ferrule.com), 2026-10-27. Atom/Sedo/Afternic prices not obtained.
- getferrule.com: registered 2026-06-24 (Cloudflare nameservers); site would not load through the proxy (not checked).
- tryferrule.com: registered 2026-08-25; site "Ferrule — a co-managed IT platform" (Ferrule trademark symbol shown). [site](https://tryferrule.com/).
- ferrulelabs.com: registered 2026-05-21; "Ferrule Labs", custom 3D-printed golf ferrules. [site](https://ferrulelabs.com/).
- ferruleco.com, ferrulepouches.com, ferrulecoffee.com: RDAP 404.

**Inferences:** Several 2026 registrations of get/try/labs variants suggest recent interest in FERRULE as a tech/software brand name (consistent with the Coldiron Class 37/42 filing, Aug 2026).

### Search collisions
**Takeaway:** No brand in caffeine, pouches, energy, supplement, coffee, vape or nicotine found; coffee results are espresso-machine brass ferrule parts.

**Cited findings** (WebSearch, 2026-10-27; queries: ferrule caffeine pouches, ferrule energy supplement brand, ferrule coffee, ferrule vape nicotine)
- Results: mobility-aid cane ferrules, rigging hardware, brass espresso machine ferrules ([Espresso Parts](https://www.espressoparts.com/products/6-mm-brass-ferrule)). No supplement/nicotine brand named Ferrule. Separate lookalike names (Feroglobin iron supplement, Ferrol) appeared.
- Software: Ferrule co-managed IT platform (tryferrule.com); golf: Ferrule Labs.

### Meaning / slang
**Cited findings**
- Urban Dictionary: three entries (umbrella tip; "especially sophisticated feral cat"; pencil eraser band), 0 votes each; "Load more" link not expanded. No drug, nicotine or sexual slang seen. [UD ferrule](https://www.urbandictionary.com/define.php?term=ferrule), 2026-10-27.
- Wiktionary: English only; metal collar/cap on a tool or stick, band holding parts; no slang. Translations: Spanish casquillo/virola/regatón/contera; French virole; German Zwinge/Hülse; Portuguese virola; Italian ghiera; Russian металлический ободок; Hindi, Mandarin, Arabic not listed. [Wiktionary ferrule](https://en.wiktionary.org/wiki/ferrule).
- Meaning of the string "ferrule" itself in other languages: not found.

**Inferences:** Italian "ferula"/Latin "ferula" (rod) is close to "ferule" (my knowledge, not sourced here): "ferule" is also an English word for a rod used to punish children, a possible negative association; UNVERIFIED, not looked up.

### Handles (2026-10-27)
- YouTube: @ferrule exists (title "Ian Bishop - YouTube"); @getferrule, @ferruleco, @ferrulepouches 404.
- X: @ferrule exists ("ferrule (@ferrule) / X"); @getferrule, @ferruleco, @ferrulepouches "User Profile Not Found".
- Instagram 429 (not checked); TikTok and Facebook not checked (generic/inconsistent pages). [x.com/ferrule](https://x.com/ferrule).

### Fit
FERRULE sounds crafted, tooled and metallic, which suits a tin and a quiet, adult, dose-conscious pouch brand, and it carries no energy or performance cue. The problems are spoken and written: people say FAIR-ul, FEH-rool, or "ferule", and spell it with one r, so word-of-mouth and search lose customers (the one-r spelling returned no trademark hits, leaving it open for a third party). It is longer and fussier than HASP. Nicotine-pouch look-alike risk is low from the name itself; youth appeal is low (though "ferule" the rod and the cat joke are minor oddities). Implied-claim risk is low. Practical issues: two live exact FERRULE marks in unrelated classes, active technology users of the name in 2026 (Coldiron IT filing, tryferrule.com), and a parked but unpriced ferrule.com.

---

## 3. RIVET

### Trademark
**Takeaway:** RIVET is blocked on the evidence seen. Rivet Global, Inc. has a Live/Pending application for RIVET that lists Class 30 coffee/tea beverages, Class 32 sport and energy drinks and Class 5 goods. This was the "unviewed" record the earlier pass flagged. A direct conflict for a caffeine pouch brand is plausible; an attorney must assess.

**Cited findings**
- Query "rivet": 265 results total, 265 seen (27 pages, all fetched and parsed). 84 are Live. Sidebar classes: Class 5 (2), Class 30 (1), Class 32 (1), Class 43 (1), Class 33 (7), Class 35 (29). UNVERIFIED mirror. [page 1](https://www.trademarkia.com/search/trademarks?query=rivet&page=1) to [page 27](https://www.trademarkia.com/search/trademarks?query=rivet&page=27), 2026-10-27.
- **RIVET, Rivet Global, Inc. (Boston, MA), serial 97690117, filed 23 Nov 2022, Live/Pending, latest status "SECOND EXTENSION - GRANTED" as of 03 Sep 2026, mark "not being used in commerce yet", attorney Muzamil A. Huq, Morrison & Foerster LLP.** Classes (Trademarkia detail page): 4 candles; 5 feminine sanitary napkins, hygiene pads, panty liners, tampons; 9 downloadable app; 30 "Non-alcoholic beverages, namely, cocoa-based beverages, herbal and non-herbal tea, coffee, tea, cocoa and espresso beverages, and beverages made with a base of coffee and espresso ..." (truncated); 32 "Soft drinks, namely, sport drinks and energy drinks; bottled water"; 35, 39 (delivery of goods; food delivery), 40, 42, 44, 45 (social-change and youth-led awareness websites). UNVERIFIED mirror. [detail page](https://www.trademarkia.com/rivet-97690117), 2026-10-27.
- Conflict between sources: a WebSearch snippet for the Justia page for the same serial described it as a new application "not yet assigned to an examiner"; Justia could not be fetched (403) so this is UNVERIFIED and likely a stale snapshot. [Justia](https://trademarks.justia.com/976/90/rivet-97690117.html) (snippet only).
- Other live RIVET marks in or near relevant classes: RIVET HOUSE, Socius Investments, Class 43 hotel/restaurant services, Live/Registered (serial 97284392); RIVET and RIVET HARD SELTZER, Iron Hill Brewery, Class 33 (hard seltzer, alcoholic beverages except beer; serials 88658882, 88658928, 90857608), Live/Registered; RIVET x2, Rivet Tax, Class 35/42, Live/Registered; RIVET, Rivet Aviation Management LLC x2, Class 35; RIVET and RIVET TRADE, DRW Innovations, Class 35/36; THE HIDDEN RIVET, Sweeney, Class 35 retail clothing x2; THE LEADING RIVET SOURCE, Goebel Fasteners, Class 8/35 x2; RIVET NUT USA, Benjamin Kurey, Class 35, Live/Pending; RIVET REVOLUTION LLC, Class 14/35. Also Delta Faucet (Class 11/21), Amazon Technologies (Class 11/20), and others in clothing, guitar and fastener classes. No Class 34 or 31 hit. Dead food-class marks: RIVET, Sinochem Agro, Class 5 pesticides (Dead 2015); RIVETS, Optimum Nutrition, Class 5 dietary supplement bars (Dead/Cancelled 2011). UNVERIFIED mirror.
- RIVETS (plural): 39 results, 4 pages all fetched. RIVETS, Soft Pretzel Franchise Systems, Class 30 soft pretzels, Live/Registered (serial 88112124). [rivets](https://www.trademarkia.com/search/trademarks?query=rivets&page=1), 2026-10-27.
- Variants: "rivit" 12 results, 2 pages fetched; one live: RIVIT, RIVIT S.R.L., Class 6/7 metal rivets. "rivett" 8 results, 1 page; one live, SHAWN RIVETT DESIGNS (Class 41/42). "revit" 18 results, 2 pages fetched: REVIT (stylized, speedometer) and REVIT, Steel Supplements, Inc., serial 98779827 and 98779845, Live/Pending 13 Oct 2026, Class 32, sports/energy drinks; REVIT-A-LITE, INCO Digestive, Class 5 animal feed supplements; REVIT, Forward Solutions, Class 35. UNVERIFIED mirror. [revit](https://www.trademarkia.com/search/trademarks?query=revit&page=1).

**Inferences:** Rivet Global's application names energy drinks and coffee beverages; a caffeine pouch is neither, but both are caffeine-delivery goods in adjacent consumer classes, so an examiner or the owner could cite or oppose. This is a question for a trademark attorney. REVIT (Steel Supplements, energy drink) differs in spelling and sound from RIVET, but is another caffeine-beverage-adjacent mark worth noting.
**Gaps:** Rivet Global's operating business, brand use and web presence not found by WebSearch. Class 30 goods text truncated. Whether the application is 1(b) intent-to-use is inferred from "not being used in commerce" and "extension granted"; not confirmed on USPTO.

### Domains
**Takeaway:** rivet.com is an active fastener business, not for sale. getrivet.com and tryrivet.com are on Afternic with asking prices. rivetcoffee.com is an existing coffee business. rivetpouches.com is unregistered per RDAP.

**Cited findings** (RDAP, 2026-10-27)
- rivet.com: registered 1995-11-17, expires 2026-11-16, last changed 2025-11-17. WebFetch: active site of Industrial Rivet & Fastener Company (RivetKing), Norwood NJ, selling rivets and tools. Not parked. [rivet.com](https://rivet.com) (a Cloudflare-style redirect page via curl; content via WebFetch).
- getrivet.com: registered 2020-01-24, Afternic nameservers; Afternic "Buy it now for $4,895.00" or make an offer. [Afternic](https://www.afternic.com/domain/getrivet.com), 2026-10-27.
- tryrivet.com: registered 2019-07-20, Afternic; "Buy it now for $2,795.00". [Afternic](https://www.afternic.com/domain/tryrivet.com), 2026-10-27.
- rivetcoffee.com: registered 2018-05-29; site "Rivet Coffee Bar & Roastery" (Indiana). [site](https://rivetcoffee.com/).
- rivetco.com: registered 2021-09-29; "Rivet Co.", a business/media/consulting company. [site](https://rivetco.com/).
- rivetlabs.com: registered 2008-10-11, expires 2027-10-11; site would not load (not checked).
- rivetpouches.com: RDAP 404.

### Search collisions
**Takeaway:** Direct collision in coffee: Rivet Coffee Bar & Roastery (Westfield and Zionsville, Indiana; ships nationally), plus other uses.

**Cited findings** (WebSearch, 2026-10-27; queries: rivet caffeine pouches, rivet energy drink, rivet supplement brand, rivet coffee brand, rivet vape nicotine pouch, Rivet Global period products)
- RIVET Coffee Bar and Roastery, Indiana, ships nationally and internationally per the article. [Towne Post](https://townepost.com/indiana/zionsvilleboonecounty/rivet-coffee-bar-and-roastery-brings-coffee-camaraderie/), [site](https://rivetcoffee.com/). No USPTO coffee registration seen on Trademarkia (the Class 30 hit is Rivet Global's pending application).
- Other: Rivet Roasters (Pierce, Nebraska) coffee shop; Riveted Coffee Drive Thru (Greenwood area); Copper Rivet Distillery's "Son of a Gun" coffee liqueur (UK); Louis Vuitton "Rivet" coffee spoons. [Norfolk Daily News](https://norfolkdailynews.com/news/how-to-make-the-perfect-cup-of-coffee/article_ecddfc62-d81a-11eb-982d-973d907ae2c5.html), [Cask Cartel](https://caskcartel.com/products/copper-rivet-son-of-a-gun-coffee-liqueur-500ml), [Louis Vuitton](https://uk.louisvuitton.com/eng-gb/products/rivet-set-of-6-coffee-spoons-nvprod5880107v/R95691).
- Energy drink: a 2011 hilobrow post describes "Rivet" as a concept energy drink (not on sale). [hilobrow](https://www.hilobrow.com/2011/02/01/riveted/). Supplement, nicotine pouch, vape: no Rivet brand found.
- Amazon "Rivet" home furniture brand (Class 11/20 live mark, Amazon Technologies).

### Meaning / slang
**Cited findings**
- Urban Dictionary: 7 visible entries, 0 votes each, plus a "Load more" link (others unseen): poor credit person; short for "rivethead" (industrial music fan); insult for a heavier woman; easily offended furry; crack in the sidewalk; frog-like person; compliment about a Ratchet and Clank character. No drug or nicotine slang seen; one derogatory body-shaming entry. [UD rivet](https://www.urbandictionary.com/define.php?term=rivet), 2026-10-27.
- Wiktionary: English noun fastener; verb "to fascinate/capture attention"; French "rivet" (m) = rivet; Catalan "rivet" = weather strip, edging, hints; Swedish "rivet" = definite form of "riv" (to tear/grate, from my knowledge not sourced); Latin verb form. Translations of the English noun: Spanish remache/roblón/rebite; French rivet; German Niet; Portuguese rebite; Italian rivetto; Mandarin 铆钉; Arabic برشام; Russian заклёпка; Hindi not listed. [Wiktionary rivet](https://en.wiktionary.org/wiki/rivet), 2026-10-27.
- Hindi meaning of the string: not found.

### Handles (2026-10-27)
- YouTube: @rivet and @rivetco exist; @getrivet, @rivetpouches 404.
- X: @rivet, @getrivet ("Chris Wellington"), @rivetco exist; @rivetpouches "User Profile Not Found".
- Instagram 429 (not checked); TikTok and Facebook not checked.

### Fit
RIVET has the best story of the three for a bolt-and-hardware visual language (a fastener that holds things firmly), and "riveting" is a friendly, accessible word. But it is the most crowded and the least ownable: 84 live marks, an active coffee roaster with the same name, a pending application that names coffee and energy drinks, a beverage alcohol owner, and rivet.com in use by a fastener company. The name has no inherent youth or sexual cue beyond the minor Urban Dictionary entries, and implied-claim risk is mild (riveted = "grips your attention" could be read as a stimulation claim, my judgement). Nicotine-pouch look-alike risk is low from the word alone.

---

## Ranking of the three (not a clearance)
1. **HASP**: fewest observed trademark conflicts in relevant classes (none in 5/29/30/31/32/34/43 across 16 exact plus 34 wildcard records, all seen); short, firm, tin-lid fit. Open items: Travex HASP app (Class 9/45, filed 28 Jul 2026), hasp.com parked at Sedo with no price, software uses (gethasp.com, hasplabs.com), "gasp/hash" mishearing, one crude Urban Dictionary acronym.
2. **FERRULE**: also no food/supplement class hit (22 of 22 seen), but weaker on spelling/pronunciation and more software activity in 2026 (Coldiron Class 37/42, tryferrule.com); ferrule.com is parked, "may be for sale", price not found.
3. **RIVET**: weakest on evidence. Rivet Global's pending RIVET application names Class 30 coffee beverages and Class 32 energy drinks (second extension granted 3 Sep 2026), Rivet Coffee Bar & Roastery already trades in coffee, and rivet.com is an active fastener business. Only worth pursuing if an attorney concludes the Rivet Global filing does not block pouches.

## For a professional
- Trademark attorney: ask for a full search (USPTO plus common law) on HASP and FERRULE, a read of Travex (HASP) and Makers Cabinet (FERRULE, Class 35), and a view on Rivet Global serial 97690117.
- Add one line to `work/decisions.md` if the owner picks a name: not done (the user restricted edits to this file).

## Remaining gaps
- Instagram, TikTok, Facebook handles unconfirmed for all names.
- Price for hasp.com and ferrule.com not found.
- USPTO and WIPO records could not be read directly; all marks are UNVERIFIED mirror data.
- Urban Dictionary "Load more" entries not seen; no foreign-language slang search beyond Wiktionary.
