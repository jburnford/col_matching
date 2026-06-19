<!-- {"case_id": "case_bamberger_a-n_e1881", "bio_ids": ["bamberger_a-n_e1881", "bamberger_a-n_e1881-2", "bamberger_n_e1881"], "stint_ids": ["Bamberger, A. N___Cape of Good Hope___1877"]} -->
# Dossier case_bamberger_a-n_e1881

## Case context

- 3 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bamberger_n_e1881'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Bamberger, A. N___Cape of Good Hope___1877'] have more than one claimant biography in this case.

## Biography `bamberger_a-n_e1881`

- Printed name: **BAMBERGER, A. N**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1886-L32028.v` — printed in editions [1886, 1888, 1889, 1890, 1896, 1897]:**

> BAMBERGER, A. N.—Resident magistrate, Bedford division, Cape Colony, 16th June, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Resident magistrate, Bedford division | Cape of Good Hope | [1886, 1888, 1889, 1890, 1896, 1897] |

## Biography `bamberger_a-n_e1881-2`

- Printed name: **BAMBERGER, A. N**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L32055.v` — printed in editions [1898]:**

> BAMBERGER, A. N.—Res. mag., Bedford div., Cape Colony, 16 June, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Res. mag., Bedford div. | Cape of Good Hope | [1898] |

## Biography `bamberger_n_e1881`

- Printed name: **BAMBERGER, N**
- Birth year: not printed
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L30141.v` — printed in editions [1894]:**

> BAMBERGER, N.—Resident magistrate, Bedford division, Cape Colony, 16th June, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Resident magistrate, Bedford division | Cape of Good Hope | [1894] |

## Candidate stint `Bamberger, A. N___Cape of Good Hope___1877`

- Staff-list name: **Bamberger, A. N** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. N. Bamberger | Accountant (the Beaufort Extension Railway) | Office of Railway Engineer | — | — |
| 1878 | A. N. Bamberger | Accountant (Beaufort Extension Railway) | Office of Railway Engineer | — | — |
| 1879 | A. N. Bamberger | Accountant and Paymaster | Beaufort Extension Railway | — | — |
| 1880 | A. N. Bamberger | Clerk and Paymaster | Beaufort Extension Railway | — | — |

### Deterministic checks: `bamberger_a-n_e1881` vs `Bamberger, A. N___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'BAMBERGER' vs stint 'Bamberger, A. N' (exact)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 42 vs bar 60: 'Resident magistrate, Bedford division' ~ 'Accountant (the Beaufort Extension Railway)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `bamberger_a-n_e1881-2` vs `Bamberger, A. N___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'BAMBERGER' vs stint 'Bamberger, A. N' (exact)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 37 vs bar 60: 'Res. mag., Bedford div.' ~ 'Accountant (the Beaufort Extension Railway)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `bamberger_n_e1881` vs `Bamberger, A. N___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'BAMBERGER' vs stint 'Bamberger, A. N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 42 vs bar 60: 'Resident magistrate, Bedford division' ~ 'Accountant (the Beaufort Extension Railway)'
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

