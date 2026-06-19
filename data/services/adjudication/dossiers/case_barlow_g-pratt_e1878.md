<!-- {"case_id": "case_barlow_g-pratt_e1878", "bio_ids": ["barlow_g-pratt_e1878"], "stint_ids": ["Barlow, G. P___North Borneo___1905", "Barlow, G. Pratt___Sarawak___1894"]} -->
# Dossier case_barlow_g-pratt_e1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `barlow_g-pratt_e1878`

- Printed name: **BARLOW, G. PRATT**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1896-L37402.v` — printed in editions [1896, 1897, 1898, 1899, 1900, 1905, 1906]:**

> BARLOW, G. PRATT.—Cadet, Sarawak Civil Service, May, 1878; resdt., (2nd class), 3rd div., Jan., 1887; result, Muka, Oct., 1890; ag. resdt., Baram, July, 1892; of Biutulu, Aug., 1893; resdt., Lower Rejang, Oct., 1894.

**Version `col1894-L30172.v` — printed in editions [1894]:**

> BARLOW, G. PRATT.—Cadet, Sarawak Civil Service, May, 1878; resdt. (2nd class), 3rd div., Jan., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Cadet, Sarawak Civil Service | Sarawak | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 1 | 1887 | resdt., (2nd class), 3rd div | Sarawak *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 2 | 1890 | result, Muka | Sarawak *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 3 | 1892 | ag. resdt., Baram | Sarawak *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 4 | 1893 | of Biutulu | Sarawak *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900, 1905, 1906] |
| 5 | 1894 | resdt., Lower Rejang | Sarawak *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900, 1905, 1906] |

## Candidate stint `Barlow, G. P___North Borneo___1905`

- Staff-list name: **Barlow, G. P** | colony: **North Borneo** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | G. P. Barlow | Resident, 2nd Class, 3rd Division | Civil Establishment | — | — |
| 1906 | G. P. Barlow | Resident, 2nd Class, 3rd Division | Civil Establishment | — | — |

### Deterministic checks: `barlow_g-pratt_e1878` vs `Barlow, G. P___North Borneo___1905`

- [PASS] surname_gate: bio 'BARLOW' vs stint 'Barlow, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Barlow, G. Pratt___Sarawak___1894`

- Staff-list name: **Barlow, G. Pratt** | colony: **Sarawak** | listed 1894–1900 | editions [1894, 1897, 1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | G. P. Barlow | Resident, 2nd Class, 4th Division | Chief Officers | — | — |
| 1897 | G. Pratt Barlow | Resident 2nd Class, 3rd Division | Civil Establishment | — | — |
| 1898 | G. Pratt Barlow | Resident 2nd Class, 3rd Division | Civil Establishment | — | — |
| 1900 | G. P. Barlow | Resident-at-Class, 3rd Division | Civil Establishment | — | — |

### Deterministic checks: `barlow_g-pratt_e1878` vs `Barlow, G. Pratt___Sarawak___1894`

- [PASS] surname_gate: bio 'BARLOW' vs stint 'Barlow, G. Pratt' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1894-1900
- [FAIL] position_sim: best 41 vs bar 60: 'resdt., Lower Rejang' ~ 'Resident 2nd Class, 3rd Division'
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

