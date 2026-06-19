<!-- {"case_id": "case_low_p-w_b1910", "bio_ids": ["low_p-w_b1910"], "stint_ids": ["Low, P. W___Kenya___1937"]} -->
# Dossier case_low_p-w_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Low, P. W___Kenya___1937` is also gate-compatible with biography(ies) outside this case: ['low_william_e1866'] (already linked elsewhere or filtered).

## Biography `low_p-w_b1910`

- Printed name: **LOW, P. W**
- Birth year: 1910 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1956-L22639.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> LOW, P. W.—b. 1910; ed. Shrewsbury Sch. and Christ's Coll., Camb.; mil. serv., 1940-43, capt.; temp. educ. offr., Ken., 1934; cadet, 1939; ag. African courts offr., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | temp. educ. offr. | Kenya | [1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1939 | cadet | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1954 | ag. African courts offr | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Low, P. W___Kenya___1937`

- Staff-list name: **Low, P. W** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | P. W. Low | Education Officer—African Education | Education | — | — |
| 1939 | P. W. Low | Education Officer, African Education | Education | — | — |
| 1940 | P. W. Low | Cadets | Provincial Administration | — | — |

### Deterministic checks: `low_p-w_b1910` vs `Low, P. W___Kenya___1937`

- [PASS] surname_gate: bio 'LOW' vs stint 'Low, P. W' (exact)
- [PASS] initials: bio ['P', 'W'] ~ stint ['P', 'W']
- [PASS] age_gate: stint starts 1937, birth 1910 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [PASS] position_sim: best 91 vs bar 60: 'cadet' ~ 'Cadets'
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

