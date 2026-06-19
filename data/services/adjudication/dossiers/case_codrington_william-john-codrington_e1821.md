<!-- {"case_id": "case_codrington_william-john-codrington_e1821", "bio_ids": ["codrington_william-john-codrington_e1821"], "stint_ids": ["Codrington, W___Trinidad___1896"]} -->
# Dossier case_codrington_william-john-codrington_e1821

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Codrington, W___Trinidad___1896` is also gate-compatible with biography(ies) outside this case: ['codrington_humphrey-william_b1879'] (already linked elsewhere or filtered).

## Biography `codrington_william-john-codrington_e1821`

- Printed name: **CODRINGTON, WILLIAM JOHN CODRINGTON**
- Birth year: not printed
- Honours: G.C.B. (1865)
- Terminal: retired 1865 — “retired, 1865.”
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26902.v` — printed in editions [1883]:**

> CODRINGTON, GENERAL SIR WILLIAM JOHN CODRINGTON, G.C.B. (1865).—Descended from Christopher Codrington, who, temp. Charles I., emigrated to Barbados; entered the army in 1821; became lieutenant-colonel Coldstream Guards in 1836; commanded an infantry brigade in the early portion of the Crimean campaign; and subsequently commanded the light division at the capture of Sebastopol; commander-in-chief of the British forces in the East, with the local rank of general, 1855, and received the brevet of lieutenant-general in 1856 "as a mark of royal approbation;" made a K.C.B. 1856, grand cross of the Sardinian order of Savoy, and commander of the legion of honour, 1856, for his services against the Russians; M.P. for Greenwich from February, 1857, to May, 1859; governor and commander-in-chief at Gibraltar, May, 1869; retired, 1865.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1821 | entered the army | — | [1883] |
| 1 | 1836 | lieutenant-colonel Coldstream Guards | — | [1883] |
| 2 | 1855–1856 | commander-in-chief of the British forces in the East | — | [1883] |
| 3 | 1856–1856 | made a K.C.B. | — | [1883] |
| 4 | 1857–1859 | M.P. | Greenwich | [1883] |
| 5 | 1869 | governor and commander-in-chief | Gibraltar | [1883] |
| 6 | ? | commanded an infantry brigade | — | [1883] |
| 7 | ? | commanded the light division | — | [1883] |

## Candidate stint `Codrington, W___Trinidad___1896`

- Staff-list name: **Codrington, W** | colony: **Trinidad** | listed 1896–1898 | editions [1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | W. Codrington | 6th Clerk | Post Office Department | — | — |
| 1897 | W. Codrington | 6th Clerk | Post Office Department | — | — |
| 1898 | W. Codrington | 6th Clerk | Post Office Department | — | — |

### Deterministic checks: `codrington_william-john-codrington_e1821` vs `Codrington, W___Trinidad___1896`

- [PASS] surname_gate: bio 'CODRINGTON' vs stint 'Codrington, W' (exact)
- [PASS] initials: bio ['W', 'J', 'C'] ~ stint ['W']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

