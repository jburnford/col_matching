<!-- {"case_id": "case_norman_charles-bathurst_b1904", "bio_ids": ["norman_charles-bathurst_b1904"], "stint_ids": ["Norman, C. B. H___Trinidad and Tobago___1922", "Norman, C. B. H___Trinidad and Tobago___1928"]} -->
# Dossier case_norman_charles-bathurst_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Norman, C. B. H___Trinidad and Tobago___1922` is also gate-compatible with biography(ies) outside this case: ['norman_henry_b1877'] (already linked elsewhere or filtered).
- NOTE: stint `Norman, C. B. H___Trinidad and Tobago___1928` is also gate-compatible with biography(ies) outside this case: ['norman_henry_b1877'] (already linked elsewhere or filtered).

## Biography `norman_charles-bathurst_b1904`

- Printed name: **NORMAN, CHARLES BATHURST**
- Birth year: 1904 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67120.v` — printed in editions [1940]:**

> NORMAN, CHARLES BATHURST.—B. 1904; ed. Harrow Schi. and Magdalen Coll., Oxford; dist. offr., Kenya, 1925; ag. asst. sec., 1936; dist. comsrr. and chmn., munic. coun., Mombasa, 1936; seconded, Zanzibar, Aug., 1936 to Jan., 1937; Palestine, Jan., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | dist. offr. | Kenya | [1940] |
| 1 | 1936 | ag. asst. sec | Kenya *(inherited from previous clause)* | [1940] |
| 2 | 1936–1937 | seconded | Zanzibar | [1940] |
| 3 | 1938 | seconded | Palestine | [1940] |

## Candidate stint `Norman, C. B. H___Trinidad and Tobago___1922`

- Staff-list name: **Norman, C. B. H** | colony: **Trinidad and Tobago** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | C. Norman | Chief Clerk | Forest Department | — | — |
| 1923 | C. Norman | Chief Clerk | Forest Department | — | — |

### Deterministic checks: `norman_charles-bathurst_b1904` vs `Norman, C. B. H___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'NORMAN' vs stint 'Norman, C. B. H' (exact)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C', 'B', 'H']
- [PASS] age_gate: stint starts 1922, birth 1904 (age 18)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Norman, C. B. H___Trinidad and Tobago___1928`

- Staff-list name: **Norman, C. B. H** | colony: **Trinidad and Tobago** | listed 1928–1939 | editions [1928, 1929, 1931, 1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | C. Norman | Chief Clerk | Forest Department | — | — |
| 1929 | C. Norman | 2nd Clerk | Department of Education | — | — |
| 1931 | C. Norman | Chief Clerk and Accountant | Department of Education | — | — |
| 1933 | C. Norman | Principal Officer and Accountant | Department of Education | — | — |
| 1934 | C. Norman | Principal Officer and Accountant, and Secretary Education Board | Department of Education | — | — |
| 1937 | C. Norman | Principal Officer and Accountant, and Secretary Education Board | Department of Education | — | — |
| 1939 | C. Norman | Principal Officer and Accountant, and Secretary Education Board | Department of Education | — | — |

### Deterministic checks: `norman_charles-bathurst_b1904` vs `Norman, C. B. H___Trinidad and Tobago___1928`

- [PASS] surname_gate: bio 'NORMAN' vs stint 'Norman, C. B. H' (exact)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C', 'B', 'H']
- [PASS] age_gate: stint starts 1928, birth 1904 (age 24)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1939
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

