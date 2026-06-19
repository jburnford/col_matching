<!-- {"case_id": "case_carter_n_e1861", "bio_ids": ["carter_n_e1861"], "stint_ids": ["Carter, N. C___Ceylon___1919"]} -->
# Dossier case_carter_n_e1861

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 80 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['carter_n_e1861'] carry a single initial only — the namesake trap applies.

## Biography `carter_n_e1861`

- Printed name: **CARTER, N.**
- Birth year: not printed
- Appears in editions: [1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L33712.v` — printed in editions [1899]:**

> CARTER, THE HON. N. (1875).—Barrister, N. mem. house of assem., 1861 to 1865; 1870, and from 1876 to Quebec, 1891; the Dominions, for the administration of justice, and rights of the crown; ch. justice, 1876-9; Sept., 1878, and again in the absence of another, 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861–1865 | mem. house of assem. | Newfoundland | [1899] |
| 1 | 1870–1891 | — | Quebec | [1899] |
| 2 | 1876–1879 | ch. justice | — | [1899] |
| 3 | 1878–1893 | — | — | [1899] |

## Candidate stint `Carter, N. C___Ceylon___1919`

- Staff-list name: **Carter, N. C** | colony: **Ceylon** | listed 1919–1925 | editions [1919, 1920, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | N. C. Carter | Inspectress of Girls' English Schools | Education Department | — | — |
| 1920 | Miss N. C. Carter | Inspectress of Girls' English Schools | Education Department | — | — |
| 1922 | N. C. Carter | Inspectress of Girls' English Schools | Education Department | — | — |
| 1925 | N. C. Carter | Inspectress of Girls' English Schools | Education Department | — | — |

### Deterministic checks: `carter_n_e1861` vs `Carter, N. C___Ceylon___1919`

- [PASS] surname_gate: bio 'CARTER' vs stint 'Carter, N. C' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N', 'C']
- [PASS] age_gate: stint starts 1919; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1925
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

