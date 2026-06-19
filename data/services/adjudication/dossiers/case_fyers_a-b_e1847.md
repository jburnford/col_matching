<!-- {"case_id": "case_fyers_a-b_e1847", "bio_ids": ["fyers_a-b_e1847"], "stint_ids": ["Fyers, A. B___Ceylon___1877", "Fyers, W. A. B___Ceylon___1877"]} -->
# Dossier case_fyers_a-b_e1847

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fyers_a-b_e1847`

- Printed name: **FYERS, A. B.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27573.v` — printed in editions [1883]:**

> FYERS, R.E., COL. A. B.—Entered Royal engineers, Dec., 1847; captain, Aug. 1856, and lieut.-col., October, 1873; served in Mauritius from 1849 until 1858, during the greater part of which time he was "government meteorological observer;" was stationed at the Curragh camp from 1858 until 1861, and at Malta from 1861 until 1865; surveyor-general of Ceylon, 26 April, 1866. Is on the seconded list.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1847 | Royal engineers | — | [1883] |
| 1 | 1849–1858 | government meteorological observer | Mauritius | [1883] |
| 2 | 1856 | captain | — | [1883] |
| 3 | 1858–1861 | — | — | [1883] |
| 4 | 1861–1865 | — | Malta | [1883] |
| 5 | 1866 | surveyor-general | Ceylon | [1883] |
| 6 | 1873 | lieut.-col. | — | [1883] |

## Candidate stint `Fyers, A. B___Ceylon___1877`

- Staff-list name: **Fyers, A. B** | colony: **Ceylon** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. B. Fyers | Surveyor-General | Survey Department | — | Lieut.-Col. |
| 1878 | A. B. Fyers | Surveyor-General | Survey Department | — | Lt.-Col. |
| 1879 | A. B. Fyers | Surveyor-General | Survey Department | — | Lt.-Col. |
| 1880 | A. B. Fyers | Surveyor-General | Survey Department | — | Lieut.-Col. |
| 1883 | Col. A. B. Fyers, R.K. | Surveyor-General | Survey Department | — | Colonel |

### Deterministic checks: `fyers_a-b_e1847` vs `Fyers, A. B___Ceylon___1877`

- [PASS] surname_gate: bio 'FYERS' vs stint 'Fyers, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fyers, W. A. B___Ceylon___1877`

- Staff-list name: **Fyers, W. A. B** | colony: **Ceylon** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. A. B. Fyers | Assistant Surveyor | Survey Department | — | — |
| 1878 | W. A. B. Fyers | Supt. of China Surveys | Survey Department | — | — |
| 1879 | W. A. B. Fyers | Supt. of China Surveys | District Surveyors | — | — |
| 1880 | W. A. B. Fyers | Supt. of China Surveys | Survey Department | — | — |
| 1883 | W. A. B. Fyers | District Surveyor | Survey Department | — | — |
| 1886 | W. A. B. Fyers | Chief Surveyor | Survey Department | — | — |

### Deterministic checks: `fyers_a-b_e1847` vs `Fyers, W. A. B___Ceylon___1877`

- [PASS] surname_gate: bio 'FYERS' vs stint 'Fyers, W. A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['W', 'A', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
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

