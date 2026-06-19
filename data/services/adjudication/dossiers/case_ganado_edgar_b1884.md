<!-- {"case_id": "case_ganado_edgar_b1884", "bio_ids": ["ganado_edgar_b1884"], "stint_ids": ["Ganado, Edgar___Malta___1922"]} -->
# Dossier case_ganado_edgar_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ganado_edgar_b1884'] carry a single initial only — the namesake trap applies.

## Biography `ganado_edgar_b1884`

- Printed name: **GANADO, EDGAR**
- Birth year: 1884 (attested in editions [1936, 1937, 1940])
- Appears in editions: [1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L60880.v` — printed in editions [1936, 1937, 1940]:**

> GANADO, PROF. EDGAR, LL.D.—B. 1884; matric., Malta Univ., 1901; LL.D., 1910; prof. of law, 1921; ag. pub. pros. and treasy. coun., 1928; judge, 1929; ex. in law, 1930.

**Version `dol1935-L57445.v` — printed in editions [1935]:**

> CANADO, PROF. EDGAR, LL.D.—B. 1884; matric., Malta Univ., 1901; LL.D., 1910; prof. of law, 1921; ag. pub. pros. and treasy. coun., 1928; judge, 1929; ex. in law, 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | matric., Malta Univ | Malta | [1935, 1936, 1937, 1940] |
| 1 | 1910 | LL.D | Malta *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 2 | 1921 | prof. of law | Malta *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 3 | 1928 | ag. pub. pros. and treasy. coun | Malta *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 4 | 1929 | judge | Malta *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 5 | 1930 | ex. in law | Malta *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |

## Candidate stint `Ganado, Edgar___Malta___1922`

- Staff-list name: **Ganado, Edgar** | colony: **Malta** | listed 1922–1940 | editions [1922, 1923, 1925, 1929, 1931, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Edgar Ganado | Civil Law | Public Instruction | — | — |
| 1923 | Edgar Ganado | Civil Law | Professors in the Malta University | — | — |
| 1925 | Edgar Ganado | Civil Law | Professors in the Malta University | — | — |
| 1929 | E Ganado | Public Prosecutor and Treasury Counsel | Crown Lawyers | — | — |
| 1931 | E. Ganado | Judge | Judicial Establishment | — | — |
| 1934 | E. Ganado | Judge | Judicial Establishment | — | — |
| 1936 | E. Ganado | Judge | Judicial Establishment | — | — |
| 1937 | E. Ganado | Judges | Judicial Establishment | — | — |
| 1939 | E. Ganado | Judge | Judicial Establishment | — | — |
| 1940 | E. Ganado | Judge | Judicial Establishment | — | — |

### Deterministic checks: `ganado_edgar_b1884` vs `Ganado, Edgar___Malta___1922`

- [PASS] surname_gate: bio 'GANADO' vs stint 'Ganado, Edgar' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1922, birth 1884 (age 38)
- [PASS] colony: 6 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1922-1940
- [PASS] position_sim: best 100 vs bar 60: 'judge' ~ 'Judge'
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

