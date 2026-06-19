<!-- {"case_id": "case_ross_e-m_b1906", "bio_ids": ["ross_e-m_b1906"], "stint_ids": ["Ross, E. M___Leeward Islands___1932"]} -->
# Dossier case_ross_e-m_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 140 official(s) with this surname in the graph's staff lists; 64 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ross_e-m_b1906`

- Printed name: **ROSS, E. M**
- Birth year: 1906 (attested in editions [1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1959-L27447.v` — printed in editions [1959, 1960, 1961, 1962, 1963]:**

> ROSS, Miss E. M.—b. 1906; ed. Newcastle-on-Tyne Church High Sch., and Northern Counties Train. Coll. of Cookery; woman educ. offr., Tang., 1947. (Tang. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | woman educ. offr. | Tanganyika | [1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Ross, E. M___Leeward Islands___1932`

- Staff-list name: **Ross, E. M** | colony: **Leeward Islands** | listed 1932–1940 | editions [1932, 1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | E. M. Ross | Senior Clerk | Judicial and Legal | — | — |
| 1936 | E. M. Ross | Senior Clerk | Judicial and Legal | — | — |
| 1936 | E. M. Ross | Senior Clerk | Judicial | — | — |
| 1939 | E. M. Ross | Senior Clerk | Judicial and Legal | — | — |
| 1940 | E. M. Ross | Senior Clerk | Judicial and Legal | — | — |

### Deterministic checks: `ross_e-m_b1906` vs `Ross, E. M___Leeward Islands___1932`

- [PASS] surname_gate: bio 'ROSS' vs stint 'Ross, E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1932, birth 1906 (age 26)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

