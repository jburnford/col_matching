<!-- {"case_id": "case_evles_c-h_e1887", "bio_ids": ["evles_c-h_e1887", "eylfs_c-h_e1883"], "stint_ids": ["Eyles, C. H___British Honduras___1888"]} -->
# Dossier case_evles_c-h_e1887

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Eyles, C. H___British Honduras___1888'] have more than one claimant biography in this case.
- Phase 1 found `evles_c-h_e1887` ↔ `Eyles, C. H___British Honduras___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Eyles, C. H___British Honduras___1888` is also gate-compatible with biography(ies) outside this case: ['eyles_c-h_e1883'] (already linked elsewhere or filtered).
- NOTE: stint `Eyles, C. H___British Honduras___1888` is also gate-compatible with biography(ies) outside this case: ['eyles_c-h_e1883'] (already linked elsewhere or filtered).

## Biography `evles_c-h_e1887`

- Printed name: **EVLES, C. H**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L33319.v` — printed in editions [1888]:**

> EVLES, C. H.—Assistant colonial surgeon, Gold Coast Colony, 1888; colonial surgeon, British Honduras, 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887 | colonial surgeon | British Honduras | [1888] |
| 1 | 1888 | Assistant colonial surgeon | Gold Coast | [1888] |

## Biography `eylfs_c-h_e1883`

- Printed name: **EYLFS, C. H**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L31447.v` — printed in editions [1894]:**

> EYLFS, C. H.—Assistant colonial surgeon, Gold Coast Colony, 1883; colonial surgeon British Honduras, 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Assistant colonial surgeon | Gold Coast | [1894] |
| 1 | 1887 | colonial surgeon British Honduras | Gold Coast *(inherited from previous clause)* | [1894] |

## Candidate stint `Eyles, C. H___British Honduras___1888`

- Staff-list name: **Eyles, C. H** | colony: **British Honduras** | listed 1888–1906 | editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1889 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1890 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1894 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1896 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1897 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1898 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1899 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1900 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1905 | C. H. Eyles | Colonial Surgeon | Medical | — | — |
| 1906 | C. H. Eyles | Colonial Surgeon | Medical | — | — |

### Deterministic checks: `evles_c-h_e1887` vs `Eyles, C. H___British Honduras___1888`

- [PASS] surname_gate: bio 'EVLES' vs stint 'Eyles, C. H' (fuzzy:1)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1906
- [PASS] position_sim: best 100 vs bar 60: 'colonial surgeon' ~ 'Colonial Surgeon'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `eylfs_c-h_e1883` vs `Eyles, C. H___British Honduras___1888`

- [PASS] surname_gate: bio 'EYLFS' vs stint 'Eyles, C. H' (fuzzy:1)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1906
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

