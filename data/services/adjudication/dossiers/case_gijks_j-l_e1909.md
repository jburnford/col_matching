<!-- {"case_id": "case_gijks_j-l_e1909", "bio_ids": ["gijks_j-l_e1909"], "stint_ids": ["Gilks, J. L___Kenya___1910"]} -->
# Dossier case_gijks_j-l_e1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `gijks_j-l_e1909` ↔ `Gilks, J. L___Kenya___1910` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Gilks, J. L___Kenya___1910` is also gate-compatible with biography(ies) outside this case: ['gilks_j-l_e1904'] (already linked elsewhere or filtered).

## Biography `gijks_j-l_e1909`

- Printed name: **GIJKS, J. L**
- Birth year: not printed
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L64708.v` — printed in editions [1930]:**

> GIJKS, J. L., M.R.C.S. (Eng.), L.R.C.P. (Lond.), F.R.C.S. (Edin.).—Medical offr., E.A.F., Aug., 1909; prin. med. offr., Kenya, Feb., 1921; mem., exec. and leg. councils; dir. med. and san'y services, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | Medical offr., E.A.F | — | [1930] |
| 1 | 1921 | prin. med. offr. | Kenya | [1930] |
| 2 | 1926 | dir. med. and san'y services | Kenya *(inherited from previous clause)* | [1930] |

## Candidate stint `Gilks, J. L___Kenya___1910`

- Staff-list name: **Gilks, J. L** | colony: **Kenya** | listed 1910–1925 | editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1919, 1920, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | J. L. Gilks | Temporary Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1911 | J. L. Gilks | Temporary Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1912 | J. L. Gilks | Temporary Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1913 | J. L. Gilks | Medical Officer | Medical | — | — |
| 1914 | J. L. Gilks | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1915 | J. L. Gilks | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1917 | J. L. Gilks | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1919 | J. L. Gilks | Medical Officers | Medical (East Africa and Uganda) | — | — |
| 1920 | J. L. Gilks | Medical Officers | Medical (East Africa and Uganda) | — | — |
| 1922 | J. L. Gilks | Principal Medical Officer | Medical | — | — |
| 1923 | J. L. Gilks | Principal Medical Officer | Medical | — | — |
| 1924 | J. L. Gilks | Principal Medical Officer | Medical | — | — |
| 1925 | J. L. Gilks | Principal Medical Officer | Medical Department | — | — |

### Deterministic checks: `gijks_j-l_e1909` vs `Gilks, J. L___Kenya___1910`

- [PASS] surname_gate: bio 'GIJKS' vs stint 'Gilks, J. L' (fuzzy:1)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1910-1925
- [PASS] position_sim: best 68 vs bar 60: 'prin. med. offr.' ~ 'Principal Medical Officer'
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

