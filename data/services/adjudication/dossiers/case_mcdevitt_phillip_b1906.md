<!-- {"case_id": "case_mcdevitt_phillip_b1906", "bio_ids": ["mcdevitt_phillip_b1906"], "stint_ids": ["McDevitt, P___Gambia___1933", "McDevitt, P___Gold Coast___1949"]} -->
# Dossier case_mcdevitt_phillip_b1906

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcdevitt_phillip_b1906'] carry a single initial only — the namesake trap applies.

## Biography `mcdevitt_phillip_b1906`

- Printed name: **McDEVITT, Phillip**
- Birth year: 1906 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L34238.v` — printed in editions [1948, 1949]:**

> McDEVITT, Phillip.—b. 1906; ed. Clydebank High Sch. and Glasgow Univ., M.A.; apptd. to col. med. and health servs., T.T., 1930; Gam., 1932; collectr. of customs, G.C., 1940; seconded to supplies dept., 1943-44; polit. admin., 1944-46.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | apptd. to col. med. and health servs., T.T | — | [1948, 1949] |
| 1 | 1932 | Gam | — | [1948, 1949] |
| 2 | 1940 | collectr. of customs | Gold Coast | [1948, 1949] |
| 3 | 1943–1944 | seconded to supplies dept | Gold Coast *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1944–1946 | polit. admin | Gold Coast *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `McDevitt, P___Gambia___1933`

- Staff-list name: **McDevitt, P** | colony: **Gambia** | listed 1933–1940 | editions [1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | P. McDevitt | Assistant Sanitary Inspector | Health Department | — | — |
| 1934 | P. McDevitt | Assistant Sanitary Inspector | Health Department | — | — |
| 1936 | P. McDevitt | Sanitary Superintendent | Health Department | — | — |
| 1937 | P. McDevitt | Sanitary Superintendent | Health Department | — | — |
| 1939 | P. McDevitt | Sanitary Superintendent | Health Department | — | — |
| 1940 | P. McDevitt | Sanitary Superintendent | Health Department | — | — |

### Deterministic checks: `mcdevitt_phillip_b1906` vs `McDevitt, P___Gambia___1933`

- [PASS] surname_gate: bio 'McDEVITT' vs stint 'McDevitt, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1933, birth 1906 (age 27)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McDevitt, P___Gold Coast___1949`

- Staff-list name: **McDevitt, P** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. McDevitt | Senior Collectors | Customs and Excise | — | — |
| 1950 | P. McDevitt | Senior Collectors | Customs and Excise | — | — |
| 1951 | P. McDevitt | Senior Collectors of Customs and Excise | Customs and Excise Department | — | — |

### Deterministic checks: `mcdevitt_phillip_b1906` vs `McDevitt, P___Gold Coast___1949`

- [PASS] surname_gate: bio 'McDEVITT' vs stint 'McDevitt, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
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

