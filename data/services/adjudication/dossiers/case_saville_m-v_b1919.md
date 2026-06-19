<!-- {"case_id": "case_saville_m-v_b1919", "bio_ids": ["saville_m-v_b1919"], "stint_ids": ["Saville, M. V___North Borneo___1950", "Saville, M. V___North Borneo___1960"]} -->
# Dossier case_saville_m-v_b1919

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `saville_m-v_b1919`

- Printed name: **SAVILLE, M. V**
- Birth year: 1919 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1965)
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1960-L27756.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965]:**

> SAVILLE, M. V., O.B.E. (1965).—b. 1919; ed. King Edward VII Sch., Sheffield, Sheffield Univ. and St. Catharine's Coll., Camb.; mil. serv., 1940–45, lieut.(A) R.N.V.R.; lect., modern studies, R.M.A., Sandhurst, 1947–49; admin. offr., N. Borneo, 1949; asst. sec. dist. offr.; dep. fin. sec., cl. IB., 1959–64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947–1949 | lect., modern studies, R.M.A., Sandhurst | — | [1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | admin. offr. | North Borneo | [1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1959–1964 | dep. fin. sec., cl. IB | North Borneo *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Saville, M. V___North Borneo___1950`

- Staff-list name: **Saville, M. V** | colony: **North Borneo** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | M. V. Saville | Assistant Secretaries (seconded from District Administration) (m) | Secretariat | — | — |
| 1950 | M. V. Saville | Cadet | District Administration | — | — |
| 1951 | M. V. Saville | Cadet | District Administration | — | — |
| 1951 | M. V. Saville | Assistant Secretaries (seconded from District Administration) (m) | Secretariat | — | — |

### Deterministic checks: `saville_m-v_b1919` vs `Saville, M. V___North Borneo___1950`

- [PASS] surname_gate: bio 'SAVILLE' vs stint 'Saville, M. V' (exact)
- [PASS] initials: bio ['M', 'V'] ~ stint ['M', 'V']
- [PASS] age_gate: stint starts 1950, birth 1919 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 27 vs bar 60: 'admin. offr.' ~ 'Cadet'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Saville, M. V___North Borneo___1960`

- Staff-list name: **Saville, M. V** | colony: **North Borneo** | listed 1960–1963 | editions [1960, 1961, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | M. V. Saville | Administrative Officer (Class IB) | Civil Establishment | — | — |
| 1961 | M. V. Saville | Administrative Officer (Class IB) | Civil Establishment | — | — |
| 1962 | M. V. Saville | Administrative Officer (Class IB) | Civil Establishment | — | — |
| 1963 | M. V. Saville | Administrative Officer (Class IB) | Civil Establishment | — | — |

### Deterministic checks: `saville_m-v_b1919` vs `Saville, M. V___North Borneo___1960`

- [PASS] surname_gate: bio 'SAVILLE' vs stint 'Saville, M. V' (exact)
- [PASS] initials: bio ['M', 'V'] ~ stint ['M', 'V']
- [PASS] age_gate: stint starts 1960, birth 1919 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1960-1963
- [FAIL] position_sim: best 49 vs bar 60: 'admin. offr.' ~ 'Administrative Officer (Class IB)'
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

