<!-- {"case_id": "case_gun-munro_s-d_b1916", "bio_ids": ["gun-munro_s-d_b1916"], "stint_ids": ["Gun-Munro, S. D___St Vincent___1961"]} -->
# Dossier case_gun-munro_s-d_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gun-munro_s-d_b1916`

- Printed name: **GUN-MUNRO, S. D**
- Birth year: 1916 (attested in editions [1955, 1956, 1957, 1958, 1959, 1962, 1964, 1965, 1966])
- Honours: M.B.E (1957)
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1962, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1955-L20930.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1962, 1964, 1965, 1966]:**

> GUN-MUNRO, S. D., M.B.E. (1957).—b. 1916; ed. Grenada Boys' Sec. Sch., and King's Coll., Lond.; dist. M.O., Grenada, 1946; res. surgeon, St. V., 1949; med. supt., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | dist. M.O. | Grenada | [1955, 1956, 1957, 1958, 1959, 1962, 1964, 1965, 1966] |
| 1 | 1949 | res. surgeon | St. Vincent | [1955, 1956, 1957, 1958, 1959, 1962, 1964, 1965, 1966] |
| 2 | 1952 | med. supt | St. Vincent *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1962, 1964, 1965, 1966] |

## Candidate stint `Gun-Munro, S. D___St Vincent___1961`

- Staff-list name: **Gun-Munro, S. D** | colony: **St Vincent** | listed 1961–1966 | editions [1961, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | S. D. Gun-Munro | Resident Surgeon | Civil Establishment | — | — |
| 1963 | S. D. Gun-Munro | Resident Surgeon | Civil Establishment | — | — |
| 1964 | S. D. Gun-Munro | Resident Surgeon | Civil Establishment | — | — |
| 1965 | S. D. Gun-Munro | Resident Surgeon | Civil Establishment | — | — |
| 1966 | S. D. Gun-Munro | Resident Surgeon | Civil Establishment | — | — |

### Deterministic checks: `gun-munro_s-d_b1916` vs `Gun-Munro, S. D___St Vincent___1961`

- [PASS] surname_gate: bio 'GUN-MUNRO' vs stint 'Gun-Munro, S. D' (exact)
- [PASS] initials: bio ['S', 'D'] ~ stint ['S', 'D']
- [PASS] age_gate: stint starts 1961, birth 1916 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'St Vincent'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1961-1966
- [FAIL] position_sim: best 42 vs bar 60: 'med. supt' ~ 'Resident Surgeon'
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

