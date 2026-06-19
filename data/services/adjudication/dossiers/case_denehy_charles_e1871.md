<!-- {"case_id": "case_denehy_charles_e1871", "bio_ids": ["denehy_charles_e1871"], "stint_ids": ["Dennehy, Charles___St Lucia___1879"]} -->
# Dossier case_denehy_charles_e1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['denehy_charles_e1871'] carry a single initial only — the namesake trap applies.
- Phase 1 found `denehy_charles_e1871` ↔ `Dennehy, Charles___St Lucia___1879` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Dennehy, Charles___St Lucia___1879` is also gate-compatible with biography(ies) outside this case: ['dennehy_charles_e1871'] (already linked elsewhere or filtered).

## Biography `denehy_charles_e1871`

- Printed name: **DENEHY, CHARLES**
- Birth year: not printed
- Honours: F.R.C.S. (Edin.) (1883)
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L33580.v` — printed in editions [1890]:**

> DENEHY, CHARLES, M.R.C.S.I., L.A.R.C.S.I., L.A., Rotunda, Dublin, F.R.C.S. (Edin.), 1883.—Medical officer, St. Mary's District, Antigua, Jan., 1871; medical officer and registrar, St. Philip's, Aug., 1875; colonial surgeon, St. Lucia, May, 1877; health officer, Castries, Sept., 1877; principal medical officer for immigration, 1878: J.P., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Medical officer | Antigua | [1890] |
| 1 | 1875 | medical officer and registrar | — | [1890] |
| 2 | 1877 | colonial surgeon | St. Lucia | [1890] |
| 3 | 1877 | health officer | — | [1890] |
| 4 | 1878 | principal medical officer for immigration | — | [1890] |
| 5 | 1885 | J.P. | — | [1890] |

## Candidate stint `Dennehy, Charles___St Lucia___1879`

- Staff-list name: **Dennehy, Charles** | colony: **St Lucia** | listed 1879–1899 | editions [1879, 1880, 1888, 1890, 1894, 1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Charles Dennehy | Colonial Surgeon | Civil Establishment | — | — |
| 1880 | Charles Dennehy | Colonial Surgeon | Civil Establishment | — | — |
| 1888 | Charles Dennehy | Immigration Medical Officer | Immigration | — | — |
| 1888 | Charles Dennehy | Colonial Surgeon | Medical | — | — |
| 1890 | Charles Dennehy | Colonial Surgeon | Medical | — | — |
| 1890 | Charles Dennehy | Immigration Medical Officer | Immigration | — | — |
| 1894 | Charles Dennehy | Colonial Surgeon | Medical | — | — |
| 1894 | Charles Dennehy | Immigration Medical Officer | Immigration | — | — |
| 1896 | Charles Dennehy | Immigration Medical Officer | Immigration | — | — |
| 1896 | Charles Dennehy | Colonial Surgeon | Medical | — | — |
| 1897 | Charles Dennehy | Immigration Medical Officers | Immigration | — | — |
| 1898 | Charles Dennehy | Immigration Medical Officer | Immigration | — | — |
| 1898 | Chas. Dennehy | Colonial Surgeon | Medical | — | — |
| 1899 | Charles Dennehy | Immigration Medical Officers | Immigration | — | — |
| 1899 | Charles Dennehy | Colonial Surgeon | Medical | — | — |

### Deterministic checks: `denehy_charles_e1871` vs `Dennehy, Charles___St Lucia___1879`

- [PASS] surname_gate: bio 'DENEHY' vs stint 'Dennehy, Charles' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Lucia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1899
- [PASS] position_sim: best 100 vs bar 60: 'colonial surgeon' ~ 'Colonial Surgeon'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1890] pos~100 (bar: >=2)
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

