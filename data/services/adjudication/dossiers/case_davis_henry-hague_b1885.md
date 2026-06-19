<!-- {"case_id": "case_davis_henry-hague_b1885", "bio_ids": ["davis_henry-hague_b1885"], "stint_ids": ["Davis, C. H. H___Gold Coast___1907", "Davis, H. R. H___Southern Nigeria___1910"]} -->
# Dossier case_davis_henry-hague_b1885

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 130 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davis_henry-hague_b1885`

- Printed name: **DAVIS, HENRY HAGUE**
- Birth year: 1885 (attested in editions [1936, 1937, 1939, 1940])
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L60136.v` — printed in editions [1936, 1937, 1939, 1940]:**

> DAVIS, HON. HENRY HAGUE.—B. 1885; ed., Brockville, Ont., Can.; Collegiate Inst., Toronto Univ. (B.A. 1907, gold medallist in polit. sci., M.A., LL.B.); Law Schil., Osgoode Hall, Toronto, 1911; called to Ontario bar 1911; K.C., 1928; judge, supreme ot., Ont., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | — | Toronto | [1936, 1937, 1939, 1940] |
| 1 | 1911 | called to Ontario bar | Ontario | [1936, 1937, 1939, 1940] |
| 2 | 1928 | K.C. | — | [1936, 1937, 1939, 1940] |
| 3 | 1933 | judge, supreme ot. | Ont. | [1936, 1937, 1939, 1940] |

## Candidate stint `Davis, C. H. H___Gold Coast___1907`

- Staff-list name: **Davis, C. H. H** | colony: **Gold Coast** | listed 1907–1909 | editions [1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | C. H. H. Davis | Inspector of Schools | Education Department | — | — |
| 1908 | C. H. H. Davis | District Commissioner | Judicial Department | — | — |
| 1909 | C. H. H. Davis | District Commissioners | Judicial Department | — | — |

### Deterministic checks: `davis_henry-hague_b1885` vs `Davis, C. H. H___Gold Coast___1907`

- [PASS] surname_gate: bio 'DAVIS' vs stint 'Davis, C. H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['C', 'H', 'H']
- [PASS] age_gate: stint starts 1907, birth 1885 (age 22)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Davis, H. R. H___Southern Nigeria___1910`

- Staff-list name: **Davis, H. R. H** | colony: **Southern Nigeria** | listed 1910–1912 | editions [1910, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | H. R. H. Davis | Assistant Conservator (2nd grade) | Forestry and Agriculture | — | — |
| 1911 | H. R. H. Davis | Assistant Conservators (2nd grade) | Forestry | — | — |
| 1912 | H. R. H. Davis | Assistant Conservators (2nd grade) | Forestry | — | — |

### Deterministic checks: `davis_henry-hague_b1885` vs `Davis, H. R. H___Southern Nigeria___1910`

- [PASS] surname_gate: bio 'DAVIS' vs stint 'Davis, H. R. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'R', 'H']
- [PASS] age_gate: stint starts 1910, birth 1885 (age 25)
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1912
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

