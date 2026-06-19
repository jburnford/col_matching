<!-- {"case_id": "case_stone_edward-frank_b1855", "bio_ids": ["stone_edward-frank_b1855"], "stint_ids": ["Stone, E. F___Trinidad and Tobago___1899"]} -->
# Dossier case_stone_edward-frank_b1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stone_edward-frank_b1855`

- Printed name: **STONE, Edward Frank**
- Birth year: 1855 (attested in editions [1917])
- Appears in editions: [1917]

### Verbatim printed entry text (OCR)

**Version `col1917-L53414.v` — printed in editions [1917]:**

> STONE, Edward Frank.—B. 1855; entd. civ. serv., Trinidad, 1st June, 1888; warden, 1st Jan., 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | entd. civ. serv. | Trinidad | [1917] |
| 1 | 1909 | warden | Trinidad *(inherited from previous clause)* | [1917] |

## Candidate stint `Stone, E. F___Trinidad and Tobago___1899`

- Staff-list name: **Stone, E. F** | colony: **Trinidad and Tobago** | listed 1899–1915 | editions [1899, 1900, 1905, 1906, 1907, 1910, 1912, 1913, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | E. F. Stone | 3rd | Post Office Department | — | — |
| 1900 | E. F. Stone | 3rd Clerk | Post Office Department | — | — |
| 1905 | E. F. Stone | Chief Clerk | San Fernando Treasury | — | — |
| 1906 | E. F. Stone | Chief Clerk | San Fernando Treasury | — | — |
| 1907 | E. F. Stone | Chief Clerk | San Fernando Treasury | — | — |
| 1910 | E. F. Stone | Warden | Warden | — | — |
| 1912 | E. F. Stone | Warden | Clerks of the Peace | — | — |
| 1913 | E. F. Stone | Warden | Wardens | — | — |
| 1915 | E. F. Stone | Inspector | Inspectors and Supervisors | — | — |

### Deterministic checks: `stone_edward-frank_b1855` vs `Stone, E. F___Trinidad and Tobago___1899`

- [PASS] surname_gate: bio 'STONE' vs stint 'Stone, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1899, birth 1855 (age 44)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1915
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

