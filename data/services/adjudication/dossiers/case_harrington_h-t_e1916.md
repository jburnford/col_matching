<!-- {"case_id": "case_harrington_h-t_e1916", "bio_ids": ["harrington_h-t_e1916"], "stint_ids": ["Harrington, H. T___Rhodesia___1905"]} -->
# Dossier case_harrington_h-t_e1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harrington_h-t_e1916`

- Printed name: **HARRINGTON, H. T**
- Birth year: not printed
- Appears in editions: [1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1918-L51169.v` — printed in editions [1918, 1919]:**

> HARRINGTON, H. T.—Asst. dist. commnr., E.A.P., Sept., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | Asst. dist. commnr. | East Africa Protectorate | [1918, 1919] |

## Candidate stint `Harrington, H. T___Rhodesia___1905`

- Staff-list name: **Harrington, H. T** | colony: **Rhodesia** | listed 1905–1910 | editions [1905, 1906, 1908, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. T. Harrington | Civil and Native Commissioner | District Courts and Offices | — | — |
| 1906 | H. T. Harrington | Civil and Native Commissioner | District Courts and Offices | — | — |
| 1908 | H. T. Harrington | Civil and Native Commissioner and Assistant Magistrate | NORTH-EASTERN RHODESIA | — | — |
| 1910 | H. T. Harrington | Civil and Native Commissioner and Assistant Magistrate | District Courts and Offices | — | — |

### Deterministic checks: `harrington_h-t_e1916` vs `Harrington, H. T___Rhodesia___1905`

- [PASS] surname_gate: bio 'HARRINGTON' vs stint 'Harrington, H. T' (exact)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1910
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

