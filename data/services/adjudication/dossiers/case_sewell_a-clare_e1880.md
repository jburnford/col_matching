<!-- {"case_id": "case_sewell_a-clare_e1880", "bio_ids": ["sewell_a-clare_e1880"], "stint_ids": ["Sewell, A. C___Natal___1886"]} -->
# Dossier case_sewell_a-clare_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sewell_a-clare_e1880`

- Printed name: **SEWELL, A. CLARE**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1888-L35993.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> SEWELL, A. CLARE.—Extra clerk, native high court, Natal, Mar., 1880; acting prosecutor, Jan., 1882; acting second clerk, attorney general's office, April, 1882; acting first clerk, Aug., 1882; acting sub-auditor, railway department, Dec., 1882; confirmed, Mar., 1882.

**Version `col1898-L35867.v` — printed in editions [1898, 1899, 1900]:**

> SEWELL, A. CLARE.—Extra clk., native high ct., Natal, Mar., 1880; ag. prosecutor, Jan., 1882; ag. 2nd clk., atty.-gen.'s office, Apr., 1882; ag. 1st clk., Aug., 1882; sub-audr., rly. dept., Mar., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Extra clerk, native high court | Natal | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1882 | acting prosecutor | Natal *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Sewell, A. C___Natal___1886`

- Staff-list name: **Sewell, A. C** | colony: **Natal** | listed 1886–1900 | editions [1886, 1888, 1889, 1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | A. C. Sewell | Sub Auditor for Railway Purposes | Audit Office | — | — |
| 1888 | A. C. Sewell | Sub Auditor for Railway Purposes | Audit Office | — | — |
| 1889 | A. C. Sewell | Sub Auditor for Railway Purposes | Audit Office | — | — |
| 1894 | A. C. Sewell | Sub Auditor | Audit Office | — | — |
| 1896 | A. C. Sewell | Sub-Auditor | Audit Office | — | — |
| 1898 | A. C. Sewell | Sub-Auditor | Audit Office | — | — |
| 1899 | A. C. Sewell | Sub-Auditor | Audit Office | — | — |
| 1900 | A. C. Sewell | Sub-Auditor | Audit Office | — | — |

### Deterministic checks: `sewell_a-clare_e1880` vs `Sewell, A. C___Natal___1886`

- [PASS] surname_gate: bio 'SEWELL' vs stint 'Sewell, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1900
- [FAIL] position_sim: best 37 vs bar 60: 'acting prosecutor' ~ 'Sub-Auditor'
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

