<!-- {"case_id": "case_adolphus_g-a_e1890", "bio_ids": ["adolphus_g-a_e1890"], "stint_ids": ["Adolphus, G. A___Gold Coast___1894"]} -->
# Dossier case_adolphus_g-a_e1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `adolphus_g-a_e1890`

- Printed name: **ADOLPHUS, G. A**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1905-L41727.v` — printed in editions [1905, 1906, 1907, 1908, 1909]:**

> ADOLPHUS, G. A.—Supervisor of customs Gold Coast Col., 1890; asst. treasr., July, 1896; ag. on several occasions as dist. comsnr., Axim and C. C. Castle; asst. treasr., Northern Nigeria, July, 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | Supervisor of customs Gold Coast Col | — | [1905, 1906, 1907, 1908, 1909] |
| 1 | 1896 | asst. treasr | — | [1905, 1906, 1907, 1908, 1909] |
| 2 | 1900 | asst. treasr. | Northern Nigeria | [1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Adolphus, G. A___Gold Coast___1894`

- Staff-list name: **Adolphus, G. A** | colony: **Gold Coast** | listed 1894–1900 | editions [1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | G. A. Adolphus | First Class Supervisors | Customs | — | — |
| 1896 | G. A. Adolphus | First-Class Supervisor | Customs | — | — |
| 1897 | G. A. Adolphus | Assistant Treasurer | Treasury | — | — |
| 1898 | G. A. Adolphus | Assistant Treasurers | Treasury | — | — |
| 1899 | G. A. Adolphus | Assistant Treasurer | Treasury | — | — |
| 1900 | G. A. Adolphus | Assistant Treasurer | Treasury | — | — |

### Deterministic checks: `adolphus_g-a_e1890` vs `Adolphus, G. A___Gold Coast___1894`

- [PASS] surname_gate: bio 'ADOLPHUS' vs stint 'Adolphus, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
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

