<!-- {"case_id": "calib_gemini_newfoundland_0277", "bio_ids": ["nevill_j-t_e1874"], "stint_ids": ["Nevill, J. T___Newfoundland___1877"]} -->
# Dossier calib_gemini_newfoundland_0277

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nevill_j-t_e1874`

- Printed name: **NEVILL, J. T**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34987.v` — printed in editions [1886]:**

> NEVILL, J. T.—Inspector of lighthouses and superintendent of public buildings, Newfoundland, Jan., 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Inspector of lighthouses and superintendent of public buildings | Newfoundland | [1886] |

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

### Deterministic checks: `nevill_j-t_e1874` vs `Nevill, J. T___Newfoundland___1877`

- [PASS] surname_gate: bio 'NEVILL' vs stint 'Nevill, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1897
- [PASS] position_sim: best 100 vs bar 60: 'Inspector of lighthouses and superintendent of public buildings' ~ 'Inspector of Lighthouses and Superintendent of Public Buildings'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1886] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

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

