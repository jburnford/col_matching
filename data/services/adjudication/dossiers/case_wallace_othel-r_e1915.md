<!-- {"case_id": "case_wallace_othel-r_e1915", "bio_ids": ["wallace_othel-r_e1915"], "stint_ids": ["Wallace, R___Victoria___1894"]} -->
# Dossier case_wallace_othel-r_e1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wallace, R___Victoria___1894` is also gate-compatible with biography(ies) outside this case: ['wallace_cyril-r_e1916'] (already linked elsewhere or filtered).

## Biography `wallace_othel-r_e1915`

- Printed name: **WALLACE, OTHEL R**
- Birth year: not printed
- Honours: L.R.C.P, L.R.C.S
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L64783.v` — printed in editions [1932]:**

> WALLACE, OTHEL R., L.R.C.P., L.R.C.S., L.M. (Ireland).—Ed. Trinity Coll., Dublin; capt., R.A.M.C. (T.F.), 1915-18; medical officer, Tanganyika Territory, June, 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | capt., R.A.M.C. (T.F.) | — | [1932] |
| 1 | 1918 | medical officer, Tanganyika Territory | Tanganyika | [1932] |

## Candidate stint `Wallace, R___Victoria___1894`

- Staff-list name: **Wallace, R** | colony: **Victoria** | listed 1894–1900 | editions [1894, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | R. Wallace | Captain | Victorian Artillery | — | — |
| 1897 | R. Wallace | Captain | Military Forces | — | Captain |
| 1898 | R. Wallace | Captain | Victorian Artillery | — | Captain |
| 1899 | R. Wallace | Major | MILITARY FORCES | — | Major |
| 1900 | R. Wallace | Major | Victorian Permanent Artillery | — | Major |

### Deterministic checks: `wallace_othel-r_e1915` vs `Wallace, R___Victoria___1894`

- [PASS] surname_gate: bio 'WALLACE' vs stint 'Wallace, R' (exact)
- [PASS] initials: bio ['O', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
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

