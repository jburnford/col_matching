<!-- {"case_id": "case_billyeald_stanhope_b1894", "bio_ids": ["billyeald_stanhope_b1894"], "stint_ids": ["Billyeald, S___British Guiana___1925", "Billyeald, S___British Guiana___1949"]} -->
# Dossier case_billyeald_stanhope_b1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['billyeald_stanhope_b1894'] carry a single initial only — the namesake trap applies.

## Biography `billyeald_stanhope_b1894`

- Printed name: **BILLYEALD, Stanhope**
- Birth year: 1894 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31194.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BILLYEALD, Stanhope.—b. 1894; on mil. serv. 1914-18, sergt.; sgt. roughrider, police, Br. Guiana, 1919; warrant offr., 1924; dist. inspr., 1927; county supt., 1937; major, Br. Guiana militia, 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | sgt. roughrider, police | British Guiana | [1948, 1949, 1950, 1951] |
| 1 | 1924 | warrant offr | British Guiana *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1927 | dist. inspr | British Guiana *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1937 | county supt | British Guiana *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1943 | major, Br. Guiana militia | British Guiana | [1948, 1949, 1950, 1951] |

## Candidate stint `Billyeald, S___British Guiana___1925`

- Staff-list name: **Billyeald, S** | colony: **British Guiana** | listed 1925–1928 | editions [1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | S. Billyeald | Riding Master | Warrant Officers | — | — |
| 1927 | S. Billyeald | Riding Master | Police | — | — |
| 1928 | S. Billyeald | Riding Master | Police | — | — |

### Deterministic checks: `billyeald_stanhope_b1894` vs `Billyeald, S___British Guiana___1925`

- [PASS] surname_gate: bio 'BILLYEALD' vs stint 'Billyeald, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1925, birth 1894 (age 31)
- [PASS] colony: 5 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1925-1928
- [FAIL] position_sim: best 43 vs bar 60: 'dist. inspr' ~ 'Riding Master'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Billyeald, S___British Guiana___1949`

- Staff-list name: **Billyeald, S** | colony: **British Guiana** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. Billyeald | Superintendent of Police | Police | — | — |
| 1950 | S. Billyeald | Superintendent of Police | Police | — | — |

### Deterministic checks: `billyeald_stanhope_b1894` vs `Billyeald, S___British Guiana___1949`

- [PASS] surname_gate: bio 'BILLYEALD' vs stint 'Billyeald, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1949, birth 1894 (age 55)
- [PASS] colony: 5 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 26 vs bar 60: 'major, Br. Guiana militia' ~ 'Superintendent of Police'
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

