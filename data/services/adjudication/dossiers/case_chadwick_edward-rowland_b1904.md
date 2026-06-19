<!-- {"case_id": "case_chadwick_edward-rowland_b1904", "bio_ids": ["chadwick_edward-rowland_b1904"], "stint_ids": ["Chadwick, E. R___Nigeria___1934"]} -->
# Dossier case_chadwick_edward-rowland_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chadwick_edward-rowland_b1904`

- Printed name: **CHADWICK, Edward Rowland**
- Birth year: 1904 (attested in editions [1953, 1954])
- Honours: O.B.E
- Appears in editions: [1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1953-L16836.v` — printed in editions [1953, 1954]:**

> CHADWICK, E. R., O.B.E.—b. 1904; ed. R. Masonic Sch. and Sheff. Univ.; admin. offr., Nig., 1927; senr. dist. offr., 1946; admin. offr., cl. I, 1948; senr. res., 1952; community dev. sec., E. region, 1952.

**Version `col1949-L31015.v` — printed in editions [1949, 1950, 1951]:**

> CHADWICK, Edward Rowland, O.B.E.—b. 1904; ed. R. Masonic Sch. and Sheff. Univ., B.Sc. (hons.); admin. offr., Nig., 1927; senr. dist. offr., 1946; admin. offr., cl. I, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | admin. offr. | Nigeria | [1949, 1950, 1951, 1953, 1954] |
| 1 | 1946 | senr. dist. offr | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954] |
| 2 | 1948 | admin. offr., cl. I | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954] |
| 3 | 1952 | senr. res | Nigeria *(inherited from previous clause)* | [1953, 1954] |

## Candidate stint `Chadwick, E. R___Nigeria___1934`

- Staff-list name: **Chadwick, E. R** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | E. R. Chadwick | Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |
| 1934 | E. R. Chadwick | — | Administrative Service | — | — |
| 1939 | E. R. Chadwick | Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `chadwick_edward-rowland_b1904` vs `Chadwick, E. R___Nigeria___1934`

- [PASS] surname_gate: bio 'CHADWICK' vs stint 'Chadwick, E. R' (exact)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1934, birth 1904 (age 30)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 34 vs bar 60: 'admin. offr.' ~ 'Assistant Secretary'
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

