<!-- {"case_id": "case_pittendrigh_a_b1902", "bio_ids": ["pittendrigh_a_b1902"], "stint_ids": ["Pittendrigh, A___Hong Kong___1949"]} -->
# Dossier case_pittendrigh_a_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pittendrigh_a_b1902'] carry a single initial only — the namesake trap applies.

## Biography `pittendrigh_a_b1902`

- Printed name: **PITTENDRIGH, A**
- Birth year: 1902 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L23551.v` — printed in editions [1956, 1957]:**

> PITTENDRIGH, A.—b. 1902; ed. Newcastle Mod. Sch.; mil. serv., 1939-46, maj.; asst. supt., police, H.K., 1945; supt., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | asst. supt., police | Hong Kong | [1956, 1957] |
| 1 | 1955 | supt | Hong Kong *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Pittendrigh, A___Hong Kong___1949`

- Staff-list name: **Pittendrigh, A** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. Pittendrigh | Assistant Superintendents | Police | — | — |
| 1950 | A. Pittendrigh | Assistant Superintendents | Police | — | — |

### Deterministic checks: `pittendrigh_a_b1902` vs `Pittendrigh, A___Hong Kong___1949`

- [PASS] surname_gate: bio 'PITTENDRIGH' vs stint 'Pittendrigh, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1949, birth 1902 (age 47)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 44 vs bar 60: 'asst. supt., police' ~ 'Assistant Superintendents'
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

