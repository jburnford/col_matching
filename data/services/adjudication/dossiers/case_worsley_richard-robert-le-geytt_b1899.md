<!-- {"case_id": "case_worsley_richard-robert-le-geytt_b1899", "bio_ids": ["worsley_richard-robert-le-geytt_b1899", "worsley_robert-lewkenor_b1893"], "stint_ids": ["Worsley, R. L___Palestine___1927"]} -->
# Dossier case_worsley_richard-robert-le-geytt_b1899

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Worsley, R. L___Palestine___1927'] have more than one claimant biography in this case.

## Biography `worsley_richard-robert-le-geytt_b1899`

- Printed name: **WORSLEY, RICHARD ROBERT LE GEYTT**
- Birth year: 1899 (attested in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: A.R.C.S, D.I.C
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L64655.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> WORSLEY, RICHARD ROBERT LE GEYTT, Ph.D. (Lond.), D.I.C., A.R.C.S., B.Sc.—B. 1899; ed. St. Paul's and R. Coll. of Sci.; R.E. O.C.B., 1918-1919; subj. dir., chem. sect., miny. of agr., Egypt, 1926; biochemist, E. African agril. research sta., Amari, Tanganyika Territory, 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1919 | R.E. O.C.B | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1926 | subj. dir., chem. sect., miny. of agr., Egypt | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1928 | biochemist, E. African agril. research sta., Amari, Tanganyika Territory | Tanganyika | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Biography `worsley_robert-lewkenor_b1893`

- Printed name: **WORSLEY, Robert Lewkenor**
- Birth year: 1893 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L37048.v` — printed in editions [1948, 1949]:**

> WORSLEY, Robert Lewkenor.—b. 1893; ed. Radley Coll. and S.E. Agric. Coll., Wye; on mil. serv., 1914-19, lieut.; Pal. Gendarmerie, 1922; comsnr., prisons, N. Rhod., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | Pal. Gendarmerie | Palestine | [1948, 1949] |
| 1 | 1942 | comsnr., prisons | Northern Rhodesia | [1948, 1949] |

## Candidate stint `Worsley, R. L___Palestine___1927`

- Staff-list name: **Worsley, R. L** | colony: **Palestine** | listed 1927–1940 | editions [1927, 1928, 1930, 1931, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | R. L. Worsley | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1928 | R. L. Worsley | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1930 | R. L. Worsley | Assistant Superintendents | Department of Police and Prisons | — | — |
| 1931 | R. L. Worsley | Assistant Superintendents | Department of Police and Prisons. | — | — |
| 1940 | R. L. Worsley | Assistant Superintendent | Department of Police and Prisons. | — | — |

### Deterministic checks: `worsley_richard-robert-le-geytt_b1899` vs `Worsley, R. L___Palestine___1927`

- [PASS] surname_gate: bio 'WORSLEY' vs stint 'Worsley, R. L' (exact)
- [PASS] initials: bio ['R', 'R', 'L', 'G'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1927, birth 1899 (age 28)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `worsley_robert-lewkenor_b1893` vs `Worsley, R. L___Palestine___1927`

- [PASS] surname_gate: bio 'WORSLEY' vs stint 'Worsley, R. L' (exact)
- [PASS] initials: bio ['R', 'L'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1940
- [FAIL] position_sim: best 26 vs bar 60: 'Pal. Gendarmerie' ~ 'Assistant Superintendent'
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

