<!-- {"case_id": "case_mosse_p-m_b1924", "bio_ids": ["mosse_p-m_b1924"], "stint_ids": ["Mosse, P. M___Northern Rhodesia___1954"]} -->
# Dossier case_mosse_p-m_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mosse_p-m_b1924`

- Printed name: **MOSSE, P. M**
- Birth year: 1924 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L24680.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> MOSSE, P. M.—b. 1924; ed. Sherborne Sch.; mil. serv., 1943-45, lt.; cadet, N. Rhod., 1948; dist. offr., 1950. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | cadet | Northern Rhodesia | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1950 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Mosse, P. M___Northern Rhodesia___1954`

- Staff-list name: **Mosse, P. M** | colony: **Northern Rhodesia** | listed 1954–1955 | editions [1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | P. M. Mosse | Private Secretary | Civil Establishment | — | — |
| 1955 | P. M. Mosse | Private Secretary | Civil Establishment | — | — |

### Deterministic checks: `mosse_p-m_b1924` vs `Mosse, P. M___Northern Rhodesia___1954`

- [PASS] surname_gate: bio 'MOSSE' vs stint 'Mosse, P. M' (exact)
- [PASS] initials: bio ['P', 'M'] ~ stint ['P', 'M']
- [PASS] age_gate: stint starts 1954, birth 1924 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1954-1955
- [FAIL] position_sim: best 31 vs bar 60: 'dist. offr' ~ 'Private Secretary'
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

