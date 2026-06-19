<!-- {"case_id": "case_lock_ronald-george_b1915", "bio_ids": ["lock_ronald-george_b1915"], "stint_ids": ["Lock, R. G___Cyprus___1957"]} -->
# Dossier case_lock_ronald-george_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lock_ronald-george_b1915`

- Printed name: **LOCK, Ronald George**
- Birth year: 1915 (attested in editions [1949, 1951])
- Appears in editions: [1949, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L33738.v` — printed in editions [1949, 1951]:**

> LOCK, Ronald George.—b. 1915 ; ed. Judd Sch., Tonbridge ; inter. L.A.A., on mil. serv., 1941-47, lt.-col., gen. list ; police constab., Pal., 1935 ; 2nd sergt., 1938 ; 1st sergt., 1939 ; inspr., 1942 ; asst. supt., 1947 ; Nig. 1948 ; supt., Eritrea & Cyrenaica police ; comsnr., Dodecanese police whilst on mil. secondment.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935–1935 | police constab. | Palestine | [1949, 1951] |
| 1 | 1938–1938 | 2nd sergt. | — | [1949, 1951] |
| 2 | 1939–1939 | 1st sergt. | — | [1949, 1951] |
| 3 | 1941–1947 | lt.-col., gen. list | — | [1949, 1951] |
| 4 | 1942–1942 | inspr. | — | [1949, 1951] |
| 5 | 1947–1947 | asst. supt. | — | [1949, 1951] |
| 6 | 1948–1948 | — | Nigeria | [1949, 1951] |

## Candidate stint `Lock, R. G___Cyprus___1957`

- Staff-list name: **Lock, R. G** | colony: **Cyprus** | listed 1957–1959 | editions [1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | R. G. Lock | Deputy Commissioner of Police | Civil Establishment | — | — |
| 1958 | R. G. Lock | Deputy Chief Constable | Civil Establishment | O.B.E. | — |
| 1959 | R. G. Lock | Deputy Chief Constable | Civil Establishment | — | — |

### Deterministic checks: `lock_ronald-george_b1915` vs `Lock, R. G___Cyprus___1957`

- [PASS] surname_gate: bio 'LOCK' vs stint 'Lock, R. G' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['R', 'G']
- [PASS] age_gate: stint starts 1957, birth 1915 (age 42)
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1959
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

