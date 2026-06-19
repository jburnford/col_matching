<!-- {"case_id": "case_plummer_gladys_b1891", "bio_ids": ["plummer_gladys_b1891"], "stint_ids": ["Plummer, G. D. G___Nigeria___1958"]} -->
# Dossier case_plummer_gladys_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['plummer_gladys_b1891'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Plummer, G. D. G___Nigeria___1958` is also gate-compatible with biography(ies) outside this case: ['plummer_g-d-g_b1905'] (already linked elsewhere or filtered).

## Biography `plummer_gladys_b1891`

- Printed name: **PLUMMER, Gladys**
- Birth year: 1891 (attested in editions [1948, 1949, 1950, 1951])
- Honours: O.B.E
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35267.v` — printed in editions [1948, 1949, 1950, 1951]:**

> PLUMMER, Gladys, O.B.E.—b. 1891; ed. County Sec. Sch., Streatham, Univ. Coll., Lond. and Lond. Day Training Coll., B.A. (dip. in educ.); apptd., Nig., 1931; dep. dir., educ. (women), 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | apptd. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1945 | dep. dir., educ. (women) | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Plummer, G. D. G___Nigeria___1958`

- Staff-list name: **Plummer, G. D. G** | colony: **Nigeria** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | G. D. G. Plummer | Deputy Director of Public Works | — | — | — |
| 1960 | G. D. G. Plummer | Controller, Works Services | Civil Establishment | — | — |

### Deterministic checks: `plummer_gladys_b1891` vs `Plummer, G. D. G___Nigeria___1958`

- [PASS] surname_gate: bio 'PLUMMER' vs stint 'Plummer, G. D. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'D', 'G']
- [PASS] age_gate: stint starts 1958, birth 1891 (age 67)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1958-1960
- [FAIL] position_sim: best 53 vs bar 60: 'dep. dir., educ. (women)' ~ 'Deputy Director of Public Works'
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

