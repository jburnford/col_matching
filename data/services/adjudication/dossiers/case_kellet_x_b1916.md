<!-- {"case_id": "case_kellet_x_b1916", "bio_ids": ["kellet_x_b1916"], "stint_ids": ["Keller, H. A___Hong Kong___1937"]} -->
# Dossier case_kellet_x_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['kellet_x_b1916'] carry a single initial only — the namesake trap applies.

## Biography `kellet_x_b1916`

- Printed name: **KELLET, (no given names printed)**
- Birth year: 1916 (attested in editions [1959, 1960, 1961, 1962, 1963])
- Honours: F. R. S
- Appears in editions: [1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1959-L24802.v` — printed in editions [1959, 1960, 1961, 1962, 1963]:**

> KELLET, F. R. S.—b. 1916; ed. Calcutta Univ.; mil. serv., 1940-46, I.M. Army S.; M.O.; gr. 'C', St. Lucia, 1947; M.O. gr. 'C' (public health) Trin., 1953; S.M.O.(S) malaria div., 1956. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | gr. 'C' | St. Lucia | [1959, 1960, 1961, 1962, 1963] |
| 1 | 1953 | M.O. gr. 'C' (public health) Trin | St. Lucia *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |
| 2 | 1956 | S.M.O.(S) malaria div | St. Lucia *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Keller, H. A___Hong Kong___1937`

- Staff-list name: **Keller, H. A** | colony: **Hong Kong** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | H. A. Keller | Honorary Consul | Consular Service | — | — |
| 1939 | H. A. Keller | Vice-Consul i/o Consular Agency | Honorary Consuls | — | — |

### Deterministic checks: `kellet_x_b1916` vs `Keller, H. A___Hong Kong___1937`

- [PASS] surname_gate: bio 'KELLET' vs stint 'Keller, H. A' (fuzzy:1)
- [PASS] initials: bio ['?'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1937, birth 1916 (age 21)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1939
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

