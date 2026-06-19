<!-- {"case_id": "case_nevill_j-t_e1864", "bio_ids": ["nevill_j-t_e1864"], "stint_ids": ["Nevill, J. T___Newfoundland___1877"]} -->
# Dossier case_nevill_j-t_e1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Nevill, J. T___Newfoundland___1877` is also gate-compatible with biography(ies) outside this case: ['nevill_j-t_e1874'] (already linked elsewhere or filtered).

## Biography `nevill_j-t_e1864`

- Printed name: **NEVILL, J. T**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L35093.v` — printed in editions [1888, 1889, 1896, 1897, 1898]:**

> NEVILL, J. T.—Superintendent of public buildings, Newfoundland, Jan., 1864; also inspector of lighthouses, Jan., 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Superintendent of public buildings | Newfoundland | [1888, 1889, 1896, 1897, 1898] |
| 1 | 1872 | also inspector of lighthouses | Newfoundland *(inherited from previous clause)* | [1888, 1889, 1896, 1897, 1898] |

## Candidate stint `Nevill, J. T___Newfoundland___1877`

- Staff-list name: **Nevill, J. T** | colony: **Newfoundland** | listed 1877–1897 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1889, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1878 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1879 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1880 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1883 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1886 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1889 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1890 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1894 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1896 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |
| 1897 | J. T. Nevill | Inspector of Lighthouses and Superintendent of Public Buildings | Civil Establishment | — | — |

### Deterministic checks: `nevill_j-t_e1864` vs `Nevill, J. T___Newfoundland___1877`

- [PASS] surname_gate: bio 'NEVILL' vs stint 'Nevill, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1897
- [PASS] position_sim: best 91 vs bar 60: 'also inspector of lighthouses' ~ 'Inspector of Lighthouses and Superintendent of Public Buildings'
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

