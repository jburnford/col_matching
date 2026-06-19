<!-- {"case_id": "case_coulson_j-f_e1866", "bio_ids": ["coulson_j-f_e1866"], "stint_ids": ["Coulson, J. F___Ceylon___1877"]} -->
# Dossier case_coulson_j-f_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coulson_j-f_e1866`

- Printed name: **COULSON, J. F**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26969.v` — printed in editions [1883]:**

> COULSON, J. F.—Superintending officer, public works department, Ceylon, 1866; acting estimator and draftsman, 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Superintending officer, public works department | Ceylon | [1883] |
| 1 | 1872 | acting estimator and draftsman | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Coulson, J. F___Ceylon___1877`

- Staff-list name: **Coulson, J. F** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. F. Coulson | Superintending Officer | Public Works Department | — | — |
| 1878 | J. F. Coulson | Superintending Officer | Public Works Department | — | — |
| 1879 | J. F. Coulson | Superintending Officer | Superintending Officers | — | — |
| 1880 | J. F. Coulson | Superintending Officer | Public Works Department | — | — |

### Deterministic checks: `coulson_j-f_e1866` vs `Coulson, J. F___Ceylon___1877`

- [PASS] surname_gate: bio 'COULSON' vs stint 'Coulson, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 23 vs bar 60: 'acting estimator and draftsman' ~ 'Superintending Officer'
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

