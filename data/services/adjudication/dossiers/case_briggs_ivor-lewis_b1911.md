<!-- {"case_id": "case_briggs_ivor-lewis_b1911", "bio_ids": ["briggs_ivor-lewis_b1911"], "stint_ids": ["Briggs, I. L___Northern Rhodesia___1939"]} -->
# Dossier case_briggs_ivor-lewis_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `briggs_ivor-lewis_b1911`

- Printed name: **BRIGGS, Ivor Lewis**
- Birth year: 1911 (attested in editions [1957])
- Honours: M.B
- Appears in editions: [1949, 1950, 1951, 1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L21424.v` — printed in editions [1957]:**

> BRIGGS, I. L.—b. 1911; ed. St. John's Coll., Jo'burg, Witwatersrand and Edin. Univs.; mil. serv., 1939-45, maj.; M.O., N. Rhod., 1938; specialist, 1951; secon. fedl. govt.

**Version `col1949-L30666.v` — printed in editions [1949, 1950, 1951]:**

> BRIGGS, Ivor Lewis, M.B., Ch.B.—b. 1911 ; ed. St. Johns Coll., Jo'burg., Witwatersrand Univ. and Edin. Univ. ; on mil. serv., 1939-45, maj. ; med. offr., N. Rhod., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | M.O. | Northern Rhodesia | [1949, 1950, 1951, 1957] |
| 1 | 1951 | specialist | Northern Rhodesia *(inherited from previous clause)* | [1957] |

## Candidate stint `Briggs, I. L___Northern Rhodesia___1939`

- Staff-list name: **Briggs, I. L** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | I. L. Briggs | Medical Officer | Medical | — | — |
| 1940 | I. L. Briggs | Medical Officer | Health | — | — |

### Deterministic checks: `briggs_ivor-lewis_b1911` vs `Briggs, I. L___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'BRIGGS' vs stint 'Briggs, I. L' (exact)
- [PASS] initials: bio ['I', 'L'] ~ stint ['I', 'L']
- [PASS] age_gate: stint starts 1939, birth 1911 (age 28)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

