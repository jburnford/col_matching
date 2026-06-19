<!-- {"case_id": "case_catti_a_e1881", "bio_ids": ["catti_a_e1881"], "stint_ids": ["Catt, Alfred___South Australia___1888", "Catt, Alfred___South Australia___1898"]} -->
# Dossier case_catti_a_e1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['catti_a_e1881'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Catt, Alfred___South Australia___1888` is also gate-compatible with biography(ies) outside this case: ['catt_a_e1881', 'catta_a_e1881'] (already linked elsewhere or filtered).
- NOTE: stint `Catt, Alfred___South Australia___1898` is also gate-compatible with biography(ies) outside this case: ['catt_a_e1881', 'catta_a_e1881'] (already linked elsewhere or filtered).

## Biography `catti_a_e1881`

- Printed name: **CATTI, A.**
- Birth year: not printed
- Appears in editions: [1905]

### Verbatim printed entry text (OCR)

**Version `col1905-L42442.v` — printed in editions [1905]:**

> CATTI, THE HON. A.—Mem. house of assem., S. Australia, since 1881; comsnr. of crown lands, S. Australia, June, 1881, to June, 1884; comsnr. of pub. wks., June, 1887, to June, 1889; chmn. of comtees., legis. assem., 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Mem. house of assem. | South Australia | [1905] |
| 1 | 1887–1889 | comsnr. of pub. wks. | — | [1905] |
| 2 | 1890–1890 | chmn. of comtees., legis. assem. | — | [1905] |

## Candidate stint `Catt, Alfred___South Australia___1888`

- Staff-list name: **Catt, Alfred** | colony: **South Australia** | listed 1888–1894 | editions [1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Hon. Alfred Catt, M.P. | Commissioner of Public Works | Executive Council | — | — |
| 1889 | Alfred Catt | Commissioner of Public Works | Commissioner of Public Works Department | — | — |
| 1889 | Hon. Alfred Catt | Commissioner of Public Works | Executive Council | — | — |
| 1894 | Alfred Catt | Chairman of Committees | House of Assembly | — | — |

### Deterministic checks: `catti_a_e1881` vs `Catt, Alfred___South Australia___1888`

- [PASS] surname_gate: bio 'CATTI' vs stint 'Catt, Alfred' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1894
- [FAIL] position_sim: best 45 vs bar 60: 'Mem. house of assem.' ~ 'Chairman of Committees'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Catt, Alfred___South Australia___1898`

- Staff-list name: **Catt, Alfred** | colony: **South Australia** | listed 1898–1906 | editions [1898, 1899, 1900, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Hon. Alfred Catt | Chairman of Committees | House of Assembly | — | — |
| 1899 | Hon. Alfred Catt | Chairman of Committees | House of Assembly | — | — |
| 1900 | Alfred Catt | Chairman of Committees, House of Assembly | House of Assembly | — | — |
| 1906 | A. Catt | Member | House of Assembly | — | — |

### Deterministic checks: `catti_a_e1881` vs `Catt, Alfred___South Australia___1898`

- [PASS] surname_gate: bio 'CATTI' vs stint 'Catt, Alfred' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1906
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

