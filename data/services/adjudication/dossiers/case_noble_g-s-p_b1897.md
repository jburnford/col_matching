<!-- {"case_id": "case_noble_g-s-p_b1897", "bio_ids": ["noble_g-s-p_b1897"], "stint_ids": ["Noble, P___Palestine___1923", "Noble, Peter___Leeward Islands___1913"]} -->
# Dossier case_noble_g-s-p_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Noble, P___Palestine___1923` is also gate-compatible with biography(ies) outside this case: ['noble_peter_e1906'] (already linked elsewhere or filtered).
- NOTE: stint `Noble, Peter___Leeward Islands___1913` is also gate-compatible with biography(ies) outside this case: ['noble_peter_e1906'] (already linked elsewhere or filtered).

## Biography `noble_g-s-p_b1897`

- Printed name: **NOBLE, G. S. P**
- Birth year: 1897 (attested in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: M.B
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L62367.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> NOBLE, G. S. P., M.B., Ch.B. (Glas.), Certif. Lond., S.H.T.M. (distinct).—B. 1897; mil. serv., 1916-18; med. offr., Tanganyika Territory, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | med. offr., Tanganyika Territory | Tanganyika | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Noble, P___Palestine___1923`

- Staff-list name: **Noble, P** | colony: **Palestine** | listed 1923–1932 | editions [1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | P. Noble | District Engineers | PUBLIC WORKS | — | — |
| 1925 | P. Noble | District Engineer | Public Works | — | — |
| 1927 | P. Noble | District Engineer | Department of Public Works | — | — |
| 1928 | P. Noble | District Engineer | Public Works | — | — |
| 1929 | P. Noble | District Engineer | Department of Public Works | — | — |
| 1930 | P. Noble | District Engineer | Public Works | — | — |
| 1931 | P. Noble | District Engineer | Public Works | — | — |
| 1932 | P. Noble | District Engineer | Public Works | — | — |

### Deterministic checks: `noble_g-s-p_b1897` vs `Noble, P___Palestine___1923`

- [PASS] surname_gate: bio 'NOBLE' vs stint 'Noble, P' (exact)
- [PASS] initials: bio ['G', 'S', 'P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1923, birth 1897 (age 26)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Noble, Peter___Leeward Islands___1913`

- Staff-list name: **Noble, Peter** | colony: **Leeward Islands** | listed 1913–1922 | editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1913 | P. Noble | Member | Legislative Council | — | — |
| 1914 | P. Noble | Official Member | Legislative Council | — | — |
| 1914 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1915 | P. Noble | Member (Official) | Legislative Council | — | — |
| 1915 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1917 | P. Noble | Non-Official Member | Legislative Council | — | — |
| 1917 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1918 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1918 | P. Noble | Official Member | Legislative Council | — | — |
| 1919 | P. Noble | Official Member | Legislative Council | — | — |
| 1919 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1920 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1920 | P. Noble | Member | Legislative Council | — | — |
| 1922 | Peter Noble | Colonial Engineer and Surveyor-General | Public Works Department | — | — |
| 1922 | P. Noble | — | — | — | — |

### Deterministic checks: `noble_g-s-p_b1897` vs `Noble, Peter___Leeward Islands___1913`

- [PASS] surname_gate: bio 'NOBLE' vs stint 'Noble, Peter' (exact)
- [PASS] initials: bio ['G', 'S', 'P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1913, birth 1897 (age 16)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1922
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

