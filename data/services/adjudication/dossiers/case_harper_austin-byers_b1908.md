<!-- {"case_id": "case_harper_austin-byers_b1908", "bio_ids": ["harper_austin-byers_b1908"], "stint_ids": ["Harper, A. B___Jamaica___1934", "Harper, A. B___Jamaica___1949"]} -->
# Dossier case_harper_austin-byers_b1908

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 31 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Harper, A. B___Jamaica___1934` is also gate-compatible with biography(ies) outside this case: ['harper_austin-bymes_b1908'] (already linked elsewhere or filtered).
- NOTE: stint `Harper, A. B___Jamaica___1949` is also gate-compatible with biography(ies) outside this case: ['harper_austin-bymes_b1908'] (already linked elsewhere or filtered).

## Biography `harper_austin-byers_b1908`

- Printed name: **HARPER, Austin Byers**
- Birth year: 1908 (attested in editions [1949, 1950])
- Honours: C.P.M
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32693.v` — printed in editions [1949, 1950]:**

> HARPER, Austin Byers.—b. 1908; ed. Blundell's Sch., Tiverton, Devon, and Agric. Coll., Cedars, Natal, S.A.; agric. dept., Nig., 1930-32; col. police, Jca., 1933; 3rd cl. inspr., 1938; 2nd cl., 1940; 1st cl., 1944.

**Version `col1951-L38870.v` — printed in editions [1951]:**

> HARPER, Austin Byers, C.P.M.—b. 1908; ed. Blundell's Sch., Tiverton, Devon; agric. dept., Nig., 1930-32; col. police, J'ca., 1933; supt., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1932 | agric. dept. | Nigeria | [1949, 1950, 1951] |
| 1 | 1933 | col. police | Jamaica | [1949, 1950, 1951] |
| 2 | 1938 | 3rd cl. inspr | Jamaica *(inherited from previous clause)* | [1949, 1950] |
| 3 | 1940 | 2nd cl | Jamaica *(inherited from previous clause)* | [1949, 1950] |
| 4 | 1944 | 1st cl | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Harper, A. B___Jamaica___1934`

- Staff-list name: **Harper, A. B** | colony: **Jamaica** | listed 1934–1940 | editions [1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | A. B. Harper | Sub-Inspector | Jamaica Constabulary | — | — |
| 1937 | A. B. Harper | Sub-Inspector | Jamaica Constabulary | — | — |
| 1940 | A. B. Harper | 3rd Class Inspector | Jamaica Constabulary | — | — |

### Deterministic checks: `harper_austin-byers_b1908` vs `Harper, A. B___Jamaica___1934`

- [PASS] surname_gate: bio 'HARPER' vs stint 'Harper, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1934, birth 1908 (age 26)
- [PASS] colony: 4 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1934-1940
- [PASS] position_sim: best 77 vs bar 60: '3rd cl. inspr' ~ '3rd Class Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Harper, A. B___Jamaica___1949`

- Staff-list name: **Harper, A. B** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. B. Harper | Superintendents of Police | POLICE | — | — |
| 1950 | A. B. Harper | Superintendent of Police | Police | — | — |
| 1951 | A. B. Harper | Superintendent of Police | POLICE | — | — |

### Deterministic checks: `harper_austin-byers_b1908` vs `Harper, A. B___Jamaica___1949`

- [PASS] surname_gate: bio 'HARPER' vs stint 'Harper, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1949, birth 1908 (age 41)
- [PASS] colony: 4 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 13 vs bar 60: '1st cl' ~ 'Superintendent of Police'
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

