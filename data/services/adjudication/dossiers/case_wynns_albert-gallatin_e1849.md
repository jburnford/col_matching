<!-- {"case_id": "case_wynns_albert-gallatin_e1849", "bio_ids": ["wynns_albert-gallatin_e1849"], "stint_ids": ["Wynns, A. G___Turks and Caicos Islands___1877"]} -->
# Dossier case_wynns_albert-gallatin_e1849

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wynns_albert-gallatin_e1849`

- Printed name: **WYNNS, ALBERT GALLATIN**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L30083.v` — printed in editions [1883]:**

> WYNNS, ALBERT GALLATIN.—Acting comptroller of customs and navigation laws in Aug., 1851, Grand Turk; assistant crown commissioner in May, 1852; acting crown commissioner from June, 1860, until September, 1861; colonial surveyor and inspector of public works, September, 1863; private secretary, President Campbell, from June, 1872, to Dec., 1873; assistant commissioner to perform the duties of colonial surveyor and inspector of public works, 1st January, 1874, together with those of police magistrate and provost-marshal; elected member of legislative council, 1849 to 1852; member of executive council, 1873; is a member of the legislative board.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1849–1852 | elected member of legislative council | — | [1883] |
| 1 | 1851–1851 | Acting comptroller of customs and navigation laws | Grand Turk | [1883] |
| 2 | 1852–1852 | assistant crown commissioner | — | [1883] |
| 3 | 1860–1861 | acting crown commissioner | — | [1883] |
| 4 | 1863–1863 | colonial surveyor and inspector of public works | — | [1883] |
| 5 | 1872–1873 | private secretary, President Campbell | — | [1883] |
| 6 | 1873–1873 | member of executive council | — | [1883] |
| 7 | 1874 | assistant commissioner | — | [1883] |

## Candidate stint `Wynns, A. G___Turks and Caicos Islands___1877`

- Staff-list name: **Wynns, A. G** | colony: **Turks and Caicos Islands** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. G. Wynns | — | Legislative Board | — | — |
| 1877 | A. G. Wynns | Assistant Commissioner at Grand Turk | Civil Establishment | — | — |
| 1878 | A. G. Wynns | — | Legislative Board | — | — |
| 1878 | A. G. Wynns | Assistant Commissioner | Civil Establishment | — | — |
| 1879 | A. G. Wynns | — | Legislative Board | — | — |
| 1879 | A. G. Wynns | Assistant Commissioner | Civil Establishment | — | — |
| 1880 | A. G. Wynns | Assistant Commissioner at Grand Turk | Civil Establishment | — | — |
| 1883 | A. G. Wynns | Member | Legislative Board | — | — |
| 1883 | A. G. Wynns | Assistant Commissioner at Grand Turk | Civil Establishment | — | — |

### Deterministic checks: `wynns_albert-gallatin_e1849` vs `Wynns, A. G___Turks and Caicos Islands___1877`

- [PASS] surname_gate: bio 'WYNNS' vs stint 'Wynns, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Turks and Caicos Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

