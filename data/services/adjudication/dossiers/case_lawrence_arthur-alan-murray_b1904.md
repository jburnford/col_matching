<!-- {"case_id": "case_lawrence_arthur-alan-murray_b1904", "bio_ids": ["lawrence_arthur-alan-murray_b1904"], "stint_ids": ["Lawrence, A. A. M___Zanzibar___1929"]} -->
# Dossier case_lawrence_arthur-alan-murray_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lawrence_arthur-alan-murray_b1904`

- Printed name: **LAWRENCE, Arthur Alan Murray**
- Birth year: 1904 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L33957.v` — printed in editions [1948, 1949, 1950]:**

> LAWRENCE, Arthur Alan Murray.—b. 1904; ed. King's Coll. Sch., Wimbledon, and Exeter Coll., Oxford; on mil. serv., 1940-42, lieut.; admin. offr., Zanz., 1928; dist. offr., Ken.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | admin. offr. | Zanzibar | [1948, 1949, 1950] |

## Candidate stint `Lawrence, A. A. M___Zanzibar___1929`

- Staff-list name: **Lawrence, A. A. M** | colony: **Zanzibar** | listed 1929–1934 | editions [1929, 1930, 1931, 1932, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | A. A. M. Lawrence | 2nd Grade Administrative Officer | District Administration | — | — |
| 1930 | A. A. M. Lawrence | Cadet | Provincial Administration | — | — |
| 1931 | A. A. M. Lawrence | Cadets | Provincial Administration | — | — |
| 1932 | A. A. M. Lawrence | 2nd Grade Administrative Officer | Provincial Administration | — | — |
| 1933 | A. A. M. Lawrence | 2nd Grade Administrative Officer | Provincial Administration | — | — |
| 1934 | A. A. M. Lawrence | 2nd Grade Administrative Officers | Provincial Administration | — | — |

### Deterministic checks: `lawrence_arthur-alan-murray_b1904` vs `Lawrence, A. A. M___Zanzibar___1929`

- [PASS] surname_gate: bio 'LAWRENCE' vs stint 'Lawrence, A. A. M' (exact)
- [PASS] initials: bio ['A', 'A', 'M'] ~ stint ['A', 'A', 'M']
- [PASS] age_gate: stint starts 1929, birth 1904 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1934
- [FAIL] position_sim: best 48 vs bar 60: 'admin. offr.' ~ '2nd Grade Administrative Officer'
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

