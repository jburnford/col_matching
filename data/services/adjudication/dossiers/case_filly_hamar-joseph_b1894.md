<!-- {"case_id": "case_filly_hamar-joseph_b1894", "bio_ids": ["filly_hamar-joseph_b1894"], "stint_ids": ["Lilly, J___Gold Coast___1950"]} -->
# Dossier case_filly_hamar-joseph_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lilly, J___Gold Coast___1950` is also gate-compatible with biography(ies) outside this case: ['lilly_john_b1902'] (already linked elsewhere or filtered).

## Biography `filly_hamar-joseph_b1894`

- Printed name: **FILLY, HAMAR JOSEPH**
- Birth year: 1894 (attested in editions [1922])
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L52133.v` — printed in editions [1922]:**

> FILLY, HAMAR JOSEPH.—B. 1894; ed. Burton-on-Trent and Queen's Coll., Camb. (math. tripes, pt. I); O.T.C., Camb.; 2nd Heut., 13th Fn. Sherwood Foresters, Feb., 1915; served, Suvla Bay, Egypt and France; wounded, Sept., 1916; discharged, Apr., 1918; cadet, Malayan civil service (S.S.), Mar., 1920; collr. of income tax, Singapore, May, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | 2nd Heut., 13th Fn. Sherwood Foresters | — | [1922] |
| 1 | 1916 | wounded | — | [1922] |
| 2 | 1918 | discharged | — | [1922] |
| 3 | 1920 | cadet, Malayan civil service (S.S.) | — | [1922] |
| 4 | 1920 | collr. of income tax | Singapore | [1922] |

## Candidate stint `Lilly, J___Gold Coast___1950`

- Staff-list name: **Lilly, J** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. Lilly | Director of Water Supply | WATER SUPPLY | — | — |
| 1951 | J. Lilly | Director of Rural Water Development | Rural Water Development | — | — |

### Deterministic checks: `filly_hamar-joseph_b1894` vs `Lilly, J___Gold Coast___1950`

- [PASS] surname_gate: bio 'FILLY' vs stint 'Lilly, J' (fuzzy:1)
- [PASS] initials: bio ['H', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1950, birth 1894 (age 56)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

