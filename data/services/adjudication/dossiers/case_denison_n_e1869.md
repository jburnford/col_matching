<!-- {"case_id": "case_denison_n_e1869", "bio_ids": ["denison_n_e1869"], "stint_ids": ["Denison, N___Straits Settlements___1888"]} -->
# Dossier case_denison_n_e1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['denison_n_e1869'] carry a single initial only — the namesake trap applies.

## Biography `denison_n_e1869`

- Printed name: **DENISON, N**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33024.v` — printed in editions [1888, 1889, 1890]:**

> DENISON, N.—Assistant to resident, Sarawak, Feb., 1869; magistrate and collector, Upper Sarawak, 1870, and assistant resident, 1871; post and shipping master, and commissioner, court of requests, Mar., 1872; clerk to general council of state, 1873; secretary to resident, Perak, Oct., 1876; collector and magistrate, Krian, May, 1877; superintendent, Lower Perak, July, 1881; J.P. for Straits Settlements, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Assistant to resident | Sarawak | [1888, 1889, 1890] |
| 1 | 1870 | magistrate and collector, Upper Sarawak | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1871 | assistant resident | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |
| 3 | 1872 | post and shipping master, and commissioner, court of requests | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |
| 4 | 1873 | clerk to general council of state | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |
| 5 | 1876 | secretary to resident, Perak | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |
| 6 | 1877 | collector and magistrate, Krian | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |
| 7 | 1881 | superintendent, Lower Perak | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |
| 8 | 1882 | J.P. for Straits Settlements | Sarawak *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Denison, N___Straits Settlements___1888`

- Staff-list name: **Denison, N** | colony: **Straits Settlements** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | N. Denison | Superintendent of Lower Perak | Perak | — | — |
| 1889 | N. Denison | — | Perak | — | — |

### Deterministic checks: `denison_n_e1869` vs `Denison, N___Straits Settlements___1888`

- [PASS] surname_gate: bio 'DENISON' vs stint 'Denison, N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

