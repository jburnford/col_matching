<!-- {"case_id": "case_knowling_george_b1842", "bio_ids": ["knowling_george_b1842"], "stint_ids": ["Knowling, G. H___Canada___1896"]} -->
# Dossier case_knowling_george_b1842

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['knowling_george_b1842'] carry a single initial only — the namesake trap applies.

## Biography `knowling_george_b1842`

- Printed name: **KNOWLING, GEORGE**
- Birth year: 1842 (attested in editions [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923])
- Appears in editions: [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1906-L46474.v` — printed in editions [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]:**

> KNOWLING, HON. GEORGE.—B. 1842; M.L.C., Newfoundland, 1897; mem. of Cabinet, 1900; mem. of treasry. bd. and govt. of savings bank, 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | M.L.C. | Newfoundland | [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |
| 1 | 1900 | mem. of Cabinet | Newfoundland *(inherited from previous clause)* | [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |

## Candidate stint `Knowling, G. H___Canada___1896`

- Staff-list name: **Knowling, G. H** | colony: **Canada** | listed 1896–1899 | editions [1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | G. H. Knowling | Member | North West Territories Legislative Assembly | — | — |
| 1897 | G. H. Knowling | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1898 | G. H. Knowling | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1899 | G. H. Knowling | Member of Legislative Assembly | Legislative Assembly | — | — |

### Deterministic checks: `knowling_george_b1842` vs `Knowling, G. H___Canada___1896`

- [PASS] surname_gate: bio 'KNOWLING' vs stint 'Knowling, G. H' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1896, birth 1842 (age 54)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1899
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

