<!-- {"case_id": "case_chase_david-austen-lisle_b1920", "bio_ids": ["chase_david-austen-lisle_b1920"], "stint_ids": ["Chase, D. A. L___Jamaica___1949"]} -->
# Dossier case_chase_david-austen-lisle_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chase_david-austen-lisle_b1920`

- Printed name: **CHASE, David Austen Lisle**
- Birth year: 1920 (attested in editions [1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L36891.v` — printed in editions [1951]:**

> CHASE, David Austen Lisle.—b. 1920; ed. Lodge Sch, Barb.; on mil. serv., 1939-45; asst. supt., police, Leeaward Is., 1940; B. Guiana, 1942; J'ca., 1948; senr. asst. supt., 1948.

**Version `col1950-L34339.v` — printed in editions [1950]:**

> CHASE, David Austen Lisle.—b. 1920; ed. Lodge Sch., Barb.; asst. supt., police, Leeward Is., 1940; B. Guiana, 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | asst. supt., police, Leeaward Is | — | [1950, 1951] |
| 1 | 1942 | B. Guiana | — | [1950, 1951] |
| 2 | 1948 | B. Guiana | Jamaica | [1951] |

## Candidate stint `Chase, D. A. L___Jamaica___1949`

- Staff-list name: **Chase, D. A. L** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. A. L. Chase | Assistant Superintendents of Police | POLICE | — | — |
| 1950 | D. A. L. Chase | Senior Assistant Superintendent of Police | Police | — | — |
| 1951 | D. A. L. Chase | Senior Assistant Superintendent of Police | POLICE | — | — |

### Deterministic checks: `chase_david-austen-lisle_b1920` vs `Chase, D. A. L___Jamaica___1949`

- [PASS] surname_gate: bio 'CHASE' vs stint 'Chase, D. A. L' (exact)
- [PASS] initials: bio ['D', 'A', 'L'] ~ stint ['D', 'A', 'L']
- [PASS] age_gate: stint starts 1949, birth 1920 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 19 vs bar 60: 'B. Guiana' ~ 'Assistant Superintendents of Police'
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

