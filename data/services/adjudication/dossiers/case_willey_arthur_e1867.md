<!-- {"case_id": "case_willey_arthur_e1867", "bio_ids": ["willey_arthur_e1867"], "stint_ids": ["Willey, A___Ceylon___1905", "Willey, V. A___Kenya___1927"]} -->
# Dossier case_willey_arthur_e1867

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['willey_arthur_e1867'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Willey, A___Ceylon___1905` is also gate-compatible with biography(ies) outside this case: ['willey_arthur_e1902'] (already linked elsewhere or filtered).
- NOTE: stint `Willey, V. A___Kenya___1927` is also gate-compatible with biography(ies) outside this case: ['willey_arthur_e1902'] (already linked elsewhere or filtered).

## Biography `willey_arthur_e1867`

- Printed name: **WILLEY, ARTHUR**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1912]

### Verbatim printed entry text (OCR)

**Version `col1908-L48195.v` — printed in editions [1908, 1909, 1910, 1912]:**

> WILLEY, ARTHUR.—D.Sc. (Lond.); M.A. (Cantab.); F.R.S.—B. 1867; director of Colombo museum, Ceylon, 25th Apr., 1902; lecturer on biology at Ceylon Med. Coll., 1902-1907; marine biologist, 1907; editor of *Spolin Zeylanica*, 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | F.R.S.—B | — | [1908, 1909, 1910, 1912] |
| 1 | 1902 | director of Colombo museum | Ceylon | [1908, 1909, 1910, 1912] |
| 2 | 1903 | editor of *Spolin Zeylanica* | Ceylon *(inherited from previous clause)* | [1908, 1909, 1910, 1912] |
| 3 | 1907 | marine biologist | Ceylon *(inherited from previous clause)* | [1908, 1909, 1910, 1912] |

## Candidate stint `Willey, A___Ceylon___1905`

- Staff-list name: **Willey, A** | colony: **Ceylon** | listed 1905–1910 | editions [1905, 1906, 1907, 1908, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. Willey | Director of the Colombo Museum | Department of Public Instruction | — | — |
| 1906 | A. Willey | Director of the Colombo Museum | Department of Public Instruction | — | — |
| 1907 | A. Willey | Director of the Colombo Museum | Department of Public Instruction | — | — |
| 1908 | A. Willey | Director of the Colombo Museum | Colombo Museum | — | — |
| 1909 | A. Willey | Director of the Colombo Museum | Colombo Museum | — | — |
| 1910 | A. Willey | Director of the Colombo Museum | Colombo Museum | — | — |

### Deterministic checks: `willey_arthur_e1867` vs `Willey, A___Ceylon___1905`

- [PASS] surname_gate: bio 'WILLEY' vs stint 'Willey, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1905-1910
- [FAIL] position_sim: best 43 vs bar 60: 'editor of *Spolin Zeylanica*' ~ 'Director of the Colombo Museum'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Willey, V. A___Kenya___1927`

- Staff-list name: **Willey, V. A** | colony: **Kenya** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | V. A. Willey | Examining Officer | Customs | — | — |
| 1928 | V. A. Willey | Examining Officer | Customs | — | — |
| 1929 | V. A. Willey | Examining Officer | Customs | — | — |
| 1930 | V. A. Willey | Examining Officer | Customs | — | — |

### Deterministic checks: `willey_arthur_e1867` vs `Willey, V. A___Kenya___1927`

- [PASS] surname_gate: bio 'WILLEY' vs stint 'Willey, V. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['V', 'A']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
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

