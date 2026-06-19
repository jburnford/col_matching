<!-- {"case_id": "case_menham_f-h_b1905", "bio_ids": ["menham_f-h_b1905"], "stint_ids": ["Menham, F. H___Malta___1950", "Menham, F. H___Mauritius___1963"]} -->
# Dossier case_menham_f-h_b1905

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `menham_f-h_b1905`

- Printed name: **MENHAM, F. H**
- Birth year: 1905 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L22815.v` — printed in editions [1963, 1964, 1965, 1966]:**

> MENHAM, F. H.—b. 1905; ed. Headlands and N. Wilts. Tech. Coll.; mil. serv., 1941-46, R.A.F., sqdn. ldr.; dep. dir. civ. avia., J'ca., 1947; dir., Malta, 1949; G.C. (later Ghana Govt. serv.), 1953; Maur., 1962.

**Version `col1959-L25984.v` — printed in editions [1959, 1960]:**

> MENHAM, F. H.—b. 1905; ed. Headlands, and N. Wilts. Tech. Coll.; mil. serv., 1941-46, sqdn. ldr. (secon. to B.O.A.C., India/Burma reg., 1944-46); dep. dir., civ. aviation, J'ca., 1947; dir., Malta, 1949; Gold Coast, 1953-59 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | dep. dir. civ. avia. | Jamaica | [1959, 1960, 1963, 1964, 1965, 1966] |
| 1 | 1949 | dir. | Malta | [1959, 1960, 1963, 1964, 1965, 1966] |
| 2 | 1953 | G.C. (later Ghana Govt. serv.) | Gold Coast | [1959, 1960, 1963, 1964, 1965, 1966] |
| 3 | 1962 | G.C. (later Ghana Govt. serv.) | Mauritius | [1963, 1964, 1965, 1966] |

## Candidate stint `Menham, F. H___Malta___1950`

- Staff-list name: **Menham, F. H** | colony: **Malta** | listed 1950–1953 | editions [1950, 1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | F. H. Menham | Director of Civil Aviation | Lt.-Governor’s Office | — | — |
| 1951 | F. H. Menham | Director of Civil Aviation | Maltese Imperial Government | — | — |
| 1952 | F. H. Menham | Director of Civil Aviation | Maltese Imperial Government | — | — |
| 1953 | F. H. Menham | Director of Civil Aviation | Maltese Imperial Government | — | — |

### Deterministic checks: `menham_f-h_b1905` vs `Menham, F. H___Malta___1950`

- [PASS] surname_gate: bio 'MENHAM' vs stint 'Menham, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1950, birth 1905 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1953
- [FAIL] position_sim: best 21 vs bar 60: 'dir.' ~ 'Director of Civil Aviation'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Menham, F. H___Mauritius___1963`

- Staff-list name: **Menham, F. H** | colony: **Mauritius** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | F. H. Menham | Director of Civil Aviation | Civil Establishment | — | — |
| 1964 | F. H. Menham | Director of Civil Aviation | Civil Establishment | — | — |
| 1965 | F. H. Menham | Director of Civil Aviation | Civil Establishment | — | — |
| 1966 | F. H. Menham | Director of Civil Aviation | Civil Establishment | — | — |

### Deterministic checks: `menham_f-h_b1905` vs `Menham, F. H___Mauritius___1963`

- [PASS] surname_gate: bio 'MENHAM' vs stint 'Menham, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1963, birth 1905 (age 58)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1966
- [FAIL] position_sim: best 32 vs bar 60: 'G.C. (later Ghana Govt. serv.)' ~ 'Director of Civil Aviation'
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

