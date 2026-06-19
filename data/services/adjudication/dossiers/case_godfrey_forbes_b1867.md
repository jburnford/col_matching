<!-- {"case_id": "case_godfrey_forbes_b1867", "bio_ids": ["godfrey_forbes_b1867"], "stint_ids": ["Godfrey, E. F___Cape of Good Hope___1905"]} -->
# Dossier case_godfrey_forbes_b1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['godfrey_forbes_b1867'] carry a single initial only — the namesake trap applies.

## Biography `godfrey_forbes_b1867`

- Printed name: **GODFREY, FORBES**
- Birth year: 1867 (attested in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932])
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1924-L54587.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]:**

> GODFREY, HON. FORBES, M.B., L.R.C.P. and S.—B. 1867; ed. Owen Sound, Ont., Coll. Inst., Toronto Univ. (M.B. and medallist); Univ. of Edinburgh and Glasgow (L.F.P. and S.); physician; el. to Ont. legis., 1907; re-el., 1908, 1911, 1914, 1919 and 1923; min. of pub. health and lab. in Ferguson adminstr., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | el. to Ont. legis. | Ontario | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1908 | re-el. | — | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |
| 2 | 1923 | min. of pub. health and lab. in Ferguson adminstr. | — | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Godfrey, E. F___Cape of Good Hope___1905`

- Staff-list name: **Godfrey, E. F** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | E. F. Godfrey | Clerk | Native Affairs Branch | — | — |
| 1906 | E. F. Godfrey | Clerk | Native Affairs Branch | — | — |
| 1907 | E. F. Godfrey | Clerk | Native Affairs Branch | — | — |
| 1908 | E. F. Godfrey | Clerk | Native Affairs Branch | — | — |
| 1909 | E. F. Godfrey | Clerks | Native Affairs Branch | — | — |

### Deterministic checks: `godfrey_forbes_b1867` vs `Godfrey, E. F___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'GODFREY' vs stint 'Godfrey, E. F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1905, birth 1867 (age 38)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

