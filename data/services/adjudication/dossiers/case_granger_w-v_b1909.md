<!-- {"case_id": "case_granger_w-v_b1909", "bio_ids": ["granger_w-v_b1909"], "stint_ids": ["Granger, W. V___Bahamas___1964"]} -->
# Dossier case_granger_w-v_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `granger_w-v_b1909`

- Printed name: **GRANGER, W. V**
- Birth year: 1909 (attested in editions [1965, 1966])
- Honours: M.B.E
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L15680.v` — printed in editions [1965, 1966]:**

> GRANGER, W. V., M.B.E.—b. 1909; ed. Govt. Public Sch., Bah.; mil. serv., 1942-46; inspr., police, Bah., 1946; asst. supt., 1951; out island comsnr., 1955; supt., 1959; asst. comsnr., 1961; dep. comsnr., 1962; ch. immigr. offr., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | inspr., police | Bahamas | [1965, 1966] |
| 1 | 1951 | asst. supt | Bahamas *(inherited from previous clause)* | [1965, 1966] |
| 2 | 1955 | out island comsnr | Bahamas *(inherited from previous clause)* | [1965, 1966] |
| 3 | 1957 | ch. immigr. offr | Bahamas *(inherited from previous clause)* | [1965, 1966] |
| 4 | 1959 | supt | Bahamas *(inherited from previous clause)* | [1965, 1966] |
| 5 | 1961 | asst. comsnr | Bahamas *(inherited from previous clause)* | [1965, 1966] |
| 6 | 1962 | dep. comsnr | Bahamas *(inherited from previous clause)* | [1965, 1966] |

## Candidate stint `Granger, W. V___Bahamas___1964`

- Staff-list name: **Granger, W. V** | colony: **Bahamas** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | W. V. Granger | Deputy Commissioner | Civil Establishment | — | — |
| 1965 | W. V. Granger | Chief Immigration Officer | Civil Establishment | — | — |
| 1966 | W. V. Granger | Chief Immigration Officer | Civil Establishment | — | — |

### Deterministic checks: `granger_w-v_b1909` vs `Granger, W. V___Bahamas___1964`

- [PASS] surname_gate: bio 'GRANGER' vs stint 'Granger, W. V' (exact)
- [PASS] initials: bio ['W', 'V'] ~ stint ['W', 'V']
- [PASS] age_gate: stint starts 1964, birth 1909 (age 55)
- [PASS] colony: 7 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1964-1966
- [PASS] position_sim: best 69 vs bar 60: 'dep. comsnr' ~ 'Deputy Commissioner'
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

