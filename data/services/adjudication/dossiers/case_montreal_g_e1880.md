<!-- {"case_id": "case_montreal_g_e1880", "bio_ids": ["montreal_g_e1880"], "stint_ids": ["Monreal, G___Malta___1877"]} -->
# Dossier case_montreal_g_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['montreal_g_e1880'] carry a single initial only — the namesake trap applies.
- Phase 1 found `montreal_g_e1880` ↔ `Monreal, G___Malta___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Monreal, G___Malta___1877` is also gate-compatible with biography(ies) outside this case: ['monreal_g_e1880'] (already linked elsewhere or filtered).

## Biography `montreal_g_e1880`

- Printed name: **MONTREAL, G**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28740.v` — printed in editions [1883]:**

> MONTREAL, G.—Controller of charitable institutions, Malta, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Controller of charitable institutions | Malta | [1883] |

## Candidate stint `Monreal, G___Malta___1877`

- Staff-list name: **Monreal, G** | colony: **Malta** | listed 1877–1886 | editions [1877, 1878, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. Monreal | Chief Clerk | Civil Establishment | — | — |
| 1878 | G. Monreal | Chief Clerk | Charitable Institutions Department | — | — |
| 1880 | G. Monreal | Chief Clerk | Charitable Institutions Department | — | — |
| 1883 | G. Monreal | Comptroller of Charitable Institutions | Charitable Institutions Department | — | — |
| 1886 | G. Monreal | Comptroller of Charitable Institutions | Charitable Institutions Department | — | — |

### Deterministic checks: `montreal_g_e1880` vs `Monreal, G___Malta___1877`

- [PASS] surname_gate: bio 'MONTREAL' vs stint 'Monreal, G' (fuzzy:1)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1886
- [PASS] position_sim: best 96 vs bar 60: 'Controller of charitable institutions' ~ 'Comptroller of Charitable Institutions'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1883] pos~96 (bar: >=2)
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

