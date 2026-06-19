<!-- {"case_id": "case_fenwick_w_e1920", "bio_ids": ["fenwick_w_e1920"], "stint_ids": ["Fenwick, W. H___Australia___1912", "Fenwick, W. H___South Australia___1888", "Fenwick, W. H___South Australia___1905"]} -->
# Dossier case_fenwick_w_e1920

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fenwick_w_e1920'] carry a single initial only — the namesake trap applies.

## Biography `fenwick_w_e1920`

- Printed name: **FENWICK, W**
- Birth year: not printed
- Appears in editions: [1927]

### Verbatim printed entry text (OCR)

**Version `col1927-L58832.v` — printed in editions [1927]:**

> FENWICK, CAPT. W.—Ast. dist. comsnr., Kenya, May, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | Ast. dist. comsnr. | Kenya | [1927] |

## Candidate stint `Fenwick, W. H___Australia___1912`

- Staff-list name: **Fenwick, W. H** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | W. H. Fenwick | Valuator | Engineer-in-Chief's Department | — | — |
| 1913 | W. H. Fenwick | Valuator | Engineer-in-Chief's Department | — | — |
| 1918 | W. H. Fenwick | Valuator | Engineering Department | — | — |

### Deterministic checks: `fenwick_w_e1920` vs `Fenwick, W. H___Australia___1912`

- [PASS] surname_gate: bio 'FENWICK' vs stint 'Fenwick, W. H' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fenwick, W. H___South Australia___1888`

- Staff-list name: **Fenwick, W. H** | colony: **South Australia** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | W. H. Fenwick | Clerk | Waterworks Department—Revenue Division | — | — |
| 1889 | W. H. Fenwick | Clerk | Waterworks Department—Revenue Division | — | — |

### Deterministic checks: `fenwick_w_e1920` vs `Fenwick, W. H___South Australia___1888`

- [PASS] surname_gate: bio 'FENWICK' vs stint 'Fenwick, W. H' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fenwick, W. H___South Australia___1905`

- Staff-list name: **Fenwick, W. H** | colony: **South Australia** | listed 1905–1917 | editions [1905, 1906, 1907, 1908, 1909, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. H. Fenwick | Clerks | Engineer-in-Chief's Department | — | — |
| 1906 | W. H. Fenwick | Clerks | Engineer-in-Chief's Department | — | — |
| 1907 | W. H. Fenwick | Clerks | Engineer-in-Chief's Department | — | — |
| 1908 | W. H. Fenwick | Clerk | Engineer-in-Chief's Department | — | — |
| 1909 | W. H. Fenwick | Clerks | Engineer-in-Chief's Department | — | — |
| 1917 | W. H. Fenwick | Valuator | Engineering Department | — | — |

### Deterministic checks: `fenwick_w_e1920` vs `Fenwick, W. H___South Australia___1905`

- [PASS] surname_gate: bio 'FENWICK' vs stint 'Fenwick, W. H' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1917
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

