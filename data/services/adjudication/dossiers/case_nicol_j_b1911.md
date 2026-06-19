<!-- {"case_id": "case_nicol_j_b1911", "bio_ids": ["nicol_j_b1911"], "stint_ids": ["Nicol, J. M___Tonga___1931", "Nicol, J. M___Western Pacific___1930"]} -->
# Dossier case_nicol_j_b1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['nicol_j_b1911'] carry a single initial only — the namesake trap applies.

## Biography `nicol_j_b1911`

- Printed name: **NICOL, J**
- Birth year: 1911 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L23260.v` — printed in editions [1956]:**

> NICOL, J.—b. 1911; ed. Robt. Gordon's Coll. and Aberdeen Univ.; entomologist, W.A. cocoa research inst., 1944; senr. entomologist, 1947; i/c W.A.C.R.I. sub-station, Nig., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | entomologist, W.A. cocoa research inst | — | [1956] |
| 1 | 1947 | senr. entomologist | — | [1956] |
| 2 | 1954 | i/c W.A.C.R.I. sub-station | Nigeria | [1956] |

## Candidate stint `Nicol, J. M___Tonga___1931`

- Staff-list name: **Nicol, J. M** | colony: **Tonga** | listed 1931–1940 | editions [1931, 1934, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. M. Nicol | District Agent | British Staff | — | — |
| 1934 | J. M. Nicol | District Agent | British Staff | — | — |
| 1939 | J. M. Nicol | District Agent | British Staff | — | — |
| 1940 | J. M. Nicol | District Agent | British Staff | — | — |

### Deterministic checks: `nicol_j_b1911` vs `Nicol, J. M___Tonga___1931`

- [PASS] surname_gate: bio 'NICOL' vs stint 'Nicol, J. M' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1931, birth 1911 (age 20)
- [FAIL] colony: no placed event resolves to 'Tonga'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Nicol, J. M___Western Pacific___1930`

- Staff-list name: **Nicol, J. M** | colony: **Western Pacific** | listed 1930–1937 | editions [1930, 1933, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | J. M. Nicol | Island Agent | British Staff | — | — |
| 1933 | J. M. Nicol | District Agent | British Staff | — | — |
| 1936 | J. M. Nicol | District Agent | British Staff | — | — |
| 1937 | J. M. Nicol | District Agent | British Staff | — | — |

### Deterministic checks: `nicol_j_b1911` vs `Nicol, J. M___Western Pacific___1930`

- [PASS] surname_gate: bio 'NICOL' vs stint 'Nicol, J. M' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1930, birth 1911 (age 19)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1937
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

