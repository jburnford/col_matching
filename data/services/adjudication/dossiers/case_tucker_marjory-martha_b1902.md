<!-- {"case_id": "case_tucker_marjory-martha_b1902", "bio_ids": ["tucker_marjory-martha_b1902"], "stint_ids": ["Tucker, Miss L. M___Gold Coast___1929"]} -->
# Dossier case_tucker_marjory-martha_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 53 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Tucker, Miss L. M___Gold Coast___1929` is also gate-compatible with biography(ies) outside this case: ['tucker_l-m_e1926', 'tucker_leslie_e1897'] (already linked elsewhere or filtered).

## Biography `tucker_marjory-martha_b1902`

- Printed name: **TUCKER, Marjory Martha**
- Birth year: 1902 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L36304.v` — printed in editions [1949, 1950, 1951]:**

> TUCKER, Marjory Martha.—b. 1902; ed. pvt.e sch. and hosp. for sick children, Gt. Ormond, Guy's, and General Lying In Hosp., Lond.; nursing sister, Gib., 1930; N. Rhod., 1936; matron, gr. II, 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | nursing sister | Gibraltar | [1949, 1950, 1951] |
| 1 | 1936 | nursing sister | Northern Rhodesia | [1949, 1950, 1951] |
| 2 | 1949 | matron, gr. II | Northern Rhodesia *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Tucker, Miss L. M___Gold Coast___1929`

- Staff-list name: **Tucker, Miss L. M** | colony: **Gold Coast** | listed 1929–1932 | editions [1929, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | Miss L. M. Tucker | Organizer of Infant and Female Education | Education Department | — | — |
| 1932 | Miss L. M. Tucker | Organizers of Infant and Female Education | Education Department | — | — |

### Deterministic checks: `tucker_marjory-martha_b1902` vs `Tucker, Miss L. M___Gold Coast___1929`

- [PASS] surname_gate: bio 'TUCKER' vs stint 'Tucker, Miss L. M' (exact)
- [PASS] initials: bio ['M', 'M'] ~ stint ['M', 'L', 'M']
- [PASS] age_gate: stint starts 1929, birth 1902 (age 27)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1932
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

