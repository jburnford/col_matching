<!-- {"case_id": "case_garcia_egbert-b_e1859", "bio_ids": ["garcia_egbert-b_e1859"], "stint_ids": ["Garcia, Egbert___Cape of Good Hope___1877", "Garcia, Egbert___Cape of Good Hope___1890"]} -->
# Dossier case_garcia_egbert-b_e1859

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Garcia, Egbert___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['garcia_egebert-b_e1859'] (already linked elsewhere or filtered).
- NOTE: stint `Garcia, Egbert___Cape of Good Hope___1890` is also gate-compatible with biography(ies) outside this case: ['garcia_egebert-b_e1859'] (already linked elsewhere or filtered).

## Biography `garcia_egbert-b_e1859`

- Printed name: **GARCIA, EGBERT B**
- Birth year: not printed
- Appears in editions: [1883, 1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L33494.v` — printed in editions [1898]:**

> GARCIA, EGBERT B.—Clerk to C.C. and R.M. Murraysburg, 1859 to 1865; clk. in G.P.O., Cape Town, 1865 to 1869; civ. consmr. and mag., Beaufort div. C. of G.H., Sept., 1872; C.C. and R.M. of Queenstown div., Feb., 1883.

**Version `col1883-L27602.v` — printed in editions [1883]:**

> GARCIA, EGBERT B.—Civil commissioner and magistrate, Beaufort division, Cape of Good Hope; appointed Dec. 1869; was clerk to C. C. and R. M. Murrysburg, 1859 to 1865; clerk in general post-office, Cape Town, 1865 to 1869.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859–1865 | Clerk to C.C. and R.M. Murraysburg | — | [1883, 1898] |
| 1 | 1865–1869 | clk. in G.P.O., Cape Town | Cape of Good Hope | [1883, 1898] |
| 2 | 1869 | appointed | — | [1883] |
| 3 | 1872 | civ. consmr. and mag., Beaufort div. C. of G.H | Cape of Good Hope *(inherited from previous clause)* | [1898] |
| 4 | 1883 | C.C. and R.M. of Queenstown div | Cape of Good Hope *(inherited from previous clause)* | [1898] |

## Candidate stint `Garcia, Egbert___Cape of Good Hope___1877`

- Staff-list name: **Garcia, Egbert** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. Garcia | Civil Commissioner and Resident Magistrate | Police Branch | — | — |
| 1878 | E. Garcia | Civil Commissioner and Resident Magistrate | DIVISION OF BEAUFORT | — | — |
| 1879 | E. Garcia | Visiting Magistrate | BEAUFORT WEST | — | — |
| 1880 | E. Garcia | Civil Commissioner and Resident Magistrate | DIVISION OF BEAUFORT | — | — |
| 1880 | E. Garcia | Visiting Magistrate | Convict Stations | — | — |

### Deterministic checks: `garcia_egbert-b_e1859` vs `Garcia, Egbert___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'GARCIA' vs stint 'Garcia, Egbert' (exact)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 42 vs bar 60: 'civ. consmr. and mag., Beaufort div. C. of G.H' ~ 'Civil Commissioner and Resident Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Garcia, Egbert___Cape of Good Hope___1890`

- Staff-list name: **Garcia, Egbert** | colony: **Cape of Good Hope** | listed 1890–1896 | editions [1890, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | E. Garcia | C.C. and R.M. | DIVISION OF QUEEN'S TOWN | — | — |
| 1896 | Egbert Garcia | R.M. | DIVISION OF KING WILLIAM'S TOWN | — | — |

### Deterministic checks: `garcia_egbert-b_e1859` vs `Garcia, Egbert___Cape of Good Hope___1890`

- [PASS] surname_gate: bio 'GARCIA' vs stint 'Garcia, Egbert' (exact)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1896
- [PASS] position_sim: best 100 vs bar 60: 'C.C. and R.M. of Queenstown div' ~ 'R.M.'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

