<!-- {"case_id": "case_golding_frederic-dennis_b1897", "bio_ids": ["golding_frederic-dennis_b1897"], "stint_ids": ["Golding, D___Jamaica___1923", "Golding, F. D___Nigeria___1934"]} -->
# Dossier case_golding_frederic-dennis_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `golding_frederic-dennis_b1897`

- Printed name: **GOLDING, Frederic Dennis**
- Birth year: 1897 (attested in editions [1948, 1949, 1951])
- Appears in editions: [1948, 1949, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32881.v` — printed in editions [1948, 1949, 1951]:**

> GOLDING, Frederic Dennis, M.A., F.R.E.S.—b. 1897; ed. Oundle Sch. and Queens' Coll., Cambridge; on mil. serv., 1915-19, lieut.; supt. of agric., Nig., 1922; 2nd entom., 1923; senr. entom., 1925; locust res. 1930-47; attended internat. locust confs., 1932, 1934 and 1938; attd. French locust res. miss., Tchad, 1935; author of papers on econ. entom. and other subj.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | lieut. | — | [1948, 1949, 1951] |
| 1 | 1922–1922 | supt. of agric. | Nigeria | [1948, 1949, 1951] |
| 2 | 1923–1923 | 2nd entom. | — | [1948, 1949, 1951] |
| 3 | 1925–1925 | senr. entom. | — | [1948, 1949, 1951] |
| 4 | 1930–1947 | locust res. | — | [1948, 1949, 1951] |
| 5 | 1932–1938 | attended internat. locust confs. | — | [1948, 1949, 1951] |
| 6 | 1935–1935 | attd. French locust res. miss. | Tchad | [1948, 1949, 1951] |

## Candidate stint `Golding, D___Jamaica___1923`

- Staff-list name: **Golding, D** | colony: **Jamaica** | listed 1923–1925 | editions [1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | D. Golding | Typists and Stenographers | Department of Agriculture | — | — |
| 1925 | D. Golding | Typists and Stenographers | Department of Science and Agriculture | — | — |

### Deterministic checks: `golding_frederic-dennis_b1897` vs `Golding, D___Jamaica___1923`

- [PASS] surname_gate: bio 'GOLDING' vs stint 'Golding, D' (exact)
- [PASS] initials: bio ['F', 'D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1923, birth 1897 (age 26)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Golding, F. D___Nigeria___1934`

- Staff-list name: **Golding, F. D** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | F. D. Golding | Entomologists | Agriculture | — | — |
| 1939 | F. D. Golding | Entomologist | Agriculture | — | — |

### Deterministic checks: `golding_frederic-dennis_b1897` vs `Golding, F. D___Nigeria___1934`

- [PASS] surname_gate: bio 'GOLDING' vs stint 'Golding, F. D' (exact)
- [PASS] initials: bio ['F', 'D'] ~ stint ['F', 'D']
- [PASS] age_gate: stint starts 1934, birth 1897 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

