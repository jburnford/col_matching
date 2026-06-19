<!-- {"case_id": "case_freislich_j-g_e1882", "bio_ids": ["freislich_j-g_e1882"], "stint_ids": ["Frieslich, J. G___Cape of Good Hope___1877"]} -->
# Dossier case_freislich_j-g_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `freislich_j-g_e1882`

- Printed name: **FREISLICH, J. G**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1886-L33603.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896]:**

> FREISLICH, J. G.—Resident magistrate, Prieksta district, Cape Colony, 19th Dec., 1882; C.C. and R.M., Middleburg, 15th Sept., 1884.

**Version `col1898-L33439.v` — printed in editions [1898, 1899, 1900]:**

> FREISLICH, J. G.—Res. mag., Prioska dist., Cape Col., Dec., 1882; C.C. and R.M., Middleburg, Sept., 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Resident magistrate, Prieksta district | Cape of Good Hope | [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900] |
| 1 | 1884 | C.C. and R.M., Middleburg | Cape of Good Hope *(inherited from previous clause)* | [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900] |

## Candidate stint `Frieslich, J. G___Cape of Good Hope___1877`

- Staff-list name: **Frieslich, J. G** | colony: **Cape of Good Hope** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. G. Frieslich | Clerk | Police Branch | — | — |
| 1878 | J. G. Frieslich | 1st Clerk | Division of Clanwilliam | — | — |

### Deterministic checks: `freislich_j-g_e1882` vs `Frieslich, J. G___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'FREISLICH' vs stint 'Frieslich, J. G' (fuzzy:2)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

