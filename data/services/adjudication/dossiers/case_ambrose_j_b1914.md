<!-- {"case_id": "case_ambrose_j_b1914", "bio_ids": ["ambrose_j_b1914"], "stint_ids": ["Ambrose, J. W. D___Singapore___1959"]} -->
# Dossier case_ambrose_j_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ambrose_j_b1914'] carry a single initial only — the namesake trap applies.

## Biography `ambrose_j_b1914`

- Printed name: **AMBROSE, J**
- Birth year: 1914 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L14290.v` — printed in editions [1964, 1965, 1966]:**

> AMBROSE, J.—b. 1914; ed. Wade Deacon Gram. Sch., Widnes; mil. serv., 1935-45, sgt. (desps.); chargeman mech., Tang., 1950; inspr. mech., 1952; ch. inspr. mech., 1963-65. (Tanzania Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | chargeman mech. | Tanganyika | [1964, 1965, 1966] |
| 1 | 1952 | inspr. mech | Tanganyika *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1963–1965 | ch. inspr. mech | Tanganyika *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Ambrose, J. W. D___Singapore___1959`

- Staff-list name: **Ambrose, J. W. D** | colony: **Singapore** | listed 1959–1963 | editions [1959, 1960, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | J. W. D. Ambrose | Puisne Judge | Civil Establishment | — | — |
| 1960 | J. W. D. Ambrose | Puisne Judges | JUDICIARY | — | — |
| 1962 | J. W. D. Ambrose | Puisne Judge | JUDICIARY | — | — |
| 1963 | J. W. D. Ambrose | Puisne Judge | JUDICIARY | — | — |

### Deterministic checks: `ambrose_j_b1914` vs `Ambrose, J. W. D___Singapore___1959`

- [PASS] surname_gate: bio 'AMBROSE' vs stint 'Ambrose, J. W. D' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'W', 'D']
- [PASS] age_gate: stint starts 1959, birth 1914 (age 45)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1963
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

