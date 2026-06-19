<!-- {"case_id": "case_andolo_charles-a_e1883", "bio_ids": ["andolo_charles-a_e1883", "dandolo_charles-a_e1883"], "stint_ids": ["Dandolo, C___Cyprus___1905"]} -->
# Dossier case_andolo_charles-a_e1883

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Dandolo, C___Cyprus___1905'] have more than one claimant biography in this case.

## Biography `andolo_charles-a_e1883`

- Printed name: **ANDOLO, CHARLES A.**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L31560.v` — printed in editions [1897]:**

> ANDOLO, CHARLES A.—Clerk, dist. ct., Larne, Cyprus, Mar., 1883; asst. regr. and inter. agent, 1886; ag. regr., July, 1886, to Sept., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Clerk, dist. ct. | Cyprus | [1897] |
| 1 | 1886 | asst. regr. and inter. agent | — | [1897] |
| 2 | 1886–1887 | ag. regr. | — | [1897] |

## Biography `dandolo_charles-a_e1883`

- Printed name: **DANDOLO, CHARLES A.**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1898]

### Verbatim printed entry text (OCR)

**Version `col1894-L31090.v` — printed in editions [1894, 1896, 1898]:**

> DANDOLO, CHARLES A.—Clerk, dist. ct., Laracca, Cyprus, Mar., 1883; asst. regtr. and interpreter, 1886; ag. regtr. July, 1886, to Sept., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Clerk, dist. ct. | Cyprus | [1894, 1896, 1898] |
| 1 | 1886 | asst. regtr. and interpreter | — | [1894, 1896, 1898] |

## Candidate stint `Dandolo, C___Cyprus___1905`

- Staff-list name: **Dandolo, C** | colony: **Cyprus** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. Dandolo | Clerk and Assistant Registrar and Interpreter | District Courts | — | — |
| 1906 | C. Dandolo | Clerk and Assistant Registrar and Interpreter | District Courts | — | — |
| 1907 | C. Dandolo | Clerk and Assistant Registrar and Interpreter | Courts of Justice | — | — |
| 1908 | C. Dandolo | Clerk and Assistant Interpreter and Registrar | Legal Departments | — | — |
| 1909 | C. Dandolo | Clerk and Assistant Interpreter and Registrar | District Courts | — | — |

### Deterministic checks: `andolo_charles-a_e1883` vs `Dandolo, C___Cyprus___1905`

- [PASS] surname_gate: bio 'ANDOLO' vs stint 'Dandolo, C' (fuzzy:1)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `dandolo_charles-a_e1883` vs `Dandolo, C___Cyprus___1905`

- [PASS] surname_gate: bio 'DANDOLO' vs stint 'Dandolo, C' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

