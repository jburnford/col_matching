<!-- {"case_id": "case_weldon_r_b1913", "bio_ids": ["weldon_r_b1913"], "stint_ids": ["Weldon, R___Nyasaland___1949"]} -->
# Dossier case_weldon_r_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['weldon_r_b1913'] carry a single initial only — the namesake trap applies.

## Biography `weldon_r_b1913`

- Printed name: **WELDON, R**
- Birth year: 1913 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L29156.v` — printed in editions [1959, 1960, 1961, 1962]:**

> WELDON, R.—b. 1913; ed. St. Edward's Sch.; asst. inspr., police, Nyasa., 1939; asst. supt., 1946; supt., 1953; senr. supt., police, 1957–61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | asst. inspr., police | Nyasaland | [1959, 1960, 1961, 1962] |
| 1 | 1946 | asst. supt | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 2 | 1953 | supt | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 3 | 1957–1961 | senr. supt., police | Nyasaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |

## Candidate stint `Weldon, R___Nyasaland___1949`

- Staff-list name: **Weldon, R** | colony: **Nyasaland** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. Weldon | Assistant Superintendent | Police and Immigration | — | — |
| 1950 | R. Weldon | Assistant Superintendents | Police and Immigration | — | — |
| 1951 | R. Weldon | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `weldon_r_b1913` vs `Weldon, R___Nyasaland___1949`

- [PASS] surname_gate: bio 'WELDON' vs stint 'Weldon, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 4 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt' ~ 'Assistant Superintendent'
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

