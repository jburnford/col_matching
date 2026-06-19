<!-- {"case_id": "case_lorimer_guy_b1909", "bio_ids": ["lorimer_guy_b1909"], "stint_ids": ["Lorimer, W. G___Federation of Malaya___1951"]} -->
# Dossier case_lorimer_guy_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lorimer_guy_b1909'] carry a single initial only — the namesake trap applies.

## Biography `lorimer_guy_b1909`

- Printed name: **LORIMER, Guy**
- Birth year: 1909 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1957-L25145.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962]:**

> LORIMER, G.—b. 1909; ed. Birkenhead Sch., St. John's Coll., Camb., and New Coll., Oxford; cadet, Nig., 1933; secon. Gam., 1939-43; admin. offr., cl. II, 1953; cl. I, N. Nig., 1957; perm. sec., N. Cams. affrs., 1960-61.

**Version `col1948-L34141.v` — printed in editions [1948, 1949, 1950, 1951]:**

> LORIMER, Guy.—b. 1909; ed. Birkenhead Sch., St. John’s Coll., Cambridge and New Coll., Oxford, M.A. (Cantab.), 1st year cert. in Arabic, London Sch. of Oriental Studies; cadet, Nig., 1933; seconded to Gam., 1939-43.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | cadet | Nigeria | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1939–1943 | secon. Gam | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1953 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1957 | cl. I | Northern Nigeria | [1957, 1958, 1959, 1960, 1961, 1962] |
| 4 | 1960–1961 | perm. sec., N. Cams. affrs | Northern Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Lorimer, W. G___Federation of Malaya___1951`

- Staff-list name: **Lorimer, W. G** | colony: **Federation of Malaya** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | W. G. Lorimer | Assistant Controllers | Foreign Exchange Control | — | — |
| 1952 | W. G. Lorimer | Assistant Controllers, Foreign Exchange Control* | Civil Establishment | — | — |

### Deterministic checks: `lorimer_guy_b1909` vs `Lorimer, W. G___Federation of Malaya___1951`

- [PASS] surname_gate: bio 'LORIMER' vs stint 'Lorimer, W. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1951, birth 1909 (age 42)
- [FAIL] colony: no placed event resolves to 'Federation of Malaya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1952
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

