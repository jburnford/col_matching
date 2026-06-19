<!-- {"case_id": "case_hayllor_harry-william_b1899", "bio_ids": ["hayllor_harry-william_b1899"], "stint_ids": ["Hayllor, H. W___Nigeria___1929"]} -->
# Dossier case_hayllor_harry-william_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hayllor_harry-william_b1899`

- Printed name: **HAYLLOR, Harry William**
- Birth year: 1899 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32779.v` — printed in editions [1949, 1950, 1951]:**

> HAYLLOR, Harry William.—b. 1899; ed. Gillespie Road Sch. and Tollington Park Central Sch.; police, Nig., 1928; prisons, 1935; supt., 1941; inspr., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | police | Nigeria | [1949, 1950, 1951] |
| 1 | 1935 | prisons | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1941 | supt | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951] |
| 3 | 1947 | inspr | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Hayllor, H. W___Nigeria___1929`

- Staff-list name: **Hayllor, H. W** | colony: **Nigeria** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | H. W. Hayllor | Superintendents (Motor Traffic Branch) | Marine | — | — |
| 1930 | H. W. Hayllor | Superintendents (Motor Traffic Branch) | Police | — | — |

### Deterministic checks: `hayllor_harry-william_b1899` vs `Hayllor, H. W___Nigeria___1929`

- [PASS] surname_gate: bio 'HAYLLOR' vs stint 'Hayllor, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1929, birth 1899 (age 30)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [FAIL] position_sim: best 14 vs bar 60: 'police' ~ 'Superintendents (Motor Traffic Branch)'
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

