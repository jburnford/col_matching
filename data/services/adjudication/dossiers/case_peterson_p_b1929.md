<!-- {"case_id": "case_peterson_p_b1929", "bio_ids": ["peterson_p_b1929"], "stint_ids": ["Paterson, E. H. P___Cyprus___1949"]} -->
# Dossier case_peterson_p_b1929

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 57 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['peterson_p_b1929'] carry a single initial only — the namesake trap applies.

## Biography `peterson_p_b1929`

- Printed name: **PETERSON, P**
- Birth year: 1929 (attested in editions [1960, 1961, 1963, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L26909.v` — printed in editions [1960, 1961, 1963, 1965, 1966]:**

> PETERSON, P.—b. 1929; ed. Wellington Coll., and Imperial Coll., London Univ.; med. offr., Mal., 1949; scientific offr., royal observatory, H.K., 1955; publ. The Rainfall of H.K. (R.O.T.N. No. 17).

**Version `col1962-L25331.v` — printed in editions [1962]:**

> PETERTON, P.—b. 1929; ed. Wellington Coll., and Imperial Coll., London Univ.; met. offr., Mal., 1949; scientific offr., royal observatory, H.K., 1955.

**Version `col1964-L20687.v` — printed in editions [1964]:**

> PETTERSON, P.—b. 1929; ed. Wellington Coll., and Imperial Coll., London Univ.; met. offr., Mal., 1949; scientific offr., royal observatory, H.K., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | med. offr. | Malaya | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1955 | scientific offr., royal observatory | Hong Kong | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Paterson, E. H. P___Cyprus___1949`

- Staff-list name: **Paterson, E. H. P** | colony: **Cyprus** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. H. P. Paterson | Nursing Sisters | Medical and Health Administration | — | — |
| 1951 | Miss E. H. P. Paterson | Nursing Sisters | Hospitals | — | — |

### Deterministic checks: `peterson_p_b1929` vs `Paterson, E. H. P___Cyprus___1949`

- [PASS] surname_gate: bio 'PETERSON' vs stint 'Paterson, E. H. P' (fuzzy:1)
- [PASS] initials: bio ['P'] ~ stint ['E', 'H', 'P']
- [PASS] age_gate: stint starts 1949, birth 1929 (age 20)
- [FAIL] colony: no placed event resolves to 'Cyprus'
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

