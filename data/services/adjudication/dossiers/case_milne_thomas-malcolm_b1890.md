<!-- {"case_id": "case_milne_thomas-malcolm_b1890", "bio_ids": ["milne_thomas-malcolm_b1890"], "stint_ids": ["Milne, T. M___Trinidad and Tobago___1933"]} -->
# Dossier case_milne_thomas-malcolm_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `milne_thomas-malcolm_b1890`

- Printed name: **MILNE, Thomas Malcolm**
- Birth year: 1890 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L34677.v` — printed in editions [1948, 1949, 1950]:**

> MILNE, Thomas Malcolm.—b. 1890; ed. St. Mary's Coll., Trinidad, solr., sup. ct. conveyancer (1914); dep. registr. and marshal, registr. friendly soc., Trin., 1931; asst. crown solr., 1932; comsnr. inland rev., 1941; also registr. of credit unions, 1945.

**Version `col1932-L62563.v` — printed in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940]:**

> MILNE, T. M.—B. 1890; dep. regiser. gen. and dep. regiser. and dep. marshal, sup. ct. and regiser., friendly societies, Trinidad, Sept., 1931; asst. crown solr., 1932.

**Version `col1933-L62129.v` — printed in editions [1933]:**

> MILNE, T. M.—B. 1890; dep. regiar. gen. and dep. marshal, sup. ct. and regiar., friendly societies, Trinidad, Sept., 1931; asst. crown solr., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | dep. registr. and marshal, registr. friendly soc. | Trinidad | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950] |
| 1 | 1932 | asst. crown solr | Trinidad *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950] |
| 2 | 1941 | comsnr. inland rev | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950] |
| 3 | 1945 | also registr. of credit unions | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Milne, T. M___Trinidad and Tobago___1933`

- Staff-list name: **Milne, T. M** | colony: **Trinidad and Tobago** | listed 1933–1949 | editions [1933, 1934, 1937, 1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | T. M. Milne | Deputy Registrar and Assistant Marshal | Judicial Department | — | — |
| 1933 | T. M. Milne | Deputy Registrar-General | Registrar-General's Department | — | — |
| 1934 | T. M. Milne | Assistant Crown Solicitor | Legal | — | — |
| 1937 | T. M. Milne | Assistant Crown Solicitor | Legal | — | — |
| 1939 | T. M. Milne | Assistant Crown Solicitor | Legal | — | — |
| 1940 | T. M. Milne | Assistant Crown Solicitor | Crown Solicitor | — | — |
| 1949 | T. M. Milne | Commissioner | Inland Revenue | — | — |

### Deterministic checks: `milne_thomas-malcolm_b1890` vs `Milne, T. M___Trinidad and Tobago___1933`

- [PASS] surname_gate: bio 'MILNE' vs stint 'Milne, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1933, birth 1890 (age 43)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1949
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

