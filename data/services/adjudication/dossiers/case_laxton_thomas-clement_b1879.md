<!-- {"case_id": "case_laxton_thomas-clement_b1879", "bio_ids": ["laxton_thomas-clement_b1879"], "stint_ids": ["Laxton, T. C___Cape of Good Hope___1906"]} -->
# Dossier case_laxton_thomas-clement_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `laxton_thomas-clement_b1879`

- Printed name: **LAXTON, THOMAS CLEMENT**
- Birth year: 1879 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L68551.v` — printed in editions [1939]:**

> LAXTON, THOMAS CLEMENT.—B. 1879; clk., postmstr.-gen.'s dept., Cape, 1898; treasy., 1901; examr., control and audit office, Cape, 1906, and Union of S.A., 1910; senr. clk., treasy., 1920; prinl. clk., pub. debt commrs., 1932; acct., 1933; sec., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | clk., postmstr.-gen.'s dept. | Cape of Good Hope | [1939] |
| 1 | 1901 | treasy | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 2 | 1906 | examr., control and audit office | Cape of Good Hope | [1939] |
| 3 | 1910 | Union of S.A | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 4 | 1920 | senr. clk., treasy | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 5 | 1932 | prinl. clk., pub. debt commrs | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 6 | 1933 | acct | Cape of Good Hope *(inherited from previous clause)* | [1939] |
| 7 | 1938 | sec | Cape of Good Hope *(inherited from previous clause)* | [1939] |

## Candidate stint `Laxton, T. C___Cape of Good Hope___1906`

- Staff-list name: **Laxton, T. C** | colony: **Cape of Good Hope** | listed 1906–1909 | editions [1906, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | T. C. Laxton | Second Class Clerk | Treasury | — | — |
| 1907 | T. C. Laxton | Second Class Clerks | Treasury | — | — |
| 1909 | T. C. Laxton | Examiners | Control and Audit Office | — | — |

### Deterministic checks: `laxton_thomas-clement_b1879` vs `Laxton, T. C___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'LAXTON' vs stint 'Laxton, T. C' (exact)
- [PASS] initials: bio ['T', 'C'] ~ stint ['T', 'C']
- [PASS] age_gate: stint starts 1906, birth 1879 (age 27)
- [PASS] colony: 8 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1906-1909
- [FAIL] position_sim: best 40 vs bar 60: 'treasy' ~ 'Examiners'
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

