<!-- {"case_id": "case_pinesent_robert-j_e1856", "bio_ids": ["pinesent_robert-j_e1856"], "stint_ids": ["Pinsent, Robert J___Newfoundland___1883"]} -->
# Dossier case_pinesent_robert-j_e1856

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pinesent_robert-j_e1856`

- Printed name: **PINESENT, ROBERT J.**
- Birth year: not printed
- Honours: D.C.L. (1881)
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L36211.v` — printed in editions [1890]:**

> PINESENT, ROBERT J., D.C.L.—Called to the bar, 1856 appointed to legislative council, Newfoundland, in 1859; created Q.C. in 1865; acting attorney-general in 1869; re-appointed to legislative council in 1869; solicitor-general in 1873; puisne judge of the supreme court in 1880; received degree of D.C.L. (Lambeth) in 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856 | Called to the bar | — | [1890] |
| 1 | 1859 | legislative council | Newfoundland | [1890] |
| 2 | 1865 | Q.C. | — | [1890] |
| 3 | 1869 | acting attorney-general | — | [1890] |
| 4 | 1869 | legislative council | — | [1890] |
| 5 | 1873 | solicitor-general | — | [1890] |
| 6 | 1880 | puisne judge of the supreme court | — | [1890] |
| 7 | 1881 | — | — | [1890] |

## Candidate stint `Pinsent, Robert J___Newfoundland___1883`

- Staff-list name: **Pinsent, Robert J** | colony: **Newfoundland** | listed 1883–1889 | editions [1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | Robert J. Pinsent | Assistant Justice | Judicial Establishment | — | — |
| 1886 | Robert J. Pinsent | Assistant Justice | Judicial Establishment | — | — |
| 1888 | Robert J. Pinsent | Assistant Justice | Judicial Establishment | — | — |
| 1889 | Robert J. Pinsent | Assistant Justice | Judicial Establishment | — | — |

### Deterministic checks: `pinesent_robert-j_e1856` vs `Pinsent, Robert J___Newfoundland___1883`

- [PASS] surname_gate: bio 'PINESENT' vs stint 'Pinsent, Robert J' (fuzzy:1)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1889
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

