<!-- {"case_id": "calib_gemini_ceylon_0051", "bio_ids": ["greene_geoffrey-phillip_b1868"], "stint_ids": ["Greene, G. P___Ceylon___1905"]} -->
# Dossier calib_gemini_ceylon_0051

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `greene_geoffrey-phillip_b1868`

- Printed name: **GREENE, Geoffrey Phillip**
- Birth year: 1868 (attested in editions [1905, 1906, 1907, 1908, 1909, 1911, 1914, 1917, 1918, 1919, 1920, 1921, 1922, 1923])
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1905-L43509.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1911, 1914, 1917, 1918, 1919, 1920, 1921, 1922, 1923]:**

> GREENE, GEOFFREY PHILIP.—B. 1868; gen. mag., Ceylon rlyws., 11th Oct., 1901.

**Version `col1909-L46828.v` — printed in editions [1909, 1910, 1912, 1913, 1915]:**

> GREENE, Geoffrey Phillip.—B. 1868; gen. mag., Ceylon rlyws., 11th Oct., 1901.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | gen. mag., Ceylon rlyws | Ceylon | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |

## Candidate stint `Greene, G. P___Ceylon___1905`

- Staff-list name: **Greene, G. P** | colony: **Ceylon** | listed 1905–1923 | editions [1905, 1906, 1907, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | G. P. Greene | General Manager | Railway Department | — | — |
| 1906 | G. P. Greene | General Manager | Railway Department | — | — |
| 1907 | G. P. Greene | General Manager | Railway Department | — | — |
| 1909 | G. P. Greene | General Manager | Railway Department | — | — |
| 1910 | G. P. Greene | General Manager | Railway Department | — | — |
| 1911 | G. P. Greene | General Manager | Railway Department | — | — |
| 1912 | G. P. Greene | General Manager | Railway Department | — | — |
| 1913 | G. P. Greene | General Manager | Railway Department | — | — |
| 1914 | G. P. Greene | General Manager | Railway Department | — | — |
| 1915 | G. P. Greene | General Manager | Railway Department | — | — |
| 1917 | G. P. Greene | General Manager | Railway Department | — | — |
| 1918 | G. P. Greene | General Manager | Railway Department | — | — |
| 1919 | G. P. Greene | General Manager | Railway Department | — | — |
| 1920 | G. P. Greene | General Manager | Railway Department | — | — |
| 1921 | G. P. Greene | General Manager | Railway Department | — | — |
| 1922 | G. P. Greene | General Manager | Railway Department | — | — |
| 1923 | G. P. Greene | General Manager | Railway Department | — | — |

### Deterministic checks: `greene_geoffrey-phillip_b1868` vs `Greene, G. P___Ceylon___1905`

- [PASS] surname_gate: bio 'GREENE' vs stint 'Greene, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1905, birth 1868 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1923
- [PASS] position_sim: best 64 vs bar 60: 'gen. mag., Ceylon rlyws' ~ 'General Manager'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 10 agreeing edition-year(s) [1905, 1906, 1907, 1909, 1910, 1911] pos~64 (bar: >=2)
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

