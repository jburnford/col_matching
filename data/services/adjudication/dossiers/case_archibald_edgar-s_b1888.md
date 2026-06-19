<!-- {"case_id": "case_archibald_edgar-s_b1888", "bio_ids": ["archibald_edgar-s_b1888"], "stint_ids": ["Archibald, Edgar S___Canada___1920"]} -->
# Dossier case_archibald_edgar-s_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `archibald_edgar-s_b1888`

- Printed name: **ARCHIBALD, EDGAR S.**
- Birth year: 1888 (attested in editions [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1920-L51455.v` — printed in editions [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940]:**

> ARCHIBALD, EDGAR S., B.A., B.S.A.—B. 1888; recd. pmrv. educn. at Yarmouth pub. schl. and Yarmouth acad.; grad. Acadia Univ., 1906; also grad. from the Nova Scotia hort. schl. in the same year, and from Nova Scotia agric. coll. in 1906; recd. deg. of Bach. of Scien. Agric. from the Ontario agric. coll., 1908; inst. of agric. and experimt. at the Nova Scotia agric. coll., 1908; prof. of agric. and farm supt. of the same coll. in 1910; entd. the serv. of the Fed. Dept. of Agric. in June, 1912, as Dominion animal husbandman at the Cent. Exptmtl. Farm, Ottawa; ag. dir. of Exptmtl. Farms, 1918-1919; dir., June, 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | inst. of agric. and experimt. | Nova Scotia | [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1910 | prof. of agric. and farm supt. | — | [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1912 | Dominion animal husbandman | Ottawa | [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1918–1919 | ag. dir. of Exptmtl. Farms | — | [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1919 | dir. | — | [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Archibald, Edgar S___Canada___1920`

- Staff-list name: **Archibald, Edgar S** | colony: **Canada** | listed 1920–1922 | editions [1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Edgar S. Archibald | Director of Experimental Farms | Agriculture and Statistics | — | — |
| 1922 | Edgar S. Archibald | Director of Experimental Farms | Department of Agriculture | — | — |

### Deterministic checks: `archibald_edgar-s_b1888` vs `Archibald, Edgar S___Canada___1920`

- [PASS] surname_gate: bio 'ARCHIBALD' vs stint 'Archibald, Edgar S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1920, birth 1888 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1922
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

