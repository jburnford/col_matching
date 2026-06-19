<!-- {"case_id": "case_lucas_n-a_b1906", "bio_ids": ["lucas_n-a_b1906"], "stint_ids": ["Lucas, N. A___Sarawak___1949"]} -->
# Dossier case_lucas_n-a_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lucas_n-a_b1906`

- Printed name: **LUCAS, N. A**
- Birth year: 1906 (attested in editions [1958, 1959, 1960])
- Appears in editions: [1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1958-L24750.v` — printed in editions [1958, 1959, 1960]:**

> LUCAS, N. A.—b. 1906; ed. Kilburn Gram. Sch.; supply offr., Sarawak, 1946; supt., customs, 1948; supt., shipping in addn., 1952; supt., customs, 1955-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | supply offr. | Sarawak | [1958, 1959, 1960] |
| 1 | 1948 | supt., customs | Sarawak *(inherited from previous clause)* | [1958, 1959, 1960] |
| 2 | 1952 | supt., shipping in addn | Sarawak *(inherited from previous clause)* | [1958, 1959, 1960] |
| 3 | 1955–1959 | supt., customs | Sarawak *(inherited from previous clause)* | [1958, 1959, 1960] |

## Candidate stint `Lucas, N. A___Sarawak___1949`

- Staff-list name: **Lucas, N. A** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | N. A. Lucas | Superintendents of Customs | Trade and Customs | — | — |
| 1950 | N. A. Lucas | Superintendent of Customs | TRADE AND CUSTOMS | — | — |
| 1951 | N. A. Lucas | Superintendent of Customs | Trade and Customs | — | — |

### Deterministic checks: `lucas_n-a_b1906` vs `Lucas, N. A___Sarawak___1949`

- [PASS] surname_gate: bio 'LUCAS' vs stint 'Lucas, N. A' (exact)
- [PASS] initials: bio ['N', 'A'] ~ stint ['N', 'A']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 4 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 74 vs bar 60: 'supt., customs' ~ 'Superintendent of Customs'
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

