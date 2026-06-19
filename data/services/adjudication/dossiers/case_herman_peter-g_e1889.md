<!-- {"case_id": "case_herman_peter-g_e1889", "bio_ids": ["herman_peter-g_e1889"], "stint_ids": ["Herman, P. G___Cape of Good Hope___1883"]} -->
# Dossier case_herman_peter-g_e1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `herman_peter-g_e1889`

- Printed name: **HERMAN, PETER G**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L33900.v` — printed in editions [1898, 1899, 1900]:**

> HERMAN, PETER G.—Chief examr. of printing accts. and requisitions, Cape, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | Chief examr. of printing accts. and requisitions | Cape of Good Hope | [1898, 1899, 1900] |

## Candidate stint `Herman, P. G___Cape of Good Hope___1883`

- Staff-list name: **Herman, P. G** | colony: **Cape of Good Hope** | listed 1883–1900 | editions [1883, 1888, 1889, 1890, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | P. G. Herman | Clerk (Second Class) | Stationery and Printing Branch | — | — |
| 1888 | P. G. Herman | Clerk (Second Class) | Stationery and Printing Branch | — | — |
| 1889 | P. G. Herman | Clerk (Second Class) | Stationery and Printing Branch | — | — |
| 1890 | P. G. Herman | Clerk (Second Class) | Stationery and Printing Branch | — | — |
| 1896 | P. G. Herman | Assistant Controller | Stationery and Printing, and Depot for Police and Government Stores | — | — |
| 1897 | P. G. Herman | Assistant Controller | Administrative Branch | — | — |
| 1898 | P. G. Herman | Assistant Controller | Stationery and Printing, and Depot for Police and Government Stores | — | — |
| 1899 | P. G. Herman | Assistant Controller | Administrative Branch | — | — |
| 1900 | P. G. Herman | Assistant Controller | Stationery and Printing, and Depot for Police and Government Stores | — | — |

### Deterministic checks: `herman_peter-g_e1889` vs `Herman, P. G___Cape of Good Hope___1883`

- [PASS] surname_gate: bio 'HERMAN' vs stint 'Herman, P. G' (exact)
- [PASS] initials: bio ['P', 'G'] ~ stint ['P', 'G']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1900
- [FAIL] position_sim: best 33 vs bar 60: 'Chief examr. of printing accts. and requisitions' ~ 'Assistant Controller'
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

