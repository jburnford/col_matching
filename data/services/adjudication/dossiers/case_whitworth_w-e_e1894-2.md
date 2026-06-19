<!-- {"case_id": "case_whitworth_w-e_e1894-2", "bio_ids": ["whitworth_w-e_e1894-2"], "stint_ids": ["Whitworth, E___Cape of Good Hope___1906"]} -->
# Dossier case_whitworth_w-e_e1894-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whitworth_w-e_e1894-2`

- Printed name: **WHITWORTH, W. E**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L36508.v` — printed in editions [1898]:**

> WHITWORTH, W. E.—Apptd., after compet. exam., ck. of the 2nd div. civ. ser., and assigned to C.O., Feb. 19th, 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | Apptd., after compet. exam., ck. of the 2nd div. civ. ser., and assigned to C.O., Feb. 19th | Colonial Office | [1898] |

## Candidate stint `Whitworth, E___Cape of Good Hope___1906`

- Staff-list name: **Whitworth, E** | colony: **Cape of Good Hope** | listed 1906–1909 | editions [1906, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | E. Whitworth | Second Class Clerk | Treasury | — | — |
| 1907 | E. Whitworth | Second Class Clerks | Treasury | — | — |
| 1909 | E. Whitworth | Examiners | Control and Audit Office | — | — |

### Deterministic checks: `whitworth_w-e_e1894-2` vs `Whitworth, E___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'WHITWORTH' vs stint 'Whitworth, E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1909
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

