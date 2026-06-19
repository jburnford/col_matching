<!-- {"case_id": "case_mcmurdo_r_b1914", "bio_ids": ["mcmurdo_r_b1914"], "stint_ids": ["McMurdo, R___British Honduras___1964"]} -->
# Dossier case_mcmurdo_r_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcmurdo_r_b1914'] carry a single initial only — the namesake trap applies.

## Biography `mcmurdo_r_b1914`

- Printed name: **McMURDO, R**
- Birth year: 1914 (attested in editions [1957, 1959, 1960, 1961, 1962])
- Appears in editions: [1957, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L25389.v` — printed in editions [1957, 1959, 1960, 1961, 1962]:**

> McMURDO, R.—b. 1914; Cumnock Academy and Glasgow Univ.; mil. serv., 1940-46, sub-lt. R.N.; educ. offr., S.L., 1950; dep. dir., educ., Trin., 1956-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1956–1961 | dep. dir., educ. | Trinidad | [1957, 1959, 1960, 1961, 1962] |

## Candidate stint `McMurdo, R___British Honduras___1964`

- Staff-list name: **McMurdo, R** | colony: **British Honduras** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | R. McMurdo | Chief Education Officer | Civil Establishment | — | — |
| 1965 | R. McMurdo | Chief Education Officer | Civil Establishment | — | — |
| 1966 | R. McMurdo | Chief Education Officer | Civil Establishment | — | — |

### Deterministic checks: `mcmurdo_r_b1914` vs `McMurdo, R___British Honduras___1964`

- [PASS] surname_gate: bio 'McMURDO' vs stint 'McMurdo, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1964, birth 1914 (age 50)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

