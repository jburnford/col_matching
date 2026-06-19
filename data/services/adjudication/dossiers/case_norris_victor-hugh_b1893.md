<!-- {"case_id": "case_norris_victor-hugh_b1893", "bio_ids": ["norris_victor-hugh_b1893"], "stint_ids": ["Norris, V. H___Straits Settlements___1933"]} -->
# Dossier case_norris_victor-hugh_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `norris_victor-hugh_b1893`

- Printed name: **NORRIS, VICTOR HUGH**
- Birth year: 1893 (attested in editions [1936, 1937, 1939, 1940])
- Honours: L.M.S
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63392.v` — printed in editions [1936, 1937, 1939, 1940]:**

> NORRIS, VICTOR HUGH, L.M.S.—B. 1893; ed. Raftes Inst. & Coll. of Medicine, S'pore; asst. surgn., S'pore, Sept., 1915; ag. med. offr., various occasions, 1917-24; asst. med. offr., Sept., 1925; dep. med. offr., Oct., 1926; med. offr., S.S., Dec., 1930; do., P. Wellesley, June, 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | asst. surgn., S'pore | — | [1936, 1937, 1939, 1940] |
| 1 | 1917–1924 | ag. med. offr., various occasions | — | [1936, 1937, 1939, 1940] |
| 2 | 1925 | asst. med. offr | — | [1936, 1937, 1939, 1940] |
| 3 | 1926 | dep. med. offr | — | [1936, 1937, 1939, 1940] |
| 4 | 1930 | med. offr. | Straits Settlements | [1936, 1937, 1939, 1940] |
| 5 | 1933 | do., P. Wellesley | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |

## Candidate stint `Norris, V. H___Straits Settlements___1933`

- Staff-list name: **Norris, V. H** | colony: **Straits Settlements** | listed 1933–1936 | editions [1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | V. H. Norris | Medical and Health Officer | Medical | — | — |
| 1934 | V. H. Norris | Medical and Health Officer | Penang | — | — |
| 1936 | V. H. Norris | Medical and Health Officer | Medical | — | — |

### Deterministic checks: `norris_victor-hugh_b1893` vs `Norris, V. H___Straits Settlements___1933`

- [PASS] surname_gate: bio 'NORRIS' vs stint 'Norris, V. H' (exact)
- [PASS] initials: bio ['V', 'H'] ~ stint ['V', 'H']
- [PASS] age_gate: stint starts 1933, birth 1893 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1936
- [FAIL] position_sim: best 47 vs bar 60: 'med. offr.' ~ 'Medical and Health Officer'
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

