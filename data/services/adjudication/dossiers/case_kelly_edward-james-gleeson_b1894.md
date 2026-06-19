<!-- {"case_id": "case_kelly_edward-james-gleeson_b1894", "bio_ids": ["kelly_edward-james-gleeson_b1894"], "stint_ids": ["Kelly, E. J___Kenya___1927"]} -->
# Dossier case_kelly_edward-james-gleeson_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kelly_edward-james-gleeson_b1894`

- Printed name: **KELLY, EDWARD JAMES GLEESON**
- Birth year: 1894 (attested in editions [1936, 1940])
- Appears in editions: [1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L62125.v` — printed in editions [1936, 1940]:**

> KELLY, EDWARD JAMES GLEESON, M.C.—B. 1894; admstve. offr., cls. IV, Nigeria, 1919; ag. Br. consul., Boma, 1929; admstve. serv., cls. II., 1933; ag. res., 1934; admstve. offr., cls. I., 1934; sec., S. Provs., 1936-38; admstve offr., staff gde., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | admstve. offr., cls. IV | Nigeria | [1936, 1940] |
| 1 | 1929 | ag. Br. consul., Boma | Nigeria *(inherited from previous clause)* | [1936, 1940] |
| 2 | 1933 | admstve. serv., cls. II | Nigeria *(inherited from previous clause)* | [1936, 1940] |
| 3 | 1934 | ag. res | Nigeria *(inherited from previous clause)* | [1936, 1940] |
| 4 | 1936–1938 | sec., S. Provs | Nigeria *(inherited from previous clause)* | [1936, 1940] |
| 5 | 1939 | admstve offr., staff gde | Nigeria *(inherited from previous clause)* | [1936, 1940] |

## Candidate stint `Kelly, E. J___Kenya___1927`

- Staff-list name: **Kelly, E. J** | colony: **Kenya** | listed 1927–1934 | editions [1927, 1929, 1930, 1931, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. J. Kelly | Clerk | Agricultural | — | — |
| 1929 | E. J. Kelly | Office Superintendent | Agricultural | — | — |
| 1930 | E. J. Kelly | Office Superintendent | Agricultural | — | — |
| 1931 | E. J. Kelly | Office Superintendent | Agricultural | — | — |
| 1932 | E. J. Kelly | Office Superintendent | Agricultural Department | — | — |
| 1934 | E. J. Kelly | Office Superintendent | Agricultural Department | — | — |

### Deterministic checks: `kelly_edward-james-gleeson_b1894` vs `Kelly, E. J___Kenya___1927`

- [PASS] surname_gate: bio 'KELLY' vs stint 'Kelly, E. J' (exact)
- [PASS] initials: bio ['E', 'J', 'G'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1927, birth 1894 (age 33)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1934
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

