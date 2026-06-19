<!-- {"case_id": "case_mackintosh_a-l_b1919", "bio_ids": ["mackintosh_a-l_b1919"], "stint_ids": ["Mackintosh, A. L___Gambia___1962"]} -->
# Dossier case_mackintosh_a-l_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mackintosh_a-l_b1919`

- Printed name: **MACKINTOSH, A. L**
- Birth year: 1919 (attested in editions [1964, 1965])
- Honours: M.B.E
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L19520.v` — printed in editions [1964, 1965]:**

> MACKINTOSH, A. L., M.B.E.—b. 1919; co-op. dept., Nig., 1953; registr. co-op. soc., Gam., 1955.

**Version `col1966-L16441.v` — printed in editions [1966]:**

> MACKINTOSH, A. L., M.B.E.—b. 1919; ed. Craigton Sch., Bellahouston Acad., Glasgow, and Co-op. Coll., Loughborough; asst. regstr., co-op. dept., E. Nig., 1953; regstr., co-op. soc., Gam., 1955. (Gambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | co-op. dept. | Nigeria | [1964, 1965, 1966] |
| 1 | 1955 | registr. co-op. soc., Gam | Nigeria *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Mackintosh, A. L___Gambia___1962`

- Staff-list name: **Mackintosh, A. L** | colony: **Gambia** | listed 1962–1963 | editions [1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | A. L. Mackintosh | Registrar of Co-operative Societies | Civil Establishment | — | — |
| 1963 | A. L. Mackintosh | Registrar of Co-operative Societies | Ministry of Agriculture | — | — |

### Deterministic checks: `mackintosh_a-l_b1919` vs `Mackintosh, A. L___Gambia___1962`

- [PASS] surname_gate: bio 'MACKINTOSH' vs stint 'Mackintosh, A. L' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1962, birth 1919 (age 43)
- [FAIL] colony: no placed event resolves to 'Gambia'
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

