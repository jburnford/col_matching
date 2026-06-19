<!-- {"case_id": "case_eagar_geoffrey_e1872", "bio_ids": ["eagar_geoffrey_e1872"], "stint_ids": ["Eagar, Geoffrey___New South Wales___1877"]} -->
# Dossier case_eagar_geoffrey_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['eagar_geoffrey_e1872'] carry a single initial only — the namesake trap applies.

## Biography `eagar_geoffrey_e1872`

- Printed name: **EAGAR, GEOFFREY**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L33190.v` — printed in editions [1886, 1888, 1889, 1890]:**

> EAGAR, HON. GEOFFREY.—Under secretary to Treasury, New South Wales, 1 Feb., 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Under secretary to Treasury | New South Wales | [1886, 1888, 1889, 1890] |

## Candidate stint `Eagar, Geoffrey___New South Wales___1877`

- Staff-list name: **Eagar, Geoffrey** | colony: **New South Wales** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Geoffrey Eagar | Under-Secretary | The Treasury | — | — |
| 1877 | Geoffrey Eagar | Commissioner | Stamp Office | — | — |
| 1878 | Geoffrey Eagar | Commissioner | Stamp Office | — | — |
| 1878 | Geoffrey Eagar | Under-Secretary | The Treasury | — | — |
| 1879 | Geoffrey Eagar | Under-Secretary | The Treasury | — | — |
| 1880 | Hon. Geoffrey Eagar | Under-Secretary | The Treasury | — | — |
| 1886 | Geoffrey Eagar | Under-Secretary | The Treasury | — | — |
| 1888 | Geoffrey Eagar | Under-Secretary | The Treasury | — | — |
| 1889 | Geoffrey Eagar | Under-Secretary | The Treasury | — | — |

### Deterministic checks: `eagar_geoffrey_e1872` vs `Eagar, Geoffrey___New South Wales___1877`

- [PASS] surname_gate: bio 'EAGAR' vs stint 'Eagar, Geoffrey' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1889
- [FAIL] position_sim: best 44 vs bar 60: 'Under secretary to Treasury' ~ 'Under-Secretary'
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

