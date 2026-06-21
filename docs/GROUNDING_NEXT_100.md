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
- NOTE: `kg_ground_mcp.py record` appends to `/tmp/results.jsonl`; before recording,
  confirm `wc -l` matches the batch size — a stale file from a prior session will
  double it. Record only the new tail (`tail -n +<N+1>`).
- Cache schema = `col_match/kg/ground.py:make_row`; `emit.py` reads `gcache[place].qid`.
- Colonies are pre-grounded from the manifest (`kg_join_manifest.py`); MCP handles
  only the town tail in `data/kg/places_worklist.mcp.jsonl`. See
  [[place-grounding-pipeline]] memory.
