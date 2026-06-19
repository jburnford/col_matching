<!-- {"case_id": "case_maciver_agnes-r_b1889", "bio_ids": ["maciver_agnes-r_b1889"], "stint_ids": ["MacIver, A. R___Straits Settlements___1922"]} -->
# Dossier case_maciver_agnes-r_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maciver_agnes-r_b1889`

- Printed name: **MACIVER, AGNES R**
- Birth year: 1889 (attested in editions [1925, 1928])
- Appears in editions: [1925, 1928]

### Verbatim printed entry text (OCR)

**Version `col1925-L57570.v` — printed in editions [1925, 1928]:**

> MACIVER, AGNES R., M.A. hon.—B. 1889; ed., Geo. Watson's Ladies' Coll., Edinburgh. High Schl., Weimar, Germany, Normal Schl., Melun, France, Edinburgh Univ. (1st cls. hon., mod. lang.), 1914; educn., dipl., Edinburgh Univ., 1915; lady supervisor, Malay girls' schls., S.S. and F.M.S., 1918; Malay certif., Schl. of Oriental Studies, 1919; passed 2nd standard, Malay, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | educn., dipl., Edinburgh Univ | — | [1925, 1928] |
| 1 | 1918 | lady supervisor, Malay girls' schls., S.S. and F.M.S | Straits Settlements | [1925, 1928] |
| 2 | 1919 | Malay certif., Schl. of Oriental Studies | Straits Settlements *(inherited from previous clause)* | [1925, 1928] |
| 3 | 1920 | passed 2nd standard, Malay | Straits Settlements *(inherited from previous clause)* | [1925, 1928] |

## Candidate stint `MacIver, A. R___Straits Settlements___1922`

- Staff-list name: **MacIver, A. R** | colony: **Straits Settlements** | listed 1922–1925 | editions [1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. R. MacIver | Lady Supervisor of Malay Girls' School, S.S. & F.M.S. | Education | — | — |
| 1925 | Miss A. R. MacIver | Lady Supervisor of Malay Girls' School, S.S. & F.M.S. | Education | — | — |

### Deterministic checks: `maciver_agnes-r_b1889` vs `MacIver, A. R___Straits Settlements___1922`

- [PASS] surname_gate: bio 'MACIVER' vs stint 'MacIver, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1922, birth 1889 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 38 vs bar 60: 'passed 2nd standard, Malay' ~ 'Lady Supervisor of Malay Girls' School, S.S. & F.M.S.'
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

