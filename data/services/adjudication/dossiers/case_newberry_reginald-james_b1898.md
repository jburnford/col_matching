<!-- {"case_id": "case_newberry_reginald-james_b1898", "bio_ids": ["newberry_reginald-james_b1898"], "stint_ids": ["Newberry, R. J___Nigeria___1934"]} -->
# Dossier case_newberry_reginald-james_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `newberry_reginald-james_b1898`

- Printed name: **NEWBERRY, Reginald James**
- Birth year: 1898 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L34898.v` — printed in editions [1948]:**

> NEWBERRY, Reginald James.—b. 1898; ed. Hele's Sch., Exeter, W.O. Sch. of Educ. (teach. dip.), Springfield Coll., Birmingham (B.of E.teach.cert.); on mil. serv., 1914-18; agric. schlmsr., Nig., 1927; agric. educ. offr., 1939; author of Elementary Reader in Agriculture for Southern Nigerian Elementary Schools and Teachers Handbook.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | agric. schlmsr. | Nigeria | [1948] |
| 1 | 1939 | agric. educ. offr | Nigeria *(inherited from previous clause)* | [1948] |

## Candidate stint `Newberry, R. J___Nigeria___1934`

- Staff-list name: **Newberry, R. J** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | R. J. Newberry | Schoolmasters | Agriculture | — | — |
| 1939 | R. J. Newberry | Schoolmaster | Agriculture | — | — |

### Deterministic checks: `newberry_reginald-james_b1898` vs `Newberry, R. J___Nigeria___1934`

- [PASS] surname_gate: bio 'NEWBERRY' vs stint 'Newberry, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1934, birth 1898 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 56 vs bar 60: 'agric. schlmsr.' ~ 'Schoolmaster'
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

