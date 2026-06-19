<!-- {"case_id": "case_sutcliffe_edward_e1910", "bio_ids": ["sutcliffe_edward_e1910"], "stint_ids": ["Sutcliffe, Edward___Leeward Islands___1922"]} -->
# Dossier case_sutcliffe_edward_e1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sutcliffe_edward_e1910'] carry a single initial only — the namesake trap applies.

## Biography `sutcliffe_edward_e1910`

- Printed name: **SUTCLIFFE, EDWARD**
- Birth year: not printed
- Honours: L.R.C.P, Lond (1907), M.R.C.S
- Appears in editions: [1921, 1922, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1921-L60270.v` — printed in editions [1921, 1922, 1923, 1924]:**

> SUTCLIFFE, EDWARD, M.R.C.S., Eng., L.R.C.P., Lond. (1907).—Med. offr., Virgin Isds., 1910-11; poor law med. offr., and vaccination offr., Holbeach Union, Lincs., 1912-20; lt., R.A.M.C., 1915-16; served in France; med. offr., dist. A., Dominica, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910–1911 | Med. offr., Virgin Isds | — | [1921, 1922, 1923, 1924] |
| 1 | 1912–1920 | poor law med. offr., and vaccination offr., Holbeach Union, Lincs | — | [1921, 1922, 1923, 1924] |
| 2 | 1915–1916 | lt., R.A.M.C | — | [1921, 1922, 1923, 1924] |
| 3 | 1920 | med. offr., dist. A. | Dominica | [1921, 1922, 1923, 1924] |

## Candidate stint `Sutcliffe, Edward___Leeward Islands___1922`

- Staff-list name: **Sutcliffe, Edward** | colony: **Leeward Islands** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Edward Sutcliffe | Medical Officer, District A. | Medical Establishment | — | — |
| 1923 | Edward Sutcliffe | Medical Officer, District A. | Medical Establishment | — | — |

### Deterministic checks: `sutcliffe_edward_e1910` vs `Sutcliffe, Edward___Leeward Islands___1922`

- [PASS] surname_gate: bio 'SUTCLIFFE' vs stint 'Sutcliffe, Edward' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1922; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
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

