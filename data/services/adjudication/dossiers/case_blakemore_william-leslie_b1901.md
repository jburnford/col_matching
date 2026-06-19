<!-- {"case_id": "case_blakemore_william-leslie_b1901", "bio_ids": ["blakemore_william-leslie_b1901"], "stint_ids": ["Blakemore, W. L___Straits Settlements___1931"]} -->
# Dossier case_blakemore_william-leslie_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blakemore_william-leslie_b1901`

- Printed name: **BLAKEMORE, WILLIAM LESLIE**
- Birth year: 1901 (attested in editions [1939, 1940])
- Honours: M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L64876.v` — printed in editions [1939, 1940]:**

> BLAKEMORE, WILLIAM LESLIE, M.B., Ch. B. (Birm.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), D.P.H. (Lond.), D.T.M. & H. (L'pool).—B. 1901; ed. Wolverhampton Gram. Schi. and Birm. Univ.; M.O., Malaya, July, 1928; ag. senr. health offr., Penang, May, 1931; ag. ch. med. offr., Malacca, Aug., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | M.O. | Malaya | [1939, 1940] |
| 1 | 1931 | ag. senr. health offr., Penang | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1937 | ag. ch. med. offr., Malacca | Malaya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Blakemore, W. L___Straits Settlements___1931`

- Staff-list name: **Blakemore, W. L** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | W. L. Blakemore | Medical and Health Officer | Penang | — | — |
| 1933 | W. L. Blakemore | Medical and Health Officer | Medical | — | — |
| 1934 | W. L. Blakemore | Medical and Health Officer | Malacca | — | — |
| 1936 | W. L. Blakemore | Medical and Health Officer | Medical | — | — |

### Deterministic checks: `blakemore_william-leslie_b1901` vs `Blakemore, W. L___Straits Settlements___1931`

- [PASS] surname_gate: bio 'BLAKEMORE' vs stint 'Blakemore, W. L' (exact)
- [PASS] initials: bio ['W', 'L'] ~ stint ['W', 'L']
- [PASS] age_gate: stint starts 1931, birth 1901 (age 30)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1936
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

