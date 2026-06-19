<!-- {"case_id": "case_harvey_a-w_e1889", "bio_ids": ["harvey_a-w_e1889"], "stint_ids": ["Harvey, W___South Australia___1877", "Harvey, W___Western Australia___1899"]} -->
# Dossier case_harvey_a-w_e1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 59 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harvey_a-w_e1889`

- Printed name: **HARVEY, A. W.**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1894-L32015.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1900, 1905]:**

> HARVEY, THE HON. A. W.—Member Newfoundland Land Legis. Council; member Exec. Council (without portfolio), 1889 to 94, and again Dec., 1894 to Dec., 1895; member of official and of legislative delegations to London on the fisheries question in 1890 and 1891 respectively; on special mission to Madrid, 1892, in connection with commercial negotiations with Spain.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889–1894 | member Exec. Council (without portfolio) | — | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 1 | 1890–1891 | member of official and of legislative delegations | London | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 2 | 1892–1892 | on special mission | Spain | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 3 | 1894–1895 | member Exec. Council (without portfolio) | — | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 4 | ? | Member | Newfoundland | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |

## Candidate stint `Harvey, W___South Australia___1877`

- Staff-list name: **Harvey, W** | colony: **South Australia** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Harvey | Surveyors | Survey Department | — | — |
| 1878 | W. Harvey | Surveyor | Survey Department | — | — |

### Deterministic checks: `harvey_a-w_e1889` vs `Harvey, W___South Australia___1877`

- [PASS] surname_gate: bio 'HARVEY' vs stint 'Harvey, W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Harvey, W___Western Australia___1899`

- Staff-list name: **Harvey, W** | colony: **Western Australia** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | W. Harvey | Resident Medical Officer | Medical Department | — | — |
| 1900 | W. Harvey | Resident Medical Officer | Medical Department | — | — |

### Deterministic checks: `harvey_a-w_e1889` vs `Harvey, W___Western Australia___1899`

- [PASS] surname_gate: bio 'HARVEY' vs stint 'Harvey, W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
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

