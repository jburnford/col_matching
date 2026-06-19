<!-- {"case_id": "case_calvin_thomas-augustus_b1892", "bio_ids": ["calvin_thomas-augustus_b1892"], "stint_ids": ["Calvin, T. A___Gold Coast___1922"]} -->
# Dossier case_calvin_thomas-augustus_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `calvin_thomas-augustus_b1892`

- Printed name: **CALVIN, THOMAS AUGUSTUS**
- Birth year: 1892 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1927-L57690.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932]:**

> CALVIN, THOMAS AUGUSTUS.—B. 1892; three years' war serv. in R.A.F.; instr., tech. schl., Accra, Gold Coast, 16th June, 1920; ag. prin., 27th May, 1923 to 14th Nov., 1923 in July, 1924 and from 10th Apr. to 26th Oct., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | instr., tech. schl. | Gold Coast | [1927, 1928, 1929, 1930, 1931, 1932] |
| 1 | 1923–1926 | ag. prin. | — | [1927, 1928, 1929, 1930, 1931, 1932] |

## Candidate stint `Calvin, T. A___Gold Coast___1922`

- Staff-list name: **Calvin, T. A** | colony: **Gold Coast** | listed 1922–1932 | editions [1922, 1923, 1924, 1927, 1928, 1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | T. A. Calvin | European Instructor | Education Department | — | — |
| 1923 | T. A. Calvin | European Masters | Education Department | — | — |
| 1924 | T. A. Calvin | European Masters | Education Department | — | — |
| 1927 | T. A. Calvin | European Master | Education Department | — | — |
| 1928 | T. A. Calvin | European Masters | Accra Technical School | — | — |
| 1929 | T. A. Calvin | European Master | Education Department | — | — |
| 1930 | T. A. Calvin | European Master | Accra Technical School | — | — |
| 1932 | T. A. Calvin | European Masters | Education Department | — | — |

### Deterministic checks: `calvin_thomas-augustus_b1892` vs `Calvin, T. A___Gold Coast___1922`

- [PASS] surname_gate: bio 'CALVIN' vs stint 'Calvin, T. A' (exact)
- [PASS] initials: bio ['T', 'A'] ~ stint ['T', 'A']
- [PASS] age_gate: stint starts 1922, birth 1892 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1932
- [FAIL] position_sim: best 41 vs bar 60: 'instr., tech. schl.' ~ 'European Instructor'
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

