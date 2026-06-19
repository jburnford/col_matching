<!-- {"case_id": "case_lewis_i-j_b1927", "bio_ids": ["lewis_i-j_b1927"], "stint_ids": ["Lewis, I. J___High Commission Territories___1963"]} -->
# Dossier case_lewis_i-j_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 157 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lewis, I. J___High Commission Territories___1963` is also gate-compatible with biography(ies) outside this case: ['lewis_j_b1924'] (already linked elsewhere or filtered).

## Biography `lewis_i-j_b1927`

- Printed name: **LEWIS, I. J**
- Birth year: 1927 (attested in editions [1962, 1963, 1964])
- Honours: M.B.E
- Appears in editions: [1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1962-L23580.v` — printed in editions [1962, 1963, 1964]:**

> LEWIS, I. J., M.B.E.—b. 1927; ed. Univ. of S. Africa; mil. serv., 1945; tssetse surv. offr., Nyasa., 1950; tssetse fly control offr., Bech. Prot., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | tssetse surv. offr. | Nyasaland | [1962, 1963, 1964] |
| 1 | 1953 | tssetse fly control offr. | Bechuanaland | [1962, 1963, 1964] |

## Candidate stint `Lewis, I. J___High Commission Territories___1963`

- Staff-list name: **Lewis, I. J** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | I. J. Lewis | Tsese Fly Control Officer | Secretariat | — | — |
| 1964 | I. J. Lewis | Tsetse Fly Control Officer | Secretariat | — | — |

### Deterministic checks: `lewis_i-j_b1927` vs `Lewis, I. J___High Commission Territories___1963`

- [PASS] surname_gate: bio 'LEWIS' vs stint 'Lewis, I. J' (exact)
- [PASS] initials: bio ['I', 'J'] ~ stint ['I', 'J']
- [PASS] age_gate: stint starts 1963, birth 1927 (age 36)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
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

