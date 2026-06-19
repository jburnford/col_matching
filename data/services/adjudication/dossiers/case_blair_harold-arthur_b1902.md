<!-- {"case_id": "case_blair_harold-arthur_b1902", "bio_ids": ["blair_harold-arthur_b1902"], "stint_ids": ["Blair, H. A___Gold Coast___1934"]} -->
# Dossier case_blair_harold-arthur_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 19 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blair_harold-arthur_b1902`

- Printed name: **BLAIR, HAROLD ARTHUR**
- Birth year: 1902 (attested in editions [1936, 1937, 1939, 1940])
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L58875.v` — printed in editions [1936, 1937, 1939, 1940]:**

> BLAIR, HAROLD ARTHUR.—B. 1902; ed. Lancing and St. Edmund Hall, Oxford; gold, Gold Coast, Apr., 1928; asst. dist. comsnt., Nov., 1928; dist. comsnt., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | gold | Gold Coast | [1936, 1937, 1939, 1940] |
| 1 | 1937 | dist. comsnt | Gold Coast *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |

## Candidate stint `Blair, H. A___Gold Coast___1934`

- Staff-list name: **Blair, H. A** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | H. A. Blair | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | H. A. Blair | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `blair_harold-arthur_b1902` vs `Blair, H. A___Gold Coast___1934`

- [PASS] surname_gate: bio 'BLAIR' vs stint 'Blair, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1934, birth 1902 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 62 vs bar 60: 'dist. comsnt' ~ 'District Commissioner'
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

