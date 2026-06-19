<!-- {"case_id": "calib_gemini_ceylon_0058", "bio_ids": ["donnan_j_b1837"], "stint_ids": ["Donnan, J___Ceylon___1877"]} -->
# Dossier calib_gemini_ceylon_0058

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['donnan_j_b1837'] carry a single initial only — the namesake trap applies.

## Biography `donnan_j_b1837`

- Printed name: **DONNAN, J**
- Birth year: 1837 (attested in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1910, 1911, 1912, 1913, 1914, 1915])
- Honours: C.M.G (1902)
- Terminal: retired 1902 — “retired, 1902.”
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1888-L33129.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1910, 1911, 1912, 1913, 1914, 1915]:**

> DONNAN, J., C.M.G. (1902).—B. 1837; mast. attendant, Colombo, Ceylon, 1863; was comanr. of govt. steamers, "Manchester" and "Pearl," from July, 1859; ret., 1902.

**Version `col1905-L42930.v` — printed in editions [1905, 1906, 1907, 1908, 1909]:**

> DONNAN, J., C.M.G. (1902).—B. 1837; mast. attendant, Colombo, Ceylon, 1863; was comdr. of govt. steamers, "Manchester" and "Pearl," from July 1859; retired, 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859 | was comanr. of govt. steamers, "Manchester" and "Pearl," from | Ceylon *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1863 | mast. attendant, Colombo | Ceylon | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1902 | ret | Ceylon *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Donnan, J___Ceylon___1877`

- Staff-list name: **Donnan, J** | colony: **Ceylon** | listed 1877–1900 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1878 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1879 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1880 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1883 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1886 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1888 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1889 | J. Donnan | Muster Attendant | Harbour Department | — | — |
| 1890 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1894 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1896 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1898 | J. Donnan | Master Attendants | Harbour Department | — | — |
| 1899 | J. Donnan | Master Attendant | Harbour Department | — | — |
| 1900 | J. Donnan | Master Attendant | Harbour Department | — | — |

### Deterministic checks: `donnan_j_b1837` vs `Donnan, J___Ceylon___1877`

- [PASS] surname_gate: bio 'DONNAN' vs stint 'Donnan, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877, birth 1837 (age 40)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1900
- [PASS] position_sim: best 74 vs bar 60: 'mast. attendant, Colombo' ~ 'Master Attendant'
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

