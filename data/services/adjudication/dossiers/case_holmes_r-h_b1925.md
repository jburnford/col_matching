<!-- {"case_id": "case_holmes_r-h_b1925", "bio_ids": ["holmes_r-h_b1925"], "stint_ids": ["Holmes, H___Northern Rhodesia___1949"]} -->
# Dossier case_holmes_r-h_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 49 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Holmes, H___Northern Rhodesia___1949` is also gate-compatible with biography(ies) outside this case: ['holmes_harold-kennard_e1900'] (already linked elsewhere or filtered).

## Biography `holmes_r-h_b1925`

- Printed name: **HOLMES, R. H**
- Birth year: 1925 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L18166.v` — printed in editions [1964, 1965, 1966]:**

> HOLMES, R. H.—b. 1925; ed. St. Philips Gram. Sch., Birmingham, Christian Bros. Secondary Sch., Ireland, and Sch. Civil Engng., Univ. Coll., Dublin; asst. engrnr., Uga., 1953; exec. engrnr., water devel., 1955; senr. exec. engrnr., water devel., 1963. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | asst. engrnr. | Uganda | [1964, 1965, 1966] |
| 1 | 1955 | exec. engrnr., water devel | Uganda *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1963 | senr. exec. engrnr., water devel | Uganda *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Holmes, H___Northern Rhodesia___1949`

- Staff-list name: **Holmes, H** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. Holmes | Education Officer | Education | — | — |
| 1951 | H. Holmes | Education Officer | Education | — | — |

### Deterministic checks: `holmes_r-h_b1925` vs `Holmes, H___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'HOLMES' vs stint 'Holmes, H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1949, birth 1925 (age 24)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
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

