<!-- {"case_id": "case_ford_frank_b1873", "bio_ids": ["ford_frank_b1873"], "stint_ids": ["Ford, F. M___Tanganyika___1922", "Ford, H. F___South Africa___1912"]} -->
# Dossier case_ford_frank_b1873

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 48 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ford_frank_b1873'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Ford, H. F___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['ford_henry-francis_e1868'] (already linked elsewhere or filtered).

## Biography `ford_frank_b1873`

- Printed name: **FORD, FRANK**
- Birth year: 1873 (attested in editions [1911])
- Honours: D.C.L, K.C
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L44744.v` — printed in editions [1911]:**

> FORD, FRANK, K.C., D.C.L.—B. 1873; ed. Toronto, pub. schls., Ontario Acad.; B.C.L., Univ.; Ontario law schl., Osgoode Hall, Toronto; called to the bar, Ontario, 1895; priv. sec. and "devil" to the late D'Alton McCarthy, Q.C., M.P., 1893 to 1897; priv. sec. to premier and atty-gen., Ontario, 1899; solr. to the treasury, Ontario, 1901; dep. atty-gen., Sask., 1906; called to the bar, N.W.T., 1906; lt.-col. commanding 95th Saskatchewan Rifles.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893–1897 | priv. sec. and "devil" to the late D'Alton McCarthy, Q.C., M.P | Ontario *(inherited from previous clause)* | [1911] |
| 1 | 1895 | called to the bar | Ontario | [1911] |
| 2 | 1899 | priv. sec. to premier and atty-gen. | Ontario | [1911] |
| 3 | 1901 | solr. to the treasury | Ontario | [1911] |
| 4 | 1906 | dep. atty-gen., Sask | Ontario *(inherited from previous clause)* | [1911] |

## Candidate stint `Ford, F. M___Tanganyika___1922`

- Staff-list name: **Ford, F. M** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | F. M. Ford | Junior Staff Surveyors | Land, Survey and Mines Department | — | Captain |
| 1923 | F. M. Ford | Senior Staff Surveyor | Land, Survey and Mines Department | — | — |
| 1924 | F. M. Ford | Senior Staff Surveyor | Land, Survey and Mines Department | — | — |
| 1925 | F. M. Ford | Senior Staff Surveyor | Land, Survey and Mines Department | — | — |

### Deterministic checks: `ford_frank_b1873` vs `Ford, F. M___Tanganyika___1922`

- [PASS] surname_gate: bio 'FORD' vs stint 'Ford, F. M' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F', 'M']
- [PASS] age_gate: stint starts 1922, birth 1873 (age 49)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ford, H. F___South Africa___1912`

- Staff-list name: **Ford, H. F** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | H. F. Ford | Registrar and Master | Supreme Court of South Africa | — | — |
| 1914 | H. F. Ford | Registrar and Master | Griqualand West Local Division | — | — |

### Deterministic checks: `ford_frank_b1873` vs `Ford, H. F___South Africa___1912`

- [PASS] surname_gate: bio 'FORD' vs stint 'Ford, H. F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['H', 'F']
- [PASS] age_gate: stint starts 1912, birth 1873 (age 39)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

