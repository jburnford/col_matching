<!-- {"case_id": "case_blake_frederick-charles_b1895", "bio_ids": ["blake_frederick-charles_b1895"], "stint_ids": ["Blake, F. C___Gold Coast___1927", "Blake, F. C___Gold Coast___1949"]} -->
# Dossier case_blake_frederick-charles_b1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blake_frederick-charles_b1895`

- Printed name: **BLAKE, Frederick Charles**
- Birth year: 1895 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31239.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BLAKE, Frederick Charles.—b. 1895; ed. Bevois Town Sch., Southampton; on mil. serv., 1914-15; ordnance survey, Eng., 1910; hydrographic branch, Admiralty, 1915-18; ordnance survey, Eng., 1918; computer, survey dept., G.C., 1924; cartographer, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | ordnance survey, Eng | — | [1948, 1949, 1950, 1951] |
| 1 | 1915–1918 | hydrographic branch, Admiralty | — | [1948, 1949, 1950, 1951] |
| 2 | 1918 | ordnance survey, Eng | — | [1948, 1949, 1950, 1951] |
| 3 | 1924 | computer, survey dept. | Gold Coast | [1948, 1949, 1950, 1951] |
| 4 | 1925 | cartographer | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Blake, F. C___Gold Coast___1927`

- Staff-list name: **Blake, F. C** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. C. Blake | Record Keeper and Cartographer | Records and Reproduction | — | — |
| 1928 | F. C. Blake | Record Keeper and Cartographer | Survey Department | — | — |
| 1929 | F. C. Blake | Record Keeper and Cartographer | Records and Reproduction | — | — |
| 1930 | F. C. Blake | Record Keeper and Cartographer | Survey Department | — | — |
| 1932 | F. C. Blake | Record Keeper and Cartographer | Survey Department | — | — |
| 1934 | F. C. Blake | Record Keeper and Cartographer | Survey Department | — | — |
| 1936 | F. C. Blake | Record Keeper and Cartographer | Survey Department | — | — |

### Deterministic checks: `blake_frederick-charles_b1895` vs `Blake, F. C___Gold Coast___1927`

- [PASS] surname_gate: bio 'BLAKE' vs stint 'Blake, F. C' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F', 'C']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1936
- [PASS] position_sim: best 100 vs bar 60: 'cartographer' ~ 'Record Keeper and Cartographer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Blake, F. C___Gold Coast___1949`

- Staff-list name: **Blake, F. C** | colony: **Gold Coast** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. C. Blake | Cartographer | Survey Department | — | — |
| 1950 | F. C. Blake | Cartographer | SURVEY DEPARTMENT | — | — |

### Deterministic checks: `blake_frederick-charles_b1895` vs `Blake, F. C___Gold Coast___1949`

- [PASS] surname_gate: bio 'BLAKE' vs stint 'Blake, F. C' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F', 'C']
- [PASS] age_gate: stint starts 1949, birth 1895 (age 54)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

