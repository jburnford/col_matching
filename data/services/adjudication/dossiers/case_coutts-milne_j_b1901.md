<!-- {"case_id": "case_coutts-milne_j_b1901", "bio_ids": ["coutts-milne_j_b1901"], "stint_ids": ["Coutts-Milne, J___Singapore___1949"]} -->
# Dossier case_coutts-milne_j_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['coutts-milne_j_b1901'] carry a single initial only — the namesake trap applies.

## Biography `coutts-milne_j_b1901`

- Printed name: **COUTTS-MILNE, J**
- Birth year: 1901 (attested in editions [1953])
- Appears in editions: [1953]

### Verbatim printed entry text (OCR)

**Version `col1953-L16989.v` — printed in editions [1953]:**

> COUTTS-MILNE, J.—b. 1901; Robt. Gordon's Coll. and Aberdeen Univ.; health offr., F.M.S., 1928; Mal. med. serv., 1935; superscale, gr. B, 1946; gr. A, 1947; ch. health offr., S'pore, 1948; D.D.M.S., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | health offr. | Federated Malay States | [1953] |
| 1 | 1935 | Mal. med. serv | Malaya | [1953] |
| 2 | 1946 | superscale, gr. B | Malaya *(inherited from previous clause)* | [1953] |
| 3 | 1947 | gr. A | Malaya *(inherited from previous clause)* | [1953] |
| 4 | 1948 | ch. health offr., S'pore | Malaya *(inherited from previous clause)* | [1953] |

## Candidate stint `Coutts-Milne, J___Singapore___1949`

- Staff-list name: **Coutts-Milne, J** | colony: **Singapore** | listed 1949–1953 | editions [1949, 1951, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Coutts-Milne | Deputy Director of Medical Services | Medical | — | — |
| 1951 | J. Coutts-Milne | Deputy Director of Medical Services | MEDICAL | — | — |
| 1953 | J. Coutts-Milne | Deputy Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `coutts-milne_j_b1901` vs `Coutts-Milne, J___Singapore___1949`

- [PASS] surname_gate: bio 'COUTTS-MILNE' vs stint 'Coutts-Milne, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1953
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

