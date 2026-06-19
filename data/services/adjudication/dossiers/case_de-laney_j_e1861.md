<!-- {"case_id": "case_de-laney_j_e1861", "bio_ids": ["de-laney_j_e1861"], "stint_ids": ["Delaney, John___Newfoundland___1877"]} -->
# Dossier case_de-laney_j_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['de-laney_j_e1861'] carry a single initial only — the namesake trap applies.

## Biography `de-laney_j_e1861`

- Printed name: **DE LANEY, J**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27125.v` — printed in editions [1883]:**

> DE LANEY, J.—Postmaster, Newfoundland, 1861; formerly inspector of roads, under board of works, and many years a member of the assembly.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Postmaster | Newfoundland | [1883] |

## Candidate stint `Delaney, John___Newfoundland___1877`

- Staff-list name: **Delaney, John** | colony: **Newfoundland** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John Delaney | Postmaster-General | Civil Establishment | — | — |
| 1878 | John Delaney | Postmaster-General | Civil Establishment | — | — |
| 1879 | John Delaney | Postmaster-General | Civil Establishment | — | — |
| 1880 | John Delaney | Postmaster-General | Civil Establishment | — | — |

### Deterministic checks: `de-laney_j_e1861` vs `Delaney, John___Newfoundland___1877`

- [PASS] surname_gate: bio 'DE LANEY' vs stint 'Delaney, John' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

