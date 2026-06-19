<!-- {"case_id": "case_clarence_arthur_e1846", "bio_ids": ["clarence_arthur_e1846"], "stint_ids": ["Clarence, A. R___Griqualand West___1877", "Clarence, A___Natal___1879"]} -->
# Dossier case_clarence_arthur_e1846

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['clarence_arthur_e1846'] carry a single initial only — the namesake trap applies.

## Biography `clarence_arthur_e1846`

- Printed name: **CLARENCE, ARTHUR**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26843.v` — printed in editions [1883]:**

> CLARENCE, ARTHUR.—Served as captain of Cape volunteers, Kafir war, 1846 and 1847; justice of the peace, Natal, Oct., 1854; chief clerk, resident magistrate's office, Pietermaritzburg, Nov., 1858; chief clerk registrar of deeds, April, 1861; sheriff of Natal, Nov., 1861; marshal of vice admiralty courts, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1846–1847 | captain of Cape volunteers | Cape | [1883] |
| 1 | 1854–1854 | justice of the peace | Natal | [1883] |
| 2 | 1858–1858 | chief clerk, resident magistrate's office | Pietermaritzburg | [1883] |
| 3 | 1861–1861 | chief clerk registrar of deeds | — | [1883] |
| 4 | 1861–1861 | sheriff | Natal | [1883] |
| 5 | 1877–1877 | marshal of vice admiralty courts | — | [1883] |

## Candidate stint `Clarence, A. R___Griqualand West___1877`

- Staff-list name: **Clarence, A. R** | colony: **Griqualand West** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. R. Clarence | 1st Clerk | Audit Branch | — | — |
| 1879 | A. R. Clarence | Chief Clerk and Accountant | Treasury | — | — |
| 1880 | A. R. Clarence | Distributor of Stamps | Treasury | — | — |

### Deterministic checks: `clarence_arthur_e1846` vs `Clarence, A. R___Griqualand West___1877`

- [PASS] surname_gate: bio 'CLARENCE' vs stint 'Clarence, A. R' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Griqualand West'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Clarence, A___Natal___1879`

- Staff-list name: **Clarence, A** | colony: **Natal** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | A. Clarence | Sheriff | Judicial Department | — | — |
| 1880 | A. Clarence | Sheriff | Judicial Department | — | — |

### Deterministic checks: `clarence_arthur_e1846` vs `Clarence, A___Natal___1879`

- [PASS] surname_gate: bio 'CLARENCE' vs stint 'Clarence, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Natal'
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

