<!-- {"case_id": "calib_gemini_natal_0259", "bio_ids": ["hunter_david_e1879"], "stint_ids": ["Hunter, D___Natal___1883"]} -->
# Dossier calib_gemini_natal_0259

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 129 official(s) with this surname in the graph's staff lists; 37 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hunter_david_e1879'] carry a single initial only — the namesake trap applies.

## Biography `hunter_david_e1879`

- Printed name: **HUNTER, DAVID**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L28092.v` — printed in editions [1883, 1886]:**

> HUNTER, DAVID.—General manager, Natal government railways, 27th September, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | General manager, Natal government railways | Natal | [1883, 1886] |

## Candidate stint `Hunter, D___Natal___1883`

- Staff-list name: **Hunter, D** | colony: **Natal** | listed 1883–1906 | editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | D. Hunter | General Manager | Natal Government Railways | — | — |
| 1886 | D. Hunter | General Manager | Natal Government Railways | — | — |
| 1888 | D. Hunter | General Manager | Natal Government Railways | — | — |
| 1889 | D. Hunter | General Manager | Natal Government Railways | — | — |
| 1890 | D. Hunter | General Manager | Natal Government Railways | — | — |
| 1894 | D. Hunter | General Manager | Natal Government Railways | — | — |
| 1896 | D. Hunter | General Manager | Railways | — | — |
| 1898 | D. Hunter | General Manager | Railways | — | — |
| 1899 | D. Hunter | General Manager | Railways | C.M.G. | — |
| 1900 | D. Hunter | General Manager | Railways | C.M.G. | — |
| 1905 | Sir D. Hunter | General Manager | Railways | K.C.M.G. | — |
| 1906 | Sir D. Hunter | General Manager | Railways | K.C.M.G. | — |

### Deterministic checks: `hunter_david_e1879` vs `Hunter, D___Natal___1883`

- [PASS] surname_gate: bio 'HUNTER' vs stint 'Hunter, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1906
- [PASS] position_sim: best 100 vs bar 60: 'General manager, Natal government railways' ~ 'General Manager'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1883, 1886] pos~100 (bar: >=2)
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

