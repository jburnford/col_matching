<!-- {"case_id": "case_hole_hugh-marshall_e1890", "bio_ids": ["hole_hugh-marshall_e1890"], "stint_ids": ["Hole, H. Marshall___Rhodesia___1908", "Hole, Hugh___Leeward Islands___1939"]} -->
# Dossier case_hole_hugh-marshall_e1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hole_hugh-marshall_e1890`

- Printed name: **HOLE, HUGH MARSHALL**
- Birth year: not printed
- Terminal: retired 1919 — “ret. with rank of lieut.-col., 1919.”
- Appears in editions: [1923]

### Verbatim printed entry text (OCR)

**Version `col1923-L55269.v` — printed in editions [1923]:**

> HOLE, HUGH MARSHALL.—Ed. at Blundell's Schl. and Balliol Coll., Oxford; joined B.S.A. Co.'s service, Apr., 1890; sec. to admstr. of Mashonaland (Dr. Jameson), 1891; civ. comsnr. and mag., Salisbury, 1893; civ. comsnr., Bulawayo, 1901; ag. admstr., N.W. Rhodesia, 1903-4 and in 1907; ret. owing to ill health, and joined staff of B.S.A. Co. in London, 1913; served with Rhodesian Horse in native rebellion, 1896, in Boer War, 1899-1900, and in European War, 1915-18; ret. with rank of lieut.-col., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | joined B.S.A. Co.'s service | — | [1923] |
| 1 | 1891 | sec. to admstr. | Mashonaland | [1923] |
| 2 | 1893 | civ. comsnr. and mag. | Salisbury | [1923] |
| 3 | 1896–1918 | served with Rhodesian Horse | — | [1923] |
| 4 | 1901 | civ. comsnr. | Bulawayo | [1923] |
| 5 | 1903–1907 | ag. admstr. | North-West Rhodesia | [1923] |
| 6 | 1913 | staff | London | [1923] |
| 7 | 1919 | rank of lieut.-col. | — | [1923] |

## Candidate stint `Hole, H. Marshall___Rhodesia___1908`

- Staff-list name: **Hole, H. Marshall** | colony: **Rhodesia** | listed 1908–1910 | editions [1908, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | H. Marshall Hole | Civil Commissioner | District Courts and Offices | — | — |
| 1910 | H. Marshall Hole | Secretary | Administrator's Department | — | — |

### Deterministic checks: `hole_hugh-marshall_e1890` vs `Hole, H. Marshall___Rhodesia___1908`

- [PASS] surname_gate: bio 'HOLE' vs stint 'Hole, H. Marshall' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hole, Hugh___Leeward Islands___1939`

- Staff-list name: **Hole, Hugh** | colony: **Leeward Islands** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | Hugh Hole | Member | Non-Official Members | — | Major |
| 1940 | Hugh Hole | — | Legislative Council (Local) | — | Major |

### Deterministic checks: `hole_hugh-marshall_e1890` vs `Hole, Hugh___Leeward Islands___1939`

- [PASS] surname_gate: bio 'HOLE' vs stint 'Hole, Hugh' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H']
- [PASS] age_gate: stint starts 1939; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

