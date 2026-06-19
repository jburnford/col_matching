<!-- {"case_id": "case_berndson_david-murray_b1874", "bio_ids": ["berndson_david-murray_b1874"], "stint_ids": ["Bernon, M___Mauritius___1921"]} -->
# Dossier case_berndson_david-murray_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `berndson_david-murray_b1874`

- Printed name: **BERNDSON, DAVID MURRAY**
- Birth year: 1874 (attested in editions [1934])
- Honours: C.B. (1930), C.M.G. (1918), M.V.O. (1910)
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L56220.v` — printed in editions [1934]:**

> BERNDSON, ADMIRAL SIR DAVID MURRAY, C.B. (1930), C.M.G. (1918), M.V.O. (1910).—B. 1874; ed. Stubbington and H.M.S. "Britannia"; served with Brass river expedit. and M'Wele expedit., 1905; Ashanti, 1906; Great War, 1914-19, including operns. in Rufiji river, 1915; served with Grand Fleet, 1918; capt., sup't., Pembroke dockyard, and senr. naval offr., Milford Haven, 1920-22; rear-adm., 1922; naval A.D.C. to the King, 1921-22; senr. naval offr., Yangtze river, 1923-26; C. in C., China station, April, 1925; Africa station, 1927-29; vice-adm'l., 1927; high commr., S. Africa, June-Dec., 1928; adm'l., 1931; adm'y. rep., L. of N. perm't. advisory comm'r., 1929-31; gov't. and comdr-in-ch., Newfoundland, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905–1905 | served with Brass river expedit. and M'Wele expedit. | — | [1934] |
| 1 | 1906–1906 | — | Ashanti | [1934] |
| 2 | 1914–1919 | Great War, including operns. in Rufiji river | — | [1934] |
| 3 | 1918–1918 | served with Grand Fleet | — | [1934] |
| 4 | 1920–1922 | capt., sup't., Pembroke dockyard, and senr. naval offr. | — | [1934] |
| 5 | 1921–1922 | naval A.D.C. to the King | — | [1934] |
| 6 | 1922–1922 | rear-adm. | — | [1934] |
| 7 | 1923–1926 | senr. naval offr., Yangtze river | — | [1934] |
| 8 | 1925–1925 | C. in C., China station | China | [1934] |
| 9 | 1927–1929 | Africa station | Africa | [1934] |
| 10 | 1927–1927 | vice-adm'l. | — | [1934] |
| 11 | 1928–1928 | high commr. | South Africa | [1934] |
| 12 | 1929–1931 | adm'y. rep., L. of N. perm't. advisory comm'r. | — | [1934] |
| 13 | 1931–1931 | adm'l. | — | [1934] |
| 14 | 1932 | gov't. and comdr-in-ch. | Newfoundland | [1934] |

## Candidate stint `Bernon, M___Mauritius___1921`

- Staff-list name: **Bernon, M** | colony: **Mauritius** | listed 1921–1927 | editions [1921, 1922, 1923, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | M. Bernon | 1st Class Tidewaiters | Outdoor Branch | — | — |
| 1922 | M. Bernon | 1st Class Tidewaiters | Outdoor Branch | — | — |
| 1923 | M. Bernon | 1st Class Tidewaiter | Outdoor Branch | — | — |
| 1925 | M. Bernon | 1st Class Tidewater | Outdoor Branch | — | — |
| 1927 | M. Bernon | 1st Class Tidewaiter | Outdoor Branch | — | — |

### Deterministic checks: `berndson_david-murray_b1874` vs `Bernon, M___Mauritius___1921`

- [PASS] surname_gate: bio 'BERNDSON' vs stint 'Bernon, M' (fuzzy:2)
- [PASS] initials: bio ['D', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1921, birth 1874 (age 47)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1927
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

