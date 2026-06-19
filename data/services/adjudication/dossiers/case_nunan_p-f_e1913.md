<!-- {"case_id": "case_nunan_p-f_e1913", "bio_ids": ["nunan_p-f_e1913", "nunan_p-f_e1913-2"], "stint_ids": ["Nunan, P. F___Kenya___1915"]} -->
# Dossier case_nunan_p-f_e1913

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Nunan, P. F___Kenya___1915'] have more than one claimant biography in this case.
- Phase 1 found `nunan_p-f_e1913` ↔ `Nunan, P. F___Kenya___1915` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `nunan_p-f_e1913-2` ↔ `Nunan, P. F___Kenya___1915` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `nunan_p-f_e1913`

- Printed name: **NUNAN, P. F**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1915-L49484.v` — printed in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924]:**

> NUNAN, P. F., M.B., B.A.-Surgeon, M.D.—Med. offr., E.A.P., Aug., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Med. offr. | East Africa Protectorate | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924] |

## Biography `nunan_p-f_e1913-2`

- Printed name: **NUNAN, P. F**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1927-L61746.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]:**

> NUNAN, P. F., M.B., Bsc.-Surg., M.D.—Med. offr., E.A.P., Aug., 1913; senr. med. offr., Tanganyika Territory, Nov., 1924; do., Kenya, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Med. offr. | East Africa Protectorate | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 1 | 1924 | senr. med. offr., Tanganyika Territory | Tanganyika | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 2 | 1925 | senr. med. offr., Tanganyika Territory | Kenya | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |

## Candidate stint `Nunan, P. F___Kenya___1915`

- Staff-list name: **Nunan, P. F** | colony: **Kenya** | listed 1915–1924 | editions [1915, 1917, 1919, 1920, 1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | P. F. Nunan | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1917 | P. F. Nunan | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1919 | P. F. Nunan | Medical Officers | Medical (East Africa and Uganda) | — | — |
| 1920 | P. F. Nunan | Medical Officers | Medical (East Africa and Uganda) | — | — |
| 1922 | P. F. Nunan | Medical Officer of Health | Medical | — | — |
| 1923 | P. F. Nunan | Medical Officer of Health | Medical | — | — |
| 1924 | P. F. Nunan | Medical Officer | Medical | — | — |

### Deterministic checks: `nunan_p-f_e1913` vs `Nunan, P. F___Kenya___1915`

- [PASS] surname_gate: bio 'NUNAN' vs stint 'Nunan, P. F' (exact)
- [PASS] initials: bio ['P', 'F'] ~ stint ['P', 'F']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1924
- [PASS] position_sim: best 70 vs bar 60: 'Med. offr.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 5 agreeing edition-year(s) [1915, 1917, 1919, 1920, 1924] pos~68 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `nunan_p-f_e1913-2` vs `Nunan, P. F___Kenya___1915`

- [PASS] surname_gate: bio 'NUNAN' vs stint 'Nunan, P. F' (exact)
- [PASS] initials: bio ['P', 'F'] ~ stint ['P', 'F']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1915-1924
- [PASS] position_sim: best 70 vs bar 60: 'Med. offr.' ~ 'Medical Officer'
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

