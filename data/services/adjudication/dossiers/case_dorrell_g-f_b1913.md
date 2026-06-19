<!-- {"case_id": "case_dorrell_g-f_b1913", "bio_ids": ["dorrell_g-f_b1913"], "stint_ids": ["Dorrell, G. F___Uganda___1949"]} -->
# Dossier case_dorrell_g-f_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dorrell_g-f_b1913`

- Printed name: **DORRELL, G. F**
- Birth year: 1913 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L22620.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> DORRELL, G. F.—b. 1913; ed. Prince of Wales Sch., Kenya; asst. engrnr., P.W.D., Uga., 1937; secon. for duty with air min. during war; asst. dir. (bdgds.), P.W.D., Uga., 1951; asst. dir. (roads), 1959; dep. engrnr.-in-chief, min. of wks., 1960; perm. sec. and engrnr.-in-chief, 1962. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | asst. engrnr., P.W.D. | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1951 | asst. dir. (bdgds.), P.W.D. | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1959 | asst. dir. (roads) | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1960 | dep. engrnr.-in-chief, min. of wks | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1962 | perm. sec. and engrnr.-in-chief | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Dorrell, G. F___Uganda___1949`

- Staff-list name: **Dorrell, G. F** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. F. Dorrell | Executive Engineers and Assistant Engineers | Public Works | — | — |
| 1951 | G. F. Dorrell | Executive Engineers and Assistant Engineers | Public Works | — | — |

### Deterministic checks: `dorrell_g-f_b1913` vs `Dorrell, G. F___Uganda___1949`

- [PASS] surname_gate: bio 'DORRELL' vs stint 'Dorrell, G. F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 5 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 46 vs bar 60: 'asst. engrnr., P.W.D.' ~ 'Executive Engineers and Assistant Engineers'
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

