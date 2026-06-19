<!-- {"case_id": "case_blake_richard-henry_e1865", "bio_ids": ["blake_richard-henry_e1865"], "stint_ids": ["Blake, R. H___Leeward Islands___1877"]} -->
# Dossier case_blake_richard-henry_e1865

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blake_richard-henry_e1865`

- Printed name: **BLAKE, RICHARD HENRY**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L26480.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> BLAKE, RICHARD HENRY.—Clerk to the magistrates, Montserrat, 1865; clerk of the market in 1870; clerk to the president, and to the councils 1877; also to the commissioners of waterworks, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | Clerk to the magistrates | Montserrat | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1870 | clerk of the market in | Montserrat *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1877 | clerk to the president, and to the councils | Montserrat *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 3 | 1880 | also to the commissioners of waterworks | Montserrat *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Blake, R. H___Leeward Islands___1877`

- Staff-list name: **Blake, R. H** | colony: **Leeward Islands** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. H. Blake | Clerk of Public Market | Civil Establishment | — | — |
| 1878 | R. H. Blake | Clerk of Public Market | Civil Establishment | — | — |
| 1879 | R. H. Blake | Clerk of Public Market | Civil Establishment | — | — |
| 1880 | R. H. Blake | Clerk of Public Market | Civil Establishment | — | — |

### Deterministic checks: `blake_richard-henry_e1865` vs `Blake, R. H___Leeward Islands___1877`

- [PASS] surname_gate: bio 'BLAKE' vs stint 'Blake, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

