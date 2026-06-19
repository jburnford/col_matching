<!-- {"case_id": "case_hedeley_harold-thomas_b1887", "bio_ids": ["hedeley_harold-thomas_b1887"], "stint_ids": ["Hedley, H. T___Straits Settlements___1923", "Hedley, T___Cape of Good Hope___1907"]} -->
# Dossier case_hedeley_harold-thomas_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hedeley_harold-thomas_b1887`

- Printed name: **HEDELEY, HAROLD THOMAS**
- Birth year: 1887 (attested in editions [1935])
- Appears in editions: [1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `dol1935-L59346.v` — printed in editions [1935]:**

> HEDELEY, HAROLD THOMAS, Incorporated Acct.—B. 1887; audit dept., S.S., Dec., 1921; i/c. external audit dept., K. Lumbur, Jan., 1922; astt. audr., grade A, Jan., 1923; ag. sr. astt. audr., Nov., 1928-Jly., 1929; audr., Penang, Aug., 1930; senr. astt. audr., S.S. and F.M.S., July, 1933.

**Version `col1932-L61027.v` — printed in editions [1932, 1933, 1934]:**

> HEDLEY, HAROLD THOMAS, Incorporated Acct.—B. 1887; audit dept., S. S., Dec., 1931; i/c. external audit dept., Kuala Lumpur, Jan., 1932; asst. audr., grade A, Jan., 1923; ag. sr. asst. audr., Nov., 1928-Jly., 1929; audr., Aug., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | audit dept. | Straits Settlements | [1935] |
| 1 | 1922 | i/c. external audit dept. | Kuala Lumpur | [1935] |
| 2 | 1923 | astt. audr., grade A | — | [1932, 1933, 1934, 1935] |
| 3 | 1928–1929 | ag. sr. astt. audr. | — | [1932, 1933, 1934, 1935] |
| 4 | 1930 | audr. | Penang | [1932, 1933, 1934, 1935] |
| 5 | 1931 | audit dept. | Straits Settlements | [1932, 1933, 1934] |
| 6 | 1932 | i/c. external audit dept. | Kuala Lumpur | [1932, 1933, 1934] |
| 7 | 1933 | senr. astt. audr. | Straits Settlements and Federated Malay States | [1935] |

## Candidate stint `Hedley, H. T___Straits Settlements___1923`

- Staff-list name: **Hedley, H. T** | colony: **Straits Settlements** | listed 1923–1931 | editions [1923, 1925, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | H. T. Hedley | Assistant Auditors | External Audit | — | — |
| 1925 | H. T. Hedley | Assistant Auditors | External Audit | — | — |
| 1931 | H. T. Hedley | Assistant Auditor | Audit Office | — | — |
| 1931 | H. T. Hedley | Assistant Auditors | External Audit | — | — |

### Deterministic checks: `hedeley_harold-thomas_b1887` vs `Hedley, H. T___Straits Settlements___1923`

- [PASS] surname_gate: bio 'HEDELEY' vs stint 'Hedley, H. T' (fuzzy:1)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1923, birth 1887 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1923-1931
- [FAIL] position_sim: best 44 vs bar 60: 'audit dept.' ~ 'Assistant Auditor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hedley, T___Cape of Good Hope___1907`

- Staff-list name: **Hedley, T** | colony: **Cape of Good Hope** | listed 1907–1909 | editions [1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | T. Hedley | Examiner | Educational Department | — | — |
| 1908 | T. Hedley | Clerks | Educational Department | — | — |
| 1909 | T. Hedley | Clerks | Educational Department | — | — |

### Deterministic checks: `hedeley_harold-thomas_b1887` vs `Hedley, T___Cape of Good Hope___1907`

- [PASS] surname_gate: bio 'HEDELEY' vs stint 'Hedley, T' (fuzzy:1)
- [PASS] initials: bio ['H', 'T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1907, birth 1887 (age 20)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1909
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

