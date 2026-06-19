<!-- {"case_id": "case_trott_henry_e1839", "bio_ids": ["trott_henry_e1839", "trott_john-henry_e1830"], "stint_ids": ["Trott, John H___Bermuda___1877"]} -->
# Dossier case_trott_henry_e1839

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['trott_henry_e1839'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Trott, John H___Bermuda___1877'] have more than one claimant biography in this case.

## Biography `trott_henry_e1839`

- Printed name: **TROTT, HENRY**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29796.v` — printed in editions [1883]:**

> TROTT, HENRY.—Provost-marshal, general of Bermuda, 16 Jan., 1839. Is also receiver of crown quit-rents of the colony, and marshal of the instance court, vice-admiralty.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1839 | Provost-marshal, general | Bermuda | [1883] |

## Biography `trott_john-henry_e1830`

- Printed name: **TROTT, JOHN HENRY**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L36040.v` — printed in editions [1886, 1888]:**

> TROTT, JOHN HENRY.—Provost-marshal, general of Bermuda, 16 Jan., 1830. Is also receiver of crown quit-rents of the colony, and marshal of the instance court, vice-admiralty.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1830 | Provost-marshal, general | Bermuda | [1886, 1888] |

## Candidate stint `Trott, John H___Bermuda___1877`

- Staff-list name: **Trott, John H** | colony: **Bermuda** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1883, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John H. Trott | Provost-Marshal | Judicial Establishment | — | — |
| 1877 | J. H. Trott | Marshal | Judicial Establishment | — | — |
| 1878 | J. H. Trott | Marshal | Judicial Establishment | — | — |
| 1878 | John H. Trott | Provost-Marshal | Judicial Establishment | — | — |
| 1879 | John H. Trott | Provost-Marshal | Judicial Establishment | — | — |
| 1879 | J. H. Trott | Marshal | Judicial Establishment | — | — |
| 1880 | John H. Trott | Provost-Marshal | Judicial Establishment | — | — |
| 1880 | J. H. Trott | Marshal | Judicial Establishment | — | — |
| 1883 | John H. Trott | Provost-Marshal | Judicial Establishment | — | — |
| 1883 | J. H. Trott | Marshal | Judicial Establishment | — | — |
| 1888 | John H. Trott | Provost-Marshal | Judicial Establishment | — | — |
| 1888 | J. H. Trott | Marshal | Judicial Establishment | — | — |

### Deterministic checks: `trott_henry_e1839` vs `Trott, John H___Bermuda___1877`

- [PASS] surname_gate: bio 'TROTT' vs stint 'Trott, John H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `trott_john-henry_e1830` vs `Trott, John H___Bermuda___1877`

- [PASS] surname_gate: bio 'TROTT' vs stint 'Trott, John H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

