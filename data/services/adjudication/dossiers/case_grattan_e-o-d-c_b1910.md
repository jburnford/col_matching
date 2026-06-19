<!-- {"case_id": "case_grattan_e-o-d-c_b1910", "bio_ids": ["grattan_e-o-d-c_b1910"], "stint_ids": ["Grattan, E. O. C___Kenya___1949"]} -->
# Dossier case_grattan_e-o-d-c_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `grattan_e-o-d-c_b1910`

- Printed name: **GRATTAN, E. O'D. C**
- Birth year: 1910 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L23524.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> GRATTAN, E. O'D. C.—b. 1910; ed. Wellington Coll., Camb. Univ. and St. Thos. Hosp.; M.O., Ken., 1947; specialist, surgical, 1953; pubns. Thyroidectomy in conjunction with the use of Hexamethonium Bromide; A case of severe Burns in an Epileptic with the loss of both Hands and Subsequent Repairs.

**Version `col1962-L21698.v` — printed in editions [1962, 1963, 1964]:**

> GRATTAN, E. O’D. C.—b. 1910; ed. Wellington Coll., Camb. Univ. and St. Thos. Hosp.; M.O., Ken., 1947; specialist, surgical, 1953–63. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1953 | specialist, surgical | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Grattan, E. O. C___Kenya___1949`

- Staff-list name: **Grattan, E. O. C** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. O. C. Grattan | Medical Officer | Medical | — | — |
| 1950 | E. O. C. Grattan | Medical Officer | Medical | — | — |
| 1951 | E. O. C. Grattan | Medical Officer | Medical | — | — |

### Deterministic checks: `grattan_e-o-d-c_b1910` vs `Grattan, E. O. C___Kenya___1949`

- [PASS] surname_gate: bio 'GRATTAN' vs stint 'Grattan, E. O. C' (exact)
- [PASS] initials: bio ['E', 'O', 'C'] ~ stint ['E', 'O', 'C']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
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

