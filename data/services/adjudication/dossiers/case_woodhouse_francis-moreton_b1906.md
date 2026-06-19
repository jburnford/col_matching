<!-- {"case_id": "case_woodhouse_francis-moreton_b1906", "bio_ids": ["woodhouse_francis-moreton_b1906"], "stint_ids": ["Woodhouse, F. M___Nigeria___1956"]} -->
# Dossier case_woodhouse_francis-moreton_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `woodhouse_francis-moreton_b1906`

- Printed name: **WOODHOUSE, Francis Moreton**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L37011.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WOODHOUSE, Francis Moreton.—b. 1906; ed. Cambridge, B.A.; cadet, Nig., 1929; asst. dist. offr., 1932; dist. offr., 1939; admin. offr., cl. II, 1941.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1932 | asst. dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1939 | dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1941 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Woodhouse, F. M___Nigeria___1956`

- Staff-list name: **Woodhouse, F. M** | colony: **Nigeria** | listed 1956–1958 | editions [1956, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | F. M. Woodhouse | Commissioner of Lands | Civil Establishment | — | — |
| 1958 | F. M. Woodhouse | Commissioner of Lands | Civil Establishment | — | — |

### Deterministic checks: `woodhouse_francis-moreton_b1906` vs `Woodhouse, F. M___Nigeria___1956`

- [PASS] surname_gate: bio 'WOODHOUSE' vs stint 'Woodhouse, F. M' (exact)
- [PASS] initials: bio ['F', 'M'] ~ stint ['F', 'M']
- [PASS] age_gate: stint starts 1956, birth 1906 (age 50)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1958
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

