<!-- {"case_id": "case_murphy_g-d_b1917", "bio_ids": ["murphy_g-d_b1917", "murphy_g-g_b1916"], "stint_ids": ["Murphy, G___Bahamas___1936"]} -->
# Dossier case_murphy_g-d_b1917

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 73 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Murphy, G___Bahamas___1936'] have more than one claimant biography in this case.

## Biography `murphy_g-d_b1917`

- Printed name: **MURPHY, G. D**
- Birth year: 1917 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L20149.v` — printed in editions [1964, 1965, 1966]:**

> MURPHY, G. D.—b. 1917; Queen's Univ., Belfast; M.O., Fiji, 1953; senr. M.O., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | M.O. | Fiji | [1964, 1965, 1966] |
| 1 | 1961 | senr. M.O | Fiji *(inherited from previous clause)* | [1964, 1965, 1966] |

## Biography `murphy_g-g_b1916`

- Printed name: **MURPHY, G. G**
- Birth year: 1916 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L25499.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> MURPHY, G. G.—b. 1916; ed. St. Finbar's Coll., Cork, Lateran Academy, Rome, and Univ. Coll., Cork; M.O., Uga., 1951; S.M.O., 1956–62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | M.O. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1956–1962 | S.M.O | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Murphy, G___Bahamas___1936`

- Staff-list name: **Murphy, G** | colony: **Bahamas** | listed 1936–1946 | editions [1936, 1939, 1940, 1946]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. Murphy | — | House of Assembly | — | — |
| 1939 | G. Murphy | Member | House of Assembly | — | — |
| 1940 | G. Murphy | Member | House of Assembly | — | — |
| 1946 | G. Murphy | Member | House of Assembly | — | — |

### Deterministic checks: `murphy_g-d_b1917` vs `Murphy, G___Bahamas___1936`

- [PASS] surname_gate: bio 'MURPHY' vs stint 'Murphy, G' (exact)
- [PASS] initials: bio ['G', 'D'] ~ stint ['G']
- [PASS] age_gate: stint starts 1936, birth 1917 (age 19)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1946
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `murphy_g-g_b1916` vs `Murphy, G___Bahamas___1936`

- [PASS] surname_gate: bio 'MURPHY' vs stint 'Murphy, G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1936, birth 1916 (age 20)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1946
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

