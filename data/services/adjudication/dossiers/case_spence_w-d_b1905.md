<!-- {"case_id": "case_spence_w-d_b1905", "bio_ids": ["spence_w-d_b1905"], "stint_ids": ["Spence, W. D___Nigeria___1934"]} -->
# Dossier case_spence_w-d_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `spence_w-d_b1905`

- Printed name: **SPENCE, W. D**
- Birth year: 1905 (attested in editions [1953])
- Appears in editions: [1953]

### Verbatim printed entry text (OCR)

**Version `col1953-L19106.v` — printed in editions [1953]:**

> SPENCE, W. D.—b. 1905; ed. Hampton Gram. Sch. and Edin. Univ.; cadet, Nig., 1930; admin. offr., cl. II., 1947; cl. I., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | cadet | Nigeria | [1953] |
| 1 | 1947 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1953] |
| 2 | 1951 | cl. I | Nigeria *(inherited from previous clause)* | [1953] |

## Candidate stint `Spence, W. D___Nigeria___1934`

- Staff-list name: **Spence, W. D** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | W. D. Spence | — | Administrative Service | — | — |
| 1939 | W. D. Spence | Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |

### Deterministic checks: `spence_w-d_b1905` vs `Spence, W. D___Nigeria___1934`

- [PASS] surname_gate: bio 'SPENCE' vs stint 'Spence, W. D' (exact)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1934, birth 1905 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 25 vs bar 60: 'cadet' ~ 'Assistant Secretary'
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

