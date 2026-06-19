<!-- {"case_id": "case_hardwick_neville-william_b1906", "bio_ids": ["hardwick_neville-william_b1906"], "stint_ids": ["Hardwick, N. W___Nigeria___1934"]} -->
# Dossier case_hardwick_neville-william_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hardwick_neville-william_b1906`

- Printed name: **HARDWICK, Neville William**
- Birth year: 1906 (attested in editions [1957])
- Appears in editions: [1949, 1950, 1951, 1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L23821.v` — printed in editions [1957]:**

> HARDWICK, N. W.—b. 1906; ed. Cranleigh Sch. and Wye Coll.; agric. dept., Nig., 1928; senr. inspr., produce, 1945; prin. produce offr., 1950; chief produce offr., 1954.

**Version `col1949-L32670.v` — printed in editions [1949, 1950, 1951]:**

> HARDWICK, Neville William.—b. 1906; ed. Cranleigh Sch. and Wye Agric. Coll. (Lond. Univ.) (cert.); apptd. agric. dept., Nig., 1928; senr. prod. offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | agric. dept. | Nigeria | [1949, 1950, 1951, 1957] |
| 1 | 1945 | senr. inspr., produce | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951, 1957] |
| 2 | 1950 | prin. produce offr | Nigeria *(inherited from previous clause)* | [1957] |
| 3 | 1954 | chief produce offr | Nigeria *(inherited from previous clause)* | [1957] |

## Candidate stint `Hardwick, N. W___Nigeria___1934`

- Staff-list name: **Hardwick, N. W** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | N. W. Hardwick | Produce Inspectors | Agriculture | — | — |
| 1939 | N. W. Hardwick | Inspectors of Produce | Agriculture | — | — |

### Deterministic checks: `hardwick_neville-william_b1906` vs `Hardwick, N. W___Nigeria___1934`

- [PASS] surname_gate: bio 'HARDWICK' vs stint 'Hardwick, N. W' (exact)
- [PASS] initials: bio ['N', 'W'] ~ stint ['N', 'W']
- [PASS] age_gate: stint starts 1934, birth 1906 (age 28)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 36 vs bar 60: 'agric. dept.' ~ 'Produce Inspectors'
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

