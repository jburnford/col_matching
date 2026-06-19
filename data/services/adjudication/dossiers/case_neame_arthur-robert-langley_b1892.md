<!-- {"case_id": "case_neame_arthur-robert-langley_b1892", "bio_ids": ["neame_arthur-robert-langley_b1892"], "stint_ids": ["Neame, A. R. L___Tanganyika___1921", "Neame, A. R. L___Tanganyika___1933"]} -->
# Dossier case_neame_arthur-robert-langley_b1892

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `neame_arthur-robert-langley_b1892`

- Printed name: **NEAME, ARTHUR ROBERT LANGLEY**
- Birth year: 1892 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67027.v` — printed in editions [1940]:**

> NEAME, ARTHUR ROBERT LANGLEY.—B.1892; B.S.A. pol., 1912-19; asst. supt., Tanganyika Territory pol., 1920; supt., 1928; ag. dep. comsr., 1933-34.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912–1919 | B.S.A. pol | — | [1940] |
| 1 | 1920 | asst. supt., Tanganyika Territory pol | Tanganyika | [1940] |
| 2 | 1928 | supt | Tanganyika *(inherited from previous clause)* | [1940] |
| 3 | 1933–1934 | ag. dep. comsr | Tanganyika *(inherited from previous clause)* | [1940] |

## Candidate stint `Neame, A. R. L___Tanganyika___1921`

- Staff-list name: **Neame, A. R. L** | colony: **Tanganyika** | listed 1921–1925 | editions [1921, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | A. R. L. Neame | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1922 | A. R. L. Neame | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1923 | A. R. L. Neame | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1924 | A. R. L. Neame | Assistant District Superintendent | Police and Prisons Department | — | — |
| 1925 | A. R. L. Neame | Assistant District Superintendent | Police and Prisons Department | — | — |

### Deterministic checks: `neame_arthur-robert-langley_b1892` vs `Neame, A. R. L___Tanganyika___1921`

- [PASS] surname_gate: bio 'NEAME' vs stint 'Neame, A. R. L' (exact)
- [PASS] initials: bio ['A', 'R', 'L'] ~ stint ['A', 'R', 'L']
- [PASS] age_gate: stint starts 1921, birth 1892 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1925
- [FAIL] position_sim: best 39 vs bar 60: 'asst. supt., Tanganyika Territory pol' ~ 'Assistant District Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Neame, A. R. L___Tanganyika___1933`

- Staff-list name: **Neame, A. R. L** | colony: **Tanganyika** | listed 1933–1940 | editions [1933, 1934, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | A. R. L. Neame | Superintendent | Police | — | — |
| 1934 | A. R. L. Neame | Superintendents | Police | — | — |
| 1940 | A. R. L. Neame | Superintendents | Police Department | — | — |

### Deterministic checks: `neame_arthur-robert-langley_b1892` vs `Neame, A. R. L___Tanganyika___1933`

- [PASS] surname_gate: bio 'NEAME' vs stint 'Neame, A. R. L' (exact)
- [PASS] initials: bio ['A', 'R', 'L'] ~ stint ['A', 'R', 'L']
- [PASS] age_gate: stint starts 1933, birth 1892 (age 41)
- [PASS] colony: 3 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1940
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

