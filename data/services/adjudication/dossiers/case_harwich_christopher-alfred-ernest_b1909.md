<!-- {"case_id": "case_harwich_christopher-alfred-ernest_b1909", "bio_ids": ["harwich_christopher-alfred-ernest_b1909"], "stint_ids": ["Harwich, A. E___Uganda___1939", "Harwich, C. A. E___Uganda___1949"]} -->
# Dossier case_harwich_christopher-alfred-ernest_b1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harwich_christopher-alfred-ernest_b1909`

- Printed name: **HARWICH, Christopher Alfred Ernest**
- Birth year: 1909 (attested in editions [1948, 1949, 1950, 1951])
- Honours: F.R.M.S
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33211.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HARWICH, Christopher Alfred Ernest, F.R.M.S.—b. 1909; ed. St. Paul's, Lond. and Univ. Coll., Riga; fellow of the medico-legal socy.; police const., Pal., 1930; cadet, asst. supt., police, Uga., 1935; asst. supt., 1939; G.C. (secondment), 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | police const. | Palestine | [1948, 1949, 1950, 1951] |
| 1 | 1935 | cadet, asst. supt., police | Uganda | [1948, 1949, 1950, 1951] |
| 2 | 1939 | asst. supt | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1948 | G.C. (secondment) | Gold Coast | [1948, 1949, 1950, 1951] |

## Candidate stint `Harwich, A. E___Uganda___1939`

- Staff-list name: **Harwich, A. E** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. E. Harwich | Superintendents, Assistant Superintendents and Cadets | Police | — | — |
| 1940 | A. E. Harwich | Superintendent, Assistant Superintendent and Cadet | Police | — | — |

### Deterministic checks: `harwich_christopher-alfred-ernest_b1909` vs `Harwich, A. E___Uganda___1939`

- [PASS] surname_gate: bio 'HARWICH' vs stint 'Harwich, A. E' (exact)
- [PASS] initials: bio ['C', 'A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1939, birth 1909 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 54 vs bar 60: 'cadet, asst. supt., police' ~ 'Superintendent, Assistant Superintendent and Cadet'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Harwich, C. A. E___Uganda___1949`

- Staff-list name: **Harwich, C. A. E** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. A. E. Harwich | Superintendents, Assistants and Cadets | Police | — | — |
| 1951 | C. A. E. Harwich | Superintendents, Assistants and Cadets | Police | — | — |

### Deterministic checks: `harwich_christopher-alfred-ernest_b1909` vs `Harwich, C. A. E___Uganda___1949`

- [PASS] surname_gate: bio 'HARWICH' vs stint 'Harwich, C. A. E' (exact)
- [PASS] initials: bio ['C', 'A', 'E'] ~ stint ['C', 'A', 'E']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 39 vs bar 60: 'asst. supt' ~ 'Superintendents, Assistants and Cadets'
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

