<!-- {"case_id": "case_woodford_w-w_e1889", "bio_ids": ["woodford_w-w_e1889"], "stint_ids": ["Woodford, William___Newfoundland___1898", "Woodford, William___Newfoundland___1910"]} -->
# Dossier case_woodford_w-w_e1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Woodford, William___Newfoundland___1898` is also gate-compatible with biography(ies) outside this case: ['woodford_w_e1918'] (already linked elsewhere or filtered).
- NOTE: stint `Woodford, William___Newfoundland___1910` is also gate-compatible with biography(ies) outside this case: ['woodford_w_e1918'] (already linked elsewhere or filtered).

## Biography `woodford_w-w_e1889`

- Printed name: **WOODFORD, W. W.**
- Birth year: not printed
- Appears in editions: [1919, 1920, 1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1919-L56825.v` — printed in editions [1919, 1920, 1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]:**

> WOODFORD, HON. W. W.—Elected M.H.A., Harbour Main, Newfoundland, 1889; chrmn., bd. of works, 1897; min. of public works, 1898, 1909, and 1918; M.E.C., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | M.H.A. | Newfoundland | [1919, 1920, 1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1897 | chrmn., bd. of works | — | [1919, 1920, 1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 2 | 1898–1918 | min. of public works | — | [1919, 1920, 1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 3 | 1918 | M.E.C. | — | [1919, 1920, 1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Woodford, William___Newfoundland___1898`

- Staff-list name: **Woodford, William** | colony: **Newfoundland** | listed 1898–1900 | editions [1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | William Woodford | Chairman, Board of Works | Civil Establishment | — | — |
| 1899 | William Woodford | Minister of Public Works | — | — | — |
| 1900 | William Woodford | Minister of Public Works | Public Works | — | — |

### Deterministic checks: `woodford_w-w_e1889` vs `Woodford, William___Newfoundland___1898`

- [PASS] surname_gate: bio 'WOODFORD' vs stint 'Woodford, William' (exact)
- [PASS] initials: bio ['W', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1900
- [FAIL] position_sim: best 15 vs bar 60: 'M.H.A.' ~ 'Chairman, Board of Works'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Woodford, William___Newfoundland___1910`

- Staff-list name: **Woodford, William** | colony: **Newfoundland** | listed 1910–1919 | editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | W. Woodford | Minister of Public Works | Department of Public Works | — | — |
| 1911 | William Woodford | Minister of Public Works | Department of Public Works | — | — |
| 1912 | William Woodford | Minister of Public Works | Department of Public Works | — | — |
| 1913 | W. Woodford | Minister of Public Works | Department of Public Works | — | — |
| 1914 | William Woodford | Minister of Public Works | Public Works | — | — |
| 1915 | William Woodford | Minister of Public Works | Public Works | — | — |
| 1917 | W. Woodford | Chairman, Board of Works | Board of Works | — | — |
| 1917 | William Woodford | Minister of Public Works | Public Works | — | — |
| 1918 | W. Woodford | Minister of Public Works | Public Works | — | — |
| 1919 | Hon. W. Woodford | Minister of Public Works | Department of Public Works | — | — |

### Deterministic checks: `woodford_w-w_e1889` vs `Woodford, William___Newfoundland___1910`

- [PASS] surname_gate: bio 'WOODFORD' vs stint 'Woodford, William' (exact)
- [PASS] initials: bio ['W', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1919
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

