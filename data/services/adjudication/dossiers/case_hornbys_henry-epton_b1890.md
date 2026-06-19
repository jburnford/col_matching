<!-- {"case_id": "case_hornbys_henry-epton_b1890", "bio_ids": ["hornbys_henry-epton_b1890"], "stint_ids": ["Hornby, H. E___Tanganyika___1922"]} -->
# Dossier case_hornbys_henry-epton_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `hornbys_henry-epton_b1890` ↔ `Hornby, H. E___Tanganyika___1922` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Hornby, H. E___Tanganyika___1922` is also gate-compatible with biography(ies) outside this case: ['hornby_henry-erton_b1890'] (already linked elsewhere or filtered).

## Biography `hornbys_henry-epton_b1890`

- Printed name: **HORNBYS, HENRY EPTON**
- Birth year: 1890 (attested in editions [1937])
- Honours: D.V.S.M, F.R.C.V.S, O.B.E
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L61896.v` — printed in editions [1937]:**

> HORNBYS, CAPT. HENRY EPTON, O.B.E., F.R.C.V.S., D.V.S.M.—B. 1890; ed. King's Coll. Schl. and R. Vety., London; lect. in bacteriology to S.E. Agrl. Coll. (Univ. of London), 1912-13; vety. offr., N. Rhodesia, 1913-20; war serv., E. Africa, N. Rhodesia Rifles, 1914-17; S.A.V.C., 1917-19; ment. in desps.; studied physiology and pathology, Univ. Coll. Schl. of Trop. Med., London, Ecole de Medicine, Paris, and Vety. Research Lab., Pretoria; vety. pathologist, Tanganyika Territory, Feb., 1922; dep. dir., vety. services and vety. pathologist, 1930; ag. dir., vety. serv., Apr., 1931 to June, 1932; dir., vety. serv., Jan., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912–1913 | lect. in bacteriology to S.E. Agrl. Coll. (Univ. of London) | — | [1937] |
| 1 | 1913–1920 | vety. offr., N. Rhodesia | — | [1937] |
| 2 | 1917–1919 | S.A.V.C | — | [1937] |
| 3 | 1922 | vety. pathologist, Tanganyika Territory | Tanganyika | [1937] |
| 4 | 1930 | dep. dir., vety. services and vety. pathologist | Tanganyika *(inherited from previous clause)* | [1937] |
| 5 | 1931–1932 | ag. dir., vety. serv | Tanganyika *(inherited from previous clause)* | [1937] |
| 6 | 1933 | dir., vety. serv | Tanganyika *(inherited from previous clause)* | [1937] |

## Candidate stint `Hornby, H. E___Tanganyika___1922`

- Staff-list name: **Hornby, H. E** | colony: **Tanganyika** | listed 1922–1934 | editions [1922, 1923, 1924, 1925, 1930, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. E. Hornby | Veterinary Pathologist | Veterinary Department | — | — |
| 1923 | H. E. Hornby | Veterinary Pathologist | Veterinary Department | — | — |
| 1924 | H. E. Hornby | Veterinary Pathologist | Veterinary Department | — | — |
| 1925 | H. E. Hornby | Veterinary Pathologist | Veterinary Department | — | — |
| 1930 | H. E. Hornby | Veterinary Pathologist | Veterinary | — | — |
| 1933 | H. E. Hornby | Director of Veterinary Services | Veterinary | — | — |
| 1934 | H. E. Hornby | Director of Veterinary Services | Veterinary | — | — |

### Deterministic checks: `hornbys_henry-epton_b1890` vs `Hornby, H. E___Tanganyika___1922`

- [PASS] surname_gate: bio 'HORNBYS' vs stint 'Hornby, H. E' (fuzzy:1)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1922, birth 1890 (age 32)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1922-1934
- [PASS] position_sim: best 67 vs bar 60: 'vety. pathologist, Tanganyika Territory' ~ 'Veterinary Pathologist'
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

