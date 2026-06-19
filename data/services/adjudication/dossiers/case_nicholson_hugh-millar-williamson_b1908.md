<!-- {"case_id": "case_nicholson_hugh-millar-williamson_b1908", "bio_ids": ["nicholson_hugh-millar-williamson_b1908"], "stint_ids": ["Nicholson, H. M. W___Tanganyika___1940"]} -->
# Dossier case_nicholson_hugh-millar-williamson_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nicholson_hugh-millar-williamson_b1908`

- Printed name: **NICHOLSON, Hugh Millar Williamson**
- Birth year: 1908 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L41209.v` — printed in editions [1951]:**

> NICHOLSON, Hugh Millar Williamson, M.P.S. (Edin.).—b. 1908 ; ed. Knox Acad., Haddington ; asst. med. storekpr., prev. serv., Uga., 1933 ; asst. med. storekpr., T.T., 1936 ; pharmacist, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | asst. med. storekpr., prev. serv. | Uganda | [1951] |
| 1 | 1936 | asst. med. storekpr., T.T | Uganda *(inherited from previous clause)* | [1951] |
| 2 | 1937 | pharmacist | Uganda *(inherited from previous clause)* | [1951] |

## Candidate stint `Nicholson, H. M. W___Tanganyika___1940`

- Staff-list name: **Nicholson, H. M. W** | colony: **Tanganyika** | listed 1940–1949 | editions [1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | H. M. W. Nicholson | Pharmacist | Medical Department | — | — |
| 1949 | H. M. W. Nicholson | Pharmacist | Medical and Sanitation | — | — |

### Deterministic checks: `nicholson_hugh-millar-williamson_b1908` vs `Nicholson, H. M. W___Tanganyika___1940`

- [PASS] surname_gate: bio 'NICHOLSON' vs stint 'Nicholson, H. M. W' (exact)
- [PASS] initials: bio ['H', 'M', 'W'] ~ stint ['H', 'M', 'W']
- [PASS] age_gate: stint starts 1940, birth 1908 (age 32)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1949
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

