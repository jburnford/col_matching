<!-- {"case_id": "case_mcnamara_d-h-a_b1923", "bio_ids": ["mcnamara_d-h-a_b1923"], "stint_ids": ["McNamara, D. H. A___Leeward Islands___1953"]} -->
# Dossier case_mcnamara_d-h-a_b1923

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcnamara_d-h-a_b1923`

- Printed name: **McNAMARA, D. H. A**
- Birth year: 1923 (attested in editions [1954, 1955, 1956, 1957])
- Appears in editions: [1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1954-L21443.v` — printed in editions [1954, 1955, 1956, 1957]:**

> McNAMARA, D. H. A.—b. 1923; ed. Queen's Royal Coll., Trin.; barrister-at-law, Lincoln's Inn; registr. and addl. mag., St. V., 1947; mag., St. Kitts, 1952; crown atty., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | registr. and addl. mag. | St. Vincent | [1954, 1955, 1956, 1957] |
| 1 | 1952 | mag. | St. Kitts | [1954, 1955, 1956, 1957] |
| 2 | 1957 | crown atty | St. Kitts *(inherited from previous clause)* | [1954, 1955, 1956, 1957] |

## Candidate stint `McNamara, D. H. A___Leeward Islands___1953`

- Staff-list name: **McNamara, D. H. A** | colony: **Leeward Islands** | listed 1953–1955 | editions [1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | D. H. A. McNamara | Magistrate | Civil Establishment | — | — |
| 1954 | D. H. A. McNamara | Magistrate | Civil Establishment | — | — |
| 1955 | D. H. A. McNamara | Magistrate | Civil Establishment | — | — |

### Deterministic checks: `mcnamara_d-h-a_b1923` vs `McNamara, D. H. A___Leeward Islands___1953`

- [PASS] surname_gate: bio 'McNAMARA' vs stint 'McNamara, D. H. A' (exact)
- [PASS] initials: bio ['D', 'H', 'A'] ~ stint ['D', 'H', 'A']
- [PASS] age_gate: stint starts 1953, birth 1923 (age 30)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1955
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

