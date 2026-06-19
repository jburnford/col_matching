<!-- {"case_id": "case_pinkeett_f-p_e1892", "bio_ids": ["pinkeett_f-p_e1892"], "stint_ids": ["Pinkett, F. P___Lagos___1898"]} -->
# Dossier case_pinkeett_f-p_e1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Pinkett, F. P___Lagos___1898` is also gate-compatible with biography(ies) outside this case: ['pinkett_f-p_e1892'] (already linked elsewhere or filtered).

## Biography `pinkeett_f-p_e1892`

- Printed name: **PINKEETT, F. P**
- Birth year: not printed
- Appears in editions: [1909]

### Verbatim printed entry text (OCR)

**Version `col1909-L49024.v` — printed in editions [1909]:**

> PINKEETT, F. P.—Solr., admitted 1892; 1st class elk., secretariat, Lagos, 1895; dist. consmr., 1897; trav. consmr., 1903; ag. prov. consmr. W. Prov.; mem. exec. and legis. couns., S. Nigeria, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | Solr., admitted | — | [1909] |
| 1 | 1895 | 1st class elk., secretariat | Lagos | [1909] |
| 2 | 1897 | dist. consmr | Lagos *(inherited from previous clause)* | [1909] |
| 3 | 1903 | trav. consmr | Lagos *(inherited from previous clause)* | [1909] |
| 4 | 1906 | mem. exec. and legis. couns. | Southern Nigeria | [1909] |

## Candidate stint `Pinkett, F. P___Lagos___1898`

- Staff-list name: **Pinkett, F. P** | colony: **Lagos** | listed 1898–1906 | editions [1898, 1899, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | F. P. Pinkett | District Commissioner | Supreme Court | — | — |
| 1899 | F. P. Pinkett | District Commissioner | Supreme Court | — | — |
| 1905 | F. P. Pinkett | Travelling Commissioners | Interior Department | — | — |
| 1906 | F. P. Pinkett | Travelling Commissioners | Interior Department | — | — |

### Deterministic checks: `pinkeett_f-p_e1892` vs `Pinkett, F. P___Lagos___1898`

- [PASS] surname_gate: bio 'PINKEETT' vs stint 'Pinkett, F. P' (fuzzy:1)
- [PASS] initials: bio ['F', 'P'] ~ stint ['F', 'P']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Lagos'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1898-1906
- [FAIL] position_sim: best 56 vs bar 60: 'dist. consmr' ~ 'District Commissioner'
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

