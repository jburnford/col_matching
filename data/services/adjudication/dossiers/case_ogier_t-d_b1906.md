<!-- {"case_id": "case_ogier_t-d_b1906", "bio_ids": ["ogier_t-d_b1906"], "stint_ids": ["Ogier, T. D___Trinidad and Tobago___1933"]} -->
# Dossier case_ogier_t-d_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ogier_t-d_b1906`

- Printed name: **OGIER, T. D**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951, 1954, 1955])
- Appears in editions: [1948, 1949, 1950, 1951, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1948-L35001.v` — printed in editions [1948, 1949, 1950, 1951, 1954, 1955]:**

> OGIER, T. D.—b. 1906; ed. Elizabeth Coll.; sub-inspr., police, Trin., 1926; inspr., 1937; senr. supt., 1939; asst. comsnr., 1951; mem., liquor reform comtee.

**Version `col1956-L23317.v` — printed in editions [1956]:**

> OGIER, T. D.—b. 1906 ; ed. Elizabeth Coll. ; asst. supt., police, Trin., 1926 ; supt., 1937 ; senr. supt., 1939 ; asst. comsnr., 1952 ; mem., comtees. on fisheries and wild life protection and spec. comtee. to revise Clubs and Hotels ordnec.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | sub-inspr., police | Trinidad | [1948, 1949, 1950, 1951, 1954, 1955, 1956] |
| 1 | 1937 | inspr | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956] |
| 2 | 1939 | senr. supt | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956] |
| 3 | 1951 | asst. comsnr | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955] |
| 4 | 1952 | asst. comsnr | Trinidad *(inherited from previous clause)* | [1956] |

## Candidate stint `Ogier, T. D___Trinidad and Tobago___1933`

- Staff-list name: **Ogier, T. D** | colony: **Trinidad and Tobago** | listed 1933–1949 | editions [1933, 1934, 1937, 1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | T. D. Ogier | Sub-Inspector | Constabulary and Gaols | — | — |
| 1934 | T. D. Ogier | Sub-Inspector | Constabulary and Gaols | — | — |
| 1937 | T. D. Ogier | Senior Sub-Inspectors | Constabulary | — | — |
| 1939 | T. D. Ogier | Superintendent | Police | — | — |
| 1940 | T. D. Ogier | Superintendent | Police | — | Captain |
| 1949 | T. D. Ogier | Superintendents | Police | — | — |

### Deterministic checks: `ogier_t-d_b1906` vs `Ogier, T. D___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'OGIER' vs stint 'Ogier, T. D' (exact)
- [PASS] initials: bio ['T', 'D'] ~ stint ['T', 'D']
- [PASS] age_gate: stint starts 1933, birth 1906 (age 27)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1949
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

