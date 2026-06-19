<!-- {"case_id": "case_woodlock_a_e1876-2", "bio_ids": ["woodlock_a_e1876-2"], "stint_ids": ["Woodlock, Arthur___Trinidad___1877"]} -->
# Dossier case_woodlock_a_e1876-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['woodlock_a_e1876-2'] carry a single initial only — the namesake trap applies.
- Phase 1 found `woodlock_a_e1876-2` ↔ `Woodlock, Arthur___Trinidad___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Woodlock, Arthur___Trinidad___1877` is also gate-compatible with biography(ies) outside this case: ['woodlock_a_e1876'] (already linked elsewhere or filtered).

## Biography `woodlock_a_e1876-2`

- Printed name: **WOODLOCK, A**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L36623.v` — printed in editions [1898]:**

> WOODLOCK, A.—Govt. med. offr., Trinidad, 1876; apptd. to Couva dist., 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Govt. med. offr. | Trinidad | [1898] |
| 1 | 1883 | apptd. to Couva dist | Trinidad *(inherited from previous clause)* | [1898] |

## Candidate stint `Woodlock, Arthur___Trinidad___1877`

- Staff-list name: **Woodlock, Arthur** | colony: **Trinidad** | listed 1877–1897 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. Woodlock | Government Medical Officer | Government Medical Officers | — | — |
| 1878 | Arthur Woodlock | Assistant-Surgeon | Medical Establishment | — | — |
| 1879 | Arthur Woodlock | Assistant-Surgeon, Colonial Hospital, Port of Spain | Medical Establishment | — | — |
| 1880 | Arthur Woodlock | Acting Resident Surgeon, San Fernando Hospital | Government Medical Officers | — | — |
| 1886 | A. Woodlock | District Medical Officer, Couva | Government Medical Officers | — | — |
| 1888 | A. Woodlock | Medical Visitor, Convict Dépôt | District Officers | — | — |
| 1889 | A. Woodlock | Medical Visitor, Convict Depot | District Officers | — | — |
| 1890 | A. Woodlock | Government Medical Officer | Government Medical Officers | — | — |
| 1894 | A. Woodlock | Government Medical Officer | Government Medical Officers | — | — |
| 1896 | A. Woodlock | Government Medical Officer | Government Medical Officers | — | — |
| 1897 | A. Woodlock | Police Surgeon | Government Medical Officers | — | — |

### Deterministic checks: `woodlock_a_e1876-2` vs `Woodlock, Arthur___Trinidad___1877`

- [PASS] surname_gate: bio 'WOODLOCK' vs stint 'Woodlock, Arthur' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1897
- [PASS] position_sim: best 67 vs bar 60: 'Govt. med. offr.' ~ 'Government Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

