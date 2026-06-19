<!-- {"case_id": "case_burton_richard-charles-fryer_e1891", "bio_ids": ["burton_richard-charles-fryer_e1891"], "stint_ids": ["Burton, R. C___Cape of Good Hope___1908"]} -->
# Dossier case_burton_richard-charles-fryer_e1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burton_richard-charles-fryer_e1891`

- Printed name: **BURTON, RICHARD CHARLES FRYER**
- Birth year: not printed
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1915-L45688.v` — printed in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]:**

> BURTON, RICHARD CHARLES FRYER.—Entd. Cape civ. serv., 1891; served in census, crown lands and other depts.; dist. forest offr., George, 1902; seconded to proceed to Royal Indian Engineering Coll., Cooper's Hill, for scientific course of forestry; working plans offr., Eastern Conservancy, Oct., 1905; dist. forest offr., George, Feb., 1909; conservator of forests, Natal, Mar., 1914; ditto, Midland conservancy, Dec., 1914; ditto, Western conservancy, Aug., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | Entd. Cape civ. serv | — | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 1 | 1902 | dist. forest offr., George | — | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 2 | 1905 | working plans offr., Eastern Conservancy | — | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 3 | 1909 | dist. forest offr., George | — | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 4 | 1914 | conservator of forests | Natal | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 5 | 1929 | ditto, Western conservancy | Natal *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |

## Candidate stint `Burton, R. C___Cape of Good Hope___1908`

- Staff-list name: **Burton, R. C** | colony: **Cape of Good Hope** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | R. Burton | District Forest Officers | Office of Chief Conservator of Forests | — | — |
| 1909 | R. Burton | District Forest Officer | Office of Chief Conservator of Forests | — | — |

### Deterministic checks: `burton_richard-charles-fryer_e1891` vs `Burton, R. C___Cape of Good Hope___1908`

- [PASS] surname_gate: bio 'BURTON' vs stint 'Burton, R. C' (exact)
- [PASS] initials: bio ['R', 'C', 'F'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
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

