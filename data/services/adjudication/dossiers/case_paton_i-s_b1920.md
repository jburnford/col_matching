<!-- {"case_id": "case_paton_i-s_b1920", "bio_ids": ["paton_i-s_b1920"], "stint_ids": ["Paton, I. S___British Guiana___1949"]} -->
# Dossier case_paton_i-s_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `paton_i-s_b1920`

- Printed name: **PATON, I. S**
- Birth year: 1920 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.P.M (1954), Q.P.M (1961)
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L26781.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> PATON, I. S., Q.P.M. (1961), C.P.M. (1954).—b. 1920; ed. High Sch., Arbroath, Morgan Academy, and Dundee Tech. Coll.; mil. serv., 1939-46, capt.; asst. supt., police, B. Guiana, 1946; Trin., 1949; supt., 1952; senr. supt., 1955; asst. comsnr., police, Tang., 1958; Uga., 1962. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. supt., police, B. Guiana | — | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1949 | asst. supt., police, B. Guiana | Trinidad | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1952 | supt | Trinidad *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1955 | senr. supt | Trinidad *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1958 | asst. comsnr., police | Tanganyika | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1962 | asst. comsnr., police | Uganda | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Paton, I. S___British Guiana___1949`

- Staff-list name: **Paton, I. S** | colony: **British Guiana** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | I. S. Paton | Assistant Superintendent of Police | Police | — | — |
| 1950 | I. S. Paton | Assistant Superintendent of Police | Police | — | — |

### Deterministic checks: `paton_i-s_b1920` vs `Paton, I. S___British Guiana___1949`

- [PASS] surname_gate: bio 'PATON' vs stint 'Paton, I. S' (exact)
- [PASS] initials: bio ['I', 'S'] ~ stint ['I', 'S']
- [PASS] age_gate: stint starts 1949, birth 1920 (age 29)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

