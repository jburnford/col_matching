<!-- {"case_id": "case_cumaraswamy_subramaniam-david_b1904", "bio_ids": ["cumaraswamy_subramaniam-david_b1904", "jumaraswamy_subramaniam-davids_b1904"], "stint_ids": ["Cumaraswamy, S. D___Ceylon___1937"]} -->
# Dossier case_cumaraswamy_subramaniam-david_b1904

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Cumaraswamy, S. D___Ceylon___1937'] have more than one claimant biography in this case.
- NOTE: stint `Cumaraswamy, S. D___Ceylon___1937` is also gate-compatible with biography(ies) outside this case: ['cumaraswamy_subramanian-davids_b1904'] (already linked elsewhere or filtered).
- NOTE: stint `Cumaraswamy, S. D___Ceylon___1937` is also gate-compatible with biography(ies) outside this case: ['cumaraswamy_subramanian-davids_b1904'] (already linked elsewhere or filtered).

## Biography `cumaraswamy_subramaniam-david_b1904`

- Printed name: **CUMARASWAMY, Subramaniam David**
- Birth year: 1904 (attested in editions [1930])
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L63724.v` — printed in editions [1930]:**

> CUMARASWAMY, Subramaniam David.—B. 1904; cadet, Ceylon civ. serv., 1929; atttd., Badulla kach, Feb., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet, Ceylon civ. serv | Ceylon | [1930] |

## Biography `jumaraswamy_subramaniam-davids_b1904`

- Printed name: **JUMARASWAMY, SUBRAMANIAM DAVIDS**
- Birth year: 1904 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63508.v` — printed in editions [1940]:**

> JUMARASWAMY, SUBRAMANIAM DAVIDS, B.A. (Lond.).—B. 1904; cadet, Ceylon civ. serv., 1929; attd. Badulla kach, Feb., 1929; attd. Batticaloa kach Jan., 1930; office asst. to asst. gov't agt., Matale, Mar., 1930; attd., Kandy kach., Sept., 1933; office asst., Kandy kach., Feb., 1934; addnl. asst. gov't agt., Matara and Hambantota, Oct., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet, Ceylon civ. serv | Ceylon | [1940] |
| 1 | 1930 | attd. Batticaloa kach | Ceylon *(inherited from previous clause)* | [1940] |
| 2 | 1933 | attd., Kandy kach | Ceylon *(inherited from previous clause)* | [1940] |
| 3 | 1934 | office asst., Kandy kach | Ceylon *(inherited from previous clause)* | [1940] |
| 4 | 1936 | addnl. asst. gov't agt., Matara and Hambantota | Ceylon *(inherited from previous clause)* | [1940] |

## Candidate stint `Cumaraswamy, S. D___Ceylon___1937`

- Staff-list name: **Cumaraswamy, S. D** | colony: **Ceylon** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | S. D. Cumaraswamy | Office Assistant | CENTRAL PROVINCE | — | — |
| 1940 | S. D. Cumaraswamy | Additional Duty Controller | Department of Labour | — | — |

### Deterministic checks: `cumaraswamy_subramaniam-david_b1904` vs `Cumaraswamy, S. D___Ceylon___1937`

- [PASS] surname_gate: bio 'CUMARASWAMY' vs stint 'Cumaraswamy, S. D' (exact)
- [PASS] initials: bio ['S', 'D'] ~ stint ['S', 'D']
- [PASS] age_gate: stint starts 1937, birth 1904 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 38 vs bar 60: 'cadet, Ceylon civ. serv' ~ 'Additional Duty Controller'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `jumaraswamy_subramaniam-davids_b1904` vs `Cumaraswamy, S. D___Ceylon___1937`

- [PASS] surname_gate: bio 'JUMARASWAMY' vs stint 'Cumaraswamy, S. D' (fuzzy:1)
- [PASS] initials: bio ['S', 'D'] ~ stint ['S', 'D']
- [PASS] age_gate: stint starts 1937, birth 1904 (age 33)
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [PASS] position_sim: best 68 vs bar 60: 'office asst., Kandy kach' ~ 'Office Assistant'
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

