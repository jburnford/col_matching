<!-- {"case_id": "case_baker_a-l_b1912", "bio_ids": ["baker_a-l_b1912"], "stint_ids": ["Baker, A. L___Fiji___1946"]} -->
# Dossier case_baker_a-l_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 91 official(s) with this surname in the graph's staff lists; 52 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `baker_a-l_b1912`

- Printed name: **BAKER, A. L.**
- Birth year: 1912 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Honours: M.B.E. (1957)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1956-L19590.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> BAKER, A. L., M.B.E. (1957).—b. 1912; ed. Sydney C. of E. Gram. Sch., N.S.W.; cl. III clk., W. Pac. H.C., 1932; clk., couns., Fiji, 1944; sec., med. dept., 1947; estab. offr., 1950-59; sec., salaries comsns., 1946, 1950, 1953 and 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932–1932 | cl. III clk. | Western Pacific High Commission | [1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1944–1944 | clk., couns. | Fiji | [1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1946–1956 | sec., salaries comsns. | — | [1956, 1957, 1958, 1959, 1960, 1961] |
| 3 | 1947–1947 | sec., med. dept. | — | [1956, 1957, 1958, 1959, 1960, 1961] |
| 4 | 1950–1959 | estab. offr. | — | [1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Baker, A. L___Fiji___1946`

- Staff-list name: **Baker, A. L** | colony: **Fiji** | listed 1946–1950 | editions [1946, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | A. L. Baker | Clerk | Legislative Council | — | — |
| 1946 | A. L. Baker | Clerk | Executive Council | — | — |
| 1950 | A. L. Baker | Secretary | Medical | — | — |

### Deterministic checks: `baker_a-l_b1912` vs `Baker, A. L___Fiji___1946`

- [PASS] surname_gate: bio 'BAKER' vs stint 'Baker, A. L' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1946, birth 1912 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1946-1950
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

