<!-- {"case_id": "case_townssend_wm-richard_e1894", "bio_ids": ["townssend_wm-richard_e1894"], "stint_ids": ["Townsend, W. R___Gambia___1905"]} -->
# Dossier case_townssend_wm-richard_e1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `townssend_wm-richard_e1894` ↔ `Townsend, W. R___Gambia___1905` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Townsend, W. R___Gambia___1905` is also gate-compatible with biography(ies) outside this case: ['townsend_wm-richard_e1894'] (already linked elsewhere or filtered).

## Biography `townssend_wm-richard_e1894`

- Printed name: **TOWNSSEND, WM. RICHARD**
- Birth year: not printed
- Appears in editions: [1908]

### Verbatim printed entry text (OCR)

**Version `col1908-L47894.v` — printed in editions [1908]:**

> TOWNSSEND, WM. RICHARD.—B.A., Dublin Univ., 1894; called to the bar, Ireland, 1894; atty.-gen., Gambia, 1st May, 1902; inspr. of schla., col. regisr. and mem. of exec. and legis. couns. during tenure of atty.-generalship; ch. mag. and M.L.C., Gambia, 6th Nov., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | B.A., Dublin Univ | — | [1908] |
| 1 | 1894 | called to the bar, Ireland | — | [1908] |
| 2 | 1902 | atty.-gen. | Gambia | [1908] |
| 3 | 1906 | ch. mag. and M.L.C. | Gambia | [1908] |

## Candidate stint `Townsend, W. R___Gambia___1905`

- Staff-list name: **Townsend, W. R** | colony: **Gambia** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. R. Townsend | Attorney-General | Attorney-General's Office | — | — |
| 1906 | W. R. Townsend | Attorney-General | Attorney-General's Office | — | — |
| 1907 | Hon. W. R. Townsend | Chief Magistrate | Judicial Department | — | — |
| 1908 | Hon. W. R. Townsend | Chief Magistrate | Judicial Department | — | — |
| 1909 | W. R. Townsend | Chief Magistrate | Judicial Department | — | — |

### Deterministic checks: `townssend_wm-richard_e1894` vs `Townsend, W. R___Gambia___1905`

- [PASS] surname_gate: bio 'TOWNSSEND' vs stint 'Townsend, W. R' (fuzzy:1)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Gambia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1905-1909
- [PASS] position_sim: best 64 vs bar 60: 'atty.-gen.' ~ 'Attorney-General'
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

