<!-- {"case_id": "case_kanagasundaram_kathirvaloo_b1912", "bio_ids": ["kanagasundaram_kathirvaloo_b1912", "kanagasundaram_kathirvaloog_b1912"], "stint_ids": ["Kanagasundaram, K___Ceylon___1937"]} -->
# Dossier case_kanagasundaram_kathirvaloo_b1912

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['kanagasundaram_kathirvaloo_b1912', 'kanagasundaram_kathirvaloog_b1912'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Kanagasundaram, K___Ceylon___1937'] have more than one claimant biography in this case.
- NOTE: stint `Kanagasundaram, K___Ceylon___1937` is also gate-compatible with biography(ies) outside this case: ['kanagasundaram_kathiravaloo_b1912'] (already linked elsewhere or filtered).
- NOTE: stint `Kanagasundaram, K___Ceylon___1937` is also gate-compatible with biography(ies) outside this case: ['kanagasundaram_kathiravaloo_b1912'] (already linked elsewhere or filtered).

## Biography `kanagasundaram_kathirvaloo_b1912`

- Printed name: **KANAGASUNDARAM, Kathirvaloo**
- Birth year: 1912 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L68084.v` — printed in editions [1939]:**

> KANAGASUNDARAM, Kathirvaloo, B.A. (hons.), Lond.—B. 1912; cadet, Ceylon civ. serv., Jan., 1935; office asst., Hambantota kach., Nov., 1935; pol. mag., Kandy, Mar., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | cadet, Ceylon civ. serv | Ceylon | [1939] |
| 1 | 1937 | pol. mag., Kandy | Ceylon *(inherited from previous clause)* | [1939] |

## Biography `kanagasundaram_kathirvaloog_b1912`

- Printed name: **KANAGASUNDARAM, KATHIRVALOOG**
- Birth year: 1912 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L62270.v` — printed in editions [1937]:**

> KANAGASUNDARAM, KATHIRVALOOG, B.A. (hons.) Lond.—B. 1912; cadet, Ceylon civ. serv., Jan., 1935; office asst., Hambantota kach., Nov., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | cadet, Ceylon civ. serv | Ceylon | [1937] |

## Candidate stint `Kanagasundaram, K___Ceylon___1937`

- Staff-list name: **Kanagasundaram, K** | colony: **Ceylon** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | K. Kanagasundaram | Office Assistant | SOUTHERN PROVINCE | — | — |
| 1940 | K. Kanagasundaram | Assistant Government Agent | PROVINCE OF SARAGAMUWA | — | — |

### Deterministic checks: `kanagasundaram_kathirvaloo_b1912` vs `Kanagasundaram, K___Ceylon___1937`

- [PASS] surname_gate: bio 'KANAGASUNDARAM' vs stint 'Kanagasundaram, K' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1937, birth 1912 (age 25)
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 38 vs bar 60: 'cadet, Ceylon civ. serv' ~ 'Assistant Government Agent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `kanagasundaram_kathirvaloog_b1912` vs `Kanagasundaram, K___Ceylon___1937`

- [PASS] surname_gate: bio 'KANAGASUNDARAM' vs stint 'Kanagasundaram, K' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1937, birth 1912 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 38 vs bar 60: 'cadet, Ceylon civ. serv' ~ 'Assistant Government Agent'
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

