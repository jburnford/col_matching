<!-- {"case_id": "case_shuffey_paul_e1908", "bio_ids": ["shuffey_paul_e1908"], "stint_ids": ["Shuffrey, P___Sierra Leone___1914"]} -->
# Dossier case_shuffey_paul_e1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['shuffey_paul_e1908'] carry a single initial only — the namesake trap applies.
- Phase 1 found `shuffey_paul_e1908` ↔ `Shuffrey, P___Sierra Leone___1914` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Shuffrey, P___Sierra Leone___1914` is also gate-compatible with biography(ies) outside this case: ['shuffrey_paul_e1908'] (already linked elsewhere or filtered).

## Biography `shuffey_paul_e1908`

- Printed name: **SHUFFEY, PAUL**
- Birth year: not printed
- Appears in editions: [1919]

### Verbatim printed entry text (OCR)

**Version `col1919-L55737.v` — printed in editions [1919]:**

> SHUFFEY, PAUL.—Ed. St. Paul's and Oxford; open schlr. of Lincoln, 1908; B.A. (greats), 1912; asst. dist. commr., S. Leone, 1913; priv. sec. to gov., 1914-15; ag. dist. commr., Imperri, 1915 and 1916-17; ag. priv. sec. to gov., 1918.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908–1908 | open schlr. of Lincoln | — | [1919] |
| 1 | 1912–1912 | B.A. (greats) | — | [1919] |
| 2 | 1913–1913 | asst. dist. commr. | Sierra Leone | [1919] |
| 3 | 1914–1915 | priv. sec. to gov. | — | [1919] |
| 4 | 1915–1917 | ag. dist. commr. | Imperri | [1919] |
| 5 | 1918–1918 | ag. priv. sec. to gov. | — | [1919] |

## Candidate stint `Shuffrey, P___Sierra Leone___1914`

- Staff-list name: **Shuffrey, P** | colony: **Sierra Leone** | listed 1914–1923 | editions [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | P. Shuffrey | Assistant District Commissioner | Provincial Administration | — | — |
| 1915 | P. Shuffrey | Assistant District Commissioner | Provincial Administration | — | — |
| 1917 | P. Shuffrey | Assistant District Commissioner | Provincial Administration | — | — |
| 1918 | P. Shuffrey | Assistant District Commissioner | Provincial Administration | — | — |
| 1919 | P. Shuffrey | Assistant District Commissioner | Provincial Administration | — | — |
| 1920 | P. Shuffrey | Assistant District Commissioner | Provincial Administration | — | — |
| 1921 | P. Shuffrey | District Commissioner | Provincial Administration | — | — |
| 1922 | P. Shuffrey | District Commissioner | Provincial Administration | — | — |
| 1923 | P. Shuffrey | District Commissioner | Provincial Administration | — | — |

### Deterministic checks: `shuffey_paul_e1908` vs `Shuffrey, P___Sierra Leone___1914`

- [PASS] surname_gate: bio 'SHUFFEY' vs stint 'Shuffrey, P' (fuzzy:1)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1914-1923
- [PASS] position_sim: best 65 vs bar 60: 'asst. dist. commr.' ~ 'Assistant District Commissioner'
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

