<!-- {"case_id": "case_pilot_l-m-j-r_b1896", "bio_ids": ["pilot_l-m-j-r_b1896"], "stint_ids": ["Pilot, Roger___Mauritius___1931"]} -->
# Dossier case_pilot_l-m-j-r_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pilot_l-m-j-r_b1896`

- Printed name: **PILOT, L. M. J. R**
- Birth year: 1896 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L18727.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> PILOT, L. M. J. R.—b. 1896; ed. Royal Coll., Maur., St. Thomas's and L.S.H.T.M.; sanitary warden, Maur., 1927; med. offr. of health, P. Louis and port health offr., Maur., 1932; D.D.M.S., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | sanitary warden | Mauritius | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1932 | med. offr. of health, P. Louis and port health offr. | Mauritius | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1952 | D.D.M.S | Mauritius *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Pilot, Roger___Mauritius___1931`

- Staff-list name: **Pilot, Roger** | colony: **Mauritius** | listed 1931–1939 | editions [1931, 1932, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. Pilot | Medical Officer | Medical and Health Department | — | — |
| 1932 | R. Pilot | Medical Officer | Medical and Health Department | — | — |
| 1936 | Roger Pilot | Medical Officer | Medical and Health Department | — | — |
| 1937 | Roger Pilot | Medical Officer | Medical and Health Department | — | — |
| 1939 | Roger Pilot | Medical Officer | Medical and Health Department | — | — |

### Deterministic checks: `pilot_l-m-j-r_b1896` vs `Pilot, Roger___Mauritius___1931`

- [PASS] surname_gate: bio 'PILOT' vs stint 'Pilot, Roger' (exact)
- [PASS] initials: bio ['L', 'M', 'J', 'R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1931, birth 1896 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1939
- [FAIL] position_sim: best 32 vs bar 60: 'med. offr. of health, P. Louis and port health offr.' ~ 'Medical Officer'
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

