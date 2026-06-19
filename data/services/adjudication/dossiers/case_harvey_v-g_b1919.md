<!-- {"case_id": "case_harvey_v-g_b1919", "bio_ids": ["harvey_v-g_b1919"], "stint_ids": ["Harvey, V. G___Uganda___1949"]} -->
# Dossier case_harvey_v-g_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 59 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harvey_v-g_b1919`

- Printed name: **HARVEY, V. G**
- Birth year: 1919 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L23051.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> HARVEY, V. G., B.E.M. (Mil.).—b. 1919; ed. North St. Council Sch., Colchester; mil. serv., 1939-47, W.O. cl. I; apptd. prisons dept., Uga., 1947; senr. asst. supt., 1951; supt., 1955; dist. supt., 1958; prisons advr., Buganda kingdom, 1958-59; senr. supt., 1961. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | apptd. prisons dept. | Uganda | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1951 | senr. asst. supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1955 | supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1958 | dist. supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | senr. supt | Uganda *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Harvey, V. G___Uganda___1949`

- Staff-list name: **Harvey, V. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | V. G. Harvey | Assistant Superintendents | Prisons | — | — |
| 1951 | V. G. Harvey | Assistant Superintendents | Prisons | — | — |

### Deterministic checks: `harvey_v-g_b1919` vs `Harvey, V. G___Uganda___1949`

- [PASS] surname_gate: bio 'HARVEY' vs stint 'Harvey, V. G' (exact)
- [PASS] initials: bio ['V', 'G'] ~ stint ['V', 'G']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 5 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 51 vs bar 60: 'senr. asst. supt' ~ 'Assistant Superintendents'
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

