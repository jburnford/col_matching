<!-- {"case_id": "case_yorston_j-h_b1916", "bio_ids": ["yorston_j-h_b1916"], "stint_ids": ["Yorston, J. H___Sierra Leone___1949"]} -->
# Dossier case_yorston_j-h_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `yorston_j-h_b1916`

- Printed name: **YORSTON, J. H**
- Birth year: 1916 (attested in editions [1956, 1957, 1958, 1959, 1960])
- Appears in editions: [1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1956-L25192.v` — printed in editions [1956, 1957, 1958, 1959, 1960]:**

> YORSTON, J. H.—b. 1916; ed. Eastham Gram. Sch. and L.N.E.Rly.; mil. serv., 1940–44; asst. traffic supt., S. Leone. rlyw., 1944; traffic supt., 1950; senr. traffic supt., G.C. rlyw., 1951; operating supt., 1952; traffic man., 1955–59 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | asst. traffic supt., S. Leone. rlyw | — | [1956, 1957, 1958, 1959, 1960] |
| 1 | 1950 | traffic supt | — | [1956, 1957, 1958, 1959, 1960] |
| 2 | 1951 | senr. traffic supt., G.C. rlyw | Gold Coast | [1956, 1957, 1958, 1959, 1960] |
| 3 | 1952 | operating supt | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |
| 4 | 1955–1959 | traffic man | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Yorston, J. H___Sierra Leone___1949`

- Staff-list name: **Yorston, J. H** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. H. Yorston | Assistant Traffic Superintendents | Railway | — | Captain |
| 1950 | J. H. Yorston | Assistant Traffic Superintendents | Traffic | — | Captain |
| 1951 | J. H. Yorston | Traffic Superintendent | Traffic | — | Captain |

### Deterministic checks: `yorston_j-h_b1916` vs `Yorston, J. H___Sierra Leone___1949`

- [PASS] surname_gate: bio 'YORSTON' vs stint 'Yorston, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

