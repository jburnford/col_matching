<!-- {"case_id": "case_gilchrist_arthur-george_b1870", "bio_ids": ["gilchrist_arthur-george_b1870"], "stint_ids": ["Gilchrist, G___Ceylon___1919", "Gilchrist, G___Ceylon___1927"]} -->
# Dossier case_gilchrist_arthur-george_b1870

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gilchrist_arthur-george_b1870`

- Printed name: **GILCHRIST, ARTHUR GEORGE**
- Birth year: 1870 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64536.v` — printed in editions [1940]:**

> GILCHRIST, ARTHUR GEORGE.—B. 1870; pres., State superannuation bd., N.S.W., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | pres., State superannuation bd. | New South Wales | [1940] |

## Candidate stint `Gilchrist, G___Ceylon___1919`

- Staff-list name: **Gilchrist, G** | colony: **Ceylon** | listed 1919–1922 | editions [1919, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | G. Gilchrist | District Engineer | Public Works Department | — | — |
| 1921 | G. Gilchrist | District Engineer | District Engineers | — | — |
| 1922 | G. Gilchrist | District Engineer | District Engineers | — | — |

### Deterministic checks: `gilchrist_arthur-george_b1870` vs `Gilchrist, G___Ceylon___1919`

- [PASS] surname_gate: bio 'GILCHRIST' vs stint 'Gilchrist, G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1919, birth 1870 (age 49)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gilchrist, G___Ceylon___1927`

- Staff-list name: **Gilchrist, G** | colony: **Ceylon** | listed 1927–1929 | editions [1927, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | G. Gilchrist | District Engineer | District Engineers | — | — |
| 1929 | G. Gilchrist | District Engineer | Government Factory | — | — |

### Deterministic checks: `gilchrist_arthur-george_b1870` vs `Gilchrist, G___Ceylon___1927`

- [PASS] surname_gate: bio 'GILCHRIST' vs stint 'Gilchrist, G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1927, birth 1870 (age 57)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1929
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

