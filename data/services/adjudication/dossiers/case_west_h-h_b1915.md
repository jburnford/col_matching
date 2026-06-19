<!-- {"case_id": "case_west_h-h_b1915", "bio_ids": ["west_h-h_b1915"], "stint_ids": ["West, H. H___Uganda___1949"]} -->
# Dossier case_west_h-h_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `West, H. H___Uganda___1949` is also gate-compatible with biography(ies) outside this case: ['west_harold_b1882'] (already linked elsewhere or filtered).

## Biography `west_h-h_b1915`

- Printed name: **WEST, H. H**
- Birth year: 1915 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1959-L29170.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964]:**

> WEST, H. H.—b. 1915; ed. Woolwich Commercial and Tech. Inst.; mil. serv., 1939-45, S/capt.; mil. affrs. offr., Uga., 1945; office asst., geol. surv. dept., 1947; acctnts., treasy., 1948; senr. acctnt., 1955; under-sec., min. health, 1961; perm. sec., 1962-63. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | mil. affrs. offr. | Uganda | [1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1947 | office asst., geol. surv. dept | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1948 | acctnts., treasy | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1955 | senr. acctnt | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1961 | under-sec., min. health | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1962–1963 | perm. sec | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `West, H. H___Uganda___1949`

- Staff-list name: **West, H. H** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. H. West | Office Assistant | GEOLOGICAL SURVEY | — | — |
| 1951 | H. H. West | Accountants | ACCOUNTANT-GENERAL | — | — |

### Deterministic checks: `west_h-h_b1915` vs `West, H. H___Uganda___1949`

- [PASS] surname_gate: bio 'WEST' vs stint 'West, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 6 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 57 vs bar 60: 'office asst., geol. surv. dept' ~ 'Office Assistant'
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

