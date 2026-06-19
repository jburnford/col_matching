<!-- {"case_id": "case_cullen_g-s_b1905", "bio_ids": ["cullen_g-s_b1905"], "stint_ids": ["Cullen, G. S___Kenya___1949", "Cullen, G___Straits Settlements___1921"]} -->
# Dossier case_cullen_g-s_b1905

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cullen_g-s_b1905`

- Printed name: **CULLEN, G. S**
- Birth year: 1905 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L22319.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> CULLEN, G. S.—b. 1905; ed. Falkirk High Sch.; temp. asst. engrn., posts and tels. dept., Ken., 1943; P.W.D., 1944; exec. engrn., 1946; admin. asst., P.W.D., 1949; admin. sec., P.W.D., 1953. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | temp. asst. engrn., posts and tels. dept. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1944 | P.W.D | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1946 | exec. engrn | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1949 | admin. asst., P.W.D | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1953 | admin. sec., P.W.D | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Cullen, G. S___Kenya___1949`

- Staff-list name: **Cullen, G. S** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. S. Cullen | Executive Engineer, Grade II | Public Works | — | — |
| 1951 | G. S. Cullen | Administrative Assistant | Public Works | — | — |

### Deterministic checks: `cullen_g-s_b1905` vs `Cullen, G. S___Kenya___1949`

- [PASS] surname_gate: bio 'CULLEN' vs stint 'Cullen, G. S' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G', 'S']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 53 vs bar 60: 'admin. asst., P.W.D' ~ 'Administrative Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Cullen, G___Straits Settlements___1921`

- Staff-list name: **Cullen, G** | colony: **Straits Settlements** | listed 1921–1925 | editions [1921, 1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | G. Cullen | Supernumerary Assistant Superintendents | Police | — | — |
| 1922 | G. Cullen | Assistant Superintendents | Police | — | — |
| 1923 | G. Cullen | Assistant Superintendent | Police | — | — |
| 1925 | G. Cullen | Assistant Superintendents | Police | — | — |

### Deterministic checks: `cullen_g-s_b1905` vs `Cullen, G___Straits Settlements___1921`

- [PASS] surname_gate: bio 'CULLEN' vs stint 'Cullen, G' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G']
- [PASS] age_gate: stint starts 1921, birth 1905 (age 16)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

