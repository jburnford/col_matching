<!-- {"case_id": "case_imlach_robert-wright_e1850", "bio_ids": ["imlach_robert-wright_e1850"], "stint_ids": ["Imlach, R. W___British Guiana___1877"]} -->
# Dossier case_imlach_robert-wright_e1850

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `imlach_robert-wright_e1850`

- Printed name: **IMLACH, Robert Wright**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L28107.v` — printed in editions [1883, 1886, 1889, 1890]:**

> IMLACH, Robert Wright.—Crown solicitor, British Guiana, 13 April, 1850.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850 | Crown solicitor | British Guiana | [1883, 1886, 1889, 1890] |

## Candidate stint `Imlach, R. W___British Guiana___1877`

- Staff-list name: **Imlach, R. W** | colony: **British Guiana** | listed 1877–1886 | editions [1877, 1878, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. W. Imlach | Crown Solicitor | Judicial Establishment | — | — |
| 1877 | R. W. Imlach | Adjutant-General | Militia | — | — |
| 1878 | R. W. Imlach | Crown Solicitor | Judicial Establishment | — | — |
| 1880 | R. W. Imlach | Crown Solicitor | Judicial Establishment | — | — |
| 1883 | R. W. Imlach | Crown Solicitor | Judicial Establishment | — | — |
| 1886 | R. W. Imlach | Crown Solicitor | Judicial Establishment | — | — |

### Deterministic checks: `imlach_robert-wright_e1850` vs `Imlach, R. W___British Guiana___1877`

- [PASS] surname_gate: bio 'IMLACH' vs stint 'Imlach, R. W' (exact)
- [PASS] initials: bio ['R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
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

