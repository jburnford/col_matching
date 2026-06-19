<!-- {"case_id": "calib_gemini_jamaica_0155", "bio_ids": ["bicknell_h-j_e1860"], "stint_ids": ["Bicknell, H. J___Jamaica___1877"]} -->
# Dossier calib_gemini_jamaica_0155

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bicknell_h-j_e1860`

- Printed name: **BICKNELL, H. J**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1896, 1898]

### Verbatim printed entry text (OCR)

**Version `col1886-L32179.v` — printed in editions [1886, 1888, 1896, 1898]:**

> BICKNELL, H. J.—Police magistrate, Kingston, Jamaica, Mar., 1860; acting judge, eastern district, Oct., 1882; R.M., St. Catherine, April, 1888.

**Version `col1889-L31823.v` — printed in editions [1889, 1890]:**

> BICKNELL, H. J.—Police magistrate, Kingston, Jamaica, Mar., 1860; acting judge, eastern district, Oct., 1882; resident magistrate, St. Catherine, April, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | Police magistrate, Kingston | Jamaica | [1886, 1888, 1889, 1890, 1896, 1898] |
| 1 | 1882 | acting judge, eastern district | Jamaica *(inherited from previous clause)* | [1886, 1888, 1889, 1890, 1896, 1898] |
| 2 | 1888 | R.M., St. Catherine | Jamaica *(inherited from previous clause)* | [1886, 1888, 1889, 1890, 1896, 1898] |

## Candidate stint `Bicknell, H. J___Jamaica___1877`

- Staff-list name: **Bicknell, H. J** | colony: **Jamaica** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1878 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1879 | H. J. Bicknell | Police Magistrate | District Courts | — | — |
| 1880 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1883 | H. J. Bicknell | Police Magistrate, Kingston | Judicial Establishment | — | — |
| 1886 | H. J. Bicknell | Police Magistrate | District Courts | — | — |
| 1888 | H. J. Bicknell | Police Magistrate | Judicial Establishment | — | — |
| 1889 | H. J. Bicknell | Resident Magistrate | Resident Magistrates | — | — |
| 1890 | H. J. Bicknell, Esq. | Resident Magistrate | Judicial Establishment | — | — |

### Deterministic checks: `bicknell_h-j_e1860` vs `Bicknell, H. J___Jamaica___1877`

- [PASS] surname_gate: bio 'BICKNELL' vs stint 'Bicknell, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1877-1890
- [PASS] position_sim: best 100 vs bar 60: 'Police magistrate, Kingston' ~ 'Police Magistrate'
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

