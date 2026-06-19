<!-- {"case_id": "case_hutchinson_c-k_b1902", "bio_ids": ["hutchinson_c-k_b1902"], "stint_ids": ["Hutchinson, C. K___Trinidad and Tobago___1933"]} -->
# Dossier case_hutchinson_c-k_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hutchinson_c-k_b1902`

- Printed name: **HUTCHINSON, C. K**
- Birth year: 1902 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L22088.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> HUTCHINSON, C. K.—b. 1902; ed. Naparima Coll.; agric. advr., Trin., 1931; chief inspr. of co-ops. and senr. agric. asst., 1939; chief inspr., dept. of co-op. devel., 1950; dep. comsnr., co-op. devel., 1953; asstd. Benham and Soulbury sugar comsns., tech. advr., canefarmers' arbit. bd., Trin.; advr. to govt. on labr. riots, 1934.

**Version `col1962-L22623.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> HUTCHINSON, C. K.—b. 1902; ed. Naparima Coll.; agric. advr., Trin., 1931; chief inspr. of co-ops. and senr. agric. asst., 1939; chief inspr., dept. of co-op. devel., 1950; dep. comsnr., co-op. devel., 1953. (T’dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | agric. advr. | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1934 | advr. to govt. on labr. riots | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1939 | chief inspr. of co-ops. and senr. agric. asst | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1950 | chief inspr., dept. of co-op. devel | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1953 | dep. comsnr., co-op. devel | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hutchinson, C. K___Trinidad and Tobago___1933`

- Staff-list name: **Hutchinson, C. K** | colony: **Trinidad and Tobago** | listed 1933–1939 | editions [1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | C. K. Hutchinson | Agricultural Adviser | Department of Agriculture | — | — |
| 1934 | C. K. Hutchinson | Agricultural Adviser | Department of Agriculture | — | — |
| 1937 | C. K. Hutchinson | Agricultural Adviser | Scientific and Technical Staff | — | — |
| 1939 | C. K. Hutchinson | Inspector Agricultural Co-operative Societies | Department of Agriculture | — | — |

### Deterministic checks: `hutchinson_c-k_b1902` vs `Hutchinson, C. K___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'HUTCHINSON' vs stint 'Hutchinson, C. K' (exact)
- [PASS] initials: bio ['C', 'K'] ~ stint ['C', 'K']
- [PASS] age_gate: stint starts 1933, birth 1902 (age 31)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1939
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

