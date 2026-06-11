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
  ml_uncertainty: float,   # GradientBoosting score (may be null)
  method: str,             # automated_linking | cross_colony_linking
                           #   | ml_discovery | gazette_discovery
  confidence: float,
  date_created: str
}]->(:COL_Official)
```

`col_matching` v1 **reuses col_pipeline's blocking** — it adjudicates clusters
the linker/ML already proposed, rather than re-generating candidates. Widening
candidate generation (e.g. surname/initial blocking to surface pairs the
conservative linker never scored) is deliberately deferred.

### 2. Stint identity — `COL_Official`

```
(:COL_Official {
  uri: str,                # col:official/{slug}/{name_key}
  canonical_name: str,
  surname: str,
  colony: str,
  first_year: int,
  last_year: int,
  editions: int,
  domain: str | null       # medical | legal | … (may be null)
})
```

`COL_Official` is thin — the discriminating evidence (honours, rank, position,
department, salary) lives on the underlying records, not here.

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

- `col_pipeline/docs/schema.md` lists the person edge as
  `(:COL_Official)-[:IS_PERSON]->(:COL_Person)`. The README and live graph use
  `CAREER_STINT` (`COL_Person → COL_Official`). `col_matching` does not read
  the person layer, so this does not affect the contract — but it's a
  source-of-truth fix worth making in `col_pipeline`.
