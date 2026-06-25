# Career-fact layer (fused career events)

`kg_emit_career_facts.py` → `data/kg/graph_stage3/career_facts.jsonl`

**Why:** the KG stores each career fact across three files that all join on
`(person_id, seq)` — the spine `career_events.jsonl` (place/colony/year/acting/
position), `role_edges.jsonl` (grounded ROLE id), `employment_edges.jsonl`
(grounded EMPLOYER org id). This emitter denormalises them into ONE self-contained
statement per event so the graph is queryable without a 3-way join:

> person — held [role_id] (acting?) — at [org_id] — in [place_qid / colony_qid] —
> during [year_start .. year_end]

**One row per spine event (189,918).** Fields: `person_id, seq, role_id, role_label,
role_modifiers, is_acting, org_id, org_label, org_type, place_qid, place_label,
colony_qid, colony_label, year_start, year_end, position_raw, role_source, org_source`.

**Coverage (of 189,918 events):**
- role grounded 90% (38% Wikidata QID / 52% internal `colkg:`)
- place_qid 73% · colony_qid 55% · dated (year_start) 95%
- employer org_id 2% (inherent — most bios name no employer, only a place)
- **complete role+place+time: 64% (121,160 events)**

**NOT fused here:** honours, qualifications, education edges are keyed by
`person_id` only (no `seq`) — they are person-level attributes, not properties of a
single career event, so they stay as their own person→X edge files.

Read-only and idempotent: rerun any time after the layer emits change. This is the
natural input for a Neo4j load or a CIDOC-CRM / RDF export (events → E7 Activity
with P14 carried_out_by / P4 has_time-span / P7 took_place_at).
