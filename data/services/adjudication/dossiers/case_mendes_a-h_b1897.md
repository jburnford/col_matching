<!-- {"case_id": "case_mendes_a-h_b1897", "bio_ids": ["mendes_a-h_b1897"], "stint_ids": ["Mendes, Alfred___Trinidad and Tobago___1933", "Mendes, Alfred___Trinidad and Tobago___1953"]} -->
# Dossier case_mendes_a-h_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mendes_a-h_b1897`

- Printed name: **MENDES, A. H**
- Birth year: 1897 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L18452.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> MENDES, A. H., M.M.—b. 1897; ed. Queen's Royal Gram. Sch., Trin., Hitchin Gram. Sch. and Mill Hill Pub. Sch., Lond.; mil. serv., 1914–17 (desps.); acctnt., Trin., 1946; dep. gen. man., port servs., 1949; gen. man., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | acctnt. | Trinidad | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1949 | dep. gen. man., port servs | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1955 | gen. man | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Mendes, Alfred___Trinidad and Tobago___1933`

- Staff-list name: **Mendes, Alfred** | colony: **Trinidad and Tobago** | listed 1933–1939 | editions [1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | Alfred Mendes | Vice-Consul | Consuls | — | — |
| 1934 | Alfred Mendes | Vice-Consul | — | — | — |
| 1937 | Alfred Mendes | Vice | Consuls | — | — |
| 1939 | Alfred Mendes | Vice-Consul | Consuls | — | — |

### Deterministic checks: `mendes_a-h_b1897` vs `Mendes, Alfred___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'MENDES' vs stint 'Mendes, Alfred' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A']
- [PASS] age_gate: stint starts 1933, birth 1897 (age 36)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Mendes, Alfred___Trinidad and Tobago___1953`

- Staff-list name: **Mendes, Alfred** | colony: **Trinidad and Tobago** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | A. H. Mendes | Deputy General Manager | Civil Establishment | — | — |
| 1954 | A. H. Mendes | Deputy General Manager | Civil Establishment | — | — |

### Deterministic checks: `mendes_a-h_b1897` vs `Mendes, Alfred___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'MENDES' vs stint 'Mendes, Alfred' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A']
- [PASS] age_gate: stint starts 1953, birth 1897 (age 56)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1954
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

