<!-- {"case_id": "case_thompson_t_b1907", "bio_ids": ["thompson_t_b1907"], "stint_ids": ["Thompson, Clarissa T___Jamaica___1922", "Thompson, T. T___British Guiana___1946"]} -->
# Dossier case_thompson_t_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 201 official(s) with this surname in the graph's staff lists; 83 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['thompson_t_b1907'] carry a single initial only — the namesake trap applies.

## Biography `thompson_t_b1907`

- Printed name: **THOMPSON, T**
- Birth year: 1907 (attested in editions [1956, 1959])
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1956-L24567.v` — printed in editions [1956, 1959]:**

> THOMPSON, T.—b. 1907; ed. Royal High Sch., Edin.; p.o.w., 1942-45; temp. survr., ships, S'pore, 1941; ag. survr.-gen. of ships, 1946; senr. engrn. and ship. survr., S'pore, 1947-58.

**Version `col1957-L27817.v` — printed in editions [1957, 1958]:**

> THOMSON, T.—b. 1907; ed. Royal High Sch., Edin.; p.o.w., 1942–45; temp. survr., ships, S.S., 1941; ag. survr.-gen. of ships, 1946; senr. engrnr. and ship. survr., S'pore, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | temp. survr., ships, S'pore | Straits Settlements | [1956, 1957, 1958, 1959] |
| 1 | 1942–1945 | p.o.w | — | [1956, 1957, 1958, 1959] |
| 2 | 1946 | ag. survr.-gen. of ships | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 3 | 1947–1958 | senr. engrn. and ship. survr., S'pore | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |

## Candidate stint `Thompson, Clarissa T___Jamaica___1922`

- Staff-list name: **Thompson, Clarissa T** | colony: **Jamaica** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Clarissa T. Thompson | Typist and Stenographer | Titles Office | — | — |
| 1923 | Clarissa T. Thompson | Typist and Stenographer | Titles Office | — | — |

### Deterministic checks: `thompson_t_b1907` vs `Thompson, Clarissa T___Jamaica___1922`

- [PASS] surname_gate: bio 'THOMPSON' vs stint 'Thompson, Clarissa T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['C', 'T']
- [PASS] age_gate: stint starts 1922, birth 1907 (age 15)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Thompson, T. T___British Guiana___1946`

- Staff-list name: **Thompson, T. T** | colony: **British Guiana** | listed 1946–1948 | editions [1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | T. T. Thompson | Member | Legislative Council | — | — |
| 1948 | T. T. Thompson | Ex officio Member | Legislative Council | — | — |

### Deterministic checks: `thompson_t_b1907` vs `Thompson, T. T___British Guiana___1946`

- [PASS] surname_gate: bio 'THOMPSON' vs stint 'Thompson, T. T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T', 'T']
- [PASS] age_gate: stint starts 1946, birth 1907 (age 39)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1946-1948
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

