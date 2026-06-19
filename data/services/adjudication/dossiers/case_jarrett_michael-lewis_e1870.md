<!-- {"case_id": "case_jarrett_michael-lewis_e1870", "bio_ids": ["jarrett_michael-lewis_e1870"], "stint_ids": ["Jarrett, M. L___Sierra Leone___1880"]} -->
# Dossier case_jarrett_michael-lewis_e1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jarrett_michael-lewis_e1870`

- Printed name: **JARRETT, MICHAEL LEWIS**
- Birth year: not printed
- Honours: L.R.C.P, M.R.C.S
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Verbatim printed entry text (OCR)

**Version `col1883-L28140.v` — printed in editions [1883, 1886]:**

> JARRETT, MICHAEL LEWIS, M.R.C.S., Lond., L.R.C.P., Edin.—Acted as assistant colonial surgeon, Sherbro, West Africa, 1870; justice of the peace for Sherbro, 1878; appointed assistant colonial surgeon, Sherbro, 1882.

**Version `col1888-L34209.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> JARRETT, MICHAEL LEWIS, M.R.C.S., Lond., L.R.C.P., Edin.—Acted as assistant colonial surgeon, Sherbro, West Africa, 1870; confirmed, 1882; is a J.P.

**Version `col1898-L34123.v` — printed in editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]:**

> JARRETT, MICHAEL LEWIS, M.R.C.S., Lond., L.R.C.P., Edin.—Acted as asst. col. surg., Sherbro, W. Africa, 1870; confirmed, 1882; is a J.P.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870 | Acted as assistant colonial surgeon, Sherbro | West Africa | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1870 | Acted as asst. col. surg., Sherbro, W. Africa | — | [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 2 | 1878 | justice of the peace for Sherbro | West Africa *(inherited from previous clause)* | [1883, 1886] |
| 3 | 1882 | appointed assistant colonial surgeon, Sherbro | West Africa *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 4 | 1882 | confirmed | — | [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |

## Candidate stint `Jarrett, M. L___Sierra Leone___1880`

- Staff-list name: **Jarrett, M. L** | colony: **Sierra Leone** | listed 1880–1900 | editions [1880, 1883, 1886, 1888, 1889, 1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | M. L. Jarrett | Assistant Colonial Surgeon | Medical | — | — |
| 1883 | M. L. Jarrett | Assistant Colonial Surgeon | Medical | — | — |
| 1886 | M. L. Jarrett | Assistant Colonial Surgeon | Sherbro | — | — |
| 1888 | M. L. Jarrett | Assistant Colonial Surgeon | Medical Establishment | — | — |
| 1889 | M. L. Jarrett | Assistant Colonial Surgeon | Medical Establishment | — | — |
| 1894 | M. L. Jarrett | Assistant Colonial Surgeon | Medical Department | — | — |
| 1894 | M. L. Jarrett | Sherbro District | — | — | — |
| 1896 | M. L. Jarrett | Assistant Colonial Surgeon | Medical Department | — | — |
| 1896 | M. L. Jarrett | Sherbro District | — | — | — |
| 1898 | M. L. Jarrett | Sherbro District | — | — | — |
| 1898 | M. L. Jarrett | Assistant Colonial Surgeon | Medical Department | — | — |
| 1899 | M. L. Jarrett | Sherbro District | — | — | — |
| 1899 | M. L. Jarrett | Assistant Colonial Surgeon | Medical Department | — | — |
| 1900 | M. L. Jarrett | Sherbro District | Registrar of Births, Deaths, and Marriages | — | — |

### Deterministic checks: `jarrett_michael-lewis_e1870` vs `Jarrett, M. L___Sierra Leone___1880`

- [PASS] surname_gate: bio 'JARRETT' vs stint 'Jarrett, M. L' (exact)
- [PASS] initials: bio ['M', 'L'] ~ stint ['M', 'L']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1900
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

