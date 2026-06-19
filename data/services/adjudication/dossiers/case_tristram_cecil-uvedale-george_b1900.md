<!-- {"case_id": "case_tristram_cecil-uvedale-george_b1900", "bio_ids": ["tristram_cecil-uvedale-george_b1900"], "stint_ids": ["Tristram, C. U. G___Nigeria___1934"]} -->
# Dossier case_tristram_cecil-uvedale-george_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tristram_cecil-uvedale-george_b1900`

- Printed name: **TRISTRAM, Cecil Uvedale George**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36488.v` — printed in editions [1948, 1949, 1950, 1951]:**

> TRISTRAM, Cecil Uvedale George, E.D.—b. 1900; ed. Wimbledon (Jesuit) Coll. and Pembroke Coll., Camb.; on mil. serv., 1940-42, maj.; cadet, Nig., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet | Nigeria | [1948, 1949, 1950, 1951] |

## Candidate stint `Tristram, C. U. G___Nigeria___1934`

- Staff-list name: **Tristram, C. U. G** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | C. U. G. Tristram | — | Administrative Service | — | — |
| 1939 | C. U. G. Tristram | Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |

### Deterministic checks: `tristram_cecil-uvedale-george_b1900` vs `Tristram, C. U. G___Nigeria___1934`

- [PASS] surname_gate: bio 'TRISTRAM' vs stint 'Tristram, C. U. G' (exact)
- [PASS] initials: bio ['C', 'U', 'G'] ~ stint ['C', 'U', 'G']
- [PASS] age_gate: stint starts 1934, birth 1900 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 25 vs bar 60: 'cadet' ~ 'Assistant Secretary'
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

