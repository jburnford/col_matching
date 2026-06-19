<!-- {"case_id": "case_hopper_harold-lancelot_b1896", "bio_ids": ["hopper_harold-lancelot_b1896", "hopper_harold-langllot_b1896"], "stint_ids": ["Hopper, H. L___Ceylon___1922"]} -->
# Dossier case_hopper_harold-lancelot_b1896

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Hopper, H. L___Ceylon___1922'] have more than one claimant biography in this case.

## Biography `hopper_harold-lancelot_b1896`

- Printed name: **HOPPER, HAROLD LANCELOT**
- Birth year: 1896 (attested in editions [1922])
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L53230.v` — printed in editions [1922]:**

> HOPPER, HAROLD LANCELOT, B.A. (Oxon).—B. 1896; cadet, Ceylon civ. serv., Aug., 1921; attld. Ratnapura Kach., Sept., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cadet, Ceylon civ. serv | Ceylon | [1922] |

## Biography `hopper_harold-langllot_b1896`

- Printed name: **HOPPER, HAROLD LANGLLOT**
- Birth year: 1896 (attested in editions [1923, 1924, 1925])
- Appears in editions: [1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1923-L55320.v` — printed in editions [1923, 1924, 1925]:**

> HOPPER, HAROLD LANGLLOT, B.A. (Oxon).—B. 1896; on mil. serv., Aug., 1915; cadet, Ceylon civ. serv., Aug., 1921; attd., Ratnapura Kach., Sept., 1921; attd., Colombo Kachcheri, July, 1922; ag. office astt. to govt. agt., Prov. of Sabaragamuwa, Sept., 1922; ag. office astt. to govt. agt., N.W. Prov., Apr., 1923; pol. mag., Dandagamuwa, Feb., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cadet, Ceylon civ. serv | Ceylon | [1923, 1924, 1925] |
| 1 | 1922 | attd., Colombo Kachcheri | Ceylon *(inherited from previous clause)* | [1923, 1924, 1925] |
| 2 | 1923 | ag. office astt. to govt. agt., N.W. Prov | Ceylon *(inherited from previous clause)* | [1923, 1924, 1925] |
| 3 | 1924 | pol. mag., Dandagamuwa | Ceylon *(inherited from previous clause)* | [1923, 1924, 1925] |

## Candidate stint `Hopper, H. L___Ceylon___1922`

- Staff-list name: **Hopper, H. L** | colony: **Ceylon** | listed 1922–1925 | editions [1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. L. Hopper | Cudets | Civil Establishment | — | — |
| 1925 | H. L. Hopper | Commissioner of Requests, Police Magistrate | Judicial Establishment | — | — |

### Deterministic checks: `hopper_harold-lancelot_b1896` vs `Hopper, H. L___Ceylon___1922`

- [PASS] surname_gate: bio 'HOPPER' vs stint 'Hopper, H. L' (exact)
- [PASS] initials: bio ['H', 'L'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 37 vs bar 60: 'cadet, Ceylon civ. serv' ~ 'Cudets'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `hopper_harold-langllot_b1896` vs `Hopper, H. L___Ceylon___1922`

- [PASS] surname_gate: bio 'HOPPER' vs stint 'Hopper, H. L' (exact)
- [PASS] initials: bio ['H', 'L'] ~ stint ['H', 'L']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 42 vs bar 60: 'ag. office astt. to govt. agt., N.W. Prov' ~ 'Commissioner of Requests, Police Magistrate'
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

