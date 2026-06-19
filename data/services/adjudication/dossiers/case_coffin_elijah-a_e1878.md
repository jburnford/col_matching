<!-- {"case_id": "case_coffin_elijah-a_e1878", "bio_ids": ["coffin_elijah-a_e1878"], "stint_ids": ["Coffin, E. A___British Honduras___1880"]} -->
# Dossier case_coffin_elijah-a_e1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coffin_elijah-a_e1878`

- Printed name: **COFFIN, ELIJAH A.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L26906.v` — printed in editions [1883]:**

> COFFIN, ELIJAH A.—Educated at Queen Elizabeth's Grammar School, Kingston-on-Thames, Surrey. Appointed clerk to clerk of courts 1st Nov., 1878; second lieutenant in Belize V.R.C., 6th Oct., 1879; acting clerk of courts, keeper of records, registrar of lands titles, 3rd Sept., to Dec., 1880; first lieutenant in Belize V.R.C. 10th June, 1881; acting clerk of courts, &c., from 4th June, 1881, to 1st April, 1882, and again from 25th May, 1882.

**Version `col1886-L32731.v` — printed in editions [1886, 1888]:**

> COFFIN, ELIJAH A.—Educated at Queen Elizabeth's Grammar School, Kingston-on-Thames, Surrey; clerk to clerk of courts, Trinidad, 1st Nov., 1878; acting clerk of courts, keeper of records, registrar of lands titles, 3rd Sept., to Dec., 1880; acting clerk of courts, &c., from 4th June, 1881, to 1st April, 1882, and again from 25th May, 1882; district magistrate Toledo district, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878–1878 | clerk to clerk of courts | Trinidad | [1883, 1886, 1888] |
| 1 | 1879–1879 | second lieutenant in Belize V.R.C. | Belize | [1883] |
| 2 | 1880–1880 | acting clerk of courts, keeper of records, registrar of lands titles | — | [1883, 1886, 1888] |
| 3 | 1881–1881 | first lieutenant in Belize V.R.C. | Belize | [1883] |
| 4 | 1881 | acting clerk of courts, &c. | — | [1883, 1886, 1888] |
| 5 | 1882 | acting clerk of courts, &c. | — | [1886, 1888] |
| 6 | 1885–1885 | district magistrate | Toledo district | [1886, 1888] |

## Candidate stint `Coffin, E. A___British Honduras___1880`

- Staff-list name: **Coffin, E. A** | colony: **British Honduras** | listed 1880–1889 | editions [1880, 1883, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | E. A. Coffin | Clerk of Courts, Keeper of Records, and Registrar of Vice-Admiralty Court | Judicial Establishment | — | — |
| 1883 | E. A. Coffin | Clerk of Courts | Judicial Establishment | — | — |
| 1889 | E. A. Coffin | Magistrate | District Magistrates | — | — |

### Deterministic checks: `coffin_elijah-a_e1878` vs `Coffin, E. A___British Honduras___1880`

- [PASS] surname_gate: bio 'COFFIN' vs stint 'Coffin, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1889
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

