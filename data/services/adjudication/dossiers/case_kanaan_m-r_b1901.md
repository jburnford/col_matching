<!-- {"case_id": "case_kanaan_m-r_b1901", "bio_ids": ["kanaan_m-r_b1901"], "stint_ids": ["Kanaan, M. R___Cyprus___1955"]} -->
# Dossier case_kanaan_m-r_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kanaan_m-r_b1901`

- Printed name: **KANAAN, M. R**
- Birth year: 1901 (attested in editions [1959])
- Honours: M.B.E
- Appears in editions: [1959]

### Verbatim printed entry text (OCR)

**Version `col1959-L24779.v` — printed in editions [1959]:**

> KANAAN, M. R., M.B.E.—b. 1901; ed. American Academy, Larnaca; co-op. offr., Cyp., 1932; asst. comsnt., co-op. devel., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | co-op. offr. | Cyprus | [1959] |
| 1 | 1939 | asst. comsnt., co-op. devel | Cyprus *(inherited from previous clause)* | [1959] |

## Candidate stint `Kanaan, M. R___Cyprus___1955`

- Staff-list name: **Kanaan, M. R** | colony: **Cyprus** | listed 1955–1959 | editions [1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | M. R. Kanaan | Assistant Commissioner for Co-operative Development | Civil Establishment | — | — |
| 1956 | M. R. Kanaan | Assistant Commissioner for Co-operative Development | Civil Establishment | — | — |
| 1957 | M. R. Kanaan | Assistant Commissioner for Co-operative Development | Civil Establishment | — | — |
| 1958 | M. R. Kanaan | Assistant Commissioner for Co-operative Development | Civil Establishment | M.B.E. | — |
| 1959 | M. R. Kanaan | Assistant Commissioner for Co-operative Development | Civil Establishment | — | — |

### Deterministic checks: `kanaan_m-r_b1901` vs `Kanaan, M. R___Cyprus___1955`

- [PASS] surname_gate: bio 'KANAAN' vs stint 'Kanaan, M. R' (exact)
- [PASS] initials: bio ['M', 'R'] ~ stint ['M', 'R']
- [PASS] age_gate: stint starts 1955, birth 1901 (age 54)
- [PASS] colony: 2 placed event(s) resolve to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1959
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
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

