<!-- {"case_id": "case_stott_d_b1913", "bio_ids": ["stott_d_b1913"], "stint_ids": ["Stott, D. J___Jamaica___1933"]} -->
# Dossier case_stott_d_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['stott_d_b1913'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Stott, D. J___Jamaica___1933` is also gate-compatible with biography(ies) outside this case: ['stott_douglas-jaffrey_b1896'] (already linked elsewhere or filtered).

## Biography `stott_d_b1913`

- Printed name: **STOTT, D**
- Birth year: 1913 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L27735.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> STOTT, D.—b. 1913; ed. L’pool Inst. High Sch., and L’pool Univ.; engrn. and survr., dept. of agric., Scotland, 1945–48; exec. engrn., N. Rhod., 1949; senr. exec. engrn., 1956; dep. dir. of roads, 1962–65. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945–1948 | engrn. and survr., dept. of agric., Scotland | — | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1949 | exec. engrn. | Northern Rhodesia | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1956 | senr. exec. engrn | Northern Rhodesia *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1962–1965 | dep. dir. of roads | Northern Rhodesia *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Stott, D. J___Jamaica___1933`

- Staff-list name: **Stott, D. J** | colony: **Jamaica** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | D. J. Stott | Senior District Engineer | Railways | — | — |
| 1934 | D. J. Stott | Senior District Engineer | Railways | — | — |

### Deterministic checks: `stott_d_b1913` vs `Stott, D. J___Jamaica___1933`

- [PASS] surname_gate: bio 'STOTT' vs stint 'Stott, D. J' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D', 'J']
- [PASS] age_gate: stint starts 1933, birth 1913 (age 20)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1934
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

