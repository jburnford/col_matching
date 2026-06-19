<!-- {"case_id": "case_lesuer_elizabeth-josephine_b1894", "bio_ids": ["lesuer_elizabeth-josephine_b1894"], "stint_ids": ["Lester, E___Gold Coast___1927"]} -->
# Dossier case_lesuer_elizabeth-josephine_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lesuer_elizabeth-josephine_b1894`

- Printed name: **LESUER, Elizabeth Josephine**
- Birth year: 1894 (attested in editions [1948, 1949])
- Honours: B.A.O, M.B, O.B.E (1948)
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L34018.v` — printed in editions [1948, 1949]:**

> LESUER, Elizabeth Josephine, O.B.E. (1948), M.B., Ch.B., B.A.O., D.P.H.(I.), D.T.M. & H. (Lond.)—b. 1894; ed. National Univ. of Ireland; med. offr. and pathologist, Sarawak, 1922; civ. intern., 1941-45.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | med. offr. and pathologist | Sarawak | [1948, 1949] |
| 1 | 1941–1945 | civ. intern | Sarawak *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Lester, E___Gold Coast___1927`

- Staff-list name: **Lester, E** | colony: **Gold Coast** | listed 1927–1932 | editions [1927, 1928, 1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. Lester | Office Assistant | Education Department | — | — |
| 1928 | E. Lester | Office Assistant | Education Department | — | — |
| 1929 | E. Lester | Office Assistant | Education Department | — | — |
| 1930 | E. Lester | Office Assistant | Education Department | — | — |
| 1932 | E. Lester | Office Assistant | Education Department | — | — |

### Deterministic checks: `lesuer_elizabeth-josephine_b1894` vs `Lester, E___Gold Coast___1927`

- [PASS] surname_gate: bio 'LESUER' vs stint 'Lester, E' (fuzzy:1)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E']
- [PASS] age_gate: stint starts 1927, birth 1894 (age 33)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1932
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

