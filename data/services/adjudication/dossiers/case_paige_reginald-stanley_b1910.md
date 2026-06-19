<!-- {"case_id": "case_paige_reginald-stanley_b1910", "bio_ids": ["paige_reginald-stanley_b1910"], "stint_ids": ["Paige, R. S___Uganda___1939"]} -->
# Dossier case_paige_reginald-stanley_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `paige_reginald-stanley_b1910`

- Printed name: **PAIGE, Reginald Stanley**
- Birth year: 1910 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35084.v` — printed in editions [1948, 1949, 1950, 1951]:**

> PAIGE, Reginald Stanley.—b. 1910; ed. Edin. Acad.; on mil. serv. 1939-46, maj. clk., treas., Ken., 1928; acctnt., acctnt.-gen.'s dept., Uga., 1937; asst. registr., co-op. soc., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | acctnt., acctnt.-gen.'s dept. | Uganda | [1948, 1949, 1950, 1951] |
| 1 | 1949 | asst. registr., co-op. soc | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Paige, R. S___Uganda___1939`

- Staff-list name: **Paige, R. S** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | R. S. Paige | Accountants | Accountant-General's Department | — | — |
| 1940 | R. S. Paige | Accountants | Accountant-General's Department | — | — |

### Deterministic checks: `paige_reginald-stanley_b1910` vs `Paige, R. S___Uganda___1939`

- [PASS] surname_gate: bio 'PAIGE' vs stint 'Paige, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1939, birth 1910 (age 29)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 55 vs bar 60: 'acctnt., acctnt.-gen.'s dept.' ~ 'Accountants'
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

