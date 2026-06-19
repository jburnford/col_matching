<!-- {"case_id": "case_dove-edwin_g-f_b1896", "bio_ids": ["dove-edwin_g-f_b1896"], "stint_ids": ["Dove-Edwin, G. F___Nigeria___1956"]} -->
# Dossier case_dove-edwin_g-f_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dove-edwin_g-f_b1896`

- Printed name: **DOVE-EDWIN, G. F**
- Birth year: 1896 (attested in editions [1953, 1954, 1955, 1957, 1958, 1959, 1960])
- Appears in editions: [1953, 1954, 1955, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1953-L17178.v` — printed in editions [1953, 1954, 1955, 1957, 1958, 1959, 1960]:**

> DOVE-EDWIN, G. F.—b. 1896; ed. C.M.S. Gram. Sch., Freetown, and Fourah Bay Coll., S.L.; barrister-at-law, Lincoln's Inn; mag., Nig., 1940; puisne judge, 1951; judge, E. regn., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | mag. | Nigeria | [1953, 1954, 1955, 1957, 1958, 1959, 1960] |
| 1 | 1951 | puisne judge | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1957, 1958, 1959, 1960] |
| 2 | 1955 | judge, E. regn | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1957, 1958, 1959, 1960] |

## Candidate stint `Dove-Edwin, G. F___Nigeria___1956`

- Staff-list name: **Dove-Edwin, G. F** | colony: **Nigeria** | listed 1956–1958 | editions [1956, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | G. F. Dove-Edwin | Judges | Civil Establishment, Eastern Region | — | — |
| 1958 | G. F. Dove-Edwin | Justices | Civil Establishment | — | — |

### Deterministic checks: `dove-edwin_g-f_b1896` vs `Dove-Edwin, G. F___Nigeria___1956`

- [PASS] surname_gate: bio 'DOVE-EDWIN' vs stint 'Dove-Edwin, G. F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1956, birth 1896 (age 60)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1956-1958
- [PASS] position_sim: best 67 vs bar 60: 'puisne judge' ~ 'Judges'
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

