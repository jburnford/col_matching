<!-- {"case_id": "case_dingli_l_b1907", "bio_ids": ["dingli_l_b1907"], "stint_ids": ["Dingli, L___Malta___1936"]} -->
# Dossier case_dingli_l_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dingli_l_b1907'] carry a single initial only — the namesake trap applies.

## Biography `dingli_l_b1907`

- Printed name: **DINGLI, L**
- Birth year: 1907 (attested in editions [1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L22360.v` — printed in editions [1960, 1961, 1962, 1963, 1964]:**

> DINGLI, L.—b. 1907; ed. Lyceum, Malta; teacher, Malta, 1926; postal clk., 1928; apptd. civil serv. (admin.), 1929; acctnt., 1948; prin. offr., 1948; chief exec. offr., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | teacher | Malta | [1960, 1961, 1962, 1963, 1964] |
| 1 | 1928 | postal clk | Malta *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |
| 2 | 1929 | apptd. civil serv. (admin.) | Malta *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |
| 3 | 1948 | acctnt | Malta *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |
| 4 | 1958 | chief exec. offr | Malta *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Dingli, L___Malta___1936`

- Staff-list name: **Dingli, L** | colony: **Malta** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | L. Dingli | Clerk, 2nd Class | Public Registry and Notary to Government | — | — |
| 1937 | L. Dingli | Clerk 2nd Class | Public Registry and Notary to Government | — | — |
| 1939 | L. Dingli | Clerk, 2nd Class | Public Registry | — | — |
| 1940 | L. Dingli | Clerk, 2nd Class | Public Registry | — | — |

### Deterministic checks: `dingli_l_b1907` vs `Dingli, L___Malta___1936`

- [PASS] surname_gate: bio 'DINGLI' vs stint 'Dingli, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1936, birth 1907 (age 29)
- [PASS] colony: 5 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 43 vs bar 60: 'apptd. civil serv. (admin.)' ~ 'Clerk, 2nd Class'
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

