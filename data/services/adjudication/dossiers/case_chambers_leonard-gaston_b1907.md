<!-- {"case_id": "case_chambers_leonard-gaston_b1907", "bio_ids": ["chambers_leonard-gaston_b1907"], "stint_ids": ["Chambers, L. G___Kenya___1932", "Chambers, L. G___Uganda___1949"]} -->
# Dossier case_chambers_leonard-gaston_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chambers_leonard-gaston_b1907`

- Printed name: **CHAMBERS, Leonard Gaston**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31700.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CHAMBERS, Leonard Gaston, M.Inst. Survsrs. (N.Z.).—b. 1907; ed. Wellington Coll., N.Z., Auckland Gram. Sch., and Auckland Univ.; mem. of town planning inst. of N.Z.; on naval serv. 1939-40, lieut.; staff survr., col. survr., 1930; asst. land offr., Mombasa, 1936-37; seconded to Zanz. as senr. survr., 1940-44; senr. survr., Uga., 1946; asst. dir., surveys, 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1930 | staff survr., col. survr. | — | [1948, 1949, 1950, 1951] |
| 1 | 1936–1937 | asst. land offr. | Mombasa | [1948, 1949, 1950, 1951] |
| 2 | 1939–1940 | lieut. | — | [1948, 1949, 1950, 1951] |
| 3 | 1940–1944 | senr. survr. | Zanzibar | [1948, 1949, 1950, 1951] |
| 4 | 1946–1946 | senr. survr. | Uganda | [1948, 1949, 1950, 1951] |
| 5 | 1950–1950 | asst. dir., surveys | — | [1948, 1949, 1950, 1951] |

## Candidate stint `Chambers, L. G___Kenya___1932`

- Staff-list name: **Chambers, L. G** | colony: **Kenya** | listed 1932–1940 | editions [1932, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | L. G. Chambers | Staff Surveyors | Survey and Registration Department | — | — |
| 1934 | L. G. Chambers | Staff Surveyor | Survey and Registration Department | — | — |
| 1936 | L. G. Chambers | Staff Surveyors | Local Government, Lands and Settlement | — | — |
| 1937 | L. G. Chambers | Staff Surveyors | Local Government, Lands and Settlement | — | — |
| 1939 | L. G. Chambers | Staff Surveyors | Lands and Settlement | — | — |
| 1940 | L. G. Chambers | Staff Surveyors | Lands and Settlement | — | — |

### Deterministic checks: `chambers_leonard-gaston_b1907` vs `Chambers, L. G___Kenya___1932`

- [PASS] surname_gate: bio 'CHAMBERS' vs stint 'Chambers, L. G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1932, birth 1907 (age 25)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Chambers, L. G___Uganda___1949`

- Staff-list name: **Chambers, L. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. G. Chambers | Senior Surveyors | Survey, Land and Mines | — | — |
| 1951 | L. G. Chambers | Assistant Director of Surveys, Assistant Land Officer and Assistant Commissioner of Mines | Survey, Land and Mines | — | — |

### Deterministic checks: `chambers_leonard-gaston_b1907` vs `Chambers, L. G___Uganda___1949`

- [PASS] surname_gate: bio 'CHAMBERS' vs stint 'Chambers, L. G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
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

