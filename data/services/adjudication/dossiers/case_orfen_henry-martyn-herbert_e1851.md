<!-- {"case_id": "case_orfen_henry-martyn-herbert_e1851", "bio_ids": ["orfen_henry-martyn-herbert_e1851"], "stint_ids": ["Orpen, H. M. H___Cape of Good Hope___1877", "Orpen, H. M. H___Cape of Good Hope___1896"]} -->
# Dossier case_orfen_henry-martyn-herbert_e1851

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Orpen, H. M. H___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['orpen_henry-martyn-herbert_e1851'] (already linked elsewhere or filtered).
- NOTE: stint `Orpen, H. M. H___Cape of Good Hope___1896` is also gate-compatible with biography(ies) outside this case: ['orpen_henry-martyn-herbert_e1851'] (already linked elsewhere or filtered).

## Biography `orfen_henry-martyn-herbert_e1851`

- Printed name: **ORFEN, Henry Martyn Herbert**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L33319.v` — printed in editions [1894]:**

> ORFEN, Henry Martyn Herbert.—Captain commanding Colesberg native levies, from Jan., 1851, to Aug., 1853, during the Kaffir war also as district adjutant of North Victoria from April, 1852, to March, 1853; held several other military appointments during the same period; Kaffir war medal; appointed to the customs department at Port Elizabeth, Dec., 1853; landing surveyor August, 1857; sub-collector and surveyor and comptroller of H.M. customs and navigation laws, Cape Town, October, 1867; temporary charge of customs department, April, 1868, assistant treasurer, accountant-general, and stamping commissioner, May, 1876; receiver-general and paymaster-general, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851–1853 | Captain commanding Colesberg native levies | Colesberg | [1894] |
| 1 | 1852–1853 | district adjutant | North Victoria | [1894] |
| 2 | 1853 | appointed to the customs department | Port Elizabeth | [1894] |
| 3 | 1857 | landing surveyor | — | [1894] |
| 4 | 1867 | sub-collector and surveyor and comptroller of H.M. customs and navigation laws | Cape Town | [1894] |
| 5 | 1868 | temporary charge of customs department | — | [1894] |
| 6 | 1876 | assistant treasurer, accountant-general, and stamping commissioner | — | [1894] |
| 7 | 1881 | receiver-general and paymaster-general | — | [1894] |

## Candidate stint `Orpen, H. M. H___Cape of Good Hope___1877`

- Staff-list name: **Orpen, H. M. H** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. M. H. Orpen | Assistant Treasurer | Treasury | — | — |
| 1878 | H. M. H. Orpen | Assistant Treasurer | Treasury | — | — |
| 1880 | H. M. H. Orpen | Assistant Treasurer | Treasury | — | — |

### Deterministic checks: `orfen_henry-martyn-herbert_e1851` vs `Orpen, H. M. H___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'ORFEN' vs stint 'Orpen, H. M. H' (fuzzy:1)
- [PASS] initials: bio ['H', 'M', 'H'] ~ stint ['H', 'M', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Orpen, H. M. H___Cape of Good Hope___1896`

- Staff-list name: **Orpen, H. M. H** | colony: **Cape of Good Hope** | listed 1896–1898 | editions [1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | H. M. H. Orpen | Paymaster-General of the Colony | District of Wynberg | — | — |
| 1896 | H. M. Orpen | Inspector | Excise, Licenses, and Stamps Branch | — | — |
| 1897 | H. M. Orpen | Inspector | Excise, Licenses, and Stamps Branch | — | — |
| 1898 | H. M. H. Orpen | Assistant Treasurer, Accountant-General, Receiver-General, and Paymaster-General of the Colony | Treasury | — | — |

### Deterministic checks: `orfen_henry-martyn-herbert_e1851` vs `Orpen, H. M. H___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'ORFEN' vs stint 'Orpen, H. M. H' (fuzzy:1)
- [PASS] initials: bio ['H', 'M', 'H'] ~ stint ['H', 'M', 'H']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
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

