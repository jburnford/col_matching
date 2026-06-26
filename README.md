# col_matching

Experimental repo for **person-matching / career-chain resolution** in the
Colonial Office List corpus, isolated from OCR and relationship extraction so
it can iterate on its own cadence (including LLM-assisted matching with Fable).

This repo **reads** from the same production Neo4j graph that `~/col_pipeline`
builds, at the `COL_Official` seam. It is **read-only** against that graph: it
never writes nodes, edges, or properties to production. Any matches it produces
are written to a *separate* experiment store or exported as files for review —
never committed back to the publication graph without explicit sign-off.

## Boundary

```
OCR  (archive-olm-pipeline)            pixels → text
  │
Extraction (col_pipeline: col.extract) text → COL_PersonRecord + institutions
  │
  ▼  ── seam: COL_Official + its records + POSSIBLE_MATCH edges (read-only)
Matching (THIS REPO)                   stints → coherent careers → (later) Wikidata
```

`col_pipeline` stays the single, publication-ready, end-to-end repo and the
source of truth for the graph. This repo is downstream of its `COL_Official`
layer and depends on nothing in its extraction/OCR code — the contract is the
graph schema, not a Python import.

## What it consumes

See [`docs/data_contract.md`](docs/data_contract.md) for the exact nodes,
edges, properties, and quarantine filters. In short: each candidate cluster is
a connected component of `POSSIBLE_MATCH` edges over `COL_Official` stints;
each stint's evidence is gathered by traversing `RECORD_OF` back to its
(non-quarantined) `COL_PersonRecord`s.

## Status

Phase 1 (services-section pipeline) is built and run; see
`docs/approach.md` and `data/services/reports/full_run_report.md`.

The printed "Record of Services" biographical sections (1883–1966) are
segmented, deduplicated across editions, parsed (rules tier ~77%, Gemini
batch fallback for the rest), and compiled into ~30k per-person biographies
with per-fact edition provenance. Careers are then built by **record-level
attachment**: each biography claims the annual staff-list records it predicts,
year by year, in the same volumes (`col_match/services/attach.py`). Stint
matching (`match.py`) is retained as an independent cross-check. Both run at
zero measured false positives against 543 hand-verified careers.

```
col-services segment      # locate + split the services sections (62 volumes)
col-services dedup        # 199k entry instances -> 42k distinct versions
col-services parse_rules  # deterministic tier (77%)
col-services llm_submit / llm_poll / llm_escalate   # Gemini batch fallback
col-services compile      # versions -> biographies (conservative merging)
col-services fetch_graph  # read-only cache of officials + records + edges
col-services attach       # biographies claim annual records (primary)
col-services match        # stint-level cross-check
col-services coverage     # coverage report
col-services eval_gold / check_twins                # evaluation harness
```

Not present yet (by design): the Fable dossier adjudication harness for the
~13k below-evidence-bar candidates, and any write path anywhere.

## Setup

```bash
cd ~/col_matching
pip install -e .
cp .env.example .env   # or rely on ~/textasdatacolonialofficelist/.env (auto-loaded)
```

Credentials resolve the same way as `col_pipeline` (`NEO4J_PROD_URI` /
`NEO4J_URI`, `NEO4J_PASSWORD`, …), falling back to the sibling repo's `.env`,
so there's a single credential source.

## Knowledge graph (LadybugDB)

The grounded person-career knowledge graph for **two corpora** — the Colonial
Office List (`data/kg`) and the India Office List (`data/iol`) — is emitted as
JSONL layers under `data/<corpus>/graph_stage3/` and loaded into an embedded
**LadybugDB** (a Kuzu-fork, Cypher) database.

Every corpus roots its outputs on the `COL_KG_OUT` environment variable
(default `data/kg`), so the same scripts build either graph. The JSONL graph
layers are committed; the `*/ladybug_db` directories are **not** (they're
~50–70 MB binaries, regenerated deterministically from the JSONL).

### Build the database

```bash
# loader deps (in addition to `pip install -e .`).
# NB: `ladybug` here is the embeddable graph DB (github.com/lbugdb/lbug, a Kuzu fork),
# NOT the "Ladybug Tools" architecture package of the same import name.
pip install ladybug pandas pyarrow

# Colonial Office List  -> data/kg/ladybug_db
COL_KG_OUT=data/kg  python3 kg_load_ladybug.py

# India Office List     -> data/iol/ladybug_db
COL_KG_OUT=data/iol python3 kg_load_ladybug.py
```

Each run drops any existing DB and rebuilds from scratch via Parquet `COPY FROM`,
then prints node/edge counts and runs validation queries. Current scale:

| corpus | persons | career events | persons→Wikidata |
|--------|--------:|--------------:|-----------------:|
| Colonial Office List (`data/kg`) | 30,080 | 189,775 | 925 |
| India Office List (`data/iol`)   | 20,362 | 129,090 | 0 *(person grounding deferred)* |

### Graph model (reified career events)

```
(Person)-[:HAS_EVENT]->(CareerEvent)-[:EVENT_ROLE]->(Role)
                        (CareerEvent)-[:EVENT_PLACE]->(Place)
                        (CareerEvent)-[:EVENT_COLONY]->(Place)
(Person)-[:EDUCATED_AT]->(Institution)
(Person)-[:EMPLOYED_BY]->(Organisation)
(Person)-[:RECEIVED]->(Honour)
(Person)-[:HOLDS_QUAL]->(Qualification)
```

Nodes carry their grounded id (a Wikidata `Q…` QID where grounded, else a stable
internal `colkg:<slug>`) plus a label. `CareerEvent` carries
`year_start`/`year_end`/`is_acting`/`position_raw`. The loader synthesizes each
reified event from `career_events.jsonl` joined to `role_edges.jsonl` (on
`person_id`+`seq`); employers are person-level (`employment_edges.jsonl`).

### Query it

```python
import ladybug
conn = ladybug.Connection(ladybug.Database("data/iol/ladybug_db"))
print(conn.execute(
    "MATCH (p:Person)-[:EMPLOYED_BY]->(o:Organisation) "
    "RETURN o.label, count(*) AS n ORDER BY n DESC LIMIT 5"
).get_as_df())
```

### Regenerating the JSONL from scratch (optional)

Rebuilding the DB needs only the committed `graph_stage3/*.jsonl`. To regenerate
those layers from the structured corpus (after re-grounding or re-dedup), re-run
the emit chain rooted on the same `COL_KG_OUT`: `kg_emit_stage3.py` (core graph)
then the per-layer worklist+emit scripts (`kg_org_worklist.py` →
`kg_ground_institutions.py emit`, `kg_position_worklist.py` → `kg_emit_roles.py`,
`kg_parse_education.py worklist` → `kg_ground_institutions.py emit`,
`kg_honour_worklist.py` → `kg_emit_honours.py`). Grounding caches
(`*_grounding.jsonl`) are committed and reused — no re-grounding needed.
