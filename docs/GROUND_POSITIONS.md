# Grounding career-event POSITIONS to occupation/role types

Resumable loop for the **role / occupation layer** of the KG. Jim's rule: ground
the JOB TYPE to a Wikidata occupation/position QID where one matches (e.g.
`judge` → **Q16533**); mint a stable internal id `colkg:<role>` where Wikidata
has no matching job type. Seniority/status qualifiers (acting, assistant, deputy,
senior, grade I) are NOT roles — they ride on the edge.

**Resume prompt after /clear:**
> Ground the next 150 positions — follow docs/GROUND_POSITIONS.md

## Pipeline (all at repo root)

1. `kg_role_norm.py` — shared parser `parse_position(raw) -> (base_role, modifiers, category)`.
   Strips leading qualifiers (acting/asst/deputy/senior/junior/additional/temporary/
   grade), expands abbreviations (mo→medical officer, d.o→district officer, supt→
   superintendent, res→resident, prov→provincial…), keeps distinctive role words
   (chief, colonial, principal, provincial, resident, puisne). Control buckets:
   `_military_service` (on military service / ranks-in-service), `_unknown`
   (empty / bare-qualifier extractions), `_honour`.
2. `kg_position_worklist.py` → `data/kg/position_worklist.jsonl`
   `{institution:<base_role>, type:<category>, count, person_ids, examples}`.
   **59,516 distinct base-roles / 188,826 events**; control: _military_service=5,293,
   _unknown=4,342. Head is concentrated: top 200 = 37% of mentions, top 500 = 45%,
   top 1000 = 51%.
3. **Grounding** — the env-overridable `kg_ground_institutions.py` harness serves
   this worklist. ALWAYS export first:
   ```bash
   export COL_WORK=data/kg/position_worklist.jsonl
   export COL_CACHE=data/kg/role_grounding.jsonl
   python3 kg_ground_institutions.py pending --n 150   # top uncached, count-desc
   python3 kg_ground_institutions.py record /tmp/roles.jsonl   # merge decisions
   python3 kg_ground_institutions.py stats
   ```
   Skip control buckets (`_*`). Cache rows:
   `{institution, type, id, label, instance_of, country_qid, source, match_type}`,
   id = `Q…` or `colkg:<Slug>`. source = mcp / reuse / internal.
4. `kg_emit_roles.py` → `roles.jsonl` + `role_edges.jsonl`. Auto-internal-mints any
   uncached non-control role (so the tail is covered WITHOUT a bulk internal-tail
   pass — grounding only needs to record QIDs for the head). Modifiers emitted as
   `edge.modifiers` (list); one edge per career event with position_raw/year.
5. `kg_dedup_nodes.py` — run after emit (folds case/spacing variants, remaps edges).

## Disposition (per base-role)

- **mcp** — bare role → Wikidata occupation/position QID. Verify via `get_statements`:
  accept if P31 is *occupation* (Q12737077), *profession*, *position* (Q4164871),
  or *public office* / a subclass. Examples likely to ground:
  judge Q16533 · barrister Q808967 · solicitor · physician/medical practitioner ·
  surgeon · civil engineer · land surveyor Q294126 · architect · accountant Q43845 ·
  auditor · clerk Q1238570 · teacher · police officer · magistrate · chaplain ·
  veterinary surgeon · colonial administrator Q17765219 · colonial governor.
- **reuse** — abbreviation/variant of an already-grounded QID (zero MCP).
- **internal** `colkg:<role>` — colonial-specific roles with no WD job type
  (district officer, district commissioner, cadet, government agent, puisne judge if
  no QID, education officer, administration officer, provincial commissioner, …).
  These are the bulk; emit mints them automatically — only ground the ones that
  genuinely map to a WD occupation.

**4-point 0-FP accept rule** (mirrors the institution pass): (1) query the bare
role, retry once on empty; (2) accept on type if any P31 is an occupation/position
class; (3) sanity-check the sense matches colonial service (judge=Q16533, not a
film/ship); (4) no candidate passes → keep internal.

MCP discipline (global CLAUDE.md): WikidataMCP **vector** search only, ≤5 calls per
message, retry the bare name once on empty.

## Triage

Ground count-desc head (top few hundred roles ≈ half of all mentions). Don't grind
the count-1 tail — emit internal-mints it. Don't ground control buckets. An
internal→QID upgrade pass can run later (cf. the org layer).

## Notes / gotchas

- Modifiers are EDGE-level. "acting colonial secretary" + "colonial secretary" →
  one node `colonial secretary`, edge carries `["acting"]`. Don't make seniority
  variants separate roles.
- `_military_service` (5,293 events) → single node `colkg:military_service` (a
  career state, not a job). `_unknown` (4,342) → role_id=null, position_raw kept
  for later review. Refine `kg_role_norm.py` ABBR/RESIDUAL sets to shrink `_unknown`.
- Some heads are ranks captured bare (captain/lieutenant) — decide per Jim whether
  to ground to military-rank QIDs or fold into military_service.
- The harness `internal`/`internal-tail`/`ambiguous` subcommands also work here,
  but `ambiguous` is rarely needed for occupations (ground generics to the general
  occupation, e.g. bare "secretary" → secretary occupation).
