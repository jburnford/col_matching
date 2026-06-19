<!-- {"case_id": "case_binney_hinbert_e1842", "bio_ids": ["binney_hinbert_e1842"], "stint_ids": ["Binney, Hibbert___Canada___1877"]} -->
# Dossier case_binney_hinbert_e1842

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['binney_hinbert_e1842'] carry a single initial only — the namesake trap applies.

## Biography `binney_hinbert_e1842`

- Printed name: **BINNEY, HINBERT**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L28892.v` — printed in editions [1883, 1886]:**

> NOVA SCOTIA, 4th Bishop of. Founded 1787.—Right Rev. HINBERT BINNEY, D.D.—Educated at King's College, London; was afterwards successively scholar and fellow of Worcester College, Oxford, where he graduated 1st class mathematics, and 2nd class classics, 1842; M.A., 1844; appointed tutor of that college in 1846, and bursar in 1848; ordained a deacon, 1842, a priest, 1843, and consecrated 4th Bishop of Nova Scotia, 1851; is an honorary fellow of King's College, London; patron of the archdeaconries of Nova Scotia and New Brunswick, and visitor of King's College, Nova Scotia. This was the first colonial see founded by Great Britain; the diocese includes Nova Scotia, Cape Breton, and Prince Edward Island.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1842–1842 | graduated 1st class mathematics, and 2nd class classics | — | [1883, 1886] |
| 1 | 1842–1842 | deacon | — | [1883, 1886] |
| 2 | 1843–1843 | priest | — | [1883, 1886] |
| 3 | 1844–1844 | M.A. | — | [1883, 1886] |
| 4 | 1846–1846 | tutor | — | [1883, 1886] |
| 5 | 1848–1848 | bursar | — | [1883, 1886] |
| 6 | 1851–1851 | 4th Bishop of Nova Scotia | Nova Scotia | [1883, 1886] |

## Candidate stint `Binney, Hibbert___Canada___1877`

- Staff-list name: **Binney, Hibbert** | colony: **Canada** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. Binney | Bishop of Nova Scotia | Church of England | — | — |
| 1877 | Hibbert Binney | Lord Bishop of Nova Scotia | Ecclesiastical | — | — |
| 1878 | H. Binney | Bishop of Nova Scotia | Church of England | — | — |
| 1878 | Hibbert Binney | Lord Bishop of Nova Scotia | Ecclesiastical | — | — |
| 1879 | H. Binney | Bishop of Nova Scotia | Church of England | — | — |
| 1879 | Right Rev. Hibbert Binney | Lord Bishop of Nova Scotia | Eccliastical | — | — |
| 1880 | H. Binney | Bishop of Nova Scotia | Church of England | — | — |
| 1880 | Hibbert Binney | Lord Bishop of Nova Scotia | Ecclesiastical | — | — |
| 1883 | H. Binney | Bishop of Nova Scotia | Church of England | — | — |
| 1886 | H. Binney | Bishop of Nova Scotia | Church of England | — | — |

### Deterministic checks: `binney_hinbert_e1842` vs `Binney, Hibbert___Canada___1877`

- [PASS] surname_gate: bio 'BINNEY' vs stint 'Binney, Hibbert' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
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

