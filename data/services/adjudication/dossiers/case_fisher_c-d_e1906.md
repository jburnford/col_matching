<!-- {"case_id": "case_fisher_c-d_e1906", "bio_ids": ["fisher_c-d_e1906"], "stint_ids": ["Fisher, D___South Australia___1877"]} -->
# Dossier case_fisher_c-d_e1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 79 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fisher_c-d_e1906`

- Printed name: **FISHER, C. D**
- Birth year: not printed
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L45723.v` — printed in editions [1910]:**

> FISHER, C. D.—Asst. dist. comsnr., E.A.P., 8th Dec., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | Asst. dist. comsnr. | East Africa Protectorate | [1910] |

## Candidate stint `Fisher, D___South Australia___1877`

- Staff-list name: **Fisher, D** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | D. Fisher, jun. | Clerk | Audit Department | — | — |
| 1878 | D. Fisher, jun. | Clerk | Registrar-General of Births, Deaths, and Marriages | — | — |
| 1879 | D. Fisher, jun. | Clerk | Registrar-General of Births, Deaths, and Marriages | — | — |
| 1880 | D. Fisher, jun. | Clerk | Registrar-General of Births, Deaths, and Marriages | — | — |

### Deterministic checks: `fisher_c-d_e1906` vs `Fisher, D___South Australia___1877`

- [PASS] surname_gate: bio 'FISHER' vs stint 'Fisher, D' (exact)
- [PASS] initials: bio ['C', 'D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

