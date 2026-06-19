<!-- {"case_id": "case_ritchie_t-m_b1896", "bio_ids": ["ritchie_t-m_b1896", "ritchie_thomas-marshall_b1895"], "stint_ids": ["Ritchie, T. M___Gold Coast___1930"]} -->
# Dossier case_ritchie_t-m_b1896

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Ritchie, T. M___Gold Coast___1930'] have more than one claimant biography in this case.

## Biography `ritchie_t-m_b1896`

- Printed name: **RITCHIE, T. M**
- Birth year: 1896 (attested in editions [1933, 1934, 1935, 1936])
- Appears in editions: [1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1933-L62962.v` — printed in editions [1933, 1934, 1935, 1936]:**

> RITCHIE, T. M.—B. 1896; foreman of wks., P.W.D., Gold Coast, 1926; inspr. of wks., 1928; mast., Agro. Tech. Schl., 1930.

**Version `col1937-L64276.v` — printed in editions [1937]:**

> RITCHIE, T. M.—B., 1896; war serv., 1914-19 (2nd lieut. flying offr.), R.A.F.; R. Scots Fusiliers); foreman of wks., P.W.D., Gold Coast, 1925; inspr. of wks., 1928; mast., Accra Tech. Schl., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | foreman of wks., P.W.D. | Gold Coast | [1937] |
| 1 | 1926 | foreman of wks., P.W.D. | Gold Coast | [1933, 1934, 1935, 1936] |
| 2 | 1928 | inspr. of wks | Gold Coast *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 3 | 1930 | mast., Agro. Tech. Schl | Gold Coast *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |

## Biography `ritchie_thomas-marshall_b1895`

- Printed name: **RITCHIE, THOMAS MARSHALL**
- Birth year: 1895 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70182.v` — printed in editions [1939, 1940]:**

> RITCHIE, THOMAS MARSHALL.—B. 1895; war serv., 1914-19 (2nd lieut. flying offr., R.A.F., R. Scots Fusiliers); foreman of wks., P.W.D., Gold Coast, 1925; inspr. of wks., 1928; mast., govt. tech. schl., 1930; prin., middle boarding schls., July, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | foreman of wks., P.W.D. | Gold Coast | [1939, 1940] |
| 1 | 1928 | inspr. of wks | Gold Coast *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1930 | mast., govt. tech. schl | Gold Coast *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1938 | prin., middle boarding schls | Gold Coast *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Ritchie, T. M___Gold Coast___1930`

- Staff-list name: **Ritchie, T. M** | colony: **Gold Coast** | listed 1930–1936 | editions [1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | T. M. Ritchie | Inspector of Works, Grade II. | II. Provincial Engineering Staff | — | — |
| 1932 | T. M. Ritchie | European Masters | Education Department | — | — |
| 1934 | T. M. Ritchie | European Masters | Education Department | — | — |
| 1936 | T. M. Ritchie | European Master | European Masters | — | — |

### Deterministic checks: `ritchie_t-m_b1896` vs `Ritchie, T. M___Gold Coast___1930`

- [PASS] surname_gate: bio 'RITCHIE' vs stint 'Ritchie, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1930, birth 1896 (age 34)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1930-1936
- [PASS] position_sim: best 62 vs bar 60: 'inspr. of wks' ~ 'Inspector of Works, Grade II.'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

### Deterministic checks: `ritchie_thomas-marshall_b1895` vs `Ritchie, T. M___Gold Coast___1930`

- [PASS] surname_gate: bio 'RITCHIE' vs stint 'Ritchie, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1930, birth 1895 (age 35)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1930-1936
- [PASS] position_sim: best 62 vs bar 60: 'inspr. of wks' ~ 'Inspector of Works, Grade II.'
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

