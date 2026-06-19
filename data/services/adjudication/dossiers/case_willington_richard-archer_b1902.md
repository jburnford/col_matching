<!-- {"case_id": "case_willington_richard-archer_b1902", "bio_ids": ["willington_richard-archer_b1902"], "stint_ids": ["Wallington, R. A___Tanganyika___1940"]} -->
# Dossier case_willington_richard-archer_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `willington_richard-archer_b1902`

- Printed name: **WILLINGTON, Richard Archer**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951])
- Honours: O.B.E. (1956)
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1948-L36921.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WILLINGTON, Richard Archer.—b. 1902; ed. Bromsgrove Sch., Univ. Coll. of N. Wales and Wadham Coll., Oxford, M.A. (Oxon.); on mil. serv. 1940-45, maj.; educ. offr., T.T., 1929.

**Version `col1950-L40470.v` — printed in editions [1950, 1951]:**

> WALLINGTON, Richard Archer.—b. 1902; ed. Bromsgrove Sch., Univ. Coll. of N. Wales and Wadhall Coll., Oxford, M.A. (Oxon); educ. offr., T.T., 1929.

**Version `col1956-L24815.v` — printed in editions [1956, 1957]:**

> WALLINGTON, R. A., O.B.E. (1956).—b. 1902; ed. Bromsgrove Sch., Univ. Coll. of N. Wales and Wadham Coll., Oxford; educ. offr., Tang., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | educ. offr. | Tanganyika Territory | [1948, 1949, 1950, 1951, 1956, 1957] |
| 1 | 1940–1945 | maj. | — | [1948, 1949, 1950, 1951] |

## Candidate stint `Wallington, R. A___Tanganyika___1940`

- Staff-list name: **Wallington, R. A** | colony: **Tanganyika** | listed 1940–1949 | editions [1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | R. A. Wallington | Superintendent of Education | Education | — | — |
| 1949 | R. A. Wallington | Education Officer | Education | — | — |

### Deterministic checks: `willington_richard-archer_b1902` vs `Wallington, R. A___Tanganyika___1940`

- [PASS] surname_gate: bio 'WILLINGTON' vs stint 'Wallington, R. A' (fuzzy:1)
- [PASS] initials: bio ['R', 'A'] ~ stint ['R', 'A']
- [PASS] age_gate: stint starts 1940, birth 1902 (age 38)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1949
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

