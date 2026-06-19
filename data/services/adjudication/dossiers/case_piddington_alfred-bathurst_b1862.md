<!-- {"case_id": "case_piddington_alfred-bathurst_b1862", "bio_ids": ["piddington_alfred-bathurst_b1862"], "stint_ids": ["Saddington, Blanche___Barbados___1923"]} -->
# Dossier case_piddington_alfred-bathurst_b1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `piddington_alfred-bathurst_b1862`

- Printed name: **PIDDINGTON, ALFRED BATHURST**
- Birth year: 1862 (attested in editions [1919, 1920, 1922])
- Appears in editions: [1919, 1920, 1922]

### Verbatim printed entry text (OCR)

**Version `col1919-L55075.v` — printed in editions [1919, 1920, 1922]:**

> PIDDINGTON, ALFRED BATHURST, K.C.—B. 1862; chief comsnr. of the interstate comsnr., Commonwealth of Australia, Aug., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | chief comsnr. of the interstate comsnr. | Commonwealth of Australia | [1919, 1920, 1922] |

## Candidate stint `Saddington, Blanche___Barbados___1923`

- Staff-list name: **Saddington, Blanche** | colony: **Barbados** | listed 1923–1924 | editions [1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | Blanche Saddington | Preparatory Mistresses | Educational | — | — |
| 1924 | Blanche Saddington | Preparatory Mistress | Educational | — | — |

### Deterministic checks: `piddington_alfred-bathurst_b1862` vs `Saddington, Blanche___Barbados___1923`

- [PASS] surname_gate: bio 'PIDDINGTON' vs stint 'Saddington, Blanche' (fuzzy:2)
- [PASS] initials: bio ['A', 'B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1923, birth 1862 (age 61)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1924
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

