<!-- {"case_id": "case_lawless_william-robert_b1893", "bio_ids": ["lawless_william-robert_b1893"], "stint_ids": ["Lawless, W. R___Gold Coast___1927"]} -->
# Dossier case_lawless_william-robert_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lawless_william-robert_b1893`

- Printed name: **LAWLESS, William Robert**
- Birth year: 1893 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33953.v` — printed in editions [1948, 1949, 1950, 1951]:**

> LAWLESS, William Robert.—b. 1893; apptd. sany. supt., gr. II, G.C., 1924; gr. I., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | apptd. sany. supt., gr. II | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1936 | gr. I | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Lawless, W. R___Gold Coast___1927`

- Staff-list name: **Lawless, W. R** | colony: **Gold Coast** | listed 1927–1929 | editions [1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. R. Lawless | Supervising Sanitary Inspector | Sanitation Branch | — | — |
| 1928 | W. R. Lawless | Superintending Sanitary Inspector | Sanitation Branch | — | — |
| 1929 | W. R. Lawless | Superintending Sanitary Inspector | Sanitation Branch | — | — |

### Deterministic checks: `lawless_william-robert_b1893` vs `Lawless, W. R___Gold Coast___1927`

- [PASS] surname_gate: bio 'LAWLESS' vs stint 'Lawless, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [FAIL] position_sim: best 48 vs bar 60: 'apptd. sany. supt., gr. II' ~ 'Superintending Sanitary Inspector'
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

