<!-- {"case_id": "case_langstone_frank_b1881", "bio_ids": ["langstone_frank_b1881"], "stint_ids": ["Langton, F___Leeward Islands___1906"]} -->
# Dossier case_langstone_frank_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['langstone_frank_b1881'] carry a single initial only — the namesake trap applies.

## Biography `langstone_frank_b1881`

- Printed name: **LANGSTONE, FRANK**
- Birth year: 1881 (attested in editions [1937, 1939])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L62499.v` — printed in editions [1937, 1939]:**

> LANGSTONE, HON. FRANK.—B. 1881; mem., N.Z. H. of R., 1922-25 and since 1928; min. of lands and comsrr. of state forests, 1936.

**Version `col1940-L65964.v` — printed in editions [1940]:**

> LANGSTONE, HON. FRANK.—B. 1881; mem., N.Z. H. of R., 1922-25 and since 1928; min. of lands and comsnr. of state forests, 1935; rep., N.Z., International Lab. Confce., Geneva, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922–1925 | mem., N.Z. H. of R. | New Zealand | [1937, 1939, 1940] |
| 1 | 1928 | mem., N.Z. H. of R. | New Zealand | [1937, 1939] |
| 2 | 1935–1935 | min. of lands and comsnr. of state forests | — | [1940] |
| 3 | 1936 | min. of lands and comsrr. of state forests | — | [1937, 1939] |
| 4 | 1939–1939 | rep., International Lab. Confce., Geneva | New Zealand | [1940] |

## Candidate stint `Langton, F___Leeward Islands___1906`

- Staff-list name: **Langton, F** | colony: **Leeward Islands** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | F. Langton | Operator | Post Office and Telephone Departments | — | — |
| 1907 | F. Langton | Operator | Post Office and Telephone Departments | — | — |
| 1908 | F. Langton | Operators | Post Office and Telephone Departments | — | — |

### Deterministic checks: `langstone_frank_b1881` vs `Langton, F___Leeward Islands___1906`

- [PASS] surname_gate: bio 'LANGSTONE' vs stint 'Langton, F' (fuzzy:2)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1906, birth 1881 (age 25)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
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

