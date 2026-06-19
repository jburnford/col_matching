<!-- {"case_id": "case_mclnnis_edward-bowater_e1865", "bio_ids": ["mclnnis_edward-bowater_e1865"], "stint_ids": ["McInnis, E. B___British Guiana___1894", "McInnis, E. B___Gold Coast___1889"]} -->
# Dossier case_mclnnis_edward-bowater_e1865

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `McInnis, E. B___British Guiana___1894` is also gate-compatible with biography(ies) outside this case: ['moinnis_edward-bowater_b1847'] (already linked elsewhere or filtered).
- NOTE: stint `McInnis, E. B___Gold Coast___1889` is also gate-compatible with biography(ies) outside this case: ['moinnis_edward-bowater_b1847'] (already linked elsewhere or filtered).

## Biography `mclnnis_edward-bowater_e1865`

- Printed name: **McLNNIS, Edward Bowater**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L34408.v` — printed in editions [1889]:**

> McLNNIS, Lieut.-Col. Edward Bowater, late 9th Lancers.—Entered the army Mar., 1865; was adjt. 9th Lancers for several years, including campaigns in Afghanistan, 1878-79-80; present at the operations near Kabul, and on Sir Frederick Roberts' march from Kabul to Kandahar, and battle of Mazra (Kandahar), 1st Sept., 1880; bronze star for Kabul, Kandahar march; medal and clasps for Kabul and Kandahar; Inspr.-Gen., G. Coast constab., Mar., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | — | — | [1889] |
| 1 | 1878–1880 | adjt. 9th Lancers | — | [1889] |
| 2 | 1880–1880 | — | — | [1889] |
| 3 | 1887 | Inspr.-Gen., G. Coast constab. | Gold Coast | [1889] |

## Candidate stint `McInnis, E. B___British Guiana___1894`

- Staff-list name: **McInnis, E. B** | colony: **British Guiana** | listed 1894–1900 | editions [1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | E. B. McInnis | Inspector-General of Police | Police | C.M.G. | Lieut.-Col. |
| 1894 | E. B. McInnis | Commandant | Militia | C.M.G. | Lieut.-Col. |
| 1896 | E. B. McInnis | Inspector-General of Police | Police | C.M.G. | Lieut.-Col. |
| 1896 | E. B. McInnis | Commandant | Militia | C.M.G. | Lieut.-Col. |
| 1898 | E. B. McInnis | Inspector-General of Police | Police | C.M.G. | Lieut.-Col. |
| 1898 | E. B. McInnis | Commandant | Militia | C.M.G. | Lieut.-Col. |
| 1899 | E. B. McInnis | Commandant | Militia | C.M.G. | Lieut.-Col. |
| 1900 | E. B. McInnis | Commandant | Militia | C.M.G. | Lieut.-Col. |

### Deterministic checks: `mclnnis_edward-bowater_e1865` vs `McInnis, E. B___British Guiana___1894`

- [PASS] surname_gate: bio 'McLNNIS' vs stint 'McInnis, E. B' (fuzzy:1)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E', 'B']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McInnis, E. B___Gold Coast___1889`

- Staff-list name: **McInnis, E. B** | colony: **Gold Coast** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | E. B. McInnis | Inspector-General | Constabulary | — | Lieut.-Col. |
| 1890 | E. B. McInnis | Inspector-General | Constabulary | C.M.G. | Lieut.-Col. |

### Deterministic checks: `mclnnis_edward-bowater_e1865` vs `McInnis, E. B___Gold Coast___1889`

- [PASS] surname_gate: bio 'McLNNIS' vs stint 'McInnis, E. B' (fuzzy:1)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E', 'B']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1890
- [FAIL] position_sim: best 40 vs bar 60: 'Inspr.-Gen., G. Coast constab.' ~ 'Inspector-General'
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

