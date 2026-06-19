<!-- {"case_id": "case_munnik_g-g_e1880", "bio_ids": ["munnik_g-g_e1880"], "stint_ids": ["Munnik, G. G___Cape of Good Hope___1877", "Munnik, G. G___South Africa___1914"]} -->
# Dossier case_munnik_g-g_e1880

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `munnik_g-g_e1880`

- Printed name: **MUNNIK, G. G**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34942.v` — printed in editions [1886]:**

> MUNNIK, G. G.—Resident magistrate, Barkly East, Cape Colony, 1st May, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Resident magistrate, Barkly East | Cape of Good Hope | [1886] |

## Candidate stint `Munnik, G. G___Cape of Good Hope___1877`

- Staff-list name: **Munnik, G. G** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. G. Munnik | Clerk | Police Branch | — | — |
| 1878 | G. G. Munnik | 1st Clerk | DIVISION OF GRAAFF-REINET | — | — |
| 1880 | G. G. Munnik | 1st Clerk | DIVISION OF GRAAFF-REINET | — | — |

### Deterministic checks: `munnik_g-g_e1880` vs `Munnik, G. G___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'MUNNIK' vs stint 'Munnik, G. G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 25 vs bar 60: 'Resident magistrate, Barkly East' ~ '1st Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Munnik, G. G___South Africa___1914`

- Staff-list name: **Munnik, G. G** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | G. G. Munnik | Senator | Senate | — | — |
| 1918 | G. G. Munnik | Senator | Senate | — | — |

### Deterministic checks: `munnik_g-g_e1880` vs `Munnik, G. G___South Africa___1914`

- [PASS] surname_gate: bio 'MUNNIK' vs stint 'Munnik, G. G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G', 'G']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

