<!-- {"case_id": "case_rush_s-v_b1914", "bio_ids": ["rush_s-v_b1914"], "stint_ids": ["Rush, S. V___Uganda___1949"]} -->
# Dossier case_rush_s-v_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rush_s-v_b1914`

- Printed name: **RUSH, S. V**
- Birth year: 1914 (attested in editions [1957, 1959, 1960, 1961])
- Appears in editions: [1957, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L26888.v` — printed in editions [1957, 1959, 1960, 1961]:**

> RUSH, S. V.—b. 1914; ed. Hurstpierpoint Coll. and Middx. Hosp., London Univ.; mil. serv., 1939–40, capt.; M.O., Uga., 1946; ophthalmic specialist, Nig., 1952; senr. specialist, 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Uganda | [1957, 1959, 1960, 1961] |
| 1 | 1952 | ophthalmic specialist | Nigeria | [1957, 1959, 1960, 1961] |
| 2 | 1958 | senr. specialist | Nigeria *(inherited from previous clause)* | [1957, 1959, 1960, 1961] |

## Candidate stint `Rush, S. V___Uganda___1949`

- Staff-list name: **Rush, S. V** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. V. Rush | Medical Officers | Medical | — | — |
| 1951 | S. V. Rush | Medical Officers | MEDICAL | — | — |

### Deterministic checks: `rush_s-v_b1914` vs `Rush, S. V___Uganda___1949`

- [PASS] surname_gate: bio 'RUSH' vs stint 'Rush, S. V' (exact)
- [PASS] initials: bio ['S', 'V'] ~ stint ['S', 'V']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 22 vs bar 60: 'M.O.' ~ 'Medical Officers'
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

