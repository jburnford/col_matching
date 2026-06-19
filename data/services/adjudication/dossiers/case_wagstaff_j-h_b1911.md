<!-- {"case_id": "case_wagstaff_j-h_b1911", "bio_ids": ["wagstaff_j-h_b1911"], "stint_ids": ["Wagstaff, J. H___Singapore___1957"]} -->
# Dossier case_wagstaff_j-h_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wagstaff_j-h_b1911`

- Printed name: **WAGSTAFF, J. H**
- Birth year: 1911 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L28075.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> WAGSTAFF, J. H.—b. 1911; ed. Bishop's Stortford Coll., and Univ. Coll., London; mil. serv., 1941-46; inspr., machy., mines dept., F.M.S., 1936; engnr., posts and tels., 1936; asst. contrlr., telecoms., 1940; contrlr. (stores) 1950; contrlr., gr. I, 1953; dir., telecoms., S'pore, 1957-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | inspr., machy., mines dept. | Federated Malay States | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1940 | asst. contrlr., telecoms | Federated Malay States *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1950 | contrlr. (stores) | Federated Malay States *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1953 | contrlr., gr. I | Federated Malay States *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1957–1962 | dir., telecoms., S'pore | Federated Malay States *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Wagstaff, J. H___Singapore___1957`

- Staff-list name: **Wagstaff, J. H** | colony: **Singapore** | listed 1957–1960 | editions [1957, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | J. H. Wagstaff | Director of Telecommunications | Civil Establishment | — | — |
| 1959 | J. H. Wagstaff | Director of Telecommunications | Civil Establishment | — | — |
| 1960 | J. H. Wagstaff | Director of Telecommunications | Ministry of National Development | — | — |

### Deterministic checks: `wagstaff_j-h_b1911` vs `Wagstaff, J. H___Singapore___1957`

- [PASS] surname_gate: bio 'WAGSTAFF' vs stint 'Wagstaff, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1957, birth 1911 (age 46)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1960
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

