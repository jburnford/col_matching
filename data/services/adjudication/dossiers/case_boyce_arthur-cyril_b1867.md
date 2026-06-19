<!-- {"case_id": "case_boyce_arthur-cyril_b1867", "bio_ids": ["boyce_arthur-cyril_b1867"], "stint_ids": ["Boyce, Arthur Cyril___Canada___1906", "Boyce, Arthur Cyril___Canada___1918"]} -->
# Dossier case_boyce_arthur-cyril_b1867

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `boyce_arthur-cyril_b1867`

- Printed name: **BOYCE, ARTHUR CYRIL**
- Birth year: 1867 (attested in editions [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931])
- Appears in editions: [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1921-L54671.v` — printed in editions [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]:**

> BOYCE, ARTHUR CYRIL.—B. 1867; ed. Wakefield, York, Carlisle; called to bar, 1890 (hons. and med.); K.C., 1908; D.C.L. (hon. couns.) Bishop's Coll., Lenoxville, 1913; unsuccessful candidate for H. of C., Canada, Algoma, 1900; elected, West Algoma, 1904; re-elected 1908 and 1911; mem., bd. of rly. comsnrs., Canada, 1917; chancellor, diocese of Algoma; hon. lieut.-col., 51st (Soo) Regt.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890–1890 | called to bar | — | [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 1 | 1900–1900 | unsuccessful candidate for H. of C. | Canada | [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 2 | 1904–1904 | elected | — | [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 3 | 1908–1908 | K.C. | — | [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 4 | 1908–1911 | re-elected | — | [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 5 | 1913–1913 | D.C.L. (hon. couns.) | — | [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 6 | 1917–1917 | mem., bd. of rly. comsnrs. | Canada | [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |

## Candidate stint `Boyce, Arthur Cyril___Canada___1906`

- Staff-list name: **Boyce, Arthur Cyril** | colony: **Canada** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | Arthur Cyril Boyce | — | — | — | — |
| 1907 | Arthur Cyril Boyce | Member of Parliament | Legislative | — | — |
| 1908 | Arthur Cyril Boyce | — | — | — | — |

### Deterministic checks: `boyce_arthur-cyril_b1867` vs `Boyce, Arthur Cyril___Canada___1906`

- [PASS] surname_gate: bio 'BOYCE' vs stint 'Boyce, Arthur Cyril' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1906, birth 1867 (age 39)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Boyce, Arthur Cyril___Canada___1918`

- Staff-list name: **Boyce, Arthur Cyril** | colony: **Canada** | listed 1918–1922 | editions [1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | A. C. Boyce | Commissioner | Permanent Railway Commission | — | — |
| 1919 | A. C. Boyce | Commissioner | Permanent Railway Commission | — | — |
| 1920 | A. C. Boyce | Commissioner | Permanent Railway Commission | — | — |
| 1922 | A. C. Boyce | Commissioner | Railway Commission | — | — |

### Deterministic checks: `boyce_arthur-cyril_b1867` vs `Boyce, Arthur Cyril___Canada___1918`

- [PASS] surname_gate: bio 'BOYCE' vs stint 'Boyce, Arthur Cyril' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1918, birth 1867 (age 51)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1918-1922
- [FAIL] position_sim: best 42 vs bar 60: 'mem., bd. of rly. comsnrs.' ~ 'Commissioner'
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

