<!-- {"case_id": "case_kettle_james-david_b1879", "bio_ids": ["kettle_james-david_b1879"], "stint_ids": ["Kettle, James David___Trinidad and Tobago___1925"]} -->
# Dossier case_kettle_james-david_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kettle_james-david_b1879`

- Printed name: **KETTLE, JAMES DAVID**
- Birth year: 1879 (attested in editions [1925, 1927])
- Honours: F.C.S, F.I.C
- Appears in editions: [1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1925-L57031.v` — printed in editions [1925, 1927]:**

> KETTLE, JAMES DAVID, B.So. (Lond.), F.I.C., F.C.S.—B. 1879; asst. govt. analyst, Trinidad, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | asst. govt. analyst | Trinidad | [1925, 1927] |

## Candidate stint `Kettle, James David___Trinidad and Tobago___1925`

- Staff-list name: **Kettle, James David** | colony: **Trinidad and Tobago** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | James David Kettle | Assistant Government Analyst | Analyst's Department | — | — |
| 1927 | James David Kettle | Assistant Government Analyst | Analyst's Department | — | — |

### Deterministic checks: `kettle_james-david_b1879` vs `Kettle, James David___Trinidad and Tobago___1925`

- [PASS] surname_gate: bio 'KETTLE' vs stint 'Kettle, James David' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1925, birth 1879 (age 46)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

