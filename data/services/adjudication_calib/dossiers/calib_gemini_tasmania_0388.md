<!-- {"case_id": "calib_gemini_tasmania_0388", "bio_ids": ["henry_r_e1878"], "stint_ids": ["Henry, Robert___Tasmania___1888"]} -->
# Dossier calib_gemini_tasmania_0388

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 74 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['henry_r_e1878'] carry a single initial only — the namesake trap applies.

## Biography `henry_r_e1878`

- Printed name: **HENRY, R**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34010.v` — printed in editions [1886]:**

> HENRY, R.—Superintendent of telegraphs, Tasmania, 1 July, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Superintendent of telegraphs | Tasmania | [1886] |

## Candidate stint `Henry, Robert___Tasmania___1888`

- Staff-list name: **Henry, Robert** | colony: **Tasmania** | listed 1888–1894 | editions [1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Robert Henry | Superintendent of Telegraphs | Electric Telegraph, Hobart | — | — |
| 1889 | Robert Henry | Superintendent of Telegraphs | Electric Telegraph | — | — |
| 1894 | Robert Henry | Superintendent of Telegraphs | Electric Telegraph | — | — |

### Deterministic checks: `henry_r_e1878` vs `Henry, Robert___Tasmania___1888`

- [PASS] surname_gate: bio 'HENRY' vs stint 'Henry, Robert' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1894
- [PASS] position_sim: best 100 vs bar 60: 'Superintendent of telegraphs' ~ 'Superintendent of Telegraphs'
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

