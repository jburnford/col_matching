<!-- {"case_id": "case_hare_reginald-charles_e1881", "bio_ids": ["hare_reginald-charles_e1881"], "stint_ids": ["Hare, R. C___Australia___1912", "Hare, R. C___Western Australia___1889"]} -->
# Dossier case_hare_reginald-charles_e1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hare_reginald-charles_e1881`

- Printed name: **HARE, REGINALD CHARLES**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33877.v` — printed in editions [1888, 1889, 1890]:**

> HARE, REGINALD CHARLES.—Clerk, treasury, Western Australia, April, 1881; police inspector, southern districts, June, 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Clerk, treasury | Western Australia | [1888, 1889, 1890] |
| 1 | 1886 | police inspector, southern districts | Western Australia *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Hare, R. C___Australia___1912`

- Staff-list name: **Hare, R. C** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | R. C. Hare | Secretary | London Agency | — | — |
| 1913 | R. C. Hare | Secretary | London Agency | — | — |

### Deterministic checks: `hare_reginald-charles_e1881` vs `Hare, R. C___Australia___1912`

- [PASS] surname_gate: bio 'HARE' vs stint 'Hare, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hare, R. C___Western Australia___1889`

- Staff-list name: **Hare, R. C** | colony: **Western Australia** | listed 1889–1909 | editions [1889, 1890, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | R. C. Hare | Wardens | Mining Department | — | — |
| 1889 | R. C. Hare | Lieut.-Colonel | Government Residents | — | Lieut.-Colonel |
| 1889 | R. C. Hare (acting) | Chairman of Quarter Sessions | Chairmen of Quarter Sessions | — | — |
| 1890 | R. C. Hare | Government Resident | Government Residents | — | — |
| 1890 | R. C. Hare | Chairmen of Quarter Sessions | Judicial Department | — | — |
| 1896 | R. C. Hare | Secretary | London Agency | — | — |
| 1897 | R. C. Hare | Secretary | London Agency | — | — |
| 1898 | R. C. Hare | Secretary | London Agency | — | — |
| 1899 | R. C. Hare | Secretary | London Agency | — | — |
| 1900 | R. C. Hare | Secretary | London Agency | — | — |
| 1905 | R. C. Hare | Secretary | London Agency | — | — |
| 1906 | R. C. Hare | Secretary | London Agency | — | — |
| 1907 | R. C. Hare | Secretary | London Agency | — | — |
| 1908 | R. C. Hare | Secretary | London Agency | — | — |
| 1909 | R. C. Hare | Secretary | London Agency | — | — |

### Deterministic checks: `hare_reginald-charles_e1881` vs `Hare, R. C___Western Australia___1889`

- [PASS] surname_gate: bio 'HARE' vs stint 'Hare, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Western Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1909
- [FAIL] position_sim: best 35 vs bar 60: 'police inspector, southern districts' ~ 'Chairman of Quarter Sessions'
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

