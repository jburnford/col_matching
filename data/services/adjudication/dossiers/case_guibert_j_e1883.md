<!-- {"case_id": "case_guibert_j_e1883", "bio_ids": ["guibert_j_e1883", "guibert_j_e1883-2"], "stint_ids": ["Guibert, J. A___Hong Kong___1906", "Guibert, J___Mauritius___1888"]} -->
# Dossier case_guibert_j_e1883

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['guibert_j_e1883', 'guibert_j_e1883-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Guibert, J___Mauritius___1888'] have more than one claimant biography in this case.
- Phase 1 found `guibert_j_e1883` ↔ `Guibert, J___Mauritius___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `guibert_j_e1883-2` ↔ `Guibert, J___Mauritius___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `guibert_j_e1883`

- Printed name: **GUIBERT, J**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1886-L33858.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896]:**

> GUIBERT, J.—Crown attorney and Queen's proctor, Mauritius, 1 July, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Crown attorney and Queen's proctor | Mauritius | [1886, 1888, 1889, 1890, 1894, 1896] |

## Biography `guibert_j_e1883-2`

- Printed name: **GUIBERT, J**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L32313.v` — printed in editions [1897]:**

> GUIBERT, J.—Crown attorney and queen's proctor, Mauritius, 1 July, 1883; ag. recvr. registrar, duns, June, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Crown attorney and queen's proctor | Mauritius | [1897] |
| 1 | 1896 | ag. recvr. registrar, duns | Mauritius *(inherited from previous clause)* | [1897] |

## Candidate stint `Guibert, J. A___Hong Kong___1906`

- Staff-list name: **Guibert, J. A** | colony: **Hong Kong** | listed 1906–1913 | editions [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | J. A. Guibert | vice-consul | Foreign Consuls | — | — |
| 1907 | J. A. Guibert | vice-consul | Foreign Consuls | — | — |
| 1908 | J. A. Guibert | Vice-Consul | Foreign Consuls | — | — |
| 1909 | J. A. Guibert | Vice-Consul | Foreign Consuls | — | — |
| 1910 | J. A. Guibert | Vice-Consul | Foreign Consuls | — | — |
| 1911 | J. A. Guibert | Vice-Consul | Foreign Consuls | — | — |
| 1912 | J. A. Guibert | vice-consul | Foreign Consuls | — | — |
| 1913 | J. A. Guibert | vice-consul | Foreign Consuls | — | — |

### Deterministic checks: `guibert_j_e1883-2` vs `Guibert, J. A___Hong Kong___1906`

- [PASS] surname_gate: bio 'GUIBERT' vs stint 'Guibert, J. A' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Guibert, J___Mauritius___1888`

- Staff-list name: **Guibert, J** | colony: **Mauritius** | listed 1888–1897 | editions [1888, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. Guibert | Crown Attorney | Procureur General's Department | — | — |
| 1890 | J. Guibert | Crown Attorney | Procureur General's Department | — | — |
| 1894 | J. Guibert | Crown Attorney | Procureur-General's Department | — | — |
| 1896 | J. Guibert | Crown Attorney | Procureur-General's Department | — | — |
| 1897 | J. Guibert | Receiver of Registration Dues and Conservator of Mortgages | Registration Office and Mortgage Department | — | — |

### Deterministic checks: `guibert_j_e1883` vs `Guibert, J___Mauritius___1888`

- [PASS] surname_gate: bio 'GUIBERT' vs stint 'Guibert, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1897
- [PASS] position_sim: best 100 vs bar 60: 'Crown attorney and Queen's proctor' ~ 'Crown Attorney'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1888, 1890, 1894, 1896] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `guibert_j_e1883-2` vs `Guibert, J___Mauritius___1888`

- [PASS] surname_gate: bio 'GUIBERT' vs stint 'Guibert, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1897
- [PASS] position_sim: best 100 vs bar 60: 'Crown attorney and queen's proctor' ~ 'Crown Attorney'
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

