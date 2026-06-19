<!-- {"case_id": "case_routledge_robert-m_e1879", "bio_ids": ["routledge_robert-m_e1879"], "stint_ids": ["Routledge, R. M___Trinidad and Tobago___1899", "Routledge, R. M___Trinidad___1894"]} -->
# Dossier case_routledge_robert-m_e1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `routledge_robert-m_e1879`

- Printed name: **ROUTLEDGE, ROBERT M**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1894-L33753.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]:**

> ROUTLEDGE, ROBERT M.—Ed. at Abdin Univ.; called to the bar, Lincoln's Inn, Nov., 1879; judge and mag., Falklands, June, 1891; judge, mag., and col. sec., Dec., 1891; stip. mag., Trinidad, 1893; acted as puisne judge on several occasions, 1894 to 1901; puisne judge, Mar., 1901; ag. ch. just., 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | called to the bar, Lincoln's Inn | — | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 1 | 1891 | judge and mag., Falklands | — | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 2 | 1893 | stip. mag. | Trinidad | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 3 | 1894–1901 | acted as puisne judge on several occasions | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 4 | 1901 | puisne judge | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 5 | 1903 | ag. ch. just | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |

## Candidate stint `Routledge, R. M___Trinidad and Tobago___1899`

- Staff-list name: **Routledge, R. M** | colony: **Trinidad and Tobago** | listed 1899–1906 | editions [1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | R. M. Routledge | Stipendiary Justice | Stipendiary Justices | — | — |
| 1900 | R. M. Routledge | Stipendiary Justice | Judicial Department | — | — |
| 1905 | R. M. Routledge | 1st Puisne Judge | Judicial Department | — | — |
| 1906 | R. M. Routledge | 1st Puisne Judge | Judicial Department | — | — |

### Deterministic checks: `routledge_robert-m_e1879` vs `Routledge, R. M___Trinidad and Tobago___1899`

- [PASS] surname_gate: bio 'ROUTLEDGE' vs stint 'Routledge, R. M' (exact)
- [PASS] initials: bio ['R', 'M'] ~ stint ['R', 'M']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1906
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Routledge, R. M___Trinidad___1894`

- Staff-list name: **Routledge, R. M** | colony: **Trinidad** | listed 1894–1898 | editions [1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | R. M. Routledge | Stipendiary Justice | Stipendiary Justices | — | — |
| 1896 | R. M. Routledge | Stipendiary Justice | Stipendiary Justices | — | — |
| 1897 | R. M. Routledge | Stipendiary Justice | Stipendiary Justices | — | — |
| 1898 | R. M. Routledge | Stipendiary Justice | Stipendiary Justices | — | — |

### Deterministic checks: `routledge_robert-m_e1879` vs `Routledge, R. M___Trinidad___1894`

- [PASS] surname_gate: bio 'ROUTLEDGE' vs stint 'Routledge, R. M' (exact)
- [PASS] initials: bio ['R', 'M'] ~ stint ['R', 'M']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1894-1898
- [FAIL] position_sim: best 37 vs bar 60: 'stip. mag.' ~ 'Stipendiary Justice'
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

