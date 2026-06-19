<!-- {"case_id": "case_hodder_w-h_b1906", "bio_ids": ["hodder_w-h_b1906"], "stint_ids": ["Hodder, W. H___Uganda___1956"]} -->
# Dossier case_hodder_w-h_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hodder_w-h_b1906`

- Printed name: **HODDER, W. H**
- Birth year: 1906 (attested in editions [1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1960-L24173.v` — printed in editions [1960, 1961]:**

> HODDER, W. H.—b. 1906; ed. Judd Sch., Tonbridge; mil. serv., 1939-45, major; asst. dir., supplies, Uga., 1945; dir., trade, 1955; under sec., min. of commerce and ind., 1958-60.

**Version `col1958-L23664.v` — printed in editions [1958, 1959]:**

> HODDER, W. H.—b. 1906; ed. Judd Sch., Tonbridge; mil. serv., 1939-45, major; asst. dir., supplies, Uga., 1945; dir., trade, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | asst. dir., supplies | Uganda | [1958, 1959, 1960, 1961] |
| 1 | 1955 | dir., trade | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 2 | 1958–1960 | under sec., min. of commerce and ind | Uganda *(inherited from previous clause)* | [1960, 1961] |

## Candidate stint `Hodder, W. H___Uganda___1956`

- Staff-list name: **Hodder, W. H** | colony: **Uganda** | listed 1956–1959 | editions [1956, 1957, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | W. H. Hodder | Director of Trade | Civil Establishment | — | — |
| 1957 | W. H. Hodder | Director of Trade | Civil Establishment | — | — |
| 1959 | W. H. Hodder | Director of Trade | Civil Establishment | — | — |

### Deterministic checks: `hodder_w-h_b1906` vs `Hodder, W. H___Uganda___1956`

- [PASS] surname_gate: bio 'HODDER' vs stint 'Hodder, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1956, birth 1906 (age 50)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1956-1959
- [PASS] position_sim: best 71 vs bar 60: 'dir., trade' ~ 'Director of Trade'
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

