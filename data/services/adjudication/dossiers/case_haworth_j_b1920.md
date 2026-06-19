<!-- {"case_id": "case_haworth_j_b1920", "bio_ids": ["haworth_j_b1920"], "stint_ids": ["Haworth, J. S___Sarawak___1950", "Haworth, J___British Somaliland___1959"]} -->
# Dossier case_haworth_j_b1920

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['haworth_j_b1920'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Haworth, J. S___Sarawak___1950` is also gate-compatible with biography(ies) outside this case: ['haworth_j-s_b1912'] (already linked elsewhere or filtered).
- NOTE: stint `Haworth, J___British Somaliland___1959` is also gate-compatible with biography(ies) outside this case: ['haworth_j-s_b1912'] (already linked elsewhere or filtered).

## Biography `haworth_j_b1920`

- Printed name: **HAWORTH, J**
- Birth year: 1920 (attested in editions [1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1959-L23962.v` — printed in editions [1959, 1960, 1961, 1962, 1963]:**

> HAWORTH, J.—b. 1920; ed. Baines Gram. Sch., Poulton-le-Fylde, Arnold Sch., Blackpool, and Edin. Univ.; mil. serv., 1943-46, major, R.A.M.C.; M.O., Nig., 1947; M.O.H., 1954; S.M.O. (health), Som., 1958. (Som. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | M.O. | Nigeria | [1959, 1960, 1961, 1962, 1963] |
| 1 | 1954 | M.O.H | Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |
| 2 | 1958 | S.M.O. (health) | Somaliland | [1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Haworth, J. S___Sarawak___1950`

- Staff-list name: **Haworth, J. S** | colony: **Sarawak** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. S. Haworth | Sanitary Superintendent | MEDICAL AND HEALTH | — | — |
| 1951 | J. S. Haworth | Sanitary Superintendent | Medical and Health | — | — |

### Deterministic checks: `haworth_j_b1920` vs `Haworth, J. S___Sarawak___1950`

- [PASS] surname_gate: bio 'HAWORTH' vs stint 'Haworth, J. S' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1950, birth 1920 (age 30)
- [FAIL] colony: no placed event resolves to 'Sarawak'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Haworth, J___British Somaliland___1959`

- Staff-list name: **Haworth, J** | colony: **British Somaliland** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | J. Haworth | Senior Medical Officer | Civil Establishment | — | — |
| 1960 | J. Haworth | Senior Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `haworth_j_b1920` vs `Haworth, J___British Somaliland___1959`

- [PASS] surname_gate: bio 'HAWORTH' vs stint 'Haworth, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1959, birth 1920 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1959-1960
- [FAIL] position_sim: best 38 vs bar 60: 'S.M.O. (health)' ~ 'Senior Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

