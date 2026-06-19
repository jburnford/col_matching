<!-- {"case_id": "case_newby_joseph_e1872", "bio_ids": ["newby_joseph_e1872"], "stint_ids": ["Newby, A. J___Straits Settlements___1934"]} -->
# Dossier case_newby_joseph_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['newby_joseph_e1872'] carry a single initial only — the namesake trap applies.

## Biography `newby_joseph_e1872`

- Printed name: **NEWBY, JOSEPH**
- Birth year: not printed
- Appears in editions: [1896]

### Verbatim printed entry text (OCR)

**Version `col1896-L40537.v` — printed in editions [1896]:**

> NEWBY, JOSEPH.—M. Inst. C.E.; engineer on staff of chief insp., Cape Town, Nov., 1872; had charge of Buffalo Committee's, and Great Kei bridges, and reconstruction of all eastern province bridges destroyed by 1874 flood; special service in military engineering works during Gealeka and Basuto wars and Tembu rebellion; in charge of Aliwal North and Klai River bridges and other works and surveys, Nov., 1877; engineering assistant, Cape Town, Sept., 1881; district inspector, 1882; chief inspector, June, 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | engineer on staff of chief insp. | Cape Colony | [1896] |
| 1 | 1874 | had charge of Buffalo Committee's, and Great Kei bridges, and reconstruction of all eastern province bridges | — | [1896] |
| 2 | 1877 | in charge of Aliwal North and Klai River bridges and other works and surveys | — | [1896] |
| 3 | 1881 | engineering assistant | Cape Colony | [1896] |
| 4 | 1882 | district inspector | — | [1896] |
| 5 | 1893 | chief inspector | — | [1896] |

## Candidate stint `Newby, A. J___Straits Settlements___1934`

- Staff-list name: **Newby, A. J** | colony: **Straits Settlements** | listed 1934–1939 | editions [1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | A. J. Newby | Inspector of Rubber Dealers | Land Office | — | — |
| 1936 | A. J. Newby | Deputy Collector of Land Revenue | Land Office | — | — |
| 1939 | A. J. Newby | Deputy Collector of Land Revenue | Land Office, Singapore | — | — |

### Deterministic checks: `newby_joseph_e1872` vs `Newby, A. J___Straits Settlements___1934`

- [PASS] surname_gate: bio 'NEWBY' vs stint 'Newby, A. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1934; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

