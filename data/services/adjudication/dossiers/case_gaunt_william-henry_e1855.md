<!-- {"case_id": "case_gaunt_william-henry_e1855", "bio_ids": ["gaunt_william-henry_e1855"], "stint_ids": ["Gaunt, W. H___Victoria___1894"]} -->
# Dossier case_gaunt_william-henry_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gaunt_william-henry_e1855`

- Printed name: **GAUNT, WILLIAM HENRY**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27614.v` — printed in editions [1883]:**

> GAUNT, WILLIAM HENRY.—Barrister at law; police magistrate and resident warden for the gold-fields of Victoria; and a justice of the peace for New South Wales; is also a coroner and visiting justice of H.M.'s gaol at Ballarat; entered the gold fields department on 6th July, 1859, placed in charge on 26th July, 1855; warden of gold fields, December, 1855, and police magistrate on 20th June, 1857; held the offices of Chinese protector and commissioner of crown lands, prior to their abolition; and while stationed on the border was a stipendiary and police magistrate for New South Wales; has served in all the gold fields of the colony, and since 1869 has been in charge of the Ballarat district.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855–1855 | placed in charge | — | [1883] |
| 1 | 1855–1855 | warden of gold fields | — | [1883] |
| 2 | 1857–1857 | police magistrate | — | [1883] |
| 3 | 1859–1859 | entered the gold fields department | — | [1883] |
| 4 | 1869 | in charge of the Ballarat district | Ballarat | [1883] |

## Candidate stint `Gaunt, W. H___Victoria___1894`

- Staff-list name: **Gaunt, W. H** | colony: **Victoria** | listed 1894–1905 | editions [1894, 1897, 1898, 1899, 1900, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | W. H. Gaunt | Judges of County Courts, Courts of Mines, and Chairmen of General Sessions | Judges of County Courts, Courts of Mines, and Chairmen of General Sessions | — | — |
| 1897 | W. H. Gaunt | Judges of County Courts, Courts of Mines, and Chairmen of General Sessions | Court of Insolvency | — | — |
| 1898 | W. H. Gaunt | Judges of County Courts, Courts of Mines, and Chairmen of General Sessions | Court of Insolvency | — | — |
| 1899 | W. H. Gaunt | Judges of County Courts, Courts of Mines, and Chairmen of General Sessions | Court of Insolvency | — | — |
| 1900 | W. H. Gaunt | Judges of County Courts, Courts of Mines, and Chairmen of General Sessions | Court of Insolvency | — | — |
| 1905 | W. H. Gaunt | Judge of County Courts, Courts of Mines, and Chairman of General Sessions | Court of Insolvency | — | — |

### Deterministic checks: `gaunt_william-henry_e1855` vs `Gaunt, W. H___Victoria___1894`

- [PASS] surname_gate: bio 'GAUNT' vs stint 'Gaunt, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1905
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

