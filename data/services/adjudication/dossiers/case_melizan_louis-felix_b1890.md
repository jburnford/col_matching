<!-- {"case_id": "case_melizan_louis-felix_b1890", "bio_ids": ["melizan_louis-felix_b1890"], "stint_ids": ["Melizan, L. F___Trinidad and Tobago___1933"]} -->
# Dossier case_melizan_louis-felix_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `melizan_louis-felix_b1890`

- Printed name: **MELIZAN, LOUIS FELIX**
- Birth year: 1890 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66744.v` — printed in editions [1940]:**

> MELIZAN, LOUIS FELIX.—B. 1890; ed. St. Mary's Coll., Trinidad and Maison de Melle-lez-Gand, Belgium; dip. d'Arp., Gand, 1917; cert. in forestry, Imperial Research Inst. and Coll., Dehra-Dun, India, 1923, with medal for surveying; temp. asst. to forest offr., Trinidad, 1915-18; 2nd dep. conserv., forests, 1923-29; asst. conserv., forests, Trinidad, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | temp. asst. to forest offr. | Trinidad | [1940] |
| 1 | 1923–1929 | 2nd dep. conserv., forests | — | [1940] |
| 2 | 1930 | asst. conserv., forests | Trinidad | [1940] |

## Candidate stint `Melizan, L. F___Trinidad and Tobago___1933`

- Staff-list name: **Melizan, L. F** | colony: **Trinidad and Tobago** | listed 1933–1940 | editions [1933, 1934, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | L. F. Melizan | Assistant Conservator of Forests | Forest Department | — | — |
| 1934 | L. F. Melizan | Assistant Conservator of Forests | Forest Department | — | — |
| 1939 | L. F. Melizan | Assistant Conservators of Forests | FOREST DEPARTMENT | — | — |
| 1940 | L. F. Melizan | Assistant Conservator | Forests | — | — |

### Deterministic checks: `melizan_louis-felix_b1890` vs `Melizan, L. F___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'MELIZAN' vs stint 'Melizan, L. F' (exact)
- [PASS] initials: bio ['L', 'F'] ~ stint ['L', 'F']
- [PASS] age_gate: stint starts 1933, birth 1890 (age 43)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
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

