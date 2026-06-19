<!-- {"case_id": "case_aggart_john-g_e1888", "bio_ids": ["aggart_john-g_e1888"], "stint_ids": ["Haggart, John Graham___Canada___1877"]} -->
# Dossier case_aggart_john-g_e1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `aggart_john-g_e1888` ↔ `Haggart, John Graham___Canada___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Haggart, John Graham___Canada___1877` is also gate-compatible with biography(ies) outside this case: ['haggart_john-g_e1872'] (already linked elsewhere or filtered).

## Biography `aggart_john-g_e1888`

- Printed name: **AGGART, JOHN G**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L32340.v` — printed in editions [1897]:**

> AGGART, THE HON. JOHN G.—Postmaster-general, Canada, 1888; minister of railways and public works, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | Postmaster-general | Canada | [1897] |
| 1 | 1892 | minister of railways and public works | Canada *(inherited from previous clause)* | [1897] |

## Candidate stint `Haggart, John Graham___Canada___1877`

- Staff-list name: **Haggart, John Graham** | colony: **Canada** | listed 1877–1908 | editions [1877, 1879, 1880, 1883, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John G. Haggart | Member of Parliament | House of Commons | — | — |
| 1879 | John G. Haggart | Member of Parliament | House of Commons | — | — |
| 1880 | John G. Haggart | Member | Constituencies | — | — |
| 1883 | John G. Haggart | Member | Constituencies, Members | — | — |
| 1888 | John G. Haggart | Member of Parliament | House of Commons | — | — |
| 1889 | J. G. Haggart | Postmaster-General | POST OFFICE DEPARTMENT | — | — |
| 1889 | J. G. Haggart | Postmaster General | THE QUEEN'S PRIVY COUNCIL FOR CANADA | — | — |
| 1890 | Hon. John G. Haggart | Member | House of Commons | — | — |
| 1890 | J. G. Haggart | Postmaster General | Queens Privy Council for Canada | — | — |
| 1890 | J. G. Haggart | Postmaster-General | Post Office Department | — | — |
| 1894 | J. G. Haggart | Minister of Railways and Canals | Railways and Canals | — | — |
| 1894 | J. G. Haggart | Minister of Railways and Canals | THE QUEEN'S PRIVY COUNCIL FOR CANADA | — | — |
| 1894 | John G. Haggart | Member of Parliament | House of Commons | — | — |
| 1896 | J. G. Haggart | Minister of Railways and Canals | Railways and Canals | — | — |
| 1896 | J. G. Haggart | Minister of Railways and Canals | RAILWAYS AND CANALS | — | — |
| 1896 | Hon. J. G. Haggart | Minister of Railways and Canals | THE QUEEN'S PRIVY COUNCIL FOR CANADA | — | — |
| 1896 | John G. Haggart | Member | House of Commons | — | — |
| 1897 | John Graham Haggart | Member of Parliament | Parliament | — | — |
| 1898 | John Graham Haggart | Member of Parliament | House of Commons | — | — |
| 1899 | Hon. John Graham Haggart | — | — | — | — |
| 1900 | Hon. John Graham Haggart | — | — | — | — |
| 1900 | Hon. J. G. Haggart | — | Privy Council | — | — |
| 1905 | J. G. Haggart | — | Privy Council Office | — | — |
| 1906 | J. G. Haggart | — | Privy Council Office | — | — |
| 1906 | Haggart | — | — | — | — |
| 1907 | Haggart | Member of Parliament | Legislative | — | — |
| 1908 | John Graham Haggart | — | — | — | — |
| 1908 | J. G. Haggart | Privy Councillor | Privy Council Office | — | — |

### Deterministic checks: `aggart_john-g_e1888` vs `Haggart, John Graham___Canada___1877`

- [PASS] surname_gate: bio 'AGGART' vs stint 'Haggart, John Graham' (fuzzy:1)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1908
- [PASS] position_sim: best 100 vs bar 60: 'Postmaster-general' ~ 'Postmaster-General'
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

