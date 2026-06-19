<!-- {"case_id": "case_bickneill_h-j_e1860", "bio_ids": ["bickneill_h-j_e1860"], "stint_ids": ["Bicknell, H. J___Jamaica___1877", "Bucknell, H___Ceylon___1896"]} -->
# Dossier case_bickneill_h-j_e1860

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `bickneill_h-j_e1860` ↔ `Bicknell, H. J___Jamaica___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Bicknell, H. J___Jamaica___1877` is also gate-compatible with biography(ies) outside this case: ['bicknell_h-j_e1860'] (already linked elsewhere or filtered).

## Biography `bickneill_h-j_e1860`

- Printed name: **BICKNEILL, H. J**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L30331.v` — printed in editions [1894]:**

> BICKNEILL, H. J.—Police magistrate, Kingston, Jamaica, Mar., 1860; acting judge, eastern district, Oct., 1882; R.M., St. Catherine, April, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | Police magistrate, Kingston | Jamaica | [1894] |
| 1 | 1882 | acting judge, eastern district | Jamaica *(inherited from previous clause)* | [1894] |
| 2 | 1888 | R.M., St. Catherine | Jamaica *(inherited from previous clause)* | [1894] |

## Candidate stint `Bicknell, H. J___Jamaica___1877`

- Staff-list name: **Bicknell, H. J** | colony: **Jamaica** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1878 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1879 | H. J. Bicknell | Police Magistrate | District Courts | — | — |
| 1880 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1883 | H. J. Bicknell | Police Magistrate, Kingston | Judicial Establishment | — | — |
| 1886 | H. J. Bicknell | Police Magistrate | District Courts | — | — |
| 1888 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1889 | H. J. Bicknell | Resident Magistrate | Resident Magistrates | — | — |
| 1890 | H. J. Bicknell, Esq. | Resident Magistrate | Judicial Establishment | — | — |

### Deterministic checks: `bickneill_h-j_e1860` vs `Bicknell, H. J___Jamaica___1877`

- [PASS] surname_gate: bio 'BICKNEILL' vs stint 'Bicknell, H. J' (fuzzy:1)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1877-1890
- [PASS] position_sim: best 100 vs bar 60: 'Police magistrate, Kingston' ~ 'Police Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Bucknell, H___Ceylon___1896`

- Staff-list name: **Bucknell, H** | colony: **Ceylon** | listed 1896–1898 | editions [1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | H. Bucknell | District Engineer, 1st Grade | Public Works Department | — | — |
| 1898 | H. Bucknell | District Engineer, 1st Grade | Public Works Department | — | — |

### Deterministic checks: `bickneill_h-j_e1860` vs `Bucknell, H___Ceylon___1896`

- [PASS] surname_gate: bio 'BICKNEILL' vs stint 'Bucknell, H' (fuzzy:2)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
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

