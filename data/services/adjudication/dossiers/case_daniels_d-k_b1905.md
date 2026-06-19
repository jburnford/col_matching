<!-- {"case_id": "case_daniels_d-k_b1905", "bio_ids": ["daniels_d-k_b1905"], "stint_ids": ["Daniels, D. K___Singapore___1949"]} -->
# Dossier case_daniels_d-k_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `daniels_d-k_b1905`

- Printed name: **DANIELS, D. K**
- Birth year: 1905 (attested in editions [1953, 1954, 1955, 1956])
- Appears in editions: [1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1953-L17077.v` — printed in editions [1953, 1954, 1955, 1956]:**

> DANIELS, D. K., O.B.E. (mil.), 1945.—b. 1905; ed. Kent Coll., Canterbury and St. Edmund Hall, Oxford; mil. serv., 1940; admin. cadet, Tang., 1928; K.A.R.R.O., 1936; ch. staff offr., B.M.A., Somalia, 1941; S.C.A.O., res. areas, Ethiopia, 1943; ch. staff offr., B.M.A., Mal., 1945-46; cl. IB., M.C.S., 1948; cl. IA, under sec., S'pore, 1949; staff offr., gr. A, dep. ch. sec., Mal., 1952-56.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | admin. cadet | Tanganyika | [1953, 1954, 1955, 1956] |
| 1 | 1936 | K.A.R.R.O | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 2 | 1941 | ch. staff offr., B.M.A., Somalia | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 3 | 1943 | S.C.A.O., res. areas, Ethiopia | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 4 | 1945–1946 | ch. staff offr., B.M.A. | Malaya | [1953, 1954, 1955, 1956] |
| 5 | 1948 | cl. IB., M.C.S | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 6 | 1949 | cl. IA, under sec., S'pore | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 7 | 1952–1956 | staff offr., gr. A, dep. ch. sec. | Malaya | [1953, 1954, 1955, 1956] |

## Candidate stint `Daniels, D. K___Singapore___1949`

- Staff-list name: **Daniels, D. K** | colony: **Singapore** | listed 1949–1952 | editions [1949, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. K. Daniels | Under Secretary | Secretariat | O.B.E. | — |
| 1951 | D. K. Daniels | Under Secretary | Administration | — | — |
| 1952 | D. K. Daniels | Under Secretary | Civil Establishment | — | — |

### Deterministic checks: `daniels_d-k_b1905` vs `Daniels, D. K___Singapore___1949`

- [PASS] surname_gate: bio 'DANIELS' vs stint 'Daniels, D. K' (exact)
- [PASS] initials: bio ['D', 'K'] ~ stint ['D', 'K']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1952
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

