<!-- {"case_id": "case_glenn_james-alexander_e1915", "bio_ids": ["glenn_james-alexander_e1915"], "stint_ids": ["Glenn, J___Mauritius___1921", "Glenn, Joseph___Canada___1914"]} -->
# Dossier case_glenn_james-alexander_e1915

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `glenn_james-alexander_e1915`

- Printed name: **GLENN, JAMES ALEXANDER**
- Birth year: not printed
- Appears in editions: [1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1931-L64742.v` — printed in editions [1931, 1932]:**

> GLENN, JAMES ALEXANDER, M.A.—Ed. Trinity Coll., Dublin; 2nd lieut., R.G.A., Dec., 1915; lieut., July, 1917; ag. capt., Nov., 1918; served in France and Palestine; demob., Jan., 1919; astt. dir. of edn., Iraq, Apr., 1920; ag. adviser, Min. of educom., Apr., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | 2nd lieut., R.G.A | — | [1931, 1932] |
| 1 | 1917 | lieut | — | [1931, 1932] |
| 2 | 1918 | ag. capt | — | [1931, 1932] |
| 3 | 1919 | demob | — | [1931, 1932] |
| 4 | 1920 | astt. dir. of edn. | Iraq | [1931, 1932] |
| 5 | 1922 | ag. adviser, Min. of educom | Iraq *(inherited from previous clause)* | [1931, 1932] |

## Candidate stint `Glenn, J___Mauritius___1921`

- Staff-list name: **Glenn, J** | colony: **Mauritius** | listed 1921–1932 | editions [1921, 1922, 1923, 1925, 1927, 1928, 1929, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. Glenn | Sub-Inspector | Police Department | — | — |
| 1922 | J. Glenn | Sub-Inspectors | Police Department | — | — |
| 1923 | J. Glenn | Sub-Inspectors | Police Department | — | — |
| 1925 | J. Glenn | Pay and Quarter Master | Police Department | — | — |
| 1927 | J. Glenn | Pay and Quarter Master | POLICE DEPARTMENT | — | — |
| 1928 | J. Glenn | Pay and Quarter Master | Police Department | — | — |
| 1929 | J. Glenn | Pay and Quarter Master | Police Department | — | — |
| 1931 | J. Glenn | Pay and Quarter Master | Police Department | — | — |
| 1932 | J. Glenn | Pay and Quarter Master | Police Department | — | — |

### Deterministic checks: `glenn_james-alexander_e1915` vs `Glenn, J___Mauritius___1921`

- [PASS] surname_gate: bio 'GLENN' vs stint 'Glenn, J' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Glenn, Joseph___Canada___1914`

- Staff-list name: **Glenn, Joseph** | colony: **Canada** | listed 1914–1917 | editions [1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | Joseph Glenn | Member | Legislative Assembly | — | — |
| 1915 | Joseph Glenn | Member | Legislative Assembly | — | — |
| 1917 | Joseph Glenn | Member for South Qu'Appelle | Legislative Assembly | — | — |

### Deterministic checks: `glenn_james-alexander_e1915` vs `Glenn, Joseph___Canada___1914`

- [PASS] surname_gate: bio 'GLENN' vs stint 'Glenn, Joseph' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1917
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

