<!-- {"case_id": "case_andrews_henry-leonard-greystone_b1887", "bio_ids": ["andrews_henry-leonard-greystone_b1887"], "stint_ids": ["Andrews, G___British Guiana___1905", "Andrews, L___Palestine___1923"]} -->
# Dossier case_andrews_henry-leonard-greystone_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 65 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `andrews_henry-leonard-greystone_b1887`

- Printed name: **ANDREWS, HENRY LEONARD GREYSTONE**
- Birth year: 1887 (attested in editions [1917, 1918, 1920, 1921, 1922, 1923, 1924])
- Appears in editions: [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1917-L47311.v` — printed in editions [1917, 1918, 1920, 1921, 1922, 1923, 1924]:**

> ANDREWS, HENRY LEONARD GREYSTONE.—B. 1887; sub-inspr., Trinidad constaby., 12th Mar., 1913.

**Version `col1919-L50234.v` — printed in editions [1919]:**

> ANDREWS, Henry Leonard Greystone.—B. 1887; sub-inspr., Trinidad constab., 12th Mar., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | sub-inspr., Trinidad constaby | Trinidad | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |

## Candidate stint `Andrews, G___British Guiana___1905`

- Staff-list name: **Andrews, G** | colony: **British Guiana** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | G. Andrews | Member | Poor | — | — |
| 1906 | G. Andrews | Member | Poor | — | — |
| 1907 | Rev. G. Andrews | Member | Poor | — | — |

### Deterministic checks: `andrews_henry-leonard-greystone_b1887` vs `Andrews, G___British Guiana___1905`

- [PASS] surname_gate: bio 'ANDREWS' vs stint 'Andrews, G' (exact)
- [PASS] initials: bio ['H', 'L', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1905, birth 1887 (age 18)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Andrews, L___Palestine___1923`

- Staff-list name: **Andrews, L** | colony: **Palestine** | listed 1923–1932 | editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | L. Andrews | District Officer | Administrative Staff | — | — |
| 1924 | L. Andrews | District Officer | Administrative Staff | — | — |
| 1925 | L. Andrews | District Officer | District Staff | — | — |
| 1927 | L. Andrews | District Officers | District Staff | — | — |
| 1928 | L. Andrews | District Officer | District Staff | — | — |
| 1929 | L. Andrews | District Officer | Civil Establishment | — | — |
| 1930 | L. Andrews | District Officer | District Staff | — | — |
| 1931 | L. Andrews | District Officer | District Staff | — | — |
| 1932 | L. Andrews | District Officer | District Staff | — | — |

### Deterministic checks: `andrews_henry-leonard-greystone_b1887` vs `Andrews, L___Palestine___1923`

- [PASS] surname_gate: bio 'ANDREWS' vs stint 'Andrews, L' (exact)
- [PASS] initials: bio ['H', 'L', 'G'] ~ stint ['L']
- [PASS] age_gate: stint starts 1923, birth 1887 (age 36)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1932
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

