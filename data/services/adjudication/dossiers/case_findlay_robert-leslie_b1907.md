<!-- {"case_id": "case_findlay_robert-leslie_b1907", "bio_ids": ["findlay_robert-leslie_b1907"], "stint_ids": ["Findlay, R. L___Nigeria___1934"]} -->
# Dossier case_findlay_robert-leslie_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `findlay_robert-leslie_b1907`

- Printed name: **FINDLAY, Robert Leslie**
- Birth year: 1907 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32583.v` — printed in editions [1948, 1950, 1951]:**

> FINDLAY, Robert Leslie.—b. 1907; ed. Fettes Coll., Edin. and Pembroke Coll., Camb., B.A. (Camb.); cadet, Nig., 1930; admin. offr., cl. II, 1948.

**Version `col1949-L32013.v` — printed in editions [1949]:**

> FINLAY, Robert Leslie.—b. 1907; ed. Fettes Coll., Edin. and Pembroke Coll., Camb., B.A. (Camb.); cadet, Nig., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1948 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1948, 1950, 1951] |

## Candidate stint `Findlay, R. L___Nigeria___1934`

- Staff-list name: **Findlay, R. L** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | R. L. Findlay | — | Administrative Service | — | — |
| 1939 | R. L. Findlay | Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `findlay_robert-leslie_b1907` vs `Findlay, R. L___Nigeria___1934`

- [PASS] surname_gate: bio 'FINDLAY' vs stint 'Findlay, R. L' (exact)
- [PASS] initials: bio ['R', 'L'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1934, birth 1907 (age 27)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 25 vs bar 60: 'cadet' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

