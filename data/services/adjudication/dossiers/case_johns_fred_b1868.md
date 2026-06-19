<!-- {"case_id": "case_johns_fred_b1868", "bio_ids": ["johns_fred_b1868"], "stint_ids": ["Johns, F___Australia___1918", "Johns, F___Southern Nigeria___1905"]} -->
# Dossier case_johns_fred_b1868

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['johns_fred_b1868'] carry a single initial only — the namesake trap applies.

## Biography `johns_fred_b1868`

- Printed name: **JOHNS, FRED**
- Birth year: 1868 (attested in editions [1915])
- Honours: F.J.I., F.J.L.
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1928, 1929, 1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1915-L48142.v` — printed in editions [1915]:**

> JOHNS, FRED, F.J.L.—B. 1868; ed. Cornw. England; on Adelaide newspaper literary sect. from 1885 to 1914; leader of the first Hansard staff, S. Australian parlmt. since Jan., 1914; author of "John's Notable Australian" (1894 and 1896), and of "Fred John's Anna" (mainly a biographical record of Australian prominent people).

**Version `col1917-L50792.v` — printed in editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1928, 1929, 1931, 1932, 1933, 1934]:**

> JOHNS, FRED, F.J.I.—B. 1868; ed. Cornwall, England; on Adelaide newspaper literary staffs from 1885 to 1914; leader of the first offi. Hansard staff, S. Australian parlmt. since July, 1914; author of "John's Notable Australians" (1906 and 1908), and of "Australasia's Prominent People," "Notables, Past and Present," "Who's who in the Commonwealth" (1922), and "A Journalist's Jottings" (1922); sec. of Adelaide branch of Royal Society of St. George, and hon. sec., Matthew Flinders' National Statue, City of Adelaide; also hon. sec., Princess Mary wedding gift fund, S. Australia.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885–1914 | on Adelaide newspaper literary sect. | Adelaide | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1928, 1929, 1931, 1932, 1933, 1934] |
| 1 | 1914 | leader of the first Hansard staff | South Australia | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1928, 1929, 1931, 1932, 1933, 1934] |

## Candidate stint `Johns, F___Australia___1918`

- Staff-list name: **Johns, F** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | F. Johns | Leader Hansard Staff | Government Reporting Department | — | — |
| 1927 | F. Johns | Leader Hansard Staff | Government Reporting Department | — | — |

### Deterministic checks: `johns_fred_b1868` vs `Johns, F___Australia___1918`

- [PASS] surname_gate: bio 'JOHNS' vs stint 'Johns, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1918, birth 1868 (age 50)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Johns, F___Southern Nigeria___1905`

- Staff-list name: **Johns, F** | colony: **Southern Nigeria** | listed 1905–1909 | editions [1905, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | F. Johns | Foreman of Works | Public Works | — | — |
| 1907 | F. Johns | Inspectors of Works | Public Works Department | — | — |
| 1909 | F. Johns | Inspectors of Works | Public Works Department | — | — |

### Deterministic checks: `johns_fred_b1868` vs `Johns, F___Southern Nigeria___1905`

- [PASS] surname_gate: bio 'JOHNS' vs stint 'Johns, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1905, birth 1868 (age 37)
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

