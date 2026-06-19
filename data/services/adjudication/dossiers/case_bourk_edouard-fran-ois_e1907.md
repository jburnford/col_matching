<!-- {"case_id": "case_bourk_edouard-fran-ois_e1907", "bio_ids": ["bourk_edouard-fran-ois_e1907"], "stint_ids": ["Bour, E. F___Mauritius___1913"]} -->
# Dossier case_bourk_edouard-fran-ois_e1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `bourk_edouard-fran-ois_e1907` ↔ `Bour, E. F___Mauritius___1913` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Bour, E. F___Mauritius___1913` is also gate-compatible with biography(ies) outside this case: ['bour_edouard-francois_e1907'] (already linked elsewhere or filtered).

## Biography `bourk_edouard-fran-ois_e1907`

- Printed name: **BOURK, Edouard François**
- Birth year: not printed
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L62675.v` — printed in editions [1931]:**

> BOURK, Edouard François.—M.R.C.S. Eng.; L.R.C.P. Lond.; I.S.A. Lond.; gov't med. off., Plaines Wilhelms dist., Mauritius, 1907; medical officer in charge H.M. troops, Mauritius, 1915-19.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | gov't med. off., Plaines Wilhelms dist. | Mauritius | [1931] |
| 1 | 1915–1919 | medical officer in charge H.M. troops | Mauritius | [1931] |

## Candidate stint `Bour, E. F___Mauritius___1913`

- Staff-list name: **Bour, E. F** | colony: **Mauritius** | listed 1913–1928 | editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | Dr. E. F. Bour | Government and Poor Law Medical Officer and Poor Law Guardian | Medical and Health Department | — | — |
| 1914 | E. F. Bour | Government and Poor Law Medical Officer | Medical and Health Department | — | — |
| 1915 | E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1917 | E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1918 | E. F. Bour | Civil Medical Practitioner | Military Officers | — | — |
| 1918 | E. F. Bour | Medical Officer | Medical and Health Department. | — | — |
| 1919 | E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1919 | E. F. Bour | Civil Medical Practitioner | Military Officers | — | — |
| 1920 | E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1920 | E. F. Bour | Civil Medical Practitioner | Military | — | — |
| 1920 | E. F. Bour | Civil Medical Practitioner | Military Officers | — | — |
| 1921 | Dr. E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1922 | E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1923 | E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1925 | E. F. Bour | Medical Officers | Medical and Health Department | — | — |
| 1927 | Dr. E. F. Bour | Medical Officer | Medical and Health Department | — | — |
| 1928 | E. F. Bour | Medical Officer | Medical and Health Department | — | — |

### Deterministic checks: `bourk_edouard-fran-ois_e1907` vs `Bour, E. F___Mauritius___1913`

- [PASS] surname_gate: bio 'BOURK' vs stint 'Bour, E. F' (fuzzy:1)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1913-1928
- [PASS] position_sim: best 100 vs bar 60: 'medical officer in charge H.M. troops' ~ 'Medical Officer'
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

