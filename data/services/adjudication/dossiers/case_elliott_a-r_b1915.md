<!-- {"case_id": "case_elliott_a-r_b1915", "bio_ids": ["elliott_a-r_b1915"], "stint_ids": ["Elliott, R___Kenya___1931", "Elliott, R___Sierra Leone___1949"]} -->
# Dossier case_elliott_a-r_b1915

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 72 official(s) with this surname in the graph's staff lists; 26 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Elliott, R___Kenya___1931` is also gate-compatible with biography(ies) outside this case: ['elliott_j-r_b1902', 'elliott_r_b1915'] (already linked elsewhere or filtered).
- NOTE: stint `Elliott, R___Sierra Leone___1949` is also gate-compatible with biography(ies) outside this case: ['elliott_j-r_b1902', 'elliott_r_b1915'] (already linked elsewhere or filtered).

## Biography `elliott_a-r_b1915`

- Printed name: **ELLIOTT, A. R**
- Birth year: 1915 (attested in editions [1958, 1959])
- Appears in editions: [1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1958-L22299.v` — printed in editions [1958, 1959]:**

> ELLIOTT, A. R.—b. 1915; ed. Batley Gram. Sch. and Wadham Coll., Oxford; mil. serv., 1940-46; B.M.A., Mal., 1945-46; cadet, G.C., 1946; asst. dist. comsnr., 1946; admin. offr., cl. III, 1952; cl. II, 1952; cl. I, 1955; perm. sec., 1957 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945–1946 | B.M.A. | Malaya | [1958, 1959] |
| 1 | 1946 | cadet | Gold Coast | [1958, 1959] |
| 2 | 1952 | admin. offr., cl. III | Gold Coast *(inherited from previous clause)* | [1958, 1959] |
| 3 | 1955 | cl. I | Gold Coast *(inherited from previous clause)* | [1958, 1959] |
| 4 | 1957 | perm. sec | Gold Coast *(inherited from previous clause)* | [1958, 1959] |

## Candidate stint `Elliott, R___Kenya___1931`

- Staff-list name: **Elliott, R** | colony: **Kenya** | listed 1931–1934 | editions [1931, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. Elliott | Land Assistants | Local Government, Lands and Settlement | — | — |
| 1934 | R. Elliott | Land Assistants | Provincial Administration | — | — |

### Deterministic checks: `elliott_a-r_b1915` vs `Elliott, R___Kenya___1931`

- [PASS] surname_gate: bio 'ELLIOTT' vs stint 'Elliott, R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1931, birth 1915 (age 16)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Elliott, R___Sierra Leone___1949`

- Staff-list name: **Elliott, R** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. Elliott | Malaria Entomologist | Health | — | — |
| 1950 | R. Elliott | Malaria Entomologist | Health | — | — |
| 1951 | R. Elliott | Malaria Entomologist | Health | — | — |

### Deterministic checks: `elliott_a-r_b1915` vs `Elliott, R___Sierra Leone___1949`

- [PASS] surname_gate: bio 'ELLIOTT' vs stint 'Elliott, R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
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

