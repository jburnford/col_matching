<!-- {"case_id": "case_rosellotty_j-c_e1864", "bio_ids": ["rosellotty_j-c_e1864"], "stint_ids": ["Rosselloty, J. C___Western Australia___1879", "Rosselloty, J. C___Western Australia___1889"]} -->
# Dossier case_rosellotty_j-c_e1864

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Rosselloty, J. C___Western Australia___1879` is also gate-compatible with biography(ies) outside this case: ['rossellotty_j-c_e1864'] (already linked elsewhere or filtered).
- NOTE: stint `Rosselloty, J. C___Western Australia___1889` is also gate-compatible with biography(ies) outside this case: ['rossellotty_j-c_e1864'] (already linked elsewhere or filtered).

## Biography `rosellotty_j-c_e1864`

- Printed name: **ROSELLOTTY, J. C**
- Birth year: not printed
- Appears in editions: [1888, 1890, 1894, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L35831.v` — printed in editions [1888, 1890, 1894]:**

> ROSELLOTTY, J. C.—Medical officer of the Sussex district, Western Australia, June, 1864; resident magistrate and medical officer of Williams and Kajimpi districts, 1876.

**Version `col1898-L35691.v` — printed in editions [1898]:**

> ROSELLOTTY, J. C.—Med. offr., Sussex dist., W. Australia, June, 1864; res. mag. and med. offr., Williams and Kajaiimp dists., 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Medical officer of the Sussex district | Western Australia | [1888, 1890, 1894] |
| 1 | 1864 | Med. offr., Sussex dist., W. Australia | — | [1898] |
| 2 | 1876 | resident magistrate and medical officer of Williams and Kajimpi districts | Western Australia *(inherited from previous clause)* | [1888, 1890, 1894] |
| 3 | 1876 | res. mag. and med. offr., Williams and Kajaiimp dists | — | [1898] |

## Candidate stint `Rosselloty, J. C___Western Australia___1879`

- Staff-list name: **Rosselloty, J. C** | colony: **Western Australia** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | J. C. Rosselloty | Resident Magistrate, Williams District | Judicial Department | — | — |
| 1879 | J. C. Rosselloty | District Medical Officer | Medical Department | — | — |
| 1880 | J. C. Rosselloty | Resident Magistrate | Judicial Department | — | — |

### Deterministic checks: `rosellotty_j-c_e1864` vs `Rosselloty, J. C___Western Australia___1879`

- [PASS] surname_gate: bio 'ROSELLOTTY' vs stint 'Rosselloty, J. C' (fuzzy:2)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Western Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1880
- [PASS] position_sim: best 100 vs bar 60: 'resident magistrate and medical officer of Williams and Kajimpi districts' ~ 'Resident Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Rosselloty, J. C___Western Australia___1889`

- Staff-list name: **Rosselloty, J. C** | colony: **Western Australia** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. C. Rosselloty | Chairman of Quarter Sessions | Chairmen of Quarter Sessions | — | — |
| 1889 | J. C. Rosselloty | District Medical Officer | Medical Department | — | — |
| 1890 | J. C. Rosselloty | Police Magistrate | Judicial Department | — | — |
| 1890 | J. C. Rosselloty | District Medical Officer | Medical Department | — | — |

### Deterministic checks: `rosellotty_j-c_e1864` vs `Rosselloty, J. C___Western Australia___1889`

- [PASS] surname_gate: bio 'ROSELLOTTY' vs stint 'Rosselloty, J. C' (fuzzy:2)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Western Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1890
- [PASS] position_sim: best 77 vs bar 60: 'resident magistrate and medical officer of Williams and Kajimpi districts' ~ 'District Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1890] pos~77 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

