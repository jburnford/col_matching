<!-- {"case_id": "case_blankson_john-ebeneezer_b1899", "bio_ids": ["blankson_john-ebeneezer_b1899"], "stint_ids": ["Blankson, J. E___Gold Coast___1949"]} -->
# Dossier case_blankson_john-ebeneezer_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blankson_john-ebeneezer_b1899`

- Printed name: **BLANKSON, John Ebeneezer**
- Birth year: 1899 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33752.v` — printed in editions [1950, 1951]:**

> BLANKSON, John Ebeneezer.—b. 1899; clk., G.C., 1918; asst. acctnt. (later acctnt.), 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | clk. | Gold Coast | [1950, 1951] |
| 1 | 1940 | asst. acctnt. (later acctnt.) | Gold Coast *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Blankson, J. E___Gold Coast___1949`

- Staff-list name: **Blankson, J. E** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. E. Blankson | Accountants | Railway and Takoradi Harbour | — | — |
| 1951 | J. E. Blankson | Accountants | Accounts Branch | — | — |

### Deterministic checks: `blankson_john-ebeneezer_b1899` vs `Blankson, J. E___Gold Coast___1949`

- [PASS] surname_gate: bio 'BLANKSON' vs stint 'Blankson, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 50 vs bar 60: 'asst. acctnt. (later acctnt.)' ~ 'Accountants'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

