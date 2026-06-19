<!-- {"case_id": "case_mcintyre_john-norbert_b1895", "bio_ids": ["mcintyre_john-norbert_b1895"], "stint_ids": ["McIntyre, J. N___Leeward Islands___1936", "McIntyre, J___Australia___1912"]} -->
# Dossier case_mcintyre_john-norbert_b1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `McIntyre, J. N___Leeward Islands___1936` is also gate-compatible with biography(ies) outside this case: ['mcintyre_john_e1898', 'mcintyre_john_e1898-2'] (already linked elsewhere or filtered).
- NOTE: stint `McIntyre, J___Australia___1912` is also gate-compatible with biography(ies) outside this case: ['mcintyre_john_e1898', 'mcintyre_john_e1898-2'] (already linked elsewhere or filtered).

## Biography `mcintyre_john-norbert_b1895`

- Printed name: **McINTYRE, John Norbert**
- Birth year: 1895 (attested in editions [1949, 1950])
- Honours: M.B.E
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L33970.v` — printed in editions [1949, 1950]:**

> McINTYRE, John Norbert, M.B.E.—b. 1895; ed. Dominica Gram. Sch.; 2nd clk., registr. off., Dominica, 1914; prin., admin. off., 1940; gov. sec., 1944.

**Version `col1951-L40450.v` — printed in editions [1951]:**

> MacINTYRE, John Norbert, M.B.E.—b. 1895; ed. Dominica Gram. Sch.; 2nd clk., registr. off., Dominica, 1914; prin., admin. off., 1940; gov. sec., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | 2nd clk., registr. off. | Dominica | [1949, 1950, 1951] |
| 1 | 1940 | prin., admin. off | Dominica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1944 | gov. sec | Dominica *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `McIntyre, J. N___Leeward Islands___1936`

- Staff-list name: **McIntyre, J. N** | colony: **Leeward Islands** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. N. McIntyre | Accountant | Treasury and Customs | — | — |
| 1939 | J. N. McIntyre | Senior Clerks | Treasury and Customs | — | — |

### Deterministic checks: `mcintyre_john-norbert_b1895` vs `McIntyre, J. N___Leeward Islands___1936`

- [PASS] surname_gate: bio 'McINTYRE' vs stint 'McIntyre, J. N' (exact)
- [PASS] initials: bio ['J', 'N'] ~ stint ['J', 'N']
- [PASS] age_gate: stint starts 1936, birth 1895 (age 41)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McIntyre, J___Australia___1912`

- Staff-list name: **McIntyre, J** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Hon. J. McIntyre | Puisne Judges | Judicial and Legal Departments | — | — |
| 1913 | Hon. J. McIntyre | Puisne Judges | Judicial and Legal Departments | — | — |

### Deterministic checks: `mcintyre_john-norbert_b1895` vs `McIntyre, J___Australia___1912`

- [PASS] surname_gate: bio 'McINTYRE' vs stint 'McIntyre, J' (exact)
- [PASS] initials: bio ['J', 'N'] ~ stint ['J']
- [PASS] age_gate: stint starts 1912, birth 1895 (age 17)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

