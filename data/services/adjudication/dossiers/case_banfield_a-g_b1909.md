<!-- {"case_id": "case_banfield_a-g_b1909", "bio_ids": ["banfield_a-g_b1909"], "stint_ids": ["Banfield, A. G___Singapore___1957", "Banfield, A. G___Straits Settlements___1933"]} -->
# Dossier case_banfield_a-g_b1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `banfield_a-g_b1909`

- Printed name: **BANFIELD, A. G**
- Birth year: 1909 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Honours: Efficiency Med (1950)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1956-L19618.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> BANFIELD, A. G., Efficiency Med. (1950).—b. 1909; ed. Dulwich Hamlet L.C.C. Sch. and London Sch. of Printing; mil. serv., 1941-46; supvr., govt. printing off., S'pore, 1932; supt., 1947; rlwy. printer, Nig., 1950; dep. govt. printer, S'pore, 1954; govt. printer, 1956-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | supvr., govt. printing off., S'pore | — | [1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1947 | supt | — | [1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1950 | rlwy. printer | Nigeria | [1956, 1957, 1958, 1959, 1960, 1961] |
| 3 | 1954 | dep. govt. printer, S'pore | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 4 | 1956–1960 | govt. printer | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Banfield, A. G___Singapore___1957`

- Staff-list name: **Banfield, A. G** | colony: **Singapore** | listed 1957–1960 | editions [1957, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | A. G. Banfield | Government Printer | Civil Establishment | — | — |
| 1959 | A. G. Banfield | Government Printer | Civil Establishment | — | — |
| 1960 | A. G. Banfield | Government Printer | MINISTRY OF CULTURE | — | — |

### Deterministic checks: `banfield_a-g_b1909` vs `Banfield, A. G___Singapore___1957`

- [PASS] surname_gate: bio 'BANFIELD' vs stint 'Banfield, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1957, birth 1909 (age 48)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1960
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Banfield, A. G___Straits Settlements___1933`

- Staff-list name: **Banfield, A. G** | colony: **Straits Settlements** | listed 1933–1939 | editions [1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | A. G. Banfield | Bindery Supervisor | Printing Office | — | — |
| 1934 | A. G. Banfield | Bindery Supervisor | Printing Office | — | — |
| 1936 | A. G. Banfield | Binder Supervisor | Printing Office | — | — |
| 1939 | A. G. Banfield | Superintendent | Straits Settlements | — | — |

### Deterministic checks: `banfield_a-g_b1909` vs `Banfield, A. G___Straits Settlements___1933`

- [PASS] surname_gate: bio 'BANFIELD' vs stint 'Banfield, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1933, birth 1909 (age 24)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1939
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

