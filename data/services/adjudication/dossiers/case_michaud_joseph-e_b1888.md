<!-- {"case_id": "case_michaud_joseph-e_b1888", "bio_ids": ["michaud_joseph-e_b1888"], "stint_ids": ["Michaud, J. Enoil___Canada___1918"]} -->
# Dossier case_michaud_joseph-e_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `michaud_joseph-e_b1888`

- Printed name: **MICHAUD, JOSEPH E.**
- Birth year: 1888 (attested in editions [1936, 1939, 1940])
- Appears in editions: [1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63061.v` — printed in editions [1936, 1939, 1940]:**

> MICHAUD, HON. JOSEPH E., B.A., LL.B.—B. 1888; ed. Quebec Seminary, Laval Univ. (B.A., 1910), St. Dunstan Univ., Charlottetown, P.E.I., Dalhousie Law Sch. (LL.B., 1913); mayor of Edmundston, N.B., 1919, 1932, 1934; el. to legis. of N.B., 1917, re-el. 1920, 1925, 1930; min. without portfolio in Foster govt., 1921, Veniot admnstr., 1923-25; el. to H. of C., 1933; re-el., 1935; min. of fisheries in govt. of Mackenzie King, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1930 | el. to legis. | New Brunswick | [1936, 1939, 1940] |
| 1 | 1919–1934 | mayor of Edmundston | New Brunswick | [1936, 1939, 1940] |
| 2 | 1921–1921 | min. without portfolio in Foster govt. | — | [1936, 1939, 1940] |
| 3 | 1923–1925 | Veniot admnstr. | — | [1936, 1939, 1940] |
| 4 | 1933–1933 | el. to H. of C. | — | [1936, 1939, 1940] |
| 5 | 1935–1935 | re-el. | — | [1936, 1939, 1940] |
| 6 | 1935–1935 | min. of fisheries | — | [1936, 1939, 1940] |

## Candidate stint `Michaud, J. Enoil___Canada___1918`

- Staff-list name: **Michaud, J. Enoil** | colony: **Canada** | listed 1918–1922 | editions [1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | J. E. Michaud | — | Constituencies | — | — |
| 1919 | J. E. Michaud | Member | Constituencies | — | — |
| 1920 | J. E. Michaud | Member | Constituencies | — | — |
| 1922 | J. Enoil Michaud | — | — | — | — |

### Deterministic checks: `michaud_joseph-e_b1888` vs `Michaud, J. Enoil___Canada___1918`

- [PASS] surname_gate: bio 'MICHAUD' vs stint 'Michaud, J. Enoil' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1918, birth 1888 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1918-1922
- [FAIL] position_sim: best 24 vs bar 60: 'mayor of Edmundston' ~ 'Member'
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

