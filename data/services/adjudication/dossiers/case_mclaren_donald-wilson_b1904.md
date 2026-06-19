<!-- {"case_id": "case_mclaren_donald-wilson_b1904", "bio_ids": ["mclaren_donald-wilson_b1904"], "stint_ids": ["McLaren, D___Uganda___1936"]} -->
# Dossier case_mclaren_donald-wilson_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mclaren_donald-wilson_b1904`

- Printed name: **McLAREN, Donald Wilson**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Honours: M.B
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34375.v` — printed in editions [1948, 1949, 1950, 1951]:**

> McLAREN, Donald Wilson, M.B., B.S. (Durham), D.T.M. (Liv.).—b. 1904; ed. Royal Gram. Sch., Newcastle-on-Tyne and Durham Univ.; med. offr., Nig., 1928; S.M.O., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | med. offr. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1948 | S.M.O | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `McLaren, D___Uganda___1936`

- Staff-list name: **McLaren, D** | colony: **Uganda** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | D. McLaren | Clerk | Land and Survey Department | — | — |
| 1937 | D. McLaren | Clerk | Land and Survey Department | — | — |
| 1939 | D. McLaren | Clerks | Land and Survey Department | — | — |
| 1940 | D. McLaren | Clerks | Land and Survey Department | — | — |

### Deterministic checks: `mclaren_donald-wilson_b1904` vs `McLaren, D___Uganda___1936`

- [PASS] surname_gate: bio 'McLAREN' vs stint 'McLaren, D' (exact)
- [PASS] initials: bio ['D', 'W'] ~ stint ['D']
- [PASS] age_gate: stint starts 1936, birth 1904 (age 32)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

