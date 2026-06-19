<!-- {"case_id": "case_mcintyre_john_e1898", "bio_ids": ["mcintyre_john_e1898", "mcintyre_john_e1898-2"], "stint_ids": ["McIntyre, J___Tasmania___1899"]} -->
# Dossier case_mcintyre_john_e1898

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcintyre_john_e1898', 'mcintyre_john_e1898-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['McIntyre, J___Tasmania___1899'] have more than one claimant biography in this case.
- Phase 1 found `mcintyre_john_e1898` ↔ `McIntyre, J___Tasmania___1899` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `mcintyre_john_e1898-2` ↔ `McIntyre, J___Tasmania___1899` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `mcintyre_john_e1898`

- Printed name: **McINTYRE, JOHN**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1908, 1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1905-L44642.v` — printed in editions [1905, 1906, 1908, 1909, 1910, 1911]:**

> McINTYRE, JOHN.—Apptd. puisane judge, Tasmania, 1898.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | Apptd. puisane judge | Tasmania | [1905, 1906, 1908, 1909, 1910, 1911] |

## Biography `mcintyre_john_e1898-2`

- Printed name: **MCINTYRE, JOHN**
- Birth year: not printed
- Appears in editions: [1907, 1914]

### Verbatim printed entry text (OCR)

**Version `col1914-L48249.v` — printed in editions [1914]:**

> MCINTYRE, HON. JOHN.—Apptd. puisne judge, Tasmania, 1898; has acted as chief justice on several occasions.

**Version `col1907-L45634.v` — printed in editions [1907]:**

> MACINTYRE, JOHN.—Apptd. puisne judge, Tasmania, 1899.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | Apptd. puisne judge | Tasmania | [1914] |
| 1 | 1899 | Apptd. puisne judge | Tasmania | [1907] |

## Candidate stint `McIntyre, J___Tasmania___1899`

- Staff-list name: **McIntyre, J** | colony: **Tasmania** | listed 1899–1909 | editions [1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | J. McIntyre | Puisne Judges | Judicial and Legal Departments | — | — |
| 1900 | J. McIntyre | Puisne Judge | Judicial and Legal Departments | — | — |
| 1905 | J. McIntyre | Puisne Judges | Judicial and Legal Departments | — | — |
| 1906 | J. McIntyre | Puisne Judges | Judicial and Legal Departments | — | — |
| 1907 | J. McIntyre | Puisne Judge | Judicial and Legal Departments | — | — |
| 1908 | J. McIntyre | Puisne Judge | Judicial and Legal Departments | — | — |
| 1909 | Hon. J. McIntyre | Puisne Judge | Judicial and Legal Departments | — | — |

### Deterministic checks: `mcintyre_john_e1898` vs `McIntyre, J___Tasmania___1899`

- [PASS] surname_gate: bio 'McINTYRE' vs stint 'McIntyre, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1899-1909
- [PASS] position_sim: best 77 vs bar 60: 'Apptd. puisane judge' ~ 'Puisne Judge'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1905, 1906, 1908, 1909] pos~76 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `mcintyre_john_e1898-2` vs `McIntyre, J___Tasmania___1899`

- [PASS] surname_gate: bio 'MCINTYRE' vs stint 'McIntyre, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1899-1909
- [PASS] position_sim: best 100 vs bar 60: 'Apptd. puisne judge' ~ 'Puisne Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1907] pos~100 (bar: >=2)
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

