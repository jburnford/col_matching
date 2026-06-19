<!-- {"case_id": "case_mulder_j-h_e1865", "bio_ids": ["mulder_j-h_e1865"], "stint_ids": ["Mulder, J. H___Leeward Islands___1877"]} -->
# Dossier case_mulder_j-h_e1865

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mulder_j-h_e1865`

- Printed name: **MULDER, J. H.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L35026.v` — printed in editions [1888]:**

> MULDER, J. H.—Clerk to colonial secretary of St. Christopher, Oct., 1865, to Mar., 1869; registrar of Springfield Cemetery, Mar., 1869; clerk to colonial secretary, Nevis, from Mar., 1869, to Mar., 1872; assistant clerk, government office, St. Christopher, from April 1872, to May, 1875; clerk to the registrar, May, 1875; 4th landing waiter, 1881; acting 3rd ditto, 1884; acting 2nd ditto, 1885; acting clerk, treasury, Nov., 1885, to Feb., 1886.

**Version `col1883-L28793.v` — printed in editions [1883, 1886]:**

> MULDER, J. H.—Was clerk to Mr. Rumsey, colonial secretary of St. Christopher, from October, 1865, to March, 1869; appointed registrar of Springfield Cemetery, March, 1869; clerk to colonial secretary, Nevis, from March, 1869, to March, 1872; assistant clerk in the government office, St. Christopher, from April, 1872, to May, 1875; clerk to the registrar, May, 1875; fourth landing waiter, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865–1869 | Clerk to colonial secretary | St. Christopher | [1883, 1886, 1888] |
| 1 | 1869 | registrar of Springfield Cemetery | — | [1883, 1886, 1888] |
| 2 | 1869–1872 | clerk to colonial secretary | Nevis | [1883, 1886, 1888] |
| 3 | 1872–1875 | assistant clerk, government office | St. Christopher | [1883, 1886, 1888] |
| 4 | 1875 | clerk to the registrar | — | [1883, 1886, 1888] |
| 5 | 1881 | 4th landing waiter | — | [1883, 1886, 1888] |
| 6 | 1884 | acting 3rd ditto | — | [1888] |
| 7 | 1885 | acting 2nd ditto | — | [1888] |
| 8 | 1885–1886 | acting clerk, treasury | — | [1888] |

## Candidate stint `Mulder, J. H___Leeward Islands___1877`

- Staff-list name: **Mulder, J. H** | colony: **Leeward Islands** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. H. Mulder | Clerk | Civil Establishment | — | — |
| 1877 | J. H. Mulder | Registrar of Springfield Cemetery | Treasury | — | — |
| 1878 | J. H. Mulder | Registrar of Springfield Cemetery | Treasury | — | — |
| 1878 | J. H. Mulder | Clerk | Civil Establishment | — | — |
| 1879 | J. H. Mulder | Registrar of Springfield Cemetery | Treasury | — | — |
| 1879 | J. H. Mulder | Clerk | Civil Establishment | — | — |
| 1880 | J. H. Mulder | Registrar of Springfield Cemetery | Treasury | — | — |
| 1880 | J. H. Mulder | Clerk | Civil Establishment | — | — |
| 1883 | J. H. Mulder | Registrar of Springfield Cemetery | Treasury | — | — |
| 1883 | J. H. Mulder, jun. | 4th Landing Waiter | Treasury | — | — |
| 1886 | J. H. Mulder, jun. | 4th Landing Waiter | Treasury | — | — |
| 1886 | J. H. Mulder | Registrar of Springfield Cemetery | Treasury | — | — |

### Deterministic checks: `mulder_j-h_e1865` vs `Mulder, J. H___Leeward Islands___1877`

- [PASS] surname_gate: bio 'MULDER' vs stint 'Mulder, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
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

