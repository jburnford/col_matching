<!-- {"case_id": "case_manford_w_e1880", "bio_ids": ["manford_w_e1880"], "stint_ids": ["Sanford, W. E___Canada___1889"]} -->
# Dossier case_manford_w_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['manford_w_e1880'] carry a single initial only — the namesake trap applies.

## Biography `manford_w_e1880`

- Printed name: **MANFORD, W**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34697.v` — printed in editions [1886]:**

> MANFORD, W.—Auditor, Gold Coast, 20 April, 1880; Controller of customs, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Auditor | Gold Coast | [1886] |
| 1 | 1885 | Controller of customs | Gold Coast *(inherited from previous clause)* | [1886] |

## Candidate stint `Sanford, W. E___Canada___1889`

- Staff-list name: **Sanford, W. E** | colony: **Canada** | listed 1889–1898 | editions [1889, 1890, 1894, 1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | W. E. Sanford | Senator | Senate of Canada | — | — |
| 1890 | W. E. Sanford | Senator | Senate | — | — |
| 1894 | W. E. Sanford | — | Senate | — | — |
| 1896 | W. E. Sanford | Senator | Senate of Canada | — | — |
| 1898 | W. E. Sanford | Senator | Senate | — | — |

### Deterministic checks: `manford_w_e1880` vs `Sanford, W. E___Canada___1889`

- [PASS] surname_gate: bio 'MANFORD' vs stint 'Sanford, W. E' (fuzzy:1)
- [PASS] initials: bio ['W'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1898
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

