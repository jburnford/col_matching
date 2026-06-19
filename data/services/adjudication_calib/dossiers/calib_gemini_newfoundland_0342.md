<!-- {"case_id": "calib_gemini_newfoundland_0342", "bio_ids": ["halfyard_w-w_e1918"], "stint_ids": ["Halfyard, W. W___Newfoundland___1917"]} -->
# Dossier calib_gemini_newfoundland_0342

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `halfyard_w-w_e1918`

- Printed name: **HALFYARD, W. W**
- Birth year: not printed
- Appears in editions: [1918]

### Verbatim printed entry text (OCR)

**Version `col1918-L51062.v` — printed in editions [1918]:**

> HALFYARD, HON. W. W.—Col. sec., Newfoundland, Jan., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | Col. sec. | Newfoundland | [1918] |

## Candidate stint `Halfyard, W. W___Newfoundland___1917`

- Staff-list name: **Halfyard, W. W** | colony: **Newfoundland** | listed 1917–1927 | editions [1917, 1918, 1919, 1921, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | W. W. Halfyard | Member for Placentia | House of Assembly | — | — |
| 1918 | Hon. W. W. Halfyard | Colonial Secretary | Colonial Secretary's Department | — | — |
| 1919 | W. W. Halfyard | Colonial Secretary | Colonial Secretary's Department | — | — |
| 1921 | W. W. Halfyard | Minister of Posts and Telegraphs | Department of Posts and Telegraphs | — | — |
| 1921 | W. Halfyard | 3rd Clerk | Colonial Secretary's Department | — | — |
| 1927 | W. Halfyard | 2nd Clerk and Accountant | Colonial Secretary's Department | — | — |

### Deterministic checks: `halfyard_w-w_e1918` vs `Halfyard, W. W___Newfoundland___1917`

- [PASS] surname_gate: bio 'HALFYARD' vs stint 'Halfyard, W. W' (exact)
- [PASS] initials: bio ['W', 'W'] ~ stint ['W', 'W']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1917-1927
- [PASS] position_sim: best 100 vs bar 60: 'Col. sec.' ~ 'Colonial Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1918] pos~100 (bar: >=2)
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

