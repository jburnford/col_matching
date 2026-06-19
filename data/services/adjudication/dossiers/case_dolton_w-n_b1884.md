<!-- {"case_id": "case_dolton_w-n_b1884", "bio_ids": ["dolton_w-n_b1884"], "stint_ids": ["Dolton, William N___Kenya___1936", "Dolton, William N___Kenya___1949"]} -->
# Dossier case_dolton_w-n_b1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dolton_w-n_b1884`

- Printed name: **DOLTON, W. N**
- Birth year: 1884 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L35021.v` — printed in editions [1950, 1951]:**

> DOLTON, W. N.—b. 1884; ed. Trinity Coll., Dublin, M.A.; inspr., schs., educ. dept., Ken., 1928; asst. sec., secretariat, 1944; chmn., cent. commodity distrbn. bd., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | inspr., schs., educ. dept. | Kenya | [1950, 1951] |
| 1 | 1944 | asst. sec., secretariat | Kenya *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1948 | chmn., cent. commodity distrbn. bd | Kenya *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Dolton, William N___Kenya___1936`

- Staff-list name: **Dolton, William N** | colony: **Kenya** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | W. N. Dolton | Inspector of Schools | Education | — | — |
| 1937 | W. N. Dolton | Inspectors of Schools | Education | — | — |
| 1939 | W. N. Dolton | Inspector of Schools | Education | — | — |
| 1940 | W. N. Dolton | Inspectors of Schools | Education | — | — |

### Deterministic checks: `dolton_w-n_b1884` vs `Dolton, William N___Kenya___1936`

- [PASS] surname_gate: bio 'DOLTON' vs stint 'Dolton, William N' (exact)
- [PASS] initials: bio ['W', 'N'] ~ stint ['W', 'N']
- [PASS] age_gate: stint starts 1936, birth 1884 (age 52)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 50 vs bar 60: 'inspr., schs., educ. dept.' ~ 'Inspector of Schools'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Dolton, William N___Kenya___1949`

- Staff-list name: **Dolton, William N** | colony: **Kenya** | listed 1949–1952 | editions [1949, 1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | William N. Dolton | Chairman | Commodity Distribution Board | — | — |
| 1950 | W. N. Dolton | Chairman | Central Commodity Distribution Board | — | — |
| 1951 | W. N. Dolton | Chairman | Central Commodity Distribution Board | — | — |
| 1952 | W. N. Dolton | Controller of Supplies | Civil Establishment | — | — |

### Deterministic checks: `dolton_w-n_b1884` vs `Dolton, William N___Kenya___1949`

- [PASS] surname_gate: bio 'DOLTON' vs stint 'Dolton, William N' (exact)
- [PASS] initials: bio ['W', 'N'] ~ stint ['W', 'N']
- [PASS] age_gate: stint starts 1949, birth 1884 (age 65)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1952
- [FAIL] position_sim: best 31 vs bar 60: 'chmn., cent. commodity distrbn. bd' ~ 'Controller of Supplies'
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

