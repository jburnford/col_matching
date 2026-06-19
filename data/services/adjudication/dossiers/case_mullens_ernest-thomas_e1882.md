<!-- {"case_id": "case_mullens_ernest-thomas_e1882", "bio_ids": ["mullens_ernest-thomas_e1882"], "stint_ids": ["Mullens, E. T___Natal___1898"]} -->
# Dossier case_mullens_ernest-thomas_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mullens_ernest-thomas_e1882`

- Printed name: **MULLENS, ERNEST THOMAS**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1908-L46443.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> MULLENS, ERNEST THOMAS.—Press assoc., Lond., 1882 to 1892; clk. and shorthand writer, legis. coun., Natal, 16th Oct., 1893; sec. to min. of lands and works, 15th Mar., 1894; to min. of agric., 1st Nov., 1901; is mem. of tender bd.; offl. mem. of land bd., Sept., 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882–1892 | Press assoc., Lond | — | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1893 | clk. and shorthand writer, legis. coun. | Natal | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1894 | sec. to min. of lands and works | Natal *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1901 | to min. of agric | Natal *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 4 | 1904 | offl. mem. of land bd | Natal *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Mullens, E. T___Natal___1898`

- Staff-list name: **Mullens, E. T** | colony: **Natal** | listed 1898–1910 | editions [1898, 1899, 1900, 1905, 1906, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | E. T. Mullens | Secretary | Lands and Works | — | — |
| 1899 | E. T. Mullens | Secretary | Lands and Works | — | — |
| 1900 | E. T. Mullens | Secretary | Lands and Works | — | — |
| 1905 | E. T. Mullens | Secretary | Ministerial Department of Agriculture | — | — |
| 1906 | E. T. Mullens | Secretary | Ministerial Department of Agriculture | — | — |
| 1907 | E. T. Mullens | Secretary | Ministerial Department of Agriculture | — | — |
| 1910 | E. T. Mullens | Secretary | Land and Agricultural Loan Fund | — | — |

### Deterministic checks: `mullens_ernest-thomas_e1882` vs `Mullens, E. T___Natal___1898`

- [PASS] surname_gate: bio 'MULLENS' vs stint 'Mullens, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1898-1910
- [FAIL] position_sim: best 26 vs bar 60: 'sec. to min. of lands and works' ~ 'Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

