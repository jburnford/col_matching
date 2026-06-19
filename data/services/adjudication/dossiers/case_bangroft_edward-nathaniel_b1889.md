<!-- {"case_id": "case_bangroft_edward-nathaniel_b1889", "bio_ids": ["bangroft_edward-nathaniel_b1889"], "stint_ids": ["Bancroft, E. N___Jamaica___1930"]} -->
# Dossier case_bangroft_edward-nathaniel_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bangroft_edward-nathaniel_b1889`

- Printed name: **BANGROFT, EDWARD NATHANIEL**
- Birth year: 1889 (attested in editions [1931])
- Honours: F.R.G.S, M.C
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1931-L62174.v` — printed in editions [1931]:**

> BANGROFT, EDWARD NATHANIEL, M.C., M.Am.Soc.'E., F.R.G.S.—B. 1889; lieut., R.E., 1916; France, 1917-18; survey engrnr., Nigerian rlys., July, 1927; survr., gen., Jamaica, May, 1929.

**Version `col1932-L58167.v` — printed in editions [1932, 1933, 1935, 1936]:**

> BANCROFT, EDWARD NATHANIEL, M.C., M.Am.Soc.C.E., F.R.G.S.—B. 1889; lieut., R.E., 1916; France, 1917-18; survey engnr., Nigerian rly., July, 1927; surv., gen., Jamaica, May, 1929.

**Version `col1934-L56361.v` — printed in editions [1934]:**

> BANCOFT, EDWARD NATHANIEL, M.C., M.Am.Soc.C.E., F.R.G.S.—B. 1889; lieut., R.E., 1916; France, 1917-18; survey engnr., Nigerian rly., July, 1927; survr., gen., Jamaica, May, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | lieut., R.E | — | [1931, 1932, 1933, 1934, 1935, 1936] |
| 1 | 1917–1918 | France | — | [1931, 1932, 1933, 1934, 1935, 1936] |
| 2 | 1927 | survey engrnr., Nigerian rlys | — | [1931, 1932, 1933, 1934, 1935, 1936] |
| 3 | 1929 | survr., gen. | Jamaica | [1931, 1932, 1933, 1934, 1935, 1936] |

## Candidate stint `Bancroft, E. N___Jamaica___1930`

- Staff-list name: **Bancroft, E. N** | colony: **Jamaica** | listed 1930–1934 | editions [1930, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | E. N. Bancroft | Surveyor-General | Crown Lands Department | — | — |
| 1933 | E. N. Bancroft | Surveyor-General | Crown Lands Department | — | — |
| 1934 | E. N. Bancroft | Surveyor-General | Crown Lands Department | — | — |

### Deterministic checks: `bangroft_edward-nathaniel_b1889` vs `Bancroft, E. N___Jamaica___1930`

- [PASS] surname_gate: bio 'BANGROFT' vs stint 'Bancroft, E. N' (fuzzy:1)
- [PASS] initials: bio ['E', 'N'] ~ stint ['E', 'N']
- [PASS] age_gate: stint starts 1930, birth 1889 (age 41)
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1934
- [FAIL] position_sim: best 42 vs bar 60: 'survr., gen.' ~ 'Surveyor-General'
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

