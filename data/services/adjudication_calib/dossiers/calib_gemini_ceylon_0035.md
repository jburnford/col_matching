<!-- {"case_id": "calib_gemini_ceylon_0035", "bio_ids": ["spence_j-b_e1886"], "stint_ids": ["Spence, J. B___Ceylon___1888"]} -->
# Dossier calib_gemini_ceylon_0035

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 57 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `spence_j-b_e1886`

- Printed name: **SPENCE, J. B**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1896-L41446.v` — printed in editions [1896, 1897]:**

> SPENCE, J. B.—Medical superintendent of Colombo lunatic asylum, Ceylon, 1886.

**Version `col1898-L36033.v` — printed in editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]:**

> SPENCE, J. B.—Med. supt. of Colombo lun. asyl., Ceylon, 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886 | Medical superintendent of Colombo lunatic asylum | Ceylon | [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Spence, J. B___Ceylon___1888`

- Staff-list name: **Spence, J. B** | colony: **Ceylon** | listed 1888–1913 | editions [1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. B. Spence | Surgeon Lunatic Asylum | Medical Department | — | — |
| 1889 | J. B. Spence | Surgeon Lunatic Asylum | Medical Department | — | — |
| 1890 | J. B. Spence | Surgeon Lunatic Asylum | Medical Department | — | — |
| 1894 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1896 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1898 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1899 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1900 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1905 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1906 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1907 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1908 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1909 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1910 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1911 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1912 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |
| 1913 | J. B. Spence | Medical Superintendent, Lunatic Asylum | Medical Department | — | — |

### Deterministic checks: `spence_j-b_e1886` vs `Spence, J. B___Ceylon___1888`

- [PASS] surname_gate: bio 'SPENCE' vs stint 'Spence, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1913
- [PASS] position_sim: best 100 vs bar 60: 'Medical superintendent of Colombo lunatic asylum' ~ 'Medical Superintendent, Lunatic Asylum'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1896, 1898, 1899, 1900] pos~100 (bar: >=2)
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

