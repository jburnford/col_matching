<!-- {"case_id": "case_moylan_e-k_e1874", "bio_ids": ["moylan_e-k_e1874"], "stint_ids": ["Moylan, E. K___Windward Islands___1880"]} -->
# Dossier case_moylan_e-k_e1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `moylan_e-k_e1874`

- Printed name: **MOYLAN, E. K**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28783.v` — printed in editions [1883]:**

> MOYLAN, E. K., LL.D. (Dublin).—Educated at the University of Dublin, where he graduated M.A. and LL.D., called to the Irish bar, 1872. Served on the West Coast of Africa in 1873; police and stipendiary magistrate, St. Vincent, 1874; acting attorney-general, Tobago, 1877; confirmed, 1878; attorney-general, Grenada, 1879; acted as chief justice of Grenada in 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | police and stipendiary magistrate | St. Vincent | [1883] |
| 1 | 1877 | acting attorney-general | Tobago | [1883] |
| 2 | 1878 | confirmed | Tobago *(inherited from previous clause)* | [1883] |
| 3 | 1879 | attorney-general | Grenada | [1883] |
| 4 | 1882 | acted as chief justice of Grenada in | Grenada *(inherited from previous clause)* | [1883] |

## Candidate stint `Moylan, E. K___Windward Islands___1880`

- Staff-list name: **Moylan, E. K** | colony: **Windward Islands** | listed 1880–1883 | editions [1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | E. K. Moylan | Attorney-General | Judicial Establishment | — | — |
| 1883 | E. K. Moylan | Attorney-General | Judicial Establishment | — | — |

### Deterministic checks: `moylan_e-k_e1874` vs `Moylan, E. K___Windward Islands___1880`

- [PASS] surname_gate: bio 'MOYLAN' vs stint 'Moylan, E. K' (exact)
- [PASS] initials: bio ['E', 'K'] ~ stint ['E', 'K']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1883
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

