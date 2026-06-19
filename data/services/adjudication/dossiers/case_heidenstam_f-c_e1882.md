<!-- {"case_id": "case_heidenstam_f-c_e1882", "bio_ids": ["heidenstam_f-c_e1882"], "stint_ids": ["Heidenstam, F. C___Cyprus___1905"]} -->
# Dossier case_heidenstam_f-c_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heidenstam_f-c_e1882`

- Printed name: **HEIDENSTAM, F. C**
- Birth year: not printed
- Honours: C.M.G (1884)
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1886-L33990.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1908, 1909]:**

> HEIDENSTAM, DR. F. C., C.M.G. (1884).—Chief medical officer, Cyprus, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Chief medical officer | Cyprus | [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Heidenstam, F. C___Cyprus___1905`

- Staff-list name: **Heidenstam, F. C** | colony: **Cyprus** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | F. C. Heidenstam | Chief Medical Officer | Medical Department | C.M.G. | — |
| 1906 | F. C. Heidenstam | Chief Medical Officer | Medical Department | C.M.G. | — |
| 1907 | F. C. Heidenstam | Chief Medical Officer | Medical Department | C.M.G. | — |
| 1908 | F. C. Heidenstam | Chief Medical Officer | Medical Department | C.M.G. | — |
| 1909 | F. C. Heidenstam | Chief Medical Officer | Medical Department | C.M.G. | — |

### Deterministic checks: `heidenstam_f-c_e1882` vs `Heidenstam, F. C___Cyprus___1905`

- [PASS] surname_gate: bio 'HEIDENSTAM' vs stint 'Heidenstam, F. C' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F', 'C']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
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

