<!-- {"case_id": "case_le-conte_louis_b1881", "bio_ids": ["le-conte_louis_b1881"], "stint_ids": ["Le Conte, L___Mauritius___1910"]} -->
# Dossier case_le-conte_louis_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['le-conte_louis_b1881'] carry a single initial only — the namesake trap applies.

## Biography `le-conte_louis_b1881`

- Printed name: **LE CONTE, LOUIS**
- Birth year: 1881 (attested in editions [1933, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1933, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L61478.v` — printed in editions [1933, 1935, 1936, 1937, 1939, 1940]:**

> LE CONTE, LOUIS.—B. 1881; mag., lesser dependencies, Mauritius, 1909; do., Mauritius and Rodrigues, Oct., 1913; ag. mast. and regir., sup. ct., 1913-14; ag. prot. of immigrts. and poor law commrs., 1914; war serv. in France and Macedonia, 1916-19; food contr., May 1920; puline judge, July, 1932; ag. ch. judge, sup. ct., Oct., 1933 and March-Ded., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | mag., lesser dependencies | Mauritius | [1933, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1913 | do., Mauritius and Rodrigues | Mauritius | [1933, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1914 | ag. prot. of immigrts. and poor law commrs | Mauritius *(inherited from previous clause)* | [1933, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1920 | food contr | Mauritius *(inherited from previous clause)* | [1933, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1932 | puline judge | Mauritius *(inherited from previous clause)* | [1933, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1933 | ag. ch. judge, sup. ct | Mauritius *(inherited from previous clause)* | [1933, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1938 | March-Ded | Mauritius *(inherited from previous clause)* | [1933, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Le Conte, L___Mauritius___1910`

- Staff-list name: **Le Conte, L** | colony: **Mauritius** | listed 1910–1915 | editions [1910, 1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | L. Le Conte | District and Stipendiary Magistrate | Minor Dependencies | — | — |
| 1911 | L. Le Conte | District and Stipendiary Magistrates | Minor Dependencies | — | — |
| 1912 | L. Le Conte | District and Stipendiary Magistrates | Minor Dependencies | — | — |
| 1913 | L. Le Conte | District and Stipendiary Magistrate | Minor Dependencies | — | — |
| 1913 | L. Le Conte | District Magistrate (Port Louis, 2nd Division) | District Magistracy | — | — |
| 1914 | L. Le Conte | 2nd Division Magistrate | District and Stipendiary Magistracies | — | — |
| 1915 | L. Le Conte | 2nd Division Magistrate | District and Stipendiary Magistracies | — | — |

### Deterministic checks: `le-conte_louis_b1881` vs `Le Conte, L___Mauritius___1910`

- [PASS] surname_gate: bio 'LE CONTE' vs stint 'Le Conte, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1910, birth 1881 (age 29)
- [PASS] colony: 7 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1910-1915
- [FAIL] position_sim: best 49 vs bar 60: 'do., Mauritius and Rodrigues' ~ '2nd Division Magistrate'
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

