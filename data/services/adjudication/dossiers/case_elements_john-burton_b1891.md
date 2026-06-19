<!-- {"case_id": "case_elements_john-burton_b1891", "bio_ids": ["elements_john-burton_b1891"], "stint_ids": ["Clements, J. B___Nyasaland___1921"]} -->
# Dossier case_elements_john-burton_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `elements_john-burton_b1891`

- Printed name: **ELEMENTS, JOHN BURTON**
- Birth year: 1891 (attested in editions [1927])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1927-L57903.v` — printed in editions [1927]:**

> ELEMENTS, JOHN BURTON, B.Sc. Forestry (Edin.)—B. 1891; for. offr., Nyassaland, 10th Sept., 1920; ag. ch. for. offr., Oct. to Dec., 1920 and May to Dec., 1923; ch. for. offr., 19th Dec., 1923.

**Version `col1928-L65064.v` — printed in editions [1928, 1929, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940]:**

> CLEMEN'TS, JOHN BURTON, D.Sc., Forestry (Edin.)—B. 1891; for. offr., Nyasa land, 10th Sept., 1920; ag. ch. for offr., Oct. to Dec., 1920 and May to Dec., 1923; ch. for offr., 19th Dec., 1923.

**Version `col1930-L63436.v` — printed in editions [1930]:**

> CLEMMENTS, JOHN BURTON, B.Sc., Forestry (Edin.)—B. 1891; for. offr., Nyasaland, 10th Sept., 1920; ag. ch. for. offr., Oct. to Dec., 1920; and May to Dec., 1923; ch. for. offr., 19th Dec., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | for. offr., Nyassaland | Nyasa land | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940] |
| 1 | 1920 | ag. ch. for. offr | Nyasaland *(inherited from previous clause)* | [1927, 1930] |
| 2 | 1923 | ag. ch. for. offr | Nyasa land *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1939, 1940] |
| 3 | 1923 | and | Nyasaland *(inherited from previous clause)* | [1930] |

## Candidate stint `Clements, J. B___Nyasaland___1921`

- Staff-list name: **Clements, J. B** | colony: **Nyasaland** | listed 1921–1940 | editions [1921, 1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. B. Clements | Forest Officer | Agricultural Department | — | — |
| 1922 | J. B. Clements | Forest Officer | Forestry Division | — | — |
| 1923 | J. B. Clements | Forest Officer | Agricultural Department | — | — |
| 1924 | J. B. Clements | Forest Officer | Forestry Division | — | — |
| 1925 | J. B. Clements | Chief Forest Officer | Agricultural Department | — | — |
| 1928 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1929 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1930 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1931 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1932 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1933 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1934 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1936 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1937 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1939 | J. B. Clements | Conservator of Forests | Forestry | — | — |
| 1940 | J. B. Clements | Conservator of Forests | Forestry | — | — |

### Deterministic checks: `elements_john-burton_b1891` vs `Clements, J. B___Nyasaland___1921`

- [PASS] surname_gate: bio 'ELEMENTS' vs stint 'Clements, J. B' (fuzzy:1)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1921, birth 1891 (age 30)
- [PASS] colony: 4 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1921-1940
- [PASS] position_sim: best 65 vs bar 60: 'ag. ch. for. offr' ~ 'Chief Forest Officer'
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

