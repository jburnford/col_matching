<!-- {"case_id": "case_sanderson_reginald-woolley_b1897", "bio_ids": ["sanderson_reginald-woolley_b1897"], "stint_ids": ["Sanderson, R. W___Gold Coast___1927", "Sanderson, R. W___Gold Coast___1934"]} -->
# Dossier case_sanderson_reginald-woolley_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sanderson_reginald-woolley_b1897`

- Printed name: **SANDERSON, REGINALD WOOLLEY**
- Birth year: 1897 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L68202.v` — printed in editions [1940]:**

> SANDERSON, REGINALD WOOLLEY.—B.1897; ed. Leeds Grammar Schol. and Christ Ch., Oxford; war serv., France, 1916-18; asst. D.C., Gold Coast, Sept., 1921; D.C., Jan., 1925; seconded as dep. ch. inspr., lab., July, 1939; ag. ch. inspr., lab., July, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | asst. D.C. | Gold Coast | [1940] |
| 1 | 1925 | D.C | Gold Coast *(inherited from previous clause)* | [1940] |
| 2 | 1939 | seconded as dep. ch. inspr., lab | Gold Coast *(inherited from previous clause)* | [1940] |

## Candidate stint `Sanderson, R. W___Gold Coast___1927`

- Staff-list name: **Sanderson, R. W** | colony: **Gold Coast** | listed 1927–1929 | editions [1927, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | R. W. Sanderson | District Commissioner | Administrative and Political Service | — | — |
| 1929 | R. W. Sanderson | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |

### Deterministic checks: `sanderson_reginald-woolley_b1897` vs `Sanderson, R. W___Gold Coast___1927`

- [PASS] surname_gate: bio 'SANDERSON' vs stint 'Sanderson, R. W' (exact)
- [PASS] initials: bio ['R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1927, birth 1897 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [FAIL] position_sim: best 17 vs bar 60: 'D.C' ~ 'District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Sanderson, R. W___Gold Coast___1934`

- Staff-list name: **Sanderson, R. W** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | R. W. Sanderson | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | R. W. Sanderson | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `sanderson_reginald-woolley_b1897` vs `Sanderson, R. W___Gold Coast___1934`

- [PASS] surname_gate: bio 'SANDERSON' vs stint 'Sanderson, R. W' (exact)
- [PASS] initials: bio ['R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1934, birth 1897 (age 37)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 17 vs bar 60: 'D.C' ~ 'District Commissioner'
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

