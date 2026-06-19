<!-- {"case_id": "case_manchester_james_e1905", "bio_ids": ["manchester_james_e1905"], "stint_ids": ["Manchester, J. R___Lagos___1896", "Manchester, Jas___Leeward Islands___1897"]} -->
# Dossier case_manchester_james_e1905

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['manchester_james_e1905'] carry a single initial only — the namesake trap applies.

## Biography `manchester_james_e1905`

- Printed name: **MANCHESTER, James**
- Birth year: not printed
- Appears in editions: [1906, 1907]

### Verbatim printed entry text (OCR)

**Version `col1906-L46834.v` — printed in editions [1906, 1907]:**

> MANCHESTER, James.—2nd clk., registr., St. Kitts, Apr., 1905; clk. to sup't. pub. wks., St. Kitts, Apr., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | 2nd clk., registr. | St. Kitts | [1906, 1907] |

## Candidate stint `Manchester, J. R___Lagos___1896`

- Staff-list name: **Manchester, J. R** | colony: **Lagos** | listed 1896–1898 | editions [1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | J. R. Manchester | — | Elective Members | — | — |
| 1898 | J. R. Manchester | Elective Member | General Legislative Council | — | — |

### Deterministic checks: `manchester_james_e1905` vs `Manchester, J. R___Lagos___1896`

- [PASS] surname_gate: bio 'MANCHESTER' vs stint 'Manchester, J. R' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Lagos'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Manchester, Jas___Leeward Islands___1897`

- Staff-list name: **Manchester, Jas** | colony: **Leeward Islands** | listed 1897–1925 | editions [1897, 1899, 1900, 1905, 1906, 1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | J. T. Manchester | Legislative Council Unofficial Member | Legislative Council | — | — |
| 1899 | J. T. Manchester | Unofficial Member, Legislative Council | Legislative Council | — | — |
| 1900 | J. T. Manchester | Legislative Council Unofficial Member | Legislative Council - Unofficial Members | — | — |
| 1905 | Hon. J. T. Manchester | Commission of the Peace | Commission of the Peace, St Kitts and Nevis | — | — |
| 1905 | J. T. Manchester | Executive Council Member | Executive Council | — | — |
| 1905 | Jas. Manchester | 2nd Clerk | Judicial | — | — |
| 1906 | Hon. J. T. Manchester | Commission of the Peace | Judicial | — | — |
| 1906 | J. T. Manchester | Executive Council Member | Executive Council | — | — |
| 1906 | J. Manchester | Clerk to Surveyor and S. P. W. | Public Works | — | — |
| 1906 | J. T. Manchester | Legislative Council Member | Legislative Council | — | — |
| 1907 | J. T. Manchester | Executive Council Member | Executive Council | — | — |
| 1907 | J. T. Manchester | Member | Commission of the Peace | — | — |
| 1907 | J. T. Manchester | Legislative Council Unofficial Member | Legislative Council | — | — |
| 1907 | J. Manchester | Clerk to Surveyor and S. P. W. | Public Works | — | — |
| 1908 | J. T. Manchester | Executive Council Member | Administration | — | — |
| 1911 | J. T. Manchester | Executive Council Member | Executive Council | — | — |
| 1912 | J. T. Manchester | Member | Executive Council | — | — |
| 1912 | J. T. Manchester | Unofficial Member | Legislative Council | — | — |
| 1913 | J. T. Manchester | Member | Executive Council | — | — |
| 1914 | J. T. Manchester | Executive Council Member | Executive Council | — | — |
| 1914 | J. T. Manchester | Unofficial Member | Legislative Council | — | — |
| 1915 | J. T. Manchester | Member | Executive Council | — | — |
| 1917 | J. T. Manchester | Executive Council Member | Executive Council | — | — |
| 1918 | J. T. Manchester | Member | Executive Council | — | — |
| 1919 | J. T. Manchester | — | Executive Council | — | — |
| 1920 | J. T. Manchester | Member, Executive Council | Executive Council | — | — |
| 1922 | J. T. Manchester | — | Executive Council | — | — |
| 1923 | J. T. Manchester | — | Executive Council | — | — |
| 1924 | J. T. Manchester | Executive Council Member | Executive Council | — | — |
| 1925 | J. T. Manchester | — | Executive Council | — | — |

### Deterministic checks: `manchester_james_e1905` vs `Manchester, Jas___Leeward Islands___1897`

- [PASS] surname_gate: bio 'MANCHESTER' vs stint 'Manchester, Jas' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1925
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

