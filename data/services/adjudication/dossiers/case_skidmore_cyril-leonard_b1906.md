<!-- {"case_id": "case_skidmore_cyril-leonard_b1906", "bio_ids": ["skidmore_cyril-leonard_b1906"], "stint_ids": ["Skidmore, C. L___Gold Coast___1932"]} -->
# Dossier case_skidmore_cyril-leonard_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `skidmore_cyril-leonard_b1906`

- Printed name: **SKIDMORE, Cyril Leonard**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951])
- Honours: A.I.C.T.A
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35922.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SKIDMORE, Cyril Leonard, B.Sc. (agric.), dip. agric. (S.E.A.C.), A.I.C.T.A.—b. 1906; ed. S.E. Agric. Coll., Wye, Agric. Econ. Research Inst., Oxford and I.C.T.A.; on mil. serv., 1939-43; agric. offr., G.C., 1928; senr., 1939; asst. dir., agric., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | agric. offr. | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1939 | senr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1946 | asst. dir., agric | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Skidmore, C. L___Gold Coast___1932`

- Staff-list name: **Skidmore, C. L** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | C. L. Skidmore | Statistics and Surveys | Divisions | — | — |
| 1934 | C. L. Skidmore | Superintendents and Assistant Superintendents | Agricultural Staff | — | — |
| 1936 | C. L. Skidmore | Superintendent/Assistant Superintendent | Agricultural Staff | — | — |

### Deterministic checks: `skidmore_cyril-leonard_b1906` vs `Skidmore, C. L___Gold Coast___1932`

- [PASS] surname_gate: bio 'SKIDMORE' vs stint 'Skidmore, C. L' (exact)
- [PASS] initials: bio ['C', 'L'] ~ stint ['C', 'L']
- [PASS] age_gate: stint starts 1932, birth 1906 (age 26)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1932-1936
- [FAIL] position_sim: best 31 vs bar 60: 'agric. offr.' ~ 'Statistics and Surveys'
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

