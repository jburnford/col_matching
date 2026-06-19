<!-- {"case_id": "case_shoritt_adam_b1859", "bio_ids": ["shoritt_adam_b1859"], "stint_ids": ["Shortt, Adam___Canada___1912"]} -->
# Dossier case_shoritt_adam_b1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['shoritt_adam_b1859'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Shortt, Adam___Canada___1912` is also gate-compatible with biography(ies) outside this case: ['shortt_adam_b1869'] (already linked elsewhere or filtered).

## Biography `shoritt_adam_b1859`

- Printed name: **SHORITT, ADAM**
- Birth year: 1859 (attested in editions [1912])
- Honours: F.R.S.C
- Appears in editions: [1912]

### Verbatim printed entry text (OCR)

**Version `col1912-L47572.v` — printed in editions [1912]:**

> SHORITT, ADAM, C.M.G. (1911); M.A., F.R.S.C.—B. 1859; ed. at Walkerton High Schl. and Queen's Univ., Canada (B.A., 1883, M.A., 1885) and Glasgow and Edin., Univ.; asst. prof. of philosophy, Queen's Univ., 1885; lect. and prof. of polit. science, 1889-1908; apptd. to civ. serv. comen., Canada, 1908; writer on history, banking and economics.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1885 | asst. prof. of philosophy, Queen's Univ | — | [1912] |
| 1 | 1889–1908 | lect. and prof. of polit. science | — | [1912] |
| 2 | 1908 | apptd. to civ. serv. comen. | Canada | [1912] |

## Candidate stint `Shortt, Adam___Canada___1912`

- Staff-list name: **Shortt, Adam** | colony: **Canada** | listed 1912–1922 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | Adam Shortt | Commissioner | Civil Service Commission | C.M.G. | — |
| 1913 | Adam Shortt | Commissioner | Civil Service Commission | C.M.G. | — |
| 1914 | Adam Shortt | Commissioner | Civil Service Commission | C.M.G. | — |
| 1915 | Adam Shortt | Commissioner | Civil Service Commission | C.M.G. | — |
| 1917 | Adam Shortt | Commissioner | Civil Service Commission | C.M.G. | — |
| 1918 | Adam Shortt | Chairman, Historical Documents Publication Board | Public Archives | C.M.G. | — |
| 1919 | Adam Shortt | Chairman, Historical Documents Publication Board | Public Archives | C.M.G. | — |
| 1920 | Adam Shortt | Chairman, Historical Documents Publication Board | Public Archives | C.M.G. | — |
| 1922 | Adam Shortt | Chairman, Historical Documents Publication Board | Public Archives | C.M.G. | — |

### Deterministic checks: `shoritt_adam_b1859` vs `Shortt, Adam___Canada___1912`

- [PASS] surname_gate: bio 'SHORITT' vs stint 'Shortt, Adam' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1912, birth 1859 (age 53)
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1912-1922
- [FAIL] position_sim: best 46 vs bar 60: 'apptd. to civ. serv. comen.' ~ 'Chairman, Historical Documents Publication Board'
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

