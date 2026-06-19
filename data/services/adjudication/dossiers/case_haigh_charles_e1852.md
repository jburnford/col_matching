<!-- {"case_id": "case_haigh_charles_e1852", "bio_ids": ["haigh_charles_e1852"], "stint_ids": ["Haigh, Charles___Jamaica___1877", "Haigh, J. C___Ceylon___1929"]} -->
# Dossier case_haigh_charles_e1852

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['haigh_charles_e1852'] carry a single initial only — the namesake trap applies.

## Biography `haigh_charles_e1852`

- Printed name: **HAIGH, CHARLES**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27815.v` — printed in editions [1883]:**

> HAIGH, CHARLES.—Entered the English excise service as second-class assistant of excise, June, 1852; first-class assistant, Nov., 1864; riding officer, April, 1855; division officer, April, 1858; examiner, March, 1865; supervisor, May, 1866; supervisor of excise, and general inspector of revenue, &c., Jamaica, April, 1869; acted as collector-general of internal revenue and excise from June to Oct., 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | Entered the English excise service as second-class assistant of excise | — | [1883] |
| 1 | 1855 | riding officer | — | [1883] |
| 2 | 1858 | division officer | — | [1883] |
| 3 | 1864 | first-class assistant | — | [1883] |
| 4 | 1865 | examiner | — | [1883] |
| 5 | 1866 | supervisor | — | [1883] |
| 6 | 1869 | supervisor of excise, and general inspector of revenue, &c. | Jamaica | [1883] |
| 7 | 1870 | acted as collector-general of internal revenue and excise from | Jamaica *(inherited from previous clause)* | [1883] |

## Candidate stint `Haigh, Charles___Jamaica___1877`

- Staff-list name: **Haigh, Charles** | colony: **Jamaica** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Charles Haigh | Supervisor of Revenue Offices | Revenue Department | — | — |
| 1878 | Charles Haigh | Supervisor of Revenue Offices | Revenue Department | — | — |

### Deterministic checks: `haigh_charles_e1852` vs `Haigh, Charles___Jamaica___1877`

- [PASS] surname_gate: bio 'HAIGH' vs stint 'Haigh, Charles' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1878
- [FAIL] position_sim: best 51 vs bar 60: 'acted as collector-general of internal revenue and excise from' ~ 'Supervisor of Revenue Offices'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Haigh, J. C___Ceylon___1929`

- Staff-list name: **Haigh, J. C** | colony: **Ceylon** | listed 1929–1940 | editions [1929, 1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | J. C. Haigh | Assistant Mycologist | Research Branch | — | — |
| 1931 | J. C. Haigh | Assistant Mycologist | Research Branch | — | — |
| 1934 | J. C. Haigh | Economic Botanist | Department of Agriculture | — | — |
| 1936 | J. C. Haigh | Economic Botanist | Department of Agriculture | — | — |
| 1937 | J. C. Haigh | Economic Botanist | Research Laboratories | — | — |
| 1940 | J. C. Haigh | Botanist | Research Laboratories | — | — |

### Deterministic checks: `haigh_charles_e1852` vs `Haigh, J. C___Ceylon___1929`

- [PASS] surname_gate: bio 'HAIGH' vs stint 'Haigh, J. C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1929; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1940
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

