<!-- {"case_id": "case_pirie_james-henry_b1893", "bio_ids": ["pirie_james-henry_b1893"], "stint_ids": ["Pirie, J. H. H___Kenya___1915", "Pirie, J___Gambia___1925"]} -->
# Dossier case_pirie_james-henry_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Pirie, J. H. H___Kenya___1915` is also gate-compatible with biography(ies) outside this case: ['pirie_j-h-h_e1913'] (already linked elsewhere or filtered).
- NOTE: stint `Pirie, J___Gambia___1925` is also gate-compatible with biography(ies) outside this case: ['pirie_george-jamieson_b1876', 'pirie_j-h-h_e1913'] (already linked elsewhere or filtered).

## Biography `pirie_james-henry_b1893`

- Printed name: **PIRIE, JAMES HENRY**
- Birth year: 1893 (attested in editions [1939])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69828.v` — printed in editions [1939]:**

> PIRIE, JAMES HENRY.—B. 1893; ed. St. Paul's Sch., Darjeeling, India; asst. storekeeper, Nigerian Eastern Rly. constr., 1931; storekeeper, Nigerian rly. open lines, 1931-37; stores aspt., do., 1937.

**Version `col1940-L67612.v` — printed in editions [1940]:**

> PIERIE, JAMES HENRY.—B. 1893; ed. St Paul's Schl., Darjeeling, India; asst. storekeeper, Nigerian Eastern Rly. constrn., 1931; storekeeper, Nigerian rly. open lines, 1931-37; stores supt., do., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | asst. storekeeper, Nigerian Eastern Rly. constr | — | [1939, 1940] |
| 1 | 1937 | stores aspt. | Dominions Office | [1939, 1940] |

## Candidate stint `Pirie, J. H. H___Kenya___1915`

- Staff-list name: **Pirie, J. H. H** | colony: **Kenya** | listed 1915–1917 | editions [1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | J. H. H. Pirie | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1917 | J. H. H. Pirie | Pathologist and Assistant Bacteriologist | Laboratories | — | — |

### Deterministic checks: `pirie_james-henry_b1893` vs `Pirie, J. H. H___Kenya___1915`

- [PASS] surname_gate: bio 'PIRIE' vs stint 'Pirie, J. H. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H', 'H']
- [PASS] age_gate: stint starts 1915, birth 1893 (age 22)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1917
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Pirie, J___Gambia___1925`

- Staff-list name: **Pirie, J** | colony: **Gambia** | listed 1925–1937 | editions [1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1927 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1928 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1929 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1930 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1931 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1932 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1933 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1934 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1936 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |
| 1937 | J. Pirie | Agricultural Superintendent | Agricultural Department | — | — |

### Deterministic checks: `pirie_james-henry_b1893` vs `Pirie, J___Gambia___1925`

- [PASS] surname_gate: bio 'PIRIE' vs stint 'Pirie, J' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J']
- [PASS] age_gate: stint starts 1925, birth 1893 (age 32)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1937
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

