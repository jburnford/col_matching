<!-- {"case_id": "case_taples_h-t_e1869", "bio_ids": ["taples_h-t_e1869"], "stint_ids": ["Staples, H. T___Ceylon___1877"]} -->
# Dossier case_taples_h-t_e1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `taples_h-t_e1869` ↔ `Staples, H. T___Ceylon___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Staples, H. T___Ceylon___1877` is also gate-compatible with biography(ies) outside this case: ['staples_h-t_e1869'] (already linked elsewhere or filtered).

## Biography `taples_h-t_e1869`

- Printed name: **TAPLES, H. T**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L36176.v` — printed in editions [1888]:**

> TAPLES, H. T.—Assistant colonial surgeon, medical department, Ceylon, 1869.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Assistant colonial surgeon, medical department | Ceylon | [1888] |

## Candidate stint `Staples, H. T___Ceylon___1877`

- Staff-list name: **Staples, H. T** | colony: **Ceylon** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. T. Staples | Assistant Colonial Surgeons | Medical Department | — | — |
| 1878 | H. T. Staples | Assistant Colonial Surgeons | Medical Department | — | — |
| 1879 | H. T. Staples | Assistant Colonial Surgeons | Medical Department | — | — |
| 1880 | H. T. Staples | Assistant Colonial Surgeons | Medical Department | — | — |
| 1883 | H. T. Staples | Assistant Colonial Surgeon | Medical Department | — | — |
| 1886 | H. T. Staples | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `taples_h-t_e1869` vs `Staples, H. T___Ceylon___1877`

- [PASS] surname_gate: bio 'TAPLES' vs stint 'Staples, H. T' (fuzzy:1)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [PASS] position_sim: best 100 vs bar 60: 'Assistant colonial surgeon, medical department' ~ 'Assistant Colonial Surgeon'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

