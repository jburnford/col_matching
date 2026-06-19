<!-- {"case_id": "case_caron_joseph-edouard_b1866", "bio_ids": ["caron_joseph-edouard_b1866"], "stint_ids": ["Caron, J. R. E. A___Canada___1883", "Caron, Joseph Edouard___Canada___1917"]} -->
# Dossier case_caron_joseph-edouard_b1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `caron_joseph-edouard_b1866`

- Printed name: **CARON, JOSEPH EDOUARD**
- Birth year: 1866 (attested in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931])
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1911-L43698.v` — printed in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]:**

> CARON, HON. JOSEPH EDOUARD.—B. 1866; ed. at St. Ann's Coll.; elected to legis. assem., Quebec, 1902, 1904, 1908, 1912 and 1916; min. without portfolio, Jan., 1909; min. of agric., Oct., 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1916 | elected to legis. assem. | Quebec | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 1 | 1909 | min. without portfolio | — | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 2 | 1909 | min. of agric. | — | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |

## Candidate stint `Caron, J. R. E. A___Canada___1883`

- Staff-list name: **Caron, J. R. E. A** | colony: **Canada** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. R. E. A. Caron | Minister of Militia | Militia and Defence Department | — | — |
| 1886 | J. R. E. A. Caron | Minister of Militia | Militia and Defence | — | — |

### Deterministic checks: `caron_joseph-edouard_b1866` vs `Caron, J. R. E. A___Canada___1883`

- [PASS] surname_gate: bio 'CARON' vs stint 'Caron, J. R. E. A' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'R', 'E', 'A']
- [PASS] age_gate: stint starts 1883, birth 1866 (age 17)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Caron, Joseph Edouard___Canada___1917`

- Staff-list name: **Caron, Joseph Edouard** | colony: **Canada** | listed 1917–1922 | editions [1917, 1918, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | Hon. Joseph Edouard Caron | Minister of Agriculture | Executive Council | — | — |
| 1918 | Joseph Edouard Caron | Minister of Agriculture | Executive Council | — | — |
| 1919 | Joseph Edouard Caron | Minister of Agriculture | Executive Council | — | — |
| 1922 | J. E. Caron | Minister of Agriculture | Executive Council | — | — |

### Deterministic checks: `caron_joseph-edouard_b1866` vs `Caron, Joseph Edouard___Canada___1917`

- [PASS] surname_gate: bio 'CARON' vs stint 'Caron, Joseph Edouard' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1917, birth 1866 (age 51)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1922
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

