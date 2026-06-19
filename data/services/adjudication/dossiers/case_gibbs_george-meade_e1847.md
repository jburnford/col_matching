<!-- {"case_id": "case_gibbs_george-meade_e1847", "bio_ids": ["gibbs_george-meade_e1847"], "stint_ids": ["Gibbs, G. M___Leeward Islands___1877"]} -->
# Dossier case_gibbs_george-meade_e1847

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 31 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gibbs_george-meade_e1847`

- Printed name: **GIBBS, GEORGE MEADE**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27624.v` — printed in editions [1883]:**

> GIBBS, GEORGE MEADE, M.A.—Archdeacon of St. Kitts, Nevis, &c.; educated at Trinity College, Dublin; obtained at entrance recommendation for honours and Hebrew prize; graduated 1847; ordained by the bishop of Lichfield, 1848, for Trinity parish, Derby; appointed to curacy of St. Mary's, Southwark, 1851; Wonston, Hants, 1856; archdeacon of St. Kitts, and rector of St. George's, Basseterre, Dec. 1861. Member executive legislative council, St. Kitts, 1862.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1847 | — | — | [1883] |
| 1 | 1848 | ordained | — | [1883] |
| 2 | 1851 | curacy of St. Mary's | Southwark | [1883] |
| 3 | 1856 | — | Wonston, Hants | [1883] |
| 4 | 1861 | archdeacon of St. Kitts, and rector of St. George's | Basseterre | [1883] |
| 5 | 1862 | Member executive legislative council | St. Kitts | [1883] |
| 6 | ? | Archdeacon | St. Kitts | [1883] |

## Candidate stint `Gibbs, G. M___Leeward Islands___1877`

- Staff-list name: **Gibbs, G. M** | colony: **Leeward Islands** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. M. Gibbs | Archdeacon | Ecclesiastical | — | — |
| 1878 | G. M. Gibbs | Archdeacon | Ecclesiastical | — | — |
| 1879 | G. M. Gibbs | Archdeacon | Ecclesiastical | — | — |
| 1880 | G. M. Gibbs | Archdeacon | Ecclesiastical | — | — |

### Deterministic checks: `gibbs_george-meade_e1847` vs `Gibbs, G. M___Leeward Islands___1877`

- [PASS] surname_gate: bio 'GIBBS' vs stint 'Gibbs, G. M' (exact)
- [PASS] initials: bio ['G', 'M'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
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

