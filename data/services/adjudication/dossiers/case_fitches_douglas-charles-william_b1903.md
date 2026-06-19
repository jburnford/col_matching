<!-- {"case_id": "case_fitches_douglas-charles-william_b1903", "bio_ids": ["fitches_douglas-charles-william_b1903"], "stint_ids": ["Fitches, D. C. W___Hong Kong___1937", "Fitches, D. C. W___Hong Kong___1950"]} -->
# Dossier case_fitches_douglas-charles-william_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fitches_douglas-charles-william_b1903`

- Printed name: **FITCHES, Douglas Charles William**
- Birth year: 1903 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L35427.v` — printed in editions [1950, 1951]:**

> FITCHES, Douglas Charles William.—b. 1903; ed. Leicester City Cl. Sch., Cantonese, Mandarin, Hakka, p.o.w., 1941-45; police constab., H.K., 1925; supt., G.P.O., 1936; asst. contrlr., posts, 1947; contrlr., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | police constab. | Hong Kong | [1950, 1951] |
| 1 | 1936 | supt., G.P.O | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1947 | asst. contrlr., posts | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1948 | contrlr | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Fitches, D. C. W___Hong Kong___1937`

- Staff-list name: **Fitches, D. C. W** | colony: **Hong Kong** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | D. Fitches | Assistant Superintendent | Post Office | — | — |
| 1939 | D. C. W. Fitches | Superintendent | Post Office | — | — |
| 1940 | D. C. W. Fitches | Superintendent | Post Office | — | — |

### Deterministic checks: `fitches_douglas-charles-william_b1903` vs `Fitches, D. C. W___Hong Kong___1937`

- [PASS] surname_gate: bio 'FITCHES' vs stint 'Fitches, D. C. W' (exact)
- [PASS] initials: bio ['D', 'C', 'W'] ~ stint ['D', 'C', 'W']
- [PASS] age_gate: stint starts 1937, birth 1903 (age 34)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 37 vs bar 60: 'police constab.' ~ 'Assistant Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Fitches, D. C. W___Hong Kong___1950`

- Staff-list name: **Fitches, D. C. W** | colony: **Hong Kong** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | D. C. W. Fitches | Controller of Posts | General Post Office, Broadcasting and Telecommunications | — | — |
| 1951 | D. C. W. Fitches | Controller of Posts | Post Office | — | — |

### Deterministic checks: `fitches_douglas-charles-william_b1903` vs `Fitches, D. C. W___Hong Kong___1950`

- [PASS] surname_gate: bio 'FITCHES' vs stint 'Fitches, D. C. W' (exact)
- [PASS] initials: bio ['D', 'C', 'W'] ~ stint ['D', 'C', 'W']
- [PASS] age_gate: stint starts 1950, birth 1903 (age 47)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 54 vs bar 60: 'contrlr' ~ 'Controller of Posts'
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

