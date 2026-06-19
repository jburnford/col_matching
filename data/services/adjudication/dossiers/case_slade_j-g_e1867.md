<!-- {"case_id": "case_slade_j-g_e1867", "bio_ids": ["slade_j-g_e1867"], "stint_ids": ["Slade, J. G___Western Australia___1877"]} -->
# Dossier case_slade_j-g_e1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `slade_j-g_e1867`

- Printed name: **SLADE, J. G**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L29513.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> SLADE, J. G.—Colonial secretary, Labuan, September, 1867; resident magistrate, Fremantle, W. Australia, Sept. 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | Colonial secretary | Labuan | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1868 | resident magistrate, Fremantle, W. Australia | Labuan *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Slade, J. G___Western Australia___1877`

- Staff-list name: **Slade, J. G** | colony: **Western Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. G. Slade | Resident Magistrate | Judicial Establishment | — | — |
| 1878 | J. G. Slade | Resident Magistrate | Judicial Establishment | — | — |
| 1879 | J. G. Slade | Resident Magistrate, Fremantle District | Judicial Department | — | — |
| 1880 | J. G. Slade | Resident Magistrate | Judicial Department | — | — |

### Deterministic checks: `slade_j-g_e1867` vs `Slade, J. G___Western Australia___1877`

- [PASS] surname_gate: bio 'SLADE' vs stint 'Slade, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

