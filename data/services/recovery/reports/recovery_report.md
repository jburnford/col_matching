# Biography-guided recovery of missing staff-list records

Date: 2026-06-13. Deterministic, file-only (no graph writes, no LLM, no API).

## What this does

Inverts the matcher: biographies are a precise index of who-served-where-when,
used to find staff-list records the upstream Neo4j extraction missed, and
recover them from the per-colony source OCR (`~/textasdatacolonialofficelist/
{year}_manual_parsed/{COLONY}.txt`). A record is proposed only when the
person's surname literally sits on a parsed OCR line — nothing is synthesized.

## Pipeline

`gaps` → `recover` → `recover_loopback` (CLI subcommands). Outputs under
`data/services/recovery/`.

## Results

### Gaps (biography postings the graph lacks a record for)
- **75,048 gap events** across **21,329 biographies**.
- 40,262 `section_present` (colony-year extracted, this officer dropped — a
  missed row); 34,786 `section_absent` (colony-year wholly absent from graph).
- 52,619 gaps resolve to an existing source OCR file (recoverable substrate).

### Recovered records
- **9,874 records recovered**, covering **6,282 biographies**:
  - **2,171 `confirmed_in_ocr`** (surname + compatible initials + matching
    position on a real OCR line) — high confidence.
  - 7,703 `surname_only` (surname + initials found, position weak/garbled or
    the biography named no position) — review queue.
- 41,911 gaps could not be confirmed and emit **no record** (35,121 surname
  absent from the file; 6,790 surname present only with incompatible initials —
  a different person). These are flagged, never fabricated.

### Precision (hand + programmatic sample, n=30 confirmed)
- 30/30 cited `source_file:line` contains the parsed name.
- 30/30 genuinely absent from the graph for that colony-year.
- 30/30 the biography surname is a true word in the parsed name (after fixing a
  substring bug where "Race" matched "Brace").

### Loop-back value
Feeding the 2,171 confirmed records back into candidate enumeration:
- biographies with ≥1 candidate: **9,706 → 10,592**.
- **909 previously unlinkable biographies become linkable** via a recovered
  record; 2,919 biographies gain a recovered candidate.
- `eval_known` stays **0 false positives** at both levels — recovered records
  do not manufacture false merges.

## Whole-section extraction worklist

1,131 colony-year source files are absent from the graph but exist on disk;
13,075 biography-postings expect them. Top targets (`section_worklist.jsonl`,
ranked by biographies expecting the section):

| bios | source file | years |
|------|-------------|-------|
| 356 | FEDERATED_MALAY_STATES (1925) | 1925–27 |
| 323 | UNFEDERATED_MALAY_STATES (1931) | 1929–31 |
| 269 | MALAYA_FEDERATED_MALAY_STATES (1936) | 1935–38 |
| 208 | UNFEDERATED_MALAY_STATES (1933) | 1932–33 |
| 195 | ZANZIBAR (1955) | 1955 |
| 131 | KENYA (1960) | 1960 |
| 130 | FEDERATION_OF_MALAYA (1948) | 1946–48 |
| 122 | FEDERATION_OF_NIGERIA (1961) | 1961–63 |
| 116 | NIGERIA (1940) | 1940–42 |

This is the concrete confirmation of the coverage ceiling: the Malay States,
Zanzibar, late Kenya/Nigeria, and Palestine staff lists were OCR'd but never
loaded into the graph. Running the upstream extractor over these files (local
Ollama, not metered) would recover whole sections, not just bio-predicted rows.

## Handoff / out of scope
- Recovered records are **proposals** for the upstream
  `textasdatacolonialofficelist` pipeline / Jim to validate and load into Neo4j;
  this phase writes files only.
- `department_raw` is the weakest field (nearest-header heuristic misfires when
  tables/governor-lists intervene); `position_raw` and `name_raw` are reliable.
- Bulk re-extraction of the worklist sections is the upstream pipeline's job.
