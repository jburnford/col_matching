<!-- {"case_id": "case_parsley_clifford-hugh_b1893", "bio_ids": ["parsley_clifford-hugh_b1893"], "stint_ids": ["Parsley, C. H___British Guiana___1917", "Parsley, C. H___British Guiana___1924"]} -->
# Dossier case_parsley_clifford-hugh_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `parsley_clifford-hugh_b1893`

- Printed name: **PARSLEY, CLIFFORD HUGH**
- Birth year: 1893 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67453.v` — printed in editions [1940]:**

> PARSLEY, CLIFFORD HUGH.—B. 1893; apprentice P.W.D., Br. Guiana, 1910; 5th cls. offr., lands and mines, 1915; served with H.M. forces, 1915-19 (Egypt and Italy); govt. survr., 1919; ret. 1932; asst. engr., P.W.D., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | apprentice P.W.D. | British Guiana | [1940] |
| 1 | 1915 | 5th cls. offr., lands and mines | British Guiana *(inherited from previous clause)* | [1940] |
| 2 | 1919 | govt. survr | British Guiana *(inherited from previous clause)* | [1940] |
| 3 | 1932 | ret | British Guiana *(inherited from previous clause)* | [1940] |
| 4 | 1939 | asst. engr., P.W.D | British Guiana *(inherited from previous clause)* | [1940] |

## Candidate stint `Parsley, C. H___British Guiana___1917`

- Staff-list name: **Parsley, C. H** | colony: **British Guiana** | listed 1917–1921 | editions [1917, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | C. H. Parsley | 5th Class Officer | Department of Lands and Mines | — | — |
| 1919 | C. H. Parsley | 5th Class Officer | Department of Lands and Mines | — | — |
| 1920 | C. H. Parsley | Government Surveyor | Department of Lands and Mines | — | — |
| 1921 | C. H. Parsley | Government Surveyor | Department of Lands and Mines | — | — |

### Deterministic checks: `parsley_clifford-hugh_b1893` vs `Parsley, C. H___British Guiana___1917`

- [PASS] surname_gate: bio 'PARSLEY' vs stint 'Parsley, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1917, birth 1893 (age 24)
- [PASS] colony: 5 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1921
- [PASS] position_sim: best 69 vs bar 60: 'govt. survr' ~ 'Government Surveyor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Parsley, C. H___British Guiana___1924`

- Staff-list name: **Parsley, C. H** | colony: **British Guiana** | listed 1924–1930 | editions [1924, 1925, 1927, 1928, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | C. H. Parsley | Government Surveyor | Department of Lands and Mines | — | — |
| 1925 | C. H. Parsley | Government Surveyor | Department of Lands and Mines | — | — |
| 1927 | C. H. Parsley | Government Surveyors | Department of Lands and Mines. | — | — |
| 1928 | C. H. Parsley | Government Surveyor | Department of Lands and Mines | — | — |
| 1930 | C. H. Parsley | Government Surveyor | Technical Staff | — | — |

### Deterministic checks: `parsley_clifford-hugh_b1893` vs `Parsley, C. H___British Guiana___1924`

- [PASS] surname_gate: bio 'PARSLEY' vs stint 'Parsley, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1924, birth 1893 (age 31)
- [PASS] colony: 5 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1924-1930
- [PASS] position_sim: best 69 vs bar 60: 'govt. survr' ~ 'Government Surveyor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

