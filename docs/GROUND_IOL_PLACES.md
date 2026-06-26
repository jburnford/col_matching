# Ground the IOL place tail (resumable MCP loop)

Self-contained runbook for grounding the India Office List place worklist to
Wikidata QIDs via the **Wikidata MCP vector search** (per the `/place-disambig`
skill: `search_items` → `get_statements`, ≤5 calls/message; NEVER the REST
`wbsearchentities` API). Survives a context clear — paste the resume prompt and
follow these steps.

## State
- **Corpus / output root:** `data/iol/` (always export `COL_KG_OUT=data/iol`).
- **Cache (the grounded result, resumable):** `data/iol/places_grounding.jsonl`
  — already seeded with 620 surfaces + the 1937-KG QIDs (`match_type:seed_iol1937`).
- **Worklist:** `data/iol/places_worklist.grounding.jsonl` (3,570 queries /
  25,816 mentions, count-descending). Institutions/noise are in
  `places_worklist.flagged.jsonl` (never ground these).
- **Batch provenance:** write each batch's results to
  `data/iol/mcp_grounding_batchNNN.jsonl` before recording.

## The loop (one batch = ~50 queries)
1. **Get the next pending queries** (skips anything already grounded/seeded):
   ```
   COL_KG_OUT=data/iol python3 kg_ground_mcp.py pending --n 50
   ```
   Each line: `{"query": "...", "count": N, "variants": [...]}`. Work top-down
   (highest count first = most mentions grounded per call).
2. **Look up each `query` via the Wikidata MCP** (follow `/place-disambig`):
   `mcp__wikidata__search_items(query)` → pick the contextually-correct India
   place → `mcp__wikidata__get_statements(qid)` to verify it is geographic
   (P31 place type / P17 country / P625 coords). ≤5 lookups per message; the
   endpoint is intermittent — retry the bare name once on an empty result.
   - Indian historical provinces are common in the tail: **N.W. Provinces /
     N.W. Prov. and Oudh** = North-Western Provinces (and Oudh) (pre-1902,
     became United Provinces); **United Prov.** = United Provinces. Ground to
     the historical entity when one exists.
   - Skip (leave for `.flagged`/ungrounded) anything that is an office,
     department, court, regiment, or railway — not a place.
3. **Write the batch results** as JSONL to `data/iol/mcp_grounding_batchNNN.jsonl`,
   one object per query:
   ```json
   {"query":"North-Western Provinces","qid":"Q...","label":"...","country_qid":"Q668","p131_qid":null,"instance_of":["..."],"has_coords":true,"match_type":"mcp_verified"}
   ```
   For a query that genuinely has no Wikidata place, write `{"query":"...","qid":null,"match_type":"ungrounded"}`.
4. **Record into the cache** (fans each grounded query out to all its surface variants):
   ```
   COL_KG_OUT=data/iol python3 kg_ground_mcp.py record --results data/iol/mcp_grounding_batchNNN.jsonl
   ```
5. Repeat. Every ~10 batches, re-emit to watch coverage climb:
   ```
   COL_KG_OUT=data/iol python3 kg_emit_stage3.py --corpus data/iol/llm_struct_corpus.stage3.jsonl --out data/iol/graph_stage3
   ```

## Targets / stopping point
- Baseline at v1 (seed + canonicalize bridge, no MCP): **73.9% of placed events grounded.**
- The count-descending head is dense with real high-frequency provinces/cities
  → fast early gains. As with the CO List, the deep singleton tail (districts,
  OCR fragments) hits a ROI cliff ~90%+; stop there and archive the residue.
- Optional: `kg_resolve_context_places.py` for the 10 ambiguous forms (C.P. /
  directional provinces) — small, do later.

## Resume prompt (paste after /clear)
> Ground the next 100 IOL town/province places — follow docs/GROUND_IOL_PLACES.md
> (export COL_KG_OUT=data/iol first).

See `[[iol-kg-build]]` memory for the full pipeline state.
