<!-- {"case_id": "case_hodgson_robert_e1872", "bio_ids": ["hodgson_robert_e1872"], "stint_ids": ["Hodgson, Robert R___Canada___1877"]} -->
# Dossier case_hodgson_robert_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 37 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hodgson_robert_e1872'] carry a single initial only — the namesake trap applies.

## Biography `hodgson_robert_e1872`

- Printed name: **HODGSON, ROBERT**
- Birth year: not printed
- Honours: KT. BACH (1869)
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L34049.v` — printed in editions [1888, 1889]:**

> HODGSON, Sir ROBERT, KT. BACH. (1869).—Chief justice, Nova Scotia, 1872; Lieutenant-Governor, 1878-9

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Chief justice | Nova Scotia | [1888, 1889] |
| 1 | 1878–1879 | Lieutenant-Governor | Nova Scotia *(inherited from previous clause)* | [1888, 1889] |

## Candidate stint `Hodgson, Robert R___Canada___1877`

- Staff-list name: **Hodgson, Robert R** | colony: **Canada** | listed 1877–1914 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. Robinson Hodgson | Private Secretary | Civil Establishment | — | — |
| 1877 | R. R. Hodgson | Provincial Aides-de-Camp | Civil Establishment | — | Lt.-Col. |
| 1877 | Robert R. Hodgson | Aides-de-Camp | Militia Establishment | — | Lt.-Col. |
| 1878 | R. Robinson Hodgson | Private Secretary | Civil Establishment | — | — |
| 1878 | R. R. Hodgson | Provincial Aides-de-Camp | Civil Establishment | — | Lt.-Col. |
| 1878 | Robert R. Hodgson | Aides-de-Camp | Militia Establishment | — | Lt.-Col. |
| 1879 | R. R. Hodgson | Provincial Aides-de-Camp | Civil Establishment | — | Lt.-Col. |
| 1879 | Robert R. Hodgson | Aides-de-Camp | Militia Establishment | — | Lt.-Col. |
| 1879 | R. Robinson Hodgson | Private Secretary | Civil Establishment | — | — |
| 1880 | R. R. Hodgson | Provincial Aide-de-Camp | Civil Establishment | — | Lieut.-Col. |

### Deterministic checks: `hodgson_robert_e1872` vs `Hodgson, Robert R___Canada___1877`

- [PASS] surname_gate: bio 'HODGSON' vs stint 'Hodgson, Robert R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1914
- [FAIL] position_sim: best 40 vs bar 60: 'Chief justice' ~ 'Private Secretary'
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

