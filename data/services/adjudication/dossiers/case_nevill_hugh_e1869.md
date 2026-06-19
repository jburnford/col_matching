<!-- {"case_id": "case_nevill_hugh_e1869", "bio_ids": ["nevill_hugh_e1869"], "stint_ids": ["Nevill, H___Ceylon___1877", "Nevill, H___Ceylon___1896"]} -->
# Dossier case_nevill_hugh_e1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['nevill_hugh_e1869'] carry a single initial only — the namesake trap applies.

## Biography `nevill_hugh_e1869`

- Printed name: **NEVILL, Hugh**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28843.v` — printed in editions [1883]:**

> NEVILL, Hugh.—Was at Magdalen College, Cambridge. Writer, Ceylon civil service, Sept. 1869; police magistrate, Point Pedro and Chavachcheri, July, 1871; acting colonial magistrate, Galagedara, Dec. 1871; acting colonial magistrate, Gampola, June, 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Was at Magdalen College, Cambridge. Writer, Ceylon civil service | Ceylon | [1883] |
| 1 | 1871 | police magistrate, Point Pedro and Chavachcheri | Ceylon *(inherited from previous clause)* | [1883] |
| 2 | 1872 | acting colonial magistrate, Gampola | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Nevill, H___Ceylon___1877`

- Staff-list name: **Nevill, H** | colony: **Ceylon** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1883, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. Nevill | Commissioner of Requests | District and Minor Courts | — | — |
| 1878 | H. Nevill | Commissioner of Requests, Police Magistrate | District and Minor Courts | — | — |
| 1879 | H. Nevill | Commissioner of Requests, Police Magistrate | Judicial Establishment | — | — |
| 1880 | H. Nevill | Commissioner of Requests | District and Minor Courts | — | — |
| 1883 | H. Nevill | Commissioner of Requests | District and Minor Courts | — | — |
| 1888 | H. Nevill | Fiscal | SOUTHERN CIRCUIT | — | — |
| 1889 | H. Nevill | Fiscal, Central Province | SOUTHERN CIRCUIT | — | — |

### Deterministic checks: `nevill_hugh_e1869` vs `Nevill, H___Ceylon___1877`

- [PASS] surname_gate: bio 'NEVILL' vs stint 'Nevill, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1889
- [FAIL] position_sim: best 53 vs bar 60: 'acting colonial magistrate, Gampola' ~ 'Commissioner of Requests, Police Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Nevill, H___Ceylon___1896`

- Staff-list name: **Nevill, H** | colony: **Ceylon** | listed 1896–1898 | editions [1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | H. Nevill | District Judge and Joint Commissioner of Requests and Police Magistrate | Northern Circuit | — | — |
| 1896 | H. Nevill | Assistant Government Agent | Government Agencies | — | — |
| 1898 | H. Nevill | Police Magistrate | Northern Circuit | — | — |

### Deterministic checks: `nevill_hugh_e1869` vs `Nevill, H___Ceylon___1896`

- [PASS] surname_gate: bio 'NEVILL' vs stint 'Nevill, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
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

