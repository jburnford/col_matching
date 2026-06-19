<!-- {"case_id": "case_macklin_joseph_b1900", "bio_ids": ["macklin_joseph_b1900"], "stint_ids": ["Macklin, J___Gold Coast___1927"]} -->
# Dossier case_macklin_joseph_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['macklin_joseph_b1900'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Macklin, J___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['macklin_joseph_e1927'] (already linked elsewhere or filtered).

## Biography `macklin_joseph_b1900`

- Printed name: **MacKLIN, Joseph**
- Birth year: 1900 (attested in editions [1950])
- Honours: A.M.I.E.E
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L37673.v` — printed in editions [1950]:**

> MacKLIN, Joseph, B.Sc., A.M.I.E.E.—b. 1900; ed. Larkhall Acad. and Royal Tech. Coll., Glasgow (dip.); engr., posts and tels., G.C., 1938; senr., 1944; asst. engr., in-ch., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | engr., posts and tels. | Gold Coast | [1950] |
| 1 | 1944 | senr | Gold Coast *(inherited from previous clause)* | [1950] |
| 2 | 1949 | asst. engr., in-ch | Gold Coast *(inherited from previous clause)* | [1950] |

## Candidate stint `Macklin, J___Gold Coast___1927`

- Staff-list name: **Macklin, J** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1928, 1929, 1930, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. Macklin | Telegraph Engineers and Assistant Telegraph Engineers | Engineering Branch | — | — |
| 1928 | J. Macklin | Telegraph Engineers and Assistant Telegraph Engineers | Engineering Branch | — | — |
| 1929 | J. Macklin | Telegraph Engineers and Assistant Telegraph Engineers | Engineering Branch | — | — |
| 1930 | J. Macklin | Telegraph Engineer | Engineering Branch | — | — |
| 1932 | J. Macklin | Telegraph Engineers and Assistant Telegraph Engineers | Engineering Branch | — | — |
| 1936 | J. Macklin | Telegraph Engineer | Engineering Branch | — | — |

### Deterministic checks: `macklin_joseph_b1900` vs `Macklin, J___Gold Coast___1927`

- [PASS] surname_gate: bio 'MacKLIN' vs stint 'Macklin, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1927, birth 1900 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1936
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

