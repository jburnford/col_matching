<!-- {"case_id": "case_cowperthwaite_s-i_b1909", "bio_ids": ["cowperthwaite_s-i_b1909"], "stint_ids": ["Cowperthwaite, S. I___Uganda___1949"]} -->
# Dossier case_cowperthwaite_s-i_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cowperthwaite_s-i_b1909`

- Printed name: **COWPERTHWAITE, S.I**
- Birth year: 1909 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L21686.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> COWPERTHWAITE, S.I.—b. 1909; ed. Devonport High Sch., and Govan High Sch., Glasgow; mil. serv., 1939-45, lieut.; acctnt., P.W.D., Uga., 1947; chief acctnt., P.W.D., S. Leone, 1952; dep. acctnt.-gen., 1956; chief acctnt., P.W.D., Uga., 1956; under-sec., min. of works., 1961-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | acctnt., P.W.D. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1952 | chief acctnt., P.W.D., S. Leone | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1956 | dep. acctnt.-gen | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1961–1962 | under-sec., min. of works | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Cowperthwaite, S. I___Uganda___1949`

- Staff-list name: **Cowperthwaite, S. I** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. I. Cowperthwaite | Accountants | Public Works | — | — |
| 1951 | S. I. Cowperthwaite | Accountants | Public Works | — | — |

### Deterministic checks: `cowperthwaite_s-i_b1909` vs `Cowperthwaite, S. I___Uganda___1949`

- [PASS] surname_gate: bio 'COWPERTHWAITE' vs stint 'Cowperthwaite, S. I' (exact)
- [PASS] initials: bio ['S', 'I'] ~ stint ['S', 'I']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 4 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 57 vs bar 60: 'acctnt., P.W.D.' ~ 'Accountants'
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

