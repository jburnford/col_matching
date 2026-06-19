<!-- {"case_id": "case_laurance_john_e1882", "bio_ids": ["laurance_john_e1882"], "stint_ids": ["Laurance, John___Western Australia___1894"]} -->
# Dossier case_laurance_john_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['laurance_john_e1882'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Laurance, John___Western Australia___1894` is also gate-compatible with biography(ies) outside this case: ['laurance_john_e1882-2', 'lawrange_c-j_e1877'] (already linked elsewhere or filtered).

## Biography `laurance_john_e1882`

- Printed name: **LAURANCE, JOHN**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L34409.v` — printed in editions [1886, 1888]:**

> LAURANCE, JOHN.—Third clerk, survey department, Western Australia, 7th November, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Third clerk, survey department | Western Australia | [1886, 1888] |

## Candidate stint `Laurance, John___Western Australia___1894`

- Staff-list name: **Laurance, John** | colony: **Western Australia** | listed 1894–1900 | editions [1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | John Laurance | Assistant Registrar and Clerk | Colonial Secretary's Department | — | — |
| 1896 | John Laurance | Assistant Registrar and Clerk | Colonial Secretary's Department | — | — |
| 1897 | John Laurance | Deputy Registrar and Clerk | Colonial Secretary's Department | — | — |
| 1898 | John Laurance | Assistant Registrar and Clerk | Colonial Secretary's Department | — | — |
| 1899 | John Laurance | Assistant Registrar and Clerk | Colonial Secretary's Department | — | — |
| 1900 | John Laurance | Registrar | Colonial Secretary's Office | — | — |

### Deterministic checks: `laurance_john_e1882` vs `Laurance, John___Western Australia___1894`

- [PASS] surname_gate: bio 'LAURANCE' vs stint 'Laurance, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Western Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1900
- [FAIL] position_sim: best 55 vs bar 60: 'Third clerk, survey department' ~ 'Assistant Registrar and Clerk'
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

