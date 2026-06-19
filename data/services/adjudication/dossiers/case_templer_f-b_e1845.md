<!-- {"case_id": "case_templer_f-b_e1845", "bio_ids": ["templer_f-b_e1845"], "stint_ids": ["Templer, F. B___Ceylon___1877"]} -->
# Dossier case_templer_f-b_e1845

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `templer_f-b_e1845`

- Printed name: **TEMPLER, F. B**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29715.v` — printed in editions [1883]:**

> TEMPLER, F. B.—Was formerly a lieutenant in the 29th regt. and sold out of the army in 1845; appointed commissioner of requests, &c., Avishawelle, Ceylon, 1845; assistant agent, Nuwara Eliya, 1849; district judge, &c., Kallurata, 1862; principal assistant colonial secretary, and clerk to the councils; continued to act as government agent, &c., for the Central Province, May, 1865; acting treasurer, June, 1867; government agent, North-west Province, December, 1867; government agent, Southern Province, June, 1868; ditto, Central Province, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1845 | Was formerly a lieutenant in the 29th regt. and sold out of the army in | — | [1883] |
| 1 | 1845 | appointed commissioner of requests, &c., Avishawelle | Ceylon | [1883] |
| 2 | 1849 | assistant agent, Nuwara Eliya | Ceylon *(inherited from previous clause)* | [1883] |
| 3 | 1862 | district judge, &c., Kallurata | Ceylon *(inherited from previous clause)* | [1883] |
| 4 | 1865 | continued to act as government agent, &c., for the Central Province | Ceylon *(inherited from previous clause)* | [1883] |
| 5 | 1867 | acting treasurer | Ceylon *(inherited from previous clause)* | [1883] |
| 6 | 1868 | government agent, Southern Province | Ceylon *(inherited from previous clause)* | [1883] |
| 7 | 1878 | ditto, Central Province | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Templer, F. B___Ceylon___1877`

- Staff-list name: **Templer, F. B** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | F. B. Templer | Government Agent | Government Agencies | — | — |
| 1878 | F. B. Templer | Government Agent | Government Agencies | — | — |
| 1879 | F. B. Templer | Government Agent | Government Agencies | — | — |
| 1880 | F. B. Templer | Government Agent | Government Agencies | — | — |

### Deterministic checks: `templer_f-b_e1845` vs `Templer, F. B___Ceylon___1877`

- [PASS] surname_gate: bio 'TEMPLER' vs stint 'Templer, F. B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 100 vs bar 60: 'government agent, Southern Province' ~ 'Government Agent'
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

