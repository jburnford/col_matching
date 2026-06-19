<!-- {"case_id": "case_gunartna_walter-dandris_b1904", "bio_ids": ["gunartna_walter-dandris_b1904"], "stint_ids": ["Gunaratna, W. D___Ceylon___1931", "Gunaratne, W. D___Ceylon___1936"]} -->
# Dossier case_gunartna_walter-dandris_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gunartna_walter-dandris_b1904`

- Printed name: **GUNARTNA, WALTER DANDRIS**
- Birth year: 1904 (attested in editions [1930])
- Appears in editions: [1929, 1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L64968.v` — printed in editions [1930]:**

> GUNARTNA, WALTER DANDRIS, B.Sc. (Lond.).—B. 1904; cadet, Ceylon civ. serv., Dec., 1927; attd., Galle kach., Jan., 1928; attd., Kandy kach., May, 1928; ag. pol. mag., Dumbars, Dec., 1928 to Jan., 1929; extra office astt., Batticaloa kach., Jan., 1929.

**Version `col1929-L60770.v` — printed in editions [1929]:**

> GUNARATNA, Walter Dandris, B.Sc. (Lond.)—B. 1904; cadet, Ceylon civ. serv., Dec., 1927; attd., Galle kach., Jan., 1928; attd., Kandy kach., May, 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet, Ceylon civ. serv | Ceylon | [1929, 1930] |
| 1 | 1928 | attd., Galle kach | Ceylon *(inherited from previous clause)* | [1929, 1930] |
| 2 | 1929 | extra office astt., Batticaloa kach | Ceylon *(inherited from previous clause)* | [1930] |

## Candidate stint `Gunaratna, W. D___Ceylon___1931`

- Staff-list name: **Gunaratna, W. D** | colony: **Ceylon** | listed 1931–1936 | editions [1931, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | W. D. Gunaratna | Office Assistant | Government Agencies | — | — |
| 1934 | W. D. Gunaratna | Office Assistant | PROVINCE OF UVA | — | — |
| 1936 | W. D. Gunaratna | Assistant Government Agent | Southern Province | — | — |

### Deterministic checks: `gunartna_walter-dandris_b1904` vs `Gunaratna, W. D___Ceylon___1931`

- [PASS] surname_gate: bio 'GUNARTNA' vs stint 'Gunaratna, W. D' (fuzzy:1)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1931, birth 1904 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1936
- [FAIL] position_sim: best 55 vs bar 60: 'extra office astt., Batticaloa kach' ~ 'Office Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Gunaratne, W. D___Ceylon___1936`

- Staff-list name: **Gunaratne, W. D** | colony: **Ceylon** | listed 1936–1940 | editions [1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. D. Gunaratne (A.G.A.) | Assistant Collector and Landing Surveyor | Southern Province | — | — |
| 1937 | W. D. Gunaratne | Assistant Collector and Landing Surveyor | Southern Province | — | — |
| 1937 | W. D. Gunaratne | Assistant Government Agent | SOUTHERN PROVINCE | — | — |
| 1940 | W. D. Gunaratne | Assistant Collector and Landing Surveyor | Northern Province | — | — |

### Deterministic checks: `gunartna_walter-dandris_b1904` vs `Gunaratne, W. D___Ceylon___1936`

- [PASS] surname_gate: bio 'GUNARTNA' vs stint 'Gunaratne, W. D' (fuzzy:2)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1936, birth 1904 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 38 vs bar 60: 'extra office astt., Batticaloa kach' ~ 'Assistant Collector and Landing Surveyor'
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

