<!-- {"case_id": "case_valentine_v-a_b1908", "bio_ids": ["valentine_v-a_b1908"], "stint_ids": ["Valentine, V. A___Jamaica___1933"]} -->
# Dossier case_valentine_v-a_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `valentine_v-a_b1908`

- Printed name: **VALENTINE, V. A**
- Birth year: 1908 (attested in editions [1963, 1964])
- Appears in editions: [1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1963-L25850.v` — printed in editions [1963, 1964]:**

> VALENTINE, V. A.—b. 1908; ed. J'ca Coll.; clk., J'ca, 1941; acctnt., 1950; senr. acctnt., 1952; asst. marktg. admnr., 1955; dep., 1961. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | clk. | Jamaica | [1963, 1964] |
| 1 | 1950 | acctnt | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 2 | 1952 | senr. acctnt | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 3 | 1955 | asst. marktg. admnr | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 4 | 1961 | dep | Jamaica *(inherited from previous clause)* | [1963, 1964] |

## Candidate stint `Valentine, V. A___Jamaica___1933`

- Staff-list name: **Valentine, V. A** | colony: **Jamaica** | listed 1933–1940 | editions [1933, 1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | V. A. Valentine | Assistant Masters | Department of Science and Agriculture | — | — |
| 1934 | V. A. Valentine | Assistant Master | Department of Science and Agriculture | — | — |
| 1937 | V. A. Valentine | Assistant Masters | Department of Science and Agriculture | — | — |
| 1940 | V. A. Valentine | Assistant Masters | Department of Science and Agriculture | — | — |

### Deterministic checks: `valentine_v-a_b1908` vs `Valentine, V. A___Jamaica___1933`

- [PASS] surname_gate: bio 'VALENTINE' vs stint 'Valentine, V. A' (exact)
- [PASS] initials: bio ['V', 'A'] ~ stint ['V', 'A']
- [PASS] age_gate: stint starts 1933, birth 1908 (age 25)
- [PASS] colony: 5 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1940
- [FAIL] position_sim: no overlapping placed event to compare
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

