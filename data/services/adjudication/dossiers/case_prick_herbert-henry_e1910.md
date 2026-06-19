<!-- {"case_id": "case_prick_herbert-henry_e1910", "bio_ids": ["prick_herbert-henry_e1910"], "stint_ids": ["Price, H. H___Bechuanaland___1911", "Price, H. H___South Africa___1912"]} -->
# Dossier case_prick_herbert-henry_e1910

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Price, H. H___Bechuanaland___1911` is also gate-compatible with biography(ies) outside this case: ['price_herbert-henry_e1910', 'price_herbert-henry_e1910-2'] (already linked elsewhere or filtered).
- NOTE: stint `Price, H. H___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['price_herbert-henry_e1910', 'price_herbert-henry_e1910-2'] (already linked elsewhere or filtered).

## Biography `prick_herbert-henry_e1910`

- Printed name: **PRICK, HERBERT HENRY**
- Birth year: not printed
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L62418.v` — printed in editions [1934]:**

> PRICK, HERBERT HENRY.—2nd cls. to asst. comrn'r., Northern Div., Bech. Prot., 1910; 2nd cls., res. comrn'r. office, 1st May, 1912; passed Cape civ. ser. lower law exam., 1910; ag. asst. res. mag., 1911-12; reg'ar. of brands, 1913; 2nd cls. and reg'ar., 1921; passed 3rd grade Sewards exam., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | 2nd cls. to asst. comrn'r., Northern Div. | Bechuanaland | [1934] |
| 1 | 1911–1912 | ag. asst. res. mag | Bechuanaland *(inherited from previous clause)* | [1934] |
| 2 | 1912 | 2nd cls., res. comrn'r. office | Bechuanaland *(inherited from previous clause)* | [1934] |
| 3 | 1913 | reg'ar. of brands | Bechuanaland *(inherited from previous clause)* | [1934] |
| 4 | 1921 | 2nd cls. and reg'ar | Bechuanaland *(inherited from previous clause)* | [1934] |
| 5 | 1927 | passed 3rd grade Sewards exam | Bechuanaland *(inherited from previous clause)* | [1934] |

## Candidate stint `Price, H. H___Bechuanaland___1911`

- Staff-list name: **Price, H. H** | colony: **Bechuanaland** | listed 1911–1925 | editions [1911, 1917, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | H. Price | Clerk | Establishment | — | — |
| 1917 | H. H. Price | Clerk | Establishment | — | — |
| 1921 | H. H. Price | Clerk | Establishment | — | — |
| 1922 | H. H. Price | Chief Clerk and Registrar | Establishment | — | — |
| 1924 | H. H. Price | Chief Clerk and Registrar | — | — | — |
| 1925 | H. H. Price | Chief Clerk and Registrar | Civil Establishment | — | — |

### Deterministic checks: `prick_herbert-henry_e1910` vs `Price, H. H___Bechuanaland___1911`

- [PASS] surname_gate: bio 'PRICK' vs stint 'Price, H. H' (fuzzy:1)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1911-1925
- [PASS] position_sim: best 62 vs bar 60: '2nd cls. and reg'ar' ~ 'Chief Clerk and Registrar'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Price, H. H___South Africa___1912`

- Staff-list name: **Price, H. H** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | H. Price | Clerk | Establishment | — | — |
| 1914 | H. H. Price | Clerk | Civil Establishment | — | — |
| 1918 | H. H. Price | Clerk | Establishment | — | — |

### Deterministic checks: `prick_herbert-henry_e1910` vs `Price, H. H___South Africa___1912`

- [PASS] surname_gate: bio 'PRICK' vs stint 'Price, H. H' (fuzzy:1)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

