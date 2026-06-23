# Grounding institutions (education first, then employers/orgs) — resumable loop

Goal: ground the **count≥2 head** (~1,757 institutions, ~88% of education mentions)
to Wikidata QIDs via MCP vector search; everyone sharing an ungrounded
institution still links via a minted **internal id** `colkg:<Slug>`.

## State
- Worklist: `data/kg/education_worklist.jsonl` (4,983 distinct, 27,238 mentions;
  rebuild: `python3 kg_education_worklist.py`).
- Cache: `data/kg/institutions_grounding.jsonl` (keyed by `institution` surface).
- count==1 tail (3,211) already minted internal ids (`internal-tail --max-count 1`).
- Wikidata-grounded so far: 15 (Univ London/Edinburgh/Cambridge/Glasgow/Oxford/
  Aberdeen-pending, Trinity Dublin/Cambridge, 4 Inns of Court, King's London,
  New College/Brasenose/Balliol Oxford) — already 4,408 mentions.

## Batch = 250 institutions per session
One batch grounds the next **250** count-desc institutions (≈50 assistant
messages × 5 MCP calls — the rate limit). At ~1,757 head institutions, that's
~7 batches. After each batch: `stats`, then `record` is already persisted to the
on-disk cache (survives /clear); optionally `git add -f` the cache for backup.
Resume prompt: **"Ground the next 250 institutions — follow docs/GROUND_INSTITUTIONS.md"**.

## Loop (≤5 MCP calls per assistant message — rate limit)
1. `python3 kg_ground_institutions.py pending --n 15` → top uncached, count-desc.
2. MCP `search_items` each (bare name first; the endpoint is INTERMITTENT —
   descriptive queries often return empty, retry bare; whole batches sometimes
   need a retry pass). Pick the QID whose description is the educational
   institution (university/college/school/Inn), NOT a building/boat-club/painting.
3. Write rows to a tmp jsonl and `record`:
   `{"institution":<surface>,"type":..,"id":"Q..","label":..,"instance_of":[..],"country_qid":..,"source":"mcp","match_type":"mcp_verified"}`
4. If no real Wikidata entity exists (obscure local school, or an org like
   "Ceylon Police"): mint an internal id —
   `echo "Ceylon Police" | python3 kg_ground_institutions.py internal -`
   → `colkg:Ceylon_Police` (all people sharing it link to that node).
5. Repeat. `stats` for coverage. Every ~10 batches, eyeball the cache for
   wrong-type grabs (building/journal/boat-club QIDs).

## Disambiguation notes
- Ambiguous bare colleges ("King's College", "Queen's College", "Trinity College"
  w/o parent) — check the worklist `examples`; prefer the parented form's QID by
  the dominant context, else flag.
- "Royal College" = real colonial schools "Royal College, Mauritius / Colombo" —
  ground per location or mint `colkg:Royal_College_Mauritius` etc.
- Inns of Court, universities, Oxbridge colleges, Sandhurst/Woolwich, famous
  public schools all HAVE QIDs — ground them; the long tail of local grammar
  schools mostly won't (internal ids).

## Then
- `python3 kg_ground_institutions.py emit` → `graph_stage3/institutions.jsonl`
  (nodes) + `education_edges.jsonl` (person→institution).
- NEXT entity class after education = **employer/org institutions** (the 3,488
  ungrounded `org` event places: railways, police, departments) — same harness,
  same internal-id scheme (Ceylon Police → `colkg:Ceylon_Police`).
