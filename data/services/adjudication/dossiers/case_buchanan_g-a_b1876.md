<!-- {"case_id": "case_buchanan_g-a_b1876", "bio_ids": ["buchanan_g-a_b1876"], "stint_ids": ["Buchanan, A___South Australia___1894", "Buchanan, G. A___Southern Nigeria___1912"]} -->
# Dossier case_buchanan_g-a_b1876

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `buchanan_g-a_b1876`

- Printed name: **BUCHANAN, G. A**
- Birth year: 1876 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L62878.v` — printed in editions [1931]:**

> BUCHANAN, G. A.—B. 1876; ed. Dumbarton Acad. and Glasgow and West of Scotland Tech. Coll.; asst. engr., Lagos rly., 1911; divnl. engr., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. engr., Lagos rly | Lagos | [1931] |
| 1 | 1927 | divnl. engr | Lagos *(inherited from previous clause)* | [1931] |

## Candidate stint `Buchanan, A___South Australia___1894`

- Staff-list name: **Buchanan, A** | colony: **South Australia** | listed 1894–1917 | editions [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | A. Buchanan | Master of Supreme Court | Supreme Court Department | — | — |
| 1896 | A. Buchanan | Master of Supreme Court | Supreme Court Department | — | — |
| 1897 | A. Buchanan | Chief Justice | Supreme Court Department | — | — |
| 1898 | A. Buchanan | Master of Supreme Court | Supreme Court Department | — | — |
| 1899 | A. Buchanan | Master of Supreme Court | Supreme Court Department | — | — |
| 1900 | A. Buchanan | Master of Supreme Court | Supreme Court Department | — | — |
| 1905 | A. Buchanan | Master of Supreme Court, also Registrar of Probates | Supreme Court Department | — | — |
| 1905 | A. Buchanan | Registrar of Probates (also Master of Supreme Court) | Probate and Succession Duties Office | — | — |
| 1906 | A. Buchanan | Master of Supreme Court (also Registrar of Probates) | Supreme Court Department | — | — |
| 1906 | A. Buchanan | Registrar of Probates (also Master of Supreme Court) | Probate and Succession Duties Office | — | — |
| 1907 | A. Buchanan | Master of Supreme Court (also Registrar of Probates, 150l.) | Supreme Court Department | — | — |
| 1907 | A. Buchanan | Registrar of Probates (also Master of Supreme Court, 700l.) | Probate and Succession Duties Office | — | — |
| 1908 | A. Buchanan | Master of Supreme Court (also Registrar of Probates, 150l.) | Supreme Court Department | — | — |
| 1908 | A. Buchanan | Registrar of Probates (also Master of Supreme Court, 700l.) | Probate and Succession Duties Office | — | — |
| 1909 | A. Buchanan | Registrar of Probates (also Master of Supreme Court, 700l.) | Probate and Succession Duties Office | — | — |
| 1909 | A. Buchanan | Master of Supreme Court (also Registrar of Probates) | Supreme Court Department | — | — |
| 1917 | Hon. A. Buchanan | Judge | Judges of the Supreme Court | — | — |

### Deterministic checks: `buchanan_g-a_b1876` vs `Buchanan, A___South Australia___1894`

- [PASS] surname_gate: bio 'BUCHANAN' vs stint 'Buchanan, A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1894, birth 1876 (age 18)
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1917
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Buchanan, G. A___Southern Nigeria___1912`

- Staff-list name: **Buchanan, G. A** | colony: **Southern Nigeria** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | G. A. Buchanan | Assistant Engineer | Engineering Department | — | — |
| 1913 | G. A. Buchanan | Assistant Engineer | Railway | — | — |

### Deterministic checks: `buchanan_g-a_b1876` vs `Buchanan, G. A___Southern Nigeria___1912`

- [PASS] surname_gate: bio 'BUCHANAN' vs stint 'Buchanan, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1912, birth 1876 (age 36)
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
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

