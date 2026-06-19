<!-- {"case_id": "case_prince_k-w_b1927", "bio_ids": ["prince_k-w_b1927"], "stint_ids": ["Prince, K. W___Leeward Islands___1955"]} -->
# Dossier case_prince_k-w_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `prince_k-w_b1927`

- Printed name: **PRINCE, K. W**
- Birth year: 1927 (attested in editions [1955, 1956, 1957])
- Appears in editions: [1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L22327.v` — printed in editions [1955, 1956, 1957]:**

> PRINCE, K. W.—b. 1927; ed. Cent. British Sch., Hong Kong, Strand Sch., Lond.; Cannings Coll., Bath, Regent St. Polytechnic, Lond.; chief engrnr., elec. light dept., St. Kitts, 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1954 | chief engrnr., elec. light dept. | St. Kitts | [1955, 1956, 1957] |

## Candidate stint `Prince, K. W___Leeward Islands___1955`

- Staff-list name: **Prince, K. W** | colony: **Leeward Islands** | listed 1955–1956 | editions [1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | K W. Prince | Chief Engineer | Civil Establishment | — | — |
| 1956 | K. W. Prince | Chief Engineer | Civil Establishment | — | — |

### Deterministic checks: `prince_k-w_b1927` vs `Prince, K. W___Leeward Islands___1955`

- [PASS] surname_gate: bio 'PRINCE' vs stint 'Prince, K. W' (exact)
- [PASS] initials: bio ['K', 'W'] ~ stint ['K', 'W']
- [PASS] age_gate: stint starts 1955, birth 1927 (age 28)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1956
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

