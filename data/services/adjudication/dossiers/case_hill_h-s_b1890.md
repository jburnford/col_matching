<!-- {"case_id": "case_hill_h-s_b1890", "bio_ids": ["hill_h-s_b1890"], "stint_ids": ["Hill, H. S___British Guiana___1911", "Hill, H. S___Tanganyika___1920"]} -->
# Dossier case_hill_h-s_b1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 111 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hill_h-s_b1890`

- Printed name: **HILL, H. S**
- Birth year: 1890 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L61108.v` — printed in editions [1932]:**

> HILL, H. S. —B. 1890; ed. Br. Guiana; cust. offr., Tanganyika Territory, 1916; supervisor, cust., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | cust. offr., Tanganyika Territory | Tanganyika | [1932] |
| 1 | 1919 | supervisor, cust | Tanganyika *(inherited from previous clause)* | [1932] |

## Candidate stint `Hill, H. S___British Guiana___1911`

- Staff-list name: **Hill, H. S** | colony: **British Guiana** | listed 1911–1920 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | H. S. Hill | 6th Class | Customs | — | — |
| 1912 | H. S. Hill | 6th Class | Customs | — | — |
| 1913 | H. S. Hill | 5th | Customs | — | — |
| 1914 | H. S. Hill | 5th Class | Customs | — | — |
| 1915 | H. S. Hill | 5th | Customs | — | — |
| 1917 | H. S. Hill | 5th | Customs | — | — |
| 1918 | H. S. Hill | 5th | Customs | — | — |
| 1919 | H. S. Hill | 4th | Customs | — | — |
| 1920 | H. S. Hill | 4th | Customs | — | — |

### Deterministic checks: `hill_h-s_b1890` vs `Hill, H. S___British Guiana___1911`

- [PASS] surname_gate: bio 'HILL' vs stint 'Hill, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1911, birth 1890 (age 21)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1920
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hill, H. S___Tanganyika___1920`

- Staff-list name: **Hill, H. S** | colony: **Tanganyika** | listed 1920–1930 | editions [1920, 1921, 1922, 1923, 1924, 1925, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | H. S. Hill | Supervisor of Customs | Customs Department | — | — |
| 1921 | H. S. Hill | Supervisors of Customs | Customs | — | — |
| 1922 | H. S. Hill | Supervisor of Customs | Customs | — | — |
| 1923 | H. S. Hill | Supervisors of Customs | Customs | — | — |
| 1924 | H. S. Hill | Supervisors of Customs | Customs | — | — |
| 1925 | H. S. Hill | Supervisors of Customs | Customs | — | — |
| 1930 | H. S. Hill | Supervisor | Customs | — | — |

### Deterministic checks: `hill_h-s_b1890` vs `Hill, H. S___Tanganyika___1920`

- [PASS] surname_gate: bio 'HILL' vs stint 'Hill, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1920, birth 1890 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1920-1930
- [PASS] position_sim: best 100 vs bar 60: 'supervisor, cust' ~ 'Supervisor'
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

