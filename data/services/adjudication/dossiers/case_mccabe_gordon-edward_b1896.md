<!-- {"case_id": "case_mccabe_gordon-edward_b1896", "bio_ids": ["mccabe_gordon-edward_b1896"], "stint_ids": ["McCabe, G. E___Nigeria___1934"]} -->
# Dossier case_mccabe_gordon-edward_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mccabe_gordon-edward_b1896`

- Printed name: **McCABE, Gordon Edward**
- Birth year: 1896 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L34215.v` — printed in editions [1948]:**

> McCABE, Gordon Edward.—b. 1896; ed. St. George's., S. Rhod.; on mil. serv. 1916-22; cadet, Nig., 1924; admin. offr., cl. II, 1943; cl. I, 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | cadet | Nigeria | [1948] |
| 1 | 1943 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1948] |
| 2 | 1945 | cl. I | Nigeria *(inherited from previous clause)* | [1948] |

## Candidate stint `McCabe, G. E___Nigeria___1934`

- Staff-list name: **McCabe, G. E** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | G. E. McCabe | — | Administrative Service | — | — |
| 1939 | G. E. McCabe | Assistant Secretary | Secretariat, Northern Provinces | — | — |

### Deterministic checks: `mccabe_gordon-edward_b1896` vs `McCabe, G. E___Nigeria___1934`

- [PASS] surname_gate: bio 'McCABE' vs stint 'McCabe, G. E' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1934, birth 1896 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
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

