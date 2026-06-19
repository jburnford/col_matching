<!-- {"case_id": "case_wall_j-l_b1919", "bio_ids": ["wall_j-l_b1919"], "stint_ids": ["Wall, J. C. L___Leeward Islands___1939", "Wall, J. C. L___Leeward Islands___1956"]} -->
# Dossier case_wall_j-l_b1919

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wall_j-l_b1919`

- Printed name: **WALL, J. L.**
- Birth year: 1919 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L18714.v` — printed in editions [1966]:**

> WALL, J. L.—b. 1919; ed. Salt Boys' High Sch., Shipley, and Leeds Univ.; mil. serv., 1940-47, lieut.; educ. offr., H.K., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940–1947 | lieut. | — | [1966] |
| 1 | 1955 | educ. offr. | Hong Kong | [1966] |

## Candidate stint `Wall, J. C. L___Leeward Islands___1939`

- Staff-list name: **Wall, J. C. L** | colony: **Leeward Islands** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. C. L. Wall | Legislative Council Member | Legislative Council | — | — |
| 1940 | J. C. L. Wall | — | Legislative Council | — | — |

### Deterministic checks: `wall_j-l_b1919` vs `Wall, J. C. L___Leeward Islands___1939`

- [PASS] surname_gate: bio 'WALL' vs stint 'Wall, J. C. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'C', 'L']
- [PASS] age_gate: stint starts 1939, birth 1919 (age 20)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Wall, J. C. L___Leeward Islands___1956`

- Staff-list name: **Wall, J. C. L** | colony: **Leeward Islands** | listed 1956–1957 | editions [1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | J. C. L. Wall | — | Executive Council | — | — |
| 1957 | J. C. L. Wall | — | Executive Council | — | — |

### Deterministic checks: `wall_j-l_b1919` vs `Wall, J. C. L___Leeward Islands___1956`

- [PASS] surname_gate: bio 'WALL' vs stint 'Wall, J. C. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'C', 'L']
- [PASS] age_gate: stint starts 1956, birth 1919 (age 37)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1957
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

