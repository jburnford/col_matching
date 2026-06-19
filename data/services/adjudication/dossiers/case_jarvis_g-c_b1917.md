<!-- {"case_id": "case_jarvis_g-c_b1917", "bio_ids": ["jarvis_g-c_b1917"], "stint_ids": ["Jarvis, G. C___Kenya___1949", "Jarvis, G. C___Sierra Leone___1958"]} -->
# Dossier case_jarvis_g-c_b1917

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jarvis_g-c_b1917`

- Printed name: **JARVIS, G. C**
- Birth year: 1917 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1966)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L24029.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> JARVIS, G. C., O.B.E. (1966).—b. 1917; ed. Portsmouth Gram. Sch.; mil. serv., 1939-45, major, R.M.; asst. audr., Ken., 1946; audr., 1948; senr. audr., H.K., 1950; prim. audr., S. Leone, 1957; dir., audit, 1958; asst. dir., O.A.D., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. audr. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | audr | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1950 | senr. audr. | Hong Kong | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1957 | prim. audr., S. Leone | Hong Kong *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1958 | dir., audit | Hong Kong *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1960 | asst. dir., O.A.D | Hong Kong *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Jarvis, G. C___Kenya___1949`

- Staff-list name: **Jarvis, G. C** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. C. Jarvis | Auditors and Assistant Auditors | Audit | — | — |
| 1950 | G. C. Jarvis | Auditors and Assistant Auditors | AUDIT | — | — |

### Deterministic checks: `jarvis_g-c_b1917` vs `Jarvis, G. C___Kenya___1949`

- [PASS] surname_gate: bio 'JARVIS' vs stint 'Jarvis, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 58 vs bar 60: 'asst. audr.' ~ 'Auditors and Assistant Auditors'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Jarvis, G. C___Sierra Leone___1958`

- Staff-list name: **Jarvis, G. C** | colony: **Sierra Leone** | listed 1958–1960 | editions [1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | G. C. Jarvis | Director of Audit | Civil Establishment | — | — |
| 1959 | G. C. Jarvis | Director of Audit | Civil Establishment | — | — |
| 1960 | G. C. Jarvis | Director of Audit | Civil Establishment | — | — |

### Deterministic checks: `jarvis_g-c_b1917` vs `Jarvis, G. C___Sierra Leone___1958`

- [PASS] surname_gate: bio 'JARVIS' vs stint 'Jarvis, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1958, birth 1917 (age 41)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
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

