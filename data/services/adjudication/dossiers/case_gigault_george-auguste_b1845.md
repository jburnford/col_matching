<!-- {"case_id": "case_gigault_george-auguste_b1845", "bio_ids": ["gigault_george-auguste_b1845"], "stint_ids": ["Gigault, George A___Canada___1879", "Gigault, George A___Canada___1906"]} -->
# Dossier case_gigault_george-auguste_b1845

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gigault_george-auguste_b1845`

- Printed name: **GIGAULT, GEORGE AUGUSTE**
- Birth year: 1845 (attested in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923, 1924])
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1911-L44952.v` — printed in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923, 1924]:**

> GIGAULT, GEORGE AUGUSTE.—B. 1845; ed. St. Hyacinthe Coll.; notary; elec. to H. of C., Canada, 1878, 1882 and 1887; dep. min. of agric., Quebec, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878–1887 | elec. to H. of C. | Canada | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923, 1924] |
| 1 | 1892 | dep. min. of agric. | Quebec | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923, 1924] |

## Candidate stint `Gigault, George A___Canada___1879`

- Staff-list name: **Gigault, George A** | colony: **Canada** | listed 1879–1890 | editions [1879, 1880, 1883, 1886, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | George A. Gigault | — | — | — | — |
| 1880 | George A. Gigault | — | — | — | — |
| 1883 | George A. Gigault | — | — | — | — |
| 1886 | George A. Gigault | — | — | — | — |
| 1889 | George A. Gigault | Member | Province of Quebec | — | — |
| 1890 | George A. Gigault | — | — | — | — |

### Deterministic checks: `gigault_george-auguste_b1845` vs `Gigault, George A___Canada___1879`

- [PASS] surname_gate: bio 'GIGAULT' vs stint 'Gigault, George A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1879, birth 1845 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1890
- [FAIL] position_sim: best 20 vs bar 60: 'elec. to H. of C.' ~ 'Member'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Gigault, George A___Canada___1906`

- Staff-list name: **Gigault, George A** | colony: **Canada** | listed 1906–1908 | editions [1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | G. A. Gigault | Deputy Minister of Agriculture | Officers of Departments | — | — |
| 1908 | G. A. Gigault | Deputy Minister of Agriculture | Officers of Departments | — | — |

### Deterministic checks: `gigault_george-auguste_b1845` vs `Gigault, George A___Canada___1906`

- [PASS] surname_gate: bio 'GIGAULT' vs stint 'Gigault, George A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1906, birth 1845 (age 61)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
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

