<!-- {"case_id": "case_dirckze_peroval-titus-lindon-laurie_b1883", "bio_ids": ["dirckze_peroval-titus-lindon-laurie_b1883"], "stint_ids": ["Dirckze, P. T. L. L___Ceylon___1937"]} -->
# Dossier case_dirckze_peroval-titus-lindon-laurie_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dirckze_peroval-titus-lindon-laurie_b1883`

- Printed name: **DIRCKZE, PEROVAL TITUS LINDON LAURIE**
- Birth year: 1883 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L66287.v` — printed in editions [1939]:**

> DIRCKZE, PEROVAL TITUS LINDON LAURIE.—B. 1883; survey dept., Ceylon, 1901; asst. inspr., mines, Jan., 1908; asst. engnr., P.W.D., 1928; govt. mineralogist May, 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | survey dept. | Ceylon | [1939] |
| 1 | 1908 | asst. inspr., mines | Ceylon *(inherited from previous clause)* | [1939] |
| 2 | 1928 | asst. engnr., P.W.D | Ceylon *(inherited from previous clause)* | [1939] |
| 3 | 1934 | govt. mineralogist | Ceylon *(inherited from previous clause)* | [1939] |

## Candidate stint `Dirckze, P. T. L. L___Ceylon___1937`

- Staff-list name: **Dirckze, P. T. L. L** | colony: **Ceylon** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | P. T. L. L. Dirckze | Government Mineralogist (acting) (also Inspector of Mines) | Department of Salt and Mineralogy | — | — |
| 1940 | P. T. Dirckze | Inspector of Mines | Department of Salt | — | — |

### Deterministic checks: `dirckze_peroval-titus-lindon-laurie_b1883` vs `Dirckze, P. T. L. L___Ceylon___1937`

- [PASS] surname_gate: bio 'DIRCKZE' vs stint 'Dirckze, P. T. L. L' (exact)
- [PASS] initials: bio ['P', 'T', 'L', 'L'] ~ stint ['P', 'T', 'L', 'L']
- [PASS] age_gate: stint starts 1937, birth 1883 (age 54)
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [PASS] position_sim: best 83 vs bar 60: 'govt. mineralogist' ~ 'Government Mineralogist (acting) (also Inspector of Mines)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

