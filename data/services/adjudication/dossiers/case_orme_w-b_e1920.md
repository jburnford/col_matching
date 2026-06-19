<!-- {"case_id": "case_orme_w-b_e1920", "bio_ids": ["orme_w-b_e1920", "orme_william-bryce_b1871"], "stint_ids": ["Orme, W. B___Straits Settlements___1922"]} -->
# Dossier case_orme_w-b_e1920

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Orme, W. B___Straits Settlements___1922'] have more than one claimant biography in this case.

## Biography `orme_w-b_e1920`

- Printed name: **ORME, W. B**
- Birth year: not printed
- Appears in editions: [1921]

### Verbatim printed entry text (OCR)

**Version `col1921-L58946.v` — printed in editions [1921]:**

> ORME, W. B.—Prin. med. offr., Johore, Jan., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | Prin. med. offr. | Johore | [1921] |

## Biography `orme_william-bryce_b1871`

- Printed name: **ORME, WILLIAM BRYCE**
- Birth year: 1871 (attested in editions [1923, 1924])
- Appears in editions: [1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1923-L57144.v` — printed in editions [1923, 1924]:**

> ORME, WILLIAM BRYCE, M.R.C.S. (Eng.), L.R.C.P. (Lond.) 1894, D.T.M. and H. Cantab., Dip. (distn.), Lond. Sch. Trop. Med., 1907 (Univ. Coll. Lond.); Imp. Ottoman Order of the Medjedieh.—B. 1871; med. offr., Larut, Perak, F.M.S., and health offr., Lower Perak; seconded for three years for the reorganisation of the Br. N. Borneo med. serv., 1913-16; P.M.O., Johore, Jan., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1916 | seconded for three years for the reorganisation of the Br. N. Borneo med. serv | — | [1923, 1924] |
| 1 | 1920 | P.M.O. | Johore | [1923, 1924] |

## Candidate stint `Orme, W. B___Straits Settlements___1922`

- Staff-list name: **Orme, W. B** | colony: **Straits Settlements** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. B. Orme | Officer seconded to Unfederated States | Medical | — | — |
| 1923 | W. B. Orme | Officer seconded to Unfederated States | Medical | — | — |

### Deterministic checks: `orme_w-b_e1920` vs `Orme, W. B___Straits Settlements___1922`

- [PASS] surname_gate: bio 'ORME' vs stint 'Orme, W. B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `orme_william-bryce_b1871` vs `Orme, W. B___Straits Settlements___1922`

- [PASS] surname_gate: bio 'ORME' vs stint 'Orme, W. B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1922, birth 1871 (age 51)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

