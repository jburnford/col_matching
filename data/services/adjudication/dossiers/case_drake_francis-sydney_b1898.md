<!-- {"case_id": "case_drake_francis-sydney_b1898", "bio_ids": ["drake_francis-sydney_b1898"], "stint_ids": ["Drake, F. S___Gold Coast___1928"]} -->
# Dossier case_drake_francis-sydney_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `drake_francis-sydney_b1898`

- Printed name: **DRAKE, Francis Sydney**
- Birth year: 1898 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L32303.v` — printed in editions [1948, 1949]:**

> DRAKE, Francis Sydney, B.Sc., M.I.M. & Cy. E.—b. 1898; ed. Felsted Sch.; on mil. serv. 1916-19; asst. engrn., Kumasi pub. health bd., 1926; exec. engrn., P.W.D., G.C., 1929; senr. exec. engrn., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. engrn., Kumasi pub. health bd | — | [1948, 1949] |
| 1 | 1929 | exec. engrn., P.W.D. | Gold Coast | [1948, 1949] |
| 2 | 1944 | senr. exec. engrn | Gold Coast *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Drake, F. S___Gold Coast___1928`

- Staff-list name: **Drake, F. S** | colony: **Gold Coast** | listed 1928–1936 | editions [1928, 1929, 1930, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | F. S. Drake | Assistant Engineer | Kumasi Town Engineering Branch | — | — |
| 1929 | F. S. Drake | Assistant Engineers | Kumasi Town Engineering Branch | — | — |
| 1930 | F. S. Drake | Assistant Engineer | Kumasi Town Engineering Branch | — | — |
| 1932 | F. S. Drake | Executive Engineer | Public Works Department | — | — |
| 1936 | F. S. Drake | Executive Engineer | Public Works Department | — | — |

### Deterministic checks: `drake_francis-sydney_b1898` vs `Drake, F. S___Gold Coast___1928`

- [PASS] surname_gate: bio 'DRAKE' vs stint 'Drake, F. S' (exact)
- [PASS] initials: bio ['F', 'S'] ~ stint ['F', 'S']
- [PASS] age_gate: stint starts 1928, birth 1898 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1928-1936
- [FAIL] position_sim: best 56 vs bar 60: 'exec. engrn., P.W.D.' ~ 'Executive Engineer'
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

