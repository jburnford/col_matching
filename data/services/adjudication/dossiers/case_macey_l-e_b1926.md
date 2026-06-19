<!-- {"case_id": "case_macey_l-e_b1926", "bio_ids": ["macey_l-e_b1926"], "stint_ids": ["Facey, L. E___Jamaica___1950"]} -->
# Dossier case_macey_l-e_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macey_l-e_b1926`

- Printed name: **MACEY, L. E**
- Birth year: 1926 (attested in editions [1963, 1964, 1965])
- Appears in editions: [1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1963-L22339.v` — printed in editions [1963, 1964, 1965]:**

> MACEY, L. E.—b. 1926; ed. St. Saviour's Sch., East Twerton Sch., Bath, and Bristol Univ.; supt., lands and survs., Sar., 1952; senr. supt., 1962-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | supt., lands and survs. | Sarawak | [1963, 1964, 1965] |
| 1 | 1962–1964 | senr. supt | Sarawak *(inherited from previous clause)* | [1963, 1964, 1965] |

## Candidate stint `Facey, L. E___Jamaica___1950`

- Staff-list name: **Facey, L. E** | colony: **Jamaica** | listed 1950–1953 | editions [1950, 1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | L. E. Facey | Government Printer | Printing | — | — |
| 1951 | L. E. Facey | Government Printer | PRINTING | — | — |
| 1952 | L. E. Facey | Government Printer | Civil Establishment | — | — |
| 1953 | L. E. Facey | Government Printer | Civil Establishment | — | — |

### Deterministic checks: `macey_l-e_b1926` vs `Facey, L. E___Jamaica___1950`

- [PASS] surname_gate: bio 'MACEY' vs stint 'Facey, L. E' (fuzzy:1)
- [PASS] initials: bio ['L', 'E'] ~ stint ['L', 'E']
- [PASS] age_gate: stint starts 1950, birth 1926 (age 24)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1953
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

