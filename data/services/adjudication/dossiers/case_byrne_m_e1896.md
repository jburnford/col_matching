<!-- {"case_id": "case_byrne_m_e1896", "bio_ids": ["byrne_m_e1896"], "stint_ids": ["Byrne, M___Victoria___1894"]} -->
# Dossier case_byrne_m_e1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['byrne_m_e1896'] carry a single initial only — the namesake trap applies.
- Phase 1 found `byrne_m_e1896` ↔ `Byrne, M___Victoria___1894` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Byrne, M___Victoria___1894` is also gate-compatible with biography(ies) outside this case: ['byrne_m_e1894'] (already linked elsewhere or filtered).

## Biography `byrne_m_e1896`

- Printed name: **BYRNE, M.**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900, 1905, 1906, 1908]

### Verbatim printed entry text (OCR)

**Version `col1898-L32492.v` — printed in editions [1898, 1899, 1900, 1905, 1906, 1908]:**

> BYRNE, M.—Sec. to law dept., Victoria, Oct., 1896. Formerly ch. clk. in same dept.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896 | Sec. to law dept. | Victoria | [1898, 1899, 1900, 1905, 1906, 1908] |

## Candidate stint `Byrne, M___Victoria___1894`

- Staff-list name: **Byrne, M** | colony: **Victoria** | listed 1894–1906 | editions [1894, 1897, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | M. Byrne | Chief Clerk | Attorney-General's Department | — | — |
| 1897 | M. Byrne | Chief Clerk | Attorney-General's Department | — | — |
| 1898 | M. Byrne | Secretary to the Law Department | Attorney-General's Department | — | — |
| 1899 | M. Byrne | Secretary to the Law Department | Attorney-General's Department | — | — |
| 1900 | M. Byrne | Secretary to the Law Department | ATTORNEY-GENERAL'S DEPARTMENT. | — | — |
| 1905 | M. Byrne | Secretary to the Law Department | Attorney-General's Department | — | — |
| 1906 | M. Byrne | Secretary to the Law Department | Attorney-General's Department | — | — |

### Deterministic checks: `byrne_m_e1896` vs `Byrne, M___Victoria___1894`

- [PASS] surname_gate: bio 'BYRNE' vs stint 'Byrne, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1906
- [PASS] position_sim: best 65 vs bar 60: 'Sec. to law dept.' ~ 'Secretary to the Law Department'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 5 agreeing edition-year(s) [1898, 1899, 1900, 1905, 1906] pos~65 (bar: >=2)
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

