<!-- {"case_id": "case_wimbush_michael-douglas_b1905", "bio_ids": ["wimbush_michael-douglas_b1905"], "stint_ids": ["Wimbush, M. D___Nigeria___1936"]} -->
# Dossier case_wimbush_michael-douglas_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wimbush_michael-douglas_b1905`

- Printed name: **WIMBUSH, Michael Douglas**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.B.E
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36966.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WIMBUSH, Michael Douglas, M.B.E.—b. 1905; ed. Haileybury Coll., Herts, and Pangbourne Nautical Coll., Berks., 2nd mates cert., B.O.T.; on mil. serv. 1939-46, capt.; survt., Nig., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | survt. | Nigeria | [1948, 1949, 1950, 1951] |

## Candidate stint `Wimbush, M. D___Nigeria___1936`

- Staff-list name: **Wimbush, M. D** | colony: **Nigeria** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | M. D. Wimbush | Senior Surveyors & Surveyors | Survey Section | — | — |
| 1939 | M. D. Wimbush | Surveyors | Survey Section | — | — |

### Deterministic checks: `wimbush_michael-douglas_b1905` vs `Wimbush, M. D___Nigeria___1936`

- [PASS] surname_gate: bio 'WIMBUSH' vs stint 'Wimbush, M. D' (exact)
- [PASS] initials: bio ['M', 'D'] ~ stint ['M', 'D']
- [PASS] age_gate: stint starts 1936, birth 1905 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1939
- [FAIL] position_sim: best 57 vs bar 60: 'survt.' ~ 'Surveyors'
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

