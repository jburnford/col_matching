<!-- {"case_id": "case_maclaren_murray_b1861", "bio_ids": ["maclaren_murray_b1861"], "stint_ids": ["Maclaren, M___Nigeria___1915"]} -->
# Dossier case_maclaren_murray_b1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['maclaren_murray_b1861'] carry a single initial only — the namesake trap applies.

## Biography `maclaren_murray_b1861`

- Printed name: **MACLAREN, MURRAY**
- Birth year: 1861 (attested in editions [1931, 1932, 1936])
- Honours: C.M.G., Commander of Order of St. John of Jerusalem, Order of Avia Portugal, Order of Avis Portugal
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L66413.v` — printed in editions [1931, 1932, 1936]:**

> MACLAREN, COL. THK. HON. MURRAY, C.A.M.C., C.M.G., L.L.D., M.D., C.M., M.R.C.S., F.A.C.S., Commander of Order of St. John of Jerusalem, also of Order of Avis Portugal.—B. 1861; ed. Grammar Sch., St. John, N.B.; univ. of New Brunswick; Edinburgh univ.; Vienna; served overseas, 1914-19; 1st el. to H. of C., Canada, 1921; re-el. at g. e., 1925 and 1926; min. of pensions and national health in Bennett admntr., 1930; lieut. gov., New Brunswick, 1935.

**Version `col1933-L61806.v` — printed in editions [1933, 1934, 1935, 1940]:**

> MACLAREN, COL. THE HON. MURRAY, C.A.M.C., C.M.G., L.D., M.D., C.M., M.R.C.S., F.A.C.S., Commander of Order of St. John of Jerusalem, also of Order of Avia Portugal.—B. 1861; ed. Grainmar Schol., St. John, N. B.; univ. of New Brunawick; Edinburgh univ.; Vienna; served overseas, 1914-19; lat el. to H. of C., Canada, 1921; re-el. at g. e., 1925 and 1926; min. of pensions and national health in Bennett admstrn., 1930; lieut. gov., New Brunswick, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | served overseas | — | [1931, 1932, 1936] |
| 1 | 1914–1919 | — | — | [1933, 1934, 1935, 1940] |
| 2 | 1921–1921 | 1st el. to H. of C. | Canada | [1931, 1932, 1933, 1934, 1935, 1936, 1940] |
| 3 | 1925–1926 | re-el. at g. e. | — | [1931, 1932, 1933, 1934, 1935, 1936, 1940] |
| 4 | 1930–1930 | min. of pensions and national health | — | [1931, 1932, 1933, 1934, 1935, 1936, 1940] |
| 5 | 1935–1935 | lieut. gov. | New Brunswick | [1931, 1932, 1933, 1934, 1935, 1936, 1940] |

## Candidate stint `Maclaren, M___Nigeria___1915`

- Staff-list name: **Maclaren, M** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | M. Maclaren | Sixty Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | M. Maclaren | Assistant District Officer | Southern Provinces | — | — |
| 1919 | M. Maclaren | Sixty Assistant District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `maclaren_murray_b1861` vs `Maclaren, M___Nigeria___1915`

- [PASS] surname_gate: bio 'MACLAREN' vs stint 'Maclaren, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1915, birth 1861 (age 54)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1919
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

