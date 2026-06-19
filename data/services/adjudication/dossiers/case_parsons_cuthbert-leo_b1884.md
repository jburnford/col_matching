<!-- {"case_id": "case_parsons_cuthbert-leo_b1884", "bio_ids": ["parsons_cuthbert-leo_b1884"], "stint_ids": ["Parsons, C___Canada___1905"]} -->
# Dossier case_parsons_cuthbert-leo_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `parsons_cuthbert-leo_b1884`

- Printed name: **PARSONS, CUTHBERT LEO**
- Birth year: 1884 (attested in editions [1932, 1933, 1934])
- Honours: M.I.R.S.E
- Appears in editions: [1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1932-L63042.v` — printed in editions [1932, 1933, 1934]:**

> PARSONS, CUTHBERT LEO, M.I.R.S.E.—B. 1884; asst. signal and telegr. engrnr., sp. services, F.M.S. Rly., Sept., 1914; dist. signal engrnr., grade II; grade I, Sept., 1923; dist. signal and telegr. engrnr., grade I, Aug., 1928; ditto, F.M.S. Rly., std. to head office, K. Lumpur, June, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | asst. signal and telegr. engrnr., sp. services, F.M.S. Rly | Federated Malay States | [1932, 1933, 1934] |
| 1 | 1923 | grade I | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1934] |
| 2 | 1928 | dist. signal and telegr. engrnr., grade I | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1934] |
| 3 | 1930 | ditto, F.M.S. Rly., std. to head office, K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1934] |

## Candidate stint `Parsons, C___Canada___1905`

- Staff-list name: **Parsons, C** | colony: **Canada** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Sir C. Parsons | General Commanding His Majesty's Forces | Imperial Military Establishment | K.C.M.G. | — |
| 1906 | Sir C. Parsons | General Commanding His Majesty's Forces | Imperial Military Establishment (Halifax) | K.C.M.G. | — |

### Deterministic checks: `parsons_cuthbert-leo_b1884` vs `Parsons, C___Canada___1905`

- [PASS] surname_gate: bio 'PARSONS' vs stint 'Parsons, C' (exact)
- [PASS] initials: bio ['C', 'L'] ~ stint ['C']
- [PASS] age_gate: stint starts 1905, birth 1884 (age 21)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

