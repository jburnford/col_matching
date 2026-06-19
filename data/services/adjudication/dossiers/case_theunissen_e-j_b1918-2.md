<!-- {"case_id": "case_theunissen_e-j_b1918-2", "bio_ids": ["theunissen_e-j_b1918-2"], "stint_ids": ["Theunissen, E. J___Nyasaland___1949", "Theunissen, E. J___Nyasaland___1962"]} -->
# Dossier case_theunissen_e-j_b1918-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Theunissen, E. J___Nyasaland___1949` is also gate-compatible with biography(ies) outside this case: ['theunissen_e-j_b1918'] (already linked elsewhere or filtered).
- NOTE: stint `Theunissen, E. J___Nyasaland___1962` is also gate-compatible with biography(ies) outside this case: ['theunissen_e-j_b1918'] (already linked elsewhere or filtered).

## Biography `theunissen_e-j_b1918-2`

- Printed name: **THEUNISSEN, E. J**
- Birth year: 1918 (attested in editions [1959])
- Appears in editions: [1959]

### Verbatim printed entry text (OCR)

**Version `col1959-L28538.v` — printed in editions [1959]:**

> THEUNISSEN, E. J.—b. 1918; ed. Royal Coll., Maur., Loughboro' Coll., and Sch. of Librarianship; clk., Maur., 1939-50; educ. offr., 1950; library organizer, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939–1950 | clk. | Mauritius | [1959] |
| 1 | 1955 | library organizer | Mauritius *(inherited from previous clause)* | [1959] |

## Candidate stint `Theunissen, E. J___Nyasaland___1949`

- Staff-list name: **Theunissen, E. J** | colony: **Nyasaland** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. J. Theunissen | Administrative Officer | Provincial and District Administration | — | — |
| 1950 | E. J. Theunissen | Assistant Secretaries | Secretariat | — | — |

### Deterministic checks: `theunissen_e-j_b1918-2` vs `Theunissen, E. J___Nyasaland___1949`

- [PASS] surname_gate: bio 'THEUNISSEN' vs stint 'Theunissen, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Theunissen, E. J___Nyasaland___1962`

- Staff-list name: **Theunissen, E. J** | colony: **Nyasaland** | listed 1962–1963 | editions [1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | E. J. Theunissen | Under Secretary | Ministry of the Chief Secretary | — | — |
| 1963 | E. J. Theunissen | Secretary to the Governor | Civil Establishment | — | — |

### Deterministic checks: `theunissen_e-j_b1918-2` vs `Theunissen, E. J___Nyasaland___1962`

- [PASS] surname_gate: bio 'THEUNISSEN' vs stint 'Theunissen, E. J' (exact)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1962, birth 1918 (age 44)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1963
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

