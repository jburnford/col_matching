<!-- {"case_id": "case_gaunson_x_e1881", "bio_ids": ["gaunson_x_e1881"], "stint_ids": ["Gaunson, B___Victoria___1880"]} -->
# Dossier case_gaunson_x_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gaunson_x_e1881'] carry a single initial only — the namesake trap applies.

## Biography `gaunson_x_e1881`

- Printed name: **GAUNSON, (no given names printed)**
- Birth year: not printed
- Terminal: resigned 1883 — “resigned, 1883.”
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L27612.v` — printed in editions [1883, 1886]:**

> GAUNSON, HON.—Commissioner of lands and survey, Victoria, 9th July, 1881; resigned, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Commissioner of lands and survey | Victoria | [1883, 1886] |

## Candidate stint `Gaunson, B___Victoria___1880`

- Staff-list name: **Gaunson, B** | colony: **Victoria** | listed 1880–1883 | editions [1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | B. Gaunson | Secretary | Land Tax Commission | — | — |
| 1883 | B. Gaunson | Secretary | Land Tax Commission | — | — |

### Deterministic checks: `gaunson_x_e1881` vs `Gaunson, B___Victoria___1880`

- [PASS] surname_gate: bio 'GAUNSON' vs stint 'Gaunson, B' (exact)
- [PASS] initials: bio ['?'] ~ stint ['B']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1883
- [FAIL] position_sim: best 29 vs bar 60: 'Commissioner of lands and survey' ~ 'Secretary'
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

