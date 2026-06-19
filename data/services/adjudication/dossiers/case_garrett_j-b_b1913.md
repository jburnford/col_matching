<!-- {"case_id": "case_garrett_j-b_b1913", "bio_ids": ["garrett_j-b_b1913"], "stint_ids": ["Garrett, J. B___Sierra Leone___1949"]} -->
# Dossier case_garrett_j-b_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `garrett_j-b_b1913`

- Printed name: **GARRETT, J. B**
- Birth year: 1913 (attested in editions [1956, 1957, 1958, 1959, 1960])
- Appears in editions: [1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1956-L21307.v` — printed in editions [1956, 1957, 1958, 1959, 1960]:**

> GARRETT, J. B.—b. 1913; ed. Northampton Poly. Inst.; U.K. serv., 1934–40; telephone engrn., posts and tels., S.L., 1940; engrn., 1946; engrn.-in-chief, 1954–59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934–1940 | U.K. serv | — | [1956, 1957, 1958, 1959, 1960] |
| 1 | 1940 | telephone engrn., posts and tels. | Sierra Leone | [1956, 1957, 1958, 1959, 1960] |
| 2 | 1946 | engrn | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |
| 3 | 1954–1959 | engrn.-in-chief | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Garrett, J. B___Sierra Leone___1949`

- Staff-list name: **Garrett, J. B** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. B. Garrett | Engineer | Engineering | — | — |
| 1950 | J. B. Garrett | Engineer | Engineering | — | — |
| 1951 | J. B. Garrett | Engineers | Engineering | — | — |

### Deterministic checks: `garrett_j-b_b1913` vs `Garrett, J. B___Sierra Leone___1949`

- [PASS] surname_gate: bio 'GARRETT' vs stint 'Garrett, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 62 vs bar 60: 'engrn' ~ 'Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

