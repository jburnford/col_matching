<!-- {"case_id": "case_addon_e-n-c_e1857", "bio_ids": ["addon_e-n-c_e1857"], "stint_ids": ["Haddon, E. C___Uganda___1939"]} -->
# Dossier case_addon_e-n-c_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `addon_e-n-c_e1857`

- Printed name: **ADDON, E. N. C.**
- Birth year: not printed
- Honours: K.C.M.G.
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L30966.v` — printed in editions [1897]:**

> ADDON, THE HON. SIR E. N. C., K.C.M.G.—Assistant commissioner, Santhial Perahs, India, 1857; supdt. of excise, Oudh; in addition to this appointment, was inspector-general of registration and superintendent of statistics for several years, and during several months secretary to financial commissioner; retired, Mar., 1877, and settled in Tasmanian; elected M.P. for West Devon, 1879, and frequently four times elected for same district; leader of opposition, 1886; minister of lands and mines and minister of education in Fysh administration, Mar., 1887; also member of the Federal Council of Australasia; agent-gen. for Tasmania, 1893; premier of Tasmania, 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857 | Assistant commissioner | India | [1897] |
| 1 | 1877 | — | Tasmania | [1897] |
| 2 | 1879 | M.P. | — | [1897] |
| 3 | 1886 | leader of opposition | — | [1897] |
| 4 | 1887 | minister of lands and mines and minister of education | — | [1897] |
| 5 | 1893 | agent-gen. | Tasmania | [1897] |
| 6 | 1894 | premier | Tasmania | [1897] |
| 7 | ? | supdt. of excise | Oudh | [1897] |

## Candidate stint `Haddon, E. C___Uganda___1939`

- Staff-list name: **Haddon, E. C** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | E. C. Haddon | Analytical Chemist | Medical | — | — |
| 1940 | E. C. Haddon | Government Chemist | Medical | — | — |

### Deterministic checks: `addon_e-n-c_e1857` vs `Haddon, E. C___Uganda___1939`

- [PASS] surname_gate: bio 'ADDON' vs stint 'Haddon, E. C' (fuzzy:1)
- [PASS] initials: bio ['E', 'N', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1939; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

