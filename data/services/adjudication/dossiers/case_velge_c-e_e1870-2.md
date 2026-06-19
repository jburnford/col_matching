<!-- {"case_id": "case_velge_c-e_e1870-2", "bio_ids": ["velge_c-e_e1870-2"], "stint_ids": ["Velge, C. E___Straits Settlements___1877"]} -->
# Dossier case_velge_c-e_e1870-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Velge, C. E___Straits Settlements___1877` is also gate-compatible with biography(ies) outside this case: ['velge_c-e_e1870'] (already linked elsewhere or filtered).

## Biography `velge_c-e_e1870-2`

- Printed name: **VELGE, C. E.**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907]

### Verbatim printed entry text (OCR)

**Version `col1905-L46435.v` — printed in editions [1905, 1906, 1907]:**

> VELGE, C. E.—Called to the bar, Mid. Tem., Michaelmas, 1870; reg'ar., sup. ct., Singapore, May, 1875; ditto, S. Stiltns., 1st Mar., 1896.

**Version `col1896-L41760.v` — printed in editions [1896, 1897, 1898, 1899, 1900]:**

> VELGE, C. E.—Called to the bar, Middle Temple, Michaelmas, 1870, registrar, sup. ct., Singapore, 4th May, 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870 | Called to the bar, Mid. Tem., Michaelmas | — | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |
| 1 | 1875 | reg'ar., sup. ct. | Singapore | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907] |
| 2 | 1896 | ditto, S. Stiltns | Singapore *(inherited from previous clause)* | [1905, 1906, 1907] |

## Candidate stint `Velge, C. E___Straits Settlements___1877`

- Staff-list name: **Velge, C. E** | colony: **Straits Settlements** | listed 1877–1908 | editions [1877, 1878, 1880, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1878 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1880 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1888 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1889 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1890 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1894 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1896 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1897 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1898 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1899 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1905 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1907 | C. E. Velge | Registrar | Judicial Department | — | — |
| 1908 | C. E. Velge | Registrar | Judicial Department | — | — |

### Deterministic checks: `velge_c-e_e1870-2` vs `Velge, C. E___Straits Settlements___1877`

- [PASS] surname_gate: bio 'VELGE' vs stint 'Velge, C. E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1908
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

