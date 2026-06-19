<!-- {"case_id": "case_woodehouse_john-leslie_b1892", "bio_ids": ["woodehouse_john-leslie_b1892"], "stint_ids": ["Woodhouse, J. L___Uganda___1919"]} -->
# Dossier case_woodehouse_john-leslie_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `woodehouse_john-leslie_b1892`

- Printed name: **WOODEHOUSE, JOHN LESLIE**
- Birth year: 1892 (attested in editions [1928])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1928-L71255.v` — printed in editions [1928]:**

> WOODEHOUSE, JOHN LESLIE.—B. 1892; ed. Merchant Taylors Schl.; ast. transport offr., with rank of lieut., Uganda Transport Corps, 27th Nov., 1914; ment. in desps. for service in German E. Africa, 22nd Nov., 1916; ast. dist. comsnr., Uganda, 30th Dec., 1916; 2nd grade adminstr. offr., Tanganyika Territory, 17th June, 1920; dist. offr., 4th June, 1926.

**Version `col1927-L63988.v` — printed in editions [1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]:**

> WOODHOUSE, JOHN LESLIE.—B. 1892; ed. Merchant Taylors Schol.; asst. transport offr., with rank of lieut., Uganda Transport Corps, Nov., 1914; ment. in despatches for service in German E. Africa, Nov., 1916; asst. dist. commnr., Uganda, Dec., 1916; 2nd grade adminstr. offr., Tanganyika Territory, June, 1920; dist. offr., June, 1926.

**Version `col1937-L65990.v` — printed in editions [1937]:**

> GOODHOUSE, JOHN LESLIE.—B. 1892; ed. merchant Taylor's Schl.; asst. transport offr., rank of lieut., Uganda Transport Corps, 1914; ment. in despatches for service in German Africa, Nov., 1916; asst. dist. commr., Tanganyika Territory, June, 1920; dist. June, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | ast. transport offr., with rank of lieut., Uganda Transport Corps | Uganda | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1916 | ment. in desps. for service in German E. Africa | Uganda | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1920 | 2nd grade adminstr. offr., Tanganyika Territory | Tanganyika | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 3 | 1926 | dist. offr | Tanganyika *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Woodhouse, J. L___Uganda___1919`

- Staff-list name: **Woodhouse, J. L** | colony: **Uganda** | listed 1919–1920 | editions [1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | J. L. Woodhouse | Assistant District Commissioner | Civil Establishment | — | — |
| 1920 | J. L. Woodhouse | Assistant District Commissioner | Administration | — | — |

### Deterministic checks: `woodehouse_john-leslie_b1892` vs `Woodhouse, J. L___Uganda___1919`

- [PASS] surname_gate: bio 'WOODEHOUSE' vs stint 'Woodhouse, J. L' (fuzzy:1)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1919, birth 1892 (age 27)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1919-1920
- [FAIL] position_sim: best 42 vs bar 60: 'ment. in desps. for service in German E. Africa' ~ 'Assistant District Commissioner'
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

