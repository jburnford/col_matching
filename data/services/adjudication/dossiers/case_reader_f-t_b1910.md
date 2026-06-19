<!-- {"case_id": "case_reader_f-t_b1910", "bio_ids": ["reader_f-t_b1910"], "stint_ids": ["Reader, F. T___Uganda___1940"]} -->
# Dossier case_reader_f-t_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reader_f-t_b1910`

- Printed name: **READER, F. T**
- Birth year: 1910 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Honours: C.P.M (1935), K.P.M (1935)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L26274.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> READER, F. T., K.P.M. (1935), C.P.M. (1935).—b. 1910; ed. City of London Sch.; constable, Pal., 1933; asst. inspr., police, Uga., 1938; asst. supt., 1949; senr. supt., 1956-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | constable | Palestine | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1938 | asst. inspr., police | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1949 | asst. supt | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1956–1962 | senr. supt | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Reader, F. T___Uganda___1940`

- Staff-list name: **Reader, F. T** | colony: **Uganda** | listed 1940–1951 | editions [1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | F. T. Reader | Assistant Inspector | Police | — | — |
| 1949 | F. T. Reader | Chief Inspectors | Police | — | — |
| 1951 | F. T. Reader | Superintendents, Assistants and Cadets | Police | — | — |

### Deterministic checks: `reader_f-t_b1910` vs `Reader, F. T___Uganda___1940`

- [PASS] surname_gate: bio 'READER' vs stint 'Reader, F. T' (exact)
- [PASS] initials: bio ['F', 'T'] ~ stint ['F', 'T']
- [PASS] age_gate: stint starts 1940, birth 1910 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1940-1951
- [FAIL] position_sim: best 57 vs bar 60: 'asst. supt' ~ 'Assistant Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

