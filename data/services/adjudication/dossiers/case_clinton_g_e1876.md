<!-- {"case_id": "case_clinton_g_e1876", "bio_ids": ["clinton_g_e1876"], "stint_ids": ["Clinton, Geo___Windward Islands___1877"]} -->
# Dossier case_clinton_g_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['clinton_g_e1876'] carry a single initial only — the namesake trap applies.

## Biography `clinton_g_e1876`

- Printed name: **CLINTON, G**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L32712.v` — printed in editions [1886]:**

> CLINTON, G.—Landing surveyor, customs, Barbados, April, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Landing surveyor, customs | Barbados | [1886] |

## Candidate stint `Clinton, Geo___Windward Islands___1877`

- Staff-list name: **Clinton, Geo** | colony: **Windward Islands** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. Clinton | Landing Surveyor | Customs | — | — |
| 1878 | Geo. Clinton | Landing Surveyor | Customs | — | — |
| 1879 | Geo. Clinton | Landing Surveyor | Customs | — | — |
| 1880 | Geo. Clinton | Landing Surveyor | Customs | — | — |
| 1883 | Geo. Clinton | Landing Surveyor | Customs | — | — |

### Deterministic checks: `clinton_g_e1876` vs `Clinton, Geo___Windward Islands___1877`

- [PASS] surname_gate: bio 'CLINTON' vs stint 'Clinton, Geo' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
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

