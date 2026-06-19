<!-- {"case_id": "case_dunn_stephen-troyte_b1868", "bio_ids": ["dunn_stephen-troyte_b1868"], "stint_ids": ["Dunn, S. T___Hong Kong___1905"]} -->
# Dossier case_dunn_stephen-troyte_b1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dunn_stephen-troyte_b1868`

- Printed name: **DUNN, STEPHEN TROYTE**
- Birth year: 1868 (attested in editions [1906, 1907, 1908, 1909, 1910])
- Honours: F.L.S, F.R.G.S
- Appears in editions: [1906, 1907, 1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1906-L45242.v` — printed in editions [1906, 1907, 1908, 1909, 1910]:**

> DUNN, STEPHEN TROYTE, F.L.S., F.R.G.S.—B. 1868; ed. Radley and Merton Coll., Oxford; B.A., 1889; asst. for India, Kew Gdns., 1899; sup., bot. and forestry dept., Hong Kong, 1903; J.P., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | B.A | — | [1906, 1907, 1908, 1909, 1910] |
| 1 | 1899 | asst. for India, Kew Gdns | — | [1906, 1907, 1908, 1909, 1910] |
| 2 | 1903 | sup., bot. and forestry dept. | Hong Kong | [1906, 1907, 1908, 1909, 1910] |
| 3 | 1906 | J.P | Hong Kong *(inherited from previous clause)* | [1906, 1907, 1908, 1909, 1910] |

## Candidate stint `Dunn, S. T___Hong Kong___1905`

- Staff-list name: **Dunn, S. T** | colony: **Hong Kong** | listed 1905–1910 | editions [1905, 1906, 1907, 1908, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | S. T. Dunn | Superintendent | Botanical and Afforestation Department | — | — |
| 1906 | S. T. Dunn | Superintendent | Botanical and Forestry Department | — | — |
| 1907 | S. T. Dunn | Superintendent | Botanical and Forestry Department | — | — |
| 1908 | S. T. Dunn | Superintendent | Botanical and Forestry Department | — | — |
| 1909 | S. T. Dunn | Superintendent | Botanical and Forestry Department | — | — |
| 1910 | S. T. Dunn | Superintendent | Botanical and Forestry Department | — | — |

### Deterministic checks: `dunn_stephen-troyte_b1868` vs `Dunn, S. T___Hong Kong___1905`

- [PASS] surname_gate: bio 'DUNN' vs stint 'Dunn, S. T' (exact)
- [PASS] initials: bio ['S', 'T'] ~ stint ['S', 'T']
- [PASS] age_gate: stint starts 1905, birth 1868 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1905-1910
- [FAIL] position_sim: best 26 vs bar 60: 'sup., bot. and forestry dept.' ~ 'Superintendent'
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

