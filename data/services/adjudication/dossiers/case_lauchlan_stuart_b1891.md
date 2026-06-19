<!-- {"case_id": "case_lauchlan_stuart_b1891", "bio_ids": ["lauchlan_stuart_b1891"], "stint_ids": ["Lauchlan, S___Nigeria___1921"]} -->
# Dossier case_lauchlan_stuart_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lauchlan_stuart_b1891'] carry a single initial only — the namesake trap applies.

## Biography `lauchlan_stuart_b1891`

- Printed name: **LAUCHLAN, Stuart**
- Birth year: 1891 (attested in editions [1935])
- Appears in editions: [1931, 1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `dol1935-L60165.v` — printed in editions [1935]:**

> LAUCHLAN, Stuart, B.Sc. (Forestry).—B. 1891; ed. Royal High Schl., Edinburgh and Edinburgh Univ.; astt. conserv., forests, Nigeria, 1914; conserv., forests, 2nd grade, 1918; senr. conserv., forests, Dec., 1927; ag. dir., forests, Aug., 1933-Jan., 1934.

**Version `col1931-L66021.v` — printed in editions [1931]:**

> LA'CHLAN, STUART, B.S.C. (FORESTRY).—B. 1891; ed. Royal High Schl., Edinburgh and Edinburgh Univ.; ast. conserv., forests, Nigeria, 1914; conserv., forests, 2nd grade, 1918; sec. conserv., forest, 1927.

**Version `col1932-L61885.v` — printed in editions [1932, 1933, 1934]:**

> LAUCHLAN, STUART, B.Sc. (FORESTRY).—B. 1891; ed. Royal High Schl., Edinburgh and Edinburgh Univ.; ast. conserv., forests, Nigeria, 1914; conserv., forests, 2nd grade, 1918; senr. conserv., forests, 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | astt. conserv., forests | Nigeria | [1931, 1932, 1933, 1934, 1935] |
| 1 | 1918 | conserv., forests, 2nd grade | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 2 | 1927 | senr. conserv., forests | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935] |
| 3 | 1933–1934 | ag. dir., forests | Nigeria *(inherited from previous clause)* | [1935] |

## Candidate stint `Lauchlan, S___Nigeria___1921`

- Staff-list name: **Lauchlan, S** | colony: **Nigeria** | listed 1921–1925 | editions [1921, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | S. Lauchlan | Conservator | Forestry | — | — |
| 1922 | S. Lauchlan | Conservator | Forestry | — | — |
| 1925 | S. Lauchlan | Conservator | Forestry | — | — |

### Deterministic checks: `lauchlan_stuart_b1891` vs `Lauchlan, S___Nigeria___1921`

- [PASS] surname_gate: bio 'LAUCHLAN' vs stint 'Lauchlan, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1921, birth 1891 (age 30)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1925
- [FAIL] position_sim: best 50 vs bar 60: 'conserv., forests, 2nd grade' ~ 'Conservator'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

