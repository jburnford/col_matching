<!-- {"case_id": "case_borland_andrew-james_b1897", "bio_ids": ["borland_andrew-james_b1897"], "stint_ids": ["Borland, A. J___Aden___1939"]} -->
# Dossier case_borland_andrew-james_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `borland_andrew-james_b1897`

- Printed name: **BORLAND, Andrew James**
- Birth year: 1897 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L31288.v` — printed in editions [1948, 1949, 1950]:**

> BORLAND, Andrew James, O.B.E. (civ.)—b. 1897; Br. P.O., 1913; on mil. serv., 1914-19, Aden home guard, 1942-43, ag. maj.; P.O., Ken., Uga. and T.T., 1921; P.M.G., Aden, 1938; dep. P.M.G., G.C., 1946; P.M.G., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Br. P.O | — | [1948, 1949, 1950] |
| 1 | 1921 | P.O., Ken., Uga. and T.T | Uganda | [1948, 1949, 1950] |
| 2 | 1938 | P.M.G. | Aden | [1948, 1949, 1950] |
| 3 | 1946 | dep. P.M.G. | Gold Coast | [1948, 1949, 1950] |
| 4 | 1947 | P.M.G | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Borland, A. J___Aden___1939`

- Staff-list name: **Borland, A. J** | colony: **Aden** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. J. Borland | Colonial Postmaster | Civil Establishment | — | — |
| 1940 | A. J. Borland | Colonial Postmaster | Civil Establishment | — | — |

### Deterministic checks: `borland_andrew-james_b1897` vs `Borland, A. J___Aden___1939`

- [PASS] surname_gate: bio 'BORLAND' vs stint 'Borland, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1939, birth 1897 (age 42)
- [PASS] colony: 1 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 18 vs bar 60: 'P.M.G.' ~ 'Colonial Postmaster'
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

