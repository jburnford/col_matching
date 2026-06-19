<!-- {"case_id": "case_cobb_frederic_b1885", "bio_ids": ["cobb_frederic_b1885"], "stint_ids": ["Cobb, C. F___Gold Coast___1949", "Cobb, F. E___Falkland Islands___1929"]} -->
# Dossier case_cobb_frederic_b1885

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cobb_frederic_b1885'] carry a single initial only — the namesake trap applies.

## Biography `cobb_frederic_b1885`

- Printed name: **COBB, FREDERIC**
- Birth year: 1885 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L65634.v` — printed in editions [1939, 1940]:**

> COBB, FREDERIC.—B. 1885; ed. Charterhouse and Worcester Coll., Oxford; B.A. (Oxon.); European mast., F.M.S., Sept., 1921; headmast., King George V Sch., Seremban, May, 1934; European mast., Victoria Inst., K. Lumpur, Apr., 1935; headmast., high schl., B. Mertajain, Sept., 1937; snr. educn. offr., Oct., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | European mast. | Federated Malay States | [1939, 1940] |
| 1 | 1934 | headmast., King George V Sch., Seremban | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1935 | European mast., Victoria Inst., K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1937 | headmast., high schl., B. Mertajain | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Cobb, C. F___Gold Coast___1949`

- Staff-list name: **Cobb, C. F** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. F. Cobb | Senior Assistant Superintendents and Assistant Superintendents | Police | — | — |
| 1951 | C. F. Cobb | Senior Assistant Superintendent / Assistant Superintendent / Cadet | Police | — | — |

### Deterministic checks: `cobb_frederic_b1885` vs `Cobb, C. F___Gold Coast___1949`

- [PASS] surname_gate: bio 'COBB' vs stint 'Cobb, C. F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1949, birth 1885 (age 64)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Cobb, F. E___Falkland Islands___1929`

- Staff-list name: **Cobb, F. E** | colony: **Falkland Islands** | listed 1929–1936 | editions [1929, 1930, 1931, 1932, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | H. V. Cobb | Lieutenants | Military | — | Lieutenant |
| 1930 | H. V. Cobb | Lieutenant | Military Department | — | Lieutenant |
| 1931 | H. V. Cobb | Lieutenant | Military Department | — | — |
| 1932 | H. V. Cobb | Lieutenants | Military Department | — | — |
| 1933 | H. V. Cobb | Lieutenants | Military Department | — | — |
| 1934 | H. V. Cobb | Lieutenants | Military Department | — | — |
| 1936 | H. V. Cobb | Lieutenant | Military Department | — | Lieutenant |

### Deterministic checks: `cobb_frederic_b1885` vs `Cobb, F. E___Falkland Islands___1929`

- [PASS] surname_gate: bio 'COBB' vs stint 'Cobb, F. E' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1929, birth 1885 (age 44)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1936
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

