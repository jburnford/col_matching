<!-- {"case_id": "case_buckley_francis-edmund_b1902", "bio_ids": ["buckley_francis-edmund_b1902"], "stint_ids": ["Buckley, E___Gold Coast___1949"]} -->
# Dossier case_buckley_francis-edmund_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `buckley_francis-edmund_b1902`

- Printed name: **BUCKLEY, Francis Edmund**
- Birth year: 1902 (attested in editions [1948, 1949, 1950])
- Honours: A.I.C.T.A, A.R.C.S
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L31491.v` — printed in editions [1948, 1949, 1950]:**

> BUCKLEY, Francis Edmund, A.R.C.S., A.I.C.T.A.—b. 1902; ed. Cheltenham Coll. and Imp. Coll. of Sci. and Tech., Lond.; col. agric. schol. at S.E. Agric. Coll. and at I.C.T.A.; supt. of agric. (later agric. offr.), Nig., 1928; senr. agric. offr., 1944; prin., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | supt. of agric. (later agric. offr.) | Nigeria | [1948, 1949, 1950] |
| 1 | 1944 | senr. agric. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1949 | prin | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Buckley, E___Gold Coast___1949`

- Staff-list name: **Buckley, E** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. Buckley | Collectors | Customs and Excise | — | — |
| 1950 | E. Buckley | Collectors | Customs and Excise | — | — |
| 1951 | E. Buckley | Collectors of Customs and Excise | Customs and Excise Department | — | — |

### Deterministic checks: `buckley_francis-edmund_b1902` vs `Buckley, E___Gold Coast___1949`

- [PASS] surname_gate: bio 'BUCKLEY' vs stint 'Buckley, E' (exact)
- [PASS] initials: bio ['F', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1949, birth 1902 (age 47)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

