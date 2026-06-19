<!-- {"case_id": "case_jameson_frank-robert-wordsworth_b1883", "bio_ids": ["jameson_frank-robert-wordsworth_b1883"], "stint_ids": ["Jameson, R. W___Canada___1898"]} -->
# Dossier case_jameson_frank-robert-wordsworth_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jameson_frank-robert-wordsworth_b1883`

- Printed name: **JAMESON, FRANK ROBERT WORDSWORTH**
- Birth year: 1883 (attested in editions [1933])
- Honours: D.S.O
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L61011.v` — printed in editions [1933]:**

> JAMESON, FRANK ROBERT WORDSWORTH, D.S.O., M.C.—B. 1883; ed. Uppingham and Emmanuel Coll., Cambridge; B.A.; on active serv., H.A.C., Sept., 1914 to Apr., 1916; R.E.'s (signal serv.), Apr., 1916 to Apr., 1919; served in Flanders, France and Italy; awarded M.C. (2 bars) and D.S.O.; capt., 1918; twice ment. in desps.; inspr., Egyptian miny. of finance, Oct., 1919 to June, 1927; ast. pvt. sec. (appts.) to S. of S. for the Cols., Apr., 1928; temp. ag. prin., C.O., Oct., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916–1919 | R.E.'s (signal serv.) | — | [1933] |
| 1 | 1918 | capt | — | [1933] |
| 2 | 1919–1927 | inspr., Egyptian miny. of finance | — | [1933] |
| 3 | 1928 | ast. pvt. sec. (appts.) to S. of S. for the Cols | — | [1933] |
| 4 | 1930 | temp. ag. prin. | Colonial Office | [1933] |

## Candidate stint `Jameson, R. W___Canada___1898`

- Staff-list name: **Jameson, R. W** | colony: **Canada** | listed 1898–1899 | editions [1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | R. W. Jameson | Member | — | — | — |
| 1899 | R. W. Jameson | — | — | — | — |

### Deterministic checks: `jameson_frank-robert-wordsworth_b1883` vs `Jameson, R. W___Canada___1898`

- [PASS] surname_gate: bio 'JAMESON' vs stint 'Jameson, R. W' (exact)
- [PASS] initials: bio ['F', 'R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1898, birth 1883 (age 15)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1899
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

