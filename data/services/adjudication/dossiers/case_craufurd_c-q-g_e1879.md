<!-- {"case_id": "case_craufurd_c-q-g_e1879", "bio_ids": ["craufurd_c-q-g_e1879", "craufurd_commdr-c-q-g_e1879"], "stint_ids": ["Craufurd, C. Q. G___Straits Settlements___1894"]} -->
# Dossier case_craufurd_c-q-g_e1879

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Craufurd, C. Q. G___Straits Settlements___1894'] have more than one claimant biography in this case.

## Biography `craufurd_c-q-g_e1879`

- Printed name: **CRAUFURD, C. Q. G**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L32853.v` — printed in editions [1886, 1888]:**

> CRAUFURD, CAPTAIN C. Q. G., R.N.—Harbour master, and superintendent of mercantile marine, Mauritius, 5th Nov., 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Harbour master, and superintendent of mercantile marine | Mauritius | [1886, 1888] |

## Biography `craufurd_commdr-c-q-g_e1879`

- Printed name: **CRAUFURD, COMMDR. C. Q. G**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894, 1896, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1889-L32532.v` — printed in editions [1889, 1890, 1894, 1896, 1898, 1899, 1900]:**

> CRAUFURD, COMMDR. C. Q. G., R.N.—Harbour master, and supt. of mercantile marine, Mauritius, Nov., 1879; mr. attndt. Straits Settts., 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Harbour master, and supt. of mercantile marine | Mauritius | [1889, 1890, 1894, 1896, 1898, 1899, 1900] |
| 1 | 1888 | mr. attndt. Straits Settts | Mauritius *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1898, 1899, 1900] |

## Candidate stint `Craufurd, C. Q. G___Straits Settlements___1894`

- Staff-list name: **Craufurd, C. Q. G** | colony: **Straits Settlements** | listed 1894–1899 | editions [1894, 1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | C. Q. G. Craufurd, R.N. | Master Attendant | Marine Department | — | — |
| 1896 | C. Q. G. Craufurd | Master Attendant | Marine Department | — | — |
| 1897 | C. Q. G. Craufurd | Master Attendant | Marine Department | — | — |
| 1898 | C. Q. G. Craufurd | Master Attendant | Marine Department | — | — |
| 1899 | C. Q. G. Craufurd | Master Attendant | Marine Department | — | — |

### Deterministic checks: `craufurd_c-q-g_e1879` vs `Craufurd, C. Q. G___Straits Settlements___1894`

- [PASS] surname_gate: bio 'CRAUFURD' vs stint 'Craufurd, C. Q. G' (exact)
- [PASS] initials: bio ['C', 'Q', 'G'] ~ stint ['C', 'Q', 'G']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1899
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `craufurd_commdr-c-q-g_e1879` vs `Craufurd, C. Q. G___Straits Settlements___1894`

- [PASS] surname_gate: bio 'CRAUFURD' vs stint 'Craufurd, C. Q. G' (exact)
- [PASS] initials: bio ['C', 'C', 'Q', 'G'] ~ stint ['C', 'Q', 'G']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1899
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

