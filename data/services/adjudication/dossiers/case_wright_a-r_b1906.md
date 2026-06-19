<!-- {"case_id": "case_wright_a-r_b1906", "bio_ids": ["wright_a-r_b1906"], "stint_ids": ["Wright, A. R___Mauritius___1961"]} -->
# Dossier case_wright_a-r_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 159 official(s) with this surname in the graph's staff lists; 63 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wright_a-r_b1906`

- Printed name: **WRIGHT, A. R**
- Birth year: 1906 (attested in editions [1963, 1964])
- Appears in editions: [1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1963-L26561.v` — printed in editions [1963, 1964]:**

> WRIGHT, A. R.—b. 1906; ed. Haverstock Sch.; mil. serv., 1944-47, maj.; supt, police, Maur., 1954; trans. comsnt., 1960-63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1954 | supt, police | Mauritius | [1963, 1964] |
| 1 | 1960–1963 | trans. comsnt | Mauritius *(inherited from previous clause)* | [1963, 1964] |

## Candidate stint `Wright, A. R___Mauritius___1961`

- Staff-list name: **Wright, A. R** | colony: **Mauritius** | listed 1961–1963 | editions [1961, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | A. R. Wright | Road Transport Commissioner | Civil Establishment | — | — |
| 1962 | A. R. Wright | Road Transport Commissioner | CIVIL ESTABLISHMENT | — | — |
| 1963 | A. R. Wright | Road Transport Commissioner | Civil Establishment | — | — |

### Deterministic checks: `wright_a-r_b1906` vs `Wright, A. R___Mauritius___1961`

- [PASS] surname_gate: bio 'WRIGHT' vs stint 'Wright, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1961, birth 1906 (age 55)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1961-1963
- [FAIL] position_sim: best 56 vs bar 60: 'trans. comsnt' ~ 'Road Transport Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1963] pos~56 (bar: >=2)
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

