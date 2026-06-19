<!-- {"case_id": "case_kelly_t-e-d_b1903", "bio_ids": ["kelly_t-e-d_b1903"], "stint_ids": ["Kelly, E. D___British Guiana___1924"]} -->
# Dossier case_kelly_t-e-d_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kelly_t-e-d_b1903`

- Printed name: **KELLY, T. E. D.**
- Birth year: 1903 (attested in editions [1957, 1958])
- Honours: C.B.E. (1946)
- Appears in editions: [1957, 1958]

### Verbatim printed entry text (OCR)

**Version `col1957-L24634.v` — printed in editions [1957, 1958]:**

> KELLY, T. E. D., C.B.E. (1946)—b. 1903; ed. Rugby Sch. and R.M.A., Woolwich; R.A. and staff, 1923-55, brigadier; instr., staff coll. and jt. services' staff coll.; defence sec., E.A.H.C., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923–1955 | R.A. and staff, brigadier | — | [1957, 1958] |
| 1 | 1956 | defence sec. | East Africa High Commission | [1957, 1958] |

## Candidate stint `Kelly, E. D___British Guiana___1924`

- Staff-list name: **Kelly, E. D** | colony: **British Guiana** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | Miss E. Kelly | 6th Class Clerk | Judicial Establishment | — | — |
| 1925 | E. D. Kelly | Clerical Assistant | Harbour Board | — | — |

### Deterministic checks: `kelly_t-e-d_b1903` vs `Kelly, E. D___British Guiana___1924`

- [PASS] surname_gate: bio 'KELLY' vs stint 'Kelly, E. D' (exact)
- [PASS] initials: bio ['T', 'E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1924, birth 1903 (age 21)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
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

