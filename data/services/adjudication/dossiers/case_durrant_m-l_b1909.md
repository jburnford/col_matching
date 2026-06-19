<!-- {"case_id": "case_durrant_m-l_b1909", "bio_ids": ["durrant_m-l_b1909"], "stint_ids": ["Durrant, M. L___Hong Kong___1953", "Durrant, M. L___Singapore___1955"]} -->
# Dossier case_durrant_m-l_b1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `durrant_m-l_b1909`

- Printed name: **DURRANT, M. L**
- Birth year: 1909 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L17198.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> DURRANT, M. L.—b. 1909; ed. Bishop Wordsworth's, Salisbury; interned, 1942-45; Br. P.O., 1926; asst. contrib. of posts, S'pore, 1939; contrir., Mal., 1950; asst. P.M.G., H.K., 1950; dir., posts, S'pore, 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | Br. P.O | — | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1939 | asst. contrib. of posts, S'pore | — | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1942–1945 | interned | — | [1953, 1954, 1955, 1956, 1957] |
| 3 | 1950 | contrir. | Malaya | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1950 | asst. P.M.G. | Hong Kong | [1953, 1954, 1955, 1956, 1957] |
| 5 | 1953 | dir., posts, S'pore | Hong Kong *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Durrant, M. L___Hong Kong___1953`

- Staff-list name: **Durrant, M. L** | colony: **Hong Kong** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | M. L. Durrant | Assistant Postmaster-General | Civil Establishment | — | — |
| 1954 | M. L. Durrant | Assistant Postmaster-General | Civil Establishment | — | — |

### Deterministic checks: `durrant_m-l_b1909` vs `Durrant, M. L___Hong Kong___1953`

- [PASS] surname_gate: bio 'DURRANT' vs stint 'Durrant, M. L' (exact)
- [PASS] initials: bio ['M', 'L'] ~ stint ['M', 'L']
- [PASS] age_gate: stint starts 1953, birth 1909 (age 44)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1953-1954
- [FAIL] position_sim: best 46 vs bar 60: 'asst. P.M.G.' ~ 'Assistant Postmaster-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Durrant, M. L___Singapore___1955`

- Staff-list name: **Durrant, M. L** | colony: **Singapore** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | M. L. Durrant | Director of Posts | Civil Establishment | — | — |
| 1956 | M. L. Durrant | Director of Posts | Civil Establishment | — | — |
| 1957 | M. L. Durrant | Director of Posts | Civil Establishment | — | — |

### Deterministic checks: `durrant_m-l_b1909` vs `Durrant, M. L___Singapore___1955`

- [PASS] surname_gate: bio 'DURRANT' vs stint 'Durrant, M. L' (exact)
- [PASS] initials: bio ['M', 'L'] ~ stint ['M', 'L']
- [PASS] age_gate: stint starts 1955, birth 1909 (age 46)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
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

