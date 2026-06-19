<!-- {"case_id": "case_brownrigg_m_e1866", "bio_ids": ["brownrigg_m_e1866"], "stint_ids": ["Brownrigg, M. E___Mauritius___1878"]} -->
# Dossier case_brownrigg_m_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['brownrigg_m_e1866'] carry a single initial only — the namesake trap applies.
- Phase 1 found `brownrigg_m_e1866` ↔ `Brownrigg, M. E___Mauritius___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Brownrigg, M. E___Mauritius___1878` is also gate-compatible with biography(ies) outside this case: ['brownrigg_m-e_e1866'] (already linked elsewhere or filtered).

## Biography `brownrigg_m_e1866`

- Printed name: **BROWNRIGG, M**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1886-L32392.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896]:**

> BROWNRIGG, M.—Police inspector, Mauritius, February, 1866; sanitary guardian, 1st January, 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Police inspector | Mauritius | [1886, 1888, 1889, 1890, 1894, 1896] |
| 1 | 1875 | sanitary guardian | Mauritius *(inherited from previous clause)* | [1886, 1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Brownrigg, M. E___Mauritius___1878`

- Staff-list name: **Brownrigg, M. E** | colony: **Mauritius** | listed 1878–1896 | editions [1878, 1879, 1880, 1883, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | M. Brownrigg | Sanitary Guardian | General Board of Health Office | — | — |
| 1879 | Brownrigg | Inspector | Police Department | — | — |
| 1879 | M. Brownrigg | Sanitary Guardian | General Board of Health Office | — | — |
| 1880 | M. Brownrigg | Sanitary Guardian | General Board of Health Office | — | — |
| 1883 | M. Brownrigg | Sanitary Guardian | Sanitary Guardians | — | — |
| 1888 | M. Brownrigg | Sanitary Guardian | General Board of Health Office | — | — |
| 1889 | M. Brownrigg | Sanitary Guardian | General Board of Health Office | — | — |
| 1890 | M. Brownrigg | Sanitary Guardian | Sanitary Guardians | — | — |
| 1894 | M. Brownrigg | Sanitary Guardians | General Board of Health Office | — | — |
| 1896 | M. Brownrigg | Sanitary Guardians | General Board of Health Office | — | — |

### Deterministic checks: `brownrigg_m_e1866` vs `Brownrigg, M. E___Mauritius___1878`

- [PASS] surname_gate: bio 'BROWNRIGG' vs stint 'Brownrigg, M. E' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M', 'E']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1896
- [PASS] position_sim: best 100 vs bar 60: 'sanitary guardian' ~ 'Sanitary Guardian'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1888, 1889] pos~100 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

