<!-- {"case_id": "case_sands_william-norman_b1875", "bio_ids": ["sands_william-norman_b1875"], "stint_ids": ["Sands, William N___St Vincent___1909", "Sands, William N___Windward Islands___1906"]} -->
# Dossier case_sands_william-norman_b1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sands_william-norman_b1875`

- Printed name: **SANDS, WILLIAM NORMAN**
- Birth year: 1875 (attested in editions [1932])
- Honours: F.L.S
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L63706.v` — printed in editions [1932]:**

> SANDS, WILLIAM NORMAN, F.L.S.—B. 1875; curator, botanic and experiment stations, Antigua, W. Indies, Sept., 1899; agrl. supt., St. Vincent, Mar., 1904; asst. economic botanist, agrl. dept., F.M.S., Jan., 1920; ag. economic botanist, various periods of 1921-1930; prin. agrl. offr., Kedah, July, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | curator, botanic and experiment stations, Antigua, W. Indies | — | [1932] |
| 1 | 1904 | agrl. supt. | St. Vincent | [1932] |
| 2 | 1920 | asst. economic botanist, agrl. dept. | Federated Malay States | [1932] |
| 3 | 1921–1930 | ag. economic botanist, various periods of | Federated Malay States *(inherited from previous clause)* | [1932] |
| 4 | 1930 | prin. agrl. offr. | Kedah | [1932] |

## Candidate stint `Sands, William N___St Vincent___1909`

- Staff-list name: **Sands, William N** | colony: **St Vincent** | listed 1909–1917 | editions [1909, 1910, 1911, 1912, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1910 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1911 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1912 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1917 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |

### Deterministic checks: `sands_william-norman_b1875` vs `Sands, William N___St Vincent___1909`

- [PASS] surname_gate: bio 'SANDS' vs stint 'Sands, William N' (exact)
- [PASS] initials: bio ['W', 'N'] ~ stint ['W', 'N']
- [PASS] age_gate: stint starts 1909, birth 1875 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'St Vincent'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1917
- [FAIL] position_sim: best 50 vs bar 60: 'agrl. supt.' ~ 'Agricultural Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Sands, William N___Windward Islands___1906`

- Staff-list name: **Sands, William N** | colony: **Windward Islands** | listed 1906–1919 | editions [1906, 1907, 1908, 1913, 1914, 1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | W. N. Sands | Agricultural Superintendent | Botanical Station | — | — |
| 1907 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1908 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1913 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1914 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1915 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1918 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |
| 1919 | W. N. Sands | Agricultural Superintendent | Agricultural Department | — | — |

### Deterministic checks: `sands_william-norman_b1875` vs `Sands, William N___Windward Islands___1906`

- [PASS] surname_gate: bio 'SANDS' vs stint 'Sands, William N' (exact)
- [PASS] initials: bio ['W', 'N'] ~ stint ['W', 'N']
- [PASS] age_gate: stint starts 1906, birth 1875 (age 31)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1919
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

