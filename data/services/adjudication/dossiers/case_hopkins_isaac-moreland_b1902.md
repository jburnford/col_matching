<!-- {"case_id": "case_hopkins_isaac-moreland_b1902", "bio_ids": ["hopkins_isaac-moreland_b1902"], "stint_ids": ["Hopkins, I. M___Trinidad and Tobago___1937"]} -->
# Dossier case_hopkins_isaac-moreland_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hopkins_isaac-moreland_b1902`

- Printed name: **HOPKINS, ISAAC MORELAND**
- Birth year: 1902 (attested in editions [1962])
- Appears in editions: [1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1962-L22439.v` — printed in editions [1962]:**

> HOPKINS, I. M.—b. 1902; ed. Bellahouston Acad., Jordan Hill Coll. for Teachers, and Univ. of Glasgow; prin., govt. training coll. for teachers, Trin., 1935; asst. dir., educ., 1947; dep. dir., 1950; dir., 1954-61.

**Version `col1936-L61689.v` — printed in editions [1936, 1937, 1939, 1940]:**

> HOPKINS, ISAAC MORELAND, B.Sc., (Glasgow).—B. 1902; ed. Bellahouston Acad., Univ. of Glasgow, Jordan Hill Coll. for Teachers; prin., govt. training coll. for teachers, Trinidad, 1935; supt., tech. classes, 1937; mem., bd. of induc. training, 1937.

**Version `col1948-L33444.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]:**

> HOPKINS, Isaac Moreland, B.Sc. (Glasgow).—b. 1902; ed. Bellahouston Acad., Glasgow, Univ. of Glasgow and Jordan Hill Coll. for Teachers, Glasgow; prin., gov. training coll. for teachers, Trin., 1935; asst. dir., educ., 1947; supt., tech. educ. and vocational training centre for ex-service men; chmn. and mem. of educ. and industrial training comtes.; supt. of tech. classes; author of Vocational Education in Trinidad.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | prin., govt. training coll. for teachers | Trinidad | [1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1937 | supt., tech. classes | Trinidad *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |
| 2 | 1947 | asst. dir., educ | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1950 | dep. dir | Trinidad *(inherited from previous clause)* | [1962] |
| 4 | 1954–1961 | dir | Trinidad *(inherited from previous clause)* | [1962] |

## Candidate stint `Hopkins, I. M___Trinidad and Tobago___1937`

- Staff-list name: **Hopkins, I. M** | colony: **Trinidad and Tobago** | listed 1937–1954 | editions [1937, 1939, 1940, 1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | I. M. Hopkins | Principal and Lecturer in Pedagogy | Government Training College | — | — |
| 1939 | I. M. Hopkins | Principal and Lecturer in Pedagogy | Government Training College | — | — |
| 1940 | I. M. Hopkins | Principal and Lecturer in Pedagogy | Government Training College | — | — |
| 1949 | I. M. Hopkins | Assistant Director of Education (Administrative) | Education | — | — |
| 1953 | I. M. Hopkins | Deputy Director | Civil Establishment | — | — |
| 1954 | I. M. Hopkins | Deputy Director | Civil Establishment | — | — |

### Deterministic checks: `hopkins_isaac-moreland_b1902` vs `Hopkins, I. M___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'HOPKINS' vs stint 'Hopkins, I. M' (exact)
- [PASS] initials: bio ['I', 'M'] ~ stint ['I', 'M']
- [PASS] age_gate: stint starts 1937, birth 1902 (age 35)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1954
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

