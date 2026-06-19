<!-- {"case_id": "case_ware_thomas-walter_b1890", "bio_ids": ["ware_thomas-walter_b1890"], "stint_ids": ["Ware, T. W___Hong Kong___1929"]} -->
# Dossier case_ware_thomas-walter_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ware_thomas-walter_b1890`

- Printed name: **WARE, THOMAS WALTER**
- Birth year: 1890 (attested in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: M.B
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L64252.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> WARE, THOMAS WALTER, M.B., Ch.B. Bristol, D.P.H. (Lond.)—B. 1890; med. offr., Bristol; med. offr., med. dept., Hong Kong, in ch., subord. staff families, Kennedy Town infec. dis. hosp. and asst., Victoria hosp., 1927; in ch., civ. hosp., 1928; visiting med. offr., Chinese hosps. and dispensaries, 1930; 2nd port health offr. and inspr., immigrts., Sept., 1932 and Nov. 1933; ag. port health offr., etc., 1933; visiting health offr., Nov., 1934; health offr., Kowloon and New Territories, June, 1937; ag. port health offr. and inspr., immigrts., Aug., 1937 to Aug., 1938; health offr., urb. cl., 1939; ag. D.D.H.S., Aug., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | med. offr., med. dept., Hong Kong, in ch., subord. staff families, Kennedy Town infec. dis. hosp. and asst., Victoria hosp | Victoria | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1928 | in ch., civ. hosp | Victoria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1930 | visiting med. offr., Chinese hosps. and dispensaries | Victoria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1932 | 2nd port health offr. and inspr., immigrts | Victoria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1933 | 2nd port health offr. and inspr., immigrts | Victoria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1934 | visiting health offr | Victoria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1937 | health offr., Kowloon and New Territories | Victoria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1939 | health offr., urb. cl | Victoria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Ware, T. W___Hong Kong___1929`

- Staff-list name: **Ware, T. W** | colony: **Hong Kong** | listed 1929–1937 | editions [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | T. W. Ware | Medical Officer | Medical Departments | — | — |
| 1930 | T. W. Ware | Medical Officer | Medical Departments | — | — |
| 1931 | T. W. Ware | Medical Officer | Medical Departments | — | — |
| 1931 | T. W. Ware | Medical Officer | Staff | — | — |
| 1932 | T. W. Ware | Medical Officer | Medical Department | — | — |
| 1933 | T. W. Ware | Second Health Officer of Port and Inspector of Emigrants (acting) | Medical Department | — | — |
| 1934 | T. W. Ware | Second Health Officer of Port and Inspector of Emigrants | Medical Department | — | — |
| 1936 | T. W. Ware | Visiting Medical Officer to Chinese Hospitals and Dispensaries | Medical Department | — | — |
| 1937 | T. W. Ware | Visiting Health Officer to Chinese Hospitals and Dispensaries | Medical Department | — | — |

### Deterministic checks: `ware_thomas-walter_b1890` vs `Ware, T. W___Hong Kong___1929`

- [PASS] surname_gate: bio 'WARE' vs stint 'Ware, T. W' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T', 'W']
- [PASS] age_gate: stint starts 1929, birth 1890 (age 39)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1937
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

