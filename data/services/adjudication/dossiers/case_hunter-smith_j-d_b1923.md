<!-- {"case_id": "case_hunter-smith_j-d_b1923", "bio_ids": ["hunter-smith_j-d_b1923"], "stint_ids": ["Hunter-Smith, J. D___Swaziland___1962", "Hunter-Smith, J.D___High Commission Territories___1959"]} -->
# Dossier case_hunter-smith_j-d_b1923

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hunter-smith_j-d_b1923`

- Printed name: **HUNTER-SMITH, J. D**
- Birth year: 1923 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L22076.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HUNTER-SMITH, J. D.—b. 1923; ed. St. Albans, Reading Univ. and I.C.T.A.; agric. offr., Tang., 1945; prin. agric. offr., Swaz., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | agric. offr. | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1956 | prin. agric. offr., Swaz | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hunter-Smith, J. D___Swaziland___1962`

- Staff-list name: **Hunter-Smith, J. D** | colony: **Swaziland** | listed 1962–1966 | editions [1962, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | J. D. Hunter-Smith | Principal Agricultural Officer | Secretariat | — | — |
| 1965 | J. D. Hunter-Smith | Deputy Director of Agriculture (Agriculture) | Secretariat | — | — |
| 1966 | J. D. Hunter-Smith | Deputy Director of Agriculture (Agriculture) | Civil Establishment | — | — |

### Deterministic checks: `hunter-smith_j-d_b1923` vs `Hunter-Smith, J. D___Swaziland___1962`

- [PASS] surname_gate: bio 'HUNTER-SMITH' vs stint 'Hunter-Smith, J. D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1962, birth 1923 (age 39)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hunter-Smith, J.D___High Commission Territories___1959`

- Staff-list name: **Hunter-Smith, J.D** | colony: **High Commission Territories** | listed 1959–1964 | editions [1959, 1960, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | J. D. Hunter-Smith | Principal Agricultural Officer | SWAZILAND | — | — |
| 1960 | J. D. Hunter-Smith | Principal Agricultural Officer | SWAZILAND | — | — |
| 1963 | J.D. Hunter-Smith | Principal Agricultural Officer | SECRETARIAT | — | — |
| 1964 | J. D. Hunter-Smith | Deputy Director of Agriculture (Agriculture) | Civil Establishment | — | — |

### Deterministic checks: `hunter-smith_j-d_b1923` vs `Hunter-Smith, J.D___High Commission Territories___1959`

- [PASS] surname_gate: bio 'HUNTER-SMITH' vs stint 'Hunter-Smith, J.D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1959, birth 1923 (age 36)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1964
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

