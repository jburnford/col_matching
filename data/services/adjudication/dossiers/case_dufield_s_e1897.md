<!-- {"case_id": "case_dufield_s_e1897", "bio_ids": ["dufield_s_e1897"], "stint_ids": ["Duffield, S___Orange River Colony___1905"]} -->
# Dossier case_dufield_s_e1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dufield_s_e1897'] carry a single initial only — the namesake trap applies.
- Phase 1 found `dufield_s_e1897` ↔ `Duffield, S___Orange River Colony___1905` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Duffield, S___Orange River Colony___1905` is also gate-compatible with biography(ies) outside this case: ['duffield_s_e1897'] (already linked elsewhere or filtered).

## Biography `dufield_s_e1897`

- Printed name: **DUFIELD, S.**
- Birth year: not printed
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L45459.v` — printed in editions [1910]:**

> DUFIELD, S.—Clk. to accontg. offr., Cape govt. rlys., 1897; bkpr. to ch. acctnt., O.F.S. (afterwards Imp. military) rlys., Oct., 1897, to 11th June, 1900; 1st clk. and bkpr. to orphan master, O.R.C., 11th June, 1900, to 1st Apr., 1903; asst. mast. of High Ct., O.R.C., 1st Apr., 1903; ag. mast. of High Ct., Jan. to June, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897–1897 | Clk. to accontg. offr. | Cape Colony | [1910] |
| 1 | 1897–1900 | bkpr. to ch. acctnt. | Orange Free State | [1910] |
| 2 | 1900–1903 | 1st clk. and bkpr. to orphan master | Orange River Colony | [1910] |
| 3 | 1903 | asst. mast. of High Ct. | Orange River Colony | [1910] |
| 4 | 1906–1906 | ag. mast. of High Ct. | — | [1910] |

## Candidate stint `Duffield, S___Orange River Colony___1905`

- Staff-list name: **Duffield, S** | colony: **Orange River Colony** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | S. Duffield | Assistant Master of the High Court | Department of the Master of the High Court | — | — |
| 1906 | S. Duffield | Assistant Master | Administration of Justice | — | — |
| 1907 | S. Duffield | Assistant Master | Administration of Justice | — | — |
| 1908 | S. Duffield | Assistant Master | Administration of Justice | — | — |
| 1909 | S. Duffield | Assistant Master | — | — | — |

### Deterministic checks: `dufield_s_e1897` vs `Duffield, S___Orange River Colony___1905`

- [PASS] surname_gate: bio 'DUFIELD' vs stint 'Duffield, S' (fuzzy:1)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Orange River Colony'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1909
- [PASS] position_sim: best 74 vs bar 60: 'asst. mast. of High Ct.' ~ 'Assistant Master of the High Court'
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

