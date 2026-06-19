<!-- {"case_id": "case_gunasekereva_septimus-thodorosus_b1881", "bio_ids": ["gunasekereva_septimus-thodorosus_b1881"], "stint_ids": ["Gunasekera, S. T___Ceylon___1925"]} -->
# Dossier case_gunasekereva_septimus-thodorosus_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gunasekereva_septimus-thodorosus_b1881`

- Printed name: **GUNASEKEREVA, SEPTIMUS THODOROSUS**
- Birth year: 1881 (attested in editions [1927])
- Appears in editions: [1927]

### Verbatim printed entry text (OCR)

**Version `col1927-L59468.v` — printed in editions [1927]:**

> GUNASEKEREVA, SEPTIMUS THODOROSUS, L.R.C.P. (Lond.), M.R.C.S. (Eng.), D.P.H. (Lond.), L.M.S. (Ceylon).—B. 1881; 1st house surg., gen. hosp., Colombo, Ceylon, Sept., 1904; med. offr., Kandy, Jan., 1907; ag. 3rd surg., gen. hosp., Colombo, Oct., 1908; dir., ankylostomiasis campaign, Dikoya and Amella, Oct., 1917 to Mar., 1920; sany. offr., Apr., 1920; ag. sany. commr., Oct., 1922; asst. dir., sany. services, Oct., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | 1st house surg., gen. hosp., Colombo | Ceylon | [1927] |
| 1 | 1907 | med. offr., Kandy | Ceylon *(inherited from previous clause)* | [1927] |
| 2 | 1908 | ag. 3rd surg., gen. hosp., Colombo | Ceylon *(inherited from previous clause)* | [1927] |
| 3 | 1917–1920 | dir., ankylostomiasis campaign, Dikoya and Amella | Ceylon *(inherited from previous clause)* | [1927] |
| 4 | 1920 | sany. offr | Ceylon *(inherited from previous clause)* | [1927] |
| 5 | 1922 | ag. sany. commr | Ceylon *(inherited from previous clause)* | [1927] |
| 6 | 1925 | asst. dir., sany. services | Ceylon *(inherited from previous clause)* | [1927] |

## Candidate stint `Gunasekera, S. T___Ceylon___1925`

- Staff-list name: **Gunasekera, S. T** | colony: **Ceylon** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | S. T. Gunasekera | Sanitary Commissioner | Sanitary Branch | — | — |
| 1927 | S. T. Gunasekera | Assistant Director of Sanitary Services | Medical Department | — | — |

### Deterministic checks: `gunasekereva_septimus-thodorosus_b1881` vs `Gunasekera, S. T___Ceylon___1925`

- [PASS] surname_gate: bio 'GUNASEKEREVA' vs stint 'Gunasekera, S. T' (fuzzy:2)
- [PASS] initials: bio ['S', 'T'] ~ stint ['S', 'T']
- [PASS] age_gate: stint starts 1925, birth 1881 (age 44)
- [PASS] colony: 7 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1925-1927
- [PASS] position_sim: best 72 vs bar 60: 'asst. dir., sany. services' ~ 'Assistant Director of Sanitary Services'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1927] pos~72 (bar: >=2)
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

