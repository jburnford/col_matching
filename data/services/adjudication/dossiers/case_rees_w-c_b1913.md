<!-- {"case_id": "case_rees_w-c_b1913", "bio_ids": ["rees_w-c_b1913", "rees_w_b1917"], "stint_ids": ["Rees, W. C___North Borneo___1950", "Rees, William___Western Pacific___1961"]} -->
# Dossier case_rees_w-c_b1913

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rees_w_b1917'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Rees, W. C___North Borneo___1950', 'Rees, William___Western Pacific___1961'] have more than one claimant biography in this case.

## Biography `rees_w-c_b1913`

- Printed name: **REES, W. C**
- Birth year: 1913 (attested in editions [1958])
- Appears in editions: [1958]

### Verbatim printed entry text (OCR)

**Version `col1958-L26303.v` — printed in editions [1958]:**

> REES, W. C., T.D.—b. 1913; ed. Cheltenham, and Trinity Coll., Camb.; mil. serv., 1939-46, major; admin. cadet, Mal., 1947; dist. offr., N. Borneo, 1948; Tang., 1951; secon., Ken., during 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | admin. cadet | Malaya | [1958] |
| 1 | 1948 | dist. offr. | North Borneo | [1958] |
| 2 | 1951 | dist. offr. | Tanganyika | [1958] |
| 3 | 1953 | secon., Ken., during | Tanganyika *(inherited from previous clause)* | [1958] |

## Biography `rees_w_b1917`

- Printed name: **REES, W**
- Birth year: 1917 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L24088.v` — printed in editions [1963, 1964, 1965, 1966]:**

> REES, W.—b. 1917; ed. Dynevor Gram. Sch., Swansea; mil. serv., 1940-45, (A) R.N.V.R., sub. lt. (desps.); asssr., gr. I, inl. rev., H.K., 1952; asst. comsnr., 1959; dep. comsnr., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | asssr., gr. I, inl. rev. | Hong Kong | [1963, 1964, 1965, 1966] |
| 1 | 1959 | asst. comsnr | Hong Kong *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1965 | dep. comsnr | Hong Kong *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Rees, W. C___North Borneo___1950`

- Staff-list name: **Rees, W. C** | colony: **North Borneo** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. C. Rees | Cadet | District Administration | — | — |
| 1951 | W. C. Rees | Cadet | District Administration | — | — |

### Deterministic checks: `rees_w-c_b1913` vs `Rees, W. C___North Borneo___1950`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1950, birth 1913 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 29 vs bar 60: 'dist. offr.' ~ 'Cadet'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `rees_w_b1917` vs `Rees, W. C___North Borneo___1950`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, W. C' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1950, birth 1917 (age 33)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Rees, William___Western Pacific___1961`

- Staff-list name: **Rees, William** | colony: **Western Pacific** | listed 1961–1966 | editions [1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | William Rees | Senior Medical Officer | British National Administration | — | — |
| 1962 | W. H. Rees | Senior Medical Officer | British National Administration | — | — |
| 1964 | W. H. Rees | Senior Medical Officer | British National Administration | — | — |
| 1965 | W. R. Rees | Senior Medical Officer | British National Administration | — | — |
| 1966 | W. R. Rees | Senior Medical Officer | British National Administration | — | — |

### Deterministic checks: `rees_w-c_b1913` vs `Rees, William___Western Pacific___1961`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, William' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W']
- [PASS] age_gate: stint starts 1961, birth 1913 (age 48)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1966
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `rees_w_b1917` vs `Rees, William___Western Pacific___1961`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, William' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1961, birth 1917 (age 44)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1966
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

