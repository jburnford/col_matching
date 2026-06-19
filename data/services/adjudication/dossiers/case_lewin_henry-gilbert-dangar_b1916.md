<!-- {"case_id": "case_lewin_henry-gilbert-dangar_b1916", "bio_ids": ["lewin_henry-gilbert-dangar_b1916"], "stint_ids": ["Lewin, H___Ceylon___1934"]} -->
# Dossier case_lewin_henry-gilbert-dangar_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lewin_henry-gilbert-dangar_b1916`

- Printed name: **LEWIN, Henry Gilbert Dangar**
- Birth year: 1916 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37270.v` — printed in editions [1950, 1951]:**

> LEWIN, Henry Gilbert Dangar.—b. 1916; ed. Winchester Coll. and Camb. Univ., B.A.; on war serv., 1942-45; cadet, customs and excise dept., S.S. and F.M.S. (S'pore.), 1939; customs offr., 1942; Penang, 1946; senr. customs offr., Lumut, 1946; prev. br., Kuala Lumpur, 1946; Raub., 1947; port divn. prev. branch, S'pore., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | cadet, customs and excise dept., S.S. and F.M.S. (S'pore.) | Straits Settlements | [1950, 1951] |
| 1 | 1942 | customs offr | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1946 | Penang | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1947 | Raub | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1948 | port divn. prev. branch, S'pore | Straits Settlements *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Lewin, H___Ceylon___1934`

- Staff-list name: **Lewin, H** | colony: **Ceylon** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | H. Lewin | Assistant Architect | Public Works Department | — | Major |
| 1936 | H. Lewin | Assistant Architect | Public Works Department | — | Major |

### Deterministic checks: `lewin_henry-gilbert-dangar_b1916` vs `Lewin, H___Ceylon___1934`

- [PASS] surname_gate: bio 'LEWIN' vs stint 'Lewin, H' (exact)
- [PASS] initials: bio ['H', 'G', 'D'] ~ stint ['H']
- [PASS] age_gate: stint starts 1934, birth 1916 (age 18)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1936
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

