<!-- {"case_id": "case_phillips_c-m_b1918", "bio_ids": ["phillips_c-m_b1918"], "stint_ids": ["Phillips, G. C. M___Kenya___1950"]} -->
# Dossier case_phillips_c-m_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 119 official(s) with this surname in the graph's staff lists; 54 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `phillips_c-m_b1918`

- Printed name: **PHILLIPS, C. M**
- Birth year: 1918 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L26331.v` — printed in editions [1957]:**

> PHILLIPS, C. M.—b. 1918; ed. Sherborne Sch., Camb. Univ. and St. Thos. Hosp.; M.O., N.Rhod., 1943; specialist, 1951; secon., fedl. govt., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | M.O. | Northern Rhodesia | [1957] |
| 1 | 1951 | specialist | Northern Rhodesia *(inherited from previous clause)* | [1957] |
| 2 | 1954 | secon., fedl. govt | Northern Rhodesia *(inherited from previous clause)* | [1957] |

## Candidate stint `Phillips, G. C. M___Kenya___1950`

- Staff-list name: **Phillips, G. C. M** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | G. C. M. Phillips | Superintendents and Assistant Superintendents, Grade I | PRISONS | — | — |
| 1951 | G. C. M. Phillips | Superintendents and Assistant Superintendents, Grade I | PRISONS | — | — |

### Deterministic checks: `phillips_c-m_b1918` vs `Phillips, G. C. M___Kenya___1950`

- [PASS] surname_gate: bio 'PHILLIPS' vs stint 'Phillips, G. C. M' (exact)
- [PASS] initials: bio ['C', 'M'] ~ stint ['G', 'C', 'M']
- [PASS] age_gate: stint starts 1950, birth 1918 (age 32)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

