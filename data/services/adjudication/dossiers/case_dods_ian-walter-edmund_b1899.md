<!-- {"case_id": "case_dods_ian-walter-edmund_b1899", "bio_ids": ["dods_ian-walter-edmund_b1899"], "stint_ids": ["Dods, I. W. E___Nigeria___1934"]} -->
# Dossier case_dods_ian-walter-edmund_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dods_ian-walter-edmund_b1899`

- Printed name: **DODS, Ian Walter Edmund**
- Birth year: 1899 (attested in editions [1950])
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L35013.v` — printed in editions [1950]:**

> DODS, Ian Walter Edmund.—b. 1899; ed. Malvern Coll., and R.M. Acad., Woolwich (under offr.), lieut., R.F.A., 1919–22; admin. offr., Nig., 1922; cl. IV., 1922; cl. III., 1930; cl. II., 1943; cl. I., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | admin. offr. | Nigeria | [1950] |
| 1 | 1930 | cl. III | Nigeria *(inherited from previous clause)* | [1950] |
| 2 | 1943 | cl. II | Nigeria *(inherited from previous clause)* | [1950] |
| 3 | 1944 | cl. I | Nigeria *(inherited from previous clause)* | [1950] |

## Candidate stint `Dods, I. W. E___Nigeria___1934`

- Staff-list name: **Dods, I. W. E** | colony: **Nigeria** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | I. W. E. Dods | — | Administrative Service | — | — |
| 1936 | I. W. E. Dods | Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `dods_ian-walter-edmund_b1899` vs `Dods, I. W. E___Nigeria___1934`

- [PASS] surname_gate: bio 'DODS' vs stint 'Dods, I. W. E' (exact)
- [PASS] initials: bio ['I', 'W', 'E'] ~ stint ['I', 'W', 'E']
- [PASS] age_gate: stint starts 1934, birth 1899 (age 35)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 8 vs bar 60: 'cl. III' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

