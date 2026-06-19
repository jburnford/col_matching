<!-- {"case_id": "case_melvill_samuel_e1851", "bio_ids": ["melvill_samuel_e1851"], "stint_ids": ["Melvill, S___Cape of Good Hope___1888", "Melvill, S___Transvaal___1879"]} -->
# Dossier case_melvill_samuel_e1851

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['melvill_samuel_e1851'] carry a single initial only — the namesake trap applies.

## Biography `melvill_samuel_e1851`

- Printed name: **MELVILL, SAMUEL**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1894-L32982.v` — printed in editions [1894, 1896, 1897]:**

> MELVILL, SAMUEL.—Served as captain commanding George native levy, Jan. to Sept., 1851; and lost arm in action at Amatola Basin, 23rd June, 1851; 2nd asst. surveyor-general, July, 1882; railway expropriation commr., Aug., 1889; was commissioner of Lichtenberg, and agent for native affairs on the south-west boundary of the Transvaal, July, 1873, to Oct., 1874; and surveyor-general from latter date to April, 1877, under the government of the S. A. Republic; and surveyor-general from April, 1877, to Aug., 1881, under British rule; first assistant surveyor-general, Cape, July, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851–1851 | captain commanding George native levy | — | [1894, 1896, 1897] |
| 1 | 1851–1851 | — | Amatola Basin | [1894, 1896, 1897] |
| 2 | 1873–1874 | commissioner of Lichtenberg, and agent for native affairs on the south-west boundary of the Transvaal | Transvaal | [1894, 1896, 1897] |
| 3 | 1874–1877 | surveyor-general | South African Republic | [1894, 1896, 1897] |
| 4 | 1877–1881 | surveyor-general | — | [1894, 1896, 1897] |
| 5 | 1882 | 2nd asst. surveyor-general | — | [1894, 1896, 1897] |
| 6 | 1889 | railway expropriation commr. | — | [1894, 1896, 1897] |
| 7 | 1892 | first assistant surveyor-general | Cape Colony | [1894, 1896, 1897] |

## Candidate stint `Melvill, S___Cape of Good Hope___1888`

- Staff-list name: **Melvill, S** | colony: **Cape of Good Hope** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | S. Melvill | Second Assistant Surveyor-General | Surveyor-General's Office | — | — |
| 1889 | S. Melvill | Second Assistant Surveyor-General | Surveyor-General's Office | — | — |
| 1890 | S. Melvill | Second Assistant Surveyor-General | Surveyor-General's Office | — | — |

### Deterministic checks: `melvill_samuel_e1851` vs `Melvill, S___Cape of Good Hope___1888`

- [PASS] surname_gate: bio 'MELVILL' vs stint 'Melvill, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Melvill, S___Transvaal___1879`

- Staff-list name: **Melvill, S** | colony: **Transvaal** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | S. Melvill | Surveyor-General | Civil Establishment | — | — |
| 1880 | S. Melvill | Surveyor-General | Civil Establishment | — | — |

### Deterministic checks: `melvill_samuel_e1851` vs `Melvill, S___Transvaal___1879`

- [PASS] surname_gate: bio 'MELVILL' vs stint 'Melvill, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Transvaal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
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

