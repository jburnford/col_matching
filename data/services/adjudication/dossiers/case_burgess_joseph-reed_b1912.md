<!-- {"case_id": "case_burgess_joseph-reed_b1912", "bio_ids": ["burgess_joseph-reed_b1912"], "stint_ids": ["Burgess, J. R___Fiji___1965"]} -->
# Dossier case_burgess_joseph-reed_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Burgess, J. R___Fiji___1965` is also gate-compatible with biography(ies) outside this case: ['burgess_j_b1918'] (already linked elsewhere or filtered).

## Biography `burgess_joseph-reed_b1912`

- Printed name: **BURGESS, Joseph Reed**
- Birth year: 1912 (attested in editions [1949, 1950, 1951])
- Honours: A.L.A.A
- Appears in editions: [1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1949-L30820.v` — printed in editions [1949, 1950, 1951]:**

> BURGESS, Joseph Reed, A.L.A.A.—b. 1912; ed. Nairobi Gov. Sch. and Nelson Sch., Wigton, Cumb.; on mil. serv., 1939–40; clk., col. aud., Ken., 1928; assessor, jt. inc. tax dep., 1940; asst. comsnr., inc. tax, 1946.

**Version `col1956-L20112.v` — printed in editions [1956, 1957, 1958, 1959, 1960]:**

> BURGESS, J. R.—b. 1912; ed. Nelson Sch.; C.A.D., 1928-39; assessor, E.A. inc. tax dept., 1940; regl. comsrr., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | clk., col. aud. | Kenya | [1949, 1950, 1951] |
| 1 | 1928–1939 | C.A.D | — | [1956, 1957, 1958, 1959, 1960] |
| 2 | 1940 | assessor, jt. inc. tax dep | Kenya *(inherited from previous clause)* | [1949, 1950, 1951, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1946 | asst. comsnr., inc. tax | Kenya *(inherited from previous clause)* | [1949, 1950, 1951] |
| 4 | 1950 | regl. comsrr | — | [1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Burgess, J. R___Fiji___1965`

- Staff-list name: **Burgess, J. R** | colony: **Fiji** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | J. R. Burgess | Deputy Comptroller | Civil Establishment | — | — |
| 1966 | J. R. Burgess | Deputy Comptroller | Civil Establishment | — | — |

### Deterministic checks: `burgess_joseph-reed_b1912` vs `Burgess, J. R___Fiji___1965`

- [PASS] surname_gate: bio 'BURGESS' vs stint 'Burgess, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1965, birth 1912 (age 53)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

