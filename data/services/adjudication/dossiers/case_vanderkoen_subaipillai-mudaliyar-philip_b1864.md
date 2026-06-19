<!-- {"case_id": "case_vanderkoen_subaipillai-mudaliyar-philip_b1864", "bio_ids": ["vanderkoen_subaipillai-mudaliyar-philip_b1864", "vanderkoen_susaipillai-mudaliar-philip_b1864"], "stint_ids": ["Vanderyken, M___Trinidad and Tobago___1914"]} -->
# Dossier case_vanderkoen_subaipillai-mudaliyar-philip_b1864

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Vanderyken, M___Trinidad and Tobago___1914'] have more than one claimant biography in this case.

## Biography `vanderkoen_subaipillai-mudaliyar-philip_b1864`

- Printed name: **VANDERKOEN, Subaipillai Mudaliyar Philip**
- Birth year: 1864 (attested in editions [1924])
- Appears in editions: [1924]

### Verbatim printed entry text (OCR)

**Version `col1924-L58526.v` — printed in editions [1924]:**

> VANDERKOEN, Subaipillai Mudaliyar Philip.—B. 1864; cls V., Ceylon civ. serv., Apr., 1921; office ast. to ast. govt. agt., Puttalam.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cls V., Ceylon civ. serv | Ceylon | [1924] |

## Biography `vanderkoen_susaipillai-mudaliar-philip_b1864`

- Printed name: **VANDERKOEN, SUSAIPILLAI MUDALIAR PHILIP**
- Birth year: 1864 (attested in editions [1922, 1923])
- Appears in editions: [1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1922-L56757.v` — printed in editions [1922, 1923]:**

> VANDERKOEN, SUSAIPILLAI MUDALIAR PHILIP.—B. 1864; cls. V., Ceylon civ. serv., Apr., 1921; office asst. to asst. gov't. agt., Puttalam.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cls. V., Ceylon civ. serv | Ceylon | [1922, 1923] |

## Candidate stint `Vanderyken, M___Trinidad and Tobago___1914`

- Staff-list name: **Vanderyken, M** | colony: **Trinidad and Tobago** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | M. Vanderyken | Assistant Priest | Roman Catholic Church | — | — |
| 1915 | M. Vanderyken | Assistant Priests | Roman Catholic Church | — | — |

### Deterministic checks: `vanderkoen_subaipillai-mudaliyar-philip_b1864` vs `Vanderyken, M___Trinidad and Tobago___1914`

- [PASS] surname_gate: bio 'VANDERKOEN' vs stint 'Vanderyken, M' (fuzzy:2)
- [PASS] initials: bio ['S', 'M', 'P'] ~ stint ['M']
- [PASS] age_gate: stint starts 1914, birth 1864 (age 50)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `vanderkoen_susaipillai-mudaliar-philip_b1864` vs `Vanderyken, M___Trinidad and Tobago___1914`

- [PASS] surname_gate: bio 'VANDERKOEN' vs stint 'Vanderyken, M' (fuzzy:2)
- [PASS] initials: bio ['S', 'M', 'P'] ~ stint ['M']
- [PASS] age_gate: stint starts 1914, birth 1864 (age 50)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
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

