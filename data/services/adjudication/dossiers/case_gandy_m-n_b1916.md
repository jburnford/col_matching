<!-- {"case_id": "case_gandy_m-n_b1916", "bio_ids": ["gandy_m-n_b1916"], "stint_ids": ["Gandy, M. N___Nyasaland___1949"]} -->
# Dossier case_gandy_m-n_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gandy_m-n_b1916`

- Printed name: **GANDY, M. N**
- Birth year: 1916 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L22743.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> GANDY, M. N.—b. 1916; ed. St. Bees Sch. and Manchester Univ.; solicitor; mil. serv., 1939-46; cadet, Nyasa., 1946; admin. offr., 1948; soc. dev. offr., 1960; res. mag., 1963. (Malawi Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Nyasaland | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1948 | admin. offr | Nyasaland *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1960 | soc. dev. offr | Nyasaland *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1963 | res. mag | Nyasaland *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Gandy, M. N___Nyasaland___1949`

- Staff-list name: **Gandy, M. N** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | M. N. Gandy | Administrative Officer | Provincial and District Administration | — | — |
| 1951 | M. N. Gandy | Assistant Secretary (seconded from District Administration) | Secretariat | — | — |

### Deterministic checks: `gandy_m-n_b1916` vs `Gandy, M. N___Nyasaland___1949`

- [PASS] surname_gate: bio 'GANDY' vs stint 'Gandy, M. N' (exact)
- [PASS] initials: bio ['M', 'N'] ~ stint ['M', 'N']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 62 vs bar 60: 'admin. offr' ~ 'Administrative Officer'
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

