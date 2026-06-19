<!-- {"case_id": "case_nisbet_john-gray_b1895", "bio_ids": ["nisbet_john-gray_b1895"], "stint_ids": ["Nisbet, J. G___Kenya___1925"]} -->
# Dossier case_nisbet_john-gray_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nisbet_john-gray_b1895`

- Printed name: **NISBET, JOHN GRAY**
- Birth year: 1895 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69408.v` — printed in editions [1939, 1940]:**

> NISBET, JOHN GRAY.—B. 1895; war serv., R.E.s., 1914-19; astt. engnr., Uganda rly., 1919; resigned, 1920; astt. engnr., K.U.R. & H., 1924; sr. astt. engnr., 1925; dist. engnr., 1928; sr. dist. engnr., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | astt. engnr., Uganda rly | Uganda | [1939, 1940] |
| 1 | 1920 | resigned | Uganda *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1924 | astt. engnr., K.U.R. & H | Uganda *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1925 | sr. astt. engnr | Uganda *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1928 | dist. engnr | Uganda *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1936 | sr. dist. engnr | Uganda *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Nisbet, J. G___Kenya___1925`

- Staff-list name: **Nisbet, J. G** | colony: **Kenya** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | J. G. Nisbet | Assistant Engineers | Engineering | — | — |
| 1927 | J. G. Nisbet | Assistant Engineers | Engineering | — | — |

### Deterministic checks: `nisbet_john-gray_b1895` vs `Nisbet, J. G___Kenya___1925`

- [PASS] surname_gate: bio 'NISBET' vs stint 'Nisbet, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1925, birth 1895 (age 30)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

