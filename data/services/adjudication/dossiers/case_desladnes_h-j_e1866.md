<!-- {"case_id": "case_desladnes_h-j_e1866", "bio_ids": ["desladnes_h-j_e1866"], "stint_ids": ["Deslandes, H. J___Ceylon___1877", "Deslandes, H. J___Ceylon___1886"]} -->
# Dossier case_desladnes_h-j_e1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Deslandes, H. J___Ceylon___1877` is also gate-compatible with biography(ies) outside this case: ['deslandes_h-j_e1866'] (already linked elsewhere or filtered).
- NOTE: stint `Deslandes, H. J___Ceylon___1886` is also gate-compatible with biography(ies) outside this case: ['deslandes_h-j_e1866'] (already linked elsewhere or filtered).

## Biography `desladnes_h-j_e1866`

- Printed name: **DESLADNES, H. J**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27166.v` — printed in editions [1883]:**

> DESLADNES, H. J.—Superintending office, public works department, Ceylon, 1866; draftsman and framer of estimates, 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Superintending office, public works department | Ceylon | [1883] |
| 1 | 1870 | draftsman and framer of estimates | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Deslandes, H. J___Ceylon___1877`

- Staff-list name: **Deslandes, H. J** | colony: **Ceylon** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. J. Deslandes | Draftsmen and Framers of Estimates | Public Works Department | — | — |
| 1878 | H. J. Deslandes | Draftsman and Framer of Estimates | Public Works Department | — | — |

### Deterministic checks: `desladnes_h-j_e1866` vs `Deslandes, H. J___Ceylon___1877`

- [PASS] surname_gate: bio 'DESLADNES' vs stint 'Deslandes, H. J' (fuzzy:2)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1878
- [PASS] position_sim: best 100 vs bar 60: 'draftsman and framer of estimates' ~ 'Draftsman and Framer of Estimates'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Deslandes, H. J___Ceylon___1886`

- Staff-list name: **Deslandes, H. J** | colony: **Ceylon** | listed 1886–1894 | editions [1886, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | H. J. Deslandes | Provl. Assistant | Public Works Department | — | — |
| 1889 | H. J. Deslandes | Provl. Engineer, Western Province | Public Works Department | — | — |
| 1890 | H. J. Deslandes | Provl. Engineer | Public Works Department | — | — |
| 1894 | H. J. Deslandes | Provl. Engineer, Southern Province | Public Works Department | — | — |

### Deterministic checks: `desladnes_h-j_e1866` vs `Deslandes, H. J___Ceylon___1886`

- [PASS] surname_gate: bio 'DESLADNES' vs stint 'Deslandes, H. J' (fuzzy:2)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1894
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

