<!-- {"case_id": "case_morley_arthur-joseph_b1905", "bio_ids": ["morley_arthur-joseph_b1905"], "stint_ids": ["Morley, A. J___Nigeria___1936"]} -->
# Dossier case_morley_arthur-joseph_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morley_arthur-joseph_b1905`

- Printed name: **MORLEY, Arthur Joseph**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34776.v` — printed in editions [1948, 1949, 1950, 1951]:**

> MORLEY, Arthur Joseph, B.Sc. (1st cl. hons. maths.) (Liv.), B.A. (hons.) (Camb.)—b. 1905; ed. Bemrose Sch., Derby, Liverpool Univ. (schol.) and Cambridge Univ.; survr., Nig., 1930; senr., 1937; asst. dir. of surveys, 1943; deleg. to assembly of internat. union of geodesy and geophysics, Washington, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | survr. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1937 | senr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1939 | deleg. to assembly of internat. union of geodesy and geophysics, Washington | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1943 | asst. dir. of surveys | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Morley, A. J___Nigeria___1936`

- Staff-list name: **Morley, A. J** | colony: **Nigeria** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | A. J. Morley | Senior Surveyors & Surveyors | Survey Section | — | — |
| 1939 | A. J. Morley | Senior Surveyors | Survey Section | — | — |

### Deterministic checks: `morley_arthur-joseph_b1905` vs `Morley, A. J___Nigeria___1936`

- [PASS] surname_gate: bio 'MORLEY' vs stint 'Morley, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1936-1939
- [FAIL] position_sim: best 48 vs bar 60: 'survr.' ~ 'Senior Surveyors & Surveyors'
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

