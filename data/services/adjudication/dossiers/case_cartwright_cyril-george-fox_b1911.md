<!-- {"case_id": "case_cartwright_cyril-george-fox_b1911", "bio_ids": ["cartwright_cyril-george-fox_b1911"], "stint_ids": ["Cartwright, C. G. F___Western Pacific___1936"]} -->
# Dossier case_cartwright_cyril-george-fox_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cartwright_cyril-george-fox_b1911`

- Printed name: **CARTWRIGHT, CYRIL GEORGE FOX**
- Birth year: 1911 (attested in editions [1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L57466.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> CARTWRIGHT, CYRIL GEORGE FOX.—B. 1911; ed. Winchester Coll. and Balliol Coll., Oxford; B.A.; cadet, Gilbert and Ellise Ic., 1934; dep. oomsnr. (temp. and provnl.), 1934; ag. sec. to govt., 1936; sec. to govt., Seychelles (seconded), 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | cadet, Gilbert and Ellise Ic | Gilbert and Ellice Islands | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1936 | ag. sec. to govt | Gilbert and Ellice Islands *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 2 | 1938 | sec. to govt., Seychelles (seconded) | Seychelles | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Cartwright, C. G. F___Western Pacific___1936`

- Staff-list name: **Cartwright, C. G. F** | colony: **Western Pacific** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | C. G. F. Cartwright | Cadet Officer | District Administration | — | — |
| 1937 | C. G. F. Cartwright | — | Secretariat | — | — |

### Deterministic checks: `cartwright_cyril-george-fox_b1911` vs `Cartwright, C. G. F___Western Pacific___1936`

- [PASS] surname_gate: bio 'CARTWRIGHT' vs stint 'Cartwright, C. G. F' (exact)
- [PASS] initials: bio ['C', 'G', 'F'] ~ stint ['C', 'G', 'F']
- [PASS] age_gate: stint starts 1936, birth 1911 (age 25)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1937
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

