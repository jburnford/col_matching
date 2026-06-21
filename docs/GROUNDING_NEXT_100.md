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
- NOTE: `kg_ground_mcp.py record` appends to `/tmp/results.jsonl`; before recording,
  confirm `wc -l` matches the batch size — a stale file from a prior session will
  double it. Record only the new tail (`tail -n +<N+1>`).
- Cache schema = `col_match/kg/ground.py:make_row`; `emit.py` reads `gcache[place].qid`.
- Colonies are pre-grounded from the manifest (`kg_join_manifest.py`); MCP handles
  only the town tail in `data/kg/places_worklist.mcp.jsonl`. See
  [[place-grounding-pipeline]] memory.
