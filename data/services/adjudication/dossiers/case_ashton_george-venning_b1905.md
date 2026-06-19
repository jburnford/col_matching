<!-- {"case_id": "case_ashton_george-venning_b1905", "bio_ids": ["ashton_george-venning_b1905"], "stint_ids": ["Ashton, G. V___Kenya___1949"]} -->
# Dossier case_ashton_george-venning_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ashton_george-venning_b1905`

- Printed name: **ASHTON, George Venning**
- Birth year: 1905 (attested in editions [1948, 1949])
- Honours: A.R.I.C.S
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L30867.v` — printed in editions [1948, 1949]:**

> ASHTON, George Venning, A.R.I.C.S.—b. 1905; ed. West Buckland Sch., N. Devon, and Coll. of Estate Management, Lond.; on mil. serv., 1939-45, maj.; survr., Nig. surveys, 1929; staff survr., Ken., 1935; clk., land office, 1938; staff survr., 1939; commanded No. 157 Base Survey Coy., E.A.E., 1944-45.

**Version `col1950-L33301.v` — printed in editions [1950, 1951]:**

> ASHTON, George Venning, A.R.I.C.S.—b. 1905; ed. West Buckland Sch., N. Devon, and Coll. of Estate Management, Lond.; on mil. serv., 1939-45, maj.; survr., Nig. surveys, 1929; clk., lands and surveys, Ken., 1938; staff survr., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | survr., Nig. surveys | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1935 | staff survr. | Kenya | [1948, 1949] |
| 2 | 1938 | clk., land office | Kenya | [1948, 1949, 1950, 1951] |
| 3 | 1939 | staff survr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1944–1945 | commanded No. 157 Base Survey Coy., E.A.E | Kenya *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Ashton, G. V___Kenya___1949`

- Staff-list name: **Ashton, G. V** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. V. Ashton | Staff Surveyors | Surveys | — | — |
| 1950 | G. V. Ashton | Staff Surveyors | Survey of Kenya | — | — |
| 1951 | G. V. Ashton | Staff Surveyors | Survey of Kenya | — | — |

### Deterministic checks: `ashton_george-venning_b1905` vs `Ashton, G. V___Kenya___1949`

- [PASS] surname_gate: bio 'ASHTON' vs stint 'Ashton, G. V' (exact)
- [PASS] initials: bio ['G', 'V'] ~ stint ['G', 'V']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

