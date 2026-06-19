<!-- {"case_id": "case_nevin_henry-miller_b1896", "bio_ids": ["nevin_henry-miller_b1896"], "stint_ids": ["Nevin, H. M___Straits Settlements___1931"]} -->
# Dossier case_nevin_henry-miller_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nevin_henry-miller_b1896`

- Printed name: **NEVIN, HENRY MILLER**
- Birth year: 1896 (attested in editions [1939, 1940])
- Honours: D.T.M, M.A, M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69358.v` — printed in editions [1939, 1940]:**

> NEVIN, HENRY MILLER, M.A., M.B., B.Ch., B.A.O. (Univ. of Dub.), D.T.M., D.T.H. (Lpool), D.P.H. (Univ. of Dub.).—B. 1896; ed. Rathmines Coll., Dublin and Dublin Univ.; Great War, 2nd lt., Royal Inniskilling Fusiliers; M. O. Malaya, Aug., 1927; pathologist II, I.M.R., Aug., 1929; title changed to pathologist, Aug., 1937; do., Penang, Oct., 1937; ag. do., S.S., March, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | M. O. Malaya | — | [1939, 1940] |
| 1 | 1929 | pathologist II, I.M.R | — | [1939, 1940] |
| 2 | 1937 | title changed to pathologist | — | [1939, 1940] |
| 3 | 1937 | do., Penang | — | [1939, 1940] |
| 4 | 1939 | ag. do. | Straits Settlements | [1939, 1940] |

## Candidate stint `Nevin, H. M___Straits Settlements___1931`

- Staff-list name: **Nevin, H. M** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. M. Nevin | Medical Officer | Medical | — | — |
| 1932 | H. M. Nevin | Medical Officer | Medical | — | — |
| 1933 | H. M. Nevin | Medical Officer | Medical | — | — |

### Deterministic checks: `nevin_henry-miller_b1896` vs `Nevin, H. M___Straits Settlements___1931`

- [PASS] surname_gate: bio 'NEVIN' vs stint 'Nevin, H. M' (exact)
- [PASS] initials: bio ['H', 'M'] ~ stint ['H', 'M']
- [PASS] age_gate: stint starts 1931, birth 1896 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

