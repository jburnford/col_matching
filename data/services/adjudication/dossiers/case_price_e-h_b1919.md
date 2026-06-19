<!-- {"case_id": "case_price_e-h_b1919", "bio_ids": ["price_e-h_b1919"], "stint_ids": ["Price, E. H___Singapore___1949"]} -->
# Dossier case_price_e-h_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 27 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `price_e-h_b1919`

- Printed name: **PRICE, E. H**
- Birth year: 1919 (attested in editions [1958, 1959, 1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1958-L26124.v` — printed in editions [1958, 1959, 1960, 1961]:**

> PRICE, E. H.—b. 1919; ed. Acton Park Sch. and Grove Pk. Sch., Wrexham, and Jesus Coll., Oxford; mil. serv., 1939-46; European master, Mal., 1947; group supvr., S'pore, 1948; vice-prin., teacher train. coll., 1953; offr. i/c, normal training, 1956; hd., secondary and upper primary dept., 1957-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | European master | Malaya | [1958, 1959, 1960, 1961] |
| 1 | 1948 | group supvr., S'pore | Malaya *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 2 | 1953 | vice-prin., teacher train. coll | Malaya *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 3 | 1956 | offr. i/c, normal training | Malaya *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 4 | 1957–1960 | hd., secondary and upper primary dept | Malaya *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |

## Candidate stint `Price, E. H___Singapore___1949`

- Staff-list name: **Price, E. H** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. H. Price | Education Officer (Men) | Education | — | — |
| 1951 | E. H. Price | Group Supervisor | Education | — | — |

### Deterministic checks: `price_e-h_b1919` vs `Price, E. H___Singapore___1949`

- [PASS] surname_gate: bio 'PRICE' vs stint 'Price, E. H' (exact)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [FAIL] colony: no placed event resolves to 'Singapore'
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

