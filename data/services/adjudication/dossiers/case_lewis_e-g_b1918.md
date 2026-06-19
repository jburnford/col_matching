<!-- {"case_id": "case_lewis_e-g_b1918", "bio_ids": ["lewis_e-g_b1918"], "stint_ids": ["Lewis, I. E. G___Uganda___1949", "Lewis, I. E. G___Uganda___1955"]} -->
# Dossier case_lewis_e-g_b1918

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 157 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lewis, I. E. G___Uganda___1949` is also gate-compatible with biography(ies) outside this case: ['lewis_i-e-g_b1904'] (already linked elsewhere or filtered).
- NOTE: stint `Lewis, I. E. G___Uganda___1955` is also gate-compatible with biography(ies) outside this case: ['lewis_i-e-g_b1904'] (already linked elsewhere or filtered).

## Biography `lewis_e-g_b1918`

- Printed name: **LEWIS, E. G**
- Birth year: 1918 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1958)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L24994.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> LEWIS, E. G., O.B.E. (1958), M.B.E. (Mil.).—b. 1918; ed. Otago Boys' High Sch. and Otago Univ., N.Z.; mil. serv., 1939-46, Lt.-col. (desps.); cadet, Nig., 1946; admin. offr., cl. II, 1955; secon., comsnt., Turks and Caicos Is., 1955-58; admin. offr., cl. I, Nig., 1959; perm. sec., 1960-62. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1955 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1959 | admin. offr., cl. I | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1960–1962 | perm. sec | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Lewis, I. E. G___Uganda___1949`

- Staff-list name: **Lewis, I. E. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | I. E. G. Lewis | Resident Magistrates | JUDICIAL | — | — |
| 1951 | I. E. G. Lewis | Resident Magistrates | Judicial | — | — |

### Deterministic checks: `lewis_e-g_b1918` vs `Lewis, I. E. G___Uganda___1949`

- [PASS] surname_gate: bio 'LEWIS' vs stint 'Lewis, I. E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['I', 'E', 'G']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Lewis, I. E. G___Uganda___1955`

- Staff-list name: **Lewis, I. E. G** | colony: **Uganda** | listed 1955–1962 | editions [1955, 1956, 1957, 1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | I. E. G. Lewis | Puisne Judge | Civil Establishment | — | — |
| 1956 | I. E. G. Lewis | Puisne Judges | Civil Establishment | — | — |
| 1957 | I. E. G. Lewis | Puisne Judge | Civil Establishment | — | — |
| 1959 | I. E. G. Lewis | Puisne Judges | Civil Establishment | — | — |
| 1960 | I. E. G. Lewis | Puisne Judge | Judiciary | — | — |
| 1961 | I. E. G. Lewis | Puisne Judge | Judiciary | — | — |
| 1962 | I. E. G. Lewis | Puisne Judge | Judiciary | — | — |

### Deterministic checks: `lewis_e-g_b1918` vs `Lewis, I. E. G___Uganda___1955`

- [PASS] surname_gate: bio 'LEWIS' vs stint 'Lewis, I. E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['I', 'E', 'G']
- [PASS] age_gate: stint starts 1955, birth 1918 (age 37)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1962
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

