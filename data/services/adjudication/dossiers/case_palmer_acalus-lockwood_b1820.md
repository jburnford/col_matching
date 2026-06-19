<!-- {"case_id": "case_palmer_acalus-lockwood_b1820", "bio_ids": ["palmer_acalus-lockwood_b1820"], "stint_ids": ["Palmer, A. L___Canada___1880"]} -->
# Dossier case_palmer_acalus-lockwood_b1820

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 25 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `palmer_acalus-lockwood_b1820`

- Printed name: **PALMER, ACALUS LOCKWOOD**
- Birth year: 1820 (attested in editions [1889, 1890, 1894, 1896, 1897, 1898])
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1889-L34993.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898]:**

> PALMER, ACALUS LOCKWOOD.—Born 1820; called to the bar, N. Brunswick, 1846; Q.C., 1867; and leader of the bar, 1874-9; member of Dominion house of commons for St. John, 1871-9; puise judge, supreme ct., N.B., and judge in equity, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1846 | called to the bar | New Brunswick | [1889, 1890, 1894, 1896, 1897, 1898] |
| 1 | 1867 | Q.C | New Brunswick *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898] |
| 2 | 1871–1879 | member of Dominion house of commons for St. John | New Brunswick *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898] |
| 3 | 1874–1879 | and leader of the bar | New Brunswick *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898] |
| 4 | 1879 | puise judge, supreme ct., N.B., and judge in equity | New Brunswick *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898] |

## Candidate stint `Palmer, A. L___Canada___1880`

- Staff-list name: **Palmer, A. L** | colony: **Canada** | listed 1880–1894 | editions [1880, 1883, 1886, 1888, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | A. L. Palmer | Puisne Judges | Judicial Establishment | — | — |
| 1883 | A. L. Palmer | Puisne Judges | Judicial Establishment | — | — |
| 1886 | A. Palmer | Member | House of Assembly | — | — |
| 1886 | A. L. Palmer | Puisne Judge | Judicial Establishment | — | — |
| 1888 | A. L. Palmer | Puisne Judge | Judicial Establishment | — | — |
| 1888 | A. Palmer | Member | House of Assembly | — | — |
| 1890 | A. Palmer | Member | House of Assembly | — | — |
| 1890 | A. L. Palmer | Puisne Judges | Provincial Establishment | — | — |
| 1894 | A. L. Palmer | Puisne Judges | Provincial Establishment | — | — |

### Deterministic checks: `palmer_acalus-lockwood_b1820` vs `Palmer, A. L___Canada___1880`

- [PASS] surname_gate: bio 'PALMER' vs stint 'Palmer, A. L' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1880, birth 1820 (age 60)
- [PASS] colony: 5 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1880-1894
- [PASS] position_sim: best 100 vs bar 60: 'member of Dominion house of commons for St. John' ~ 'Member'
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

