<!-- {"case_id": "case_findlay_alexander-john_b1886", "bio_ids": ["findlay_alexander-john_b1886"], "stint_ids": ["Findlay, A. J___Nigeria___1921", "Findlay, A. J___Zanzibar___1932"]} -->
# Dossier case_findlay_alexander-john_b1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `findlay_alexander-john_b1886`

- Printed name: **FINDLAY, ALEXANDER JOHN**
- Birth year: 1886 (attested in editions [1933, 1934, 1935, 1936, 1937])
- Appears in editions: [1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1933-L59773.v` — printed in editions [1933, 1934, 1935, 1936, 1937]:**

> FINDLAY, ALEXANDER JOHN.—B. 1886; ed. Aberdeen Grammar Schl., Aberdeen Univ. and North of Scotland Coll. of Agr.; M.A., B.Sc. (agric.), N.D.A., N.D.D., sup't., agr., Nigeria, 1912; senr. sup't., 1922; asst. dir., 1927; dep. dir., 1930; dir., agr., Zanzibar, 1931; M.L.C., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | M.A., B.Sc. (agric.), N.D.A., N.D.D., sup't., agr. | Nigeria | [1933, 1934, 1935, 1936, 1937] |
| 1 | 1922 | senr. sup't | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 2 | 1927 | asst. dir | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 3 | 1930 | dep. dir | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 4 | 1931 | dir., agr. | Zanzibar | [1933, 1934, 1935, 1936, 1937] |
| 5 | 1932 | M.L.C | Zanzibar *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Findlay, A. J___Nigeria___1921`

- Staff-list name: **Findlay, A. J** | colony: **Nigeria** | listed 1921–1925 | editions [1921, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | A. J. Findlay | Superintendent | Agriculture, Southern Provinces | — | — |
| 1922 | A. J. Findlay | Superintendent | Agriculture | — | — |
| 1925 | A. J. Findlay | Senior Superintendent | Agriculture | — | — |

### Deterministic checks: `findlay_alexander-john_b1886` vs `Findlay, A. J___Nigeria___1921`

- [PASS] surname_gate: bio 'FINDLAY' vs stint 'Findlay, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1921, birth 1886 (age 35)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1921-1925
- [PASS] position_sim: best 60 vs bar 60: 'senr. sup't' ~ 'Senior Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Findlay, A. J___Zanzibar___1932`

- Staff-list name: **Findlay, A. J** | colony: **Zanzibar** | listed 1932–1937 | editions [1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | A. J. Findlay | Director of Agriculture and Government Chemist | Agricultural Department | — | — |
| 1933 | A. J. Findlay | Director of Agriculture | Agricultural Department | — | — |
| 1934 | A. J. Findlay | Director of Agriculture | Agricultural Department | — | — |
| 1936 | A. J. Findlay | Director of Agriculture | Agricultural Department | — | — |
| 1937 | A. J. Findlay | Director of Agriculture | Agricultural Department | — | — |

### Deterministic checks: `findlay_alexander-john_b1886` vs `Findlay, A. J___Zanzibar___1932`

- [PASS] surname_gate: bio 'FINDLAY' vs stint 'Findlay, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1932, birth 1886 (age 46)
- [PASS] colony: 2 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1932-1937
- [FAIL] position_sim: best 47 vs bar 60: 'dir., agr.' ~ 'Director of Agriculture'
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

