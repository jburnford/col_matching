# Data contract — the `COL_Official` seam

This is the exact, read-only interface `col_matching` consumes from the
production Neo4j graph built by `col_pipeline`. If the graph schema changes
upstream, this document and `col_match/graph.py` are what must be updated.

Source of truth for the upstream schema: `~/col_pipeline/docs/schema.md`
(plus the live graph at `bolt://206.12.90.118:7687`). Where the two disagree,
the live graph wins — see **Known drift** below.

## What we read

### 1. Candidate clusters — `POSSIBLE_MATCH`

A candidate cluster is a connected component of `COL_Official` nodes joined by
`POSSIBLE_MATCH` edges whose `uncertainty` is at or below a chosen threshold.

```
(:COL_Official)-[:POSSIBLE_MATCH {
  uncertainty: float,      # 0.0 = certain match … 1.0 = certain non-match
  method: str,             # automated_linking | cross_colony_linking
                           #   | ml_discovery | gazette_discovery
  ml_uncertainty: float,   # GradientBoosting score (present on ~67% of edges)
  ml_probability: float,   # (present on ~67% of edges)
  chain_validated: bool,   # (present on ~58% of edges)
  domain_match, name_specificity, gap_years, editions_gap, editions_missed,
  a_editions, b_editions, a_last_position, a_last_dept,
  b_first_position, b_first_dept,    # per-edge evidence (some partial-coverage)
  score_version: str, date_created: str
}]->(:COL_Official)
```

There is **no** `confidence` property on `POSSIBLE_MATCH` (it's on
`COL_PersonRecord`-stage provenance, not here). Verified against the live graph
2026-06-11.

`col_matching` v1 **reuses col_pipeline's blocking** — it adjudicates clusters
the linker/ML already proposed, rather than re-generating candidates. Widening
candidate generation (e.g. surname/initial blocking to surface pairs the
conservative linker never scored) is deliberately deferred.

### 2. Stint identity — `COL_Official`

```
(:COL_Official {
  id: str,                 # IDENTIFIER, e.g. "Metzger, J. M___Sierra Leone___1878"
                           #   = name___colony___first_year (triple underscore)
  name: str,               # surname-first display name (NOT `canonical_name`)
  colony: str,
  first_year: int,
  last_year: int,
  num_editions: int,       # count of editions
  editions: list[int]      # the actual edition years, e.g. [1878, 1879, 1883, …]
})
```

`COL_Official` is the leanest node — the discriminating evidence (honours, rank,
position, department, salary, `canonical_name`, `surname`) lives on the
underlying `COL_PersonRecord`s, not here. **This shape was verified against the
live graph 2026-06-11 and differs materially from `col_pipeline/docs/schema.md`,
which is stale** (see Known drift). Officials are keyed and joined by `id`.

### 3. Per-stint evidence — `RECORD_OF` → `COL_PersonRecord`

For each official, traverse back to its records and collect the evidence a
human (or model) would use to judge whether two stints are the same person:

```
(:COL_PersonRecord {
  name_raw, canonical_name, surname, given_names,
  position_raw, department_raw,
  salary_min, salary_max, salary_currency,
  honors: list[str], qualifications: list[str], military_rank: str | null,
  location: str | null,
  colony, year,
  quarantined: bool | null, quarantine_reason: str | null
})-[:RECORD_OF]->(:COL_Official)
```

## Quarantine filters (MANDATORY)

The graph carries known-bad records flagged but **not** removed. The accessor
must exclude them, or the model reasons over contamination and ghosts:

| Filter | What | Why |
|---|---|---|
| `quarantined = true` | any flagged record (esp. `quarantine_reason = 'governor_chain_ghost'` — 3,563 records, 2,710 still carry `RECORD_OF`) | dead-by-edition-year people; quarantine is a flag, not a downstream filter upstream |
| Aden 1922 | `colony = 'Aden' AND year = 1922` (921 records, ~88% with no position) | honours-list contamination; upstream fix exists but was never applied |
| Lagos 1879 / 1883 | `colony = 'Lagos' AND year IN [1879, 1883]` | narrative-only-source hallucination, quarantined in the extraction audit |

An official left with zero surviving evidence after filtering is dropped from
the cluster.

## What we MUST NOT do

- **No writes to production.** Read-only. Adjudication results go to a separate
  store or to files for review.
- **No Wikidata `SAME_AS` to production.** Anchoring is gated and stays the
  publication repo's decision; this repo does not commit anchors.
- **No silent trust of upstream counts.** Numbers in `col_pipeline`'s paper
  docs were stale at one point (see `~/col_pipeline/REVIEW_2026-05-07.md`);
  treat the live graph, not the docs, as authoritative.

## Known drift (upstream, informational)

`col_pipeline/docs/schema.md` is materially stale versus the live graph
(verified 2026-06-11). The matching contract above reflects the live graph, not
the doc. Discrepancies found:

- **`COL_Official` identifier**: doc says `uri` (`col:official/{slug}/{name_key}`);
  live graph has **no `uri`** — officials are keyed by `id`
  (`name___colony___first_year`). All 68,335 officials have null `uri`.
- **`COL_Official` name**: doc says `canonical_name` + `surname` + `domain`;
  live node has `name` only (no `canonical_name`/`surname`/`domain`).
- **`COL_Official.editions`**: doc says `editions: int`; live graph has
  `editions: list[int]` (the years) plus `num_editions: int` (the count).
- **`POSSIBLE_MATCH.confidence`**: doc lists it; not present on the live edge.
- **Person edge**: doc says `(:COL_Official)-[:IS_PERSON]->(:COL_Person)`; README
  and live graph use `CAREER_STINT` (`COL_Person → COL_Official`).
  `col_matching` doesn't read the person layer, so this one doesn't affect us.

These are source-of-truth fixes worth making in `col_pipeline/docs/schema.md`.
