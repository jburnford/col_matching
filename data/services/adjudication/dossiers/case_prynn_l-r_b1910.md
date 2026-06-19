<!-- {"case_id": "case_prynn_l-r_b1910", "bio_ids": ["prynn_l-r_b1910"], "stint_ids": ["Prynn, L. R___Singapore___1949"]} -->
# Dossier case_prynn_l-r_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `prynn_l-r_b1910`

- Printed name: **PRYNN, L. R**
- Birth year: 1910 (attested in editions [1956, 1957, 1958, 1959])
- Honours: C.P.M (1954)
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L23622.v` — printed in editions [1956, 1957, 1958, 1959]:**

> PRYNN, L. R., C.P.M. (1954).—b. 1910; ed. St. Austell Sec. Sch.; interned, 1942-45; prob. inspr., police, S.S., 1932; inspr., 1935; senr., 1941; asst. supt., 1946; supt., police, S'pore, 1952-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | prob. inspr., police | Straits Settlements | [1956, 1957, 1958, 1959] |
| 1 | 1935 | inspr | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 2 | 1941 | senr | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 3 | 1942–1945 | interned | — | [1956, 1957, 1958, 1959] |
| 4 | 1946 | asst. supt | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 5 | 1952–1958 | supt., police, S'pore | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |

## Candidate stint `Prynn, L. R___Singapore___1949`

- Staff-list name: **Prynn, L. R** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. R. Prynn | Assistant Superintendents of Police | Police | — | — |
| 1951 | L. R. Prynn | Assistant Superintendents | Police | — | — |

### Deterministic checks: `prynn_l-r_b1910` vs `Prynn, L. R___Singapore___1949`

- [PASS] surname_gate: bio 'PRYNN' vs stint 'Prynn, L. R' (exact)
- [PASS] initials: bio ['L', 'R'] ~ stint ['L', 'R']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
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

