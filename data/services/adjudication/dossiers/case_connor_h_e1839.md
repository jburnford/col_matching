<!-- {"case_id": "case_connor_h_e1839", "bio_ids": ["connor_h_e1839"], "stint_ids": ["Connor, H___Natal___1879"]} -->
# Dossier case_connor_h_e1839

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['connor_h_e1839'] carry a single initial only — the namesake trap applies.

## Biography `connor_h_e1839`

- Printed name: **CONNOR, H.**
- Birth year: not printed
- Honours: KNT., BACH. (1880)
- Appears in editions: [1883, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L26947.v` — printed in editions [1883, 1888, 1889, 1890]:**

> CONNOR, SIR H., KNT., BACH. (1880), LL.D., Dublin University.—Called to the bar in Ireland, 1839; was chief justice and judicial assessor at the Gold Coast, 1854; was for some time acting governor of that settlement; fourth puisne judge, Cape of Good Hope, 1868; first puisne judge, Natal, 1858, acting chief justice, 1864; chief justice, 1874; also member of the executive council and judge of the vice-admiralty court.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1839–1839 | Called to the bar | Ireland | [1883, 1888, 1889, 1890] |
| 1 | 1854–1854 | chief justice and judicial assessor | Gold Coast | [1883, 1888, 1889, 1890] |
| 2 | 1858–1858 | first puisne judge | Natal | [1883, 1888, 1889, 1890] |
| 3 | 1864–1864 | acting chief justice | — | [1883, 1888, 1889, 1890] |
| 4 | 1868–1868 | fourth puisne judge | Cape of Good Hope | [1883, 1888, 1889, 1890] |
| 5 | 1874–1874 | chief justice | — | [1883, 1888, 1889, 1890] |

## Candidate stint `Connor, H___Natal___1879`

- Staff-list name: **Connor, H** | colony: **Natal** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | H. Connor | Chief Justice | Judicial Department | — | — |
| 1880 | Sir H. Connor | Chief Justice | Judicial Department | — | — |

### Deterministic checks: `connor_h_e1839` vs `Connor, H___Natal___1879`

- [PASS] surname_gate: bio 'CONNOR' vs stint 'Connor, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
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

