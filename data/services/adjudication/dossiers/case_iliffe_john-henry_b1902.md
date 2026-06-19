<!-- {"case_id": "case_iliffe_john-henry_b1902", "bio_ids": ["iliffe_john-henry_b1902"], "stint_ids": ["Iliffe, J. H___Palestine___1932"]} -->
# Dossier case_iliffe_john-henry_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `iliffe_john-henry_b1902`

- Printed name: **ILIFFE, John Henry**
- Birth year: 1902 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L33550.v` — printed in editions [1948]:**

> ILIFFE, John Henry.—b. 1902; ed. Market Bosworth Gram. Sch. and Emmanuel Coll., Cambridge (schol.), M.A. (Cantab.); Br. Sch. of Archaeology Athens, dip in class. archaeol., lecturer in classics, Univ. Coll., N. Wales, 1925-7; asst. professor of Archaeology, Univ. of Toronto, and keeper of classical collection, Royal Ontario museum, Toronto, 1927-31; keeper of the Pal. archaeological museum, dept. of antiquities, 1931; food contr., 1943-44; asst. Br. res., Trans Jordan, 1944-46; author of a catalogue of the Greek Vases in the Royal Ontario Museum of Archaeology and a short guide to the exhibition illustrating the stone and bronze ages in Palestine, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925–1927 | Br. Sch. of Archaeology Athens, dip in class. archaeol., lecturer in classics, Univ. Coll., N. Wales | — | [1948] |
| 1 | 1927–1931 | asst. professor of Archaeology, Univ. of Toronto, and keeper of classical collection, Royal Ontario museum, Toronto | — | [1948] |
| 2 | 1931 | keeper of the Pal. archaeological museum, dept. of antiquities | — | [1948] |
| 3 | 1937 | author of a catalogue of the Greek Vases in the Royal Ontario Museum of Archaeology and a short guide to the exhibition illustrating the stone and bronze ages in Palestine | Trans Jordan *(inherited from previous clause)* | [1948] |
| 4 | 1943–1944 | food contr | — | [1948] |
| 5 | 1944–1946 | asst. Br. res. | Trans Jordan | [1948] |

## Candidate stint `Iliffe, J. H___Palestine___1932`

- Staff-list name: **Iliffe, J. H** | colony: **Palestine** | listed 1932–1940 | editions [1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | J. H. Iliffe | Keeper of Museum | Department of Antiquities | — | — |
| 1940 | J. H. Iliffe | Keeper, Archeological Museum | Department of Antiquities | — | — |

### Deterministic checks: `iliffe_john-henry_b1902` vs `Iliffe, J. H___Palestine___1932`

- [PASS] surname_gate: bio 'ILIFFE' vs stint 'Iliffe, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1932, birth 1902 (age 30)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1940
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

