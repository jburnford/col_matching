<!-- {"case_id": "case_hagan_joseph-samson_e1883", "bio_ids": ["hagan_joseph-samson_e1883"], "stint_ids": ["Hagan, Joseph___Gold Coast___1890"]} -->
# Dossier case_hagan_joseph-samson_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hagan_joseph-samson_e1883`

- Printed name: **HAGAN, JOSEPH SAMSON**
- Birth year: not printed
- Appears in editions: [1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1896-L39263.v` — printed in editions [1896]:**

> HAGAN, JOSEPH SAMSON.—Ed. Wesleyan High Schl., Cape Coast; employed temporarily in various depts., Nov. 1888-85; powder magazine keeper, Accra, Oct. 1885; junr. clk. gov. off., Mar., 1887; dep. regtr. and interpr., Akuse, June, 1888; 2nd clk. gov. office, Jan., 1891; accompanied Governor on various tours of inspection; qr. mr. sergt., Gold Coast rifle vol., April, 1894.

**Version `col1897-L32333.v` — printed in editions [1897]:**

> HAGAN, JOSEPH SAMSON.—Ed. Wesleyan High Sch., Cape Coast; employed temporarily in various depts., Nov. 1883-85; powder magazine keeper, Accra, Oct. 1885; junr. clk. gov. off., Mar., 1887; dep. regr. and interpr., Akuse, June, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883–1885 | employed temporarily in various depts | — | [1897] |
| 1 | 1885 | powder magazine keeper, Accra | — | [1896, 1897] |
| 2 | 1887 | junr. clk. gov. off | — | [1896, 1897] |
| 3 | 1888–1885 | employed temporarily in various depts | — | [1896] |
| 4 | 1888 | dep. regtr. and interpr., Akuse | — | [1896, 1897] |
| 5 | 1891 | 2nd clk. gov. office | — | [1896] |
| 6 | 1894 | qr. mr. sergt., Gold Coast rifle vol | Gold Coast | [1896] |

## Candidate stint `Hagan, Joseph___Gold Coast___1890`

- Staff-list name: **Hagan, Joseph** | colony: **Gold Coast** | listed 1890–1900 | editions [1890, 1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | J. S. Hagan | Junior Clerk | Governor's Office | — | — |
| 1894 | J. S. Hagan | 2nd Clerk | Governor's Office | — | — |
| 1894 | J. A. Hagan | 2nd Class Clerks and Sorters | Post Office | — | — |
| 1896 | J. S. Hagan | Clerk | Governor's Office | — | — |
| 1898 | J. S. Hagan | Clerk | Governor's Office | — | — |
| 1899 | J. S. Hagan | Clerk | Governor's Office | — | — |
| 1900 | J. S. Hagan | 1st Clerk | Governor's Office | — | — |

### Deterministic checks: `hagan_joseph-samson_e1883` vs `Hagan, Joseph___Gold Coast___1890`

- [PASS] surname_gate: bio 'HAGAN' vs stint 'Hagan, Joseph' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1900
- [FAIL] position_sim: best 33 vs bar 60: 'qr. mr. sergt., Gold Coast rifle vol' ~ '2nd Class Clerks and Sorters'
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

