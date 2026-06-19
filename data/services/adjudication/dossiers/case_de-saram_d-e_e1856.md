<!-- {"case_id": "case_de-saram_d-e_e1856", "bio_ids": ["de-saram_d-e_e1856"], "stint_ids": ["de Saram, D. E___Ceylon___1877"]} -->
# Dossier case_de-saram_d-e_e1856

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-saram_d-e_e1856`

- Printed name: **DE SARAM, D. E**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L27154.v` — printed in editions [1883, 1886]:**

> DE SARAM, D. E.—Acting commissioner of requests, &c., Gampola, Ceylon, 1862; a writer in the service of that colony, 1856; confirmed as commissioner of requests, Gampola, 1857; commissioner of requests and police magistrate, Kandy, 1862; police magistrate, Colombo, January, 1863; district judge, Kurunegala, 1868; acting district judge, Jaffna, May, 1873; confirmed, 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856 | a writer in the service of that colony | Ceylon *(inherited from previous clause)* | [1883, 1886] |
| 1 | 1857 | confirmed as commissioner of requests, Gampola | Ceylon *(inherited from previous clause)* | [1883, 1886] |
| 2 | 1862 | Acting commissioner of requests, &c., Gampola | Ceylon | [1883, 1886] |
| 3 | 1863 | police magistrate, Colombo | Ceylon *(inherited from previous clause)* | [1883, 1886] |
| 4 | 1868 | district judge, Kurunegala | Ceylon *(inherited from previous clause)* | [1883, 1886] |
| 5 | 1873 | acting district judge, Jaffna | Ceylon *(inherited from previous clause)* | [1883, 1886] |
| 6 | 1875 | confirmed | Ceylon *(inherited from previous clause)* | [1883, 1886] |

## Candidate stint `de Saram, D. E___Ceylon___1877`

- Staff-list name: **de Saram, D. E** | colony: **Ceylon** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | D. E. de Saram | District Judge and Joint Commissioner of Requests and Police Magistrate | District and Minor Courts | — | — |
| 1878 | D. E. de Saram | District Judge and Joint Commissioner of Requests and Police Magistrate | District and Minor Courts | — | — |
| 1879 | D. E. de Saram | District Judge and Joint Commissioner of Requests and Police Magistrate | Judicial Establishment | — | — |
| 1880 | D. E. de Saram | District Judge and Joint Commissioner of Requests and Police Magistrate | District and Minor Courts | — | — |
| 1883 | D. E. de Saram | District Judge and Joint Commissioner of Requests and Police Magistrate | District and Minor Courts | — | — |
| 1886 | D. E. de Saram | District Judge, Commissioner of Requests, Police Magistrate | District and Minor Courts | — | — |

### Deterministic checks: `de-saram_d-e_e1856` vs `de Saram, D. E___Ceylon___1877`

- [PASS] surname_gate: bio 'DE SARAM' vs stint 'de Saram, D. E' (exact)
- [PASS] initials: bio ['D', 'E'] ~ stint ['D', 'E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [FAIL] position_sim: best 21 vs bar 60: 'confirmed' ~ 'District Judge, Commissioner of Requests, Police Magistrate'
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

