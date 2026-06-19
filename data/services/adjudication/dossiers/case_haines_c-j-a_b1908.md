<!-- {"case_id": "case_haines_c-j-a_b1908", "bio_ids": ["haines_c-j-a_b1908"], "stint_ids": ["Haines, C. J. A___Singapore___1949"]} -->
# Dossier case_haines_c-j-a_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `haines_c-j-a_b1908`

- Printed name: **HAINES, C. J. A**
- Birth year: 1908 (attested in editions [1956, 1957, 1958, 1959])
- Honours: C.P.M (1950)
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L21619.v` — printed in editions [1956, 1957, 1958, 1959]:**

> HAINES, C. J. A., C.P.M. (1950).—b. 1908; ed. L.C.C. and Mddx Schs. and privately; interned, 1942-45; prob. inspr., police, S.S. and F.M.S., 1930; inspr., 1933; senr., 1939; inspr., detec. branch, S'pore, 1940; senr., 1941; asst. supt., police, 1941; I.C.D., 1946; supt., 1952; S.O.I., police H.Q., 1954; ag. asst. comsnr., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | prob. inspr., police, S.S. and F.M.S | Straits Settlements | [1956, 1957, 1958, 1959] |
| 1 | 1933 | inspr | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 2 | 1939 | senr | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 3 | 1940 | inspr., detec. branch, S'pore | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 4 | 1941 | senr | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 5 | 1942–1945 | interned | — | [1956, 1957, 1958, 1959] |
| 6 | 1946 | I.C.D | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 7 | 1952 | supt | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 8 | 1954 | S.O.I., police H.Q | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 9 | 1955 | ag. asst. comsnr | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |

## Candidate stint `Haines, C. J. A___Singapore___1949`

- Staff-list name: **Haines, C. J. A** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. J. A. Haines | Assistant Superintendents of Police | Police | — | — |
| 1951 | C. J. A. Haines | Superintendents | Police | — | — |

### Deterministic checks: `haines_c-j-a_b1908` vs `Haines, C. J. A___Singapore___1949`

- [PASS] surname_gate: bio 'HAINES' vs stint 'Haines, C. J. A' (exact)
- [PASS] initials: bio ['C', 'J', 'A'] ~ stint ['C', 'J', 'A']
- [PASS] age_gate: stint starts 1949, birth 1908 (age 41)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

