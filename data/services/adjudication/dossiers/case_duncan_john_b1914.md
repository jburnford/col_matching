<!-- {"case_id": "case_duncan_john_b1914", "bio_ids": ["duncan_john_b1914"], "stint_ids": ["Duncan, J. A. A___Sierra Leone___1931", "Duncan, John___Hong Kong___1949"]} -->
# Dossier case_duncan_john_b1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 40 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['duncan_john_b1914'] carry a single initial only — the namesake trap applies.

## Biography `duncan_john_b1914`

- Printed name: **DUNCAN, John**
- Birth year: 1914 (attested in editions [1955, 1956, 1957, 1958, 1959])
- Appears in editions: [1950, 1951, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1955-L20493.v` — printed in editions [1955, 1956, 1957, 1958, 1959]:**

> DUNCAN, J.—b. 1914; ed. Dunfermline High Sch., Edin., Munich and Rostock Univs., Sorbonne and Exeter Coll., Oxford; mil. serv., 1940-43, capt.; cadet, G.C., 1938; asst. dist. comsnr., 1939; dist. comsnr., 1945; admin. offr., cl. II, 1951; cl. I, 1953-58 (Ghana civil service).

**Version `col1950-L35119.v` — printed in editions [1950, 1951]:**

> DUNCAN, John.—b. 1914; ed. Dunfermline High Sch., Edin. Univ., Munich and Rostock Univs., and the Sorbonne; on mil. serv., 1940-43; admin. cadet, G.C., 1938; asst. dist. comsnr., 1939; dist. comsnr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | cadet | Gold Coast | [1950, 1951, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1939 | asst. dist. comsnr | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1955, 1956, 1957, 1958, 1959] |
| 2 | 1945 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1955, 1956, 1957, 1958, 1959] |
| 3 | 1951 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959] |
| 4 | 1953–1958 | cl. I | Gold Coast *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959] |

## Candidate stint `Duncan, J. A. A___Sierra Leone___1931`

- Staff-list name: **Duncan, J. A. A** | colony: **Sierra Leone** | listed 1931–1937 | editions [1931, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. A. A. Duncan | Assistant Director, Health Service | Health Department | — | — |
| 1933 | J. A. A. Duncan | Assistant Director, Health Service | Health Department | — | — |
| 1934 | J. A. A. Duncan | Assistant Director, Health Service | Health Department | — | — |
| 1936 | J. A. A. Duncan | Assistant Director, Medical Services | Health Department | — | — |
| 1937 | J. A. A. Duncan | Assistant Director, Medical Services | Health Branch | — | — |

### Deterministic checks: `duncan_john_b1914` vs `Duncan, J. A. A___Sierra Leone___1931`

- [PASS] surname_gate: bio 'DUNCAN' vs stint 'Duncan, J. A. A' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'A', 'A']
- [PASS] age_gate: stint starts 1931, birth 1914 (age 17)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1937
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Duncan, John___Hong Kong___1949`

- Staff-list name: **Duncan, John** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. H. S. Duncan | Surveyors of Ships | Surveyors of Ships Office | — | — |
| 1950 | J. H. S. Duncan | Surveyor of Ships | Marine | — | — |
| 1951 | J. H. S. Duncan | Surveyor of Ships | Marine | — | — |

### Deterministic checks: `duncan_john_b1914` vs `Duncan, John___Hong Kong___1949`

- [PASS] surname_gate: bio 'DUNCAN' vs stint 'Duncan, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
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

