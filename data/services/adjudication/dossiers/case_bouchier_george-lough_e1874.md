<!-- {"case_id": "case_bouchier_george-lough_e1874", "bio_ids": ["bouchier_george-lough_e1874"], "stint_ids": ["Bourchier, G. L___Straits Settlements___1888"]} -->
# Dossier case_bouchier_george-lough_e1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `bouchier_george-lough_e1874` ↔ `Bourchier, G. L___Straits Settlements___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Bourchier, G. L___Straits Settlements___1888` is also gate-compatible with biography(ies) outside this case: ['bourchier_george-lough_e1874'] (already linked elsewhere or filtered).

## Biography `bouchier_george-lough_e1874`

- Printed name: **BOUCHIER, GEORGE LOUGH**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L32273.v` — printed in editions [1886, 1888]:**

> BOUCHIER, GEORGE LOUGH.—In public works department, Canada, 1874-7; appointed to public works department, Ceylon, September, 1877, assistant-superintendent of works and surveys, Straits Settlements, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874–1877 | public works department | Canada | [1886, 1888] |
| 1 | 1877 | public works department | Ceylon | [1886, 1888] |
| 2 | 1883 | assistant-superintendent of works and surveys | Straits Settlements | [1886, 1888] |

## Candidate stint `Bourchier, G. L___Straits Settlements___1888`

- Staff-list name: **Bourchier, G. L** | colony: **Straits Settlements** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | G. L. Bourchier | Assistant Superintendent of Works | Public Works and Survey Departments | — | — |
| 1889 | G. L. Bourchier | Assistant Superintendent of Works and Surveys | Public Works and Survey Departments | — | — |

### Deterministic checks: `bouchier_george-lough_e1874` vs `Bourchier, G. L___Straits Settlements___1888`

- [PASS] surname_gate: bio 'BOUCHIER' vs stint 'Bourchier, G. L' (fuzzy:1)
- [PASS] initials: bio ['G', 'L'] ~ stint ['G', 'L']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1889
- [PASS] position_sim: best 99 vs bar 60: 'assistant-superintendent of works and surveys' ~ 'Assistant Superintendent of Works and Surveys'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1888] pos~83 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

## Adjudication constraints (binding)

- The prime directive is NO FALSE MERGES. A missed link is recoverable; a
  wrong one silently corrupts the historical record. When in doubt, leave
  the stint unassigned.
- Surname identity is NOT evidence: every candidate here already shares the
  surname (it is the blocking key). Only position, place, dates, honours,
  initials/forenames, and edition co-occurrence count.
- Single-initial biographies (e.g. "J. Lewis") must never be merged on
  shared-stint or tenure-overlap evidence alone; they need a strong
  independent dimension (specific position match, shared honour, or
  multi-edition co-occurrence).
- A stint belongs to AT MOST one biography. If two biographies in this case
  could plausibly hold the same stint, assign it to neither.
- Respect hard chronology: nobody serves before age ~15 or after death.
- Generic junior titles (clerk, cadet, assistant) recur constantly; a title
  match alone on a common office is weak evidence.

