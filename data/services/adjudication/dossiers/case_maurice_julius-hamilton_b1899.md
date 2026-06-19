<!-- {"case_id": "case_maurice_julius-hamilton_b1899", "bio_ids": ["maurice_julius-hamilton_b1899"], "stint_ids": ["Maurice, J. H___Trinidad and Tobago___1937", "Maurice, J. Hamilton___Windward Islands___1950"]} -->
# Dossier case_maurice_julius-hamilton_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maurice_julius-hamilton_b1899`

- Printed name: **MAURICE, Julius Hamilton**
- Birth year: 1899 (attested in editions [1949, 1950, 1951, 1953, 1954, 1955])
- Appears in editions: [1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1949-L34243.v` — printed in editions [1949, 1950, 1951, 1953, 1954, 1955]:**

> MAURICE, Julius Hamilton.—b. 1899; ed. St. Mary's Coll., Trin. and Univ. of Lond., Inst. of Educ., B.A. (Lond.), inter B.Sc. (econ., Lond.); asst. lect., gov. training coll. for teachers, Trin., 1932; asst. inspr., schs., Trin., 1938; resdt. inspr., schs., Tobago, 1942; seconded educ. offr., Dominica, 1947; author of paper on post-primary education, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | asst. lect., gov. training coll. for teachers | Trinidad | [1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1938 | asst. inspr., schs. | Trinidad | [1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1938 | author of paper on post-primary education | Dominica *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954, 1955] |
| 3 | 1942 | resdt. inspr., schs. | Tobago | [1949, 1950, 1951, 1953, 1954, 1955] |
| 4 | 1947 | seconded educ. offr. | Dominica | [1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Maurice, J. H___Trinidad and Tobago___1937`

- Staff-list name: **Maurice, J. H** | colony: **Trinidad and Tobago** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | J. H. Maurice | Assistant Lecturer | Government Training College | — | — |
| 1939 | J. H. Maurice | Assistant Inspector | Department of Education | — | — |
| 1940 | J. H. Maurice | Assistant Inspector | Education | — | — |

### Deterministic checks: `maurice_julius-hamilton_b1899` vs `Maurice, J. H___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'MAURICE' vs stint 'Maurice, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1937, birth 1899 (age 38)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Maurice, J. Hamilton___Windward Islands___1950`

- Staff-list name: **Maurice, J. Hamilton** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. Hamilton Maurice | Education Officer | EDUCATION | — | — |
| 1952 | J. Hamilton Maurice | Education Officer | Civil Establishment | — | — |

### Deterministic checks: `maurice_julius-hamilton_b1899` vs `Maurice, J. Hamilton___Windward Islands___1950`

- [PASS] surname_gate: bio 'MAURICE' vs stint 'Maurice, J. Hamilton' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1950, birth 1899 (age 51)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

