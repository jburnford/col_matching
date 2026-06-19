<!-- {"case_id": "case_ayre_andrew-fawcett_e1883", "bio_ids": ["ayre_andrew-fawcett_e1883"], "stint_ids": ["Ayre, A. F___Straits Settlements___1888"]} -->
# Dossier case_ayre_andrew-fawcett_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ayre_andrew-fawcett_e1883`

- Printed name: **AYRE, ANDREW FAWCETT**
- Birth year: not printed
- Honours: A.M.I.C.E
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L31993.v` — printed in editions [1886]:**

> AYRE, ANDREW FAWCETT.—Educated at Archbishop Holgate's College, York; associate member of the Institute of Civil Engineers, 1883; appointed superintendent of works and surveys in Malacca, Straits Settlements, June, 1883.

**Version `col1888-L31906.v` — printed in editions [1888, 1889, 1890]:**

> AYRE, ANDREW FAWCETT, A.M.I.C.E.—Educated at Archbishop Holgate's College, York; superintendent of works and surveys in Malacca, Straits Settlements, June, 1883; acting superintendent of works and surveys, Singapore, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | associate member of the Institute of Civil Engineers | — | [1886] |
| 1 | 1883 | appointed superintendent of works and surveys in Malacca | Straits Settlements | [1886, 1888, 1889, 1890] |
| 2 | 1885 | acting superintendent of works and surveys | Singapore | [1888, 1889, 1890] |

## Candidate stint `Ayre, A. F___Straits Settlements___1888`

- Staff-list name: **Ayre, A. F** | colony: **Straits Settlements** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | A. F. Ayre | Superintendent of Works and Surveys | Malacca | — | — |
| 1889 | A. F. Ayre | Official | Malacca | — | — |

### Deterministic checks: `ayre_andrew-fawcett_e1883` vs `Ayre, A. F___Straits Settlements___1888`

- [PASS] surname_gate: bio 'AYRE' vs stint 'Ayre, A. F' (exact)
- [PASS] initials: bio ['A', 'F'] ~ stint ['A', 'F']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

