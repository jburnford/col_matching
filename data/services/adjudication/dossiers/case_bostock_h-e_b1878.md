<!-- {"case_id": "case_bostock_h-e_b1878", "bio_ids": ["bostock_h-e_b1878"], "stint_ids": ["Bostock, Hewitt___Canada___1897", "Bostock, Hewitt___Canada___1912"]} -->
# Dossier case_bostock_h-e_b1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bostock_h-e_b1878`

- Printed name: **BOSTOCK, H. E**
- Birth year: 1878 (attested in editions [1931, 1932, 1933, 1934])
- Honours: M.I.C.E
- Appears in editions: [1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1931-L62656.v` — printed in editions [1931, 1932, 1933, 1934]:**

> BOSTOCK, MAJOR H. E., O.B.E. (Mily.), R. of O. (R.E.), M.I.C.E.—B. 1878; ed. Marlborough and Univ. Coll., London; asst. engnr., Gold Coast harbrs. and Sierra Leone harbr., 1909; Br. Army, France, R.E. (ment. in despatches), 1915-19; res. engnr., Lagos harbr. wks., 1921; port engnr., harbr. dept., Lagos, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | asst. engnr., Gold Coast harbrs. and Sierra Leone harbr | Gold Coast | [1931, 1932, 1933, 1934] |
| 1 | 1915–1919 | Br. Army, France, R.E. (ment. in despatches) | Gold Coast *(inherited from previous clause)* | [1931, 1932, 1933, 1934] |
| 2 | 1921 | res. engnr., Lagos harbr. wks | Lagos | [1931, 1932, 1933, 1934] |
| 3 | 1923 | port engnr., harbr. dept. | Lagos | [1931, 1932, 1933, 1934] |

## Candidate stint `Bostock, Hewitt___Canada___1897`

- Staff-list name: **Bostock, Hewitt** | colony: **Canada** | listed 1897–1900 | editions [1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | Hewitt Bostock | — | British Columbia | — | — |
| 1898 | Hewitt Bostock | Member | — | — | — |
| 1899 | Hewitt Bostock | Member | Legislative Assembly | — | — |
| 1900 | Hewitt Bostock | — | — | — | — |

### Deterministic checks: `bostock_h-e_b1878` vs `Bostock, Hewitt___Canada___1897`

- [PASS] surname_gate: bio 'BOSTOCK' vs stint 'Bostock, Hewitt' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H']
- [PASS] age_gate: stint starts 1897, birth 1878 (age 19)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bostock, Hewitt___Canada___1912`

- Staff-list name: **Bostock, Hewitt** | colony: **Canada** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Hewitt Bostock | Senator | Senate of Canada - Senators | — | — |
| 1913 | Hewitt Bostock | Senator | Senate | — | — |
| 1914 | Hewitt Bostock | Senator | Senate of Canada | — | — |
| 1915 | Hewitt Bostock | — | Senate | — | — |
| 1917 | Hewitt Bostock | Senator | Senate | — | — |
| 1918 | Hewitt Bostock | Senator | Senate | — | — |
| 1919 | Hewitt Bostock | Senator | Senate | — | — |
| 1920 | Hewitt Bostock | Senator | Senate | — | — |
| 1922 | Hewitt Bostock | Minister of Public Works | Public Works | — | — |
| 1922 | Hon. Hewitt Bostock | Senator | Senators | — | — |
| 1922 | Hewitt Bostock | Minister of Public Works | THE MINISTRY | — | — |

### Deterministic checks: `bostock_h-e_b1878` vs `Bostock, Hewitt___Canada___1912`

- [PASS] surname_gate: bio 'BOSTOCK' vs stint 'Bostock, Hewitt' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H']
- [PASS] age_gate: stint starts 1912, birth 1878 (age 34)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1922
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

