<!-- {"case_id": "case_pugh_william-robert-bernard_b1907", "bio_ids": ["pugh_william-robert-bernard_b1907"], "stint_ids": ["Pugh, W. R. B___Kenya___1936"]} -->
# Dossier case_pugh_william-robert-bernard_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pugh_william-robert-bernard_b1907`

- Printed name: **PUGH, William Robert Bernard**
- Birth year: 1907 (attested in editions [1950, 1951])
- Honours: K.P.M (1947)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L38867.v` — printed in editions [1950, 1951]:**

> PUGH, William Robert Bernard, K.P.M. (1947).—b. 1907; ed. Malvern Coll.; police const., Ken., 1929; asst. supt., 1933; supt., 1947; senr., 1948; dep. comsnr., G.C., 1949.

**Version `col1948-L35361.v` — printed in editions [1948, 1949]:**

> PUGH, William Robert Bernard.—b. 1907; ed. Malvern Coll.; police const., Ken., 1929; asst. supt., 1933; supt., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | police const. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1933 | asst. supt | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1947 | supt | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1948 | senr | Kenya *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1949 | dep. comsnr. | Gold Coast | [1950, 1951] |

## Candidate stint `Pugh, W. R. B___Kenya___1936`

- Staff-list name: **Pugh, W. R. B** | colony: **Kenya** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. R. B. Pugh | Assistant Superintendent | Police Department | — | — |
| 1937 | W. R. B. Pugh | Assistant Superintendent | Police Department | — | — |
| 1939 | W.R.R. Pugh | Assistant Superintendent | Police Department | — | — |
| 1940 | W. R. B. Pugh | Assistant Superintendent | Police Department | — | — |

### Deterministic checks: `pugh_william-robert-bernard_b1907` vs `Pugh, W. R. B___Kenya___1936`

- [PASS] surname_gate: bio 'PUGH' vs stint 'Pugh, W. R. B' (exact)
- [PASS] initials: bio ['W', 'R', 'B'] ~ stint ['W', 'R', 'B']
- [PASS] age_gate: stint starts 1936, birth 1907 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt' ~ 'Assistant Superintendent'
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

