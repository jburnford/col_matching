<!-- {"case_id": "case_marston_s_e1917", "bio_ids": ["marston_s_e1917"], "stint_ids": ["Marston, S___Uganda___1927"]} -->
# Dossier case_marston_s_e1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['marston_s_e1917'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Marston, S___Uganda___1927` is also gate-compatible with biography(ies) outside this case: ['marston_s_e1917-2'] (already linked elsewhere or filtered).

## Biography `marston_s_e1917`

- Printed name: **MARSTON, S**
- Birth year: not printed
- Appears in editions: [1918, 1919, 1920, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1918-L52621.v` — printed in editions [1918, 1919, 1920, 1923, 1924]:**

> MARSTON, S.—Treasy. astt., E.A.P., Jan., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | Treasy. astt. | East Africa Protectorate | [1918, 1919, 1920, 1923, 1924] |

## Candidate stint `Marston, S___Uganda___1927`

- Staff-list name: **Marston, S** | colony: **Uganda** | listed 1927–1933 | editions [1927, 1928, 1929, 1930, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | S. Marston | Deputy Treasurer | Treasury and Savings Bank | — | — |
| 1928 | S. Marston | Deputy Treasurer | Treasury and Savings Bank | — | — |
| 1929 | S. Marston | Deputy Treasurer | Treasury and Savings Bank | — | — |
| 1930 | S. Marston | Deputy Treasurer | Treasury and Savings Bank | — | — |
| 1933 | S. Marston | Treasurer and Controller of Savings Bank | Treasury and Savings Bank | — | — |

### Deterministic checks: `marston_s_e1917` vs `Marston, S___Uganda___1927`

- [PASS] surname_gate: bio 'MARSTON' vs stint 'Marston, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1933
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

