<!-- {"case_id": "case_gill_oscar-sayle_b1880", "bio_ids": ["gill_oscar-sayle_b1880"], "stint_ids": ["Gill, S___Uganda___1927"]} -->
# Dossier case_gill_oscar-sayle_b1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Gill, S___Uganda___1927` is also gate-compatible with biography(ies) outside this case: ['gill_henry-sewell-currier_b1903'] (already linked elsewhere or filtered).

## Biography `gill_oscar-sayle_b1880`

- Printed name: **GILL, OSCAR SAYLE**
- Birth year: 1880 (attested in editions [1933, 1934])
- Appears in editions: [1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1933-L60137.v` — printed in editions [1933, 1934]:**

> GILL, OSCAR SAYLE.—B. 1880; operating engrnr., eleo. dept., Ceylon, Nov., 1927; ch. engrnr. and man., eleo. undertakings, June, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | operating engrnr., eleo. dept. | Ceylon | [1933, 1934] |
| 1 | 1932 | ch. engrnr. and man., eleo. undertakings | Ceylon *(inherited from previous clause)* | [1933, 1934] |

## Candidate stint `Gill, S___Uganda___1927`

- Staff-list name: **Gill, S** | colony: **Uganda** | listed 1927–1933 | editions [1927, 1928, 1929, 1930, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | S. Gill | Drilling Engineer | Geological Survey | — | — |
| 1928 | S. Gill | Drilling Engineer | Geological Survey | — | — |
| 1929 | S. Gill | Drilling Engineer | Geological Survey | — | — |
| 1930 | S. Gill | Drilling Engineer | Geological Survey | — | — |
| 1933 | S. Gill | Drilling Engineer | Drilling Section | — | — |

### Deterministic checks: `gill_oscar-sayle_b1880` vs `Gill, S___Uganda___1927`

- [PASS] surname_gate: bio 'GILL' vs stint 'Gill, S' (exact)
- [PASS] initials: bio ['O', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1927, birth 1880 (age 47)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1933
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

