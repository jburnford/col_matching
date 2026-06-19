<!-- {"case_id": "case_tohill_john-douglas_b1885", "bio_ids": ["tohill_john-douglas_b1885"], "stint_ids": ["Tothill, J. D___Fiji___1927", "Tothill, J. D___Uganda___1930"]} -->
# Dossier case_tohill_john-douglas_b1885

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Tothill, J. D___Fiji___1927` is also gate-compatible with biography(ies) outside this case: ['toghill_john-douglas_b1888'] (already linked elsewhere or filtered).
- NOTE: stint `Tothill, J. D___Uganda___1930` is also gate-compatible with biography(ies) outside this case: ['toghill_john-douglas_b1888'] (already linked elsewhere or filtered).

## Biography `tohill_john-douglas_b1885`

- Printed name: **TOHILL, John Douglas**
- Birth year: 1885 (attested in editions [1934])
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L63600.v` — printed in editions [1934]:**

> TOHILL, John Douglas.—B. 1885; ed. Blundell's Schl.; Ontario Agr. Coll. (Toronto Univ.); B.Sc., Agr., 1910; Cornell Univ., U.S.A.; Graduate Schl., 1913, 1914; Harvard Univ., D.Sc., 1922; agt. and expert, U.S. Bureau of Entomology, 1910-11; entomologist, entomological branch, Ottawa, 1911-24; seconded as dir., Levuana campaign, Fiji, for two years Nov., 1924; ag. dir., agr., Fiji, May, 1925; dir., Levuana campaign and agr., 1926; dir. agr., Uganda, June, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910–1911 | agt. and expert | — | [1934] |
| 1 | 1911–1924 | entomologist | — | [1934] |
| 2 | 1924 | seconded as dir., Levuana campaign | Fiji | [1934] |
| 3 | 1925 | ag. dir., agr. | Fiji | [1934] |
| 4 | 1926 | dir., Levuana campaign and agr. | — | [1934] |
| 5 | 1929 | dir. agr. | Uganda | [1934] |

## Candidate stint `Tothill, J. D___Fiji___1927`

- Staff-list name: **Tothill, J. D** | colony: **Fiji** | listed 1927–1929 | editions [1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. D. Tothill | Superintendent of Agriculture, Director of Entomology | Department of Agriculture | — | — |
| 1928 | J. D. Tothill | Superintendent of Agriculture; Director of Entomology | Department of Agriculture | — | — |
| 1929 | J. D. Tothill | Superintendent of Agriculture | Department of Agriculture | — | — |

### Deterministic checks: `tohill_john-douglas_b1885` vs `Tothill, J. D___Fiji___1927`

- [PASS] surname_gate: bio 'TOHILL' vs stint 'Tothill, J. D' (fuzzy:1)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1927, birth 1885 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [FAIL] position_sim: best 26 vs bar 60: 'ag. dir., agr.' ~ 'Superintendent of Agriculture'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Tothill, J. D___Uganda___1930`

- Staff-list name: **Tothill, J. D** | colony: **Uganda** | listed 1930–1937 | editions [1930, 1933, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | J. D. Tothill | Director of Agriculture | Agricultural Department | — | — |
| 1933 | J. D. Tothill | Director of Agriculture | Agricultural Department | — | — |
| 1936 | J. D. Tothill | Director of Agriculture | Agricultural Department | — | — |
| 1937 | J. D. Tothill | Director of Agriculture | Agricultural Department | — | — |

### Deterministic checks: `tohill_john-douglas_b1885` vs `Tothill, J. D___Uganda___1930`

- [PASS] surname_gate: bio 'TOHILL' vs stint 'Tothill, J. D' (fuzzy:1)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1930, birth 1885 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1937
- [FAIL] position_sim: best 47 vs bar 60: 'dir. agr.' ~ 'Director of Agriculture'
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

