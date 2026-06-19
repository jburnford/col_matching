<!-- {"case_id": "case_stokes_thomas-george_b1894", "bio_ids": ["stokes_thomas-george_b1894"], "stint_ids": ["Stokes, T. G___Hong Kong___1929", "Stokes, T. G___Hong Kong___1949"]} -->
# Dossier case_stokes_thomas-george_b1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stokes_thomas-george_b1894`

- Printed name: **STOKES, Thomas George**
- Birth year: 1894 (attested in editions [1950])
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L39871.v` — printed in editions [1950]:**

> STOKES, Thomas George.—b. 1894; ed. Fort St. High Sch. and Tech. Coll., Sydney, 1st cl. B.O.T. cert. of comp.; on naval serv., 1915-18, engnr. offr.; on mil. serv., 1945-46, maj.; cl. II offr., senr. cler. and acctg. staff, H.K., 1928; cl. I, 1941; senr. exec. offr., cl. II, 1947; cl. I, 1949; fin. liaison offr., Australia, 1942-44; mem., Br. min. of war trans. passengers priority comtce., Australia, 1943-44; staff offr., gr. II, B.M.A., H.K.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | engnr. offr. | — | [1950] |
| 1 | 1928 | cl. II offr., senr. cler. and acctg. staff | Hong Kong | [1950] |
| 2 | 1941 | cl. I | — | [1950] |
| 3 | 1942–1944 | fin. liaison offr. | Australia | [1950] |
| 4 | 1943–1944 | mem., Br. min. of war trans. passengers priority comtce. | Australia | [1950] |
| 5 | 1945–1946 | maj. | — | [1950] |
| 6 | 1947 | senr. exec. offr., cl. II | — | [1950] |
| 7 | 1949 | cl. I | — | [1950] |

## Candidate stint `Stokes, T. G___Hong Kong___1929`

- Staff-list name: **Stokes, T. G** | colony: **Hong Kong** | listed 1929–1937 | editions [1929, 1930, 1931, 1933, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | T. G. Stokes | Senior Clerks | Audit Department (under the Director of Colonial Audit, London) | — | — |
| 1930 | T. G. Stokes | Examiner | Audit Department (under the Director of Colonial Audit, London) | — | — |
| 1931 | T. G. Stokes | Examiner | Audit Department | — | — |
| 1933 | T. G. Stokes | Acting Chief Accountant | Kowloon-Canton Railway | — | — |
| 1936 | T. G. Stokes | Accountant | Police Department | — | — |
| 1937 | T. G. Stokes | Accountant | Police Department | — | — |

### Deterministic checks: `stokes_thomas-george_b1894` vs `Stokes, T. G___Hong Kong___1929`

- [PASS] surname_gate: bio 'STOKES' vs stint 'Stokes, T. G' (exact)
- [PASS] initials: bio ['T', 'G'] ~ stint ['T', 'G']
- [PASS] age_gate: stint starts 1929, birth 1894 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1937
- [FAIL] position_sim: best 44 vs bar 60: 'cl. II offr., senr. cler. and acctg. staff' ~ 'Acting Chief Accountant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Stokes, T. G___Hong Kong___1949`

- Staff-list name: **Stokes, T. G** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. G. Stokes | Chief Accountant | Posts and Telegraphs | — | — |
| 1950 | T. G. Stokes | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `stokes_thomas-george_b1894` vs `Stokes, T. G___Hong Kong___1949`

- [PASS] surname_gate: bio 'STOKES' vs stint 'Stokes, T. G' (exact)
- [PASS] initials: bio ['T', 'G'] ~ stint ['T', 'G']
- [PASS] age_gate: stint starts 1949, birth 1894 (age 55)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

