<!-- {"case_id": "case_kennedy_henry-toffley-money_b1886", "bio_ids": ["kennedy_henry-toffley-money_b1886"], "stint_ids": ["Kennedy, Murdoch___Canada___1912", "Kennedy, T___Commonwealth Of Australia___1905"]} -->
# Dossier case_kennedy_henry-toffley-money_b1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 63 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kennedy_henry-toffley-money_b1886`

- Printed name: **KENNEDY, HENRY TOFFLEY MONEY**
- Birth year: 1886 (attested in editions [1929])
- Honours: A.M.I.C.E
- Appears in editions: [1929]

### Verbatim printed entry text (OCR)

**Version `col1929-L61583.v` — printed in editions [1929]:**

> KENNEDY, HENRY TOFFLEY MONEY, A.M.I.C.E.—B. 1886; ed. Elstow schl. City and Guilds Coll.; instr., tech. schl. F.M.S., Sept., 1914; ag. timber suptd., F.M.S. ryls., Dec., 1914; contr., timber supplies, F.M.S. rly., Jan., 1919; ditto, forest dept., S. Stittms. and F.M.S., Jan., 1928; sent to report on timber utilization problems in India and Burma, May, 1924; on spl. duty, Madison, U.S.A., Nov. to Dec., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | instr., tech. schl. F.M.S | — | [1929] |
| 1 | 1914 | ag. timber suptd., F.M.S. ryls | Federated Malay States | [1929] |
| 2 | 1919 | contr., timber supplies, F.M.S. rly | Federated Malay States | [1929] |
| 3 | 1924 | sent to report on timber utilization problems in India and Burma | Federated Malay States *(inherited from previous clause)* | [1929] |
| 4 | 1926 | on spl. duty, Madison, U.S.A | Federated Malay States *(inherited from previous clause)* | [1929] |
| 5 | 1928 | ditto, forest dept., S. Stittms. and F.M.S | Federated Malay States *(inherited from previous clause)* | [1929] |

## Candidate stint `Kennedy, Murdoch___Canada___1912`

- Staff-list name: **Kennedy, Murdoch** | colony: **Canada** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1918, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Murdoch Kennedy | Member | Legislative Assembly | — | — |
| 1912 | Murdoch Kennedy | Without Portfolio | Executive Council | — | — |
| 1913 | Murdoch Kennedy | Without Portfolio | Executive Council | — | — |
| 1914 | Murdoch Kennedy | Member | Legislative Assembly | — | — |
| 1915 | Murdoch Kennedy | Member | Legislative Assembly | — | — |
| 1918 | Murdoch Kennedy | Without Portfolio | Executive Council | — | — |
| 1918 | Murdoch Kennedy | District Member | Queen's County | — | — |
| 1920 | M. Kennedy | Assemblyman | Queen's County | — | — |
| 1922 | M. Kennedy | Assemblyman | Queen's County | — | — |

### Deterministic checks: `kennedy_henry-toffley-money_b1886` vs `Kennedy, Murdoch___Canada___1912`

- [PASS] surname_gate: bio 'KENNEDY' vs stint 'Kennedy, Murdoch' (exact)
- [PASS] initials: bio ['H', 'T', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1912, birth 1886 (age 26)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Kennedy, T___Commonwealth Of Australia___1905`

- Staff-list name: **Kennedy, T** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | T. Kennedy | Member of Legislative Assembly | Parliament | — | — |
| 1907 | T. Kennedy | Auditor and Examiner | Metropolitan Board of Water Supply & Sewerage | — | — |
| 1907 | T. Kennedy | Indi | — | — | — |

### Deterministic checks: `kennedy_henry-toffley-money_b1886` vs `Kennedy, T___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'KENNEDY' vs stint 'Kennedy, T' (exact)
- [PASS] initials: bio ['H', 'T', 'M'] ~ stint ['T']
- [PASS] age_gate: stint starts 1905, birth 1886 (age 19)
- [FAIL] colony: no placed event resolves to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

