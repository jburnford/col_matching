<!-- {"case_id": "case_culligan_arthur_b1879", "bio_ids": ["culligan_arthur_b1879"], "stint_ids": ["Culligan, A. A___Cape of Good Hope___1905", "Culligan, Arthur___Canada___1913"]} -->
# Dossier case_culligan_arthur_b1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['culligan_arthur_b1879'] carry a single initial only — the namesake trap applies.

## Biography `culligan_arthur_b1879`

- Printed name: **CULLIGAN, ARTHUR**
- Birth year: 1879 (attested in editions [1918, 1919, 1920, 1921, 1922, 1923])
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1918-L49676.v` — printed in editions [1918, 1919, 1920, 1921, 1922, 1923]:**

> CULLIGAN, HON. ARTHUR.—B. 1879; lumberman and farmer; elected to legis. assem., New Brunswick, 1912; min. without portfolio in Murray adminst., 1917.

**Version `col1924-L53393.v` — printed in editions [1924, 1925]:**

> CULEGAN, HON. ARTHUR.—B. 1879; lumberman and farmer; elected to legis. assem., New Brunswick, 1912; min. without portfolio in Murray admtn., 1917.

**Version `col1927-L58184.v` — printed in editions [1927]:**

> CULEIGAN, HON. ARTHUR.—B. 1879; lumberman and farmer; elected to legis. assem. New Brunswick, 1912; min. without portfolio in Murray admstr., 1917.

**Version `col1928-L65351.v` — printed in editions [1928]:**

> CULLEGAN, HON. ARTHUR.—B. 1879; lumberman and farmer; elected to legis. assem., New Brunswick, 1912; min. without portfolio in Murray admin., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | elected to legis. assem. | New Brunswick | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928] |
| 1 | 1917 | min. without portfolio in Murray adminst | New Brunswick *(inherited from previous clause)* | [1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928] |

## Candidate stint `Culligan, A. A___Cape of Good Hope___1905`

- Staff-list name: **Culligan, A. A** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. A. Culligan | Clerk | Native Affairs Branch | — | — |
| 1906 | A. A. Culligan | Clerk | Native Affairs Branch | — | — |
| 1907 | A. A. Culligan | Clerk | Native Affairs Branch | — | — |
| 1908 | A. A. Culligan | Clerk | Native Affairs Branch | — | — |
| 1909 | A. A. Culligan | Clerks | Native Affairs Branch | — | — |

### Deterministic checks: `culligan_arthur_b1879` vs `Culligan, A. A___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'CULLIGAN' vs stint 'Culligan, A. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'A']
- [PASS] age_gate: stint starts 1905, birth 1879 (age 26)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Culligan, Arthur___Canada___1913`

- Staff-list name: **Culligan, Arthur** | colony: **Canada** | listed 1913–1917 | editions [1913, 1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | Arthur Culligan | Member | Constituencies | — | — |
| 1914 | Arthur Culligan | Member | House of Assembly | — | — |
| 1915 | Arthur Culligan | — | — | — | — |
| 1917 | Arthur Culligan | Without Portfolio | Executive Council | — | — |
| 1917 | Arthur Culligan | Member | Constituencies | — | — |

### Deterministic checks: `culligan_arthur_b1879` vs `Culligan, Arthur___Canada___1913`

- [PASS] surname_gate: bio 'CULLIGAN' vs stint 'Culligan, Arthur' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1913, birth 1879 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1913-1917
- [PASS] position_sim: best 100 vs bar 60: 'min. without portfolio in Murray adminst' ~ 'Without Portfolio'
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

