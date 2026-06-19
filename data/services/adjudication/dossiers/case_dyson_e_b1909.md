<!-- {"case_id": "case_dyson_e_b1909", "bio_ids": ["dyson_e_b1909"], "stint_ids": ["Dyson, E. T___Ceylon___1936"]} -->
# Dossier case_dyson_e_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dyson_e_b1909'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Dyson, E. T___Ceylon___1936` is also gate-compatible with biography(ies) outside this case: ['dyson_edward-trevor_b1892'] (already linked elsewhere or filtered).

## Biography `dyson_e_b1909`

- Printed name: **DYSON, E**
- Birth year: 1909 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L22626.v` — printed in editions [1959, 1960, 1961, 1962]:**

> DYSON, Miss E.—b. 1909; ed. Milton Mount Coll., Crawley, and Manchester Univ.; woman educ. offr., Tang., 1948-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948–1961 | woman educ. offr. | Tanganyika | [1959, 1960, 1961, 1962] |

## Candidate stint `Dyson, E. T___Ceylon___1936`

- Staff-list name: **Dyson, E. T** | colony: **Ceylon** | listed 1936–1940 | editions [1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. T. Dyson | Government Agent | Northern Province | — | — |
| 1937 | E. T. Dyson | Collector | Northern Province | — | — |
| 1937 | E. T. Dyson | Government Agent | NORTHERN PROVINCE | — | — |
| 1940 | E. T. Dyson | Government Agent | Government Agencies | — | — |

### Deterministic checks: `dyson_e_b1909` vs `Dyson, E. T___Ceylon___1936`

- [PASS] surname_gate: bio 'DYSON' vs stint 'Dyson, E. T' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1936, birth 1909 (age 27)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

