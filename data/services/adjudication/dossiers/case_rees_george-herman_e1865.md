<!-- {"case_id": "case_rees_george-herman_e1865", "bio_ids": ["rees_george-herman_e1865"], "stint_ids": ["Rees, George H___Jamaica___1877", "Rees, H___Cape of Good Hope___1906", "Rees, H___South Africa___1912"]} -->
# Dossier case_rees_george-herman_e1865

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rees_george-herman_e1865`

- Printed name: **REES, GEORGE HERMAN**
- Birth year: not printed
- Terminal: resigned 1882 — “resigned, 5th May, 1882.”
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29213.v` — printed in editions [1883]:**

> REES, GEORGE HERMAN.—Entered the office of the inspector of prisons, Jamaica, 20th April, 1865; principal clerk in the office of the governor's private secretary, 22nd December, 1865; 2nd-class clerk in the colonial secretariat, 8th September, 1866; and principal clerk in the office of the island medical establishment, 1st Dec., 1871; chief clerk, 1st Oct., 1875; secretary to central board of health and quarantine Board, 7th Nov., 1878; resigned, 5th May, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | Entered the office of the inspector of prisons | Jamaica | [1883] |
| 1 | 1866 | 2nd-class clerk in the colonial secretariat | Jamaica *(inherited from previous clause)* | [1883] |
| 2 | 1871 | and principal clerk in the office of the island medical establishment | Jamaica *(inherited from previous clause)* | [1883] |
| 3 | 1875 | chief clerk | Jamaica *(inherited from previous clause)* | [1883] |
| 4 | 1878 | secretary to central board of health and quarantine Board | Jamaica *(inherited from previous clause)* | [1883] |

## Candidate stint `Rees, George H___Jamaica___1877`

- Staff-list name: **Rees, George H** | colony: **Jamaica** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | George H. Rees | Chief Clerk | Medical Department | — | — |
| 1878 | George H. Rees | Chief Clerk | Medical Department | — | — |
| 1879 | George H. Rees | Chief Clerk | Medical Department | — | — |
| 1880 | George H. Rees | Chief Clerk | Medical Department | — | — |

### Deterministic checks: `rees_george-herman_e1865` vs `Rees, George H___Jamaica___1877`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, George H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 100 vs bar 60: 'chief clerk' ~ 'Chief Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Rees, H___Cape of Good Hope___1906`

- Staff-list name: **Rees, H** | colony: **Cape of Good Hope** | listed 1906–1909 | editions [1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | H. Rees | Clerks | Diamond Mines | — | — |
| 1907 | H. Rees | Inspector of Claims, Barkly West | Diamond Mines | — | — |
| 1908 | H. Rees | Inspector of Claims | Mines | — | — |
| 1909 | H. Rees | Inspector of Clutius, Barkly West | Mines | — | — |

### Deterministic checks: `rees_george-herman_e1865` vs `Rees, H___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Rees, H___South Africa___1912`

- Staff-list name: **Rees, H** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | H. Rees | Registrar of Claims | Department of Mines | — | — |
| 1914 | H. Rees | Mining Commissioners | Analyses | — | — |
| 1918 | H. Rees | Mining Commissioners | Department of Mines and Industries | — | — |

### Deterministic checks: `rees_george-herman_e1865` vs `Rees, H___South Africa___1912`

- [PASS] surname_gate: bio 'REES' vs stint 'Rees, H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

