<!-- {"case_id": "case_mclelan_a-w_e1881-2", "bio_ids": ["mclelan_a-w_e1881-2"], "stint_ids": ["McLelan, A. W___Canada___1878"]} -->
# Dossier case_mclelan_a-w_e1881-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `McLelan, A. W___Canada___1878` is also gate-compatible with biography(ies) outside this case: ['mclelan_a-w_e1881-3'] (already linked elsewhere or filtered).

## Biography `mclelan_a-w_e1881-2`

- Printed name: **McLELAN, A. W.**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34649.v` — printed in editions [1886]:**

> McLELAN, Hon. A. W.—President of the privy council for the Dominion of Canada until 1881, when appointed minister of marine and fisheries; represented Canada in connection with the International Fisheries Exhibition of 1883 held in London.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | minister of marine and fisheries | — | [1886] |
| 1 | 1883–1883 | represented Canada | London | [1886] |
| 2 | ?–1881 | President of the privy council | Canada | [1886] |

## Candidate stint `McLelan, A. W___Canada___1878`

- Staff-list name: **McLelan, A. W** | colony: **Canada** | listed 1878–1897 | editions [1878, 1879, 1883, 1886, 1888, 1889, 1890, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | A. W. McLelan | Senator | Senate of Canada | — | — |
| 1879 | A. W. McLelan | Senator | Senate of Canada | — | — |
| 1883 | A. W. McLelan | Minister | DEPARTMENT OF MARINE AND FISHERIES | — | — |
| 1883 | A. W. McLelan | — | — | — | — |
| 1883 | A. W. McLelan | Minister of Marine and Fisheries | THE QUEEN'S PRIVY COUNCIL FOR CANADA | — | — |
| 1886 | A. W. McLelan | Minister of Marine and Fisheries | The Queen's Privy Council for Canada | — | — |
| 1886 | A. W. McLelan | Minister | Marine and Fisheries | — | — |
| 1886 | A. W. McLelan | Minister of Fisheries | Department of Fisheries | — | — |
| 1888 | A. W. McLelan | Postmaster-General | Post Office Department | — | — |
| 1888 | A. W. McLelan | Member | Province of Nova Scotia | — | — |
| 1888 | Hon. A. W. McLelan | Postmaster-General | THE QUEEN'S PRIVY COUNCIL FOR CANADA | — | — |
| 1889 | A. W. McLelan | Lieut. Governor of Nova Scotia | Members of the Privy Council who are not now members of the Cabinet | — | — |
| 1890 | Hon. A. W. McLelan | Lieutenant-Governor | Seat of Government—HALIFAX. | — | — |
| 1890 | Hon. A. W. McLelan | Lieutenant-Governor | Lieutenant-Governors since Confederation. | — | — |
| 1896 | A. W. McLelan | Lieutenant-Governor | Lieutenant-Governors | — | — |

### Deterministic checks: `mclelan_a-w_e1881-2` vs `McLelan, A. W___Canada___1878`

- [PASS] surname_gate: bio 'McLELAN' vs stint 'McLelan, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1897
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

