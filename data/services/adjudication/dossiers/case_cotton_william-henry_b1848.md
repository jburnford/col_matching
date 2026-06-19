<!-- {"case_id": "case_cotton_william-henry_b1848", "bio_ids": ["cotton_william-henry_b1848"], "stint_ids": ["Cotton, W. H___Canada___1913"]} -->
# Dossier case_cotton_william-henry_b1848

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cotton_william-henry_b1848`

- Printed name: **COTTON, WILLIAM HENRY**
- Birth year: 1848 (attested in editions [1913, 1914])
- Appears in editions: [1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1913-L44966.v` — printed in editions [1913, 1914]:**

> COTTON, MAJOR GEN. WILLIAM HENRY.—B. 1848; ed. Toronto and Quebec High Schls.; 1st cls. certif., Roy. Mil. Schl., Quebec, 1865; lieut., Quebec garrison arty., 1866; lieut., Ottawa garrison arty., 1868; capt., schl. of gunnery, 1871; brevet-maj., Canadian arty., 1872; lieut.-col., 1882; col., 1900; brig.-gen., 1907; major-gen., June, 1912; D. O. C., M.D., No. 3, 1893; No. 4, 1897; O. C., Ottawa brigade-, 1897; qtrmr.-gen., 1901; master, gen. ordnance, 1904; O. C., Western Ontario, 1908-1911; O. C., 2nd div., 1911-1912; inspr.-gen. of Canadian militia, Dec., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | 1st cls. certif., Roy. Mil. Schl., Quebec | — | [1913, 1914] |
| 1 | 1866 | lieut., Quebec garrison arty | — | [1913, 1914] |
| 2 | 1868 | lieut., Ottawa garrison arty | — | [1913, 1914] |
| 3 | 1871 | capt., schl. of gunnery | — | [1913, 1914] |
| 4 | 1872 | brevet-maj., Canadian arty | — | [1913, 1914] |
| 5 | 1882 | lieut.-col | — | [1913, 1914] |
| 6 | 1893 | D. O. C., M.D., No. 3 | Dominions Office | [1913, 1914] |
| 7 | 1897 | No. 4 | Dominions Office *(inherited from previous clause)* | [1913, 1914] |
| 8 | 1900 | col | — | [1913, 1914] |
| 9 | 1901 | qtrmr.-gen | Dominions Office *(inherited from previous clause)* | [1913, 1914] |
| 10 | 1904 | master, gen. ordnance | Dominions Office *(inherited from previous clause)* | [1913, 1914] |
| 11 | 1907 | brig.-gen | — | [1913, 1914] |
| 12 | 1908–1911 | O. C., Western Ontario | Dominions Office *(inherited from previous clause)* | [1913, 1914] |
| 13 | 1911–1912 | O. C., 2nd div | Dominions Office *(inherited from previous clause)* | [1913, 1914] |
| 14 | 1912 | major-gen | — | [1913, 1914] |
| 15 | 1912 | inspr.-gen. of Canadian militia | Dominions Office *(inherited from previous clause)* | [1913, 1914] |

## Candidate stint `Cotton, W. H___Canada___1913`

- Staff-list name: **Cotton, W. H** | colony: **Canada** | listed 1913–1915 | editions [1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | W. H. Cotton | Inspector-General | Militia and Defence | — | — |
| 1914 | Major-General W. H. Cotton | Inspector-General | Department of Militia and Defence | — | Major-General |
| 1915 | W. H. Cotton | Inspector-General | Permanent Railway Commission | — | — |

### Deterministic checks: `cotton_william-henry_b1848` vs `Cotton, W. H___Canada___1913`

- [PASS] surname_gate: bio 'COTTON' vs stint 'Cotton, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1913, birth 1848 (age 65)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1915
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

