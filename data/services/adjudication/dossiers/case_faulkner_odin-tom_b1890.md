<!-- {"case_id": "case_faulkner_odin-tom_b1890", "bio_ids": ["faulkner_odin-tom_b1890"], "stint_ids": ["Faulkner, O. T___Nigeria___1922"]} -->
# Dossier case_faulkner_odin-tom_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `faulkner_odin-tom_b1890`

- Printed name: **FAULKNER, ODIN TOM**
- Birth year: 1890 (attested in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: C.M.G (1928)
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1929-L60158.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> FAULKNER, ODIN TOM, C.M.G. (1928).—B. 1890; ed. St. Albans and Caius Coll., Cambridge (Schol.), B.A. (1st cls., nat. sci. triplos, 1911); dipl., agr., 1912; mycologist and agrl. expert to Rubber Growers' Assocn., Malaya, 1912-14; dep. dir., agr. to govt. of Punjab 1914-21; dir., agr., Nigeria, 1921; do., S.S. and advr. on agr., F.M.S., 1936; prin., Imp. School of Trop. Agrio., Trinidad (seconded), 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | dipl., agr | — | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1912–1914 | mycologist and agrl. expert to Rubber Growers' Assocn. | Malaya | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1914–1921 | dep. dir., agr. to govt. of Punjab | Malaya *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1921 | dir., agr. | Nigeria | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1936 | do., S.S. and advr. on agr. | Federated Malay States | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1938 | prin., Imp. School of Trop. Agrio., Trinidad (seconded) | Trinidad | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Faulkner, O. T___Nigeria___1922`

- Staff-list name: **Faulkner, O. T** | colony: **Nigeria** | listed 1922–1925 | editions [1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | O. T. Faulkner | Director | Agriculture | — | — |
| 1923 | O. T. Faulkner | Director | Agriculture | — | — |
| 1925 | O. T. Faulkner | Director | Agriculture | — | — |

### Deterministic checks: `faulkner_odin-tom_b1890` vs `Faulkner, O. T___Nigeria___1922`

- [PASS] surname_gate: bio 'FAULKNER' vs stint 'Faulkner, O. T' (exact)
- [PASS] initials: bio ['O', 'T'] ~ stint ['O', 'T']
- [PASS] age_gate: stint starts 1922, birth 1890 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 40 vs bar 60: 'dir., agr.' ~ 'Director'
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

