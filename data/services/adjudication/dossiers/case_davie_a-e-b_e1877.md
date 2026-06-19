<!-- {"case_id": "case_davie_a-e-b_e1877", "bio_ids": ["davie_a-e-b_e1877"], "stint_ids": ["Davie, A. E. B___Canada___1886"]} -->
# Dossier case_davie_a-e-b_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davie_a-e-b_e1877`

- Printed name: **DAVIE, A. E. B**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1886-L32949.v` — printed in editions [1886, 1888, 1889]:**

> DAVIE, HON. A. E. B., Q.C.—Attorney-general, British Columbia, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | Attorney-general | British Columbia | [1886, 1888, 1889] |

## Candidate stint `Davie, A. E. B___Canada___1886`

- Staff-list name: **Davie, A. E. B** | colony: **Canada** | listed 1886–1889 | editions [1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | A. E. B. Davie | Attorney-General | Attorney-General's Office | — | — |
| 1888 | A. E. B. Davie | Attorney-General | Attorney-General's Office | — | — |
| 1888 | A. E. B. Davie | Member | Legislative Assembly | — | — |
| 1888 | A. E. B. Davie | Attorney-General | Executive Council | — | — |
| 1889 | A. E. B. Davie | Attorney-General | Executive Council | — | — |

### Deterministic checks: `davie_a-e-b_e1877` vs `Davie, A. E. B___Canada___1886`

- [PASS] surname_gate: bio 'DAVIE' vs stint 'Davie, A. E. B' (exact)
- [PASS] initials: bio ['A', 'E', 'B'] ~ stint ['A', 'E', 'B']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1889
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

