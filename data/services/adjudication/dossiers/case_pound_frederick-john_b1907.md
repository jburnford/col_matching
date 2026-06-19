<!-- {"case_id": "case_pound_frederick-john_b1907", "bio_ids": ["pound_frederick-john_b1907"], "stint_ids": ["Pound, F. J___Trinidad and Tobago___1937"]} -->
# Dossier case_pound_frederick-john_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pound_frederick-john_b1907`

- Printed name: **POUND, Frederick John**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951])
- Honours: O.B.E.
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35314.v` — printed in editions [1948, 1949, 1950, 1951]:**

> POUND, Frederick John, O.B.E., Ph.D., B.Sc. (Lond.), B.Sc. (Reading).—b. 1907; ed. Sexey's Reading, and I.C.T.A. (cocoa research); cocoa agronomist, 1935; senr. agric. offr., Trin., 1944; dep. dir., agric. (crop husbandry), 1948; visited S. America 1937, 1938, 1942 and 1944 on cocoa research.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | cocoa agronomist | — | [1948, 1949, 1950, 1951] |
| 1 | 1944 | senr. agric. offr. | Trinidad | [1948, 1949, 1950, 1951] |
| 2 | 1948 | dep. dir., agric. (crop husbandry) | — | [1948, 1949, 1950, 1951] |

## Candidate stint `Pound, F. J___Trinidad and Tobago___1937`

- Staff-list name: **Pound, F. J** | colony: **Trinidad and Tobago** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | F. J. Pound | Cocoa Agronomist | Scientific and Technical Staff | — | — |
| 1937 | F. J. Pound | Superintendent, River Estate | Botanical Department | — | — |
| 1939 | F. J. Pound | Superintendent, River Estate | Botanical Department | — | — |
| 1939 | F. J. Pound | Cocoa Agronomist | Department of Agriculture | — | — |
| 1940 | F. J. Pound | Agronomist | Department of Agriculture | — | — |

### Deterministic checks: `pound_frederick-john_b1907` vs `Pound, F. J___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'POUND' vs stint 'Pound, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1937, birth 1907 (age 30)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
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

