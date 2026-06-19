<!-- {"case_id": "case_van-renen_andries-christoffel_e1890", "bio_ids": ["van-renen_andries-christoffel_e1890"], "stint_ids": ["van Renen, A. C___Cape of Good Hope___1896"]} -->
# Dossier case_van-renen_andries-christoffel_e1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `van-renen_andries-christoffel_e1890`

- Printed name: **VAN RENEN, Andries Christoffel**
- Birth year: not printed
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L68972.v` — printed in editions [1931]:**

> VAN RENEN, Andries Christoffel.—Appointed 7th Jan., 1890 to the law dept., Cape of Good Hope; astt. mag., Sept., 1901; mag., Feb., 1908; senr. relieving mag., Sept., 1912; mag., Port Elizabeth, Jan., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | law dept. | Cape of Good Hope | [1931] |
| 1 | 1901 | astt. mag. | — | [1931] |
| 2 | 1908 | mag. | — | [1931] |
| 3 | 1912 | senr. relieving mag. | — | [1931] |
| 4 | 1930 | mag. | Port Elizabeth | [1931] |

## Candidate stint `van Renen, A. C___Cape of Good Hope___1896`

- Staff-list name: **van Renen, A. C** | colony: **Cape of Good Hope** | listed 1896–1897 | editions [1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | A. C. van Renen | Examiner of Accounts | Accounting Branch | — | — |
| 1897 | A. C. van Renen | Examiner of Accounts | Accounting Branch | — | — |

### Deterministic checks: `van-renen_andries-christoffel_e1890` vs `van Renen, A. C___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'VAN RENEN' vs stint 'van Renen, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1896-1897
- [FAIL] position_sim: best 21 vs bar 60: 'law dept.' ~ 'Examiner of Accounts'
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

