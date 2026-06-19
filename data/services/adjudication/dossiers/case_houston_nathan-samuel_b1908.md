<!-- {"case_id": "case_houston_nathan-samuel_b1908", "bio_ids": ["houston_nathan-samuel_b1908"], "stint_ids": ["Houston, N. S___Jamaica___1950"]} -->
# Dossier case_houston_nathan-samuel_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `houston_nathan-samuel_b1908`

- Printed name: **HOUSTON, Nathan Samuel**
- Birth year: 1908 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L39272.v` — printed in editions [1951]:**

> HOUSTON, Nathan Samuel.—b. 1908; elem. educ.; constable, J'ca., 1927; 1st cl., 1936; cpl., 1939; sergt., 1943; sergt. maj., 1946; inspr., 1949; asst. supt., police, 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | constable | Jamaica | [1951] |
| 1 | 1936 | 1st cl | Jamaica *(inherited from previous clause)* | [1951] |
| 2 | 1939 | cpl | Jamaica *(inherited from previous clause)* | [1951] |
| 3 | 1943 | sergt | Jamaica *(inherited from previous clause)* | [1951] |
| 4 | 1946 | sergt. maj | Jamaica *(inherited from previous clause)* | [1951] |
| 5 | 1949 | inspr | Jamaica *(inherited from previous clause)* | [1951] |

## Candidate stint `Houston, N. S___Jamaica___1950`

- Staff-list name: **Houston, N. S** | colony: **Jamaica** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | N. S. Houston | Assistant Superintendent of Police | Police | — | — |
| 1951 | N. S. Houston | Assistant Superintendent of Police | POLICE | — | — |

### Deterministic checks: `houston_nathan-samuel_b1908` vs `Houston, N. S___Jamaica___1950`

- [PASS] surname_gate: bio 'HOUSTON' vs stint 'Houston, N. S' (exact)
- [PASS] initials: bio ['N', 'S'] ~ stint ['N', 'S']
- [PASS] age_gate: stint starts 1950, birth 1908 (age 42)
- [PASS] colony: 6 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 28 vs bar 60: 'sergt. maj' ~ 'Assistant Superintendent of Police'
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

