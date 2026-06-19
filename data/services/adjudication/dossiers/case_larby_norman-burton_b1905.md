<!-- {"case_id": "case_larby_norman-burton_b1905", "bio_ids": ["larby_norman-burton_b1905"], "stint_ids": ["Larby, N. B___Kenya___1936"]} -->
# Dossier case_larby_norman-burton_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `larby_norman-burton_b1905`

- Printed name: **LARBY, Norman Burton**
- Birth year: 1905 (attested in editions [1950, 1951])
- Honours: O.B.E (1957)
- Appears in editions: [1950, 1951, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1950-L37143.v` — printed in editions [1950, 1951]:**

> LARBY, Norman Burton.—b. 1905; ed. Bedford Modern Sch. and Downing Coll., Camb., M.A. (Cantab.), dip. educ. (Lond.); asst. mstr., Ken., 1927; senr. educ. offr., 1947; asst. dir., educ., 1950.

**Version `col1956-L22411.v` — printed in editions [1956, 1957, 1958, 1959]:**

> LARBY, N. B., O.B.E. (1957).—b. 1905; ed. Bedford Modern Sch. and Downing Coll., Camb.; educ. offr., Ken., 1927; senr., 1947; asst. dir., educ., 1950; dep. dir., 1954-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. mstr. | Kenya | [1950, 1951] |
| 1 | 1947 | senr. educ. offr | Kenya *(inherited from previous clause)* | [1950, 1951, 1956, 1957, 1958, 1959] |
| 2 | 1950 | asst. dir., educ | Kenya *(inherited from previous clause)* | [1950, 1951, 1956, 1957, 1958, 1959] |
| 3 | 1954–1958 | dep. dir | — | [1956, 1957, 1958, 1959] |

## Candidate stint `Larby, N. B___Kenya___1936`

- Staff-list name: **Larby, N. B** | colony: **Kenya** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | N. B. Larby | Education Officer—European Education | Education | — | — |
| 1937 | N. B. Larby | Education Officer—European Education | Education | — | — |
| 1939 | N. B. Larby | Education Officer, Arab Education | Education | — | — |

### Deterministic checks: `larby_norman-burton_b1905` vs `Larby, N. B___Kenya___1936`

- [PASS] surname_gate: bio 'LARBY' vs stint 'Larby, N. B' (exact)
- [PASS] initials: bio ['N', 'B'] ~ stint ['N', 'B']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1939
- [FAIL] position_sim: best 26 vs bar 60: 'asst. mstr.' ~ 'Education Officer, Arab Education'
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

