<!-- {"case_id": "case_gwynne_e-castres_e1851", "bio_ids": ["gwynne_e-castres_e1851"], "stint_ids": ["Gwynne, E. C___South Australia___1877"]} -->
# Dossier case_gwynne_e-castres_e1851

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gwynne_e-castres_e1851`

- Printed name: **GWYNNE, E. CASTRES**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27806.v` — printed in editions [1883]:**

> GWYNNE, E. CASTRES.—Nominee member of legislative council, S. Australia, from Aug. 1851 to 1856; elected and served as member of the legislative council Oct. 1856, to Oct. 1859; attorney-general, 1857; third judge, March 1859; second judge and primary judge in equity, 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851–1856 | Nominee member of legislative council | S. Australia | [1883] |
| 1 | 1856–1859 | member of the legislative council | — | [1883] |
| 2 | 1857 | attorney-general | — | [1883] |
| 3 | 1859 | third judge | — | [1883] |
| 4 | 1867 | second judge and primary judge in equity | — | [1883] |

## Candidate stint `Gwynne, E. C___South Australia___1877`

- Staff-list name: **Gwynne, E. C** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. C. Gwynne | Second Judge | Supreme Court | — | — |
| 1878 | E. C. Gwynne | Second Judge | Judges of the Supreme Court | — | — |
| 1879 | E. C. Gwynne | Second Judge | JUDGES OF THE SUPREME COURT | — | — |
| 1880 | E. C. Gwynne | Second Judge | Judges of the Supreme Court | — | — |

### Deterministic checks: `gwynne_e-castres_e1851` vs `Gwynne, E. C___South Australia___1877`

- [PASS] surname_gate: bio 'GWYNNE' vs stint 'Gwynne, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
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

