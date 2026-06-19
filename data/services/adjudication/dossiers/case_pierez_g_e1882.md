<!-- {"case_id": "case_pierez_g_e1882", "bio_ids": ["pierez_g_e1882", "pieriez_g_e1882", "pierrez_g_e1882"], "stint_ids": ["Pierez, G. E___Antigua___1890"]} -->
# Dossier case_pierez_g_e1882

## Case context

- 3 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pierez_g_e1882', 'pieriez_g_e1882', 'pierrez_g_e1882'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Pierez, G. E___Antigua___1890'] have more than one claimant biography in this case.

## Biography `pierez_g_e1882`

- Printed name: **PIEREZ, G**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1886, 1889, 1890, 1894, 1896, 1898, 1905]

### Verbatim printed entry text (OCR)

**Version `col1886-L35287.v` — printed in editions [1886, 1889, 1890, 1894, 1896, 1898, 1905]:**

> PIEREZ, G., M.B., C.M.—Medical officer, Antigua, 8 Feb., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Medical officer | Antigua | [1886, 1889, 1890, 1894, 1896, 1898, 1905] |

## Biography `pieriez_g_e1882`

- Printed name: **PIERIEZ, G**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L36825.v` — printed in editions [1899]:**

> PIERIEZ, G., M.B., C.M.—Med. offr., Antigua, Feb., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Med. offr. | Antigua | [1899] |

## Biography `pierrez_g_e1882`

- Printed name: **PIERREZ, G**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1888, 1900]

### Verbatim printed entry text (OCR)

**Version `col1888-L35538.v` — printed in editions [1888, 1900]:**

> PIERREZ, G., M.B., C.M.—Medical officer, Antigua, 8 Feb., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Medical officer | Antigua | [1888, 1900] |

## Candidate stint `Pierez, G. E___Antigua___1890`

- Staff-list name: **Pierez, G. E** | colony: **Antigua** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | G. E. Pierez | — | Medical | — | — |
| 1894 | G. E. Pierez | — | Medical | — | — |

### Deterministic checks: `pierez_g_e1882` vs `Pierez, G. E___Antigua___1890`

- [PASS] surname_gate: bio 'PIEREZ' vs stint 'Pierez, G. E' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Antigua'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `pieriez_g_e1882` vs `Pierez, G. E___Antigua___1890`

- [PASS] surname_gate: bio 'PIERIEZ' vs stint 'Pierez, G. E' (fuzzy:1)
- [PASS] initials: bio ['G'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Antigua'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `pierrez_g_e1882` vs `Pierez, G. E___Antigua___1890`

- [PASS] surname_gate: bio 'PIERREZ' vs stint 'Pierez, G. E' (fuzzy:1)
- [PASS] initials: bio ['G'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Antigua'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

