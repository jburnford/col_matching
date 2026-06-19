<!-- {"case_id": "case_knight_m-t_e1866", "bio_ids": ["knight_m-t_e1866"], "stint_ids": ["Knight, Mc. T___Newfoundland___1877", "Knight, Mc. T___Newfoundland___1906"]} -->
# Dossier case_knight_m-t_e1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 72 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `knight_m-t_e1866`

- Printed name: **KNIGHT, M. T**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1896-L39830.v` — printed in editions [1896, 1897, 1898]:**

> KNIGHT, M. T.—Financial secy., Newfoundland, 1866-9; survivor-general, 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866–1869 | Financial secy. | Newfoundland | [1896, 1897, 1898] |
| 1 | 1894 | survivor-general | Newfoundland *(inherited from previous clause)* | [1896, 1897, 1898] |

## Candidate stint `Knight, Mc. T___Newfoundland___1877`

- Staff-list name: **Knight, Mc. T** | colony: **Newfoundland** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | M. Knight | Collector (Labrador) | Civil Establishment | — | — |
| 1878 | M. Knight | Collector (Labrador) | Civil Establishment | — | — |
| 1879 | M. Knight | Collector (Labrador) | Civil Establishment | — | — |
| 1880 | Michael Knight | Accountant | Civil Establishment | — | — |
| 1886 | Mc. T. Knight | Secretary Board of Works | Civil Establishment | — | — |
| 1888 | M. T. Knight | Financial Secretary | Civil Establishment | — | — |
| 1889 | M. T. Knight | Financial Secretary | Civil Establishment | — | — |

### Deterministic checks: `knight_m-t_e1866` vs `Knight, Mc. T___Newfoundland___1877`

- [PASS] surname_gate: bio 'KNIGHT' vs stint 'Knight, Mc. T' (exact)
- [PASS] initials: bio ['M', 'T'] ~ stint ['M', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Knight, Mc. T___Newfoundland___1906`

- Staff-list name: **Knight, Mc. T** | colony: **Newfoundland** | listed 1906–1909 | editions [1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | M. T. Knight | Secretary | Public Works | — | — |
| 1907 | M. T. Knight | Secretary | Public Works | — | — |
| 1908 | M. T. Knight | Secretary | Department of Public Works | — | — |
| 1909 | M. T. Knight | Secretary | Department of Public Works | — | — |

### Deterministic checks: `knight_m-t_e1866` vs `Knight, Mc. T___Newfoundland___1906`

- [PASS] surname_gate: bio 'KNIGHT' vs stint 'Knight, Mc. T' (exact)
- [PASS] initials: bio ['M', 'T'] ~ stint ['M', 'T']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1909
- [FAIL] position_sim: best 33 vs bar 60: 'survivor-general' ~ 'Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

