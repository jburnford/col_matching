<!-- {"case_id": "case_rowlands_claude-richard_b1895", "bio_ids": ["rowlands_claude-richard_b1895"], "stint_ids": ["Rowlands, C. R___Kenya___1927"]} -->
# Dossier case_rowlands_claude-richard_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rowlands_claude-richard_b1895`

- Printed name: **ROWLANDS, CLAUDE RICHARD**
- Birth year: 1895 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L68126.v` — printed in editions [1940]:**

> ROWLANDS, CLAUDE RICHARD, M.M.—B. 1895; Br. P.O., Mar., 1919 to Jan., 1920; postal clk. and telegraphist, Kenya and Uganda, 1920; junr. postmr., 1927; asst. survr., posts and tels., Nigeria, 1927; survr., 1931; P.M.G., Sierra Leone, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919–1920 | Br. P.O | — | [1940] |
| 1 | 1920 | postal clk. and telegraphist, Kenya and Uganda | Kenya | [1940] |
| 2 | 1927 | junr. postmr | Kenya *(inherited from previous clause)* | [1940] |
| 3 | 1927 | asst. survr., posts and tels. | Nigeria | [1940] |
| 4 | 1931 | survr | Nigeria *(inherited from previous clause)* | [1940] |
| 5 | 1939 | P.M.G. | Sierra Leone | [1940] |

## Candidate stint `Rowlands, C. R___Kenya___1927`

- Staff-list name: **Rowlands, C. R** | colony: **Kenya** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | C. R. Rowlands | Junior Postmasters | Post and Telegraph Department | — | — |
| 1928 | C. R. Rowlands | Junior Postmasters | Post and Telegraph Department | — | — |

### Deterministic checks: `rowlands_claude-richard_b1895` vs `Rowlands, C. R___Kenya___1927`

- [PASS] surname_gate: bio 'ROWLANDS' vs stint 'Rowlands, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1928
- [PASS] position_sim: best 76 vs bar 60: 'junr. postmr' ~ 'Junior Postmasters'
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

