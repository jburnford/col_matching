<!-- {"case_id": "case_cumber_j-a_b1920", "bio_ids": ["cumber_j-a_b1920"], "stint_ids": ["Cumber, J. A___Cayman Islands___1964"]} -->
# Dossier case_cumber_j-a_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cumber_j-a_b1920`

- Printed name: **CUMBER, J. A**
- Birth year: 1920 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965])
- Honours: M.B.E (1954)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1960-L22051.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965]:**

> CUMBER, J. A., M.B.E. (1954), T.D.—b. 1920; ed. Richmond Gram. Sch.; mil. serv., 1939-46, major; dist. offr., Ken., 1947; asst. sec., 1954; senr. dist. comsnr., 1960; senr. D.O., 1961-63; admint., Cayman Is., 1964.

**Version `col1958-L21776.v` — printed in editions [1958, 1959]:**

> CUMBER, J. A., M.B.E. (1954), T.D.—b. 1920; ed. Richmond County Sch. and Richmond Art Sch.; mil. serv., 1938–46; dist. offr., Ken., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | dist. offr. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1954 | asst. sec | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1960 | senr. dist. comsnr | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1961–1963 | senr. D.O | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1964 | admint., Cayman Is | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Cumber, J. A___Cayman Islands___1964`

- Staff-list name: **Cumber, J. A** | colony: **Cayman Islands** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | J. A. Cumber | Administrator (also Registrar-General) | Civil Establishment | — | — |
| 1965 | J. A. Cumber | Administrator (also Registrar-General) | Civil Establishment | — | — |
| 1966 | J. A. Cumber | Administrator (also Registrar-General) | Civil Establishment | — | — |

### Deterministic checks: `cumber_j-a_b1920` vs `Cumber, J. A___Cayman Islands___1964`

- [PASS] surname_gate: bio 'CUMBER' vs stint 'Cumber, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1964, birth 1920 (age 44)
- [FAIL] colony: no placed event resolves to 'Cayman Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

