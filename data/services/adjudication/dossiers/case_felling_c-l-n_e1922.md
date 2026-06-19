<!-- {"case_id": "case_felling_c-l-n_e1922", "bio_ids": ["felling_c-l-n_e1922"], "stint_ids": ["Felling, C. L. N___Kenya___1924"]} -->
# Dossier case_felling_c-l-n_e1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `felling_c-l-n_e1922`

- Printed name: **FELLING, C. L. N**
- Birth year: not printed
- Honours: C.M.G
- Appears in editions: [1924, 1925, 1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1924-L54171.v` — printed in editions [1924, 1925, 1927, 1928]:**

> FELLING, C. L. N., C.M.G.—S. African Ilya.; seconded to Kenya as gen. man., Uganda Ilya., Dec., 1922; mem., leg. coun.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | seconded to Kenya as gen. man., Uganda Ilya | Uganda | [1924, 1925, 1927, 1928] |

## Candidate stint `Felling, C. L. N___Kenya___1924`

- Staff-list name: **Felling, C. L. N** | colony: **Kenya** | listed 1924–1927 | editions [1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | C.L.N. Felling | General Manager | Railway | C.M.G. | — |
| 1925 | C. L. N. Felling | General Manager | Railway | C.M.G. | — |
| 1927 | C.L.N. Felling | General Manager | Railway | C.M.G. | — |

### Deterministic checks: `felling_c-l-n_e1922` vs `Felling, C. L. N___Kenya___1924`

- [PASS] surname_gate: bio 'FELLING' vs stint 'Felling, C. L. N' (exact)
- [PASS] initials: bio ['C', 'L', 'N'] ~ stint ['C', 'L', 'N']
- [PASS] age_gate: stint starts 1924; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
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

