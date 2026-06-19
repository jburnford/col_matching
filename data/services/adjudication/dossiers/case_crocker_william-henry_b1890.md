<!-- {"case_id": "case_crocker_william-henry_b1890", "bio_ids": ["crocker_william-henry_b1890"], "stint_ids": ["Crocker, W. H___Gold Coast___1927", "Crocker, William H___Sierra Leone___1934"]} -->
# Dossier case_crocker_william-henry_b1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crocker_william-henry_b1890`

- Printed name: **CROCKER, WILLIAM HENRY**
- Birth year: 1890 (attested in editions [1933, 1934, 1935, 1936])
- Appears in editions: [1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1933-L58940.v` — printed in editions [1933, 1934, 1935, 1936]:**

> CROCKER, WILLIAM HENRY.—B. 1890; served in R.A.S.C. (M.T.) in Mesopotamia, Persia and India; ast. gov't. printer, Gold Coast, 1921; ag. gov't. printer, 1925, 1927, 1928, 1930 and 1932; supl., gov't. press, 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921–1921 | ast. gov't. printer | Gold Coast | [1933, 1934, 1935, 1936] |
| 1 | 1925–1932 | ag. gov't. printer | — | [1933, 1934, 1935, 1936] |
| 2 | 1928–1928 | supl., gov't. press | — | [1933, 1934, 1935, 1936] |

## Candidate stint `Crocker, W. H___Gold Coast___1927`

- Staff-list name: **Crocker, W. H** | colony: **Gold Coast** | listed 1927–1932 | editions [1927, 1928, 1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. H. Crocker | Assistant Government Printers | Printing Office | — | — |
| 1928 | W. H. Crocker | Assistant Government Printer | Printing Office | — | — |
| 1929 | W. H. Crocker | Superintendent Government Press | Printing Office | — | — |
| 1930 | W. H. Crocker | Superintendent Government Press | Printing Office | — | — |
| 1932 | W. H. Crocker | Superintendent Government Press | Printing Office | — | — |

### Deterministic checks: `crocker_william-henry_b1890` vs `Crocker, W. H___Gold Coast___1927`

- [PASS] surname_gate: bio 'CROCKER' vs stint 'Crocker, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1927, birth 1890 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Crocker, William H___Sierra Leone___1934`

- Staff-list name: **Crocker, William H** | colony: **Sierra Leone** | listed 1934–1937 | editions [1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | W. H. Crocker | Government Printer | Printing Department | — | — |
| 1936 | William H. Crocker | Government Printer | Printing Department | — | — |
| 1937 | W. H. Crocker | Government Printer | Printing and Stationery Department | — | — |

### Deterministic checks: `crocker_william-henry_b1890` vs `Crocker, William H___Sierra Leone___1934`

- [PASS] surname_gate: bio 'CROCKER' vs stint 'Crocker, William H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1934, birth 1890 (age 44)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1937
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

