<!-- {"case_id": "case_graxnum_edward-t_e1883", "bio_ids": ["graxnum_edward-t_e1883"], "stint_ids": ["Grannum, E. T___Barbados___1899"]} -->
# Dossier case_graxnum_edward-t_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Grannum, E. T___Barbados___1899` is also gate-compatible with biography(ies) outside this case: ['grannum_edward-t_e1883'] (already linked elsewhere or filtered).

## Biography `graxnum_edward-t_e1883`

- Printed name: **GRAXNUM, EDWARD T**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L35185.v` — printed in editions [1900]:**

> GRAXNUM, EDWARD T.—Representative of Bridgetown, Barbados Assem., 1883; J.P., 1886; mem. exec. comttee., 1885-89, and 1890-91; mem. gen. bd. of health, 1885; deleg. to Washington as to tariff arrangements under McKinley Act, 1891; aud.-gen., Barbados, 1894; ag. col. sec. and mem. exec. comn., Aug. to Dec., 1895, and July to Nov., 1896; ag. col. sec.; mem. of exec. comn., May to Sept., 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Representative of Bridgetown, Barbados Assem | Barbados | [1900] |
| 1 | 1885–1889 | mem. exec. comttee | Barbados *(inherited from previous clause)* | [1900] |
| 2 | 1886 | J.P | Barbados *(inherited from previous clause)* | [1900] |
| 3 | 1890–1891 | mem. exec. comttee | Barbados *(inherited from previous clause)* | [1900] |
| 4 | 1891 | deleg. to Washington as to tariff arrangements under McKinley Act | Barbados *(inherited from previous clause)* | [1900] |
| 5 | 1894 | aud.-gen. | Barbados | [1900] |
| 6 | 1895 | ag. col. sec. and mem. exec. comn | Barbados *(inherited from previous clause)* | [1900] |
| 7 | 1896 | ag. col. sec. and mem. exec. comn | Barbados *(inherited from previous clause)* | [1900] |
| 8 | 1897 | mem. of exec. comn | Barbados *(inherited from previous clause)* | [1900] |

## Candidate stint `Grannum, E. T___Barbados___1899`

- Staff-list name: **Grannum, E. T** | colony: **Barbados** | listed 1899–1919 | editions [1899, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1905 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1906 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1907 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1908 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1909 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1910 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1911 | E. T. Grannum | Auditor-General | Audit Office | — | — |
| 1912 | The Hon. E. T. Grannum | Auditor-General | Audit Office | C.M.G. | — |
| 1913 | The Hon. E. T. Grannum | Auditor-General | Audit Office | C.M.G. | — |
| 1914 | E. T. Grannum | Auditor-General | Audit Office | C.M.G. | — |
| 1915 | The Hon. E. T. Grannum | Auditor-General | Audit Office | C.M.G. | — |
| 1917 | E. T. Grannum | Auditor-General | Audit Office | C.M.G. | — |
| 1918 | The Hon. E. T. Grannum | Auditor-General | Audit Office | C.M.G. | — |
| 1919 | E. T. Grannum | Auditor-General | Audit Office | C.M.G. | — |

### Deterministic checks: `graxnum_edward-t_e1883` vs `Grannum, E. T___Barbados___1899`

- [PASS] surname_gate: bio 'GRAXNUM' vs stint 'Grannum, E. T' (fuzzy:1)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 9 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1899-1919
- [FAIL] position_sim: best 20 vs bar 60: 'mem. of exec. comn' ~ 'Auditor-General'
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

