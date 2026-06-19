<!-- {"case_id": "case_lancaster_duncan-gordon_b1893", "bio_ids": ["lancaster_duncan-gordon_b1893"], "stint_ids": ["Lancaster, D. G___Northern Rhodesia___1928"]} -->
# Dossier case_lancaster_duncan-gordon_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lancaster_duncan-gordon_b1893`

- Printed name: **LANCASTER, Duncan Gordon**
- Birth year: 1893 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33909.v` — printed in editions [1948, 1950, 1951]:**

> LANCASTER, Duncan Gordon.—b. 1893 ; ed. Heston House Sch. and Shoreham Gram. Sch. ; on mil. serv. 1914-18 ; trpr., B.S.A. police, S. Rhod., 1911 ; police, N. Rhod., 1914 ; resig. 1922 ; re-engaged, police, N. Rhod., 1924 ; elephant control offr., 1936 ; game ranger, 1940 ; asst. game warden, 1941 ; author of Tentative Chronology of the Aba-Ngoni Genealogy of their Chiefs and Notes.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | trpr., B.S.A. police | Southern Rhodesia | [1948, 1950, 1951] |
| 1 | 1914 | police | Northern Rhodesia | [1948, 1950, 1951] |
| 2 | 1922 | resig | Northern Rhodesia *(inherited from previous clause)* | [1948, 1950, 1951] |
| 3 | 1924 | re-engaged, police | Northern Rhodesia | [1948, 1950, 1951] |
| 4 | 1936 | elephant control offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1950, 1951] |
| 5 | 1940 | game ranger | Northern Rhodesia *(inherited from previous clause)* | [1948, 1950, 1951] |
| 6 | 1941 | asst. game warden | Northern Rhodesia *(inherited from previous clause)* | [1948, 1950, 1951] |

## Candidate stint `Lancaster, D. G___Northern Rhodesia___1928`

- Staff-list name: **Lancaster, D. G** | colony: **Northern Rhodesia** | listed 1928–1931 | editions [1928, 1929, 1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | D. G. Lancaster | Sergeants, 3rd Class | Town and District Police Branch | — | — |
| 1929 | D. G. Lancaster | Assistant Inspectors | Town and District Police Branch | — | — |
| 1930 | D. G. Lancaster | Assistant Inspector | Civil Police Branch | — | — |
| 1931 | D. G. Lancaster | Assistant Inspector | Civil Police Branch | — | — |

### Deterministic checks: `lancaster_duncan-gordon_b1893` vs `Lancaster, D. G___Northern Rhodesia___1928`

- [PASS] surname_gate: bio 'LANCASTER' vs stint 'Lancaster, D. G' (exact)
- [PASS] initials: bio ['D', 'G'] ~ stint ['D', 'G']
- [PASS] age_gate: stint starts 1928, birth 1893 (age 35)
- [PASS] colony: 6 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1928-1931
- [FAIL] position_sim: best 29 vs bar 60: 're-engaged, police' ~ 'Sergeants, 3rd Class'
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

