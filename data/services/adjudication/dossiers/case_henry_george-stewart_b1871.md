<!-- {"case_id": "case_henry_george-stewart_b1871", "bio_ids": ["henry_george-stewart_b1871"], "stint_ids": ["Henry, G___Leeward Islands___1900", "Henry, G___St Christopher and Nevis___1896"]} -->
# Dossier case_henry_george-stewart_b1871

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 42 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `henry_george-stewart_b1871`

- Printed name: **HENRY, GEORGE STEWART**
- Birth year: 1871 (attested in editions [1924, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934])
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1924-L55048.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934]:**

> HENRY, HON. GEORGE STEWART, B.A., LL.B.—B. 1871; ed. pub. schs., Upper Can. Coll., Univ. of Toronto, and Ont. Agric. Coll.; farmer; el. to Ont. legis., at by-el., 1913; re-el., 1914, 1919 and 1923; min. of pub. wks. and highways in Ferguson admnstr., 1923; premier, Ontario, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1913 | el. to Ont. legis. | Ontario | [1924, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934] |
| 1 | 1914–1923 | re-el. | — | [1924, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934] |
| 2 | 1923–1923 | min. of pub. wks. and highways in Ferguson admnstr. | — | [1924, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934] |
| 3 | 1930–1930 | premier | Ontario | [1924, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934] |

## Candidate stint `Henry, G___Leeward Islands___1900`

- Staff-list name: **Henry, G** | colony: **Leeward Islands** | listed 1900–1908 | editions [1900, 1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | G. Henry | Head Warden | Gaol | — | — |
| 1905 | G. Henry | Chief Warden | Gaol | — | — |
| 1906 | G. Henry | Chief Warden | Gaol | — | — |
| 1907 | G. Henry | Chief Warden | Gaol | — | — |
| 1908 | G. Henry | Warder | Gaol | — | — |

### Deterministic checks: `henry_george-stewart_b1871` vs `Henry, G___Leeward Islands___1900`

- [PASS] surname_gate: bio 'HENRY' vs stint 'Henry, G' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G']
- [PASS] age_gate: stint starts 1900, birth 1871 (age 29)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Henry, G___St Christopher and Nevis___1896`

- Staff-list name: **Henry, G** | colony: **St Christopher and Nevis** | listed 1896–1898 | editions [1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | G. Henry | Superintendent and Head Warder | Gaol | — | — |
| 1898 | G. Henry | Head Warder | Gaol | — | — |

### Deterministic checks: `henry_george-stewart_b1871` vs `Henry, G___St Christopher and Nevis___1896`

- [PASS] surname_gate: bio 'HENRY' vs stint 'Henry, G' (exact)
- [PASS] initials: bio ['G', 'S'] ~ stint ['G']
- [PASS] age_gate: stint starts 1896, birth 1871 (age 25)
- [FAIL] colony: no placed event resolves to 'St Christopher and Nevis'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
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

