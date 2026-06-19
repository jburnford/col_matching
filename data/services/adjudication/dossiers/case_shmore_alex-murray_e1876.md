<!-- {"case_id": "case_shmore_alex-murray_e1876", "bio_ids": ["shmore_alex-murray_e1876"], "stint_ids": ["Ashmore, A. M___Ceylon___1878", "Ashmore, A. M___Ceylon___1905"]} -->
# Dossier case_shmore_alex-murray_e1876

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `shmore_alex-murray_e1876` ↔ `Ashmore, A. M___Ceylon___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Ashmore, A. M___Ceylon___1878` is also gate-compatible with biography(ies) outside this case: ['ashmore_alex-murray_b1855'] (already linked elsewhere or filtered).
- NOTE: stint `Ashmore, A. M___Ceylon___1905` is also gate-compatible with biography(ies) outside this case: ['ashmore_alex-murray_b1855'] (already linked elsewhere or filtered).

## Biography `shmore_alex-murray_e1876`

- Printed name: **SHMORE, ALEX. MURRAY**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L30612.v` — printed in editions [1897]:**

> SHMORE, ALEX. MURRAY.—Writer, Ceylon vice, 1876; police magistrate, Panvila, 1878; assistant government agent, Western Pro- es, 1883; ditto, Central Province, 1884; ng second assistant colonial secretary, 1887; unstr. of requests and pol. mag., Kandy, 1891; g colonial sec., Gold Coast, Feb., 1894; rec., Cyprus, March, 1895; ag. chief sec., June to , 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Writer, Ceylon vice | Ceylon | [1897] |
| 1 | 1878 | police magistrate, Panvila | Ceylon *(inherited from previous clause)* | [1897] |
| 2 | 1883 | assistant government agent, Western Pro- es | Ceylon *(inherited from previous clause)* | [1897] |
| 3 | 1884 | ditto, Central Province | Ceylon *(inherited from previous clause)* | [1897] |
| 4 | 1887 | ng second assistant colonial secretary | Ceylon *(inherited from previous clause)* | [1897] |
| 5 | 1891 | unstr. of requests and pol. mag., Kandy | Ceylon *(inherited from previous clause)* | [1897] |
| 6 | 1894 | g colonial sec. | Gold Coast | [1897] |
| 7 | 1895 | rec. | Cyprus | [1897] |
| 8 | 1896 | ag. chief sec., June to | Cyprus *(inherited from previous clause)* | [1897] |

## Candidate stint `Ashmore, A. M___Ceylon___1878`

- Staff-list name: **Ashmore, A. M** | colony: **Ceylon** | listed 1878–1894 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | A. M. Ashmore | Writer | Colonial Secretary's Office | — | — |
| 1879 | A. M. Ashmore | Writer | Colonial Secretary's Office | — | — |
| 1880 | A. M. Ashmore | Commissioner of Requests / Police Magistrate | District and Minor Courts | — | — |
| 1883 | A. M. Ashmore | Commissioner of Requests / Police Magistrate | District and Minor Courts | — | — |
| 1886 | A. M. Ashmore | Office Assistant | Government Agencies | — | — |
| 1888 | A. M. Ashmore | Office Assistant | Central Province | — | — |
| 1889 | A. M. Ashmore | Office Assistant | Government Agencies | — | — |
| 1890 | A. M. Ashmore | Assistant Government Agent | Government Agencies | — | — |
| 1894 | A. M. Ashmore | Commissioner of Requests and Police Magistrate | — | — | — |

### Deterministic checks: `shmore_alex-murray_e1876` vs `Ashmore, A. M___Ceylon___1878`

- [PASS] surname_gate: bio 'SHMORE' vs stint 'Ashmore, A. M' (fuzzy:1)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 6 event tenure(s) overlap stint years 1878-1894
- [PASS] position_sim: best 100 vs bar 60: 'Writer, Ceylon vice' ~ 'Writer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Ashmore, A. M___Ceylon___1905`

- Staff-list name: **Ashmore, A. M** | colony: **Ceylon** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. M. Ashmore | Lieut.-Governor and Colonial Secretary | Civil Establishment | C.M.G. | — |
| 1906 | Sir A. M. Ashmore | Lieut.-Governor and Colonial Secretary | Civil Establishment | K.C.M.G. | — |

### Deterministic checks: `shmore_alex-murray_e1876` vs `Ashmore, A. M___Ceylon___1905`

- [PASS] surname_gate: bio 'SHMORE' vs stint 'Ashmore, A. M' (fuzzy:1)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

