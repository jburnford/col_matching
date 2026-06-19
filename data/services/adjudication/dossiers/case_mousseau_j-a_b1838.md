<!-- {"case_id": "case_mousseau_j-a_b1838", "bio_ids": ["mousseau_j-a_b1838"], "stint_ids": ["Mousseau, Jos. Alfred___Canada___1879", "Mousseau, Joseph Alfred___Canada___1883"]} -->
# Dossier case_mousseau_j-a_b1838

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mousseau_j-a_b1838`

- Printed name: **MOUSSEAU, J. A.**
- Birth year: 1838 (attested in editions [1883, 1886])
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L28781.v` — printed in editions [1883, 1886]:**

> MOUSSEAU, HON. J. A., Q.C.—Born 1838, called to the bar of Lower Canada (now province of Quebec), 1860; created a Queen's counsel, 1878; entered Canadian House of Commons, 1874, where he still sits; president of privy council, 8th Nov., 1880; secretary of State for the Dominion of Canada, 20th May, 1881, to July, 1882; premier of the province of Quebec, 1882; puisne judge of the Superior Court, Quebec, 26th January, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860–1860 | called to the bar | Lower Canada | [1883, 1886] |
| 1 | 1874 | entered Canadian House of Commons | Canada | [1883, 1886] |
| 2 | 1878–1878 | Queen's counsel | — | [1883, 1886] |
| 3 | 1880–1880 | president of privy council | — | [1883, 1886] |
| 4 | 1881–1882 | secretary of State | Canada | [1883, 1886] |
| 5 | 1882–1882 | premier | Quebec | [1883, 1886] |
| 6 | 1884–1884 | puisne judge of the Superior Court | Quebec | [1883, 1886] |

## Candidate stint `Mousseau, Jos. Alfred___Canada___1879`

- Staff-list name: **Mousseau, Jos. Alfred** | colony: **Canada** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Jos. Alfred Mousseau | — | — | — | — |
| 1880 | Jos. Alfred Mousseau | — | — | — | — |

### Deterministic checks: `mousseau_j-a_b1838` vs `Mousseau, Jos. Alfred___Canada___1879`

- [PASS] surname_gate: bio 'MOUSSEAU' vs stint 'Mousseau, Jos. Alfred' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1879, birth 1838 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1879-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Mousseau, Joseph Alfred___Canada___1883`

- Staff-list name: **Mousseau, Joseph Alfred** | colony: **Canada** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | Joseph Alfred Mousseau | Premier of Quebec | THE QUEEN'S PRIVY COUNCIL FOR CANADA | — | — |
| 1886 | Joseph Alfred Mousseau | Puisne Judge of the Superior Court of Quebec | The Queen's Privy Council for Canada | — | — |

### Deterministic checks: `mousseau_j-a_b1838` vs `Mousseau, Joseph Alfred___Canada___1883`

- [PASS] surname_gate: bio 'MOUSSEAU' vs stint 'Mousseau, Joseph Alfred' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1883, birth 1838 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1886
- [FAIL] position_sim: best 46 vs bar 60: 'secretary of State' ~ 'Premier of Quebec'
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

