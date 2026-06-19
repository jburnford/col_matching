<!-- {"case_id": "case_heasman_r-b_e1947", "bio_ids": ["heasman_r-b_e1947", "heasman_r-b_e1947-2"], "stint_ids": ["Heasman, R. B___Federation of Malaya___1949"]} -->
# Dossier case_heasman_r-b_e1947

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Heasman, R. B___Federation of Malaya___1949'] have more than one claimant biography in this case.
- Phase 1 found `heasman_r-b_e1947` ↔ `Heasman, R. B___Federation of Malaya___1949` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `heasman_r-b_e1947-2` ↔ `Heasman, R. B___Federation of Malaya___1949` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `heasman_r-b_e1947`

- Printed name: **HEASMAN, R. B**
- Birth year: not printed
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32797.v` — printed in editions [1949, 1950, 1951]:**

> HEASMAN, R. B.—compt.-gen. of inc. tax, Mal., 1947 (on temp. trans. fr. Bd. of Inl. Rev.).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | compt.-gen. of inc. tax | Malaya | [1949, 1950, 1951] |

## Biography `heasman_r-b_e1947-2`

- Printed name: **HEASMAN, R. B**
- Birth year: not printed
- Appears in editions: [1953]

### Verbatim printed entry text (OCR)

**Version `col1953-L17663.v` — printed in editions [1953]:**

> HEASMAN, R. B.—compt.-gen. of inc. tax, Mal., 1947 (trans. fr. home C.S.); compt.-gen., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | compt.-gen. of inc. tax | Malaya | [1953] |
| 1 | 1949 | compt.-gen | Malaya *(inherited from previous clause)* | [1953] |

## Candidate stint `Heasman, R. B___Federation of Malaya___1949`

- Staff-list name: **Heasman, R. B** | colony: **Federation of Malaya** | listed 1949–1952 | editions [1949, 1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. B. Heasman | Comptroller-General of Income Tax | Civil Establishment | — | — |
| 1950 | R. B. Heasman | Comptroller-General of Income Tax | Civil Establishment | — | — |
| 1951 | R. B. Heasman | Comptroller-General of Income Tax | INCOME TAX | — | — |
| 1952 | R. B. Heasman | Comptroller-General of Income Tax* | Civil Establishment | — | — |

### Deterministic checks: `heasman_r-b_e1947` vs `Heasman, R. B___Federation of Malaya___1949`

- [PASS] surname_gate: bio 'HEASMAN' vs stint 'Heasman, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Federation of Malaya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1952
- [PASS] position_sim: best 75 vs bar 60: 'compt.-gen. of inc. tax' ~ 'Comptroller-General of Income Tax'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1949, 1950, 1951] pos~75 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `heasman_r-b_e1947-2` vs `Heasman, R. B___Federation of Malaya___1949`

- [PASS] surname_gate: bio 'HEASMAN' vs stint 'Heasman, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Federation of Malaya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1952
- [PASS] position_sim: best 75 vs bar 60: 'compt.-gen. of inc. tax' ~ 'Comptroller-General of Income Tax'
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

