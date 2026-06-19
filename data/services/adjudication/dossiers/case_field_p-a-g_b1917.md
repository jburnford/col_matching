<!-- {"case_id": "case_field_p-a-g_b1917", "bio_ids": ["field_p-a-g_b1917"], "stint_ids": ["Field, P. A. G___Uganda___1949", "Field, P. A. G___Uganda___1959"]} -->
# Dossier case_field_p-a-g_b1917

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Field, P. A. G___Uganda___1949` is also gate-compatible with biography(ies) outside this case: ['field_albert_e1874'] (already linked elsewhere or filtered).
- NOTE: stint `Field, P. A. G___Uganda___1959` is also gate-compatible with biography(ies) outside this case: ['field_albert_e1874'] (already linked elsewhere or filtered).

## Biography `field_p-a-g_b1917`

- Printed name: **FIELD, P. A. G**
- Birth year: 1917 (attested in editions [1957, 1958, 1960, 1961, 1962, 1963])
- Honours: O.B.E (1954)
- Appears in editions: [1957, 1958, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L22994.v` — printed in editions [1957, 1958, 1960, 1961, 1962, 1963]:**

> FIELD, P. A. G., O.B.E. (1954).—b. 1917; ed. Canford Sch., Wimborne, and Trinity Coll., Camb.; mil. serv., 1939–45, capt.; cadet, Uga., 1945; D.O., 1947; senr. D.O., 1958; dist. comsnr., Acholi, 1959–62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | cadet | Uganda | [1957, 1958, 1960, 1961, 1962, 1963] |
| 1 | 1947 | cadet | Dominions Office | [1957, 1958, 1960, 1961, 1962, 1963] |
| 2 | 1958 | senr. D.O | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963] |
| 3 | 1959–1962 | dist. comsnr., Acholi | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963] |

## Candidate stint `Field, P. A. G___Uganda___1949`

- Staff-list name: **Field, P. A. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. A. G. Field | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | P. A. G. Field | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `field_p-a-g_b1917` vs `Field, P. A. G___Uganda___1949`

- [PASS] surname_gate: bio 'FIELD' vs stint 'Field, P. A. G' (exact)
- [PASS] initials: bio ['P', 'A', 'G'] ~ stint ['P', 'A', 'G']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Field, P. A. G___Uganda___1959`

- Staff-list name: **Field, P. A. G** | colony: **Uganda** | listed 1959–1962 | editions [1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | P. A. G. Field | Senior District Officers | Civil Establishment | — | — |
| 1960 | P. A. G. Field | Senior District Officer | Civil Establishment | — | — |
| 1961 | P. A. G. Field | Senior District Officer | Civil Establishment | — | — |
| 1962 | P. A. G. Field | Provincial Commissioner | Civil Establishment | — | — |

### Deterministic checks: `field_p-a-g_b1917` vs `Field, P. A. G___Uganda___1959`

- [PASS] surname_gate: bio 'FIELD' vs stint 'Field, P. A. G' (exact)
- [PASS] initials: bio ['P', 'A', 'G'] ~ stint ['P', 'A', 'G']
- [PASS] age_gate: stint starts 1959, birth 1917 (age 42)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1962
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

