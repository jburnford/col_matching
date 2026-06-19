<!-- {"case_id": "case_herchenroder_l_e1862", "bio_ids": ["herchenroder_l_e1862"], "stint_ids": ["Herchenroder, L___Mauritius___1877"]} -->
# Dossier case_herchenroder_l_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['herchenroder_l_e1862'] carry a single initial only — the namesake trap applies.

## Biography `herchenroder_l_e1862`

- Printed name: **HERCHENRODER, L**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27973.v` — printed in editions [1883]:**

> HERCHENRODER, L.—First clerk in the registration and mortgage department, Mauritius, April, 1862.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | First clerk in the registration and mortgage department | Mauritius | [1883] |

## Candidate stint `Herchenroder, L___Mauritius___1877`

- Staff-list name: **Herchenroder, L** | colony: **Mauritius** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | L. Herchenroder | Senior Clerk | Registration and Mortgage Department | — | — |
| 1878 | L. Herchenroder | Senior Clerks | Registration and Mortgage Department | — | — |
| 1879 | L. Herchenroder | Senior Clerk | Registration and Mortgage Department | — | — |

### Deterministic checks: `herchenroder_l_e1862` vs `Herchenroder, L___Mauritius___1877`

- [PASS] surname_gate: bio 'HERCHENRODER' vs stint 'Herchenroder, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

