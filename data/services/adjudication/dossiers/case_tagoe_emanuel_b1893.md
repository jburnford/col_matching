<!-- {"case_id": "case_tagoe_emanuel_b1893", "bio_ids": ["tagoe_emanuel_b1893", "tagoe_emmanuel_b1893"], "stint_ids": ["Tagoe, E___Gold Coast___1927"]} -->
# Dossier case_tagoe_emanuel_b1893

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['tagoe_emanuel_b1893', 'tagoe_emmanuel_b1893'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Tagoe, E___Gold Coast___1927'] have more than one claimant biography in this case.

## Biography `tagoe_emanuel_b1893`

- Printed name: **TAGOE, EMANUEL**
- Birth year: 1893 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L68851.v` — printed in editions [1940]:**

> TAGOE, EMANUEL, 1st Cls. Teacher's Certif.—B. 1893; ed. Wesleyan High Grade Schl. and Govt. Training Coll., Accra; inspr., schl., Gold Coast, July, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | inspr., schl. | Gold Coast | [1940] |

## Biography `tagoe_emmanuel_b1893`

- Printed name: **TAGOE, Emmanuel**
- Birth year: 1893 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36279.v` — printed in editions [1948, 1949, 1950, 1951]:**

> TAGOE, Emmanuel.—b. 1893; ed. Govt. Training Coll., Accra (1st. cl. teach. cert.); inspr. of schs., G.C., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | inspr. of schs. | Gold Coast | [1948, 1949, 1950, 1951] |

## Candidate stint `Tagoe, E___Gold Coast___1927`

- Staff-list name: **Tagoe, E** | colony: **Gold Coast** | listed 1927–1934 | editions [1927, 1928, 1929, 1930, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. Tagoe | Junior African Medical Officer | Medical Department | — | — |
| 1928 | E. Tagoe | African Medical Officers | Medical Department | — | — |
| 1929 | E. Tagoe | African Medical Officers | Medical Department | — | — |
| 1930 | E. Tagoe | African Medical Officers | Medical Department | — | — |
| 1932 | E. Tagoe | African Medical Officer | Medical Department | — | — |
| 1934 | E. Tagoe | African Medical Officers | Medical Department | — | — |

### Deterministic checks: `tagoe_emanuel_b1893` vs `Tagoe, E___Gold Coast___1927`

- [PASS] surname_gate: bio 'TAGOE' vs stint 'Tagoe, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `tagoe_emmanuel_b1893` vs `Tagoe, E___Gold Coast___1927`

- [PASS] surname_gate: bio 'TAGOE' vs stint 'Tagoe, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1934
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

