<!-- {"case_id": "case_hoey_alfred-ernest_e1900", "bio_ids": ["hoey_alfred-ernest_e1900"], "stint_ids": ["Hoey, A. E___Kenya___1918"]} -->
# Dossier case_hoey_alfred-ernest_e1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hoey_alfred-ernest_e1900`

- Printed name: **HOEY, ALFRED ERNEST**
- Birth year: not printed
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L56567.v` — printed in editions [1925]:**

> HOEY, ALFRED ERNEST.—S.A. War, 1900-1; asst. acot., P.W.D., E.A.P., 1908; acot., 1913; trooper, E.A. Mtd. Rifles, 1915; paymr. and machine gun offr., K.A.R., 1916-17; ag. ch. acot., P.W.D., Kenya, 1923; ag. gov't. coast agt., 1924; Queen's S.A. med. (6 clasps), '1914-15' Star, Br. War and Victory med.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1901 | — | South Africa | [1925] |
| 1 | 1908–1908 | asst. acot., P.W.D. | East Africa Protectorate | [1925] |
| 2 | 1913–1913 | acot. | — | [1925] |
| 3 | 1915–1915 | trooper, E.A. Mtd. Rifles | East Africa | [1925] |
| 4 | 1916–1917 | paymr. and machine gun offr., K.A.R. | — | [1925] |
| 5 | 1923–1923 | ag. ch. acot., P.W.D. | Kenya | [1925] |
| 6 | 1924–1924 | ag. gov't. coast agt. | — | [1925] |

## Candidate stint `Hoey, A. E___Kenya___1918`

- Staff-list name: **Hoey, A. E** | colony: **Kenya** | listed 1918–1925 | editions [1918, 1919, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | A. E. Hoey | Accountant | Public Works | — | — |
| 1919 | A. E. Hoey | Accountants | Public Works | — | — |
| 1922 | A. E. Hoey | Accountant | Public Works | — | — |
| 1923 | A. E. Hoey | Accountant | Public Works | — | — |
| 1924 | A. E. Hoey | Accountant and Storekeeper | Accounts and Stores | — | — |
| 1925 | A. E. Hoey | Accountant and Storekeeper | Accounts and Stores | — | — |

### Deterministic checks: `hoey_alfred-ernest_e1900` vs `Hoey, A. E___Kenya___1918`

- [PASS] surname_gate: bio 'HOEY' vs stint 'Hoey, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1918-1925
- [FAIL] position_sim: best 42 vs bar 60: 'ag. ch. acot., P.W.D.' ~ 'Accountant'
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

