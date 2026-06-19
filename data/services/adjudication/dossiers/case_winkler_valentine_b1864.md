<!-- {"case_id": "case_winkler_valentine_b1864", "bio_ids": ["winkler_valentine_b1864"], "stint_ids": ["Winkler, Valentine___Canada___1894", "Winkler, Valentine___Canada___1906"]} -->
# Dossier case_winkler_valentine_b1864

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['winkler_valentine_b1864'] carry a single initial only — the namesake trap applies.

## Biography `winkler_valentine_b1864`

- Printed name: **WINKLER, VALENTINE**
- Birth year: 1864 (attested in editions [1918, 1919, 1920])
- Appears in editions: [1918, 1919, 1920]

### Verbatim printed entry text (OCR)

**Version `col1918-L55402.v` — printed in editions [1918, 1919, 1920]:**

> WINKLER, HON. VALENTINE.—B. 1864; lumber merchant; elec. to legis. ass., Manitoba, 1892, 1896, and 1899; unsuccessful candidate for H. of C., 1900; re-elec. to legis. ass., 1900, and in 1903, 1907, 1910, 1914, and 1915; min. of agric. and immigrtn. in Norris admnstr., May, 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892–1899 | elec. to legis. ass. | Manitoba | [1918, 1919, 1920] |
| 1 | 1900–1900 | unsuccessful candidate for H. of C. | — | [1918, 1919, 1920] |
| 2 | 1900–1915 | re-elec. to legis. ass. | — | [1918, 1919, 1920] |
| 3 | 1915 | min. of agric. and immigrtn. in Norris admnstr. | — | [1918, 1919, 1920] |

## Candidate stint `Winkler, Valentine___Canada___1894`

- Staff-list name: **Winkler, Valentine** | colony: **Canada** | listed 1894–1898 | editions [1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | V. Winkler | Member | Members | — | — |
| 1896 | V. Winkler | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1897 | V. Winkler | Member | Members | — | — |
| 1898 | V. Winkler | Member | Legislative Assembly | — | — |

### Deterministic checks: `winkler_valentine_b1864` vs `Winkler, Valentine___Canada___1894`

- [PASS] surname_gate: bio 'WINKLER' vs stint 'Winkler, Valentine' (exact)
- [PASS] initials: bio ['V'] ~ stint ['V']
- [PASS] age_gate: stint starts 1894, birth 1864 (age 30)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Winkler, Valentine___Canada___1906`

- Staff-list name: **Winkler, Valentine** | colony: **Canada** | listed 1906–1918 | editions [1906, 1908, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | Valentine Winkler | Member for Rhinelands | Legislative Assembly | — | — |
| 1908 | Valentine Winkler | Member | Legislative Assembly | — | — |
| 1913 | Valentine Winkler | Member of Legislative Assembly | Members | — | — |
| 1914 | Valentine Winkler | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1915 | Valentine Winkler | Member for Morden & Rhineland | — | — | — |
| 1917 | Valentine Winkler | Minister | Agriculture and Immigration | — | — |
| 1917 | Valentine Winkler | Minister of Agriculture and Immigration | Executive Council | — | — |
| 1918 | Valentine Winkler | Minister of Agriculture and Immigration | Executive Council | — | — |

### Deterministic checks: `winkler_valentine_b1864` vs `Winkler, Valentine___Canada___1906`

- [PASS] surname_gate: bio 'WINKLER' vs stint 'Winkler, Valentine' (exact)
- [PASS] initials: bio ['V'] ~ stint ['V']
- [PASS] age_gate: stint starts 1906, birth 1864 (age 42)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1918
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

