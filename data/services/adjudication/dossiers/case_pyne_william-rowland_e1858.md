<!-- {"case_id": "case_pyne_william-rowland_e1858", "bio_ids": ["pyne_william-rowland_e1858"], "stint_ids": ["Pyne, W. R___Trinidad___1878"]} -->
# Dossier case_pyne_william-rowland_e1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pyne_william-rowland_e1858`

- Printed name: **PYNE, WILLIAM ROWLAND**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29184.v` — printed in editions [1883]:**

> PYNE, WILLIAM ROWLAND.—Government clerk, Falkland Islands, Feb., 1858; acting colonial secretary, Jan., 1862; colonial secretary, Sep., 1862; justice of the peace, Dec., 1862; member of the executive council, Jan., 1863; president of the island of Montserrat, Feb., 1867; transferred, in consequence of the confederation of the Leeward Islands and the abolition of the subordinate governments of that group, to British Guiana, as stipendiary magistrate, in charge of the Berbice River district, 1880; receiver-general of Trinidad, Oct., 1872; is a member of the legislative council; acting colonial secretary, Dec., 1876, and again in June, 1880; administrated the government of Trinidad in July, 1880; appointed delegate representing the government of Trinidad at the conference held in Barbados to consider the best means to be adopted for the maintenance of telegraphic communication with the West Indies and other parts, April, 1882; acting colonial secretary June, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | Government clerk | Falkland Islands | [1883] |
| 1 | 1862 | acting colonial secretary | Falkland Islands *(inherited from previous clause)* | [1883] |
| 2 | 1863 | member of the executive council | Falkland Islands *(inherited from previous clause)* | [1883] |
| 3 | 1867 | president of the island of Montserrat | Falkland Islands *(inherited from previous clause)* | [1883] |
| 4 | 1872 | receiver-general of Trinidad | Falkland Islands *(inherited from previous clause)* | [1883] |
| 5 | 1876 | acting colonial secretary | Falkland Islands *(inherited from previous clause)* | [1883] |
| 6 | 1880 | transferred, in consequence of the confederation of the Leeward Islands and the abolition of the subordinate governments of that group, to British Guiana, as stipendiary magistrate, in charge of the Berbice River district | Falkland Islands *(inherited from previous clause)* | [1883] |
| 7 | 1882 | appointed delegate representing the government of Trinidad at the conference held in Barbados to consider the best means to be adopted for the maintenance of telegraphic communication with the West Indies and other parts | Falkland Islands *(inherited from previous clause)* | [1883] |

## Candidate stint `Pyne, W. R___Trinidad___1878`

- Staff-list name: **Pyne, W. R** | colony: **Trinidad** | listed 1878–1883 | editions [1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | W. R. Pyne | Receiver-General | Receiver-General's Department | — | — |
| 1879 | W. R. Pyne | Receiver-General | Receiver-General's Department | — | — |
| 1880 | W. R. Pyne | Receiver-General | Receiver-General's Department | — | — |
| 1883 | W. R. Pyne | Receiver-General | Receiver-General's Department | — | — |

### Deterministic checks: `pyne_william-rowland_e1858` vs `Pyne, W. R___Trinidad___1878`

- [PASS] surname_gate: bio 'PYNE' vs stint 'Pyne, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1883
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

