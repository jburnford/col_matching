<!-- {"case_id": "case_blanc_g-b_e1862", "bio_ids": ["blanc_g-b_e1862"], "stint_ids": ["Blanc, G. B___Dominica___1886", "Blanc, G. B___Leeward Islands___1877"]} -->
# Dossier case_blanc_g-b_e1862

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blanc_g-b_e1862`

- Printed name: **BLANC, G. B**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L26482.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> BLANC, G. B.—Chief engineer and inspector of roads, Dominica, 27th Nov., 1862.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Chief engineer and inspector of roads | Dominica | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Blanc, G. B___Dominica___1886`

- Staff-list name: **Blanc, G. B** | colony: **Dominica** | listed 1886–1890 | editions [1886, 1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | G. B. Blanc | Civil Engineer and Inspector of Roads | Civil Establishment | — | — |
| 1888 | G. B. Blanc | Civil Engineer and Inspector of Roads | Civil Engineer and Inspector of Roads | — | — |
| 1890 | G. B. Blanc | Colonial Engineer | Civil Establishment | — | — |

### Deterministic checks: `blanc_g-b_e1862` vs `Blanc, G. B___Dominica___1886`

- [PASS] surname_gate: bio 'BLANC' vs stint 'Blanc, G. B' (exact)
- [PASS] initials: bio ['G', 'B'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Dominica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Blanc, G. B___Leeward Islands___1877`

- Staff-list name: **Blanc, G. B** | colony: **Leeward Islands** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. B. Blanc | Civil Engineer and Inspector of Roads | Civil Engineer and Inspector of Roads | — | — |
| 1879 | G. B. Blanc, Esq. | Crown Nominee | Legislative Assembly | — | — |
| 1879 | G. B. Blanc | Civil Engineer and Inspector of Roads | Civil Establishment | — | — |
| 1880 | G. B. Blanc | Civil Engineer and Inspector of Roads | Civil Establishment | — | — |
| 1880 | G. B. Blanc | — | Legislative Assembly - Cronon Nominees | — | — |
| 1883 | G. B. Blanc | Civil Engineer and Inspector of Roads | Civil Establishment | — | — |
| 1883 | G. B. Blanc | Crown Nominee | Legislative Assembly | — | — |

### Deterministic checks: `blanc_g-b_e1862` vs `Blanc, G. B___Leeward Islands___1877`

- [PASS] surname_gate: bio 'BLANC' vs stint 'Blanc, G. B' (exact)
- [PASS] initials: bio ['G', 'B'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

