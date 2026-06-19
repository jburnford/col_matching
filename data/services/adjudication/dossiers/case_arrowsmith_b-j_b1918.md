<!-- {"case_id": "case_arrowsmith_b-j_b1918", "bio_ids": ["arrowsmith_b-j_b1918"], "stint_ids": ["Arrowsmith, B. J___North Borneo___1949"]} -->
# Dossier case_arrowsmith_b-j_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `arrowsmith_b-j_b1918`

- Printed name: **ARROWSMITH, B. J**
- Birth year: 1918 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L20187.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> ARROWSMITH, B. J.—b. 1918; ed. Ealing Coll.; mil. serv., 1939-48, major; asst. supt., police, N. Borneo, 1949; dep. supt., 1956; supt., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | asst. supt., police | North Borneo | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1956 | dep. supt | North Borneo *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1961 | supt | North Borneo *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Arrowsmith, B. J___North Borneo___1949`

- Staff-list name: **Arrowsmith, B. J** | colony: **North Borneo** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. Arrowsmith | Accountants | Treasury | — | — |
| 1950 | B. J. Arrowsmith | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `arrowsmith_b-j_b1918` vs `Arrowsmith, B. J___North Borneo___1949`

- [PASS] surname_gate: bio 'ARROWSMITH' vs stint 'Arrowsmith, B. J' (exact)
- [PASS] initials: bio ['B', 'J'] ~ stint ['B', 'J']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 45 vs bar 60: 'asst. supt., police' ~ 'Assistant Superintendent'
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

