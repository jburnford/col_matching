<!-- {"case_id": "case_newton_henry-hibbert_b1861", "bio_ids": ["newton_henry-hibbert_b1861"], "stint_ids": ["Newton, H. H___Australia___1912", "Newton, H___New South Wales___1889"]} -->
# Dossier case_newton_henry-hibbert_b1861

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `newton_henry-hibbert_b1861`

- Printed name: **NEWTON, HENRY HIBBERT**
- Birth year: 1861 (attested in editions [1915, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925])
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1915-L49428.v` — printed in editions [1915, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> NEWTON, HENRY HIBBERT.—B. 1861; entd. law dept., Victoria, 1880; joined staff of legis. assem., 1884; clk. astt., 1902; clk. of legis. assem., 1910; and clk. of parlms.

**Version `col1917-L52134.v` — printed in editions [1917]:**

> NEWTON, Henry Hibbert.—B. 1861; educated at law department, Victoria, 1880; joined staff of legislative assembly, 1884; clerk assistant, 1902; clerk of legislative assembly, 1910; and clerk of parliament.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | entd. law dept. | Victoria | [1915, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1884 | joined staff of legis. assem | Victoria *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1902 | clk. astt | Victoria *(inherited from previous clause)* | [1915, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1902 | clerk assistant | — | [1917] |
| 4 | 1910 | clk. of legis. assem | Victoria *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Newton, H. H___Australia___1912`

- Staff-list name: **Newton, H. H** | colony: **Australia** | listed 1912–1927 | editions [1912, 1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | H. H. Newton | Clerk of the Assembly | Legislative Assembly | — | — |
| 1913 | H. H. Newton | Clerk of the Assembly | Parliamentary Staff | — | — |
| 1918 | H. H. Newton | Clerk of the Parliaments and Clerk of the Assembly | Legislative Assembly | — | — |
| 1927 | H. H. Newton | Clerk of the Council | Legislative Council | — | — |

### Deterministic checks: `newton_henry-hibbert_b1861` vs `Newton, H. H___Australia___1912`

- [PASS] surname_gate: bio 'NEWTON' vs stint 'Newton, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1912, birth 1861 (age 51)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Newton, H___New South Wales___1889`

- Staff-list name: **Newton, H** | colony: **New South Wales** | listed 1889–1906 | editions [1889, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | H. Newton | Harbour Master, Newcastle | Marine Board | — | — |
| 1894 | H. Newton | Harbour Master | Marine Board | — | — |
| 1896 | H. Newton | Harbour Master | Marine Board | — | — |
| 1897 | H. Newton | Harbour Master | Harbour Master | — | — |
| 1898 | H. Newton | Harbour Master | Marine Board | — | — |
| 1899 | H. Newton | Harbour Master | Marine Board | — | — |
| 1900 | H. Newton | Harbour Master | Marine Board | — | — |
| 1905 | H. Newton | Deputy-Superintendent | Department of Navigation | — | — |
| 1906 | H. Newton | Deputy-Superintendent | Department of Navigation | — | — |

### Deterministic checks: `newton_henry-hibbert_b1861` vs `Newton, H___New South Wales___1889`

- [PASS] surname_gate: bio 'NEWTON' vs stint 'Newton, H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1889, birth 1861 (age 28)
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1906
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

