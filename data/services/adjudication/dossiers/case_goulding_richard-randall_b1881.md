<!-- {"case_id": "case_goulding_richard-randall_b1881", "bio_ids": ["goulding_richard-randall_b1881"], "stint_ids": ["Goulding, R. R___Straits Settlements___1931"]} -->
# Dossier case_goulding_richard-randall_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `goulding_richard-randall_b1881`

- Printed name: **GOULDING, RICHARD RANDALL**
- Birth year: 1881 (attested in editions [1932])
- Honours: M.N.Z.I.S
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L60587.v` — printed in editions [1932]:**

> GOULDING, RICHARD RANDALL, M.N.Z.I.S.—B.1881; survey dept., N. Zealand, Apr., 1898; Sept., 1904; surv., trig. survey br., F.M.S., May, 1907; astt. supt., trig. survey br., Jan., 1913; supt., rev. surveys, Johore, Jly., 1923; astt., trig. br., survey dept., F.M.S. and S.S., Sept., 1927; supt., rev. surveys, Pahang, May, 1929; astt., rev. surveys, Perak, Feb., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | survey dept., N. Zealand | — | [1932] |
| 1 | 1904 | survey dept., N. Zealand | — | [1932] |
| 2 | 1907 | surv., trig. survey br. | Federated Malay States | [1932] |
| 3 | 1913 | astt. supt., trig. survey br | Federated Malay States *(inherited from previous clause)* | [1932] |
| 4 | 1923 | supt., rev. surveys, Johore, Jly | Federated Malay States *(inherited from previous clause)* | [1932] |
| 5 | 1927 | astt., trig. br., survey dept., F.M.S. and S.S | Federated Malay States | [1932] |
| 6 | 1929 | supt., rev. surveys, Pahang | Federated Malay States *(inherited from previous clause)* | [1932] |
| 7 | 1930 | astt., rev. surveys, Perak | Federated Malay States *(inherited from previous clause)* | [1932] |

## Candidate stint `Goulding, R. R___Straits Settlements___1931`

- Staff-list name: **Goulding, R. R** | colony: **Straits Settlements** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R R Goulding | Senior Superintendent | SURVEYS | — | — |
| 1932 | R. R. Goulding | Senior Superintendent, Perak | Surveys | — | — |

### Deterministic checks: `goulding_richard-randall_b1881` vs `Goulding, R. R___Straits Settlements___1931`

- [PASS] surname_gate: bio 'GOULDING' vs stint 'Goulding, R. R' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1931, birth 1881 (age 50)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

