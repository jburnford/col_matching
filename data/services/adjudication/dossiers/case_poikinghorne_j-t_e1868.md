<!-- {"case_id": "case_poikinghorne_j-t_e1868", "bio_ids": ["poikinghorne_j-t_e1868"], "stint_ids": ["Polkinghorne, J. T___Natal___1880"]} -->
# Dossier case_poikinghorne_j-t_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Polkinghorne, J. T___Natal___1880` is also gate-compatible with biography(ies) outside this case: ['polkinghorne_j-t_e1868'] (already linked elsewhere or filtered).

## Biography `poikinghorne_j-t_e1868`

- Printed name: **POIKINGHORNE, J. T**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L35451.v` — printed in editions [1898]:**

> POIKINGHORNE, Hon. J. T.—Mem. legis. coun., Natal, 1868 to 1879; of the exec. coun. from 1872; col. treas., 1879-93; is J.P.; pres. of legis. coun. on introduction of responsible govt., 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868–1879 | Mem. legis. coun. | Natal | [1898] |
| 1 | 1872 | of the exec. coun. from | Natal *(inherited from previous clause)* | [1898] |
| 2 | 1879–1893 | col. treas | Natal *(inherited from previous clause)* | [1898] |
| 3 | 1893 | pres. of legis. coun. on introduction of responsible govt | Natal *(inherited from previous clause)* | [1898] |

## Candidate stint `Polkinghorne, J. T___Natal___1880`

- Staff-list name: **Polkinghorne, J. T** | colony: **Natal** | listed 1880–1894 | editions [1880, 1883, 1886, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | J. T. Polkinghorne | Treasurer | Treasury Department | — | — |
| 1883 | J. T. Polkinghorne | Treasurer | Treasury Office | — | — |
| 1886 | J. T. Polkinghorne | Treasurer | Treasury Office | — | — |
| 1888 | J. T. Polkinghorne | Treasurer | Treasury Office | — | — |
| 1889 | J. T. Polkinghorne | Treasurer | Treasury Office | — | — |
| 1890 | J. T. Polkinghorne | Treasurer | Treasury Office | — | — |
| 1894 | The Hon. J. T. Polkinghorne | President | Legislative Council Office | — | — |

### Deterministic checks: `poikinghorne_j-t_e1868` vs `Polkinghorne, J. T___Natal___1880`

- [PASS] surname_gate: bio 'POIKINGHORNE' vs stint 'Polkinghorne, J. T' (fuzzy:1)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1880-1894
- [FAIL] position_sim: best 56 vs bar 60: 'col. treas' ~ 'Treasurer'
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

