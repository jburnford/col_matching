<!-- {"case_id": "case_winster_reginald-thomas-herbert-fletcher_b1885", "bio_ids": ["winster_reginald-thomas-herbert-fletcher_b1885"], "stint_ids": ["Winter, R___Nigeria___1929"]} -->
# Dossier case_winster_reginald-thomas-herbert-fletcher_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `winster_reginald-thomas-herbert-fletcher_b1885`

- Printed name: **WINSTER, Reginald Thomas Herbert Fletcher**
- Birth year: 1885 (attested in editions [1948, 1949, 1950, 1951])
- Honours: K.C.M.G. (1948), P.C. (1945)
- Terminal: resigned 1949 — “resig., 1949”
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36985.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WINSTER, 1st Baron (1942) of Witherslack, Reginald Thomas Herbert Fletcher, K.C.M.G. (1948), P.C. (1945).—b. 1885; J.P. County of Surrey, M.P. 1923–24 and 1935–41; min. of civil aviation, 1945–46; gov. and c.in-c., Cyp., 1947; resig., 1949; joint author of The Air Defences of Great Britain and of The War on Our Doorstep.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923–1941 | M.P. | — | [1948, 1949, 1950, 1951] |
| 1 | 1945–1946 | min. of civil aviation | — | [1948, 1949, 1950, 1951] |
| 2 | 1947–1947 | gov. and c.in-c. | Cyprus | [1948, 1949, 1950, 1951] |

## Candidate stint `Winter, R___Nigeria___1929`

- Staff-list name: **Winter, R** | colony: **Nigeria** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | R. Winter | Superintendents (Motor Traffic Branch) | Marine | D.C.M., M.M. | — |
| 1930 | R. Winter | Superintendents (Motor Traffic Branch) | Police | D.C.M., M.M. | — |

### Deterministic checks: `winster_reginald-thomas-herbert-fletcher_b1885` vs `Winter, R___Nigeria___1929`

- [PASS] surname_gate: bio 'WINSTER' vs stint 'Winter, R' (fuzzy:1)
- [PASS] initials: bio ['R', 'T', 'H', 'F'] ~ stint ['R']
- [PASS] age_gate: stint starts 1929, birth 1885 (age 44)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

