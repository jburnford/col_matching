<!-- {"case_id": "case_higgins_samuel-victor_b1898", "bio_ids": ["higgins_samuel-victor_b1898"], "stint_ids": ["Higgins, S. V___Jamaica___1937", "Higgins, S. V___Jamaica___1949"]} -->
# Dossier case_higgins_samuel-victor_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `higgins_samuel-victor_b1898`

- Printed name: **HIGGINS, Samuel Victor**
- Birth year: 1898 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32881.v` — printed in editions [1949, 1950, 1951]:**

> HIGGINS, Samuel Victor.—b. 1898; ed. Newport, Co. Down, Lisburn Methodist Coll., Co. Antrim, N. Ireland; on mil. serv. 1914-19; S.S.M., Jca. constab., 1924; sub. inspr., 1932; 3rd cl. inspr., 1935; 2nd cl., 1940; 1st cl., 1943; seconded as ch. immig. offr.; security offr. and ch. aliens offr., 1939-45.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | S.S.M., Jca. constab | Jamaica | [1949, 1950, 1951] |
| 1 | 1932 | sub. inspr | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1935 | 3rd cl. inspr | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 3 | 1939–1945 | security offr. and ch. aliens offr | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 4 | 1940 | 2nd cl | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 5 | 1943 | 1st cl | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Higgins, S. V___Jamaica___1937`

- Staff-list name: **Higgins, S. V** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | S. V. Higgins | 3rd Class Inspector | Jamaica Constabulary | — | — |
| 1940 | S. V. Higgins | 3rd Class Inspector | Jamaica Constabulary | — | — |

### Deterministic checks: `higgins_samuel-victor_b1898` vs `Higgins, S. V___Jamaica___1937`

- [PASS] surname_gate: bio 'HIGGINS' vs stint 'Higgins, S. V' (exact)
- [PASS] initials: bio ['S', 'V'] ~ stint ['S', 'V']
- [PASS] age_gate: stint starts 1937, birth 1898 (age 39)
- [PASS] colony: 6 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1937-1940
- [PASS] position_sim: best 77 vs bar 60: '3rd cl. inspr' ~ '3rd Class Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Higgins, S. V___Jamaica___1949`

- Staff-list name: **Higgins, S. V** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. V. Higgins | Superintendents of Police | POLICE | — | — |
| 1950 | S. V. Higgins | Superintendent of Police | Police | — | — |
| 1951 | S. V. Higgins | Superintendent of Police | POLICE | — | — |

### Deterministic checks: `higgins_samuel-victor_b1898` vs `Higgins, S. V___Jamaica___1949`

- [PASS] surname_gate: bio 'HIGGINS' vs stint 'Higgins, S. V' (exact)
- [PASS] initials: bio ['S', 'V'] ~ stint ['S', 'V']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [PASS] colony: 6 placed event(s) resolve to 'Jamaica'
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

