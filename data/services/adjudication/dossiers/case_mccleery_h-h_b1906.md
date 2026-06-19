<!-- {"case_id": "case_mccleery_h-h_b1906", "bio_ids": ["mccleery_h-h_b1906"], "stint_ids": ["McCleery, H. H___Tanganyika___1952"]} -->
# Dossier case_mccleery_h-h_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mccleery_h-h_b1906`

- Printed name: **McCLEERY, H. H**
- Birth year: 1906 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965]

### Verbatim printed entry text (OCR)

**Version `col1953-L18243.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965]:**

> McCLEERY, H. H.—b. 1906; ed. Christ's Hosp. and St. Catharine's Coll., Camb.; cadet, Tang., 1930; asst. dist. offr., 1932; dist. offr., 1942; dep. prov. comsnr., 1949; dir. estab., 1951; prov. comantr., 1953; ret., 1954; supvr. o/seas serv. courses, Camb. Univ., 1954. (Tang. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | cadet | Tanganyika | [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965] |
| 1 | 1932 | asst. dist. offr | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965] |
| 2 | 1942 | dist. offr | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965] |
| 3 | 1949 | dep. prov. comsnr | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965] |
| 4 | 1951 | dir. estab | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965] |
| 5 | 1953 | prov. comantr | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965] |
| 6 | 1954 | ret | Tanganyika *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1960, 1963, 1965] |

## Candidate stint `McCleery, H. H___Tanganyika___1952`

- Staff-list name: **McCleery, H. H** | colony: **Tanganyika** | listed 1952–1953 | editions [1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | H. H. McCleery | Director of Establishments | Civil Establishment | — | — |
| 1953 | H. H. McCleery | Senior Provincial Commissioners | Civil Establishment | — | — |

### Deterministic checks: `mccleery_h-h_b1906` vs `McCleery, H. H___Tanganyika___1952`

- [PASS] surname_gate: bio 'McCLEERY' vs stint 'McCleery, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1952, birth 1906 (age 46)
- [PASS] colony: 7 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1952-1953
- [FAIL] position_sim: best 51 vs bar 60: 'dir. estab' ~ 'Director of Establishments'
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

