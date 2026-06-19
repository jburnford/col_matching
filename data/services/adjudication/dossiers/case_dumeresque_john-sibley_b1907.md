<!-- {"case_id": "case_dumeresque_john-sibley_b1907", "bio_ids": ["dumeresque_john-sibley_b1907"], "stint_ids": ["Dumeresque, J. S___Singapore___1949"]} -->
# Dossier case_dumeresque_john-sibley_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dumeresque_john-sibley_b1907`

- Printed name: **DUMERESQUE, John Sibley**
- Birth year: 1907 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L32336.v` — printed in editions [1948]:**

> DUMERESQUE, John Sibley.—b.1907; on mil. serv. 2nd world war, maj.; attd. Mal. bdcasting. Corp.; dir. of bdcasting, Mal., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | dir. of bdcasting | Malaya | [1948] |

## Candidate stint `Dumeresque, J. S___Singapore___1949`

- Staff-list name: **Dumeresque, J. S** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. S. Dumeresque | Director of Broadcasting | Broadcasting | — | — |
| 1951 | J. S. Dumeresque | Director of Broadcasting, Malaya | Broadcasting | — | — |

### Deterministic checks: `dumeresque_john-sibley_b1907` vs `Dumeresque, J. S___Singapore___1949`

- [PASS] surname_gate: bio 'DUMERESQUE' vs stint 'Dumeresque, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [FAIL] colony: no placed event resolves to 'Singapore'
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

