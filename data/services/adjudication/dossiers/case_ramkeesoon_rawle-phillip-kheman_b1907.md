<!-- {"case_id": "case_ramkeesoon_rawle-phillip-kheman_b1907", "bio_ids": ["ramkeesoon_rawle-phillip-kheman_b1907"], "stint_ids": ["Ramkeesoon, Rawle___Trinidad and Tobago___1933", "Ramkeesoon, Rawle___Trinidad and Tobago___1953"]} -->
# Dossier case_ramkeesoon_rawle-phillip-kheman_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ramkeesoon_rawle-phillip-kheman_b1907`

- Printed name: **RAMKEESOON, Rawle Phillip Kheman**
- Birth year: 1907 (attested in editions [1951])
- Honours: L.C.P
- Appears in editions: [1951, 1956, 1957, 1959]

### Verbatim printed entry text (OCR)

**Version `col1951-L41839.v` — printed in editions [1951]:**

> RAMKEESOON, Rawle Phillip Kheman, B.A. (hons.), Lond., L.C.P.—b. 1907; ed. Queen's Royal Coll., Trin. and Lond. Univ.; asst. inspr., schs., Trin., 1931; inspr., 1936; ch. inspr., 1947.

**Version `col1956-L23673.v` — printed in editions [1956, 1957, 1959]:**

> RAMKEESOON, R. P. K.—b. 1907; ed. Queen’s Royal Coll., Trin., and Lond. Univ.; asst. inspr., schs., Trin., 1931; chief inspr., 1947; asst. dir., educ., 1950–58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | asst. inspr., schs. | Trinidad | [1951, 1956, 1957, 1959] |
| 1 | 1936 | inspr | Trinidad *(inherited from previous clause)* | [1951] |
| 2 | 1947 | ch. inspr | Trinidad *(inherited from previous clause)* | [1951, 1956, 1957, 1959] |
| 3 | 1950–1958 | asst. dir., educ | Trinidad *(inherited from previous clause)* | [1956, 1957, 1959] |

## Candidate stint `Ramkeesoon, Rawle___Trinidad and Tobago___1933`

- Staff-list name: **Ramkeesoon, Rawle** | colony: **Trinidad and Tobago** | listed 1933–1940 | editions [1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | Rawle Ramkeesoon | Assistant Inspector | Department of Education | — | — |
| 1934 | Rawle Ramkeesoon | Assistant Inspectors | Department of Education | — | — |
| 1937 | Rawle Ramkeesoon | Assistant Inspector | Department of Education | — | — |
| 1939 | Rawle Ramkeesoon | Assistant Inspector | Department of Education | — | — |
| 1940 | R. Ramkeesoon | Inspector of Schools | Education | — | — |

### Deterministic checks: `ramkeesoon_rawle-phillip-kheman_b1907` vs `Ramkeesoon, Rawle___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'RAMKEESOON' vs stint 'Ramkeesoon, Rawle' (exact)
- [PASS] initials: bio ['R', 'P', 'K'] ~ stint ['R']
- [PASS] age_gate: stint starts 1933, birth 1907 (age 26)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ramkeesoon, Rawle___Trinidad and Tobago___1953`

- Staff-list name: **Ramkeesoon, Rawle** | colony: **Trinidad and Tobago** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | R. Ramkeesoon | Assistant Director (Administrative) | Civil Establishment | — | — |
| 1954 | R. Ramkeesoon | Assistant Director (Administrative) | Civil Establishment | — | — |

### Deterministic checks: `ramkeesoon_rawle-phillip-kheman_b1907` vs `Ramkeesoon, Rawle___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'RAMKEESOON' vs stint 'Ramkeesoon, Rawle' (exact)
- [PASS] initials: bio ['R', 'P', 'K'] ~ stint ['R']
- [PASS] age_gate: stint starts 1953, birth 1907 (age 46)
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

