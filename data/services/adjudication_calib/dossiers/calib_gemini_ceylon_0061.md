<!-- {"case_id": "calib_gemini_ceylon_0061", "bio_ids": ["hartley_chas_e1896"], "stint_ids": ["Hartley, C___Ceylon___1899"]} -->
# Dossier calib_gemini_ceylon_0061

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 35 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hartley_chas_e1896'] carry a single initial only — the namesake trap applies.

## Biography `hartley_chas_e1896`

- Printed name: **HARTLEY, CHAS**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1905-L43703.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1918, 1919, 1920, 1921]:**

> HARTLEY, CHAS.—M.A., Cantab.; lecturer in English and modern languages, Royal Coll., Ceylon, 11th Dec., 1896; principal, Royal Coll., 23rd June, 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | lecturer in English and modern languages, Royal Coll. | Ceylon | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1918, 1919, 1920, 1921] |
| 1 | 1903 | principal, Royal Coll | Ceylon *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1918, 1919, 1920, 1921] |

## Candidate stint `Hartley, C___Ceylon___1899`

- Staff-list name: **Hartley, C** | colony: **Ceylon** | listed 1899–1920 | editions [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | C. Hartley | Lecturer in English and Modern Languages, Royal College | Public Instructor | — | — |
| 1900 | C. Hartley | Lecturer in English and Modern Languages, Royal College | Department of Public Instruction | — | — |
| 1905 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1906 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1907 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1908 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1909 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1910 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1911 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1912 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1913 | C. Hartley | Principal of the Royal College | Department of Public Instruction | — | — |
| 1914 | C. Hartley | Principal of the Royal College | Education Department | — | — |
| 1915 | C. Hartley | Principal of the Royal College | Education Department | — | — |
| 1917 | C. Hartley | Principal of the Royal College | Education Department | — | — |
| 1918 | C. Hartley | Principal of the Royal College | Education Department | — | — |
| 1919 | C. Hartley | Principal of the Royal College | Education Department | — | — |
| 1920 | C. Hartley | Principal of the Royal College | Education Department | — | — |

### Deterministic checks: `hartley_chas_e1896` vs `Hartley, C___Ceylon___1899`

- [PASS] surname_gate: bio 'HARTLEY' vs stint 'Hartley, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1899-1920
- [PASS] position_sim: best 97 vs bar 60: 'lecturer in English and modern languages, Royal Coll.' ~ 'Lecturer in English and Modern Languages, Royal College'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 11 agreeing edition-year(s) [1905, 1906, 1907, 1908, 1909, 1910] pos~86 (bar: >=2)
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

