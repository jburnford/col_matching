<!-- {"case_id": "calib_gemini_jamaica_0147", "bio_ids": ["trench_d-p_e1848"], "stint_ids": ["Trench, Daniel Power___Jamaica___1877"]} -->
# Dossier calib_gemini_jamaica_0147

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `trench_d-p_e1848`

- Printed name: **TRENCH, D. P.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29785.v` — printed in editions [1883]:**

> TRENCH, D. P.—Auditor of accounts in the prison department of Jamaica, March 14, 1848; appointed second commissioner of audit on March 21, 1856; inspector and director of the public hospital and lunatic asylum, Jan. 11, 1859, when that office was first created; inspector of the revenue department on the creation of that office in March, 1865; and collector general of Jamaica upon the amalgamation of the customs, excise, and internal revenue departments in March, 1869; official member of the legislative council 1866.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1848 | Auditor of accounts in the prison department | Jamaica | [1883] |
| 1 | 1856 | second commissioner of audit | — | [1883] |
| 2 | 1859 | inspector and director of the public hospital and lunatic asylum | — | [1883] |
| 3 | 1865 | inspector of the revenue department | — | [1883] |
| 4 | 1866 | official member of the legislative council | — | [1883] |
| 5 | 1869 | collector general | Jamaica | [1883] |

## Candidate stint `Trench, Daniel Power___Jamaica___1877`

- Staff-list name: **Trench, Daniel Power** | colony: **Jamaica** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Daniel Power Trench | Collector-General | Revenue Department | — | — |
| 1877 | The Hon. D. P. Trench | Collector General | Legislative Council | — | — |
| 1878 | Daniel Power Trench | Collector-General | Revenue Department | — | — |
| 1878 | The Hon. D. P. Trench | Collector General | Official Members | — | — |
| 1879 | D. P. Trench | Collector General | Official Members | — | — |
| 1879 | Daniel Power Trench | Collector-General | Revenue Department | — | — |
| 1880 | D. P. Trench | Collector General | Legislative Council | — | — |
| 1880 | Daniel Power Trench | Collector-General | Revenue Department | — | — |
| 1883 | Daniel Power Trench | Collector-General | Revenue Department | — | — |
| 1883 | D. P. Trench | Collector General | Civil Establishment | — | — |

### Deterministic checks: `trench_d-p_e1848` vs `Trench, Daniel Power___Jamaica___1877`

- [PASS] surname_gate: bio 'TRENCH' vs stint 'Trench, Daniel Power' (exact)
- [PASS] initials: bio ['D', 'P'] ~ stint ['D', 'P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'collector general' ~ 'Collector General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1883] pos~100 (bar: >=2)
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

