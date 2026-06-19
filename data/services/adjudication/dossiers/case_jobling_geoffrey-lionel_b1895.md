<!-- {"case_id": "case_jobling_geoffrey-lionel_b1895", "bio_ids": ["jobling_geoffrey-lionel_b1895"], "stint_ids": ["Jobling, G. L___Nigeria___1956", "Jobling, G. L___Uganda___1928"]} -->
# Dossier case_jobling_geoffrey-lionel_b1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jobling, G. L___Nigeria___1956` is also gate-compatible with biography(ies) outside this case: ['jobling_geoffrey-lionel_b1899'] (already linked elsewhere or filtered).
- NOTE: stint `Jobling, G. L___Uganda___1928` is also gate-compatible with biography(ies) outside this case: ['jobling_geoffrey-lionel_b1899'] (already linked elsewhere or filtered).

## Biography `jobling_geoffrey-lionel_b1895`

- Printed name: **JOBLING, Geoffrey Lionel**
- Birth year: 1895 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L62183.v` — printed in editions [1937]:**

> JOBLING, Geoffrey Lionel—B. 1895; Bowen Schl., Brisbane; called to bar, Gray's Inn; served German S.W. Africa, 1915; R.A.F., 1918-19; law dept., B.S.A., Rhodesia, Nov., 1915; asst. regtr., Rhodesia; asst. offr. recr. in bankery, 1920; gen., asst. regtr., lands and deeds, births, deaths and marriages, asst. companies, asst. custodian enemy property, local clearing office, asst. regtr., Uganda, June, 1927; crown coun., Uganda Territory, Aug., 1929; ag. solr.-gen., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | served German S.W. Africa | — | [1937] |
| 1 | 1915 | law dept., B.S.A. | Rhodesia | [1937] |
| 2 | 1918–1919 | R.A.F | — | [1937] |
| 3 | 1920 | asst. offr. recr. in bankery | Rhodesia *(inherited from previous clause)* | [1937] |
| 4 | 1927 | gen., asst. regtr., lands and deeds, births, deaths and marriages, asst. companies, asst. custodian enemy property, local clearing office, asst. regtr. | Uganda | [1937] |
| 5 | 1929 | crown coun., Uganda Territory | Uganda | [1937] |
| 6 | 1934 | ag. solr.-gen | Uganda *(inherited from previous clause)* | [1937] |

## Candidate stint `Jobling, G. L___Nigeria___1956`

- Staff-list name: **Jobling, G. L** | colony: **Nigeria** | listed 1956–1958 | editions [1956, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | G. L. Jobling | Judges | Civil Establishment | — | — |
| 1958 | G. L. Jobling | Judge | Civil Establishment | — | — |

### Deterministic checks: `jobling_geoffrey-lionel_b1895` vs `Jobling, G. L___Nigeria___1956`

- [PASS] surname_gate: bio 'JOBLING' vs stint 'Jobling, G. L' (exact)
- [PASS] initials: bio ['G', 'L'] ~ stint ['G', 'L']
- [PASS] age_gate: stint starts 1956, birth 1895 (age 61)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1958
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Jobling, G. L___Uganda___1928`

- Staff-list name: **Jobling, G. L** | colony: **Uganda** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | G. L. Jobling | Registrar, High Court | Legal | — | — |
| 1929 | G. L. Jobling | Registrar, High Court | Legal | — | — |

### Deterministic checks: `jobling_geoffrey-lionel_b1895` vs `Jobling, G. L___Uganda___1928`

- [PASS] surname_gate: bio 'JOBLING' vs stint 'Jobling, G. L' (exact)
- [PASS] initials: bio ['G', 'L'] ~ stint ['G', 'L']
- [PASS] age_gate: stint starts 1928, birth 1895 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1928-1929
- [FAIL] position_sim: best 43 vs bar 60: 'crown coun., Uganda Territory' ~ 'Registrar, High Court'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

