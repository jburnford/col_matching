<!-- {"case_id": "case_sedgewick_robert_e1888", "bio_ids": ["sedgewick_robert_e1888"], "stint_ids": ["Sedgewick, Robert___Canada___1898"]} -->
# Dossier case_sedgewick_robert_e1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sedgewick_robert_e1888'] carry a single initial only — the namesake trap applies.

## Biography `sedgewick_robert_e1888`

- Printed name: **SEDGEWICK, ROBERT**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1896-L41253.v` — printed in editions [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]:**

> SEDGEWICK, ROBERT, Q.C.—Deputy minister of justice and solicitor of Indian affairs, Canada, 1888; now a puisne judge, supreme court.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | Deputy minister of justice and solicitor of Indian affairs | Canada | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Sedgewick, Robert___Canada___1898`

- Staff-list name: **Sedgewick, Robert** | colony: **Canada** | listed 1898–1906 | editions [1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Robert Sedgewick | Puisne Judge | Supreme Court of Canada | — | — |
| 1899 | Robert Sedgewick | Puisne Judge | Supreme Court of Canada | — | — |
| 1900 | Robert Sedgewick | Puisne Judge | Supreme Court of Canada | — | — |
| 1905 | Robert Sedgewick | Puisne Judge | Supreme Court of Canada | — | — |
| 1906 | Robert Sedgewick | Puisne Judge | Supreme Court of Canada | — | — |

### Deterministic checks: `sedgewick_robert_e1888` vs `Sedgewick, Robert___Canada___1898`

- [PASS] surname_gate: bio 'SEDGEWICK' vs stint 'Sedgewick, Robert' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1906
- [FAIL] position_sim: best 24 vs bar 60: 'Deputy minister of justice and solicitor of Indian affairs' ~ 'Puisne Judge'
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

