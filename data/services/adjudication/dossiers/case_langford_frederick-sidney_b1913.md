<!-- {"case_id": "case_langford_frederick-sidney_b1913", "bio_ids": ["langford_frederick-sidney_b1913"], "stint_ids": ["Langford, F. S___Jamaica___1949"]} -->
# Dossier case_langford_frederick-sidney_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `langford_frederick-sidney_b1913`

- Printed name: **LANGFORD, Frederick Sidney**
- Birth year: 1913 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1951, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L21787.v` — printed in editions [1963, 1964, 1965, 1966]:**

> LANGFORD, F. S.—b. 1913; Pal. police, 1940; asst. supt., J'ca, 1948; dep. supt., 1952; supt., 1955; senr. supt., 1962. (J'ca Govt. service.)

**Version `col1951-L39914.v` — printed in editions [1951]:**

> LANGFORD, Frederick Sidney.—b. 1913; ed. Sec. Sch.; apptd. police, Pal., 1940; asst. supt., J’ca., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | Pal. police | Palestine | [1951, 1963, 1964, 1965, 1966] |
| 1 | 1948 | asst. supt. | Jamaica | [1951, 1963, 1964, 1965, 1966] |
| 2 | 1952 | dep. supt | Jamaica *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 3 | 1955 | supt | Jamaica *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 4 | 1962 | senr. supt | Jamaica *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Langford, F. S___Jamaica___1949`

- Staff-list name: **Langford, F. S** | colony: **Jamaica** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. S. Langford | Assistant Superintendents of Police | POLICE | — | — |
| 1950 | F. S. Langford | Assistant Superintendent of Police | Police | — | — |

### Deterministic checks: `langford_frederick-sidney_b1913` vs `Langford, F. S___Jamaica___1949`

- [PASS] surname_gate: bio 'LANGFORD' vs stint 'Langford, F. S' (exact)
- [PASS] initials: bio ['F', 'S'] ~ stint ['F', 'S']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 4 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 42 vs bar 60: 'asst. supt.' ~ 'Assistant Superintendent of Police'
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

