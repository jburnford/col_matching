<!-- {"case_id": "case_mills_a-g_b1912", "bio_ids": ["mills_a-g_b1912"], "stint_ids": ["Mills, A. G___Leeward Islands___1951"]} -->
# Dossier case_mills_a-g_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 43 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mills_a-g_b1912`

- Printed name: **MILLS, A. G**
- Birth year: 1912 (attested in editions [1954, 1955])
- Appears in editions: [1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1954-L21602.v` — printed in editions [1954, 1955]:**

> MILLS, A. G.—b. 1912; ed. Medway Tech. Coll., Gillingham, and Reading Univ.; mil. serv., 1940-46, capt.; ch. engnr. and man., elec. and cold storage dept., St. Kitts, 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | ch. engnr. and man., elec. and cold storage dept. | St. Kitts | [1954, 1955] |

## Candidate stint `Mills, A. G___Leeward Islands___1951`

- Staff-list name: **Mills, A. G** | colony: **Leeward Islands** | listed 1951–1954 | editions [1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | A. G. Mills | Chief Electrical Engineer and Manager | ELECTRICITY | — | — |
| 1952 | A. G. Mills | Chief Electrical Engineer and Manager | Civil Establishment | — | — |
| 1953 | A. G. Mills | Chief Electrical Engineer and Manager | Civil Establishment | — | — |
| 1954 | A. G. Mills | Chief Electrical Engineer and Manager | Civil Establishment | — | — |

### Deterministic checks: `mills_a-g_b1912` vs `Mills, A. G___Leeward Islands___1951`

- [PASS] surname_gate: bio 'MILLS' vs stint 'Mills, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1951, birth 1912 (age 39)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1954
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

