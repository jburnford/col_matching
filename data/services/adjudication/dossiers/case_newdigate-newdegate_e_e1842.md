<!-- {"case_id": "case_newdigate-newdegate_e_e1842", "bio_ids": ["newdigate-newdegate_e_e1842"], "stint_ids": ["Newdigate-Newdegate, E___Bermuda___1889"]} -->
# Dossier case_newdigate-newdegate_e_e1842

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['newdigate-newdegate_e_e1842'] carry a single initial only — the namesake trap applies.

## Biography `newdigate-newdegate_e_e1842`

- Printed name: **NEWDIGATE-NEWDEGATE, E**
- Birth year: not printed
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L35872.v` — printed in editions [1890]:**

> NEWDIGATE-NEWDEGATE, MAJ.-GEN. E.—Served with rifle brigade at Halifax, 1842-46; Canada, 1846-52; Malta, 1858-60; in Canada on particular service, 1860-61; maj.-gen., commdg. div. in Zulu war, 1879; gov. of Bermuda, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1842–1846 | Served with rifle brigade at Halifax | — | [1890] |
| 1 | 1846–1852 | Served with rifle brigade at Halifax | Canada | [1890] |
| 2 | 1858–1860 | Served with rifle brigade at Halifax | Malta | [1890] |
| 3 | 1860–1861 | in Canada on particular service | Malta *(inherited from previous clause)* | [1890] |
| 4 | 1879 | maj.-gen., commdg. div. in Zulu war | Malta *(inherited from previous clause)* | [1890] |
| 5 | 1889 | gov. of Bermuda | Malta *(inherited from previous clause)* | [1890] |

## Candidate stint `Newdigate-Newdegate, E___Bermuda___1889`

- Staff-list name: **Newdigate-Newdegate, E** | colony: **Bermuda** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | E. Newdigate-Newdegate | Governor and Commander-in-Chief | Civil Establishment | C.B. | — |
| 1890 | E. Newdigate-Newdegate | Governor and Commander-in-Chief | Civil Establishment | C.B. | Lieut.-General |

### Deterministic checks: `newdigate-newdegate_e_e1842` vs `Newdigate-Newdegate, E___Bermuda___1889`

- [PASS] surname_gate: bio 'NEWDIGATE-NEWDEGATE' vs stint 'Newdigate-Newdegate, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

