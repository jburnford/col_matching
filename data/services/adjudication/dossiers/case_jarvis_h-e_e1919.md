<!-- {"case_id": "case_jarvis_h-e_e1919", "bio_ids": ["jarvis_h-e_e1919"], "stint_ids": ["Jarvis, H. E___Uganda___1929"]} -->
# Dossier case_jarvis_h-e_e1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jarvis_h-e_e1919`

- Printed name: **JARVIS, H. E**
- Birth year: not printed
- Appears in editions: [1920, 1922]

### Verbatim printed entry text (OCR)

**Version `col1920-L54684.v` — printed in editions [1920, 1922]:**

> JARVIS, H. E.—Tempy. astt. dist. commrs., E.A.P., June, 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | Tempy. astt. dist. commrs. | East Africa Protectorate | [1920, 1922] |

## Candidate stint `Jarvis, H. E___Uganda___1929`

- Staff-list name: **Jarvis, H. E** | colony: **Uganda** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | H. E. Jarvis | Road Foreman | Public Works | — | — |
| 1930 | H. E. Jarvis | Clerk | Police and Prisons | — | — |

### Deterministic checks: `jarvis_h-e_e1919` vs `Jarvis, H. E___Uganda___1929`

- [PASS] surname_gate: bio 'JARVIS' vs stint 'Jarvis, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1929; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

