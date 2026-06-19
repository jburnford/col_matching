<!-- {"case_id": "case_allan_francis-halliday_e1894", "bio_ids": ["allan_francis-halliday_e1894"], "stint_ids": ["Allan, F H___Straits Settlements___1931"]} -->
# Dossier case_allan_francis-halliday_e1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `allan_francis-halliday_e1894`

- Printed name: **ALLAN, FRANCIS HALLIDAY**
- Birth year: not printed
- Honours: A.M.I.C.E
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L61925.v` — printed in editions [1940]:**

> ALLAN, FRANCIS HALLIDAY, B.Sc. (Eng.), A.M.I.C.E.—Jr. 1894; ed. George Watson's Coll., Edin., Edin. Univ.; astt. engr., P.W.D., F.M.S., Mar., 1924; ar. drainage and irrign. engr., Sept., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | Jr | — | [1940] |
| 1 | 1924 | astt. engr., P.W.D. | Federated Malay States | [1940] |
| 2 | 1938 | ar. drainage and irrign. engr | Federated Malay States *(inherited from previous clause)* | [1940] |

## Candidate stint `Allan, F H___Straits Settlements___1931`

- Staff-list name: **Allan, F H** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | F H Allan | Assistant Engineers | PUBLIC WORKS | — | — |
| 1933 | F. H. Allan | Assistant Drainage and Irrigation Engineer | Drainage and Irrigation Department | — | — |

### Deterministic checks: `allan_francis-halliday_e1894` vs `Allan, F H___Straits Settlements___1931`

- [PASS] surname_gate: bio 'ALLAN' vs stint 'Allan, F H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

