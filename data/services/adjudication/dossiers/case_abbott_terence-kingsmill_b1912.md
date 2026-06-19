<!-- {"case_id": "case_abbott_terence-kingsmill_b1912", "bio_ids": ["abbott_terence-kingsmill_b1912"], "stint_ids": ["Abbott, T. K___North Borneo___1953", "Abbott, T. K___Seychelles___1949"]} -->
# Dossier case_abbott_terence-kingsmill_b1912

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Abbott, T. K___North Borneo___1953` is also gate-compatible with biography(ies) outside this case: ['abbott_t-kings-mill_e1837', 'abbott_x_b1914'] (already linked elsewhere or filtered).
- NOTE: stint `Abbott, T. K___Seychelles___1949` is also gate-compatible with biography(ies) outside this case: ['abbott_t-kings-mill_e1837', 'abbott_x_b1914'] (already linked elsewhere or filtered).

## Biography `abbott_terence-kingsmill_b1912`

- Printed name: **ABBOTT, Terence Kingsmill**
- Birth year: 1912 (attested in editions [1953, 1954])
- Honours: M.B
- Appears in editions: [1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1953-L16277.v` — printed in editions [1953, 1954]:**

> ABBOTT, T. K.—b. 1912 ; ed. King’s Sch., Parramatta, Univ. Sydney and Sydney Hosp.; mil. serv., 1941-45, maj.; M.O.H., H.K., 1940 ; resig. and re-apptd. Borneo, 1945 ; ag. D.M. and H.S., Sarawak, 1945 ; M.O.H., Tang., 1947 ; S.M.O., Sey., 1948 ; D.D.M.S., N. Borneo, 1951.

**Version `col1950-L33071.v` — printed in editions [1950, 1951]:**

> ABBOTT, Terence Kingsmill, M.B., B.S. (Sydney), D.P.H. (Lond.).—b. 1912; ed. King's Sch., Parramatta, Univ. Sydney and Sydney Hosp.; on mil. serv. 1941-45, maj.; M.O.H., H.K., 1940; resig. and re-entered Borneo, 1945; ag. D.M. and H.S. Sarawak, 1945; M.O.H., Tang., 1947; S.M.O., Seychelles, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | M.O.H. | Hong Kong | [1950, 1951, 1953, 1954] |
| 1 | 1945 | resig. and re-apptd. Borneo | Hong Kong *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 2 | 1945 | ag. D.M. and H.S. | Sarawak | [1953, 1954] |
| 3 | 1947 | M.O.H. | Tanganyika | [1950, 1951, 1953, 1954] |
| 4 | 1948 | S.M.O. | Seychelles | [1950, 1951, 1953, 1954] |
| 5 | 1951 | D.D.M.S. | North Borneo | [1953, 1954] |

## Candidate stint `Abbott, T. K___North Borneo___1953`

- Staff-list name: **Abbott, T. K** | colony: **North Borneo** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | T. K. Abbott | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1954 | T. K. Abbott | Deputy Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `abbott_terence-kingsmill_b1912` vs `Abbott, T. K___North Borneo___1953`

- [PASS] surname_gate: bio 'ABBOTT' vs stint 'Abbott, T. K' (exact)
- [PASS] initials: bio ['T', 'K'] ~ stint ['T', 'K']
- [PASS] age_gate: stint starts 1953, birth 1912 (age 41)
- [PASS] colony: 1 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1954
- [FAIL] position_sim: best 21 vs bar 60: 'D.D.M.S.' ~ 'Deputy Director of Medical Services'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Abbott, T. K___Seychelles___1949`

- Staff-list name: **Abbott, T. K** | colony: **Seychelles** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. K. Abbott | Senior Medical Officer | Medical | — | — |
| 1950 | T. K. Abbott | Senior Medical Officer | MEDICAL | — | — |
| 1951 | T. K. Abbott | Senior Medical Officer | MEDICAL | — | — |

### Deterministic checks: `abbott_terence-kingsmill_b1912` vs `Abbott, T. K___Seychelles___1949`

- [PASS] surname_gate: bio 'ABBOTT' vs stint 'Abbott, T. K' (exact)
- [PASS] initials: bio ['T', 'K'] ~ stint ['T', 'K']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Seychelles'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 16 vs bar 60: 'S.M.O.' ~ 'Senior Medical Officer'
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

