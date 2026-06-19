<!-- {"case_id": "case_harrison_wilfred-hugh-lane_b1900", "bio_ids": ["harrison_wilfred-hugh-lane_b1900"], "stint_ids": ["Harrison, W. H. L___Kenya___1936", "Harrison, W___Nigeria___1936"]} -->
# Dossier case_harrison_wilfred-hugh-lane_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 85 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Harrison, W. H. L___Kenya___1936` is also gate-compatible with biography(ies) outside this case: ['harrison_w_b1905', 'harrison_wilfrid-hugh-lane_b1900'] (already linked elsewhere or filtered).
- NOTE: stint `Harrison, W___Nigeria___1936` is also gate-compatible with biography(ies) outside this case: ['harrison_cuthbert-woodville_b1874', 'harrison_w_b1905', 'harrison_wilfrid-hugh-lane_b1900', 'harrison_william-charles-burke-l_b1904'] (already linked elsewhere or filtered).

## Biography `harrison_wilfred-hugh-lane_b1900`

- Printed name: **HARRISON, Wilfred Hugh Lane**
- Birth year: 1900 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33189.v` — printed in editions [1948, 1949]:**

> HARRISON, Wilfred Hugh Lane.—b. 1900; ed. Durham Sch. and R.N. Coll., Keyham, R.N.; on naval serv. 1939-45 (comdr., R.N. ret.)); hse. mastr., Borstal inst., 1932; supt., approved sch., Ken., 1934; supt. of prisons, H.K., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932–1932 | hse. mastr. | — | [1948, 1949] |
| 1 | 1934–1934 | supt., approved sch. | Kenya | [1948, 1949] |
| 2 | 1939–1945 | on naval serv. | — | [1948, 1949] |
| 3 | 1939–1939 | supt. of prisons | Hong Kong | [1948, 1949] |

## Candidate stint `Harrison, W. H. L___Kenya___1936`

- Staff-list name: **Harrison, W. H. L** | colony: **Kenya** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. H. L. Harrison | Superintendent, Class III Approved School | Prisons Department | — | Lt.-Comdr. |
| 1937 | W. H. L. Harrison | Superintendent, Class III Approved School | Prisons Department | — | Lt. Comdr |
| 1939 | W. H. L. Harrison | Superintendent, Class III Approved School | Prisons Department | — | — |

### Deterministic checks: `harrison_wilfred-hugh-lane_b1900` vs `Harrison, W. H. L___Kenya___1936`

- [PASS] surname_gate: bio 'HARRISON' vs stint 'Harrison, W. H. L' (exact)
- [PASS] initials: bio ['W', 'H', 'L'] ~ stint ['W', 'H', 'L']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Harrison, W___Nigeria___1936`

- Staff-list name: **Harrison, W** | colony: **Nigeria** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. Harrison | Senior Surveyors & Surveyors | Survey Section | — | — |
| 1939 | W. Harrison | Surveyors | Survey Section | — | — |

### Deterministic checks: `harrison_wilfred-hugh-lane_b1900` vs `Harrison, W___Nigeria___1936`

- [PASS] surname_gate: bio 'HARRISON' vs stint 'Harrison, W' (exact)
- [PASS] initials: bio ['W', 'H', 'L'] ~ stint ['W']
- [PASS] age_gate: stint starts 1936, birth 1900 (age 36)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

