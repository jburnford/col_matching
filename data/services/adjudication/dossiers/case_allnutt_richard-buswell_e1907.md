<!-- {"case_id": "case_allnutt_richard-buswell_e1907", "bio_ids": ["allnutt_richard-buswell_e1907", "allutt_richard-buswell_b1907"], "stint_ids": ["Allnutt, R. B___Leeward Islands___1949"]} -->
# Dossier case_allnutt_richard-buswell_e1907

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Allnutt, R. B___Leeward Islands___1949'] have more than one claimant biography in this case.

## Biography `allnutt_richard-buswell_e1907`

- Printed name: **ALLNUTT, RICHARD BUSWELL**
- Birth year: not printed
- Appears in editions: [1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1934-L56201.v` — printed in editions [1934, 1935, 1936]:**

> ALLNUTT, RICHARD BUSWELL, B.Sc. (Agric.)—B.—1907; ed Malvern Coll. and S. Eastern Agric. Coll., Wye (B.Sc. (agric.) (Lond.) and dipl., agr., 1928; crop. observn. offr., Norfolk agric. sta., 1928-30; dist. agric. offr., Tanganyika Territory, July, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | B.— | — | [1934, 1935, 1936] |
| 1 | 1928–1930 | crop. observn. offr., Norfolk agric. sta | — | [1934, 1935, 1936] |
| 2 | 1930 | dist. agric. offr., Tanganyika Territory | Tanganyika | [1934, 1935, 1936] |

## Biography `allutt_richard-buswell_b1907`

- Printed name: **ALLUTT, RICHARD BUSWELL**
- Birth year: 1907 (attested in editions [1937])
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L58450.v` — printed in editions [1937]:**

> ALLUTT, RICHARD BUSWELL, B.Sc.—B. 1907; ed Malvern Coll. and S. Eastern Coll., Wye; B.Sc. (agr.) (Lond.) and dipl. 1928; crop. observn. offr., Norfolk agr., 1928-30; dist. agrl. offr., Tanganyika Territory, July, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | B.Sc. (agr.) (Lond.) and dipl | — | [1937] |
| 1 | 1928–1930 | crop. observn. offr., Norfolk agr | — | [1937] |
| 2 | 1930 | dist. agrl. offr., Tanganyika Territory | Tanganyika | [1937] |

## Candidate stint `Allnutt, R. B___Leeward Islands___1949`

- Staff-list name: **Allnutt, R. B** | colony: **Leeward Islands** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. B. Allnutt | Director of Agriculture | AGRICULTURE | — | — |
| 1950 | R. B. Allnutt | Director of Agriculture | Agriculture | — | — |
| 1951 | R. B. Allnutt | Director of Agriculture | Agriculture | — | — |

### Deterministic checks: `allnutt_richard-buswell_e1907` vs `Allnutt, R. B___Leeward Islands___1949`

- [PASS] surname_gate: bio 'ALLNUTT' vs stint 'Allnutt, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `allutt_richard-buswell_b1907` vs `Allnutt, R. B___Leeward Islands___1949`

- [PASS] surname_gate: bio 'ALLUTT' vs stint 'Allnutt, R. B' (fuzzy:1)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

