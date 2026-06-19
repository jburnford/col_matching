<!-- {"case_id": "case_wilkes_richard-leslie-vaughan_b1904", "bio_ids": ["wilkes_richard-leslie-vaughan_b1904"], "stint_ids": ["Wilkes, R. L. V___Sierra Leone___1957"]} -->
# Dossier case_wilkes_richard-leslie-vaughan_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wilkes_richard-leslie-vaughan_b1904`

- Printed name: **WILKES, Richard Leslie Vaughan**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36853.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WILKES, Richard Leslie Vaughan.—b. 1904; ed. Fonthill, E. Grinstead, Eton and Balliol Coll., Oxford, B.A. (hons.) (Oxon.); cadet, Nig., 1928; admin. offr., cl. II, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1946 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Wilkes, R. L. V___Sierra Leone___1957`

- Staff-list name: **Wilkes, R. L. V** | colony: **Sierra Leone** | listed 1957–1958 | editions [1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | R. L. V. Wilkes | Chairman | Public Service Commission | — | — |
| 1958 | R. L. V. Wilkes | Public Service Commission, Chairman | Civil Establishment | — | — |

### Deterministic checks: `wilkes_richard-leslie-vaughan_b1904` vs `Wilkes, R. L. V___Sierra Leone___1957`

- [PASS] surname_gate: bio 'WILKES' vs stint 'Wilkes, R. L. V' (exact)
- [PASS] initials: bio ['R', 'L', 'V'] ~ stint ['R', 'L', 'V']
- [PASS] age_gate: stint starts 1957, birth 1904 (age 53)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1958
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

