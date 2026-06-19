<!-- {"case_id": "case_compton_m-c_b1911", "bio_ids": ["compton_m-c_b1911"], "stint_ids": ["Compton, M. C___Singapore___1949"]} -->
# Dossier case_compton_m-c_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `compton_m-c_b1911`

- Printed name: **COMPTON, M. C**
- Birth year: 1911 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L16948.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> COMPTON, M. C.—b. 1911; ed. King's Sch., Rochester; mil. serv., 1940-43; B.M.A., Mal., 1945; cadet, M.C.S., 1946; fin. sec's offr., S'pore, 1947; cl. IV, 1949; cl. III, ag. dep. fin. sec., 1951; immigr. serv., 1953; contrlr., immigr., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | B.M.A. | Malaya | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1946 | cadet, M.C.S | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1947 | fin. sec's offr., S'pore | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 3 | 1949 | cl. IV | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1951 | cl. III, ag. dep. fin. sec | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 5 | 1953 | immigr. serv | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 6 | 1954 | contrlr., immigr | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Compton, M. C___Singapore___1949`

- Staff-list name: **Compton, M. C** | colony: **Singapore** | listed 1949–1957 | editions [1949, 1951, 1953, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | M. C. Compton | Assistant Financial Secretaries (M.C.S. Class IV) | Secretariat | — | — |
| 1951 | M. C. Compton | Principal Assistant Financial Secretary | Administration | — | — |
| 1953 | M. C. Compton | Deputy Financial Secretary | Civil Establishment | — | — |
| 1955 | M. C. Compton | Controller of Immigration | Civil Establishment | — | — |
| 1956 | M. C. Compton | Controller of Immigration | Civil Establishment | — | — |
| 1957 | M. C. Compton | Controller of Immigration | Civil Establishment | — | — |

### Deterministic checks: `compton_m-c_b1911` vs `Compton, M. C___Singapore___1949`

- [PASS] surname_gate: bio 'COMPTON' vs stint 'Compton, M. C' (exact)
- [PASS] initials: bio ['M', 'C'] ~ stint ['M', 'C']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1957
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

