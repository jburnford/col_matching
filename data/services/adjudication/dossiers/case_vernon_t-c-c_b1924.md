<!-- {"case_id": "case_vernon_t-c-c_b1924", "bio_ids": ["vernon_t-c-c_b1924"], "stint_ids": ["Vernon, T. C. C___British Honduras___1962"]} -->
# Dossier case_vernon_t-c-c_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vernon_t-c-c_b1924`

- Printed name: **VERNON, T. C. C**
- Birth year: 1924 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22687.v` — printed in editions [1964, 1965, 1966]:**

> VERNON, T. C. C.—b. 1924; ed. St. Michael's Coll., B. Hond.; jun. clk., B. Hond., 1945; 3rd cl. clk., 1946; 1st cl. clk., 1955; asst. assr. income tax, 1957; assr., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | jun. clk. | British Honduras | [1964, 1965, 1966] |
| 1 | 1946 | 3rd cl. clk | British Honduras *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1955 | 1st cl. clk | British Honduras *(inherited from previous clause)* | [1964, 1965, 1966] |
| 3 | 1957 | asst. assr. income tax | British Honduras *(inherited from previous clause)* | [1964, 1965, 1966] |
| 4 | 1961 | assr | British Honduras *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Vernon, T. C. C___British Honduras___1962`

- Staff-list name: **Vernon, T. C. C** | colony: **British Honduras** | listed 1962–1966 | editions [1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | T. C. C. Vernon | Assessor of Income Tax | Civil Establishment | — | — |
| 1963 | T. C. C. Vernon | Assessor of Income Tax | Civil Establishment | — | — |
| 1964 | T. C. C. Vernon | Assessor of Income Tax | Civil Establishment | — | — |
| 1965 | T. C. C. Vernon | Assessor of Income Tax | Civil Establishment | — | — |
| 1966 | T. C. C. Vernon | Commissioner of Income Tax | Civil Establishment | — | — |

### Deterministic checks: `vernon_t-c-c_b1924` vs `Vernon, T. C. C___British Honduras___1962`

- [PASS] surname_gate: bio 'VERNON' vs stint 'Vernon, T. C. C' (exact)
- [PASS] initials: bio ['T', 'C', 'C'] ~ stint ['T', 'C', 'C']
- [PASS] age_gate: stint starts 1962, birth 1924 (age 38)
- [PASS] colony: 5 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1962-1966
- [PASS] position_sim: best 76 vs bar 60: 'asst. assr. income tax' ~ 'Assessor of Income Tax'
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

