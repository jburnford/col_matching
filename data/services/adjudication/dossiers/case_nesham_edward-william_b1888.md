<!-- {"case_id": "case_nesham_edward-william_b1888", "bio_ids": ["nesham_edward-william_b1888"], "stint_ids": ["Nesham, E. W___Gold Coast___1927"]} -->
# Dossier case_nesham_edward-william_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nesham_edward-william_b1888`

- Printed name: **NESHAM, EDWARD WILLIAM**
- Birth year: 1888 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69354.v` — printed in editions [1939, 1940]:**

> NESHAM, MAJOR EDWARD WILLIAM.—B. 1888; ed. Torquay High Schl.; articled pupil, Dominion observatory, Ottawa, Canada, 1909-13; Canadian govt. dept. of the Int. Internat. Bdy. survey br. of Dominion observatory, 1909-14; geodetic engr., 1919; R.E. 1915-20, Gallipoli, France and Germany; Croix de Guerre (French); thrice ment. in desps.; survr., survey dept., Gold Coast, 1924-36; dep. commr. lands and survr.-gen., Nigeria, Aug., 1936; ag. commr. do., 1937-38; dep. commr. of land and dir. of surveys, Apr., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909–1913 | articled pupil, Dominion observatory | Canada | [1939, 1940] |
| 1 | 1915–1920 | R.E. | — | [1939, 1940] |
| 2 | 1919–1919 | geodetic engr. | — | [1939, 1940] |
| 3 | 1924–1936 | survr., survey dept. | Gold Coast | [1939, 1940] |
| 4 | 1936–1936 | dep. commr. lands and survr.-gen. | Nigeria | [1939, 1940] |
| 5 | 1937–1938 | ag. commr. do. | Nigeria | [1939, 1940] |
| 6 | 1939–1939 | dep. commr. of land and dir. of surveys | — | [1939, 1940] |

## Candidate stint `Nesham, E. W___Gold Coast___1927`

- Staff-list name: **Nesham, E. W** | colony: **Gold Coast** | listed 1927–1934 | editions [1927, 1929, 1930, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | Major E. W. Nesham | Surveyors | Provincial Survey Sections | — | Major |
| 1929 | E. W. Nesham | Surveyors | Provincial Survey Sections | — | Major |
| 1930 | E. W. Nesham | Surveyors | Survey Department | — | Major |
| 1934 | E. W. Nesham | Surveyor | Survey Department | — | Major |

### Deterministic checks: `nesham_edward-william_b1888` vs `Nesham, E. W___Gold Coast___1927`

- [PASS] surname_gate: bio 'NESHAM' vs stint 'Nesham, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1927, birth 1888 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1934
- [FAIL] position_sim: best 56 vs bar 60: 'survr., survey dept.' ~ 'Surveyor'
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

