<!-- {"case_id": "calib_gemini_newfoundland_0300", "bio_ids": ["conroy_j-g_e1880"], "stint_ids": ["Conroy, J. G___Newfoundland___1889"]} -->
# Dossier calib_gemini_newfoundland_0300

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `conroy_j-g_e1880`

- Printed name: **CONROY, J. G**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917]

### Verbatim printed entry text (OCR)

**Version `col1888-L32776.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917]:**

> CONROY, J. G.—Central District Court judge, Newfoundland, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Central District Court judge | Newfoundland | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917] |

## Candidate stint `Conroy, J. G___Newfoundland___1889`

- Staff-list name: **Conroy, J. G** | colony: **Newfoundland** | listed 1889–1915 | editions [1889, 1894, 1896, 1897, 1898, 1899, 1900, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. G. Conroy | Central District Court Judges | Judicial Establishment | — | — |
| 1894 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1896 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1897 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1898 | J. G. Conroy | Central District Court Judge | NEWFOUNDLAND—NEW SOUTH WALES | — | — |
| 1899 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1900 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1906 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1907 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1908 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1909 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1910 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1911 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1912 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1913 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1914 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |
| 1915 | J. G. Conroy | Central District Court Judge | Judicial Establishment | — | — |

### Deterministic checks: `conroy_j-g_e1880` vs `Conroy, J. G___Newfoundland___1889`

- [PASS] surname_gate: bio 'CONROY' vs stint 'Conroy, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1915
- [PASS] position_sim: best 100 vs bar 60: 'Central District Court judge' ~ 'Central District Court Judge'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1889, 1894] pos~99 (bar: >=2)
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

