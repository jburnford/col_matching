<!-- {"case_id": "case_rose_w-v_b1919", "bio_ids": ["rose_w-v_b1919"], "stint_ids": ["Rose, W. V___Barbados___1953"]} -->
# Dossier case_rose_w-v_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 50 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rose_w-v_b1919`

- Printed name: **ROSE, W. V**
- Birth year: 1919 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1965)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L23888.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> ROSE, W. V., O.B.E. (1965).—b. 1919; ed. Munro Coll., J'ca, Pembroke Coll., Camb. and I.C.T.A.; agric. offr., Nyasa., 1943; dep. dir., agric., Barb., 1953; asst. dir., agric., W. Nig., 1956; ch. agric. extension serv. offr., 1959; ch. res. offr. (agric.), Uga., 1961; comsnr., agric., 1962–65. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | agric. offr. | Nyasaland | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | dep. dir., agric. | Barbados | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | asst. dir., agric. | Western Nigeria | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1959 | ch. agric. extension serv. offr | Western Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | ch. res. offr. (agric.) | Uganda | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1962–1965 | comsnr., agric | Uganda *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Rose, W. V___Barbados___1953`

- Staff-list name: **Rose, W. V** | colony: **Barbados** | listed 1953–1956 | editions [1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | W. V. Rose | Deputy Director | Civil Establishment | — | — |
| 1954 | W. V. Rose | Deputy Director | Civil Establishment | — | — |
| 1955 | W. V. Rose | Deputy Director | Civil Establishment | — | — |
| 1956 | W. V. Rose | Deputy Director | Civil Establishment | — | — |

### Deterministic checks: `rose_w-v_b1919` vs `Rose, W. V___Barbados___1953`

- [PASS] surname_gate: bio 'ROSE' vs stint 'Rose, W. V' (exact)
- [PASS] initials: bio ['W', 'V'] ~ stint ['W', 'V']
- [PASS] age_gate: stint starts 1953, birth 1919 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1956
- [FAIL] position_sim: best 50 vs bar 60: 'dep. dir., agric.' ~ 'Deputy Director'
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

