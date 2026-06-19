<!-- {"case_id": "case_tagliaferro_napoleone_e1864", "bio_ids": ["tagliaferro_napoleone_e1864"], "stint_ids": ["Tagliaferro, Napoleon___Leeward Islands___1897", "Tagliaferro, Napoleon___Malta___1883"]} -->
# Dossier case_tagliaferro_napoleone_e1864

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['tagliaferro_napoleone_e1864'] carry a single initial only — the namesake trap applies.

## Biography `tagliaferro_napoleone_e1864`

- Printed name: **TAGLIAFERRO, NAPOLEONE**
- Birth year: not printed
- Appears in editions: [1900]

### Verbatim printed entry text (OCR)

**Version `col1900-L37455.v` — printed in editions [1900]:**

> TAGLIAFERRO, NAPOLEONE.—Ed. Malta Univ., and Paris Sorbonne; prof. of physics in the univ., 1864; prin. of univ., and sec. to educn. dept., 1880-7; offr. in charge of educn. dept., May to Sept., 1887; asst. dir. of educ., Sept., 1887 to Dec., 1897; registr. of census of the Maltese Is., Feb., 1891, to Mar., 1892; dir. of educn., July, 1897, with a seat in exec. coun. and in coun. of govt., since Apr., 1899.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864–1864 | prof. of physics in the univ. | — | [1900] |
| 1 | 1880–1887 | prin. of univ., and sec. to educn. dept. | — | [1900] |
| 2 | 1887–1887 | offr. in charge of educn. dept. | — | [1900] |
| 3 | 1887–1897 | asst. dir. of educ. | — | [1900] |
| 4 | 1891–1892 | registr. of census | Maltese Islands | [1900] |
| 5 | 1897 | dir. of educn. | — | [1900] |

## Candidate stint `Tagliaferro, Napoleon___Leeward Islands___1897`

- Staff-list name: **Tagliaferro, Napoleon** | colony: **Leeward Islands** | listed 1897–1899 | editions [1897, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | N. Tagliaferro | Assistant and Secretary to the Senate of the Malta University | Educational | — | — |
| 1899 | Napoleon Tagliaferro | Director of Education | Educational | — | — |

### Deterministic checks: `tagliaferro_napoleone_e1864` vs `Tagliaferro, Napoleon___Leeward Islands___1897`

- [PASS] surname_gate: bio 'TAGLIAFERRO' vs stint 'Tagliaferro, Napoleon' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1899
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Tagliaferro, Napoleon___Malta___1883`

- Staff-list name: **Tagliaferro, Napoleon** | colony: **Malta** | listed 1883–1905 | editions [1883, 1886, 1889, 1898, 1899, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | N. Tagliaferro | Principal of the University and Secretary to the Education Department | Educational | — | — |
| 1886 | N. Tagliaferro | Principal of the University and Secretary to the Education Department | Educational | — | — |
| 1889 | N. Tagliaferro | Assistant and Secretary to the Senate of the Malta University | Educational | — | — |
| 1898 | Napoleon Tagliaferro | Director of Education | Educational | — | — |
| 1899 | Napoleon Tagliaferro | Director of Education | Educational | — | — |
| 1905 | Napoleon Tagliaferro | Director of Education | Educational | — | — |

### Deterministic checks: `tagliaferro_napoleone_e1864` vs `Tagliaferro, Napoleon___Malta___1883`

- [PASS] surname_gate: bio 'TAGLIAFERRO' vs stint 'Tagliaferro, Napoleon' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1905
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

