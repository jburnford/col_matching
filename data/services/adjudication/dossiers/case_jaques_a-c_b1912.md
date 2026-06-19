<!-- {"case_id": "case_jaques_a-c_b1912", "bio_ids": ["jaques_a-c_b1912"], "stint_ids": ["Jaques, A. C___Basutoland___1965"]} -->
# Dossier case_jaques_a-c_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jaques_a-c_b1912`

- Printed name: **JAQUES, A. C**
- Birth year: 1912 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L22786.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> JAQUES, A. C.—b. 1912; ed. Pretoria Boys' High Sch., and Witwatersrand Univ.; mil. serv., 1941-45; capt.; M.O., Basuto., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | M.O. | Basutoland | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Jaques, A. C___Basutoland___1965`

- Staff-list name: **Jaques, A. C** | colony: **Basutoland** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | A. C. Jaques | Senior Medical Officer | Secretariat | — | — |
| 1966 | A. C. Jaques | Senior Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `jaques_a-c_b1912` vs `Jaques, A. C___Basutoland___1965`

- [PASS] surname_gate: bio 'JAQUES' vs stint 'Jaques, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1965, birth 1912 (age 53)
- [PASS] colony: 1 placed event(s) resolve to 'Basutoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

