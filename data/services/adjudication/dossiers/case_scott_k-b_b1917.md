<!-- {"case_id": "case_scott_k-b_b1917", "bio_ids": ["scott_k-b_b1917"], "stint_ids": ["Scott, K. B___St Helena___1955", "Scott, K___Nyasaland___1939"]} -->
# Dossier case_scott_k-b_b1917

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 151 official(s) with this surname in the graph's staff lists; 65 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `scott_k-b_b1917`

- Printed name: **SCOTT, K. B**
- Birth year: 1917 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1955-L22604.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> SCOTT, K. B., M.B.E. (Mil.)—b. 1917; ed. Merchant Taylors' Sch.; mil. serv., 1939–46, lieut.-comdr.(S), R.N.V.R. (desps.); cadet, Nig., 1946; admin. offr., cl. IV., 1949; cl. III, 1951; cl. II, 1954; secon., govt. sec. and magistrate, St. H., 1954–57; admin. offr., gr. 6, 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Nigeria | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1949 | admin. offr., cl. IV | Nigeria *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1951 | cl. III | Nigeria *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1954 | cl. II | Nigeria *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1960 | admin. offr., gr. 6 | Nigeria *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Scott, K. B___St Helena___1955`

- Staff-list name: **Scott, K. B** | colony: **St Helena** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | K. B. Scott | Government Secretary and Magistrate | Civil Establishment | — | — |
| 1956 | K. B. Scott | Government Secretary and Magistrate | Civil Establishment | — | — |
| 1957 | K. B. Scott | Government Secretary and Magistrate | CIVIL ESTABLISHMENT | — | — |

### Deterministic checks: `scott_k-b_b1917` vs `Scott, K. B___St Helena___1955`

- [PASS] surname_gate: bio 'SCOTT' vs stint 'Scott, K. B' (exact)
- [PASS] initials: bio ['K', 'B'] ~ stint ['K', 'B']
- [PASS] age_gate: stint starts 1955, birth 1917 (age 38)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Scott, K___Nyasaland___1939`

- Staff-list name: **Scott, K** | colony: **Nyasaland** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | K. Scott | Nurses | Medical | — | — |
| 1940 | K. Scott | Nurse | Medical | — | — |

### Deterministic checks: `scott_k-b_b1917` vs `Scott, K___Nyasaland___1939`

- [PASS] surname_gate: bio 'SCOTT' vs stint 'Scott, K' (exact)
- [PASS] initials: bio ['K', 'B'] ~ stint ['K']
- [PASS] age_gate: stint starts 1939, birth 1917 (age 22)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

