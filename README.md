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

Scaffold only. Present: the read-only graph accessor and the documented
contract. Not present yet (by design): the dossier serializer, the Fable
adjudication harness, and any evaluation framework.

## Setup

```bash
cd ~/col_matching
pip install -e .
cp .env.example .env   # or rely on ~/textasdatacolonialofficelist/.env (auto-loaded)
```

Credentials resolve the same way as `col_pipeline` (`NEO4J_PROD_URI` /
`NEO4J_URI`, `NEO4J_PASSWORD`, …), falling back to the sibling repo's `.env`,
so there's a single credential source.
