<!-- {"case_id": "case_siung_e_b1902", "bio_ids": ["siung_e_b1902"], "stint_ids": ["Siung, E___Trinidad and Tobago___1933", "Siung, E___Trinidad and Tobago___1949"]} -->
# Dossier case_siung_e_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['siung_e_b1902'] carry a single initial only — the namesake trap applies.

## Biography `siung_e_b1902`

- Printed name: **SIUNG, E**
- Birth year: 1902 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L24143.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> SIUNG, E.—b. 1902; ed. Queen's Royal Coll., Trin., Edin. and L'pool Univs.; govt. M.O., Trin., 1930; radiologist, 1940. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | govt. M.O. | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1940 | radiologist | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Siung, E___Trinidad and Tobago___1933`

- Staff-list name: **Siung, E** | colony: **Trinidad and Tobago** | listed 1933–1937 | editions [1933, 1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | E. Siung | Medical Officer | Medical Establishment | — | — |
| 1934 | E. Siung | Medical Officer | Government Medical Officers | — | — |
| 1937 | E. Siung | Medical Officer | Medical Officers | — | — |

### Deterministic checks: `siung_e_b1902` vs `Siung, E___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'SIUNG' vs stint 'Siung, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1933, birth 1902 (age 31)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1937
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Siung, E___Trinidad and Tobago___1949`

- Staff-list name: **Siung, E** | colony: **Trinidad and Tobago** | listed 1949–1954 | editions [1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. Siung | Radiologists | Radiological Branch | — | — |
| 1953 | E. Siung | Radiologist | Civil Establishment | — | — |
| 1954 | E. Siung | Radiologist | Civil Establishment | — | — |

### Deterministic checks: `siung_e_b1902` vs `Siung, E___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'SIUNG' vs stint 'Siung, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1949, birth 1902 (age 47)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

