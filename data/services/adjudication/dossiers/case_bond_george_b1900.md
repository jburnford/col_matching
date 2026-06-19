<!-- {"case_id": "case_bond_george_b1900", "bio_ids": ["bond_george_b1900"], "stint_ids": ["Bond, G. H___Hong Kong___1937"]} -->
# Dossier case_bond_george_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bond_george_b1900'] carry a single initial only — the namesake trap applies.

## Biography `bond_george_b1900`

- Printed name: **BOND, George**
- Birth year: 1900 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33789.v` — printed in editions [1950, 1951]:**

> BOND, George.—b. 1900; apptd. W/T stn., Maur., 1923; ch. inspr., E. & T. dept., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | apptd. W/T stn. | Mauritius | [1950, 1951] |
| 1 | 1939 | ch. inspr., E. & T. dept | Mauritius *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Bond, G. H___Hong Kong___1937`

- Staff-list name: **Bond, G. H** | colony: **Hong Kong** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | G. H. Bond | Architect | Public Works Department | — | — |
| 1939 | G. H. Bond | Architect | Public Works Department | — | — |
| 1940 | G. H. Bond | Architects | Public Works Department | — | — |

### Deterministic checks: `bond_george_b1900` vs `Bond, G. H___Hong Kong___1937`

- [PASS] surname_gate: bio 'BOND' vs stint 'Bond, G. H' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1937, birth 1900 (age 37)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
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

