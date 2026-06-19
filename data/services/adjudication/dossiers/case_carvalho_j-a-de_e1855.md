<!-- {"case_id": "case_carvalho_j-a-de_e1855", "bio_ids": ["carvalho_j-a-de_e1855"], "stint_ids": ["Carvalho, J. A___Hong Kong___1877"]} -->
# Dossier case_carvalho_j-a-de_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carvalho_j-a-de_e1855`

- Printed name: **CARVALHO, J. A. DE.**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1886-L32583.v` — printed in editions [1886]:**

> CARVALHO, J. A. DE.—Appointed second clerk and accountant in the treasury, Hong Kong, Aug. 16th, 1855; promoted to first clerk and cashier, January 16th, 1860; appointed assistant superintendent fire brigade, Sept. 12th, 1875, which appointment he resigned on Dec. 31st, 1883; created a J.P. for the colony, Dec., 1883.

**Version `col1888-L32547.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899]:**

> CARVALHO, J. A. DE.—Second clerk and accountant in the treasury, Hong Kong, Aug. 16, 1855; first clerk and cashier, Jan. 16, 1860; assistant superintendent fire brigade, Sept. 1875, to Dec., 1883; J.P. for the colony, Dec., 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | second clerk and accountant in the treasury | Hong Kong | [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 1 | 1860 | first clerk and cashier | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 2 | 1875–1883 | assistant superintendent fire brigade | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 3 | 1883 | J.P. for the colony | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |

## Candidate stint `Carvalho, J. A___Hong Kong___1877`

- Staff-list name: **Carvalho, J. A** | colony: **Hong Kong** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1878 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1879 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1880 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1883 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1883 | J. A. Carvalho | Assistant Superintendent | Fire Brigade | — | — |
| 1886 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1888 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1889 | J. A. Carvalho | 1st Clerk and Cashier | Treasurer's Department | — | — |
| 1890 | J. A. Carvalho | Clerk and Cashier | Treasurer's Department | — | — |

### Deterministic checks: `carvalho_j-a-de_e1855` vs `Carvalho, J. A___Hong Kong___1877`

- [PASS] surname_gate: bio 'CARVALHO' vs stint 'Carvalho, J. A' (exact)
- [PASS] initials: bio ['J', 'A', 'D'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1890
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

