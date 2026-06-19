<!-- {"case_id": "case_verbeke_frederic_e1871", "bio_ids": ["verbeke_frederic_e1871", "verreke_fredrick_e1871"], "stint_ids": ["Verbeke, F___British Guiana___1877"]} -->
# Dossier case_verbeke_frederic_e1871

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['verbeke_frederic_e1871', 'verreke_fredrick_e1871'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Verbeke, F___British Guiana___1877'] have more than one claimant biography in this case.

## Biography `verbeke_frederic_e1871`

- Printed name: **VERBEKE, FREDERIC**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29856.v` — printed in editions [1883]:**

> VERBEKE, FREDERIC.—Sixth clerk in administrator-general's office, British Guiana, 15th April, 1871; 5th clerk, 30th Oct., 1872; 4th clerk, 30th April, 1874; 1874; sub-administrator, Berbice, 27th Feb., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Sixth clerk in administrator-general's office | British Guiana | [1883] |
| 1 | 1872 | 5th clerk | British Guiana *(inherited from previous clause)* | [1883] |
| 2 | 1874 | 4th clerk | British Guiana *(inherited from previous clause)* | [1883] |
| 3 | 1875 | sub-administrator, Berbice | British Guiana *(inherited from previous clause)* | [1883] |

## Biography `verreke_fredrick_e1871`

- Printed name: **VERREKE, FREDRICK**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L36108.v` — printed in editions [1886]:**

> VERREKE, FREDRICK.—Sixth clerk in administrator-general's office, British Guiana, 15th April, 1871; 5th clerk, 30th Oct., 1872; 4th clerk, 30th April, 1874; 1874; sub-administrator, Berbice, 27th Feb., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Sixth clerk in administrator-general's office | British Guiana | [1886] |
| 1 | 1872 | 5th clerk | British Guiana *(inherited from previous clause)* | [1886] |
| 2 | 1874 | 4th clerk | British Guiana *(inherited from previous clause)* | [1886] |
| 3 | 1875 | sub-administrator, Berbice | British Guiana *(inherited from previous clause)* | [1886] |

## Candidate stint `Verbeke, F___British Guiana___1877`

- Staff-list name: **Verbeke, F** | colony: **British Guiana** | listed 1877–1886 | editions [1877, 1878, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | F. Verbeke | 6th Clerk to Administrator-General | Judicial Establishment | — | — |
| 1878 | F. Verbeke | 4th Clerk to Administrator-General | Judicial Establishment | — | — |
| 1880 | F. Verbeke | 4th Clerk to Administrator-General | Judicial Establishment | — | — |
| 1883 | F. Verbeke | 4th Clerk to Administrator-General | Judicial Establishment | — | — |
| 1886 | F. Verbeke | 4th Clerk | Judicial Establishment | — | — |

### Deterministic checks: `verbeke_frederic_e1871` vs `Verbeke, F___British Guiana___1877`

- [PASS] surname_gate: bio 'VERBEKE' vs stint 'Verbeke, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [FAIL] position_sim: best 49 vs bar 60: 'sub-administrator, Berbice' ~ '6th Clerk to Administrator-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `verreke_fredrick_e1871` vs `Verbeke, F___British Guiana___1877`

- [PASS] surname_gate: bio 'VERREKE' vs stint 'Verbeke, F' (fuzzy:1)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [FAIL] position_sim: best 49 vs bar 60: 'sub-administrator, Berbice' ~ '6th Clerk to Administrator-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

