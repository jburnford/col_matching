<!-- {"case_id": "case_pugh_j_e1910", "bio_ids": ["pugh_j_e1910"], "stint_ids": ["Pugh, J___Kenya___1911"]} -->
# Dossier case_pugh_j_e1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pugh_j_e1910'] carry a single initial only — the namesake trap applies.
- Phase 1 found `pugh_j_e1910` ↔ `Pugh, J___Kenya___1911` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Pugh, J___Kenya___1911` is also gate-compatible with biography(ies) outside this case: ['pugh_john_e1910'] (already linked elsewhere or filtered).

## Biography `pugh_j_e1910`

- Printed name: **PUGH, J**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1912-L47045.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928]:**

> PUGH, J.—Med. offr., E.A.P., Jan., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | Med. offr. | East Africa Protectorate | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928] |

## Candidate stint `Pugh, J___Kenya___1911`

- Staff-list name: **Pugh, J** | colony: **Kenya** | listed 1911–1925 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1919, 1920, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | J. Pugh | Sleeping Sickness | Medical (East Africa and Uganda) | — | — |
| 1912 | J. Pugh | Sleeping Sickness | Medical (East Africa and Uganda) | — | — |
| 1913 | J. Pugh | Sleeping Sickness | Medical | — | — |
| 1914 | J. Pugh | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1915 | J. Pugh | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1917 | J. Pugh | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1919 | J. Pugh | Medical Officers | Medical (East Africa and Uganda) | — | — |
| 1920 | J. Pugh | Medical Officers | Medical (East Africa and Uganda) | — | — |
| 1922 | J. Pugh | Senior Medical Officer | Medical | — | — |
| 1923 | J. Pugh | Senior Medical Officer | Medical | — | — |
| 1924 | J. Pugh | Senior Medical Officer | Medical | — | — |
| 1925 | J. Pugh | Senior Medical Officer | Medical Department | — | — |

### Deterministic checks: `pugh_j_e1910` vs `Pugh, J___Kenya___1911`

- [PASS] surname_gate: bio 'PUGH' vs stint 'Pugh, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1925
- [PASS] position_sim: best 70 vs bar 60: 'Med. offr.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 5 agreeing edition-year(s) [1914, 1915, 1917, 1919, 1920] pos~68 (bar: >=2)
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

