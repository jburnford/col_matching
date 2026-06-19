<!-- {"case_id": "case_tumford_william-bryant_b1900", "bio_ids": ["tumford_william-bryant_b1900"], "stint_ids": ["Mumford, W. B___Tanganyika___1924"]} -->
# Dossier case_tumford_william-bryant_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tumford_william-bryant_b1900`

- Printed name: **TUMFORD, William Bryant**
- Birth year: 1900 (attested in editions [1925])
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1925-L58101.v` — printed in editions [1925]:**

> TUMFORD, William Bryant, B.A. (Cantab.), B. 1900; ed. Manchester Gram. Schi. and St. John's Coll., Cambridge; matros, trip, 1920; shipman, R.N., 1918-19; diploma of educn., London, 1923; B. of E. teachers certif., 1923; mast., educn. dept., Tanganyika Territory, 1923.

**Version `col1924-L56762.v` — printed in editions [1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934]:**

> MUMFORD, WILLIAM BRYANT, B.A. (Cantab.).—B. 1900; ed. Manchester Gram. Schl. and St. John's Coll., Cambridge; maths. tripos, 1920; midshipman, R.N., 1918-19; diploma of educn., London, 1923; B. of E. teachers certif., 1923; asst. mast., eduon. dept., Tanganyika Territory, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1919 | shipman, R.N. | — | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 1 | 1920–1920 | matros, trip | — | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 2 | 1923–1923 | diploma of educn. | London | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 3 | 1923–1923 | B. of E. teachers certif. | — | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 4 | 1923–1923 | mast., educn. dept. | Tanganyika Territory | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |

## Candidate stint `Mumford, W. B___Tanganyika___1924`

- Staff-list name: **Mumford, W. B** | colony: **Tanganyika** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | W. B. Mumford | Assistant Masters | Education Department | — | — |
| 1925 | W. B. Mumford | Assistant Masters | Education Department | — | — |

### Deterministic checks: `tumford_william-bryant_b1900` vs `Mumford, W. B___Tanganyika___1924`

- [PASS] surname_gate: bio 'TUMFORD' vs stint 'Mumford, W. B' (fuzzy:1)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1924, birth 1900 (age 24)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
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

