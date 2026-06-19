<!-- {"case_id": "case_chamberlin_brown_e1867", "bio_ids": ["chamberlin_brown_e1867"], "stint_ids": ["Chamberlin, Brown___Canada___1877"]} -->
# Dossier case_chamberlin_brown_e1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['chamberlin_brown_e1867'] carry a single initial only — the namesake trap applies.

## Biography `chamberlin_brown_e1867`

- Printed name: **CHAMBERLIN, BROWN**
- Birth year: not printed
- Honours: C.M.G. (1870)
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1888-L32592.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> CHAMBERLIN, BROWN, LT.-COL., C.M.G. (1870).—Member House of Commons of Canada for county of Mississquoi, 1867 to 1870; in command 60th Bat. Canadian Active Militia, 1869 to 1871; in 1870 commanded battalion, and for a time the whole force, engaged in repelling Fenian invasion at Eccles Hill, for which created C.M.G.; appointed Queen's printer, and retired from Parliament, 1870; Queen's printer and controller of stationery, with rank as Deputy Minister, July, 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867–1870 | Member House of Commons | Canada | [1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1869–1871 | in command 60th Bat. Canadian Active Militia | Canada | [1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | 1870–1870 | commanded battalion, and for a time the whole force, engaged in repelling Fenian invasion | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 3 | 1870–1870 | Queen's printer | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 4 | 1886 | Queen's printer and controller of stationery | — | [1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Chamberlin, Brown___Canada___1877`

- Staff-list name: **Chamberlin, Brown** | colony: **Canada** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Brown Chamberlin | Queen's Printer | Queen's Printer's Branch | C.M.G. | — |
| 1878 | Brown Chamberlin | Queen's Printer | Queen's Printer's Branch | C.M.G. | — |
| 1879 | Brown Chamberlin | Queen's Printer | Queen's Printer's Branch | C.M.G. | — |
| 1880 | Brown Chamberlin | Queen's Printer | Queen's Printer's Branch | C.M.G. | — |
| 1883 | Brown Chamberlin | Queen's Printer | Queen's Printer's Branch | C.M.G. | Lt. Col. |
| 1886 | Brown Chamberlin | Queen's Printer | Queen's Printer's Branch. | C.M.G. | Lt.-Col. |
| 1888 | Brown Chamberlin | Queen's Printer and Controller of Stationery | Department of Public Printing and Stationery | C.M.G. | Lt.-Col. |
| 1889 | Lt.-Col. Brown Chamberlin | Queen's Printer and Controller of Stationery | Public Printing and Stationery | C.M.G. | Lt.-Col. |
| 1890 | Lt.-Col. Brown Chamberlin | Queen's Printer and Controller of Stationery | Public Printing and Stationery | C.M.G. | Lt.-Col. |

### Deterministic checks: `chamberlin_brown_e1867` vs `Chamberlin, Brown___Canada___1877`

- [PASS] surname_gate: bio 'CHAMBERLIN' vs stint 'Chamberlin, Brown' (exact)
- [PASS] initials: bio ['B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G.
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

