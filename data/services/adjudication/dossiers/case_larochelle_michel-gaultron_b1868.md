<!-- {"case_id": "case_larochelle_michel-gaultron_b1868", "bio_ids": ["larochelle_michel-gaultron_b1868"], "stint_ids": ["LaRochelle, Michel G___Canada___1912"]} -->
# Dossier case_larochelle_michel-gaultron_b1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `larochelle_michel-gaultron_b1868`

- Printed name: **LAROCHELLE, MICHEL GAULTRON**
- Birth year: 1868 (attested in editions [1910, 1911, 1912, 1913, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925])
- Honours: K.C, K.C. B.A
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1910-L47039.v` — printed in editions [1910, 1911, 1912, 1913, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> LAROCHELLE, MICHEL GAULTRON, K.C. B.A., LL.D.—B. 1868; ed. at Nicolet Coll. and Laval Univ.; priv. sec. to Sir Wilfrid Laurier, 1886-90; barr-at-law, 1891; recorder of Henrietta Street, Montreal, 1895; mem. of civ. ser. comm., Canada, 1908.

**Version `col1914-L47854.v` — printed in editions [1914]:**

> LAROCHELE, MICHEL GAULTRON, K.C., B.A.—B. 1868; ed. at Nicolet Coll. and Laval Univ.; priv. sec. to Sir Wilfrid Laurier, 1886-90; barr.-at-law, 1891; recorder of St. Henri, Montreal, 1895; mem. of civ. ser. coman., Canada, 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1886–1890 | priv. sec. to Sir Wilfrid Laurier | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1891 | barr-at-law | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1895 | recorder of Henrietta Street, Montreal | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1908 | mem. of civ. ser. comm. | Canada | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `LaRochelle, Michel G___Canada___1912`

- Staff-list name: **LaRochelle, Michel G** | colony: **Canada** | listed 1912–1917 | editions [1912, 1913, 1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Michel G. LaRochelle | Commissioner | Civil Service Commission | — | — |
| 1913 | Michel G. LaRochelle | Commissioner | Civil Service Commission | — | — |
| 1914 | Michel G. LaRochelle | Commissioner | Civil Service Commission | — | — |
| 1915 | Michel G. LaRochelle | Commissioner | Civil Service Commission | — | — |
| 1917 | Michel G. LaRochelle | Commissioner | Civil Service Commission | — | — |

### Deterministic checks: `larochelle_michel-gaultron_b1868` vs `LaRochelle, Michel G___Canada___1912`

- [PASS] surname_gate: bio 'LAROCHELLE' vs stint 'LaRochelle, Michel G' (exact)
- [PASS] initials: bio ['M', 'G'] ~ stint ['M', 'G']
- [PASS] age_gate: stint starts 1912, birth 1868 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1917
- [FAIL] position_sim: best 45 vs bar 60: 'mem. of civ. ser. comm.' ~ 'Commissioner'
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

