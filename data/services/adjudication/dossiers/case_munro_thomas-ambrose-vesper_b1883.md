<!-- {"case_id": "case_munro_thomas-ambrose-vesper_b1883", "bio_ids": ["munro_thomas-ambrose-vesper_b1883"], "stint_ids": ["Munro, A___Jamaica___1925", "Munro, T. A. V___Bahamas___1914"]} -->
# Dossier case_munro_thomas-ambrose-vesper_b1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `munro_thomas-ambrose-vesper_b1883`

- Printed name: **MUNRO, THOMAS AMBROSE VESPER**
- Birth year: 1883 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1927-L61566.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> MUNRO, THOMAS AMBROSE VESPER.—B. 1883; harbinr., Bahamas, 1st Sept., 1913; ag. marshal, admv. sub., sup. ct., 1919.

**Version `col1915-L49348.v` — printed in editions [1915, 1917, 1919, 1920, 1921, 1922, 1923, 1924]:**

> MUNRO, THOMAS AMBROSE VESPER.—B. 1883; port offr., Bahamas, 1913.

**Version `col1918-L53010.v` — printed in editions [1918]:**

> MUNRO, THOMAS AMBROSE VESPER.—B. 1883; PORT OFF., BAHAMAS, 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | harbinr. | Bahamas | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1919 | ag. marshal, admv. sub., sup. ct | Bahamas *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Munro, A___Jamaica___1925`

- Staff-list name: **Munro, A** | colony: **Jamaica** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | A. Munro | Attorney-General | Privy Council | — | — |
| 1927 | A. Munro | — | Privy Council | — | — |

### Deterministic checks: `munro_thomas-ambrose-vesper_b1883` vs `Munro, A___Jamaica___1925`

- [PASS] surname_gate: bio 'MUNRO' vs stint 'Munro, A' (exact)
- [PASS] initials: bio ['T', 'A', 'V'] ~ stint ['A']
- [PASS] age_gate: stint starts 1925, birth 1883 (age 42)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Munro, T. A. V___Bahamas___1914`

- Staff-list name: **Munro, T. A. V** | colony: **Bahamas** | listed 1914–1921 | editions [1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | T. A. V. Munro | Port Officer | Treasury and Customs Department | — | — |
| 1915 | T. A. V. Munro | Port Officer | Treasury Department | — | — |
| 1917 | T. A. V. Munro | Port Officer | Customs | — | — |
| 1918 | T. A. V. Munro | Port Officer | Customs | — | — |
| 1919 | T. A. V. Munro | Port Officer | Customs | — | — |
| 1920 | T. A. V. Munro | Port Officer | Customs | — | — |
| 1921 | T. A. V. Munro | Port Officer | Customs | — | — |

### Deterministic checks: `munro_thomas-ambrose-vesper_b1883` vs `Munro, T. A. V___Bahamas___1914`

- [PASS] surname_gate: bio 'MUNRO' vs stint 'Munro, T. A. V' (exact)
- [PASS] initials: bio ['T', 'A', 'V'] ~ stint ['T', 'A', 'V']
- [PASS] age_gate: stint starts 1914, birth 1883 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1914-1921
- [FAIL] position_sim: best 21 vs bar 60: 'harbinr.' ~ 'Port Officer'
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

