<!-- {"case_id": "case_snell_douglas-goddard_b1908", "bio_ids": ["snell_douglas-goddard_b1908"], "stint_ids": ["Snell, D. G___Uganda___1940"]} -->
# Dossier case_snell_douglas-goddard_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `snell_douglas-goddard_b1908`

- Printed name: **SNELL, Douglas Goddard**
- Birth year: 1908 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Honours: L.R.C.P, M.B
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L27364.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> SNELL, D. G.—b. 1908; ed. Oakham Sch., St. Thos. Hosp. and London Univ.; mil. serv., 1939; capt.; M.O., Uga., 1936; S.M.O., 1949; asst. D.M.S., 1956; prin. M.O., 1960-62. (Uga. Govt. service.)

**Version `col1948-L36030.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SNELL, Douglas Goddard, M.B., B.S. (Lond.), M.R.C.S. (Eng.), L.R.C.P., D.T.M. & H. (Lond.).—b. 1908; ed. Oakham Sch., St. Thos. Hosp. and London Univ.; on mil. serv. 1939, capt.; med. offr., Uga., 1936; S.M.O., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | M.O. | Uganda | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1949 | S.M.O | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1950 | S.M.O | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1956 | asst. D.M.S | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1960–1962 | prin. M.O | Uganda *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Snell, D. G___Uganda___1940`

- Staff-list name: **Snell, D. G** | colony: **Uganda** | listed 1940–1951 | editions [1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | D. G. Snell | Medical Officer | Medical | — | — |
| 1949 | D. G. Snell | Medical Officers | Medical | — | — |
| 1951 | D. G. Snell | Senior Medical Officers | MEDICAL | — | — |

### Deterministic checks: `snell_douglas-goddard_b1908` vs `Snell, D. G___Uganda___1940`

- [PASS] surname_gate: bio 'SNELL' vs stint 'Snell, D. G' (exact)
- [PASS] initials: bio ['D', 'G'] ~ stint ['D', 'G']
- [PASS] age_gate: stint starts 1940, birth 1908 (age 32)
- [PASS] colony: 5 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1940-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

