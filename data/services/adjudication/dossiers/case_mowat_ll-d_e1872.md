<!-- {"case_id": "case_mowat_ll-d_e1872", "bio_ids": ["mowat_ll-d_e1872"], "stint_ids": ["Mowat, D___Canada___1896"]} -->
# Dossier case_mowat_ll-d_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mowat_ll-d_e1872`

- Printed name: **MOWAT, LL.D**
- Birth year: not printed
- Honours: Sir OLIVER K.C.M.G (1892)
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L33488.v` — printed in editions [1897]:**

> MOWAT, Sir OLIVER K.C.M.G. (1892), LL.D., Q.C.—Attorney-general and premier, Ontario, 25th Oct., 1872; senator and minister of justice (Canada), June, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Attorney-general and premier | Ontario | [1897] |
| 1 | 1896 | senator and minister of justice (Canada) | Ontario *(inherited from previous clause)* | [1897] |

## Candidate stint `Mowat, D___Canada___1896`

- Staff-list name: **Mowat, D** | colony: **Canada** | listed 1896–1899 | editions [1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | D. Mowat | Member | North West Territories Legislative Assembly | — | — |
| 1897 | D. Mowat | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1898 | D. Mowat | Member of Legislative Assembly | Legislative Assembly | — | — |
| 1899 | D. Mowat | Member of Legislative Assembly | Legislative Assembly | — | — |

### Deterministic checks: `mowat_ll-d_e1872` vs `Mowat, D___Canada___1896`

- [PASS] surname_gate: bio 'MOWAT' vs stint 'Mowat, D' (exact)
- [PASS] initials: bio ['L', 'D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1896-1899
- [FAIL] position_sim: best 41 vs bar 60: 'senator and minister of justice (Canada)' ~ 'Member of Legislative Assembly'
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

