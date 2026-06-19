<!-- {"case_id": "case_liesching_l-f_e1855", "bio_ids": ["liesching_l-f_e1855"], "stint_ids": ["Liesching, L. F___Ceylon___1877"]} -->
# Dossier case_liesching_l-f_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `liesching_l-f_e1855`

- Printed name: **LIESCHING, L. F**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28387.v` — printed in editions [1883]:**

> LIESCHING, L. F.—Sub-collector and landing waiter at Trincomalee, Ceylon, June, 1855; commissioner of requests, &c., Point Pedro, 1855; assistant government agent, Jaffna, 1862; district judge, Tangalla, June, 1864; assistant government agent, Anuradhapura, June 1, 1867; assistant government agent, Putalam, July, 1872; acting fiscal for the western province, Nov. 1872; appointment confirmed, June, 1873; acting superintendent of convict establishment, in addition to duties as fiscal, September, 1873; and acting inspector general of prisons, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | Sub-collector and landing waiter at Trincomalee | Ceylon | [1883] |
| 1 | 1862 | assistant government agent, Jaffna | Ceylon *(inherited from previous clause)* | [1883] |
| 2 | 1864 | district judge, Tangalla | Ceylon *(inherited from previous clause)* | [1883] |
| 3 | 1867 | assistant government agent, Anuradhapura, June 1 | Ceylon *(inherited from previous clause)* | [1883] |
| 4 | 1872 | assistant government agent, Putalam | Ceylon *(inherited from previous clause)* | [1883] |
| 5 | 1873 | appointment confirmed | Ceylon *(inherited from previous clause)* | [1883] |
| 6 | 1878 | and acting inspector general of prisons | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Liesching, L. F___Ceylon___1877`

- Staff-list name: **Liesching, L. F** | colony: **Ceylon** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | L. F. Liesching | Commissioner of Requests, Police Magistrate | District and Minor Courts | — | — |
| 1878 | L. F. Liesching | Fiscal | District and Minor Courts | — | — |
| 1879 | L. F. Liesching | Fiscal | Judicial Establishment | — | — |
| 1880 | L. F. Liesching | Fiscal | District and Minor Courts | — | — |
| 1883 | L. F. Liesching | Fiscal | District and Minor Courts | — | — |

### Deterministic checks: `liesching_l-f_e1855` vs `Liesching, L. F___Ceylon___1877`

- [PASS] surname_gate: bio 'LIESCHING' vs stint 'Liesching, L. F' (exact)
- [PASS] initials: bio ['L', 'F'] ~ stint ['L', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1883
- [FAIL] position_sim: best 44 vs bar 60: 'and acting inspector general of prisons' ~ 'Commissioner of Requests, Police Magistrate'
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

