<!-- {"case_id": "case_little_francis-edward_b1884", "bio_ids": ["little_francis-edward_b1884"], "stint_ids": ["Little, F. E___Tanganyika___1921", "Little, F. E___Tanganyika___1933"]} -->
# Dossier case_little_francis-edward_b1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `little_francis-edward_b1884`

- Printed name: **LITTLE, Francis Edward**
- Birth year: 1884 (attested in editions [1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66166.v` — printed in editions [1940]:**

> LITTLE, Francis Edward.—B. 1884; Natal pol., 1909-13; S.M.R., 1913-19; Tanganyika Territory pol., 1919; asst. supt., 1920; supt., 1928; Col. Police Medal, 1939.

**Version `col1939-L68674.v` — printed in editions [1939]:**

> LITTLE, FRANCIS EDWARD.—B. 1884; Natal pol., 1909-13; S.M.R., 1913-19; Tanganyika Terr. tory pol., 1919; asst. supr., 1920; supt., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909–1913 | Natal pol | Natal | [1939, 1940] |
| 1 | 1913–1919 | S.M.R | Natal *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1919 | Tanganyika Territory pol | Tanganyika | [1939, 1940] |
| 3 | 1920 | asst. supt | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1928 | supt | Tanganyika *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1939 | Col. Police Medal | Tanganyika *(inherited from previous clause)* | [1940] |

## Candidate stint `Little, F. E___Tanganyika___1921`

- Staff-list name: **Little, F. E** | colony: **Tanganyika** | listed 1921–1925 | editions [1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | F. E. Little | Pay and Quartermaster | Police and Prisons Department | — | — |
| 1922 | F. E. Little | Pay and Quartermaster | Police and Prisons Department | — | — |
| 1923 | F. E. Little | Pay and Quartermaster | Police and Prisons Department | — | — |
| 1924 | F. E. Little | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1925 | F. E. Little | Assistant District Superintendent | Police and Prisons Department | — | — |

### Deterministic checks: `little_francis-edward_b1884` vs `Little, F. E___Tanganyika___1921`

- [PASS] surname_gate: bio 'LITTLE' vs stint 'Little, F. E' (exact)
- [PASS] initials: bio ['F', 'E'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1921, birth 1884 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1921-1925
- [FAIL] position_sim: best 44 vs bar 60: 'Tanganyika Territory pol' ~ 'Pay and Quartermaster'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Little, F. E___Tanganyika___1933`

- Staff-list name: **Little, F. E** | colony: **Tanganyika** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | F. E. Little | Superintendent | Police | — | — |
| 1934 | F. E. Little | Superintendents | Police | — | — |

### Deterministic checks: `little_francis-edward_b1884` vs `Little, F. E___Tanganyika___1933`

- [PASS] surname_gate: bio 'LITTLE' vs stint 'Little, F. E' (exact)
- [PASS] initials: bio ['F', 'E'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1933, birth 1884 (age 49)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1934
- [FAIL] position_sim: best 44 vs bar 60: 'supt' ~ 'Superintendent'
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

