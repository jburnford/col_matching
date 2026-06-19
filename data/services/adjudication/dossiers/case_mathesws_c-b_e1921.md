<!-- {"case_id": "case_mathesws_c-b_e1921", "bio_ids": ["mathesws_c-b_e1921"], "stint_ids": ["Mathew, C___Uganda___1937"]} -->
# Dossier case_mathesws_c-b_e1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Mathew, C___Uganda___1937` is also gate-compatible with biography(ies) outside this case: ['mathew_charles_b1903'] (already linked elsewhere or filtered).

## Biography `mathesws_c-b_e1921`

- Printed name: **MATHESWS, C. B**
- Birth year: not printed
- Appears in editions: [1924]

### Verbatim printed entry text (OCR)

**Version `col1924-L56450.v` — printed in editions [1924]:**

> MATHESWS, C. B.—Ast. dist. commr., Kenya, Feb., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Ast. dist. commr. | Kenya | [1924] |

## Candidate stint `Mathew, C___Uganda___1937`

- Staff-list name: **Mathew, C** | colony: **Uganda** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | C. Mathew | Crown Counsel | Crown Law Office | — | — |
| 1939 | C. Mathew | Judicial Adviser | Provincial Administration | — | — |
| 1940 | C. Mathew | Judicial Adviser, Buganda | Provincial Administration | — | — |

### Deterministic checks: `mathesws_c-b_e1921` vs `Mathew, C___Uganda___1937`

- [PASS] surname_gate: bio 'MATHESWS' vs stint 'Mathew, C' (fuzzy:2)
- [PASS] initials: bio ['C', 'B'] ~ stint ['C']
- [PASS] age_gate: stint starts 1937; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
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

