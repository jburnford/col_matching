<!-- {"case_id": "case_hugo_francois-daniel_b1883", "bio_ids": ["hugo_francois-daniel_b1883"], "stint_ids": ["Hugo, Daniel___Orange River Colony___1908", "Hugo, Daniel___South Africa___1912", "Hugo, F. D___Natal___1910"]} -->
# Dossier case_hugo_francois-daniel_b1883

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hugo, Daniel___Orange River Colony___1908` is also gate-compatible with biography(ies) outside this case: ['hugo_j-d_e1877'] (already linked elsewhere or filtered).
- NOTE: stint `Hugo, Daniel___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['hugo_j-d_e1877'] (already linked elsewhere or filtered).

## Biography `hugo_francois-daniel_b1883`

- Printed name: **HUGO, FRANCOIS DANIEL**
- Birth year: 1883 (attested in editions [1932, 1933, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1932, 1933, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L61318.v` — printed in editions [1932, 1933, 1935, 1936, 1937, 1939, 1940]:**

> HUGO, FRANCOIS DANIEL, B.A.—B. 1883; inspr. schls., Natal, Apr., 1916; ch. inspr., schls., Jan., 1931; sup't, educn., Aug., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | inspr. schls. | Natal | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1931 | ch. inspr., schls | Natal *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Hugo, Daniel___Orange River Colony___1908`

- Staff-list name: **Hugo, Daniel** | colony: **Orange River Colony** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | Daniel Hugo | Member | Electoral Division | — | — |
| 1909 | Daniel Hugo | Member | Electoral Division | — | — |

### Deterministic checks: `hugo_francois-daniel_b1883` vs `Hugo, Daniel___Orange River Colony___1908`

- [PASS] surname_gate: bio 'HUGO' vs stint 'Hugo, Daniel' (exact)
- [PASS] initials: bio ['F', 'D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1908, birth 1883 (age 25)
- [FAIL] colony: no placed event resolves to 'Orange River Colony'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hugo, Daniel___South Africa___1912`

- Staff-list name: **Hugo, Daniel** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Daniel Hugo | Provincial Council Member | Provincial Council | — | — |
| 1914 | Daniel Hugo | Member of Provincial Council | Provincial Council | — | — |

### Deterministic checks: `hugo_francois-daniel_b1883` vs `Hugo, Daniel___South Africa___1912`

- [PASS] surname_gate: bio 'HUGO' vs stint 'Hugo, Daniel' (exact)
- [PASS] initials: bio ['F', 'D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1912, birth 1883 (age 29)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hugo, F. D___Natal___1910`

- Staff-list name: **Hugo, F. D** | colony: **Natal** | listed 1910–1927 | editions [1910, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | F. D. Hugo | Assistant Inspectors | Education Department | — | — |
| 1927 | F. D. Hugo | Chief Inspector of Schools | Education Department | — | — |

### Deterministic checks: `hugo_francois-daniel_b1883` vs `Hugo, F. D___Natal___1910`

- [PASS] surname_gate: bio 'HUGO' vs stint 'Hugo, F. D' (exact)
- [PASS] initials: bio ['F', 'D'] ~ stint ['F', 'D']
- [PASS] age_gate: stint starts 1910, birth 1883 (age 27)
- [PASS] colony: 2 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1910-1927
- [FAIL] position_sim: best 59 vs bar 60: 'inspr. schls.' ~ 'Chief Inspector of Schools'
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

