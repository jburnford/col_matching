<!-- {"case_id": "case_rowland_j-w_b1852", "bio_ids": ["rowland_j-w_b1852", "rowland_j-w_e1880"], "stint_ids": ["Rowland, J. W___Lagos___1889"]} -->
# Dossier case_rowland_j-w_b1852

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Rowland, J. W___Lagos___1889'] have more than one claimant biography in this case.

## Biography `rowland_j-w_b1852`

- Printed name: **ROWLAND, J. W**
- Birth year: 1852 (attested in editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921])
- Honours: C.M.G (1897)
- Terminal: retired 1897 — “retired, 1897.”
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1888-L35845.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> ROWLAND, J. W.—Assistant colonial surgeon, Gold Coast Colony, 15 May, 1880; district commissioner, Lagos, 1887; colonial surgeon, 1887.

**Version `col1898-L35705.v` — printed in editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> ROWLAND, J. W., C.M.G. (1897).—B., 1852; asst. col. surg., G. Coast Coll., May, 1880; dist. consmr., Lagos, 1887; col. surg., 1887; retired, 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Assistant colonial surgeon | Gold Coast | [1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1880 | asst. col. surg., G. Coast Coll | — | [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1887 | district commissioner | Lagos | [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Biography `rowland_j-w_e1880`

- Printed name: **ROWLAND, J. W**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L35558.v` — printed in editions [1886]:**

> ROWLAND, J. W.—Assistant colonial surgeon, Gold Coast Colony, 15 May, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Assistant colonial surgeon | Gold Coast | [1886] |

## Candidate stint `Rowland, J. W___Lagos___1889`

- Staff-list name: **Rowland, J. W** | colony: **Lagos** | listed 1889–1897 | editions [1889, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. W. Rowland | Colonial Surgeon and Health Officer | Medical Department | — | — |
| 1896 | J. W. Rowland | Colonial Surgeon and Health Officer | Medical | — | — |
| 1897 | J. W. Rowland | Chief Medical Officer | Medical | — | — |

### Deterministic checks: `rowland_j-w_b1852` vs `Rowland, J. W___Lagos___1889`

- [PASS] surname_gate: bio 'ROWLAND' vs stint 'Rowland, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1889, birth 1852 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Lagos'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1897
- [FAIL] position_sim: best 38 vs bar 60: 'district commissioner' ~ 'Chief Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `rowland_j-w_e1880` vs `Rowland, J. W___Lagos___1889`

- [PASS] surname_gate: bio 'ROWLAND' vs stint 'Rowland, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Lagos'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1897
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

