<!-- {"case_id": "case_chitty_edward-charles_b1896", "bio_ids": ["chitty_edward-charles_b1896"], "stint_ids": ["Chitty, E. C___Straits Settlements___1931"]} -->
# Dossier case_chitty_edward-charles_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chitty_edward-charles_b1896`

- Printed name: **CHITTY, Edward Charles**
- Birth year: 1896 (attested in editions [1940])
- Honours: M.B, M.C
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63110.v` — printed in editions [1940]:**

> CHITTY, Edward Charles, M.C., M.B., Ch. B. (Aberdeen), F.R.C.S. (Edin.).—B. 1896; med. offr., F.M.S., Mar., 1926; ag. prof., clin. surgery., S'pore, Apr., 1932; surg., grade B., Sept., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | med. offr. | Federated Malay States | [1940] |
| 1 | 1932 | ag. prof., clin. surgery., S'pore | Federated Malay States *(inherited from previous clause)* | [1940] |
| 2 | 1936 | surg., grade B | Federated Malay States *(inherited from previous clause)* | [1940] |

## Candidate stint `Chitty, E. C___Straits Settlements___1931`

- Staff-list name: **Chitty, E. C** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E. C. Chitty | Medical Officer | Medical | — | — |
| 1932 | E. C. Chitty | Medical Officer | Medical | — | — |
| 1933 | E. C. Chitty | Medical Officer | Medical | M.C. | — |

### Deterministic checks: `chitty_edward-charles_b1896` vs `Chitty, E. C___Straits Settlements___1931`

- [PASS] surname_gate: bio 'CHITTY' vs stint 'Chitty, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1931, birth 1896 (age 35)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.C
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

