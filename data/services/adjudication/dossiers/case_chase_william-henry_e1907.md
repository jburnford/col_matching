<!-- {"case_id": "case_chase_william-henry_e1907", "bio_ids": ["chase_william-henry_e1907"], "stint_ids": ["Chase, W. H___Bechuanaland___1906", "Chase, W. H___South Africa___1912"]} -->
# Dossier case_chase_william-henry_e1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Chase, W. H___Bechuanaland___1906` is also gate-compatible with biography(ies) outside this case: ['chase_william-henry_b1880'] (already linked elsewhere or filtered).
- NOTE: stint `Chase, W. H___South Africa___1912` is also gate-compatible with biography(ies) outside this case: ['chase_william-henry_b1880'] (already linked elsewhere or filtered).

## Biography `chase_william-henry_e1907`

- Printed name: **CHASE, WILLIAM HENRY**
- Birth year: not printed
- Honours: F.R.C.V.S., L.R.C.V.S.
- Appears in editions: [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1909-L44428.v` — printed in editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]:**

> CHASE, WILLIAM HENRY, F.R.C.V.S., L.R.C.V.S., 1907.—Gov. vet. surg., Bechuanaland Prot. (W.), hon. sub-inspr., Bechuanaland Prot. police.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | Gov. vet. surg., hon. sub-inspr. | Bechuanaland Protectorate | [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923] |

## Candidate stint `Chase, W. H___Bechuanaland___1906`

- Staff-list name: **Chase, W. H** | colony: **Bechuanaland** | listed 1906–1925 | editions [1906, 1907, 1909, 1911, 1917, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | W. H. Chase | Veterinary Surgeon | Civil Establishment | — | — |
| 1907 | W. H. Chase | Veterinary Surgeon | Establishment | — | — |
| 1909 | W. H. Chase | Veterinary Surgeon | Establishment | — | — |
| 1911 | W. H. Chase | Veterinary Surgeon | Establishment | — | — |
| 1917 | W. H. Chase | Chief Veterinary Surgeon | Establishment | — | — |
| 1921 | W. H. Chase | Chief Veterinary Surgeon | Establishment | — | — |
| 1922 | W. H. Chase | Chief Veterinary Surgeon | Establishment | — | — |
| 1924 | W. H. Chase | Chief Veterinary Surgeon | — | — | — |
| 1925 | W. H. Chase | Chief Veterinary Officer | Civil Establishment | — | — |

### Deterministic checks: `chase_william-henry_e1907` vs `Chase, W. H___Bechuanaland___1906`

- [PASS] surname_gate: bio 'CHASE' vs stint 'Chase, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1925
- [FAIL] position_sim: best 45 vs bar 60: 'Gov. vet. surg., hon. sub-inspr.' ~ 'Chief Veterinary Surgeon'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Chase, W. H___South Africa___1912`

- Staff-list name: **Chase, W. H** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | W. H. Chase | Veterinary Surgeon | Establishment | — | — |
| 1914 | W. H. Chase | Veterinary Surgeon | Civil Establishment | — | — |
| 1918 | W. H. Chase | Chief Veterinary Surgeon | Establishment | — | — |

### Deterministic checks: `chase_william-henry_e1907` vs `Chase, W. H___South Africa___1912`

- [PASS] surname_gate: bio 'CHASE' vs stint 'Chase, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
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

