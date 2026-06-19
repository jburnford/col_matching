<!-- {"case_id": "calib_gemini_fiji_0092", "bio_ids": ["langford_john_e1874"], "stint_ids": ["Langford, John___Fiji___1879"]} -->
# Dossier calib_gemini_fiji_0092

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['langford_john_e1874'] carry a single initial only — the namesake trap applies.

## Biography `langford_john_e1874`

- Printed name: **LANGFORD, JOHN**
- Birth year: not printed
- Honours: I.S.O (1907)
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1889-L34130.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898, 1905, 1906, 1907, 1909, 1910]:**

> LANGFORD, JOHN, I.S.O. (1907).—Clk., col. sec.'s office, Fiji, Oct., 1874; ch. clk. and clk. of legis. coun., Jan., 1878; registr., sup. ct., and curator of intestate estates, June, 1884.

**Version `col1899-L35931.v` — printed in editions [1899]:**

> LANGFORD, JOHN.—CLK., COL. SEC.'S OFFICE, FIJI, OCT., 1874; CH. CLK. AND CLK. OF LEGIS. COUN., JAN., 1878; REGISTR. SUP. CT., AND CURATOR OF INTESTATE ESTATES, JUNE, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Clk., col. sec.'s office | Fiji | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1909, 1910] |
| 1 | 1878 | ch. clk. and clk. of legis. coun | Fiji *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1909, 1910] |
| 2 | 1884 | registr., sup. ct., and curator of intestate estates | Fiji *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906, 1907, 1909, 1910] |

## Candidate stint `Langford, John___Fiji___1879`

- Staff-list name: **Langford, John** | colony: **Fiji** | listed 1879–1906 | editions [1879, 1880, 1883, 1886, 1888, 1889, 1894, 1897, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | John Langford | First Clerk and Clerk of Council | Civil Establishment | — | — |
| 1880 | John Langford | First Clerk and Clerk of Council | — | — | — |
| 1883 | J. Langford | Clerk | — | — | — |
| 1883 | John Langford | Chief Clerk and Clerk to the Legislative Council | Colonial Secretary's Department | — | — |
| 1886 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |
| 1888 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | DEPARTMENT OF JUSTICE | — | — |
| 1889 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | DEPARTMENT OF JUSTICE | — | — |
| 1894 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |
| 1897 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |
| 1898 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |
| 1899 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |
| 1900 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |
| 1905 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |
| 1906 | John Langford | Registrar of Supreme Court, and Curator of Intestate Estates | Department of Justice | — | — |

### Deterministic checks: `langford_john_e1874` vs `Langford, John___Fiji___1879`

- [PASS] surname_gate: bio 'LANGFORD' vs stint 'Langford, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1879-1906
- [PASS] position_sim: best 100 vs bar 60: 'Clk., col. sec.'s office' ~ 'Clerk'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1889, 1894, 1897, 1898] pos~93 (bar: >=2)
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

