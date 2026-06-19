<!-- {"case_id": "case_cullen_james-reynolds_b1900", "bio_ids": ["cullen_james-reynolds_b1900", "cullen_james-reynolds_b1901"], "stint_ids": ["Cullen, J. R___Cyprus___1934"]} -->
# Dossier case_cullen_james-reynolds_b1900

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Cullen, J. R___Cyprus___1934'] have more than one claimant biography in this case.
- Phase 1 found `cullen_james-reynolds_b1900` ↔ `Cullen, J. R___Cyprus___1934` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `cullen_james-reynolds_b1901` ↔ `Cullen, J. R___Cyprus___1934` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `cullen_james-reynolds_b1900`

- Printed name: **CULLEN, James Reynolds**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32061.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CULLEN, James Reynolds.—b. 1900; ed. Tonbridge Sch., Balliol Coll., Oxford, M.A. (Oxon), schol. and 1st hon. mods., 2nd litt. hum.; on mil. serv. 1940-45, capt.; dir. of educ., Cyp., 1930; dir. ol educ., Uga., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | dir. of educ. | Cyprus | [1948, 1949, 1950, 1951] |
| 1 | 1945 | dir. ol educ. | Uganda | [1948, 1949, 1950, 1951] |

## Biography `cullen_james-reynolds_b1901`

- Printed name: **CULLEN, JAMES REYNOLDS**
- Birth year: 1901 (attested in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L63533.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> CULLEN, JAMES REYNOLDS, M.A. (Oxon.).—B. 1901; ed. Tonbridge and Balliol Coll., Oxford; Hertford schol., 1919; 1st hors. mods., 1920; 2nd lit. hum., 1922; dir., educon., Cyprus, Sept., 1930; do., Mauritius, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | Hertford schol | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1920 | 1st hors. mods | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1922 | 2nd lit. hum | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 3 | 1930 | dir., educon. | Cyprus | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 4 | 1939 | dir., educon. | Mauritius | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Cullen, J. R___Cyprus___1934`

- Staff-list name: **Cullen, J. R** | colony: **Cyprus** | listed 1934–1939 | editions [1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | J. R. Cullen | Director of Education | Education Department | — | — |
| 1936 | J. R. Cullen | Director of Education | Education Department | — | — |
| 1939 | J. R. Cullen | Director of Education | Education Department | — | — |

### Deterministic checks: `cullen_james-reynolds_b1900` vs `Cullen, J. R___Cyprus___1934`

- [PASS] surname_gate: bio 'CULLEN' vs stint 'Cullen, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1934, birth 1900 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [PASS] position_sim: best 69 vs bar 60: 'dir. of educ.' ~ 'Director of Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `cullen_james-reynolds_b1901` vs `Cullen, J. R___Cyprus___1934`

- [PASS] surname_gate: bio 'CULLEN' vs stint 'Cullen, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1934, birth 1901 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [PASS] position_sim: best 65 vs bar 60: 'dir., educon.' ~ 'Director of Education'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1934, 1936] pos~65 (bar: >=2)
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

