<!-- {"case_id": "case_sinclair_a-d_b1904", "bio_ids": ["sinclair_a-d_b1904", "sinclair_augustus-o_e1861"], "stint_ids": ["Sinclair, A___Gambia___1949"]} -->
# Dossier case_sinclair_a-d_b1904

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 49 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Sinclair, A___Gambia___1949'] have more than one claimant biography in this case.
- NOTE: stint `Sinclair, A___Gambia___1949` is also gate-compatible with biography(ies) outside this case: ['sinclair_augustus-c_e1866'] (already linked elsewhere or filtered).
- NOTE: stint `Sinclair, A___Gambia___1949` is also gate-compatible with biography(ies) outside this case: ['sinclair_augustus-c_e1866'] (already linked elsewhere or filtered).

## Biography `sinclair_a-d_b1904`

- Printed name: **SINCLAIR, A. D**
- Birth year: 1904 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L27900.v` — printed in editions [1959, 1960, 1961, 1962]:**

> SINCLAIR, A. D.—b. 1904; ed. Aberdeen Univ.; surgn. capt., R.N., 1953; med. supt., gen. hosp., Barb., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | surgn. capt., R.N | — | [1959, 1960, 1961, 1962] |
| 1 | 1958 | med. supt., gen. hosp. | Barbados | [1959, 1960, 1961, 1962] |

## Biography `sinclair_augustus-o_e1861`

- Printed name: **SINCLAIR, AUGUSTUS O**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L36051.v` — printed in editions [1888, 1889, 1890]:**

> SINCLAIR, AUGUSTUS O.—Secretary to hospital and lunatic asylum commission, Jamaica, 1861; to Kingston fire commission, 1862; to post office commission, 1866; chief and pay clerk, constabulary, 1866; superintendent, government printing establishment, July, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1861 | Secretary to hospital and lunatic asylum commission | Jamaica | [1888, 1889, 1890] |
| 1 | 1862 | to Kingston fire commission | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1866 | to post office commission | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890] |
| 3 | 1879 | superintendent, government printing establishment | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Sinclair, A___Gambia___1949`

- Staff-list name: **Sinclair, A** | colony: **Gambia** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. Sinclair | Commissioner | ADMINISTRATIVE SERVICE (including Secretariat) | — | — |
| 1950 | A. Sinclair | Senior Assistant Secretary | Administrative Service | — | — |
| 1951 | A. Sinclair | Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries | Administrative Service | — | — |

### Deterministic checks: `sinclair_a-d_b1904` vs `Sinclair, A___Gambia___1949`

- [PASS] surname_gate: bio 'SINCLAIR' vs stint 'Sinclair, A' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `sinclair_augustus-o_e1861` vs `Sinclair, A___Gambia___1949`

- [PASS] surname_gate: bio 'SINCLAIR' vs stint 'Sinclair, A' (exact)
- [PASS] initials: bio ['A', 'O'] ~ stint ['A']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

