<!-- {"case_id": "case_hawkes_william-blackburne_b1883", "bio_ids": ["hawkes_william-blackburne_b1883"], "stint_ids": ["Hawkes, W. B___Straits Settlements___1931"]} -->
# Dossier case_hawkes_william-blackburne_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hawkes_william-blackburne_b1883`

- Printed name: **HAWKES, WILLIAM BLACKBURNE**
- Birth year: 1883 (attested in editions [1932, 1933])
- Honours: A.I.M. and M (1911), V.D
- Appears in editions: [1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1932-L60976.v` — printed in editions [1932, 1933]:**

> HAWKES, CAPT. WILLIAM BLACKBURNE, V.D., A.I.M. and M. (1911).—B. 1883; ch. asst. to comsnr., Abomee expdn., Ashanti, July, 1908; capt. Legion of Frontiersmen, 1911-1914; supernmy. inspr., mines, Batu Gajah, July, 1914; inspr., mines, Tapah, Sept., 1914; licensing offr., motor cars, Batang Padang in addn., Jan., 1915; 2nd lieut., 3rd Royal Sappers and Miners (seconded), Indian Army, Sept., 1917; capt., 1st (K.G.O.), Jan., 1918; demob., Dec., 1919 (General Service and Victory and Afghan Medals); suppr., mines, Dec., 1919; capt., R.E. reg. army R. of O., Jan., 1920; 1st cls. mag. in addn., Sept., 1920; 1st cls. mag., Ulu Selangor, Feb., 1922; asst. warden, mines, Sept., 1924; ag. warden, mines, in addn., Oct.-Nov., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | ch. asst. to comsnr., Abomee expdn. | Ashanti | [1932, 1933] |
| 1 | 1911–1914 | capt. Legion of Frontiersmen | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 2 | 1914 | supernmy. inspr., mines, Batu Gajah | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 3 | 1915 | licensing offr., motor cars, Batang Padang in addn | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 4 | 1917 | 2nd lieut., 3rd Royal Sappers and Miners (seconded), Indian Army | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 5 | 1918 | capt., 1st (K.G.O.) | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 6 | 1919 | demob | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 7 | 1920 | capt., R.E. reg. army R. of O | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 8 | 1922 | 1st cls. mag., Ulu Selangor | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 9 | 1924 | asst. warden, mines | Ashanti *(inherited from previous clause)* | [1932, 1933] |
| 10 | 1930 | ag. warden, mines, in addn., Oct.- | Ashanti *(inherited from previous clause)* | [1932, 1933] |

## Candidate stint `Hawkes, W. B___Straits Settlements___1931`

- Staff-list name: **Hawkes, W. B** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | W. B. Hawkes | Assistant Wardens of Mines | Mines | — | — |
| 1933 | W. B. Hawkes | Senior Inspectors of Mines | Mines | — | — |

### Deterministic checks: `hawkes_william-blackburne_b1883` vs `Hawkes, W. B___Straits Settlements___1931`

- [PASS] surname_gate: bio 'HAWKES' vs stint 'Hawkes, W. B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1931, birth 1883 (age 48)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

