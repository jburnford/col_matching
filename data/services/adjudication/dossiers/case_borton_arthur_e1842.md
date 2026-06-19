<!-- {"case_id": "case_borton_arthur_e1842", "bio_ids": ["borton_arthur_e1842"], "stint_ids": ["Borton, Arthur___Leeward Islands___1897", "Borton, Arthur___Virgin Islands___1890"]} -->
# Dossier case_borton_arthur_e1842

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['borton_arthur_e1842'] carry a single initial only — the namesake trap applies.

## Biography `borton_arthur_e1842`

- Printed name: **BORTON, ARTHUR**
- Birth year: not printed
- Honours: G.C.M.G. (1880), K.C.B.
- Terminal: retired 1884 — “retired 7th June, 1884.”
- Appears in editions: [1886, 1888, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32265.v` — printed in editions [1886, 1888, 1890]:**

> BORTON, GENERAL SIR ARTHUR, G.C.M.G. (1880), K.C.B.—Appointed governor and commander-in-chief of Malta, June, 1878; served with the 9th Regiment the campaign of 1842 in Afghanistan (medal), and that of 1845-6 on the Sutlej, including the battles of Moodkee and Ferozeshah (medal and clasp), in the latter he succeeded to the command of the regiment, and was severely wounded; served also the campaign in the Crimea, in command of the regiment, from 27th Nov., 1854, including the siege and fall of Sebastopol and assault on the batteries on the 16th June (medal with clasp, C.B.), Knight of the Legion of Honour, 3rd class of the Medjidieh, and Turkish medal; retired 7th June, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1842–1842 | — | Afghanistan | [1886, 1888, 1890] |
| 1 | 1845–1846 | command of the regiment | — | [1886, 1888, 1890] |
| 2 | 1854 | command of the regiment | Crimea | [1886, 1888, 1890] |
| 3 | 1878 | governor and commander-in-chief | Malta | [1886, 1888, 1890] |

## Candidate stint `Borton, Arthur___Leeward Islands___1897`

- Staff-list name: **Borton, Arthur** | colony: **Leeward Islands** | listed 1897–1899 | editions [1897, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | Arthur Borton | Governor | Governors | G.C.M.G., K.C.B. | — |
| 1899 | Sir Arthur Borton | Governor | Governors | G.C.M.G., K.C.B. | — |

### Deterministic checks: `borton_arthur_e1842` vs `Borton, Arthur___Leeward Islands___1897`

- [PASS] surname_gate: bio 'BORTON' vs stint 'Borton, Arthur' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1899
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: G.C.M.G., K.C.B.
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Borton, Arthur___Virgin Islands___1890`

- Staff-list name: **Borton, Arthur** | colony: **Virgin Islands** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | Sir Arthur Borton | Governor | Governors | G.C.M.G., K.C.B. | — |
| 1894 | Gen. Sir Arthur Borton | Governor | Governors | G.C.M.G., K.C.B. | — |

### Deterministic checks: `borton_arthur_e1842` vs `Borton, Arthur___Virgin Islands___1890`

- [PASS] surname_gate: bio 'BORTON' vs stint 'Borton, Arthur' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Virgin Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: G.C.M.G., K.C.B.
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

