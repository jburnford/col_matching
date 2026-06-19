<!-- {"case_id": "case_loinsworth_robert-carlton_b1902", "bio_ids": ["loinsworth_robert-carlton_b1902"], "stint_ids": ["Loinsworth, R. C___Trinidad and Tobago___1937"]} -->
# Dossier case_loinsworth_robert-carlton_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `loinsworth_robert-carlton_b1902`

- Printed name: **LOINSWORTH, Robert Carlton**
- Birth year: 1902 (attested in editions [1956, 1957])
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L22608.v` — printed in editions [1956, 1957]:**

> LOINSWORTH, R. C.—b. 1902; ed. Queen's Royal Coll., Trin., and Bristol Univ.; asst. master, Queen's Royal Coll., Trin., 1935; supt., exams., 1950; asst. dir., educ., 1954.

**Version `col1948-L34123.v` — printed in editions [1948, 1949, 1950, 1951]:**

> LOINSWORTH, Robert Carlton.—b. 1902; ed. Queen’s Royal Coll., Trinidad, Bristol Univ., B.A. (French), dip. super., Paris Univ., dip. educ., Bristol Univ.; asst. mstr., Queen’s Royal Coll., 1935; supt. of examination, Trin., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | asst. master, Queen's Royal Coll. | Trinidad | [1948, 1949, 1950, 1951, 1956, 1957] |
| 1 | 1945 | supt. of examination | Trinidad | [1948, 1949, 1950, 1951] |
| 2 | 1950 | supt., exams | Trinidad *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1954 | asst. dir., educ | Trinidad *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Loinsworth, R. C___Trinidad and Tobago___1937`

- Staff-list name: **Loinsworth, R. C** | colony: **Trinidad and Tobago** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | R. C. Loinsworth | Assistant Master | Queen's Royal College | — | — |
| 1939 | R. C. Loinsworth | Assistant Master | Queen's Royal College | — | — |
| 1940 | R. C. Loinsworth | Master | Queen's Royal College | — | — |

### Deterministic checks: `loinsworth_robert-carlton_b1902` vs `Loinsworth, R. C___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'LOINSWORTH' vs stint 'Loinsworth, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1937, birth 1902 (age 35)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
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

