<!-- {"case_id": "case_coleman_s-w_b1914", "bio_ids": ["coleman_s-w_b1914"], "stint_ids": ["Coleman, S. W___Northern Rhodesia___1961"]} -->
# Dossier case_coleman_s-w_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coleman_s-w_b1914`

- Printed name: **COLEMAN, S. W**
- Birth year: 1914 (attested in editions [1961, 1962, 1963])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L20856.v` — printed in editions [1961, 1962, 1963]:**

> COLEMAN, S. W.—b. 1914; ed. Faversham Gram. Sch.; solicitor; dep. comsnr., local govt., N. Rhod., 1958; under-sec., 1961.

**Version `col1964-L15877.v` — printed in editions [1964, 1965, 1966]:**

> COLEMAN, S. W.—b. 1914; ed. Faversham Gram. Sch.; solicitor (Eng.); mil. serv., 1940–46; dep. comsnr., local govt., N. Rhod., 1958; under-secr., min. of local govt. and soc. welfare, 1961. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1958 | dep. comsnr., local govt. | Northern Rhodesia | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1961 | under-sec | Northern Rhodesia *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Coleman, S. W___Northern Rhodesia___1961`

- Staff-list name: **Coleman, S. W** | colony: **Northern Rhodesia** | listed 1961–1964 | editions [1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | S. W. Coleman | Deputy Commissioner | Civil Establishment | — | — |
| 1962 | S. W. Coleman | Under Secretary | Civil Establishment | — | — |
| 1963 | S. W. Coleman | Under Secretary | Civil Establishment | — | — |
| 1964 | S. W. Coleman | Under Secretaries | Civil Establishment | — | — |

### Deterministic checks: `coleman_s-w_b1914` vs `Coleman, S. W___Northern Rhodesia___1961`

- [PASS] surname_gate: bio 'COLEMAN' vs stint 'Coleman, S. W' (exact)
- [PASS] initials: bio ['S', 'W'] ~ stint ['S', 'W']
- [PASS] age_gate: stint starts 1961, birth 1914 (age 47)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1961-1964
- [FAIL] position_sim: best 55 vs bar 60: 'dep. comsnr., local govt.' ~ 'Deputy Commissioner'
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

