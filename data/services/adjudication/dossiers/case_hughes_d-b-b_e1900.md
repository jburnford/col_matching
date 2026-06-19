<!-- {"case_id": "case_hughes_d-b-b_e1900", "bio_ids": ["hughes_d-b-b_e1900"], "stint_ids": ["Hughes, D. B. B___Grenada___1910", "Hughes, D. B. B___Windward Islands___1905"]} -->
# Dossier case_hughes_d-b-b_e1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 122 official(s) with this surname in the graph's staff lists; 39 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hughes_d-b-b_e1900`

- Printed name: **HUGHES, D. B. B**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1905-L43883.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927]:**

> HUGHES, D. B. B., M.B.C.M. (Edin.).—1st prizeman, senior surgery; medallist, anatomy and pathology; ag. surg. in charge, col. hosp., Grenada, 1900; dist. med. offr., Saint Vincent, Dec., 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | ag. surg. in charge, col. hosp. | Grenada | [1905, 1906, 1907, 1908, 1909, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927] |

## Candidate stint `Hughes, D. B. B___Grenada___1910`

- Staff-list name: **Hughes, D. B. B** | colony: **Grenada** | listed 1910–1932 | editions [1910, 1911, 1912, 1917, 1921, 1927, 1929, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | D. Hughes | Medical Officer, District No. 10 | Medical | — | — |
| 1911 | D. Hughes | Medical Officer, District No. 10 | Medical | — | — |
| 1912 | D. Hughes | Medical Officer, District No. 5 | Medical | — | — |
| 1917 | D. B. Hughes | Medical Officer, District No. 9 | Medical | — | — |
| 1921 | D. B. B. Hughes | District Medical Officer | Medical | — | — |
| 1927 | D. B. B. Hughes | District Medical Officer | Medical | — | — |
| 1929 | D. B. B. Hughes | District Medical Officers | Medical | — | — |
| 1932 | D. B. B. Hughes | District Medical Officer | Medical | — | — |

### Deterministic checks: `hughes_d-b-b_e1900` vs `Hughes, D. B. B___Grenada___1910`

- [PASS] surname_gate: bio 'HUGHES' vs stint 'Hughes, D. B. B' (exact)
- [PASS] initials: bio ['D', 'B', 'B'] ~ stint ['D', 'B', 'B']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Grenada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1910-1932
- [FAIL] position_sim: best 36 vs bar 60: 'ag. surg. in charge, col. hosp.' ~ 'Medical Officer, District No. 9'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hughes, D. B. B___Windward Islands___1905`

- Staff-list name: **Hughes, D. B. B** | colony: **Windward Islands** | listed 1905–1925 | editions [1905, 1906, 1907, 1908, 1913, 1914, 1915, 1919, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | D. Hughes | Medical Officer, District No. 10 | Medical | — | — |
| 1906 | D. Hughes | Medical Officer, District No. 10 | Medical | — | — |
| 1907 | D. Hughes | Medical Officer, District No. 10 | Medical | — | — |
| 1908 | D. Hughes | Medical Officer, District No. 10 | Medical | — | — |
| 1913 | D. Hughes | Medical Officer, District No. 5 | Medical | — | — |
| 1914 | D. Hughes | Medical Officer, District No. 5 | Medical | — | — |
| 1915 | D. B. Hughes | Medical Officer, District No. 9 | Medical | — | — |
| 1919 | D. B. B. Hughes | District Medical Officer | Medical | — | — |
| 1922 | D. B. B. Hughes | District Medical Officers | Medical | — | — |
| 1923 | D. B. B. Hughes | District Medical Officer | Medical | — | — |
| 1924 | D. B. B. Hughes | District Medical Officer | Medical | — | — |
| 1925 | D. B. B. Hughes | District Medical Officers | Medical | — | — |

### Deterministic checks: `hughes_d-b-b_e1900` vs `Hughes, D. B. B___Windward Islands___1905`

- [PASS] surname_gate: bio 'HUGHES' vs stint 'Hughes, D. B. B' (exact)
- [PASS] initials: bio ['D', 'B', 'B'] ~ stint ['D', 'B', 'B']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1925
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

