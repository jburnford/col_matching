<!-- {"case_id": "case_bice_john-george_b1853", "bio_ids": ["bice_john-george_b1853"], "stint_ids": ["Bice, J. G___Australia___1912", "Bice, J. G___South Australia___1900"]} -->
# Dossier case_bice_john-george_b1853

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bice_john-george_b1853`

- Printed name: **BICE, JOHN GEORGE**
- Birth year: 1853 (attested in editions [1921, 1922, 1923])
- Appears in editions: [1910, 1911, 1913, 1914, 1915, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1921-L54471.v` — printed in editions [1921, 1922, 1923]:**

> BICE, HON. JOHN GEORGE, M.L.C.—B. in Cornwall, 1853; M.L.C., S. Australia, since 1894; min. controlling N. Territory, 1908-9; ch. sec., 1909-10, 1912-14 and since May, 1919; comsnr., public works, 1917-19.

**Version `col1910-L44286.v` — printed in editions [1910, 1911, 1913, 1914, 1915]:**

> BICE, JOHN GEORGE.—M.L.C., S. Aust., 1894; min. controlling N. Territory and min. for water supply, 1908; ch. sec. and min. of industry, 1909-10; chief sec., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | M.L.C. | South Australia | [1910, 1911, 1913, 1914, 1915, 1921, 1922, 1923] |
| 1 | 1908–1909 | min. controlling N. Territory | Northern Territory | [1910, 1911, 1913, 1914, 1915, 1921, 1922, 1923] |
| 2 | 1909 | ch. sec. | — | [1910, 1911, 1913, 1914, 1915, 1921, 1922, 1923] |
| 3 | 1912 | chief sec | — | [1910, 1911, 1913, 1914, 1915] |
| 4 | 1917–1919 | comsnr., public works | — | [1921, 1922, 1923] |

## Candidate stint `Bice, J. G___Australia___1912`

- Staff-list name: **Bice, J. G** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | J. G. Bice | Member, Northern Electoral District | Parliament | — | — |
| 1913 | Hon. J. G. Bice | Chief Secretary | Chief Secretary's Department | — | — |
| 1918 | J. G. Bice | Commissioner of Public Works | Office of Commissioner of Public Works | — | — |

### Deterministic checks: `bice_john-george_b1853` vs `Bice, J. G___Australia___1912`

- [PASS] surname_gate: bio 'BICE' vs stint 'Bice, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1912, birth 1853 (age 59)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bice, J. G___South Australia___1900`

- Staff-list name: **Bice, J. G** | colony: **South Australia** | listed 1900–1906 | editions [1900, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | J. G. Bice | Member, Legislative Council | Legislative Council | — | — |
| 1906 | J. G. Bice | Member | Legislative Council | — | — |

### Deterministic checks: `bice_john-george_b1853` vs `Bice, J. G___South Australia___1900`

- [PASS] surname_gate: bio 'BICE' vs stint 'Bice, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1900, birth 1853 (age 47)
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1900-1906
- [FAIL] position_sim: best 22 vs bar 60: 'M.L.C.' ~ 'Member'
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

