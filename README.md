# Imperial Careers — an open knowledge graph of the Colonial & India Office Lists

A grounded, person-career **knowledge graph** built from the printed
*Colonial Office List* (1862–1966) and *India Office List* (1886–1947): tens of
thousands of imperial officials, the posts they held, where and when they
served, where they were educated, and the honours they received — with people,
places, roles and institutions linked to **Wikidata** wherever possible.

🌍 **Explore the interactive atlas:** <http://jimclifford.ca/col_matching/>

## Open data — free for anyone to use

The data in this repository is dedicated to the **public domain under
[CC0 1.0](LICENSE-DATA)** — copy it, remix it, build on it, for any purpose,
no permission needed. The source code is **[MIT](LICENSE)** licensed.

Attribution is *requested but not required*. If it helps your research or
teaching, a citation is appreciated (see [Citing this data](#citing-this-data)).

**You do not need to run any pipeline to use the data.** The finished graph is
committed directly to this repo under `data/{kg,iol}/graph_stage3/` as plain
JSONL — clone it and you have everything. Two ready-to-load databases are
documented below; or just read the JSONL files directly in Python, R, pandas,
DuckDB, etc.

| corpus | persons | career events | grounded to Wikidata |
|--------|--------:|--------------:|---------------------:|
| Colonial Office List (`data/kg`) | 27,739 | 180,830 | 1,119 persons |
| India Office List (`data/iol`)   | 18,233 | 120,307 | *(person grounding deferred)* |

Places, roles, organisations, schools and honours are grounded too: e.g. the CO
graph resolves ~131k events to a Wikidata place QID and links 1,518 schools and
20 honour types to Wikidata.

---

## Quick start: load the graph

```bash
git clone <this repo> && cd col_matching
pip install -e .
```

`COL_KG_OUT` selects which corpus to load (`data/kg` = Colonial Office List,
`data/iol` = India Office List). Everything below works for either.

### Option A — LadybugDB (embedded, zero setup)

LadybugDB is an embeddable Cypher graph database (a Kuzu fork) — no server, the
database is a single local file. This is the fastest way to start querying.

> ⚠️ `pip install ladybug` here gets the **graph database**
> (github.com/lbugdb/lbug), *not* the unrelated "Ladybug Tools" package of the
> same import name.

```bash
pip install ladybug pandas pyarrow

COL_KG_OUT=data/kg  python3 kg_load_ladybug.py     # -> data/kg/ladybug_db
COL_KG_OUT=data/iol python3 kg_load_ladybug.py     # -> data/iol/ladybug_db
```

```python
import ladybug
conn = ladybug.Connection(ladybug.Database("data/kg/ladybug_db"))
print(conn.execute(
    "MATCH (p:Person)-[:HAS_EVENT]->(e:CareerEvent)-[:EVENT_PLACE]->(pl:Place) "
    "RETURN pl.label, count(*) AS n ORDER BY n DESC LIMIT 5"
).get_as_df())
```

### Option B — Neo4j

Loads the same graph into any Neo4j over Bolt. **It targets a local Neo4j
(`bolt://localhost:7687`) by default and only ever creates nodes carrying an
`:ICKG` marker label**, so it is safe to run against a shared database — it will
not disturb other data, and the two corpora coexist (each tagged
`ICKG_corpus = "co" | "iol"`).

```bash
pip install neo4j      # already a dependency of `pip install -e .`

# point at your Neo4j (defaults shown):
export KG_NEO4J_URI=bolt://localhost:7687
export KG_NEO4J_USER=neo4j
export KG_NEO4J_PASSWORD=neo4j

COL_KG_OUT=data/kg  python3 kg_load_neo4j.py       # Colonial Office List
COL_KG_OUT=data/iol python3 kg_load_neo4j.py       # India Office List
```

Re-running clears and reloads that corpus; pass `--keep` to append instead. In
Neo4j the node labels are prefixed (`:ICKG_Person`, `:ICKG_Place`, …):

```cypher
MATCH (p:ICKG_Person {ICKG_corpus:'co'})-[:HAS_EVENT]->(e:ICKG_CareerEvent)-[:EVENT_PLACE]->(pl:ICKG_Place)
RETURN pl.label, count(*) AS n ORDER BY n DESC LIMIT 5
```

Both loaders print node/edge counts and run validation queries when they finish.

---

## Graph model (reified career events)

Each career event is reified as its own node, so people, roles, places and time
are all independently traversable:

```
(Person)-[:HAS_EVENT]->(CareerEvent)-[:EVENT_ROLE]->(Role)
                        (CareerEvent)-[:EVENT_PLACE]->(Place)     // where served
                        (CareerEvent)-[:EVENT_COLONY]->(Place)    // colony/jurisdiction
(Person)-[:EDUCATED_AT]->(Institution)
(Person)-[:EMPLOYED_BY]->(Organisation)
(Person)-[:RECEIVED]->(Honour)
(Person)-[:HOLDS_QUAL]->(Qualification)
```

`CareerEvent` carries `year_start` / `year_end` / `is_acting` / `position_raw`.
Every node carries a grounded id — a Wikidata `Q…` QID where grounded, otherwise
a stable internal `colkg:<slug>` — plus a human-readable label. `Person` nodes
additionally carry `wikidata_qid` / `wikidata_label` when grounded.

### The data files (`data/{kg,iol}/graph_stage3/`)

One JSON object per line. The loaders read these; you can too.

| file | what it is |
|------|------------|
| `persons.jsonl` | one row per resolved person (surname, given names, birth year, # attestations) |
| `career_events.jsonl` | the event spine — one row per person-posting, with year/place/colony |
| `role_edges.jsonl` | grounded role/position per event (`person_id` + `seq`) |
| `career_facts.jsonl` | denormalised flat view (event ⋈ role) — handy for a quick read |
| `places.jsonl` / `roles.jsonl` / `organisations.jsonl` / `institutions.jsonl` / `honour_nodes.jsonl` | grounded node tables |
| `employment_edges.jsonl` / `education_edges.jsonl` / `honour_edges.jsonl` / `qualification_edges.jsonl` | person-level edges |
| `person_grounding.final.jsonl` | person → Wikidata QID (zero-false-positive set) |
| `kg_stats.json` / `v3_manifest.json` | counts and per-layer grounding coverage |

---

## Citing this data

If you use this in research or teaching, please cite the archived snapshot
(which carries a DOI):

> Jim Clifford. *Imperial Careers: a grounded person-career knowledge graph of
> the Colonial Office List and India Office List.* Dataset.
> Zenodo DOI: **`<add after first release>`**

Each tagged GitHub release is automatically archived to Zenodo and minted a DOI
(see [Releasing a citable snapshot](#releasing-a-citable-snapshot)). Until the
first release, cite this repository URL.

---

## How the graph was built (provenance)

The graph is the downstream product of a longer pipeline; you don't need any of
it to *use* the data, but here is the lineage:

1. **OCR** of the printed Lists (raw CO text is committed under `raw_ocr/`).
2. **Person resolution** — the printed "Record of Services" biographies are
   segmented, deduplicated across editions, and compiled into per-person
   biographies with per-fact edition provenance (`col_match/services/`).
3. **Structuring** — each biography is parsed (rules tier + LLM fallback) into
   structured career events.
4. **Grounding** — people, places, roles, schools, organisations and honours
   are linked to Wikidata using semantic (vector) search plus zero-false-
   positive verification gates (`kg_ground_*.py`, `verify_*_qids.py`).
5. **Emit** — the grounded graph is written as the `graph_stage3/*.jsonl`
   layers (`kg_emit_stage3.py` and the per-layer emit scripts).

`COL_KG_OUT` reroots the entire pipeline, so the same scripts build either
corpus. The grounding caches (`*_grounding.jsonl`) are committed and reused, so
rebuilding the JSONL needs no re-grounding. Design notes and per-stage loops are
in [`docs/`](docs/) (start with `docs/LADYBUG_DB.md`, `docs/CAREER_FACTS.md`).

### Relationship to the production pipeline

This repo is the *matching / knowledge-graph* layer. It is **read-only** against
the separate `col_pipeline` production Neo4j graph that supplies the extracted
`COL_Official` records — it never writes to that graph. See
[`docs/data_contract.md`](docs/data_contract.md) for that seam. (The `kg_load_*`
loaders here build a *separate* database from the published JSONL and never
touch production.)

## Releasing a citable snapshot

To mint a DOI for a version of the data:

1. Connect the GitHub repo to <https://zenodo.org> once (Zenodo → GitHub, flip
   the repo on).
2. Cut a GitHub release / tag (e.g. `v1.0-data`). Zenodo archives the repo
   (data included) and mints a DOI automatically.
3. Paste the DOI into the badge above and the citation block.
