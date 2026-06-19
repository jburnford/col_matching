<!-- {"case_id": "case_semple_robert_b1876", "bio_ids": ["semple_robert_b1876", "simple_robert_b1873"], "stint_ids": ["Semple, R___Sierra Leone___1913"]} -->
# Dossier case_semple_robert_b1876

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['semple_robert_b1876', 'simple_robert_b1873'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Semple, R___Sierra Leone___1913'] have more than one claimant biography in this case.

## Biography `semple_robert_b1876`

- Printed name: **SEMPLE, ROBERT**
- Birth year: 1876 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L70519.v` — printed in editions [1939]:**

> SEMPLE, HON. ROBERT.—B. 1876; ed. Sofia Schol., N.S.W.; mem. N.Z. H. of R., 1918-19 and since 1928; min. of pub. wks. and min. of transp., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1919 | mem. N.Z. H. of R. | New Zealand | [1939] |
| 1 | 1928 | mem. N.Z. H. of R. | New Zealand | [1939] |
| 2 | 1935 | min. of pub. wks. and min. of transp. | — | [1939] |

## Biography `simple_robert_b1873`

- Printed name: **SIMPLE, Robert**
- Birth year: 1873 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L64567.v` — printed in editions [1937, 1940]:**

> SIMPLE, Hon. Robert.—B. 1873; ed. Sofala Sch., N.S.W; mem. N.Z. H. of R., 1918-19 and since 1928; min. of pub. wks. and min. of transport, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1919 | mem. N.Z. H. of R. | N.Z. | [1937, 1940] |
| 1 | 1936 | min. of pub. wks. and min. of transport | — | [1937, 1940] |

## Candidate stint `Semple, R___Sierra Leone___1913`

- Staff-list name: **Semple, R** | colony: **Sierra Leone** | listed 1913–1922 | editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | R. Semple | Medical Officer | Medical Department | — | — |
| 1914 | R. Semple | Medical Officer | Medical Department | — | — |
| 1915 | R. Semple | Medical Officer | Medical | — | — |
| 1917 | R. Semple | Medical Officer | Medical | — | — |
| 1918 | R. Semple | Medical Officer | Medical | — | — |
| 1919 | R. Semple | Medical Officers, W.A.M.S. | Medical | — | — |
| 1920 | R. Semple | Medical Officers | Medical | — | — |
| 1921 | R. Semple | Medical Officer | Medical | — | — |
| 1922 | R. Semple | Medical Officer | Medical | — | — |

### Deterministic checks: `semple_robert_b1876` vs `Semple, R___Sierra Leone___1913`

- [PASS] surname_gate: bio 'SEMPLE' vs stint 'Semple, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1913, birth 1876 (age 37)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `simple_robert_b1873` vs `Semple, R___Sierra Leone___1913`

- [PASS] surname_gate: bio 'SIMPLE' vs stint 'Semple, R' (fuzzy:1)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1913, birth 1873 (age 40)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1922
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

