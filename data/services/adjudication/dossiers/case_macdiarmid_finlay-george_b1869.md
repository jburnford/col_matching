<!-- {"case_id": "case_macdiarmid_finlay-george_b1869", "bio_ids": ["macdiarmid_finlay-george_b1869"], "stint_ids": ["MacDiarmid, F. G___Canada___1917", "Macdiarmid, Finlay George___Canada___1915"]} -->
# Dossier case_macdiarmid_finlay-george_b1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macdiarmid_finlay-george_b1869`

- Printed name: **MACDIARMID, FINLAY GEORGE**
- Birth year: 1869 (attested in editions [1917, 1918])
- Terminal: resigned 1919 — “defeated at g.e., Oct., 1919, and resigned portfolio.”
- Appears in editions: [1917, 1918, 1920]

### Verbatim printed entry text (OCR)

**Version `col1917-L51441.v` — printed in editions [1917, 1918]:**

> MACDIARMID, HON. FINLAY GEORGE.—B. 1869; ed. at public schl. and Ridgetown (Ont.) Coll. Inst.; elec. to legis. assem., Ontario, 1898; re-elec., 1902, 1905, 1908, 1911 and 1914; min. of pub. wks., 1914.

**Version `col1920-L55362.v` — printed in editions [1920]:**

> MACDIARMID, HON. FINLAY GEORGE.—B. 1869; ed. at public schl. and Ridgerton (Ont.) Coll. Inst.; elec. to legis. assem., Ontario, 1898; re-elec., 1902, 1906, 1908, 1911 and 1914; min. of pub. wks., 1914; defeated at g.e., Oct., 1919, and resigned portfolio.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1898 | elec. to legis. assem. | Ontario | [1917, 1918, 1920] |
| 1 | 1902–1914 | re-elec. | — | [1917, 1918, 1920] |
| 2 | 1914–1914 | min. of pub. wks. | — | [1917, 1918, 1920] |

## Candidate stint `MacDiarmid, F. G___Canada___1917`

- Staff-list name: **MacDiarmid, F. G** | colony: **Canada** | listed 1917–1918 | editions [1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | F. G. MacDiarmid | Member | Legislative Assembly | — | — |
| 1918 | F. G. MacDiarmid | Member | Legislative Assembly | — | — |

### Deterministic checks: `macdiarmid_finlay-george_b1869` vs `MacDiarmid, F. G___Canada___1917`

- [PASS] surname_gate: bio 'MACDIARMID' vs stint 'MacDiarmid, F. G' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1917, birth 1869 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Macdiarmid, Finlay George___Canada___1915`

- Staff-list name: **Macdiarmid, Finlay George** | colony: **Canada** | listed 1915–1919 | editions [1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | Finlay G. Macdiarmid | Minister | Department of Public Works | — | — |
| 1917 | Finlay G. Macdiarmid | Minister | Public Works | — | — |
| 1917 | Finlay George Macdiarmid | Minister of Public Works | Executive Council | — | — |
| 1918 | Finlay G. Macdiarmid | Minister | Department of Public Works | — | — |
| 1918 | Finlay George Macdiarmid | Minister of Public Works | Executive Council | — | — |
| 1919 | Finlay G. Macdiarmid | Minister | Department of Public Works | — | — |

### Deterministic checks: `macdiarmid_finlay-george_b1869` vs `Macdiarmid, Finlay George___Canada___1915`

- [PASS] surname_gate: bio 'MACDIARMID' vs stint 'Macdiarmid, Finlay George' (exact)
- [PASS] initials: bio ['F', 'G'] ~ stint ['F', 'G']
- [PASS] age_gate: stint starts 1915, birth 1869 (age 46)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1919
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

