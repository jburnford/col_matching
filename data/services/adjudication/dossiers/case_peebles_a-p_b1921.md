<!-- {"case_id": "case_peebles_a-p_b1921", "bio_ids": ["peebles_a-p_b1921"], "stint_ids": ["Peebles, A. P___Western Pacific___1951"]} -->
# Dossier case_peebles_a-p_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peebles_a-p_b1921`

- Printed name: **PEEBLES, A. P**
- Birth year: 1921 (attested in editions [1959, 1960, 1961])
- Appears in editions: [1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1959-L26759.v` — printed in editions [1959, 1960, 1961]:**

> PEEBLES, A. P.—b. 1921; ed. Beath High Sch., and St. Andrews Univ.; mil. serv., 1940-45, sub-lt. (R.N.); cadet, W. Pac. H.C., 1948; admin. offr., B.S.I.P., 1948; secon., New Heb., 1952; B.S.I.P., 1954; dist. offr., Tang., 1957; sec., Anglo-French conf. on N. Heb., 1954; econ. surv. of Bena Wattle Scheme, 1959.

**Version `col1962-L25270.v` — printed in editions [1962]:**

> PEEBLES, A. P.—b. 1921; ed. Beath High Sch., and St. Andrews Univ.; mil. serv., 1940-45, sub-lt. (R.N.); cadet, W. Pac. H.C., 1948; admin. offr., B.S.I.P., 1948; secon., New Heb., 1952; B.S.I.P., 1954; dist. offr., Tang., 1957.

**Version `col1963-L23671.v` — printed in editions [1963]:**

> PEERLES, A. P.—b. 1921; ed. Beath High Sch., and St. Andrews Univ.; mil. serv., 1940-45, sub-lt. (R.N.); cadet, W. Pac. H.C., 1948; admin. offr., B.S.I.P., 1948; secon., New Heb., 1952; B.S.I.P., 1954; dist. offr., Tang., 1957-62. (Tang. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | cadet, W. Pac. H.C | Western Pacific | [1959, 1960, 1961, 1962, 1963] |
| 1 | 1952 | secon., New Heb | Western Pacific *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |
| 2 | 1954 | B.S.I.P | Western Pacific *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |
| 3 | 1954 | sec., Anglo-French conf. on N. Heb | Tanganyika *(inherited from previous clause)* | [1959, 1960, 1961] |
| 4 | 1957 | dist. offr. | Tanganyika | [1959, 1960, 1961, 1962, 1963] |
| 5 | 1959 | econ. surv. of Bena Wattle Scheme | Tanganyika *(inherited from previous clause)* | [1959, 1960, 1961] |

## Candidate stint `Peebles, A. P___Western Pacific___1951`

- Staff-list name: **Peebles, A. P** | colony: **Western Pacific** | listed 1951–1956 | editions [1951, 1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | A. P. Peebles | Assistant Secretary | Secretariat | — | — |
| 1951 | A. P. Peebles | Cadet Officers | District Administration | — | — |
| 1953 | A. P. Peebles | Administration Officer | British National Administration | — | — |
| 1954 | A. P. Peebles | Administration Officer | British National Administration | — | — |
| 1955 | A. P. Peebles | Administrative Officer | Civil Establishment | — | — |
| 1956 | A. P. Peebles | Assistant Secretary | Civil Establishment | — | — |

### Deterministic checks: `peebles_a-p_b1921` vs `Peebles, A. P___Western Pacific___1951`

- [PASS] surname_gate: bio 'PEEBLES' vs stint 'Peebles, A. P' (exact)
- [PASS] initials: bio ['A', 'P'] ~ stint ['A', 'P']
- [PASS] age_gate: stint starts 1951, birth 1921 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Western Pacific'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1951-1956
- [FAIL] position_sim: best 53 vs bar 60: 'cadet, W. Pac. H.C' ~ 'Cadet Officers'
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

