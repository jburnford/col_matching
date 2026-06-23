# Runbook: ground the next 100 town-tail places

**Trigger (paste this after `/clear`):**
> Ground the next 100 town-tail places — follow docs/GROUNDING_NEXT_100.md

Self-contained. Working dir: `~/col_matching`. Grounds the next 100 highest-frequency
ungrounded place queries into the project cache via the Wikidata **MCP** server
(per the `place-disambig` skill). Resumable: each run skips everything already in
the cache, so just repeat until the pending list is empty.

## Context & rules (do not break these)
- Use **`mcp__wikidata__search_items`** ONLY for QIDs — never invent a QID. The REST
  API is banned for disambiguation (see global CLAUDE.md).
- **≤5 search calls in parallel per message** (the WikidataMCP rate cap). One batch
  of 5 per assistant turn.
- The endpoint is **intermittent**: if a search returns empty / "No matching items",
  retry with a shorter plain query (e.g. `Nassau`, not `Nassau Bahamas capital`).
- **Historical-entity rule**: prefer the colonial-era entity for our 1860s–1960s
  corpus — `British Ceylon Q918153`, `British rule in Burma Q2376315`,
  `Anglo-Egyptian Sudan Q541455`, `Transvaal Colony Q1187978`, `Cape Colony Q370736`.
  Use the modern QID only if no period entity exists; note it.
- **Old-World / colonial-capital default** for ambiguous names given corpus context
  (`Georgetown`→Guyana capital, `Kingston`→Jamaica). When a town's QID didn't surface,
  re-search plain and pick the city (not the district/diocese/parish).
- **Precision over recall**: if a query is a compound grouping (`Ken. and Uga.`,
  `S.S. and F.M.S.`) or a genuinely ambiguous initialism (`N.S.`, `C.A.`, `N.T.`),
  do NOT guess — record it `match_type:"ungrounded"`, qid null.

## Steps

### 1. Get the pending list — COUNT-PRIORITIZED (since batch 031)
```
cd ~/col_matching
python3 - <<'PY'
import json, subprocess
pend=[json.loads(l) for l in subprocess.run(["python3","kg_ground_mcp.py","pending","--n","1000000"],
    capture_output=True,text=True).stdout.splitlines()]
pend.sort(key=lambda r:-r['count'])           # highest-count first = concentrated value
open("/tmp/pending.jsonl","w").writelines(json.dumps(p,ensure_ascii=False)+"\n" for p in pend[:100])
print("remaining",len(pend),"| count>=2",sum(1 for p in pend if p['count']>=2))
PY
wc -l /tmp/pending.jsonl
```
Each line: `{query, count, context_resolved, variants:[...]}`. **Per the 2026-06-22
scope analysis, feed count-desc, NOT file order** — value is concentrated in the
count>=2 head (~1,700 entries = 2pp); the 5,000 count-1 singletons are diminishing
returns. Stop ~93% (ceiling is ~94% — ~30% of the tail is irreducible noise:
compounds/institutions/initialisms/OCR-frags). If 0 lines, grounding is complete.

### 2. Ground in batches of 5
For each batch of 5 queries, call `mcp__wikidata__search_items` 5× in ONE message.
Pick the best geographic candidate per the rules above (use
`mcp__wikidata__get_statements` only when you must verify a historical/ambiguous
pick). Append each decision as one JSON line to `/tmp/results.jsonl`:
```json
{"query":"<exact query from pending>","qid":"Q123","label":"...","country_qid":"Q.. or null","instance_of":["city"],"has_coords":true,"match_type":"mcp_verified"}
```
`match_type`: `mcp_verified` if you checked statements, else `mcp_unverified`;
`ungrounded` (qid null) for the skip cases. Keep `query` byte-for-byte identical to
the pending line — it's the join key.

### 3. Record into the cache (writes our schema, fans out to variants)
```
python3 kg_ground_mcp.py record --results /tmp/results.jsonl
```
Writes `make_row` rows to `data/kg/places_grounding.jsonl` (keyed by surface
`place`; one row per variant). Accepts JSONL or a JSON array.

### 4. Sanity-check + coverage
```
python3 - <<'PY'
import json,collections
rows=[json.loads(l) for l in open("data/kg/places_grounding.jsonl")]
print("cache rows",len(rows),"| with QID",sum(bool(r.get("qid")) for r in rows))
print(dict(collections.Counter(r.get("match_type") for r in rows)))
wl=[json.loads(l) for l in open("data/kg/places_worklist.grounding.jsonl") if not l.startswith("#")]
g={r["place"] for r in rows if r.get("qid")}
cov=sum(r["count"] for r in wl if any(v in g for v in [r["query"]]+[x[0] for x in r.get("variants",[])]))
tot=sum(r["count"] for r in wl); print(f"grounded mentions {cov}/{tot} ({100*cov/tot:.0f}%)")
PY
```

### 5. Save batch + commit (do NOT push unless asked)
Bump NNN to the next number (`ls data/kg/mcp_grounding_batch*`):
```
cp /tmp/results.jsonl data/kg/mcp_grounding_batchNNN.jsonl
git add -f data/kg/places_grounding.jsonl data/kg/mcp_grounding_batchNNN.jsonl
git commit -m "Ground town-tail places batch NNN via Wikidata MCP (place-disambig)"
```

## QID verification (run periodically, e.g. every ~5 batches)
`verify_place_qids.py` validates EVERY distinct QID in `places_grounding.jsonl` against live
Wikidata via batched SPARQL (read-only lookup of known QIDs — NOT REST disambiguation, so it's
allowed). It fetches instance-of (P31) + country + coords and classifies each QID:
- **OK** — has a P31 that is a subclass* of a geographic root (settlement/admin-entity/region/
  country/feature). **OK_COORDS** — no P31 but carries coordinates (under-typed real point).
- **NONPLACE** — resolves with a P31 but NONE geographic (event/ethnic-group/company/history-topic
  → likely wrong entity). Coords do NOT rescue these (events carry coords too).
- **STUB** — no P31, no coords (statement-less item / redirect / deleted → unverifiable).
```
python3 verify_place_qids.py            # -> report + flagged + summary
```
Outputs `qid_verification_report.jsonl` (all), `qid_verification_flagged.jsonl` (non-OK), and
keep a hand-written `qid_verification_adjudication.jsonl` (verdict per flag) + append fixes to
`qid_verification_corrections.jsonl`. **First full run (2026-06-23, 1,312 QIDs): 1,300 OK / 1
OK_COORDS / 10 flagged.** Fixed 2 real errors (Matang Q61082734 ethnic-group→ungrounded; Sonthal
Q132450366 stub→Santhal Pargana division Q7420152). Remaining flags adjudicated KEEP except
**Egypt Q2474428** ('Egyptian history under the British', a manifest QID) → FLAG_FOR_JIM. NOTE: a
few non-place QIDs (Egypt, Belize-settlement, Royal Niger Co) come from the **vetted manifest**, not
MCP — the verifier checks manifest groundings too; don't unilaterally rewrite manifest QIDs.
Lesson baked in: bare-name MCP picks with a thin/blank search line can land on stubs/wrong-type
items — verification catches them after the fact; for new picks prefer a get_statements check when
the search line has no description.

## State (update after each run)
- Branch: `kg-place-canonicalization` (not pushed).
- Latest: **batch 034 (count-prioritized, 300-entry) done — coverage 91.12% of 168,301 mentions**.
- **SCOPE DECISION 2026-06-22 (Jim approved "reuse pass + prioritized batches"):** After 30
  file-order batches, per-batch ROI collapsed (famous places like Baghdad/New Delhi still appearing
  only because file-order interleaves them with singletons). Analysis: 6,930 pending = 8,724 mentions
  (5.18%); 75% are count-1 singletons; hard ceiling ~94% (irreducible noise ~30%). Two levers applied:
  (1) **Reuse pass 01** — auto-grounded 166 zero-FP spelling/abbrev variants of already-grounded QIDs
  (script: fuzzy-match pending vs cache, EXACT-token tier only, drop bare-ambiguous provinces; +229
  mentions, no MCP calls). Files: `mcp_grounding_reuse_pass01.jsonl` + `reuse_pass01_candidates.jsonl`.
  ⚠️ the OK/REVIEW fuzzy tiers had directional-flip FPs (N.→S., E.→W.) — DO NOT auto-accept those;
  only EXACT-token punctuation/diacritic variants are safe. (2) **Count-prioritized batches** (031+):
  feed count-desc — grounds ~44/batch at count 2-3 (~2x the mention-value of file-order singletons).
  Plan: ~10-15 prioritized batches to ~93%, then stop (singletons = archive as known residual).
- Batch 001 done: 94 grounded / 6 skipped; coverage **80%** of 168,301 mentions.
- Batch 002 (Penang/Saint Vincent/Malaya … set) recovered from a stale `/tmp/results.jsonl`
  and saved to disk (was already in the cache, provenance file was missing).
- Batch 003 done: 89 grounded / 11 skipped (compounds + ambiguous initialisms:
  Union, North, Selangor and Pahang, Mauritius and Rodrigues, Kenya and Uganda,
  S. Sttlmts. and F.M.S., Malay States, E. Africa and Uganda Prots., N.R., T.W.I.,
  Kenya Uga. and T.T.); coverage now **83%** of 168,301 mentions.
- Batch 004 done: 91 grounded / 9 skipped (Commonwealth, Dominion, South, district A.,
  N.W. district, S.S. & F.M.S., Transvaal and O.R.C., France and Belgium,
  E. Africa and Uganda); coverage now **84%** of 168,301 mentions. `kach.`/`kachcheri`
  Ceylon entries grounded to their town (Kurunegala/Anuradhapura/Jaffna); B.C./N.C./Br.
  abbreviations resolved (British Central Africa, Niger Coast, British Bechuanaland).
- Batch 005 done: 76 grounded / 24 skipped; coverage now **85%** of 168,301 mentions.
  Count-22-and-below tail has a higher skip rate (more compounds like "Mal. and S'pore",
  "France and Italy"; ambiguous initialisms E.A.G.C./C.As./C.P./N.T./D.T.C.; OCR
  fragments Kong/Eng. Kong; military units W.A.F.F./Indian Army). More resolved abbrevs:
  S./N.P. Provs. Nigeria, Br. E. Africa→East Africa Protectorate, Trans-Jordan→Emirate,
  S. Cams.→Southern Cameroons, British West Indies, W./E. Aden Protectorate→Aden
  Protectorate parent. OCR variants folded: Coomassie→Kumasi, Kurnegalle→Kurunegala,
  Matura→Matara, Cape-town→Cape Town.
- Batch 006 done: 78 grounded / 22 skipped; coverage now **86%** of 168,301 mentions
  (count-14–17 tail). Skips: compounds (Kowloon and New Territories, St. Lucia and Tobago,
  St. Thomas and St. James); ambiguous initialisms (B.H., U.P., S.A.C., U.S. of S., M.E.,
  N.T. (South)); generic words (colony, dominion); ambiguous bare names (St. Joseph,
  Caroni county, Windward district, Leeward district, district B., Colo West, Barkly Asylum);
  no-clean-entity (Dandagamuwa, Kroh→Pengkalan Hulu typed as mukim). Resolved: "kach."
  Ceylon entries→towns (Batticaloa/Badulla/Ratnapura); compound colony Demerara-Essequibo
  Q5255160 grounded as ONE historical entity; S.P./S. Nigeria→Southern Nigeria Protectorate
  Q2062030; D.W.W.I.(OCR for D.W.I.)→Danish West Indies Q829655; "Sudan government"→
  Anglo-Egyptian Sudan Q541455; G. Coast Colony→Gold Coast Colony Q503623. OCR variants
  folded: Matelle→Matale, Trincomalie→Trincomalee, Rotumah→Rotuma, Mannár→Mannar.
  Ambiguous city-names resolved by colonial-corpus default: Worcester→Western Cape,
  Belfast→N. Ireland, Nelson→New Zealand, Black River→Jamaica.
- Batch 007 done: 66 grounded / 34 skipped; coverage holds at **86%** of 168,301 mentions
  (count-11–14 tail; lower per-item counts so coverage % barely moves). Big SA/Ceylon/Malaya
  town run grounded (Potchefstroom, Lichtenburg, Germiston, Winburg, Boshof, Britstown,
  Bredasdorp, Kokstad, Port Alfred/Nolloth, Pietersburg→Polokwane, Pietermaritzburg,
  Graham's Town→Makhanda; Kalutara/Matara/Puttalam/Harispattu "kach."/division; Batu Pahat,
  Johor stuff). Historical polities: Br. Somaliland Q662653, B.C.A. Protectorate Q2642989,
  Bechuanaland Protectorate Q747314 (Northern division→parent), Transvaal/Union of S.A.,
  Griqualand East, Thembuland, Matabeleland. Institutions grounded as place nodes:
  Hong Kong Observatory Q1537282 (=Royal Observatory HK), Elsenburg Agric. Institute.
  OCR/abbrev folds: Suakim→Suakin, Manaar→Mannar, D'Urban→Durban, B. Pahat→Batu Pahat,
  Simla→Shimla, N'Eliya→Nuwara Eliya, Piquetberg→Piketberg, Taipo→Tai Po. Continent "Africa"
  grounded to Q15 (consistent with Australasia). Skips: ambiguous initialisms (S.P., S., K.,
  D., H.O., C.R.O., K.A.R./B.E.F./E.A.V.R.O./S.S.C.S. military), compounds (Selangor and
  N. Sembilan, Egypt and Palestine, Tembuland and Transkei, K. and Irak, Penang and Prov.
  Wellesley), generics (interior, western/southern province, N. division, Admiralty, Baltic,
  Niger, district B), ambiguous bare names (Richmond, Barkly, Griqualand, St. Thomas, N. York,
  N. Frontier), institutions w/o clean QID (Nairobi prison, Inst. medical Resch. F.M.S.),
  no-entity (Ulu Kelantan, Krobo).
- Batch 008 done: 85 grounded / 15 skipped; coverage now **87%** of 168,301 mentions
  (count-10–11 tail). Heavy SA/Ceylon/Malaya/Guyana/Caribbean town run. Historical polities
  grounded: South African Republic Q550374 (S. African Repub./Republic), British Solomon
  Islands Q13410267 (Solomon Is./Br. Sol. Is.), South-West Africa Q953068 (S.W.A.), Southern/
  Northern Nigeria Protectorate, Federation of Nigeria Q5440850 (Fed. Nig.), Northern Territories
  of the Gold Coast Q1998749, Ellice Islands Q3593530, Dominion of Newfoundland Q38610 (Newfndl.),
  Orange Free State Province (O.F.S.), British Virgin Islands (Virgin Islds.), Cyrenaica.
  Colonial-name folds: Lourenço Marques→Maputo, Rangoon→Yangon, Nanking→Nanjing, Pietersburg
  →Polokwane, Province Wellesley→Seberang Perai. OCR/abbrev folds: Suakim already, Kurunégala/
  Ratnapoora/Kégalla/Kaigalle→Ceylon towns, Pr. Ed. Is.→PEI, S. Settlimts.→Straits Settlements
  Q376178, B. Padang→Batang Padang, P. Wellesley, Brun.→Brunei, Xmas I.→Christmas Island,
  Lon.→London, Havre→Le Havre. Institutions/jurisdictions as place nodes: England and Wales
  Q1156248, Greyville divn. of Durban Q131686477. Continent "Africa" already grounded prior batch.
  Skips: ambiguous initialisms/abbrevs (Man., C.S.A.R., Lake Victoria area), generic words
  (interior, eastern/western/southern province, board of education, defence headqrs., Nigerian
  secrt., Western system), compounds (Canada and W. Indies, Egypt and Pal.), ambiguous bare
  names (St. Michael's, Aro, Perak North), no-entity (Kikuyu Prov.), OCR fragment (igua).
  Two-Praso ambiguity resolved: Prahsue→Assin Praso Q20118773 (the historical Pra-river camp).
- Batch 009 done: 62 grounded / 38 skipped; coverage holds at **87%** of 168,301 mentions
  (count-9–10 tail; low per-item counts so % is flat). SA/Ceylon/Malaya/Caribbean town run
  (Standerton, Robertson, Benoni, Kuruman, Tulbagh, Eshowe, Dikoya, Kalutara←Caltura, Kinta
  District, Pasir Puteh, Sandakan, Corozal←Corosal, Abaco Islands). Renamed-town folds:
  Maritzburg→Pietermaritzburg Q185591, Joh'burg→Johannesburg, Somerset East→KwaNojoli Q1021900,
  Roberts Heights→Thaba Tshwane Q7708831, Negapatam→Nagapattinam, Winnebah→Winneba. Historical
  polities: British Kaffraria Q918121, British Central Africa Protectorate Q2642989 (B. C. Africa
  protectorate), Orange Free State Province Q1971200 (O.F.S.), Union of South Africa Q193619
  (S. Afr./Union S. Africa), British Windward Islands Q2660774 (Windward Is. (Grenada)), British
  Guiana Q918126 (Br. G.), Essequibo colony Q1368792, Griqualand West Q2547918 (Diamond Fields).
  Inns of Court grounded as place nodes: Middle Temple Q925942 (Mid. Tem.), Lincoln's Inn Q69482.
  Whitehall→road Q214820. Quebec→modern province Q176 (corpus is 1860s+, not the 1763 colony).
  Skips: ambiguous initialisms (I.O., G.W.R., N.P., W.P., K.L., U.F.O., N.W.R., E.P.), compounds
  (Carlsruhe and Darmstadt, Selangor and Negri Sembilan, Natal and Zululand, Chilaw and Puttalam,
  Lagos and S. Nigeria, N. and S. America, Basutoland Bech. protectorate and Swaz., T.R. and P.S.,
  W. E. Africa protectorate), generics (northern district, Colony, protectorate, home, Eastern
  Prov., fedl. government, N.W. prov., district "A"), institutions/military (I.C.T.A., Georgetown
  prison, H.M.S. "Worcester", R.A.F.), ambiguous bare names (St. George West, Portland), no-clean-
  entity (L. Islds., Dal, N. Russia, Klip River division, Karene District, Berbice judicial
  district, Cleveland Divn. of N. Riding). Reused cross-search QIDs without re-searching: Lincoln's
  Inn (from Middle Temple search), British Guiana (from Essequibo/Berbice searches).
- Batch 010 done: 62 grounded / 38 skipped; coverage now **88%** of 168,301 mentions
  (count-8–9 tail). Towns across SA/Ceylon/Malaya/Caribbean/Canada/Australia/NZ/UK/Germany:
  Standerton-style run incl. Ermelo, Graaff-Reinet, Mossel Bay, Riversdale, Verulam (Natal),
  Jaffna, Kayts, Galagedara, Nuwara Eliya (N. Eliya), Kuala Lumpur, Malacca, Kuala Langat
  (K. Langat), Lipis District, Batu Gajah (B. Gajah), Nibong Tebal (N. Tebal), Hulu Selangor
  (U. Selangor), Lagos, Saltpond, Calabar (Old Calabar), Degema, Twillingate, Vancouver,
  Brandon-style, S. Grafton (NSW), Adelaide, Dunedin, Buenos Aires, Mexico, Stuttgart, Dresden,
  Cheltenham, Bexhill, Camberley-style Surrey/Suffolk/Ayrshire counties. Colonial polities/regions:
  Sierra Leone Colony and Protectorate Q30059027 (S. Leone protectorate), Southern Cameroons
  Q1542471 (S. Cameroons), Federation of Malaya Q1479726 (F. of Mal.), Ashanti Region Q398417
  (Ashantee), United Provinces of Agra and Oudh Q2160037 (United Provs. India), Turks and Caicos
  Q18221 (Caicos Is.), Transkei Q466551 (Transkeian Territories), Pondoland Q14555010, Uva
  Province Q876293, Ra/Lomaiviti Fiji provinces, Turkana County, Waziristan/Tirah (NW frontier
  regions), Berbera (Somaliland), Mukalla (Hadhramaut/Aden), Lake Ngami (N'Gami). Inner Temple
  Q1233784 (Inner Tem.) as place node. Reused cross-search/prior-batch QIDs: Kurunegala (Kurunégalla/
  Kornegalle), Straits Settlements (S. Stlimts.), Johannesburg (Jo'burg), South African Republic
  (late S.A.R.), Newcastle Natal (Newcastle division), Diego Martin, Haifa, Hulu Selangor, Lomaiviti.
  Skips: ambiguous initialisms (N.T. (North), N. P., E. A. P., M.V.I., Cams., Win., Maid., rlwys.),
  compounds (Transvaal and O.F.S., F.M.S. and S. Sttlmts., Aden and Som.), military units (Fife
  Artillery Militia, Lovat Scouts Yeomanry, Nigerian marine), generics (district C, West district,
  S. district New Territories), ambiguous bare names (St. John, Alexandra, Toledo, Rhod.,
  S. Renfrew, S. Australian, Heidelberg [Transvaal vs W.Cape vs Germany]), no-clean-entity
  (Zoutpansberg = only mountain range Soutpansberg, not the district; gr. I, gr. B OCR fragments).
- Batch 011 done: 62 grounded / 38 skipped; coverage holds at **88%** of 168,301 mentions
  (count-7–8 tail; low per-item counts so % is flat). Towns SA/Ceylon/Malaya/Caribbean/Canada/
  Australia/NZ/UK/Middle East: Ixopo, Uniondale, Victoria West, Lydenburg, Boksburg, Senekal,
  Couva/Tacarigua/Toco (Trinidad), Montego Bay, Townsville, Norwich, Harwich, Bradford, Cranbrook
  (BC), Khartoum, Muscat, Tehran (Teheran), Hebron, Jaffa, Dar es Salaam, Benin City, Puttalam
  (Putlam), Kegalle (Kegalla kach.), Alor Setar (Alor Star). Historical polities/regions: United
  States of the Ionian Islands Q1063498 (Ionian Is.), Federation of South Arabia Q834486, Federated
  Malay States Q1400154, British Bechuanaland Q4530733 (distinct from Bechuanaland Protectorate),
  Griqualand East Q5157575, New Territories Q596660 (New Terrs./new terr.), Tokelau Q36823 (Union
  Group/Union Islands), Trinidad and Tobago Q754, Saint Catherine Parish Jamaica, Saint Vincent
  island Q379656, Pamplemousses District (Mauritius), Taranaki/Otago (NZ regions), Pilbara (Pilbarry,
  WA), Terengganu (Treng.), Rotuma. Rivers as geographic nodes: Demerara River Q1185369 (Demerara/
  Demerary), Mazaruni River Q1487312 (Massaruni). Langeberg→mountain range Q1734011. Institution as
  place node: National Museum of Colombo Q2033487 (Colombo museum). Downing-street→Downing Street
  Q192687. Key West→city Q485186. Reused prior-batch/cross-search QIDs: Newfoundland (Newfld./Newfd./
  Newf'dld.→Q38610), British Solomon Islands, Niger Coast Protectorate, Inanda, Kimberley (Kimberley
  Cape Colony), Durban (Durban division). Skips: military (U.D.F., Union defence forces, H.K.V.D.C.,
  Trinidad local forces), companies/events (Imperial Brit. East Africa Compy., Br. Empire Exhibn.,
  Alsagoff concession), initialisms (N.Y., C. Prov., C.A.D., C.O., F.A.P.), compounds (Berbice and
  distcts., Straits Settlements and F.M.S., Perak and Dindings, Quebec and Washington, Fiji and W.
  Pacific, Potchefstroom and Krugersdorp dists.), generics/ambiguous (Coast, E. Coast, America,
  Malay, West Africa, northern territory, same constituency, Devonport, Perak South, South Dorset,
  Egyptian government), OCR fragments/no-entity (N. tory, I, ma, Colo East, Trusan, Upper Tugela,
  Bruas, Mano Salija, Toro.).
- Batch 012 done: 63 grounded / 37 skipped; coverage holds at **88%** of 168,301 mentions
  (count-6–7 tail). World cities/counties: Westminster, Stafford, Leicester, Northumberland,
  Birkenhead, Leamington Spa, Barnet, Karlsruhe (Carlsruhe), Tokyo, Madrid, Russia, Spain, Panama,
  Sicily, Paphos (Papho), Grevena, Eastern Rumelia (Eastern Roumelia), Khartoum, Tehran, Hebron,
  Jaffa, Khyber Pass, Geelong, Port Darwin (→Darwin), Townsville-style; Canada: Fredericton,
  Placentia, Bonaventure, Kingston Ont., Manitoba, Harbour Main; SA: Vereeniging, Lydenburg-style,
  Onderstepoort, Griquatown (→Griekwastad), Glen Grey (→Lady Frere), Clanwilliam, Umlazi; Ceylon:
  Kalpitiya, Colombo (Colombo Kachcheri/district), Karunegala (→Kurunegala); Caribbean: Bermuda,
  Barbados, Montego Bay-style, Kingstown (St Vincent), Dieppe Bay Town, Tacarigua-style. Historical
  polities/regions: Orange River Colony Q1142179 (O.R.C.), Cape Colony Q370736 (Cape Col.), South
  African Republic Q550374 (S.A. Repub./South African Republic), United States of the Ionian Islands,
  British rule in Burma Q2376315 (Burmah), Eastern Rumelia, Assam Q1164, Ijebu Ode Q1023726 (Jebu),
  Yingkou Q75150 (Newchwang). Continents/big geo: North America Q49, Taiwan Q865 (Formosa), Lake
  Malawi Q5532 (Lake Nyasa), Rukwa Lake Q1143935, Demerara/Mazaruni rivers (prior). Reused QIDs:
  Straits Settlements (S. Sttlmnts./S. Sttlimts./Str. Settls.), Durban (D'Urban), Savanne District,
  Msinga (Umsinga division), Bedford, Quebec (P.Q.), Port Antonio, Australia (Australian
  Commonwealth), Otago. Skips: railways (Trinidad/Mal. rlwys.), military admin (O.E.T.A., Sandhurst,
  Victoria Inst., Zanzibar govt), initialisms (B.B. and S., V.Is., W.P., N.Cent.Prov., S.S.E.A.P.),
  compounds (N. Sembilan and Malacca, Point Pedro and Chavakachcheri, Wind. and Leeward Is., France
  Gallipoli Salonica and Egypt, Selangor Negri Sembilan and Pahang, Ashanti and N. Territories,
  Georgetown and East Bank Demerara), generics/regions (N./W. reg., West Africa settlements, Cent.
  Angoniland), ambiguous (Sutherland, Cross River [river vs state], Sydney House), no-clean-entity
  (Klip River/Lower Tugela divisions, Royal Alfred Observatory, Gopeng), OCR fragments (gr. A, Colo.
  E., d Coast, St. ia, anda, Kalu-, B/T., district D).
- Batch 013 done: 48 grounded / 52 skipped; coverage holds at **88%** of 168,301 mentions
  (count-6 tail; very low per-item counts so % is flat — skip rate rises here). World cities/
  regions grounded: Rio de Janeiro Q8678, Kabul Q5838, Folkestone Q375314, Wembley Q146858,
  Argentina Q414, Libya Q1016, Somerset Q23157 (English county), Victoria Australia Q36687,
  Australia Q408 (Commonwealth of Austr.), New Brunswick Q1965 (also N. Bruns.). SA towns:
  Heilbron, Hoopstad, Willowmore, Kuruman (Kuruman Br. Bech.), Nqamakwe (Ngamakwe), Bedford
  Eastern Cape Q813857 (Bedford division). Ceylon: Kandy Q203197 (Kandy Kachcheri), Dambulla
  Q377343 (Dambool), Chavakacheri Q1068504 (Chavagacherry). Malaya: Selangor Q189710 (Salangor),
  Hulu Selangor Q2741737 (Ulu Selangor extension), Kota Bharu Q651131 (Khota Bharu). W. Africa:
  Ibadan Q183298, Ada Foah Q345860 (Addah), Sekondi-Takoradi Q243293 (Secondee), Borgu Q893575,
  Bunyoro Q889897, Kampala Q3894, Freetown Q3780, Méko Q33391468 (Meko W. Prov.). Caribbean:
  Roseau Q36281, Saint Kitts island Q204989 (S. Kitts), Ragged Island Q1532634 (Bahamas).
  Historical polities/regions: Transvaal Province Q190959 (Transvaal Provl. division), Southern
  Nigeria Protectorate Q2062030 (Southern Provinces Nigeria, per batch 008), North-West Frontier
  Province Q4412467, Rajputana Q3929733, Cape Colony Q370736 (C. of G.H. = Cape of Good Hope),
  Tanganyika Territory Q158725, Western Samoa Trust Territory Q7988268 (W. Samoa, the 1920-62
  period entity), Quthing Q1003318 (Basutoland/Lesotho). Geo/institution as place nodes: Kalahari
  Desert Q47700, Royal Arsenal Q2170996 (Woolwich Arsenal), Horse Guards barracks Q492350, Flacq
  District Q911651 (district of Flacq). Reused: Straits Settlements Q376178 (S. Settments./S.
  Settlms.). Skips: compounds (S. and N. Rhodesia, Gold Coast and Lagos, Antigua and Montserrat,
  Dikoya and Amella, Ashanti and N. Territories, France and Gallipoli, Mannar and Mullaittivu,
  Bridgetown and St. Michael, Nadroga and Colo West, U.S.A. and Canada, Ken. Uga. and T.T.,
  F.M.S. & S.S., S.S. and F.M.S., Hatton-Nuwara Eliya), directional fragments (S./N. Kedah, S.
  Malacca, N. Australia), initialisms (D.P.W., O.S.O., Tob., Br. H., B. Pahang), institutions/
  events (admiralty, Cape H. of A. = Cape House of Assembly, Crown Agents, Imp. Confce., Tyne
  garrison, Inst. medical Research F.M.S.), generic/ambiguous (St. Mary, St. Andrew, Wodehouse,
  Northern district, S. district Grenada, district C./F., East Coast, St. George East, King's
  county, S. India, Colony and protectorate), no-clean-entity (West African Settlements / W.
  Africa Sttlmts. — no distinct WD entity surfaced; Lower Tugela & Ndwandwe divisions; Fingoland;
  Qua country; R. Honduras = Br. vs Republic ambiguity), OCR fragments (in addn., Apus, Midland
  conservancy).
- Batch 014 done: 54 grounded / 46 skipped; coverage holds at **88%** of 168,301 mentions
  (count-6 tail). World cities/countries: Rio-style — Lisbon Q597, Florence Q2044, Peru Q419,
  Lithuania Q37, Jerusalem Q1218 (Jerus.), Chongqing Q11725 (Chung King), Cádiz Q15682
  (Andalusia (Cadiz)), Buenos Aires Q1486 (Buenos Ayres/B. Aires), Kyrenia Q206760, Limassol
  Q185632 (Limasol), Meerut Q200237, Kadapa Q30651 (Cuddapah). Australia/NZ: Western Australia
  Q3206 (West Aust./West-Australia), Victoria-style York WA Q994000, Hobart Q40191 (Hobart Town),
  Port Adelaide Q3908652, Charters Towers Q1020266, Ipswich Qld Q1009253, Hāwera Q998452. SA
  towns: Bloemfontein Q37701, Johannesburg Q34647 (Jo'burg.), Rustenburg Q182049, Prieska
  Q1021731, Klerksdorp Q1015647, Amersfoort Mpumalanga Q2553018 (Amersfoort T'vaal), Simon's Town
  Q1013370, Witwatersrand Q587808 (district→mountain-range geo node). Malaya/Mauritius: Batu Pahat
  Q2891912 (B. Pahat Johore), Plaines Wilhems District Q1053595, Rivière du Rempart District
  Q1053565 (both accent variants). W. Africa: Ondo Q1853310, Axim Q792509, Sulima Q2006220
  (Sulymah), Keta Municipal District Q1432726 (Quittah), Muri Q11883435 (Muri prov.), Congo Free
  State Q76048. India/Cyprus/UK: Punjab former province Q2629708 (Punjaub), Guildford Q213465,
  Liskeard Q2019908, Toxteth Q1757189 (Toxteth division Liverpool), Brodsworth Q2553777, Barbados
  Q244 (Barbadoes). Caribbean/Pacific/Lesotho: Basseterre Q41295, Viti Levu Q208198 (Vitu Levu),
  Leribe District Q819987, New Hebrides Q752431 (New Heb.). Historical polities reused/grounded:
  Cape Colony Q370736 (colony of Cape of Good Hope), South African Republic Q550374 (S.A.
  Republic), Orange River Colony Q1142179 (O.R.C. admn.), Natal Province Q917867 (Natal (Union)),
  Assin Praso Q20118773 (Prahsu, reuse batch 008). Skips: ambiguous bare names (Windsor, Utrecht
  [NL city vs Natal town], Hamilton, Salisbury [England vs Rhodesia], Waterloo, Umgeni/Umgeni
  division [river search kept returning empty — defer], West Devon, Leeward), directional/region
  fragments (N. Queensland, N. Wales, Gold Coast S., S. Trin., east. district, Upper Sarawak,
  N. district Nehch.), initialisms (N. R., W.A.M.S., B.W.A., N.Z. H. of R., h.q. E.A. Cmd.),
  railways/admin/institutions (Cape government rlwys., Mal. rlw., Mal. P.W.S., Nigeria rlways.,
  Nigeria survey, Western System, open lines, magistracy, colonial, government house, Cape
  government, Sungei Buloh leper settlement, Shing Mun Valley scheme), compounds (Egypt and
  France, Maur. and Rodrigues, Windward and Leeward Is., Aden and Sheikh Othman), districts w/o
  clean entity (South Nyasa, Corentyne Coast judicial, Kaffrarian outpost, West Simcoe), no-entity
  (Uganda Kingdom [Buganda vs Protectorate ambiguity], Noniti country, East Indies, various
  dists.), OCR fragments (Balapeta-Modera).
- Batch 015 done: 56 grounded / 44 skipped; coverage now **89%** of 168,301 mentions
  (count-5–6 tail). World cities/countries: Damascus Q3766, Cuba Q241, Siberia Q5428, Lomé Q3792,
  Rhine Q584, Hawaii Q782, Great Britain Q23666, Mesopotamia Q11767 (Mespot.), Arabian Peninsula
  Q31945 (Arabia), İzmir Q35997 (Smyrna), Xiamen Q68744 (Amoy), Allahabad→Prayagraj Q162442,
  Meerut-style. Australia/NZ/Canada: Victoria BC Q2132, Onehunga Q3352699, Cook Islands Q26988,
  Kings County NB Q1670967, New Zealand Q664 (N Z.), Australia Q408 (Aust.), Quebec Q176 (Que.).
  SA towns: Bloemfontein-style — Kroonstad Q264014, Kenhardt Q3643099, Wepener Q841619, Fraserburg
  Q2609896, Stutterheim Q1021884, Qonce Q1016100 (King Williamstown), Du Toit's Pan Q5310079
  (Dutoitspan, Kimberley diamond mine). Ceylon: Colombo Q35381 (Colombo Kach./Columbo), Galle
  Q319366, Hambantota Q1025283, Kalpitiya Q14220105 (Kalpitya). Malaya: Pahang Q191346, Rembau
  Q2219158, Balik Pulau Q4850899, Port Klang Q11155122 (P. Swettenham = Port Swettenham). W./E.
  Africa & islands: Serowe Q855634, Ngamiland Q3339267, Mangochi Q1890257 (Fort Johnston), Macuata
  Q1365304 (Fiji), Savanne District Q1053600 (Mauritius), Salt Cay Q426843, Arima Q661405,
  Kingstown Q41474 (Kingstown district), Stanley Q12245 (Falklands). Caribbean/UK: Stockton-on-Tees
  Q989418, Waiapu River Q1764797. Historical polities (several reused): East Africa Protectorate
  Q876185 (Brit. E. Africa / B.E.A. / E.A. protectorate — all → same), German East Africa Q153963,
  British Somaliland Q662653 (Br. Som., reuse), Northern Nigeria Protectorate Q585408 (N. Prov.
  Nigeria), Southern Nigeria Protectorate Q2062030 (Southern Provs. Nigeria, reuse), Natal Province
  Q917867 (Natal prov. divn., reuse), Griqualand East Q5157575 (E. Griqualand, reuse), Malakand
  Agency Q1820054 (the colonial-era entity, not the modern district). Skips: compounds (Sarawak N.
  Borneo and Brunei, Antigua and St. Kitts, Sierra Leone and Gambia, N. and S. Nigeria, East Africa
  and Uganda Prots., F.M.S. and S.S.), military (R.A.M.C., N.Z.E.F., Home Forces, B. Guiana local
  forces/militia, E.A.T.R.O., engrg. headqrs.), institutions (Raffles Inst., St. John's savings
  bank, D.P.W. F.M.S., L.C.C., Union H. of A. / H. of A. = House of Assembly), generic/directional
  (Western Prov., Southern/central/east. division, district E/No. 1, U. Perak, S. Prov. Ashanti,
  N. Frontier district, S. Eastern Prov., Lagos Hinterland, Union government, Egyptian), ambiguous
  bare names (Bethlehem [Palestine vs Free State], Soufriere, Beaconsfield, Basse-terre [St Kitts vs
  Guadeloupe], Samaria [region vs city]), unresolved-by-search (North Toronto Ontario, Umgeni
  division — river search again empty, Kegalle [only Town-A/B GN divisions surface], Sadong [Sarawak
  river/district, no clean settlement]), OCR fragment (New brides, B.).
- Batch 016 done: 53 grounded / 47 skipped; coverage holds at **89%** of 168,301 mentions
  (count-5 tail). World cities/countries: Amsterdam Q727, Munich Q1726, Cardiff Q10690, Corfu
  Q121378, Canberra Q3114, Brazil Q155, Guadeloupe Q17012, Samaria Region Q124371650 (Samaria,
  Pal.). UK/London: Islington Q125163, South Kensington Q1045096, Preston Q184090, Dorset Q23159
  (reuse). Canada/Australia/NZ: Kamouraska Q1103923, Victoria BC Q2132, Cariboo Q2938768, New
  South Wales Q3224 (N.S.W.), Goulburn Q605235, Norfolk Island Q31057, Cocos (Keeling) Islands
  Q36004. SA towns: Caledon Q777884, Harrismith Q1586262, Mahlabatini Q6395826, Impendle Q10925601
  (Impendhle), Ulundi Q1013421, Lions River Q13035272 (Lions River division), Ndwedwe Local
  Municipality Q1717872 (Ndwedwe division), Bloemfontein Q37701 (Bloemfontein O.R.C., reuse).
  Ceylon/Malaya/Borneo/Fiji: Trincomalee Q323873, Kudat Q23041 (N. Borneo), Taveuni Q1138545
  (Taviuni), George Town Penang Q61092 (reuse). Caribbean/Pacific: St Ann's Bay Q630692, Portland
  Parish Q125148, Grenadines Q503482, Banaba Island Q271901 (Ocean Is.), Larnaca Q171882 (Larnaka),
  Bahamas Q778 (Bahamas census), Mbale City Q1015727. Historical polities (many reused): East
  Africa Protectorate Q876185 (Brit. E. Africa protectorate), British Central Africa Protectorate
  Q2642989 (both "Brit. Cen." and "Br. Central" spellings), Gilbert and Ellice Islands Q1050859
  (G. and E. Is.), British Leeward Islands Q1796551 (Leeward Island), Saint Kitts and Nevis Q763
  (St. Christopher and Nevis), Antigua and Barbuda Q781, Newfoundland Q38610 (Newfnd./New-foundland),
  Tokelau Q36823 (Union Is., reuse), Cape Province Q849164 (Cape prov. divn. — consistent with
  Natal prov. divn. last batch), Berbice Q675322 (cty. Berbice), Stellaland Q1269234 (Boer
  republic), Eswatini Q1050 (Swaziland adminstrn.), Ijebu Ode Q1023726 (Jebu Ode, reuse), Western
  Australia Q3206 (W. Australian, reuse). Skips: compounds (Cape and Union of S. Africa, St. James
  and Trelawny, Colo N. and E., Gallipoli and France), military/institutions (R.A.P., R.A.M.C.-
  style, St. Helena volrs, Belize pris., Scotland Yard, Br. Museum, Colonial and Indian Exhibition,
  Impl. confce., Basuto. M.P., English schls., official Gaz.), directional/generic provinces (W./E.
  Prov. Ashanti, E. Prov. S. Nigeria, N.C. Prov., N.W. Prov., Quebec E./West, Colo North, east
  province, Northern Border, Transkeian conservancy, W. Coast of Africa, South Malacca again),
  ambiguous bare names (St. Louis, Trinity, St. George's, Santa Cruz, Maitland, Longford, Alfred /
  Alfred co., Vincent), districts/letters (district "A."/"C", St., P. W., Cols.), search-resistant
  (Vergenoegen, Stockenstrom, Inanda division, prov. of Zululand [only modern district / wrong-era
  bantustan surface], Plaisance, Panvila, Muka OCR).
- Batch 017 done: 58 grounded / 42 skipped; coverage holds at **89%** of 168,301 mentions
  (count-5 tail). World cities/towns: Toowoomba Q478302, Albury Q331764 (NSW), Yucatán
  Q60176, Basra Q48195, Peshawar Q1113311, Bath Q22889 (Somerset, Old-World default),
  Leominster Q550424, Worcestershire Q23135, Wakefield Q216638, Cheam Q2240615 (Sutton),
  Antananarivo Q3915, Réunion Q17070, Alderney Q179313, New Westminster Q876122 (BC),
  Ferryland Q927864 (both Newfndld./Newfndl. spellings). W. Africa: Dixcove Q1231673,
  Abeokuta Q206484, Sokoto Q336350, Asaba Q1061665, Umuahia Q203301, Benin City Q320704
  (bare "Benin"), Zaria Q147975, Akim Tafo Q20119033 ("Tafo, G.C."), Busoga Q691037 (Uganda
  kingdom). Ceylon: Kegalle Q1968268, Peradeniya Q489744, Sabaragamuwa Province Q853272,
  Hambantota Q1025283 (Hambantotte, reuse). SA/Natal: Port Elizabeth→Gqeberha Q125434 (both
  "Cape Colony" and "Cape of Good Hope" variants), Weenen Q2096873, Msinga Local Municipality
  Q278422 (Umsinga magistracy), Qonce Q1016100 (King William's Town, reuse), Pietermaritzburg
  Q185591 (P.M. Burg., reuse). Malaya/Borneo/Pacific: Kinta District Q2781356, Rawang Q2072124
  (Selangor), Sabah Q179029 (modern state, literal name), Suva Q38807, Balaclava Q4849747 (Vic.
  suburb). Historical polities: Niger Coast Protectorate Q2566427 (all 3 "Oil Rivers/Oil Riv.
  Proteo." variants → one entity), British Cameroons Q1028835 (Br. Cams.), British North Borneo
  Q1147441 (N. Born., reused from Sabah search), Bengal Presidency Q817165, Province of Canada
  Q1121436 (late province of Canada), British rule in Burma Q2376315 (British Burmah, reuse),
  Gilbert and Ellice Islands Q1050859 (reuse), New Territories Q596660 (New Terr., reuse),
  Syria Q858 (Syrian Republic — no clean period "Syrian Republic" entity surfaced). Bourke
  county of Victoria Q5177825. Continents/regions grounded (consistent w/ Africa/N.America
  precedent): North America Q49 (reuse), Caribbean Q664609. South Caicos Q1814473 (Cockburn
  harbour = its main settlement). Nicosia Q3856 (Nikosia), Jerusalem Q1218 (reuse), Stanley
  Q12245 (Falklands, reuse). Skips: compounds (Klip River and Weenen counties, Transkei and
  Tembuland, Transvaal and Swaziland, Ken. and Uga. rlwys.), military (Rhine Army, W. African
  F.F. = West African Frontier Force, Cape and African station), institutions (B.G. museum,
  W.Pac.H.C., S. African parlt., legislative assem., Constantinople Embassy, Barb. Even. Inst.,
  Maur. Inst., L.G.B. = Local Government Board, minister of supply), generics (Dependencies,
  overseas, Union., Northern Provinces, Savanna), ambiguous initialisms (N. Border, L. Is.,
  N. B., Vict., Sel., Ky., L. C., C.), electoral/division fragments (county of Quebec, Quebec
  East, Mid Clarendon, New South, Inanda Division), ambiguous bare names (Mentone [Menton FR vs
  Mentone Vic], Bath was kept but Lucia/Regent skipped), no-entity (Dumbara [valley near Kandy],
  Amani [Tanganyika research station], Kissy [Freetown suburb — search empty x3], Mbaruk [person
  name], Benin territories [region grouping]).
- Batch 018 done: 61 grounded / 39 skipped; coverage holds at **89%** of 168,301 mentions
  (count-4–5 tail). World cities/counties: Essex Q23240, Oxfordshire Q23169, Devon Q23156
  (all ceremonial counties), Aberdeenshire Q3290674 (historic county — Scotland uses historic
  for corpus era), Dover Q179224, Govan Q1414040 (Glasgow), Oban Q935702, Algiers Q3561,
  Addis Ababa Q3624, San Francisco Q62, Nablus Q214178, Halifax Q2141 (NS), St. John's Q2082
  (Newfoundland), Vancouver Q24639, New Westminster-style, Moose Jaw Q1019496, Twillingate
  Q1732099 (town, for "Twillingate district"), Akaroa Q416098 + Ohakune Q2016369 (NZ). SA towns:
  George Q370456 (W. Cape), Warrenton Q1832033 (N. Cape), Bethulie Q646067 (Free State),
  Amersfoort Q2553018 (bare "Amersfoort" → SA Transvaal town per corpus, NOT the NL city).
  W. Africa: Kaduna Q208318, Keffi Q3510599, Zaria-area, Anomabu Q567542 (Anamaboe), Achimota
  Q4673778 (Accra). Ceylon: Kandy Q203197 (Kandy Kach., reuse), Kurunegala Q776887 (Kuruengala),
  Matara Q13360574 (Mátara), Harispattuwa Divisional Secretariat Q5657965 (Harispattu).
  Malaya/Borneo run: Kajang Q1946482, Seremban Q847610 (Seramban), Johor Bahru Q231318 (Johore
  Bharu), Bukit Mertajam Q2158697 (B. Mertajam), Sitiawan Q7531901, Batang Padang Q1938723,
  Rembau Q2219158 (reuse), Negeri Sembilan Q213893 (Neg. Semb.), Singapore Q334 (the city, for
  "Singapore, Straits Settlements"), Straits Settlements Q376178 (Straits Sttlmts., reuse). Fiji:
  Suva-area, Nadi Q619443, Tailevu Q1365322 (Tai Levu). Caribbean/Pacific: Barbados Q244 (reuse),
  Great Inagua Q3115958 (Inagua), Rum Cay Q1859950, Cocos (Keeling) Q36004 (reuse), Sheikh Othman
  Q377588 (Aden). Australia: York WA Q994000 (reuse), Hobart Q40191 (reuse). India/Pakistan:
  N.W. Frontier Province Q4412467 (reuse), Hazara Q10773634. Historical polities: German East
  Africa Q153963 (both "German E. Africa (Tanganyika Territory)" AND "G.E. Africa" → same),
  Eswatini Q1050 (Swaziland admstrn., reuse), Gilbert and Ellice Islands Q1050859 (reuse),
  Batavia Q1199713 (the 1619–1949 colonial Dutch East Indies capital, NOT modern Jakarta). Geo
  feature: Black Sea Q166 (consistent w/ grounding seas/lakes/rivers). Institution-as-place:
  Central Experimental Farm Ottawa Q4504150 (consistent w/ observatories/museums prior). Tai Po
  Q1758870 (Taipo, reuse-style). Skips: compounds (Federated Malay States Java and Sumatra,
  Kenya-Uganda-Tanganyika, Palestine and Syria, France and Palestine, Flanders and N. Russia,
  N'gamiland and Ghanzi, France and Germany, Lagos— S. Nigeria), institutions (E.A.A.R.I. Amani,
  E. African Currency board, Roseau town board, Trinity Church Colombo, government laboratories
  F.M.S., observatory), prisons/military (Georgetown pris., Glendairy prison, Shorncliffe camp,
  E.E.F. = Egyptian Expeditionary Force, China station naval), forestry conservancies (Natal/
  Eastern/Western conservancy), initialisms (G.W.B., N.F.F., C.C., S. Bank Prov., N. protectorate),
  divisions (Umlazi division, per Inanda-division precedent), ambiguous bare names (Victoria East
  [Cape division], St. Peter, St. Ann [parishes], Hay, West Indian, Niger Prov., Pondos [ethnonym]),
  district letters (District "C" Barbados), no-entity (St. John's River Ceylon), OCR fragments
  (st., W. Pacific ew Hebrides).
- Batch 019 done: 64 grounded / 36 skipped; coverage holds at **89%** of 168,301 mentions
  (count-4 tail). World cities/counties: Albania Q222, Norfolk Q23109, Kent Q23298, Hereford
  Q204720, Sevenoaks Q939838 (Kent), Hull→Kingston upon Hull Q128147, Falmouth Q478029 (Cornwall,
  Old-World default over Jamaica/Antigua), Chicago Q1297, Honolulu Q18094, Beijing Q956 (Peking),
  Jeddah Q374365, Darfur Q46733 (region), Gedaref→Al Qadarif Q311199, Port Sudan Q208718, Jijiga
  Q755763 (Jigjiga), Moudros Q1014244 (Mudros, Lemnos). Canada: Alberta Q1951 (Alta.), Edmonton
  Q2096, Fogo Q5464123 + Harbour Grace Q3127313 (Newfoundland). SA/Rhodesia towns: Bulawayo
  Q193250, Laingsburg Q927822, Kranskop Q1021915 (Krantzkop), Heidelberg Gauteng Q1594009
  (Heidelberg Transvaal — disambiguates the earlier bare-"Heidelberg" skip), Durban Q5468,
  Pinetown Q985839, Gaborone Q3919 (Gaberones). Malaya/Borneo/Fiji: Keningau Q1299852 (Keningan,
  Sabah), Limbang Q2181642 (Sarawak), Kota Tinggi Q935184 (K. Tinggi), Penang Q188096 (Penang
  division → state), Rewa Province Q1365257 (Fiji), Viti Levu Q208198 (reuse). Ceylon: Vavuniya
  Q1191330, Nuwara Eliya Q1340579 (kach., reuse), Northern Province Q598745 (N. Prov.),
  Nuwerakalawiya→North Central Province Q1057124. Caribbean: Dominica Q784, Sandy Point Town
  Q1972542 (St. Kitts), Barbados Q244 (reuse), Limassol Q185632 (reuse). Regions grounded
  (consistent w/ continents/Caribbean precedent): Middle East Q7204 (search only surfaced it via
  "Middle East Asia"→empty; bare "Middle East" returned it), Melanesia Q37394, Central Queensland
  Q5061728, Taranaki Region Q140207, Nandi County Q1964569 (Kenya), Ikot Ekpene Q680926 (Nigeria
  LGA). Historical polities (mostly reused): Niger Coast Protectorate Q2566427, Southern Nigeria
  Protectorate Q2062030 (South. Nigeria + S. Nigeria protectorate), British Bechuanaland Q4530733
  (B. Bechuanaland), N.W. Frontier Province Q4412467, German East Africa Q153963 (Ger. E. Africa),
  British Somaliland Q662653 (Som. protectorate), South West Africa Q953068 (S.W. Africa prot.),
  Quthing Q1003318, Eswatini Q1050 (Swaziland admnstrn.), British Central Africa Protectorate
  Q2642989 (Brit. Cent.), Sekondi-Takoradi Q243293 (Takoradi), Straits Settlements Q376178
  (S. Settmts.), British Malaya Q871091 (Br. Malaya), Northern Rhodesia Q953903 (N.Rhod.).
  ENDPOINT WAS VERY FLAKY this run — Beijing/Limbang/Jeddah/Bulawayo/Laingsburg/Kent/Penang/
  Darfur/Heidelberg/Chicago/Durban/Hull/Falmouth/Jijiga all needed plain-query retries (many
  returned "No matching items" on the descriptive first query). Skips: compounds (Praslin and
  La Digue, France Belgium and Italy, India and Aden, Cork and Plymouth, S. Settlimts. and F.M.S.,
  Malay States and Brunei, S'pore and Penang, fedl. government Rhod. and Nyasa.), forestry
  conservancies (Eastern/Midland/Western Conservancy, Transkeian — per batch 018 precedent),
  military/institutions (New Scotland Yard, Br. Guiana militia, government of Malta, W.A.I.F.O.R.,
  Yallahs Valley land authy., army, public accts., Brandport refugee camp), initialisms (B.S.A.,
  B.N.G. [British New Guinea — no clean colony entity surfaced], E. A. Y., Ind.), directional/
  generic fragments (N. Selangor, South protectorate, No. 3 mining district, N. district New
  Territories, Western Canada, S. African, W. African, Upper Rejang), ambiguous bare names
  (Queen's Town, Queen's Co., Bethesda, Macedonia, Matabele [ethnonym]).
- Batch 020 done: 54 grounded / 46 skipped; coverage holds at **89%** of 168,301 mentions
  (count-4 tail; skip rate rising as the tail fills with compounds/initialisms/districts).
  UK/Europe: Isle of Wight Q9679, Bedfordshire Q23143 (Beds.), Dorchester Q503331 (Dorset,
  Old-World default), Newark-on-Trent Q49940 (Newark, Old-World default), Midlothian Q67317221
  (historic county — Scotland uses historic per Aberdeenshire batch 018 precedent), Great Yarmouth
  Q237253, Stratfield Mortimer Q1982217 (Berkshire), Ulster Q93195 (Irish province), County Antrim
  Q189592, Budapest Q1781, Nice Q33959, Denmark Q35, Valparaíso Q33986. Canada/Australia/Africa
  cities: Ontario Q1904, Melbourne Q3141, Dakar Q3718, Castries Q41699 (St Lucia capital), Port
  Louis Q3929 (Pt. Louis 3rd division → city), Spanish Town Q846939 (Jamaica). SA towns/regions:
  Ingwavuma Q5138677, Greytown Q1021891 (Natal), Eshowe Q1367652 (divn.), Cape Peninsula Q748494,
  Tongoland→Maputaland Q4280999 (the historical Tongaland region of N. KZN). Ceylon: Kalutara
  Q1295530 (Kach.), Gampola Q8264065, Chilaw Q2495639 (Chilau), Nuwarakalawiya→North Central
  Province Q1057124 (reuse of last batch's Nuwerakalawiya). Malaya/Borneo: Seremban Q847610 (reuse),
  Gemas Q3523772, Matang Q61082734 (Perak), Belize District Q506056. India/Pakistan: Multan
  Q185453 (Mooltan), Ambala Q456624 (Umballa), Santal Parganas district Q132450366 (Sonthal),
  Hazara Q10773634 (reuse). Caribbean/Pacific: Eleuthera Q1141700 (Bahamas), Vere Parish Q60770124
  (Jamaica), Port Maria Q265115 (Jamaica), Seychelles Q1042, Cedros Q5057178 (Trinidad), Lyttelton
  Q911909 (NZ). Historical polities (mostly reused): Union of South Africa Q193619 (Union of
  Africa), South African Republic Q550374 (Transvaal Republic + Transvaal State), Transvaal
  Province Q190959 (Transvaal prov. division), East Africa Protectorate Q876185 (B. East Africa),
  Transkei Q466551 (Transkeian territory), Province of Canada Q1121436 (prov. of Canada),
  Republic of New Granada Q630882 (New Grenada), Darién Province Q688660 (Darien). U. States→Q30,
  Norfolk-style counties. ENDPOINT FLAKY AGAIN — Dakar/Ingwavuma/Middelburg/Gemas/Eleuthera/Antrim/
  Darién/Eshowe/Matang/Great Yarmouth/Castries/Gampola/Ulster/Nice all needed plain-query retries
  (often a full batch of 5 came back empty, then succeeded on the bare name). Skips: compounds
  (Sudan and S. Africa, Sarawak N. Borneo Brunei, N. Rhod. and Nyasa., Adelaide and Sydney
  Melbourne, Kimberley and De Beers, Stuttgart and Darmstadt, W. Falkland and S. Shetland, dists.
  A. and B., Larut and Krian [two Perak districts, no single clean entity]), military/institutions
  (Pacific station, Chinese protectorate Ipoh, Basseterre town board, Amani, U.K. board of inland
  rev., Chelsea barracks, South Kensington Museum [V&A], Sarawak Rangers, 1st Royal Lanark Militia,
  U.N., O.A.S., O.D.M.), initialisms/abbrev (M.S., N.W.R., W.A., E.A.F., F.P., S.E. Provs., W.P.
  Nigeria), directional/generic provinces (S. Abyssinia, E. reg., northern division, E./W.
  Gloucestershire/Bristol, E. Transvaal, Eastern Province, Upper Umkomanzi, Bechuanaland border),
  district letters (district "D."/"C", Buxton district), electoral (Comox-Atlin), ambiguous bare
  names (Middelburg [two SA towns — Mpumalanga vs E.Cape], St. Philip, St. James, Tasmanian
  [adjective], station), no-clean-entity (East Coolgardie Goldfield — only Coolgardie town + an
  electoral district surfaced, not the goldfield).
- Batch 021 done: 54 grounded / 46 skipped; coverage now **90%** of 168,301 mentions
  (count-4 tail). UK/Europe: Cork Q36647, Yorkshire Q163 (historic county), Hampshire Q23204
  (Hants), Shoeburyness Q593890, Cheadle skipped (ambiguous). Africa: Monrovia Q3748, Tangier
  Q126148, Banjul Q3726 (Bathurst, Gambia), Boma Q223917 (Congo), Sherbro Island Q2001267
  (both "Sherbro West Africa" + "Sherbro, S. Leone"), Yaba Q3509639 (Lagos), Lagos Q8673,
  Uruan Q11058133 (Nigeria LGA), Portuguese Mozambique Q889394 (period entity for bare
  "Mozambique" per historical-entity rule), Chikwawa Q1022541 + Mulanje Q1865092 (Malawi),
  Entebbe Q211970. SA towns (Western/Eastern Cape run): Clanwilliam Q1025657, Taung Q2096879
  (Taungs), Oudtshoorn Q951049, Somerset West Q1290313, Swellendam Q1023257, Tulbagh Q1937242,
  Graaff-Reinet Q1004667, Table Bay Q531909 (the Cape bay). Asia/ME: Kandahar Q45604, Sindh
  Q37211 (Scinde), Sumatra Q3492, Hejaz Q169977 (Hedjaz region), Cameron Highlands District
  Q1028741. Australia/NZ/Pacific: Gippsland Q1526531, Swansea Tasmania Q986654, Waikato Region
  Q139918, Northern Territory Q3235 (North Territory), Barossa Valley Q698920, Efate Q266594,
  Perim Q1160017. Canada/Caribbean: Bay de Verde Q2892176 (Newfoundland), Halifax Q2141 (N.S.,
  reuse), Northwest Territories Q2007, St. George's Q41547 (Grenada), Barbuda Island Q21052035,
  Mangrove Cay Q2702334 (Bahamas), Bartica Q809428 (Guyana), Chacachacare Q77021 (Trinidad),
  Zeitoun Q4116309 (Cairo district). Reused polities: Essequibo colony Q1368792 (Esse-quibo +
  Essequibo district), Transvaal Province Q190959 (T'vaal), Johannesburg Q34647 (J'burg.),
  Australia Q408 (Commonw. of Australia), British Somaliland Q662653 (B. Somaliland), NWFP
  Q4412467, Maputo Q3922 (Lourenço Marques). ENDPOINT FLAKY THROUGHOUT — most descriptive
  queries returned empty and only resolved on bare-name retries (Taung, St. George's, Tulbagh,
  Somerset West, Swansea, Uruan, Waikato, Swellendam, Hampshire, Mozambique, Banjul, Bay de
  Verde, Chikwawa, Mulanje, Boma, Perim, Northwest Territories, Barossa, Zeitoun all needed a
  second pass). Skips: compounds (Upper and Lower Doombera, Perak and Sungei Ujong, Mal. and
  S'pore., S. Provs. and Colony, Mesopotamia and N. Persia, Nos. 3 and 4 mining dists.,
  Roberts Heights and Transvaal commd.), military/institutions (Br. Hond. constaby., G. Coast
  volrs., Ashanti camp, Sudan rlways., Uganda Marine, B. of T. offices Glasgow, S. Kensington
  museum, minister of civil aviation, government of India, crown mines, Australian Museum,
  O.E.T.A.(S)), directional/generic (N. Cent. prov., N.E./Northern/Eastern/western district,
  Canadian N.W., S.-W./E. Transvaal, Upper Shire, North Victoria, Gold Field district),
  district letters (district "E", Strand Division, Peter's Hall district, McCarthy Prov.),
  initialisms (S.R., KE, N.), ambiguous bare names (St. Andrew's parish, St. James-style,
  Christ Church, Cheadle [two England towns], Colo [Fiji fragment], Robber's Is. [unclear OCR],
  county Caroni [only river/swamp surfaced], North Central Province [multi-country bare],
  N. Sherbro), no-clean-entity (Imperri [Sierra Leone chiefdom not in WD], co. of Quebec).
- Batch 022 (out-of-band province cluster, 2026-06-21): 19 grounded / 2 skipped. **`pending` emits
  in WORKLIST FILE ORDER, not count-desc** — a cluster of 21 country-qualified provinces had been
  appended at the worklist tail (lines 7709–7729) and would have been served ~76 batches out
  despite being the highest-frequency ungrounded places (count 5–109, ~745 mentions). Grounded
  directly by building a results file keyed to their exact surfaces. Ceylon provinces (clean,
  continuous w/ Sri Lanka): Western Q856686, Central Q190716, Eastern Q1046126, Southern Q876308,
  Northern Q598745. Sierra Leone: Northern Q912359. Nigeria regions/protectorates: Northern Region
  Q3509092, Eastern Region Q3509795 (also for "Eastern Province, Nigeria"), Western Region Q3509075
  (also for "Western Province, Nigeria"), Southern Provinces→Southern Nigeria Protectorate Q2062030,
  Northern Provinces→Northern Nigeria Protectorate Q585408. Gold Coast provinces→modern Ghana
  regions: Central Q846323, Western Q870155, Eastern Q405670. Kenya: Eastern Province Q328493
  (former province). Uganda provinces→regions: Western Q2559188, Eastern Q2559220. Skipped: Central
  Province Nigeria (S. Nigeria province dissolved, no successor region), Central Province Sierra
  Leone (never existed — SL had N/S/E/Western Area only). NOTE: colonial Nigeria/Gold Coast/Uganda
  "Provinces" grounded to their modern Region successors (slight period conflation, but the only WD
  node for the geographic area). Coverage after: **90.0% (151,431/168,301); count>=5 pending now 0.**
- Batch 023 done: 47 grounded / 53 skipped; coverage now **90.1%** of 168,301 mentions
  (count-4 tail, FILE-ORDER batch — max pending count is now 4; verified no buried high-count
  cluster by dumping all 7,731 pending sorted by count). World cities/regions: Enugu Q465022,
  East London Q209537 (E. London Cape of Good Hope), Kuching Q220445, Benin River Q19543934,
  North-Western Provinces Q138521 (N.W. Provinces and Oudh — the British-India period entity),
  Haputale Q3533257, Karamoja Q2614835 (Uganda sub-region), Lower Egypt Q463871, County Durham
  Q23082, Hilir Perak Q2381489 (lower Perak), Mumbai Q1156 (Bombay India), British Columbia
  Q1973 (OCR "British Colombia"), Stuttgart Q1022 (Stuttgartt), Swan River Colony Q1162123
  (Swan River W. Australia — period entity), Christchurch Q79990, Canterbury Region Q657004,
  London Ontario Q92561, Teluk Intan Q1317145 (Telok Anson), Berbice River Q2896921, Ilorin
  Q587085, Douala Q132830 (Duala), Kwahu Q3330858 (Ghana town), Nibong Tebal Q848853 (Nebong
  Tebal), Mullaitivu Q507144 (Mulletivoe), Savusavu Q619440 (Savu Savu), Ireland Q27 (Eire),
  Dublin Q1761 (Dub.), Coast Province Kenya Q185371 (coast Kenya), Repton Q1018787 (Derbyshire
  village), Montreal Q340 (district of Montreal → city), Demerara Q1185346 (historic region of
  the Guianas — the clean Demerara node, distinct from Demerara River/Demerara-Mahaica).
  Institutions-as-place: Sarawak State Museum Q3329752, Kew Observatory Q3348489, Stormsrivier
  settlement Q7620269. Historical polity (one entity for the compound name): Federation of
  Rhodesia and Nyasaland Q654342. Reused prior-batch QIDs (no re-search): British Central Africa
  Protectorate Q2642989 (Br. Cent. Africa), Australia Q408 (C. of Australia), Johannesburg Q34647
  (J'burg), Pietermaritzburg Q185591 (city division P.M. Burg), Gold Coast Colony Q503623 (G.C.
  Colony), Harispattuwa Q5657965 (Harrispattoo), Nuwara Eliya Q1340579 (Nuwera Ellia x2), Entebbe
  Q211970, New Brunswick Q1965, Bunyoro Q889897 (Unyoro), Singapore Q334 (S'pore divn.). ENDPOINT
  DROPPED one call (N.W. Provinces) and returned empty on several descriptive queries (Telok Anson,
  Berbice River, Savusavu, Repton, Near East, Demerara, Storms River) — all resolved on bare-name
  retries. Skips (53): compounds (Singapore and Malacca, Kenya Uganda, S.S. and N. Borneo, Antigua
  and the Leeward Islands, Bridgetown and district A, Durban Greytown Newcastle Ixopo and Umlazi,
  re-united provinces, Australian colonies), institutions/boards/offices (agriculture prod. and
  settlement board, colonial geol. surveys, Gozo courts, minister of finance, M. Health, legislative
  co., chief and D. Hong Kong, Accra sisal plantn., Chilungula/Masasi constrn.), railways (Ceylon
  rlwys., Nigeria rlwys.), military/events (53rd Sikhs F.F., Igbo Patrol, Pal. conferences),
  initialisms (B. D. and M., D.C.S., D.O.S., B.H.T.F., t. E. Africa), directional/generic fragments
  (St. John's E., E. Newfndld., E. Newfld., W. Demerara, West Prov., 1st district Saint Lucia,
  Northern Frontier, city, island, East), region-groupings w/ no clean WD node (Kavirondo [Nyanza],
  Batoka district [Zambia plateau], Angoniland [Ngoni, Nyasaland], Ishan [Esan division], Benin
  Terr., Asaba Hint., Near East [only Middle East Q7204 surfaces — already grounded separately],
  Congo [Free State vs river vs country ambiguity], Northern Territories (Neutral Zone) [specific
  Anglo-German zone, no distinct node]), ambiguous bare name (Ravensthorpe [WA town vs England
  village]), OCR fragments (in, ne, g., St. ay, Virgin April, Br. Caribbean pre-fed. estab.).
- Batch 024 done: 45 grounded / 55 skipped; coverage now **90.16%** of 168,301 mentions
  (count-3 tail; skip rate rising as tail fills with compounds/initialisms/prisons/mines/military).
  Verified no buried high-count cluster (dumped all 7,631 pending sorted by count — max is 4).
  World cities/towns: Calgary Q36312, Crewe Q648810, Ramsgate Q736439 (Kent), Staffordshire Q23105
  (Staffs. + Staffordshire), Ahmedabad Q1070, Omdurman Q180921, Sorel-Tracy Q142010 (Sorel Quebec),
  Anuradhapura Q5724 (Kachcheri/Kach. ×2), Piet Retief Q1395427, Kuala Kubu Bharu Q684062 (K. Kubu),
  Taiping Q1011190, Tanjung Malim Q3537158 (T. Malim), Kemaman District Q1827701, Labasa Q579556 +
  Levuka Q26692 (Fiji), Dewetsdorp Q593434, Mandeville Q1807660 (Maudeville District of Manchester),
  Montego Bay Q637555 (St. James), Fanning Is.→Tabuaeran Q127335 (Kiribati atoll, not the Falklands
  islet). Jamaica parishes/places: Saint Elizabeth Parish Q1473646 (St. Elizabeth), Saint Mary Parish
  Q633565 (St. Mary Jamaica). India regions/districts: Kanara Q3010684 (Canara region), Ratnagiri
  district Q1771768 (Rutnagherry district). Region/geo: Lake Kyoga Q124978 (Lake Kioga), Seberang
  Perai Q1861984 (Prov. of Wellesley = Province Wellesley), South America Q18 (S. America — continent,
  per Africa/N.America precedent). Institution-as-place: Kew Gardens Q188617 (Royal Gardens Kew).
  Abaco Islands Q304371 (Abaco Bahamas). Reused prior-batch QIDs: British Central Africa Protectorate
  Q2642989 (B. Cent. Africa), Straits Settlements Q376178 (S. Sttmts.), Saint Vincent Q379656,
  Teluk Intan Q1317145 (T. Anson), NWFP Q4412467 (N.W. frontier of India), Spanish Town Q846939,
  Tanganyika Territory Q158725, Kandy Q203197 (kachcheri), Colombo Q35381 (mun.), Southern Nigeria
  Protectorate Q2062030 (Nigeria S. Provs.), Northern Territories of the Gold Coast Q1998749 (N.T.),
  Portuguese Mozambique Q889394 (Port. E. Africa), Arima Q661405, Galle Q319366 (Kach.), Matara
  Q13360574 (Kachcheri). ENDPOINT FLAKY (one batch of 5 returned 4 empties — Staffordshire/Lake
  Kyoga/Ahmedabad/Damaraland all needed plain-name retries). Skips (55): prisons/penal settlements
  (H.M.'s penal settlement Massaruni ×2, Suva gaol, New Amsterdam prison Berbice), mines (Durban
  Roodepoort Deep Mine, Village Main Reef), military (Marlborough Hussar Vol. N.Z., N.Z. Militia,
  Malay States Guides, G. Coast Constaby. Hausas), institutions/orgs (Inst. for medical Research,
  Lagos harbour works, S. African Reserve Bank, co-op. socs., United Farmers of Ontario, L. of N.,
  Overseas Bases), forestry conservancy (Transkeian conservancy Cape Colony — per precedent),
  compounds (Aden and India, Nigeria Gold Coast Sierra Leone and Gambia, England and France, Gopeng
  and Kampar, Br. Columbia and N. Can., B.C. and Yukon, Colombo and Negombo, Kedah and Perlis, North
  Borneo and Labuan, Kwahu and Ashanti-Akim, Cape and Transvaal, Antigua-Montserrat, Dists. A. and
  B.), directional/generic (district D., West Algoma, N.W. Manchester, N.W. Ashanti, Kinta North,
  Derbyshire W., eastern districts, Southern Province, province, African coast, Hinterland, Home,
  Queen's), initialisms/adjectives (R. of O., G.E.I.C., Australian, Malayan, junks), wrong-era only
  node (Damaraland — only the 1970s bantustan Q1158213 surfaces, not colonial-era region; per prov.-
  of-Zululand precedent), ambiguous bare names (Flinders, Hope Town, Herschel), no-clean-entity
  (Balapitimodara [Balapitiya estuary, OCR-ish — only the town Balapitiya surfaces], Laroot River).
- Batch 025 done: 51 grounded / 50 skipped (incl. 1 out-of-band buried count-4); coverage now
  **90.25%** of 168,301 mentions (count-3 tail). Buried count-4 "Northern District, Palestine"
  found via full-pending sort — SKIPPED (only modern Israel Northern District Q189942 surfaces,
  wrong-era; no Mandatory-Palestine "Northern District" node). World cities/towns: Brockville
  Q34047, Beverley Q851718 (Yorks, Old-World default), Shrewsbury Q201970, Ramsgate-style, Ripon
  Q661529 (Ripon divn. Yorks), Southwark Q5273898, Calgary-style, Sorel-style, Dar es Salaam Q1960,
  Kano Q182984, Oyo Q1023703, Livingstone Q1866604 (Zambia), Omdurman-style, Qinhuangdao Q58560
  (Chinwangtao, China treaty port), Port of Spain Q39178. SA/Natal/Free State towns: Jagersfontein
  Q2460233, Fauresmith Q985813, Aliwal North Q2143142 (Aliwal N.), Dewetsdorp-style, Stanger→KwaDukuza
  Q10676708, Nquthu Local Municipality Q2003963 (Nqutu district Zululand), Dundee→Q1265538 (Natal
  town, for both "Dundee district" + "Dundee division"), Hlatikulu Q3235603 (Swaziland). Malaya/Fiji:
  Larut Matang Selama Q2694747 (Larut Perak), Endau Q5375966 (Johore), Kukup Q6442600 (Johor village),
  Bua Q1365265 (Fiji province, for "Bua" + "Bua Prov."), Levuka-style, Tarawa Q2486 (Kiribati atoll).
  Ceylon: Bentota Q4890663 (Bentotte), Anuradhapura-style. Trinidad: Mayaro Q6796869, Naparima Plain
  Q16969039 (region for Naparima ward). Ghana/Nigeria/Cameroon: Nsawam Q2003928, Northern Cameroons
  Q111207687 (N. Cameroons — period node, distinct from Southern Cameroons). NZ: Westland District
  Q2119644. Regions/countries grounded: Serbia Q403, South America Q18 (S. America, continent),
  Suez Canal Q899 (waterway), Hadhramaut Q1517159 (Hadhramaut States→region), British Togoland Q797527
  (British Zone of Togoland). Reused prior-batch QIDs: Southern Nigeria Protectorate Q2062030 (Colony
  and protectorate of S. Nigeria), Transvaal Province Q190959 (Prov. divn.), Eastern Province Ceylon
  Q1046126, South West Africa Q953068 (S.W. Africa Protectorate), Eshowe Q1367652 (Zululand), Quebec
  Q176 (prov. of), Kota Bharu Q651131, German East Africa Q153963 (G.E.A. Tanganyika Terr.), British
  Malaya Q871091, Saint Kitts and Nevis Q763 (S. Kitts-Nevis), Johannesburg Q34647 (North), Nova
  Scotia Q1952 (N. Scotia), Simon's Town Q1013370 (Simonstown), Uruan Q11058133 (frontier station),
  Federation of Rhodesia and Nyasaland Q654342, Larnaca Q171882 (district). Skips (50): compounds
  (Aden and India-style: G. Coast and Lagos, Colombo and Galle, Belgium and France, Kenya-Uganda,
  Nyasaland-Rhodesia, Washington and Ottawa, Egypt Mesopotamia and India, Canada Australia New
  Zealand, British Honduras and Cent. America, Fortress and Sheikh Othman Townships), prisons
  (Freetown gaol), institutions/orgs/govt (Union senate, national provident fund, Indian immignts.,
  government of Union of S. Africa, E. Africa currency board, Inst. for medical Research FMS,
  Carmichael St. Georgetown, Bulford Camp), military/ships (H.M.S. "Conway", Umunze Awka Patrol),
  forestry conservancy (eastern conservancy), region-groupings (Malay Native States, Niger
  Territories, Syrian Coast, Out Islands, Hadhramaut already done), wrong-era/no-clean-node (Northern
  District Palestine, Nichol Bay district [only WA bay/locality, not the pastoral district]),
  divisions per precedent (Lower Tugela division Natal, Klip River division, Up. Umkomanzi, N.
  Malacca, S. Wales district, W. frontier, Northern Circuit, East Luangwa), ambiguous bare names
  (Bergen [Norway vs NL], Rietfontein [many SA], St. Johns, St. Mark's parish, West End, Chapeau,
  Coronation, Kafir [ethnonym], Birrim [Ghana river/region], Ioma/Kairuku [Papua stations — search
  not run, low value]), initialisms (G.N.R., N.C.P., district "I").
- Batch 026 done: 48 grounded / 52 skipped; coverage now **90.34%** of 168,301 mentions
  (count-3 tail; verified no buried high-count cluster — max pending count is 3). World cities:
  New Orleans Q34404, Birmingham Q2256 (B'ham), Stockholm Q1754, Casablanca Q7903 (Casa Blanca),
  Baden-Baden Q4100, Cherbourg-Octeville Q160199 (the historical city of Cherbourg), Chelsea Q743535
  (London area), Reading Q161491, Hastings Q29245 (E. Sussex, Old-World default over NZ), Shrewsbury-
  style, Pembrokeshire Q213361 (Wales), Saint-Hyacinthe Q141873 (Quebec), Brockville-style. Africa
  towns/cities/regions: Kisumu Q214485, Kabale Q588930, Tenom Q1011955 (Sabah), Dar-style, Kano-style,
  Ankole Q538636 (former kingdom Uganda), West Nile sub-region Q4261446 (W. Nile), Zeila Q157800
  (Zeyla, Somaliland), Gezira Q309469 (Sudan state), Ambriz Q458731 (Angola commune — query mislabeled
  "South West Africa"), Volta Region Q712832 (Volta district), Tabankulu→Ntabankulu LM Q527085.
  Asia/ME: Jaffna Q215277 (Jaffra), Matale Q1540498 (Mátale + Mátalé accent variants), Tampin Q2219146
  (Negri Sembilan), Makran Q695111 (Mekran S. Persia — region), Qinhuangdao-style. Pacific/Caribbean:
  Lau Islands Q1062438 (Lau Archipelago), Westmoreland Parish Q1440250 (Jamaica), Sea Islands Q1535683
  (Sea Is. S. Carolina), Naparima-style. Country/region: Philippines Q928, Angola→Portuguese Angola
  Q2826232 (period entity per historical-entity rule). Canada: Perth County Q177690, United Counties of
  Prescott and Russell Q1815593 (county of Russell), Eketāhuna Q377814 (NZ), Smithfield Q820535 (Free
  State town — bare name grounded to SA per surrounding OFS corpus context). Reused prior-batch QIDs:
  Northern Nigeria Protectorate Q585408 (N. Provs. Kaduna), South West Africa Q953068 (S. West Africa),
  Saint Vincent Q379656 (Windward Islands St V.), Muri Q11883435 (Prov.), Sokoto Q336350 (Prov.),
  Ficksburg Q1014580, Transvaal Province Q190959, Selangor Q189710 (Salangore), Rewa Province Q1365257,
  Gilbert and Ellice Islands Q1050859 (Coly.), Northern Cameroons Q111207687, Ontario Q1904, Kota Bharu
  Q651131 (K. Bahru). ENDPOINT FLAKY (one batch of 5 returned all-empty — Tampin/Gezira/Ankole/Zeila/
  Makran all needed bare-name retries). Skips (52): compounds (Trinidad and Grenada, France and England,
  Washington Paris and St. Petersburg, Rarotonga and Penrhyn Is., St. Kitts and Dominica, Kowloon and
  New Territories HK, E. Africa and Uganda protectorate, Straits Settlements F.M.S. and Hong Kong,
  Grenada and St. Vincent, Australia and N.Z., Nuwara Eliya-Hatton, Tenom-Tawau, Aquamoo and Crepee),
  institutions/orgs/govt (general list, W. African lands committee, public works, Imp./Impl. Economic+
  education Confce., Dominion government, Transvaal State Arty., Barbados volunteers, Berm. trade devel.
  board, F.M. Chinese protectorate Perak, B.B.C., C.O. confce.), prisons (Glendairy pris., general
  penitentiary), military/ships (R.G.A. S.R., E.A.L.F.O., H.M.S. "Minotaur", Admlty.), region-groupings
  /directional (Western Division B.N.G. [no clean British New Guinea node, per batch 019], Northern
  protectorate, Nupe Prov. [ethnonym/kingdom, no clean province node], W. African dependencies, South
  Bourke, S. Africa eastern dists., west coast district BG, Africa protectorate, Siamese Malay States,
  Lower Umfolosei), wrong-era/ambiguous-only (Zoutpansberg Transvaal [only mountain range Soutpansberg,
  per batch 010], Zambesia [BSAC vs Mozambique ambiguity], Syracuse [NY vs Sicily], St. Ann's, Whim
  Corentyne [obscure Guyana village], Lastron OFS [OCR]), initialisms/fragments (Chin., n., W., Admlty.,
  district "D.", Palma and Leckie).
- Batch 027 done: 63 grounded / 37 skipped; coverage now **90.45%** of 168,301 mentions
  (count-3 tail; verified no buried high-count cluster — max pending count is 3). World cities/
  counties: Agra Q42941, Naples Q2634, Limerick Q133315, Stroud Q281749 (Gloucs.), Barnsley
  Q54212 (S. Yorks), Banbury Q806160 (Oxon), Berwick→Berwick-upon-Tweed Q504678, Melrose Q632993
  (Scottish Borders, Old-World default), Herts→Hertfordshire Q3410 (ceremonial per England
  precedent), Hampstead Q25610 ("division of Middlesex"→London area), Somerset House Q1344889
  (London building, institution-as-place), Winnipeg Q2135, Darbhanga Q1136189 ("Durbhunga
  Tirhoot"), Saugor district→Sagar district Q2085421, Morar→Morar Cantonment Q2725698 (Gwalior),
  Nowshera Q2003745 (KPK Pakistan). Australia/NZ/Pacific: Tenterfield Q1002140 (NSW), Westbury
  Tasmania Q385934, Launceston Q339527 (Tas.), Rottnest→Rottnest Island Q585317 (WA), Geraldton
  Q605267 (WA), Wyndham Q477835 (Cambridge Gulf, Kimberley WA), Van Dieman's Land→Q1780114
  (period colony), Kingdom of Tonga→Tonga Q678, Fanning Island→Tabuaeran Q127335 (reuse b024).
  Malaya/Borneo: Kampar Q22694790 (Perak town), Fraser's Hill Q3086678 (Pahang), Baram Q7311426
  (Sarawak district), Bintulu Q594209, Lundu Q6704167, Trans Krian→Kerian District Q2674376,
  Sri Menanti→Seri Menanti Q3132595, Batang Padang Q1938723 (reuse b018), S. Stlts./Str. Settl.→
  Straits Settlements Q376178 (reuse). Ceylon: Haldummulla Q5641318, Anuradhpura→Anuradhapura
  Q5724 (reuse b024). Africa towns: Winnebah→Winneba Q1188560 (Gold Coast), Sekondi→Sekondi-
  Takoradi Q243293 (reuse), Salt Pond→Saltpond Q340149, Abeokuta Q206484 (reuse b017), Ikoroda/
  Ikorodu→Ikorodu Q1658159. SA/Natal: Hopetown Q618063 (N. Cape), Fort Beaufort Q473216 (E.
  Cape), Fort Carnarvon→Carnarvon Q625378 (N. Cape town), division of Ixopo→Ixopo Q827279,
  Inanda Natal→Inanda Q12730377, Mapumulo→Maphumulo Q1892042, Nkandhla district→Nkandla Q498225,
  Tugela Valley→Tugela River Q476317, Lions River Q13035272 (reuse b016), Weenen division→Weenen
  Q2096873 (reuse b011), Taungs→Taung Q2096879 (reuse b021). Caribbean/Guyana: Corozal Q882907
  (Belize), Turk's Islands→Turks and Caicos Q18221, St. Elizabeth Jamaica→Q1473646 (reuse b024),
  St. Ann Jamaica→Saint Ann Parish Q1326284, Essequibo river Q589911. Regions/countries:
  Central America Q27611 (subregion, per continent precedent), Hellenes→Kingdom of Greece Q209065
  (period entity), Roumania→Kingdom of Romania Q203493 (period entity). ENDPOINT FLAKY (Baram/
  Bintulu/Ikorodu first pass empty; Hertfordshire/Stroud/Wyndham/Tonga whole batch empty; Nowshera/
  Haldummulla needed bare-name retries). Skips (37): directional/letter districts (S.W. district
  Penang, northern district NSW, district C. Dominica, district H., Port of Spain North, Colo. N./
  Colo. W. [Fiji frags per precedent], Victoria district, Elgin district, York District), generics/
  anaphora (board, that colony, same province, Commonwealth government, Western Provinces), ambiguous
  province frags (north-central province ×2, N. Central Prov. — Ceylon vs India, no country
  qualifier), compounds (Samoan and Union Groups, Kalpitiya and Puttalam, Natal and Orange Free
  State, Vavuniya and Mullaitivu), institutions (Indian and Colonial Exhibition, Melbourne harbour
  trust, S. African museum, Edin. Royal Infirmary, Kirkdale prison Liverpool), military (4th Light
  Dragoons), region-groupings (Western Pacific Islands, W. Pacific Is., N. circuit Ceylon [judicial]),
  ambiguous bare names (Maryborough [Qld vs Vic], Republic of S.A. [SAR vs RSA]), initialisms/OCR
  frags (S.A.H.C., Larnt., H. Honduras, Orang general).
- Batch 028 done: 56 grounded / 44 skipped; coverage now **90.55%** of 168,301 mentions
  (count-3 tail; verified no buried high-count cluster — max pending count is 3). UK/Ireland:
  Lincolnshire Q23090 (ceremonial), Cheshire Q23064 (ceremonial), Bury Q47822 (Gtr Manchester/
  Lancashire), High Wycombe Q64116 (Bucks), Huddersfield Q201812, Dunwich Q188020 (Suffolk,
  Old-World default over Qld), Tavistock Q668262 (Devon), Berwick-style; Scot.→Scotland Q22,
  Gt. Brit.→Great Britain Q23666 (reuse b015). Canada: Athabasca→Athabasca District Q5283393
  (period NWT district, not the town), Lennoxville Q672089 (Quebec), Arthabaska→Arthabaska County
  Q2991091 (historic Quebec county), Wentworth County Ontario Q7983017, Guyshorough→Guysborough
  Q5622877 (N.S.), British Columbia Q1973 (reuse b023). Africa: De Aar Q743069 + Hondeklip Bay
  Q2935301 + Murraysburg Q2365106 + Sterkstroom Q3642303 (Cape towns), Cape Town Q5465 ("and
  district"), Pram Pram→Prampram Q15045728 + Tamale Q217040 + Akwapim→Akropong-Akuapem Q4701715
  (Ghana), Opobo→Opobo Town Q3238928 (Nigeria city-state), Nairobi Q3870 (E.A.P.), Naivasha
  Q1007647 (Prov.→town), Ogaden Q137555 (region), Mafia Island Q713391 (Tanzania), G.C. colonial→
  Gold Coast Colony Q503623 (reuse), Niger C. Protec.→Niger Coast Protectorate Q2566427 (reuse),
  Sherbro country→Sherbro Island Q2001267 (reuse), Nthn. Rhodn.→Northern Rhodesia Q953903 (reuse),
  Pietermaritzburg Q185591 (county/city division, reuse), Harisputtu→Harispattuwa Q5657965 (reuse).
  Caribbean/Atlantic: St. Salvador→San Salvador Island Q845540 (Bahamas, per Long Cay/Bahama Is.
  cluster context), Long Cay Q1232322 (Bahamas), Bahama Is.→Bahamas Q778 (reuse), Green Turtle Cay
  Q3249446 (Abaco), Black River Mauritius→Riviere Noire District Q873740, Naparima ward union→
  Naparima Plain Q16969039 (reuse), Chavakacheri Q1068504 (reuse), Larnaca Q171882 (reuse), Windward
  Islds.→British Windward Islands Q2660774 + Lee-ward Is.→British Leeward Islands Q1796551 (reuse).
  Asia/Pacific/Aus/NZ: Nudea/Nuddea→Nadia District 1787-1947 Q139099436 (period entity), Cuddapah
  +Cuddapah district→Kadapa Q30651 (reuse), Lau prov.→Lau Q513104 (Fiji), Mount Gambier Q327348
  (SA), Greymouth Q934790 (NZ), Newera Ellia→Nuwara Eliya Q1340579 (reuse), Sclangor→Selangor
  Q189710 (reuse), Dorset Q23159 (reuse). Europe: Dodecanese Q131555 (island group). ENDPOINT
  FLAKY (Huddersfield/Dodecanese/Akuapem/Dunwich/Guysborough/Cheshire first-pass empty, resolved on
  bare-name retries). Skips (44): directional/letter/descriptive districts (S.W. district Penang
  [prior], north-west, E. Coast district Br. N. Borneo, western district of county of St. George
  w/ Port of Spain, Leckie east district, N.W. province, Northern Prov., N. and W. Provs.),
  compounds (Scinde and Punjaub, Grand Port and Savanne, St. Silas and St. Albans, Guatemala and
  British Honduras, Chilaw-Puttalam, Mauritius (Rodrigues), Canada and Ireland, Kenya Uganda and
  Tanganyika Territory), institutions/govt/military (B. Guiana bindry. survey, rlwys. Palestine,
  Caterham Asylum, government of Victoria, Dominion Government, Victoria Gaol Hong Kong, Union
  Defence Forces, Makogai leper asylum, fed. government, Keyham naval barracks, Chinese hosps. and
  dispensaries, B.M.A., W.A.C.), conservancy (Natal conservancy), generics/anaphora (board,
  same/that province-style: "Province Alcock", "S. Angoniland" [Angoniland no node, per b023]),
  ambiguous bare names (Newington, Milton, St. Michael [parish], Marquette, Turkey in Asia, St.
  John's River [Ceylon, per b018], Chin. Singapore), no-clean-entity/OCR frags (Nowbutpore, Kaihihi
  Pas, Chircop, Yilgarn gold fields [goldfield, per East Coolgardie precedent], Marimba district,
  Ryton-on-Dunsmore [only war-memorial node surfaced]).
- Batch 029 done: 38 grounded / 62 skipped; coverage now **90.62%** of 168,301 mentions
  (count-3 tail; HIGH skip rate — this slice was institution/military/initialism-heavy. Verified no
  buried high-count cluster — max pending count is 3). New grounds: Bulgaria→Kingdom of Bulgaria
  Q147909 (period entity, per Greece/Romania precedent), mandated Territory of New Guinea→Q1443945
  (1920 Australian mandate), Mosul prov.→Mosul Vilayet Q1969497, Sulaimani→Sulaymaniyah Q191204,
  Willowvale Q3644236 (E. Cape), Gilbert Is.→Gilbert Islands Q271876 (distinct from Gilbert+Ellice
  colony Q1050859), Pitcairn Is.→Q35672, Dominion observatory Ottawa→Dominion Observatory Q266818
  (institution-as-place, per observatory precedent), Warringah Q377295 (NSW former LGA), Wolmaransstad
  Q3642582, Gunnedah Q1554825 (NSW), Kluang Q1200738 (Johor), Besut Q1884571 (Terengganu), Gibr.→
  Gibraltar Q1410, Barking Q377720 (London), Sorrell→Sorell Q2118504 (Tas), Manchuria Q81126
  (region), Hanbow→Hankou Q1208250 (Wuhan), Reitz Q2208947 (Free State), Concordia Q3642542
  (Namaqualand). Reused QIDs (no re-search): N. Rhodesia (Fort Jameson)→Northern Rhodesia Q953903,
  N.W.F.P.→Q4412467, Rhod. and Nyasa ×2→Federation of Rhodesia and Nyasaland Q654342, Kota Tinggi
  Q935184, B. Malaya→British Malaya Q871091, Swellendam Q1023257, J'lem district→Jerusalem Q1218,
  Chungking→Chongqing Q11725, Kingwilliamstown→Qonce Q1016100, Birm.→Birmingham Q2256, G. & E. Is.→
  Gilbert and Ellice Islands Q1050859, B.C.A./Brit. Cent. Africa/Cent. Africa protectorate ×3→
  British Central Africa Protectorate Q2642989, Fogo Q5464123, city of Halifax→Q2141, Cape Tn.→Cape
  Town Q5465. ENDPOINT FLAKY (Warringah/Kigezi/Kluang/Besut/Concordia first-pass empty, resolved on
  retries). Search-resistant (skipped, real but vector search wouldn't surface clean node): Robertson
  district (3 attempts — only church/suburb/lake nodes return), Kigezi (Uganda sub-region — only
  wildlife-reserve/school surface), Emtonjaneni (Zululand magistracy), Beautiful Plains (Manitoba RM
  — only school-division/electoral surface). Skips (62, this tail is dense with them): institutions/
  research-stns/observatory-adjacent (inst. for medical research, E.A. agric. res. inst. Amani,
  Forest Products Inst., F.M.S. museums, Raffles Instn., Rothamsted exper. stn., Cameroons plantations,
  H.M. dockyard Simon's Town, Fort instns. Saint Vincent, Crown Mines, Ken. prisons), military
  (Durban Light Infy., Forth and Clyde Defences, Br. Guiana Militia Band, Arab Legion, Royal Navy,
  Donegal Artillery, W.O. and Eastern Cmd., Hants and Isle of Wight Arty., B.M.A. (B. Borneo)),
  railways (Nigerian Ry., K.U.R.), offices/govt (minister of health, Nigerian secrtn., Br. mission in
  Czechoslovakia), initialisms (W.A.I.T.R., D.O. and C.O., E.A.P. & S.C., Ghan.), compounds (N. and S.
  China, India and in Burma, Dominica and St. L., Aden and protectorate of S. Arabia, Lagos and S.
  Cams., United Kingdom Normandy Holland and Germany, Kedah/Perlis, Macuata and Bua, S.W. Africa and
  France, E. Africa and overseas, Manitoba and N.W.T., Br. Caribbean), directional/generic province
  frags (N. Provs. Ashanti, Victoria W., N. Palestine, Northern Transvaal, North Perak, N. Nyasa,
  Cross Riv. division, S. Prov. Western Australia, various areas, district "F", Corentyne judicial
  district, U. of S.A. [Union vs University ambiguous], Nigerian [adjective], Prov. Alcock [per b028]),
  ambiguous bare names (Mowbray, Granada [Spain vs Grenada WI], Delarey).
- Batch 030 done: 40 grounded / 60 skipped; coverage now **90.69%** of 168,301 mentions
  (count-3 tail; HIGH skip rate again — institution/military/OCR-fragment dense. Verified no buried
  high-count cluster — max pending count is 3). New grounds: Baghdad Q1530, Prince of Wales Island→
  Penang Island Q1150673 (colonial name for Penang), Pontefract Q1009235, Carriacon→Carriacou Q795647,
  Three-Rivers→Trois-Rivières Q44012, Para→Pará Q39517 (Brazil state), Kumasi Q182059, K. Treng.→
  Kuala Terengganu Q846502, Falkland Is. Dependencies Q5431953, N. Delhi→New Delhi Q987, Canada West→
  Province of Canada Q1121436 (period polity — no distinct "Canada West" node), Highbury Q124394
  (London), London England Q84, Island of Malta→Q193896 (the island, distinct from country Q233),
  maritime provinces Canada→Maritimes Q731613, Tamworth Q704864 (Staffs, Old-World default), Akuse
  Q4701984 (Ghana), Darmstadt Q2973, Galkisse→Dehiwala-Mount Lavinia Q24462 (Galkissa=Mt Lavinia),
  Portugal Q45, Winchester Q172157, Middlesbrough Q171866, S. Wales→South Wales region Q1286223,
  Basingstoke Q810196, Tamworth, Carriacou, Highbury. Reused QIDs: Weenen Q2096873, S.W.A. protectorate→
  South West Africa Q953068, Keffi Q3510599, Oil Rivers protectorate→Niger Coast Protectorate Q2566427,
  Haifa Q41621, Spanish Twn.→Spanish Town Q846939, Port Swetten-→Port Klang Q11155122, Somerset (East)
  →KwaNojoli Q1021900, Fed. of Malaya Q1479726, Freestown→Freetown Q3780, Leeward Isles→British
  Leeward Islands Q1796551, Pekin→Beijing Q956, N. Nigeria→Northern Nigeria Protectorate Q585408,
  British Guinea→British Guiana Q918126, KW Town→Qonce Q1016100, Kaffrarian→British Kaffraria Q918121.
  ENDPOINT FLAKY (Kumasi/Highbury/London/Malta/Morpeth/Winchester/Middlesbrough first-pass empty,
  resolved on retries). Search-resistant skip: Isles de Los (Guinea archipelago — only member islands
  Kassa/Rouma surface, not the group node). Skips (60): OCR fragments (tlmts., ec., t., s, e, stine,
  g Tebal, Port Swetten- [grounded], ganyika Territory, 3. Coast, Gold last, gr. C., P. R. G., W/o. I,
  European gr., Plain Wrahem District), institutions/military/railways/offices (Midland inspectorate,
  Canadian militia, vagrant dépôt, B.M.A. Somaliland, Somali affrs., Somerset Light Infantry, M.E.L.F.,
  Nig. coal corpn., conf. of comsns. of labr., minister supply, African education, Lagos Prison, royal
  horse artillery, Br. India Coy., G.C. rlwys.(+harbours), rlwys. Tanganyika, N.Z. govt rlwys., Pal.
  rlwys, Lyceum Malta, board agr., B.O.T., executive co., R.N., Worcester militia, Nig. G.E.U.),
  initialisms (C.O. and C.R.O., W.A.M.S., I.C.A.O., B.O.T.), compounds (Kimberley and De Beers,
  Rodriguez and luna Islands, Kenya Uga. and Tang., Singapore and F.M.S., England and Ireland,
  Barberton Pilgrim's Rest and Rhodesia, Dahomey border), directional/generic (West Toronto, Eastern
  divn., Haifa N. district [grounded to Haifa], N. Provs.-style, West Birmingham, Houssa [ethnonym],
  Ziland [OCR Zululand?]), ambiguous bare (Eccles Hill, Br. Borneo terrs.).
- Reuse pass 01 (2026-06-22): +166 zero-FP variant groundings, 90.69%->90.82%. See SCOPE DECISION above.
- Batch 031 done (FIRST count-prioritized): 44 grounded / 56 skipped; coverage now **90.88%**
  (count 2-3 head). Real towns/counties cluster here vs the institution-heavy file-order tail. Grounds:
  Thirsk Q641274, Bareilly Q213026, York County NB Q1752038, Wellington NZ Q23661, Jaffa Q180294,
  Namaqualand Q1757791, Bunbury WA Q256711, Albany WA Q704257, Wolverhampton Q126269, South Australia
  Q35715, Dalston Q2499366, Beersheba Q41843, Co. Kilkenny Q180231, Hulu Langat Q4251470 (Ulu Langat),
  Temerloh Q2437966, St. Andrew Parish Grenada Q977183, Parramatta Q21319, Baqubah Q270821, Calliaqua
  Q5021973, Grand Forks BC Q984028, Bloemfontein Q37701, Christiania->Oslo Q585, Saint Christopher-
  Nevis-Anguilla Q1637975 (the 1958-83 colony), Southern Province Sierra Leone Q772185, Northern
  Frontier District Kenya Q55643233. Verified reuses (no re-search): Gilbert+Ellice Q1050859, Dindings/
  Dinding->Manjung Q2302576 (x3), Griqualand West Q2547918, Cent. Prov. Kandy->Central Province Ceylon
  Q190716, Simon's Town Q1013370, Timcomalie->Trincomalee Q323873, Nablus Q214178, Co. Durham Q23082
  (x2), Negr Sembilan->Negeri Sembilan Q213893, Anuradhapura Q5724, Cape colonial->Cape Colony Q370736,
  Portsmouth Q72259, German E. Africa Q153963, Selangor Q189710, Tokio->Tokyo Q1490. Skips (56):
  institutions/military/railways, compounds, directional frags, OCR (Pantura, Bassema, Kologha),
  search-resistant (Hanover Square, Stockenstrom, Ndwandwe). Bucks. deferred (didn't verify QID).
- Batch 032 done (count-prioritized): 42 grounded / 58 skipped; coverage now **90.93%**
  (count-2 head). Real towns/regions cluster here. New grounds: Peterborough Q172438 (Old-World
  default over Ontario), Poplar Q123360 (Tower Hamlets London), Saltcoats Q1018756 (N. Ayrshire,
  Old-World default over Saskatchewan), Colesberg Q2232441 (Colesburg, N. Cape), Napier Q203380
  (borough of Napier, NZ), Bhutan Q917 (Bhootan), Maputo Bay Q1134899 (Delagoa Bay), Belgaum
  Q270176, Bajaur District Q804133 (colonial agency=modern district), Wakkerstroom Q1565776,
  Berry Islands Q827173 (Bahamas), Galilee Q83241 (region), Upper Canada Q795427 (period colony,
  distinct from Canada West=Province of Canada), Buxton Q971223 (Derbyshire, Old-World default),
  Mysore Q10086 (city, not kingdom Q1165631), Euphrates Q34589 (river), Mussoorie Q668395,
  Quebec City Q2145 (Queb. City), Kingdom of Nejd and Hejaz Q1756546 (Hejaz and Nejd, period
  polity), Kuala Lumpur Q1865 (K. Lumpor), Sepang Q20460195 (Malaysia town — needed lang=ms to
  surface past Indonesian Sepangs), Riversdale Q2120963 (C.P. = W. Cape town). Reused QIDs (no
  re-search): Kota Bharu Q651131 (Kota Baharu), Teluk Intan Q1317145 (Teluk Anson), Hobart Q40191
  (Hobart Town), Ratnagiri district Q1771768 (Rutnagherry), Kurunegala Q776887 (Kurune gala),
  Mafia Island Q713391, San Francisco Q62 (San Fr'isco), South West Africa Q953068 (S.W.A.
  admstn.), Bloemfontein Q37701 (Bloem. O.R.C.), Western Region Uganda Q2559188 (Western Prov.
  Uganda), Transvaal Province Q190959 (Africa (Transvaal Provl. division)), Tanganyika Territory
  Q158725 (Tanganyika Terry.), Gampola Q8264065 (Gampolla), Northern Frontier District Kenya
  Q55643233, Galle Q319366 (Kachcheri), NWFP Q4412467 (N.W. Frontier Prov.), Quebec Q176 (Prov.
  of Queb. + Quebec Canada), Hopetown Q618063 (Hopetown Division Cape Colony), Sherbro Island
  Q2001267 (Sherbro district). ENDPOINT VERY FLAKY (Peterborough/Poplar/Napier/Belgaum/Cathcart/
  Buxton/Sepang/Mysore/Mussoorie/Kuala Lumpur/Riversdale/Adelaide-obs all empty on first
  descriptive query, most resolved on bare-name retries; Sepang needed lang=ms). Search-resistant
  skips (real but no clean node surfaced): Cathcart (SA Eastern Cape town never surfaced — only
  Glasgow/Victoria/NSW Cathcarts), Regency of Tunis (only French-protectorate Q2017684 + disambig
  page — no clean Ottoman-Beylik period node), Adelaide observatory + Adel. obser. + Royal Alfred
  Observ. Mauritius (observatory nodes wouldn't surface), Theopolis (obscure E. Cape mission).
  Skips (58, dense): initialisms (B.M.P., F.S., C.A.C., S.A.M.C., T.P.D., H. of C., N. Terr.),
  compounds (F.S. and F.M.S., Hejaz reuse aside / S.S. and Hong-Kong, S. Sttlmts. and Malay
  States, Singapore and Labuan, France Belgium and Palestine, Seistan and Kain), military
  (Argyll and Bute/Sutherland Rifles, Egyptian Army, Gold Coast Volunteers, Cape M.R., Glam.
  Artil. Militia, 5th Roy. Dub. Fus., Trinidad Light Horse, Overseas Forces of Canada), institutions
  (Dom. fuel board, Imp./Ottawa Confce., New Providence asylum, inland rev., U.F.O. government),
  forestry conservancy (Eastern Conservancy), directional/generic frags (W. Afr., N.W. Can.,
  West. Prov., N. Divn., Coast Negri Sembilan, S. Eastern division Papua, East Scotland),
  divisions (St. Ann's division Montreal City, Curragh district, Jerusalem-Jaffa district, Santa
  Cruz district of St. Elizabeth), ambiguous bare (St Mary, R. Guiana, Turkish Arabia,
  Russo-Afghan boundary), OCR frags (Seibu, Lavana, Saioniya, Ekel).
- Batch 033 done (count-prioritized): 42 grounded / 58 skipped; coverage now **90.98%**
  (count-2 head). New grounds: Eastbourne Q208262 (Old-World), Fortune Bay Q2879449 (Newfoundland),
  Lindley Q3642967 (Free State), Kitchener Q200166 (Ontario — both bare + "Berlin (Kitchener)"),
  Finland Q33, Nasinu Q26715 (Fiji), Port Dickson Q653801 (P. Dickson), Nadarivatu District
  Q61713485 (Fiji), Parit Buntar Q1973063 (P. Buntar), Mongu Q644799 (Barotse, Zambia), Chipata
  Q856151 (Fort Jameson — the town, distinct from b029 grounding "N. Rhodesia (Fort Jameson)" to
  Northern Rhodesia), Banffshire Q806432 (historic county, Scotland-historic precedent), Reddersburg
  Q2514168 (O.R.C.), Komga Q3644419 (Komgha), Dimbula Q5277189 (Ceylon village), Roebourne Q941071
  (Pilbara WA), Road Town Q179431 (BVI capital), Nicaragua Q811, Tanga Q152902 (Tanzania), Dikoya
  Q5276565 (Ceylon), Estcourt Q985827 (Natal, divn.→town), Gizo Q1236908 (Solomon Is. capital),
  Malayan Union Q976099 (Mal. Union, 1946-48 polity), Rouen Q30974 (Rouen area), Ambepussa Q4064029
  (Ambepusse, Ceylon). Reused QIDs (no re-search): Kew Gardens Q188617 (Royal Botanic Gardens Kew),
  South Caicos Q1814473 (Cockburn Harbour Turks Island), Gilbert and Ellice Islands Q1050859,
  Gilbert Islands Q271876 (Gilbert group — distinct from G&E colony), Straits Settlements Q376178
  (Str. Settlts. + S. Sttlns.), Niger Coast Protectorate Q2566427 (H.B.M.'s ...), Kurunegala Q776887
  (Kurunegalle), Haldummulla Q5641318 (Haldumulla), Mahlabatini Q6395826 (division), Northern Nigeria
  Protectorate Q585408 (N. Provinces Nigeria), Zaria Q147975 (prov.), Mulanje Q1865092 (Mlanje +
  Mlanji district), Downing Street Q192687 (Downing st.), Berbice Q675322 (county of Burbice).
  ENDPOINT VERY FLAKY (almost every descriptive query empty first pass; all resolved on bare-name
  retries). Ambiguous-bare SKIPS (multiple strong candidates, no corpus qualifier): Akim (only
  Akyem ethnonym Q418389 surfaces — per Matabele/Pondos precedent), Bangor (Wales Q234178 vs N.
  Ireland Q806551), Yarmouth (Great Yarmouth vs IoW vs Nova Scotia), Corangamite (shire/federal-
  electorate/parish/lake — colonial county didn't surface), St. Andrew Trinidad, S. Arabia (Aden
  vs Saudi). Skips (58, dense): compounds (S. and N. Rhod., Nigeria and Cameroons, Dominica and St.
  Kitts, Gros Islet and Anse La Range, Ceylon...Java Sumatra and India, London and New York,
  Bechuanaland...Swaziland, Gopang and Kampar, Bahamas and Br. Hond., N. and S. Rhodesia, Cape Colony
  and Basutoland, Avisawalla and Pasyala, S.L. and Gam., G.C. and Lagos, Malta and Rome, Man. and
  N.W.T., France and Mesopotamia, Br. N. Borneo and Labuan, Egypt and Suez defences, Fiji and W.
  Pacific services, Perth to Adelaide route, Gascoyne and Lyons, Br. Somaliland-Ethiopia), institutions
  (Impl./Tech. Inst., Admiralty Somerset house, Melbourne Intl Exhibition, Aden tech. inst., New
  Providence asylum, concentration camp Wynburg, Br. residency New Hebrides), military (Salonika Front,
  Johannesburg mtd. rifles, Egypt/Suez defences), directional/generic/letter (York West, So. district
  Bechuanaland, Eastern Transvaal, North district, Eastern prov., home counties district, district D.
  St. Kitts/Barbados, county of St. George, U. Kelantan [no entity, per b007], P. P. Vryheid [unclear
  prefix], O. C.), ambiguous parishes (St. George's, St. Patrick, St. James' Barbados), OCR/obscure
  (Malya Sukumaland, Millwood Knysna, Klipdam, Lytton, Estcourt aside).
- Batch 034 done (count-prioritized, **300-entry triple batch** = the user's "next 300" request):
  123 grounded / 177 skipped; coverage now **91.12%** (count-2 head; all entries count 2 — the
  count>=3 head is now exhausted). ~50 of the 123 were zero-MCP reuses of already-grounded QIDs
  (kach./district/province/country-qualifier variants + OCR variants: N.Eliya/N'Eliya kach.→Nuwara
  Eliya, Domincia→Dominica, S'pre/B.S.Sttlmts→Singapore/Straits Settlements, Inauda→Inanda,
  Dindinga→Manjung, Malaya Negapatam→Nagapattinam, prov.Well.→Seberang Perai, etc.). New MCP grounds
  span world cities (Warsaw Q270, Lahore Q11739, Rawalpindi Q93230, Bordeaux Q1479, Brazzaville Q3844,
  Giza Q81788, Gaza City Q47492, Carlisle Q192896, Lincoln Q180057, Rugby Q623765, Toronto Q172),
  SA/Natal towns (Dordrecht E.Cape Q652552, Koffiefontein Q2460230, Thaba'Nchu Q1256430, Barkly East
  Q808291, Peddie Q3642191 [Fort Peddie], Ubombo Q7876579, uMlalazi LM Q311805 [Umlalazi district]),
  Malaya/Borneo (Alor Gajah Q4734629, Pekan Q3235637, Raub Q2352205, Kapit Q2219731, Kuantan Q817578,
  Kuala Kangsar Q1790832 [K.Kangear], Tanjong Pagar Q868368, Jerejak Q13639254, Kennedy Town Q3497036),
  Africa (Iringa District Q1888339, Moyamba District Q597538, Lüderitz Q159325 [Luderitzbucht], Ebute
  Metta Q5332126, Ilesa Q763595, Bende Q49101286, Harar Q190184, Magadi Q7193354, Mzimba District
  Q1045435 [Mombera], Acholiland Q1779859, Kweneng District Q57599, MacCarthy Island Q224775), Fiji
  (Namosi Q1365295, Nggela Islands Q513066), Canada (Orillia Q2373358, Carbonear Q2937956, Lunenburg
  NS Q105441), Caribbean/Guyana (New Amsterdam Q923811, Cayo District Q508773 [Cayo+El Cayo], Crooked
  Island Q1140993, New Providence Q858513, Curepipe Q1002525, Robben Island Q192493). **Historical-
  entity-rule picks** (period node over modern): Tigray Province Q1974228 (not modern region), Phuket
  former Siam circle Q108180040, Dutch East Indies Q188161 (Netherlands Indies + N.E.I. — NOT the
  memorized Q188712), Surinam Dutch colony Q7646305 (Dutch Guiana), German South-West Africa colony
  Q153665 (G.S.W.Africa), Upper Egypt region Q203751 (corrects memorized Q1810094 — ALWAYS search,
  don't trust memory), Borno State Q130626 (Bornu, province→state successor), Pomeroon-Supenaam Q680382
  (Pomeroon district, district→region). Geo features: North Sea Q1693. Endpoint VERY flaky again
  (almost every descriptive query empty first pass; all resolved on bare-name retries). Search-resistant
  SKIPS (real but no clean node surfaced): St. George's Bermuda (3 misses — Grenada's Q41547 is a
  FALSE reuse, different place), Sussex New Brunswick (3 misses), Springlands Guyana (only NZ/Aus
  surface), Gcalekaland (only insects+ruler, per Damaraland precedent). 177 skips are the usual dense
  tail: compounds (Selangor and Penang, India and Ceylon, Mannar and Mullaitivu…), initialisms
  (N.W., S.A., N.F.D., G.W.Rly., P.M.G., L.S.T.M…), military (Royal Engineers, K.S.L.I., Egyptian
  army…), institutions/exhibitions (Australian Museum, Sydney/Melbourne/Calcutta Exhibition, Malta
  public library…), forestry conservancies (Midland/Eastern Conservancy Cape Colony, per precedent),
  letter/directional districts (district "D" Dominica, Larut Perak North, Umgeni division…), ambiguous
  bare (Lambton, Picton, Ivanhoe, Caroni, Queen's co., Ciskei [bantustan, wrong-era]). QID VERIFIER
  RUN after batch (1,369 QIDs, all 70+ new picks OK; the 10 flags are all pre-existing — Egypt manifest,
  Inns of Court, Naparima/N.Cameroons/NFD stubs).
- NOTE: `kg_ground_mcp.py record` appends to `/tmp/results.jsonl`; before recording,
  confirm `wc -l` matches the batch size — a stale file from a prior session will
  double it. Record only the new tail (`tail -n +<N+1>`).
- Cache schema = `col_match/kg/ground.py:make_row`; `emit.py` reads `gcache[place].qid`.
- Colonies are pre-grounded from the manifest (`kg_join_manifest.py`); MCP handles
  only the town tail in `data/kg/places_worklist.mcp.jsonl`. See
  [[place-grounding-pipeline]] memory.
