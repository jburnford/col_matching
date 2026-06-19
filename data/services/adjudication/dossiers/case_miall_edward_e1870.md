<!-- {"case_id": "case_miall_edward_e1870", "bio_ids": ["miall_edward_e1870"], "stint_ids": ["Miall, Edward___Canada___1877"]} -->
# Dossier case_miall_edward_e1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['miall_edward_e1870'] carry a single initial only — the namesake trap applies.

## Biography `miall_edward_e1870`

- Printed name: **MIALL, EDWARD**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1898-L34822.v` — printed in editions [1898, 1899, 1900, 1905, 1906]:**

> MIALL, EDWARD.—Entered public service, Canada, 1870; asst. comsnr. inld. rev., 1872; attended fishery comsnr., Halifax, 1877; mem. of Pacific Rly. comsnr. of inquiry, 1880-1; dep. min., comsnr. of inld. rev., and comsnr. of standards, Jan., 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870 | Entered public service | Canada | [1898, 1899, 1900, 1905, 1906] |
| 1 | 1872 | asst. comsnr. inld. rev | Canada *(inherited from previous clause)* | [1898, 1899, 1900, 1905, 1906] |
| 2 | 1877 | attended fishery comsnr., Halifax | Canada *(inherited from previous clause)* | [1898, 1899, 1900, 1905, 1906] |
| 3 | 1880–1881 | mem. of Pacific Rly. comsnr. of inquiry | Canada *(inherited from previous clause)* | [1898, 1899, 1900, 1905, 1906] |
| 4 | 1883 | dep. min., comsnr. of inld. rev., and comsnr. of standards | Canada *(inherited from previous clause)* | [1898, 1899, 1900, 1905, 1906] |

## Candidate stint `Miall, Edward___Canada___1877`

- Staff-list name: **Miall, Edward** | colony: **Canada** | listed 1877–1900 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Edward Miall, Jr. | Assistant Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1878 | Edward Miall, Jr. | Assistant Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1879 | Edward Miall, Jr. | Assistant Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1880 | Edward Miall | Assistant Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1883 | Edward Miall | Assistant Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1886 | Edward Miall | Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1888 | Edward Miall | Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1889 | Edward Miall | Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1890 | Edward Miall | Commissioner of Inland Revenue | Inland Revenue Department | — | — |
| 1894 | E. Miall | Commissioner of Inland Revenue | Department of Inland Revenue | — | — |
| 1896 | E. Miall | Commissioner of Inland Revenue | Department of Inland Revenue | — | — |
| 1897 | E. Miall | Commissioner of Inland Revenue | Department of Inland Revenue | — | — |
| 1898 | E. Miall | Commissioner of Inland Revenue | Department of Inland Revenue | — | — |
| 1900 | E. Miall | Commissioner of Inland Revenue | Department of Inland Revenue | — | — |

### Deterministic checks: `miall_edward_e1870` vs `Miall, Edward___Canada___1877`

- [PASS] surname_gate: bio 'MIALL' vs stint 'Miall, Edward' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1877-1900
- [PASS] position_sim: best 67 vs bar 60: 'asst. comsnr. inld. rev' ~ 'Assistant Commissioner of Inland Revenue'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

