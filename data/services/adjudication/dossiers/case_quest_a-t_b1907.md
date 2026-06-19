<!-- {"case_id": "case_quest_a-t_b1907", "bio_ids": ["quest_a-t_b1907"], "stint_ids": ["Guest, A. T___Bermuda___1939"]} -->
# Dossier case_quest_a-t_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `quest_a-t_b1907` ↔ `Guest, A. T___Bermuda___1939` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Guest, A. T___Bermuda___1939` is also gate-compatible with biography(ies) outside this case: ['guest_a-t_b1907'] (already linked elsewhere or filtered).

## Biography `quest_a-t_b1907`

- Printed name: **QUEST, A. T**
- Birth year: 1907 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L23655.v` — printed in editions [1957]:**

> QUEST, A. T.—b. 1907; ed. Canada; ch. immig. offr., Berm., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | ch. immig. offr. | Bermuda | [1957] |

## Candidate stint `Guest, A. T___Bermuda___1939`

- Staff-list name: **Guest, A. T** | colony: **Bermuda** | listed 1939–1966 | editions [1939, 1940, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. T. Guest | Chief Immigration Officer | Immigration | — | — |
| 1940 | A. T. Guest | Chief Immigration Officer | Immigration | — | — |
| 1949 | A. T. Guest | Chief Immigration Officer | Immigration | — | — |
| 1950 | A. T. Guest | Chief Immigration Officer | Immigration | — | — |
| 1951 | A. T. Guest | Chief Immigration Officer | IMMIGRATION | — | — |
| 1952 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1953 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1954 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1955 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1957 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1958 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1959 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1960 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1961 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1962 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1963 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1964 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1965 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |
| 1966 | A. T. Guest | Chief Immigration Officer | Civil Establishment | — | — |

### Deterministic checks: `quest_a-t_b1907` vs `Guest, A. T___Bermuda___1939`

- [PASS] surname_gate: bio 'QUEST' vs stint 'Guest, A. T' (fuzzy:1)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1939, birth 1907 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Bermuda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1966
- [PASS] position_sim: best 68 vs bar 60: 'ch. immig. offr.' ~ 'Chief Immigration Officer'
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

