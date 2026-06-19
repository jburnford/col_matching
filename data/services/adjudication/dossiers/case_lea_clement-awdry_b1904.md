<!-- {"case_id": "case_lea_clement-awdry_b1904", "bio_ids": ["lea_clement-awdry_b1904"], "stint_ids": ["Lea, C. A___Federation of Malaya___1951", "Lea, C. A___Singapore___1949"]} -->
# Dossier case_lea_clement-awdry_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lea_clement-awdry_b1904`

- Printed name: **LEA, Clement Awdry**
- Birth year: 1904 (attested in editions [1954])
- Appears in editions: [1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1954-L21215.v` — printed in editions [1954]:**

> LEA, C. A.—b. 1904; ed. St. Lawrence Coll., Ramsgate, Toronto Univ. and Emmanuel Coll., Camb.; mil. serv., 1942-45; prob. met. offr., S.S., 1932; met. offr., 1934; asst. dir., met. servs., S'pore, 1948; dir., 1951.

**Version `col1950-L37195.v` — printed in editions [1950, 1951, 1953]:**

> LEA, Clement Awdry, B.A. (hons.), Toronto Ph.D. (Cantab.).—b. 1904; ed. St. Lawrence Coll., Ramsgate, Univ. of Toronto, and Cambridge; on mil. serv., 1942-45; probr., meteorological offr., S.S., 1932; meteorological offr., 1934; asst. dir., meteorological serv., S'pore., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | prob. met. offr. | Straits Settlements | [1950, 1951, 1953, 1954] |
| 1 | 1934 | met. offr | Straits Settlements *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 2 | 1948 | asst. dir., met. servs., S'pore | Straits Settlements *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 3 | 1951 | dir | Straits Settlements *(inherited from previous clause)* | [1954] |

## Candidate stint `Lea, C. A___Federation of Malaya___1951`

- Staff-list name: **Lea, C. A** | colony: **Federation of Malaya** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | C. A. Lea | Assistant Director | Meteorological | — | — |
| 1952 | C. A. Lea | Director, Malayan Meteorological Service* | Civil Establishment | — | — |

### Deterministic checks: `lea_clement-awdry_b1904` vs `Lea, C. A___Federation of Malaya___1951`

- [PASS] surname_gate: bio 'LEA' vs stint 'Lea, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1951, birth 1904 (age 47)
- [FAIL] colony: no placed event resolves to 'Federation of Malaya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1952
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Lea, C. A___Singapore___1949`

- Staff-list name: **Lea, C. A** | colony: **Singapore** | listed 1949–1954 | editions [1949, 1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. A. Lea | Meteorological Officers | Meteorological | — | — |
| 1951 | C. A. Lea | Assistant Director of Meteorological Services | Meteorological Services | — | — |
| 1952 | C. A. Lea | Director of Meteorological Services (Acting) | Civil Establishment | — | — |
| 1953 | C. A. Lea | Director Meteorological Services | Civil Establishment | — | — |
| 1954 | C. A. Lea | Director of Meteorological Services | Civil Establishment | — | — |

### Deterministic checks: `lea_clement-awdry_b1904` vs `Lea, C. A___Singapore___1949`

- [PASS] surname_gate: bio 'LEA' vs stint 'Lea, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [FAIL] colony: no placed event resolves to 'Singapore'
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

