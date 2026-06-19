<!-- {"case_id": "case_wier_r-s_e1871", "bio_ids": ["wier_r-s_e1871"], "stint_ids": ["Wier, R. S___British Honduras___1878"]} -->
# Dossier case_wier_r-s_e1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wier, R. S___British Honduras___1878` is also gate-compatible with biography(ies) outside this case: ['wier_r-s_e1874'] (already linked elsewhere or filtered).

## Biography `wier_r-s_e1871`

- Printed name: **WIER, R. S.**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L36682.v` — printed in editions [1888]:**

> WIER, R. S.-Chief clerk , customs department, and copyist, secretariat, Lagos, Dec. , 1871 ; clerk and keeper of debtors prison, June, 1875 2 ; nd

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Chief clerk, customs department, and copyist, secretariat | Lagos | [1888] |
| 1 | 1875 | clerk and keeper of debtors prison | — | [1888] |

## Candidate stint `Wier, R. S___British Honduras___1878`

- Staff-list name: **Wier, R. S** | colony: **British Honduras** | listed 1878–1888 | editions [1878, 1879, 1880, 1883, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | R. S. Wier | Clerk in Treasury | Customs | — | — |
| 1879 | R. S. Wier | Clerk in Treasury | Customs | — | — |
| 1880 | R. S. Wier | Chief Clerk | Customs | — | — |
| 1883 | R. S. Wier | Chief Clerk | Customs | — | — |
| 1888 | R. S. Wier | Chief Clerk | Treasury and Customs Department, &c. | — | — |

### Deterministic checks: `wier_r-s_e1871` vs `Wier, R. S___British Honduras___1878`

- [PASS] surname_gate: bio 'WIER' vs stint 'Wier, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1888
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

