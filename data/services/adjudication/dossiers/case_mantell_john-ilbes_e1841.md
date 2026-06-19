<!-- {"case_id": "case_mantell_john-ilbes_e1841", "bio_ids": ["mantell_john-ilbes_e1841"], "stint_ids": ["Mantell, J___Ceylon___1877"]} -->
# Dossier case_mantell_john-ilbes_e1841

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mantell_john-ilbes_e1841`

- Printed name: **MANTELL, JOHN ILBES**
- Birth year: not printed
- Honours: KNT (1867)
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34781.v` — printed in editions [1888, 1889, 1890]:**

> MANTELL, SIR JOHN ILBES, KNT. (1867)—Queen's advocate, Gambia, 1841 to 1847; chief justice, 1847 to 1867; stipendiary magistrate, Manchester, 1869-1885.

**Version `col1883-L28585.v` — printed in editions [1883, 1886]:**

> MANTELL, Sir JOHN I., Knt. (1867).—Queen's advocate, Gambia, 1841 to 1847; chief justice, 1847 to 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1841–1847 | Queen's advocate | Gambia | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1847–1867 | chief justice | Gambia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1869–1885 | stipendiary magistrate, Manchester | Gambia *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Mantell, J___Ceylon___1877`

- Staff-list name: **Mantell, J** | colony: **Ceylon** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Mantell | Assistant Surveyor | Survey Department | — | — |
| 1878 | J. Mantell | District Surveyor | Survey Department | — | — |
| 1879 | J. Mantell | District Surveyor | District Surveyors | — | — |

### Deterministic checks: `mantell_john-ilbes_e1841` vs `Mantell, J___Ceylon___1877`

- [PASS] surname_gate: bio 'MANTELL' vs stint 'Mantell, J' (exact)
- [PASS] initials: bio ['J', 'I'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

