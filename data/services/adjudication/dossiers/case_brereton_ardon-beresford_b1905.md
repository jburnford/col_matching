<!-- {"case_id": "case_brereton_ardon-beresford_b1905", "bio_ids": ["brereton_ardon-beresford_b1905"], "stint_ids": ["Brereton, A. B___Windward Islands___1933"]} -->
# Dossier case_brereton_ardon-beresford_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brereton_ardon-beresford_b1905`

- Printed name: **BRERETON, Ardon Beresford**
- Birth year: 1905 (attested in editions [1951])
- Honours: M.B
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L36413.v` — printed in editions [1951]:**

> BRERETON, Ardon Beresford, M.B., Ch.B. (Edin.), D.M.R.E. (Camb.).—b. 1905; ed. St. Vincent Gram. Sch., Edin. Univ., Edin. Royal Infirm., Camb. Univ. and Middx. Hosp., Lond.; post-grad. wk. in U.S.A., 1945; apptd. med. offr., 1931; med. offr. in charge radiological clinic, St. V., 1937; res. surg. in addn., 1947; radiologist, G.C., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | apptd. med. offr | — | [1951] |
| 1 | 1937 | med. offr. in charge radiological clinic | St. Vincent | [1951] |
| 2 | 1945 | post-grad. wk. in U.S.A | — | [1951] |
| 3 | 1947 | res. surg. in addn | St. Vincent *(inherited from previous clause)* | [1951] |
| 4 | 1949 | radiologist | Gold Coast | [1951] |

## Candidate stint `Brereton, A. B___Windward Islands___1933`

- Staff-list name: **Brereton, A. B** | colony: **Windward Islands** | listed 1933–1936 | editions [1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | A. B. Brereton | District Medical Officer | Medical | — | — |
| 1936 | A. B. Brereton | District Medical Officer | Medical | — | — |

### Deterministic checks: `brereton_ardon-beresford_b1905` vs `Brereton, A. B___Windward Islands___1933`

- [PASS] surname_gate: bio 'BRERETON' vs stint 'Brereton, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1933, birth 1905 (age 28)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1936
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

