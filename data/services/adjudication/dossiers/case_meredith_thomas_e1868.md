<!-- {"case_id": "case_meredith_thomas_e1868", "bio_ids": ["meredith_thomas_e1868"], "stint_ids": ["Meredith, T___Straits Settlements___1888"]} -->
# Dossier case_meredith_thomas_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['meredith_thomas_e1868'] carry a single initial only — the namesake trap applies.

## Biography `meredith_thomas_e1868`

- Printed name: **MEREDITH, THOMAS**
- Birth year: not printed
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L34609.v` — printed in editions [1889, 1890]:**

> MEREDITH, THE REV. ARCHDEACON THOMAS.—Graduated at Exeter Coll., Oxon., B.A., 3rd class Nat. Science, 1868; M.A., 1871, curate of Eristock, Dio. S. Asaph, 1869-72; chaplain to Sir Watkin Williams Wynn, Bart., M.P., 1872-75; senior curate of Holy Trinity, St. Marylebone, 1875-81; colonial chaplain of Singapore, Sept., 1881; Archdeacon, 1882; Surrogate, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868–1868 | B.A., 3rd class Nat. Science | — | [1889, 1890] |
| 1 | 1869–1872 | curate of Eristock, Dio. S. Asaph | — | [1889, 1890] |
| 2 | 1871–1871 | M.A. | — | [1889, 1890] |
| 3 | 1872–1875 | chaplain to Sir Watkin Williams Wynn, Bart., M.P. | — | [1889, 1890] |
| 4 | 1875–1881 | senior curate of Holy Trinity, St. Marylebone | — | [1889, 1890] |
| 5 | 1881 | colonial chaplain | Singapore | [1889, 1890] |
| 6 | 1882–1882 | Archdeacon | — | [1889, 1890] |
| 7 | 1882–1882 | Surrogate | — | [1889, 1890] |

## Candidate stint `Meredith, T___Straits Settlements___1888`

- Staff-list name: **Meredith, T** | colony: **Straits Settlements** | listed 1888–1890 | editions [1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | T. Meredith | Chaplain, The Ven. Archdeacon | Ecclesiastical | — | — |
| 1890 | T. Meredith | Chaplain | Ecclesiastical | — | — |

### Deterministic checks: `meredith_thomas_e1868` vs `Meredith, T___Straits Settlements___1888`

- [PASS] surname_gate: bio 'MEREDITH' vs stint 'Meredith, T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
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

