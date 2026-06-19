<!-- {"case_id": "case_murray_francis-peel_e1879", "bio_ids": ["murray_francis-peel_e1879"], "stint_ids": ["Murray, F___Griqualand West___1879", "Murray, Francis P___Ceylon___1886"]} -->
# Dossier case_murray_francis-peel_e1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 123 official(s) with this surname in the graph's staff lists; 63 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `murray_francis-peel_e1879`

- Printed name: **MURRAY, FRANCIS PEEL**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L28812.v` — printed in editions [1883, 1886, 1888]:**

> MURRAY, FRANCIS PEEL.—Private secretary to the governor of Fiji, 1879-80; deputy high commissioner for the Western Pacific, in Rotuman, June, 1880; acting colonial secretary of Fiji, December, 1880; private secretary to the governor of New Zealand, 1881; private secretary to governor of Ceylon, 1883; secretary to the commission appointed to inquire into the Western Pacific High Commission, 1883.

**Version `col1889-L34775.v` — printed in editions [1889, 1890]:**

> MURRAY, FRANCIS PEEL.—Private secretary to governor, Fiji, 1879-80; deputy high commissioner for the Western Pacific, in Rotumah, June, 1880; acting colonial secretary, Fiji, Dec., 1880; private secretary to the governor of New Zealand, 1881; secretary to commission appointed to inquire into Western Pacific High Commission, 1883; private secretary to governor of Ceylon, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1880 | Private secretary to the governor of Fiji | Fiji | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1880 | deputy high commissioner for the Western Pacific, in Rotuman | Fiji | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1880 | acting colonial secretary of Fiji | — | [1883, 1886, 1888] |
| 3 | 1881 | private secretary to the governor of New Zealand | Fiji *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1883 | private secretary to governor of Ceylon | Fiji *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |
| 5 | 1883 | secretary to the commission appointed to inquire into the Western Pacific High Commission | Fiji *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Murray, F___Griqualand West___1879`

- Staff-list name: **Murray, F** | colony: **Griqualand West** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | F. Murray | Dispenser | Medical Department, Kimberley | — | — |
| 1880 | F. Murray | Dispenser | Medical Department, Kimberley | — | — |

### Deterministic checks: `murray_francis-peel_e1879` vs `Murray, F___Griqualand West___1879`

- [PASS] surname_gate: bio 'MURRAY' vs stint 'Murray, F' (exact)
- [PASS] initials: bio ['F', 'P'] ~ stint ['F']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Griqualand West'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Murray, Francis P___Ceylon___1886`

- Staff-list name: **Murray, Francis P** | colony: **Ceylon** | listed 1886–1888 | editions [1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | Francis P. Murray | Private Secretaries | Civil Establishment | — | — |
| 1888 | Francis P. Murray | Private Secretary | Civil Establishment | — | — |

### Deterministic checks: `murray_francis-peel_e1879` vs `Murray, Francis P___Ceylon___1886`

- [PASS] surname_gate: bio 'MURRAY' vs stint 'Murray, Francis P' (exact)
- [PASS] initials: bio ['F', 'P'] ~ stint ['F', 'P']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1888
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

