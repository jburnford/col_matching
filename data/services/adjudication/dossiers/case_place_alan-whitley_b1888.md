<!-- {"case_id": "case_place_alan-whitley_b1888", "bio_ids": ["place_alan-whitley_b1888"], "stint_ids": ["Place, A. W___Uganda___1927"]} -->
# Dossier case_place_alan-whitley_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `place_alan-whitley_b1888`

- Printed name: **PLACE, ALAN WHITLEY**
- Birth year: 1888 (attested in editions [1935, 1936, 1937])
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `dol1935-L61501.v` — printed in editions [1935, 1936, 1937]:**

> PLACE, ALAN WHITLEY.—B. 1888; native affrs. dept., S. Rhodesia, 1910-19; milly. serv., 2nd Rhodesia Regt., 1915-16, 4th K. A. R., 1916-24; cadet, Uganda, 1924; astt. sec., 1927; temp. serving in D.O. and C.O., 1928-29; senr. astt. sec., Uganda, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910–1919 | native affrs. dept. | Southern Rhodesia | [1935, 1936, 1937] |
| 1 | 1915–1916 | milly. serv., 2nd Rhodesia Regt. | — | [1935, 1936, 1937] |
| 2 | 1916–1924 | 4th K. A. R. | — | [1935, 1936, 1937] |
| 3 | 1924 | cadet | Uganda | [1935, 1936, 1937] |
| 4 | 1927 | astt. sec. | — | [1935, 1936, 1937] |
| 5 | 1928–1929 | temp. serving in D.O. and C.O. | — | [1935, 1936, 1937] |
| 6 | 1934 | senr. astt. sec. | Uganda | [1935, 1936, 1937] |

## Candidate stint `Place, A. W___Uganda___1927`

- Staff-list name: **Place, A. W** | colony: **Uganda** | listed 1927–1929 | editions [1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | A. W. Place | Administrative Officer | Provincial Administration | — | — |
| 1928 | A. W. Place | Assistant Secretary | Secretariat | — | — |
| 1929 | A. W. Place | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `place_alan-whitley_b1888` vs `Place, A. W___Uganda___1927`

- [PASS] surname_gate: bio 'PLACE' vs stint 'Place, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1927, birth 1888 (age 39)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [FAIL] position_sim: best 25 vs bar 60: 'cadet' ~ 'Assistant Secretary'
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

