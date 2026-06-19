<!-- {"case_id": "case_pearse_benjamin-w_e1861", "bio_ids": ["pearse_benjamin-w_e1861"], "stint_ids": ["Pearse, B. W___Canada___1877"]} -->
# Dossier case_pearse_benjamin-w_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pearse_benjamin-w_e1861`

- Printed name: **PEARSE, BENJAMIN W**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29049.v` — printed in editions [1883]:**

> PEARSE, BENJAMIN W.—Assistant surveyor-general, Vancouver Island, 1861; previously employed in same capacity by Hudson Bay Company during their tenure of the island, 1868; now resident engineer for Dominion Public Works, in Victoria.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Assistant surveyor-general | Vancouver Island | [1883] |
| 1 | 1868 | previously employed in same capacity by Hudson Bay Company during their tenure of the island | Vancouver Island *(inherited from previous clause)* | [1883] |

## Candidate stint `Pearse, B. W___Canada___1877`

- Staff-list name: **Pearse, B. W** | colony: **Canada** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | B. W. Pearse | Engineer | Dominion Public Works | — | — |
| 1878 | B. W. Pearse | Engineer | DOMINION PUBLIC WORKS | — | — |
| 1879 | B. W. Pearse | Engineer | DOMINION PUBLIC WORKS | — | — |

### Deterministic checks: `pearse_benjamin-w_e1861` vs `Pearse, B. W___Canada___1877`

- [PASS] surname_gate: bio 'PEARSE' vs stint 'Pearse, B. W' (exact)
- [PASS] initials: bio ['B', 'W'] ~ stint ['B', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
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

