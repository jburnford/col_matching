<!-- {"case_id": "case_evelyn-wright_graham-fortescue_b1900", "bio_ids": ["evelyn-wright_graham-fortescue_b1900"], "stint_ids": ["Evelyn-Wright, G. F___Nigeria___1929"]} -->
# Dossier case_evelyn-wright_graham-fortescue_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `evelyn-wright_graham-fortescue_b1900`

- Printed name: **EVELYN-WRIGHT, Graham Fortescue**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32488.v` — printed in editions [1948, 1949, 1950, 1951]:**

> EVELYN-WRIGHT, Graham Fortescue.—b. 1900; ed. King's Sch., Canterbury, Eng., and Potchefstroom Coll., S.A.; on mil. serv. 1914-18 and 1939-45, capt.; apptd. to police, Bech., 1923; asst. comsnt., police, Nig., 1927; supt., 1944; senr., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | apptd. to police | Bechuanaland | [1948, 1949, 1950, 1951] |
| 1 | 1927 | asst. comsnt., police | Nigeria | [1948, 1949, 1950, 1951] |
| 2 | 1944 | supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1949 | senr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Evelyn-Wright, G. F___Nigeria___1929`

- Staff-list name: **Evelyn-Wright, G. F** | colony: **Nigeria** | listed 1929–1939 | editions [1929, 1930, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | G. F. Evelyn-Wright | Commissioners and Assistant Commissioners | Marine | — | — |
| 1930 | G. F. Evelyn-Wright | Commissioners and Assistant Commissioners | Police | — | — |
| 1933 | G. F. Evelyn-Wright | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | G. F. Evelyn-Wright | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | G. F. Evelyn-Wright | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | G. F. Evelyn-Wright | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `evelyn-wright_graham-fortescue_b1900` vs `Evelyn-Wright, G. F___Nigeria___1929`

- [PASS] surname_gate: bio 'EVELYN-WRIGHT' vs stint 'Evelyn-Wright, G. F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1929, birth 1900 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1939
- [FAIL] position_sim: best 49 vs bar 60: 'asst. comsnt., police' ~ 'Commissioners and Assistant Commissioners'
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

