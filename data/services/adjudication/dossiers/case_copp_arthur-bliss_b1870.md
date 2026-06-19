<!-- {"case_id": "case_copp_arthur-bliss_b1870", "bio_ids": ["copp_arthur-bliss_b1870"], "stint_ids": ["Copp, Arthur Bliss___Canada___1906"]} -->
# Dossier case_copp_arthur-bliss_b1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `copp_arthur-bliss_b1870`

- Printed name: **COPP, Arthur Bliss**
- Birth year: 1870 (attested in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934])
- Appears in editions: [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934]

### Verbatim printed entry text (OCR)

**Version `col1922-L51602.v` — printed in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934]:**

> COPP, Hon. Arthur Bliss.—B., 1870; ed. pub. schls., prov. normal schl., Mt. Allison Univ., New Brunswick, Dalhousie Law Schl., Halifax, N.S., Harvard Law Schl. (LL.B. 1894); admitted to bar, N.B. 1895; mem., legis. ass., N.B., 1901-12; el. to H.C., bye-el., Feb., 1915; re-el., g.e., 1917 and 1921; sec. of state of Canada, 29th Dec., 1921; senator, Sept., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | admitted to bar | New Brunswick | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934] |
| 1 | 1901–1912 | mem., legis. ass. | New Brunswick | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934] |
| 2 | 1915 | el. to H.C. | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934] |
| 3 | 1917–1921 | re-el. | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934] |
| 4 | 1921 | sec. of state | Canada | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934] |
| 5 | 1925 | senator | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1934] |

## Candidate stint `Copp, Arthur Bliss___Canada___1906`

- Staff-list name: **Copp, Arthur Bliss** | colony: **Canada** | listed 1906–1912 | editions [1906, 1907, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | Arthur B. Copp | Member | House of Assembly | — | — |
| 1907 | Arthur B. Copp | Member | Members | — | — |
| 1912 | Arthur B. Copp | — | — | — | — |

### Deterministic checks: `copp_arthur-bliss_b1870` vs `Copp, Arthur Bliss___Canada___1906`

- [PASS] surname_gate: bio 'COPP' vs stint 'Copp, Arthur Bliss' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1906, birth 1870 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1912
- [FAIL] position_sim: best 32 vs bar 60: 'mem., legis. ass.' ~ 'Member'
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

