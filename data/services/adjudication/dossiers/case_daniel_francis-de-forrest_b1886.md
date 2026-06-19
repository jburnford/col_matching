<!-- {"case_id": "case_daniel_francis-de-forrest_b1886", "bio_ids": ["daniel_francis-de-forrest_b1886"], "stint_ids": ["Daniel, F. de F___Nigeria___1918", "Daniel, F___British Guiana___1924"]} -->
# Dossier case_daniel_francis-de-forrest_b1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `daniel_francis-de-forrest_b1886`

- Printed name: **DANIEL, FRANCIS DE FORREST**
- Birth year: 1886 (attested in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1932, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L59504.v` — printed in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940]:**

> DANIEL, FRANCIS DE FORREST.—B. 1886; ed. Marlborough Coll.; admitted solr., 1910; asst. accountant, Lagos rly., July, 1912; transfd., cust. dept., May, 1913; asst. dist. offr., N. Prov., Nigeria, July, 1914; res., Mar., 1930; staff grade, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | admitted solr | — | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1912 | asst. accountant, Lagos rly | Lagos | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1913 | transfd., cust. dept | Lagos *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1914 | asst. dist. offr., N. Prov. | Nigeria | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1930 | res | Nigeria *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1937 | staff grade | Nigeria *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Daniel, F. de F___Nigeria___1918`

- Staff-list name: **Daniel, F. de F** | colony: **Nigeria** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | F. de F. Daniel | Sixty‑four Assistant District Officer | Northern Provinces | — | — |
| 1919 | F. de F. Daniel | Sixty-four Assistant District Officers | NORTHERN PROVINCES | — | — |

### Deterministic checks: `daniel_francis-de-forrest_b1886` vs `Daniel, F. de F___Nigeria___1918`

- [PASS] surname_gate: bio 'DANIEL' vs stint 'Daniel, F. de F' (exact)
- [PASS] initials: bio ['F', 'D', 'F'] ~ stint ['F', 'D', 'F']
- [PASS] age_gate: stint starts 1918, birth 1886 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1918-1919
- [FAIL] position_sim: best 56 vs bar 60: 'asst. dist. offr., N. Prov.' ~ 'Sixty‑four Assistant District Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Daniel, F___British Guiana___1924`

- Staff-list name: **Daniel, F** | colony: **British Guiana** | listed 1924–1930 | editions [1924, 1925, 1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | F. Daniel | Senior Masters | Queen's College | — | — |
| 1925 | F. Daniel | Senior Masters | Queen's College | — | — |
| 1927 | F. Daniel | Senior Masters | Education | — | — |
| 1928 | F. Daniel | Senior Masters | Education | — | — |
| 1929 | F. Daniel | Assistant Master | Education | — | — |
| 1930 | F. Daniel | Assistant Master | Education | — | — |

### Deterministic checks: `daniel_francis-de-forrest_b1886` vs `Daniel, F___British Guiana___1924`

- [PASS] surname_gate: bio 'DANIEL' vs stint 'Daniel, F' (exact)
- [PASS] initials: bio ['F', 'D', 'F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1924, birth 1886 (age 38)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1930
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

