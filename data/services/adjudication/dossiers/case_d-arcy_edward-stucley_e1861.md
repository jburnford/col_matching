<!-- {"case_id": "case_d-arcy_edward-stucley_e1861", "bio_ids": ["d-arcy_edward-stucley_e1861"], "stint_ids": ["D'Arcy, E. S___Cape of Good Hope___1877"]} -->
# Dossier case_d-arcy_edward-stucley_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `d-arcy_edward-stucley_e1861`

- Printed name: **D'ARCY, EDWARD STUCLEY**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1883-L27078.v` — printed in editions [1883, 1886, 1888, 1889]:**

> D'ARCY, EDWARD STUCLEY.—Clerk in the office of the secretary to government, and auditor of British Kaffraria, Sept., 1861; 2nd class clerk, customs department, Port Elizabeth, Cape of Good Hope, June, 1866; first clerk, principal controller's office, June, 1870; acting resident magistrate and sub-collector of customs, Simon's Town, 1874; chief clerk, port off Cape Town, Jan., 1875; upon active service as lieutenant, Duke of Edinburgh's Own Volunteer Rifles in the Transkeian Territory, 1879; extra aide-de-camp to H.E. the Governor, 17th July, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Clerk in the office of the secretary to government, and auditor of British Kaffraria | — | [1883, 1886, 1888, 1889] |
| 1 | 1866 | 2nd class clerk, customs department, Port Elizabeth | Cape of Good Hope | [1883, 1886, 1888, 1889] |
| 2 | 1870 | first clerk, principal controller's office | Cape of Good Hope *(inherited from previous clause)* | [1883, 1886, 1888, 1889] |
| 3 | 1874 | acting resident magistrate and sub-collector of customs, Simon's Town | Cape of Good Hope *(inherited from previous clause)* | [1883, 1886, 1888, 1889] |
| 4 | 1875 | chief clerk, port off Cape Town | Cape of Good Hope *(inherited from previous clause)* | [1883, 1886, 1888, 1889] |
| 5 | 1879 | upon active service as lieutenant, Duke of Edinburgh's Own Volunteer Rifles in the Transkeian Territory | Cape of Good Hope *(inherited from previous clause)* | [1883, 1886, 1888, 1889] |

## Candidate stint `D'Arcy, E. S___Cape of Good Hope___1877`

- Staff-list name: **D'Arcy, E. S** | colony: **Cape of Good Hope** | listed 1877–1889 | editions [1877, 1878, 1880, 1883, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. S. D'Arcy | Chief Clerk and Warehousekeeper | Port of Cape Town | — | — |
| 1878 | E. S. D'Arcy | Chief Clerk and Warehousekeeper | Port of Cape Town | — | — |
| 1880 | E. S. D'Arcy | Chief Clerk and Warehousekeeper | Port of Cape Town | — | — |
| 1883 | E. S. D'Arcy | Chief Clerk and Warehousekeeper | PORT OF CAPE TOWN | — | — |
| 1888 | E. S. D'Arcy | Chief Clerk and Warehousekeeper | General Management Department | — | — |
| 1889 | E. S. D'Arcy | Chief Clerk and Warehousekeeper | PORT OF CAPE TOWN | — | — |

### Deterministic checks: `d-arcy_edward-stucley_e1861` vs `D'Arcy, E. S___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'D'ARCY' vs stint 'D'Arcy, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1889
- [FAIL] position_sim: best 56 vs bar 60: 'chief clerk, port off Cape Town' ~ 'Chief Clerk and Warehousekeeper'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

