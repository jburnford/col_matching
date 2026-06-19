<!-- {"case_id": "calib_gemini_malta_0248", "bio_ids": ["ransley_g-j_b1900"], "stint_ids": ["Ransley, G. J___Malta___1949"]} -->
# Dossier calib_gemini_malta_0248

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ransley_g-j_b1900`

- Printed name: **RANSLEY, G. J**
- Birth year: 1900 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960])
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1955-L22376.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960]:**

> RANSLEY, G. J.—b. 1900; ed. Garrison Sch.; postal clk., Malta, 1919; sub. inspr. of police, 1931; inspr., 1939; dir., approved sch., 1941; secon. reg. protection offr., 1942-44; dir., prisons, 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | postal clk. | Malta | [1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1931 | sub. inspr. of police | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1939 | inspr | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1941 | dir., approved sch | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |
| 4 | 1942–1944 | secon. reg. protection offr | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |
| 5 | 1944 | dir., prisons | Malta *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Ransley, G. J___Malta___1949`

- Staff-list name: **Ransley, G. J** | colony: **Malta** | listed 1949–1960 | editions [1949, 1950, 1951, 1952, 1953, 1954, 1955, 1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. J. Ransley | Director of Prisons | PRISONS | — | — |
| 1950 | G. J. Ransley | Director of Prisons | PRISONS | — | — |
| 1951 | G. J. Ransley | Director of Prisons | PRISONS | — | — |
| 1952 | G. J. Ransley | Director of Prisons | Maltese Government | — | — |
| 1953 | G. J. Ransley | Director of Prisons | The Maltese Government | — | — |
| 1954 | G. J. Ransley | Director of Prisons | The Maltese Government | — | — |
| 1955 | G. J. Ransley | Director of Prisons | THE MALTESE GOVERNMENT | — | — |
| 1957 | G. J. Ransley | Director of Prisons | The Maltese Government | — | — |
| 1958 | G. J. Ransley | Director of Prisons | The Maltese Government | — | — |
| 1959 | G. J. Ransley | Director of Prisons | The Maltese Government | — | — |
| 1960 | G. J. Ransley | Director of Prisons | Judiciary | — | — |

### Deterministic checks: `ransley_g-j_b1900` vs `Ransley, G. J___Malta___1949`

- [PASS] surname_gate: bio 'RANSLEY' vs stint 'Ransley, G. J' (exact)
- [PASS] initials: bio ['G', 'J'] ~ stint ['G', 'J']
- [PASS] age_gate: stint starts 1949, birth 1900 (age 49)
- [PASS] colony: 6 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1960
- [PASS] position_sim: best 100 vs bar 60: 'dir., prisons' ~ 'Director of Prisons'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1955, 1957, 1958] pos~100 (bar: >=2)
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

