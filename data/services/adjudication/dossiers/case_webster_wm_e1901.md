<!-- {"case_id": "case_webster_wm_e1901", "bio_ids": ["webster_wm_e1901"], "stint_ids": ["Webster, G. W___Nigeria___1917", "Webster, W. A. King___Aden___1949", "Webster, W___Commonwealth Of Australia___1905"]} -->
# Dossier case_webster_wm_e1901

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['webster_wm_e1901'] carry a single initial only — the namesake trap applies.

## Biography `webster_wm_e1901`

- Printed name: **WEBSTER, WM.**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1917-L54011.v` — printed in editions [1917, 1918]:**

> WEBSTER, HON. WM.—M.L.A., New South Wales, July, 1901, to Nov., 1903; mem. H. of R., C. of A., general elections, 1903, 1906, 1910, 1913, 1914; mem. of royal comnr. on postal services, 1908-10; postmr.-gen., C. of A., 27th Oct., 1915.

**Version `col1919-L56602.v` — printed in editions [1919]:**

> WEBSTER, Hox. Wm.—M.L.A., New South Wales, July, 1901, to Nov., 1903; mem. H. of R., C. of A., general elections, 1903, 1906, 1910, 1913, 1914; mem. of royal coms. on postal services, 1908-10; poetm.-gen., C. of A., 27th Oct., 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1903 | M.L.A. | New South Wales | [1917, 1918, 1919] |
| 1 | 1903 | mem. H. of R. | Commonwealth of Australia | [1917, 1918, 1919] |
| 2 | 1908–1910 | mem. of royal comnr. on postal services | — | [1917, 1918, 1919] |
| 3 | 1915 | postmr.-gen. | Commonwealth of Australia | [1917, 1918, 1919] |

## Candidate stint `Webster, G. W___Nigeria___1917`

- Staff-list name: **Webster, G. W** | colony: **Nigeria** | listed 1917–1919 | editions [1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | G. W. Webster | Second Class Resident | Northern Provinces | — | — |
| 1918 | G. W. Webster | Second Class Resident | Northern Provinces | D.S.O. | — |
| 1919 | G. W. Webster | Fifteen Second Class Residents | NORTHERN PROVINCES | — | — |

### Deterministic checks: `webster_wm_e1901` vs `Webster, G. W___Nigeria___1917`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, G. W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Webster, W. A. King___Aden___1949`

- Staff-list name: **Webster, W. A. King** | colony: **Aden** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. A. King Webster | Fisheries Officer (Colony and Prot.) | Fisheries | — | — |
| 1950 | W. A. King Webster | Fisheries Officer (Colony and Prot.) | Fisheries | — | — |

### Deterministic checks: `webster_wm_e1901` vs `Webster, W. A. King___Aden___1949`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, W. A. King' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'A', 'K']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Aden'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Webster, W___Commonwealth Of Australia___1905`

- Staff-list name: **Webster, W** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. Webster | — | — | — | — |
| 1907 | W. Webster | Member | Legislative Assembly | — | — |

### Deterministic checks: `webster_wm_e1901` vs `Webster, W___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Commonwealth Of Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1907
- [FAIL] position_sim: best 50 vs bar 60: 'mem. H. of R.' ~ 'Member'
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

