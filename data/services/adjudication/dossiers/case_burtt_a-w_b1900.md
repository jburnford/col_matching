<!-- {"case_id": "case_burtt_a-w_b1900", "bio_ids": ["burtt_a-w_b1900"], "stint_ids": ["Burtt, A. W___Singapore___1951", "Burtt, A. W___Straits Settlements___1936"]} -->
# Dossier case_burtt_a-w_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burtt_a-w_b1900`

- Printed name: **BURTT, A. W**
- Birth year: 1900 (attested in editions [1950, 1951, 1953, 1954, 1955])
- Appears in editions: [1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1950-L34095.v` — printed in editions [1950, 1951, 1953, 1954, 1955]:**

> BURTT, A. W.—b. 1900; ed. Ackworth Sch., Yorks, and B'h'm Univ.; water examr., Nig., 1928; asst. govt. analyst, S'pore, 1932; senr., 1936; dep., Penang, 1937; senr. chmst., 1946; ch. chmst., S'pore, 1947; dir., chemistry, Mal., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | water examr. | Nigeria | [1950, 1951, 1953, 1954, 1955] |
| 1 | 1932 | asst. govt. analyst, S'pore | Nigeria *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 2 | 1936 | senr | Nigeria *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 3 | 1937 | dep., Penang | Nigeria *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 4 | 1946 | senr. chmst | Nigeria *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 5 | 1947 | ch. chmst., S'pore | Nigeria *(inherited from previous clause)* | [1950, 1951, 1953, 1954, 1955] |
| 6 | 1953 | dir., chemistry | Malaya | [1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Burtt, A. W___Singapore___1951`

- Staff-list name: **Burtt, A. W** | colony: **Singapore** | listed 1951–1955 | editions [1951, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | A. W. Burtt | Chief Chemist | Chemistry | — | — |
| 1953 | A. W. Burtt | Chief Chemist | Civil Establishment | — | — |
| 1954 | A. W. Burtt | Director of Chemistry, Malaya | Civil Establishment | — | — |
| 1955 | A. W. Burtt | Director of Chemistry, Malaya | Civil Establishment | — | — |

### Deterministic checks: `burtt_a-w_b1900` vs `Burtt, A. W___Singapore___1951`

- [PASS] surname_gate: bio 'BURTT' vs stint 'Burtt, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1951, birth 1900 (age 51)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1955
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Burtt, A. W___Straits Settlements___1936`

- Staff-list name: **Burtt, A. W** | colony: **Straits Settlements** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | A. W. Burtt | Asst. Analysts, S'pore | Analyst's Department | — | — |
| 1939 | A. W. Burtt | Senior Assistant Analyst | Analyst's Department | — | — |

### Deterministic checks: `burtt_a-w_b1900` vs `Burtt, A. W___Straits Settlements___1936`

- [PASS] surname_gate: bio 'BURTT' vs stint 'Burtt, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

