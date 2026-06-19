<!-- {"case_id": "case_okes_h_e1880-2", "bio_ids": ["okes_h_e1880-2"], "stint_ids": ["Okes, Holt___Cape of Good Hope___1877", "Okes, Holt___Cape of Good Hope___1890"]} -->
# Dossier case_okes_h_e1880-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['okes_h_e1880-2'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Okes, Holt___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['okes_h_e1880'] (already linked elsewhere or filtered).
- NOTE: stint `Okes, Holt___Cape of Good Hope___1890` is also gate-compatible with biography(ies) outside this case: ['okes_h_e1880'] (already linked elsewhere or filtered).

## Biography `okes_h_e1880-2`

- Printed name: **OKES, H**
- Birth year: not printed
- Appears in editions: [1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1899-L36641.v` — printed in editions [1899, 1900, 1905]:**

> OKES, H.—C. C. and res. mag., Victoria E. div., Cape Col., Apr., 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | C. C. and res. mag., Victoria E. div. | Cape of Good Hope | [1899, 1900, 1905] |

## Candidate stint `Okes, Holt___Cape of Good Hope___1877`

- Staff-list name: **Okes, Holt** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | H. Okes | Clerk | Police Branch | — | — |
| 1878 | H. Okes | 1st Clerk | DIVISION OF COLESBERG | — | — |
| 1880 | H. Okes | Civil Commissioner and Resident Magistrate | DISTRICT OF WILLOWMORE | — | — |

### Deterministic checks: `okes_h_e1880-2` vs `Okes, Holt___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'OKES' vs stint 'Okes, Holt' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 54 vs bar 60: 'C. C. and res. mag., Victoria E. div.' ~ 'Civil Commissioner and Resident Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Okes, Holt___Cape of Good Hope___1890`

- Staff-list name: **Okes, Holt** | colony: **Cape of Good Hope** | listed 1890–1896 | editions [1890, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | H. Okes | C.C. and R.M. | DIVISION OF WILLOWMORE | — | — |
| 1896 | Holt Okes | R.M. | Division of Victoria West | — | — |

### Deterministic checks: `okes_h_e1880-2` vs `Okes, Holt___Cape of Good Hope___1890`

- [PASS] surname_gate: bio 'OKES' vs stint 'Okes, Holt' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1896
- [FAIL] position_sim: best 50 vs bar 60: 'C. C. and res. mag., Victoria E. div.' ~ 'C.C. and R.M.'
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

