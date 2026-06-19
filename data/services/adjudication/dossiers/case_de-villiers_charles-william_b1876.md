<!-- {"case_id": "case_de-villiers_charles-william_b1876", "bio_ids": ["de-villiers_charles-william_b1876"], "stint_ids": ["de Villiers, C. W___South Africa___1912"]} -->
# Dossier case_de-villiers_charles-william_b1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-villiers_charles-william_b1876`

- Printed name: **DE VILLIERS, CHARLES WILLIAM**
- Birth year: 1876 (attested in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925])
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1913-L45263.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> DE VILLIERS, CHARLES WILLIAM, B.A., LL.B. (Cape).—B. 1876; ed. at Boys Pub. Schil., Worcester, Cape Colony, and S. African Univ., Cape Town; admitted advocate of sup. ct., Cape Colony, Jan., 1901; law adviser to Transvaal govt., July, 1908; ag. atty.-gen., Transvaal, Oct., 1910, to May, 1911; law adviser, June, 1913; ag. atty.-gen., Cape Prov., Sept., 1914; atty.-gen., Transvaal, Nov., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | advocate of sup. ct. | Cape Colony | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1908 | law adviser | Transvaal | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1910–1911 | ag. atty.-gen. | Transvaal | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1913 | law adviser | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 4 | 1914 | ag. atty.-gen. | Cape Province | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `de Villiers, C. W___South Africa___1912`

- Staff-list name: **de Villiers, C. W** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | C. W. de Villiers | Law Advisers | Department of Justice | — | — |
| 1914 | C. W. de Villiers | Law Advisers | Department of Justice | — | — |
| 1918 | C. W. de Villiers | Attorney-General, Transvaal | Department of Justice | — | — |

### Deterministic checks: `de-villiers_charles-william_b1876` vs `de Villiers, C. W___South Africa___1912`

- [PASS] surname_gate: bio 'DE VILLIERS' vs stint 'de Villiers, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1912, birth 1876 (age 36)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

