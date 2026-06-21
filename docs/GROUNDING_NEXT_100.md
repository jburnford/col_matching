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

### 1. Get the pending list
```
cd ~/col_matching
python3 kg_ground_mcp.py pending --n 100 > /tmp/pending.jsonl
wc -l /tmp/pending.jsonl
```
Each line: `{query, count, context_resolved, variants:[...]}`. Work top (highest
count) down. If 0 lines, grounding is complete — stop and tell the user.

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

## State (update after each run)
- Branch: `kg-place-canonicalization` (not pushed).
- Latest: **batch 012 done — coverage 88% of 168,301 mentions** (see detail below).
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
- NOTE: `kg_ground_mcp.py record` appends to `/tmp/results.jsonl`; before recording,
  confirm `wc -l` matches the batch size — a stale file from a prior session will
  double it. Record only the new tail (`tail -n +<N+1>`).
- Cache schema = `col_match/kg/ground.py:make_row`; `emit.py` reads `gcache[place].qid`.
- Colonies are pre-grounded from the manifest (`kg_join_manifest.py`); MCP handles
  only the town tail in `data/kg/places_worklist.mcp.jsonl`. See
  [[place-grounding-pipeline]] memory.
