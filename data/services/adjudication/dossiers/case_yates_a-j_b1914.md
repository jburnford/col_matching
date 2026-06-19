<!-- {"case_id": "case_yates_a-j_b1914", "bio_ids": ["yates_a-j_b1914"], "stint_ids": ["Yates, A. J___Nyasaland___1949"]} -->
# Dossier case_yates_a-j_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `yates_a-j_b1914`

- Printed name: **YATES, A. J**
- Birth year: 1914 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: C.P.M (1961), Q.P.M (1964)
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1959-L29571.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> YATES, A. J., Q.P.M. (1964), C.P.M. (1961)—b. 1914; ed. Ashford Gram. Sch., and Royal Agric. Coll., Cirencester; mil. serv., 1939-42; vet. dept., Nyasa, 1939-43; asst. inspr., police, 1943; asst. supt., 1948; supt., 1954; senr., 1960; asst. comsnr., 1962-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939–1943 | vet. dept. | Nyasaland | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1943 | asst. inspr., police | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1948 | asst. supt | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1954 | supt | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1960 | senr | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 5 | 1962–1964 | asst. comsnr | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Yates, A. J___Nyasaland___1949`

- Staff-list name: **Yates, A. J** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. J. Yates | Assistant Superintendent | Police and Immigration | — | — |
| 1950 | A. J. Yates | Assistant Superintendents | Police and Immigration | — | — |
| 1951 | A. J. Yates | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `yates_a-j_b1914` vs `Yates, A. J___Nyasaland___1949`

- [PASS] surname_gate: bio 'YATES' vs stint 'Yates, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 6 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt' ~ 'Assistant Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

