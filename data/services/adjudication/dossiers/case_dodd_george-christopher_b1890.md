<!-- {"case_id": "case_dodd_george-christopher_b1890", "bio_ids": ["dodd_george-christopher_b1890"], "stint_ids": ["Dodd, G. C___Straits Settlements___1915"]} -->
# Dossier case_dodd_george-christopher_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dodd_george-christopher_b1890`

- Printed name: **DODD, GEORGE CHRISTOPHER**
- Birth year: 1890 (attested in editions [1932])
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L59733.v` — printed in editions [1932]:**

> DODD, GEORGE CHRISTOPHER.—B. 1890; barrister-at-law, Gray's Inn, 1930; cadet (S.S.), Nov., 1914; attd. to Chinese Prot., Singapore, Dec., 1914; attd., govt. monopolies, Singapore, Jan., 1915; asst. censor, cable office, Sept., 1917; attd. col. sect., Nov., 1918 to Jan., 1919; asst. prot., Chinese, Penang, Jly., 1922; ag. dep. treas., in addn., Nov., 1926; ag. dist. judge and 1st mag., Singapore, Jan., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | cadet (S.S.) | — | [1932] |
| 1 | 1914 | attd. to Chinese Prot. | Singapore | [1932] |
| 2 | 1915 | attd., govt. monopolies | Singapore | [1932] |
| 3 | 1917 | asst. censor, cable office | Singapore *(inherited from previous clause)* | [1932] |
| 4 | 1918–1919 | attd. col. sect | Singapore *(inherited from previous clause)* | [1932] |
| 5 | 1922 | asst. prot., Chinese, Penang, Jly | Singapore *(inherited from previous clause)* | [1932] |
| 6 | 1926 | ag. dep. treas., in addn | Singapore *(inherited from previous clause)* | [1932] |
| 7 | 1930 | barrister-at-law, Gray's Inn | — | [1932] |
| 8 | 1931 | ag. dist. judge and 1st mag. | Singapore | [1932] |

## Candidate stint `Dodd, G. C___Straits Settlements___1915`

- Staff-list name: **Dodd, G. C** | colony: **Straits Settlements** | listed 1915–1921 | editions [1915, 1917, 1918, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | G. C. Dodd | Cadets | Colonial Secretary's Office | — | — |
| 1915 | G. C. Dodd | Cadet | Cadet Service | — | — |
| 1917 | G. C. Dodd | Passed Cadet | Cadet Service | — | — |
| 1917 | G. C. Dodd | Clerks | Colonial Secretary's Office | — | — |
| 1918 | G. C. Dodd | Cadet | Colonial Secretary's Office | — | — |
| 1918 | G. C. Dodd | Passed Cadet | Cadet Service | — | — |
| 1919 | G. C. Dodd | Cadet Service Officer - Class V | Cadet Service | — | — |
| 1920 | G. C. Dodd | Officer, Cadet Service | Cadet Service | — | — |
| 1921 | G. C. Dodd | — | Civil Establishment | — | — |
| 1921 | G. C. Dodd | Assistant Superintendent, Government Monopolies | Malacca | — | — |

### Deterministic checks: `dodd_george-christopher_b1890` vs `Dodd, G. C___Straits Settlements___1915`

- [PASS] surname_gate: bio 'DODD' vs stint 'Dodd, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1915, birth 1890 (age 25)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1921
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

