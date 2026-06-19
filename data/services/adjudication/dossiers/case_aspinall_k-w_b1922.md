<!-- {"case_id": "case_aspinall_k-w_b1922", "bio_ids": ["aspinall_k-w_b1922"], "stint_ids": ["Aspinall, K. W___Nyasaland___1955"]} -->
# Dossier case_aspinall_k-w_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `aspinall_k-w_b1922`

- Printed name: **ASPINALL, K. W**
- Birth year: 1922 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1956-L19528.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> ASPINALL, K. W.—b. 1922; ed. Preston Gram. Sch. and Royal Vet. Coll., London; vet. offr., Tang., 1944; D.D.V.S., Nyasa., 1954; D.V.S., 1960-64. (Malawi Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | vet. offr. | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1954 | D.D.V.S. | Nyasaland | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1960–1964 | D.V.S | Nyasaland *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Aspinall, K. W___Nyasaland___1955`

- Staff-list name: **Aspinall, K. W** | colony: **Nyasaland** | listed 1955–1964 | editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | K. W. Aspinall | Deputy Director | Civil Establishment | — | — |
| 1956 | K. W. Aspinall | Deputy Director | Civil Establishment | — | — |
| 1957 | K. W. Aspinall | Deputy Director | Civil Establishment | — | — |
| 1958 | K. W. Aspinall | Deputy Director | Civil Establishment | — | — |
| 1959 | K. W. Aspinall | Deputy Director | Civil Establishment | — | — |
| 1960 | K. W. Aspinall | Deputy Director | Civil Establishment | — | — |
| 1961 | K. W. Aspinall | Director of Veterinary Services | Civil Establishment | — | — |
| 1962 | K. W. Aspinall | Director of Veterinary Services | Ministry of Natural Resources and Local Government | — | — |
| 1963 | K. W. Aspinall | Director of Veterinary Services | Ministry of Natural Resources | — | — |
| 1964 | K. W. Aspinall | Director of Veterinary Services | Ministry of Natural Resources | — | — |

### Deterministic checks: `aspinall_k-w_b1922` vs `Aspinall, K. W___Nyasaland___1955`

- [PASS] surname_gate: bio 'ASPINALL' vs stint 'Aspinall, K. W' (exact)
- [PASS] initials: bio ['K', 'W'] ~ stint ['K', 'W']
- [PASS] age_gate: stint starts 1955, birth 1922 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1955-1964
- [FAIL] position_sim: best 21 vs bar 60: 'D.D.V.S.' ~ 'Deputy Director'
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

