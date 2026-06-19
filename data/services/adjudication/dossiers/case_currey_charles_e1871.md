<!-- {"case_id": "case_currey_charles_e1871", "bio_ids": ["currey_charles_e1871"], "stint_ids": ["Currey, Charles___Cape of Good Hope___1877"]} -->
# Dossier case_currey_charles_e1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['currey_charles_e1871'] carry a single initial only — the namesake trap applies.

## Biography `currey_charles_e1871`

- Printed name: **CURREY, CHARLES**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L34488.v` — printed in editions [1900]:**

> CURREY, CHARLES.—Entered the col. sec.'s office, Cape, June, 1871; apptd. 3rd class ck., Aug., 1872; 2nd class, July, 1874; promoted dept. of crown lands and pub. wks., Oct., 1879; ch. ck., office of crown lands and pub. wks., Apr., 1881; sec. to the diamond mining comsir., Sept., 1881; from 1882 has frequently acted as asst. comsir. of crown lands and pub. wks.; asst. comsir. of crown lands and pub. wks., Apr., 1892; permanent head of dept. of lands, mines, and agricul., Sept., 1892; under sec. for agricul., 1893; mem. of geologi. comsir.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Entered the col. sec.'s office | Cape Colony | [1900] |
| 1 | 1872 | 3rd class ck. | — | [1900] |
| 2 | 1874 | 2nd class clerk | — | [1900] |
| 3 | 1879 | dept. of crown lands and pub. wks. | — | [1900] |
| 4 | 1881 | ch. ck., office of crown lands and pub. wks. | — | [1900] |
| 5 | 1881 | sec. to the diamond mining comsir. | — | [1900] |
| 6 | 1882 | acted as asst. comsir. of crown lands and pub. wks. | — | [1900] |
| 7 | 1892 | asst. comsir. of crown lands and pub. wks. | — | [1900] |
| 8 | 1892 | permanent head of dept. of lands, mines, and agricul. | — | [1900] |
| 9 | 1893 | under sec. for agricul. | — | [1900] |

## Candidate stint `Currey, Charles___Cape of Good Hope___1877`

- Staff-list name: **Currey, Charles** | colony: **Cape of Good Hope** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1883, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Charles Currey | Clerk of the Second Class | Colonial Secretary's Department | — | — |
| 1878 | Charles Currey | Clerk, Second Class | Colonial Secretary's Department | — | — |
| 1879 | Charles Currey | Clerk of the Second Class | Colonial Secretary's Office | — | — |
| 1880 | C. A. Currey | Clerks | Department of the Commissioner of Crown Lands and Public Works | — | — |
| 1883 | Charles Currey | Chief Clerk | Department of the Commissioner of Crown Lands and Public Works | — | — |
| 1888 | Charles Currey | Chief Clerk | Commissioner's Office | — | — |

### Deterministic checks: `currey_charles_e1871` vs `Currey, Charles___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'CURREY' vs stint 'Currey, Charles' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

