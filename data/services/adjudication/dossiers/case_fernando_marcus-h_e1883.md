<!-- {"case_id": "case_fernando_marcus-h_e1883", "bio_ids": ["fernando_marcus-h_e1883"], "stint_ids": ["Fernando, M___Fiji___1897"]} -->
# Dossier case_fernando_marcus-h_e1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Fernando, M___Fiji___1897` is also gate-compatible with biography(ies) outside this case: ['fernando_hilary-marcus_b1864'] (already linked elsewhere or filtered).

## Biography `fernando_marcus-h_e1883`

- Printed name: **FERNANDO, MARCUS H.**
- Birth year: not printed
- Appears in editions: [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1899-L34799.v` — printed in editions [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910]:**

> FERNANDO, MARCUS H.—Ed. Royal Coll., Colombo, and Univ. Coll., Lond.; Ceylon Govt. Univ. and Gilchrist scholar, 1883; B.Sc., 1886; M.B., 1888; gold medallist in med. and forensic med.; M.D., 1889; fellow of Univ. Coll., Lond., 1890; col. surg., civil med. dept., Ceylon; registr. of Ceylon Med. Coll., lecturer on pathology, 1890, and analyst to govt. of Ceylon; reported on epidemics of malarial fever, 1895; also in Bombay, 1897, on epidemics of plague; physician, gen. hosps., Colombo, 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883–1883 | Ceylon Govt. Univ. and Gilchrist scholar | Ceylon | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 1 | 1886–1886 | B.Sc. | — | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 2 | 1888–1888 | M.B. | — | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 3 | 1889–1889 | M.D. | — | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 4 | 1890–1890 | fellow | — | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 5 | 1890–1890 | registr. of Ceylon Med. Coll., lecturer on pathology, and analyst to govt. | Ceylon | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 6 | 1895–1895 | — | — | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 7 | 1897–1897 | — | Bombay | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |
| 8 | 1897–1897 | physician, gen. hosps. | Ceylon | [1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |

## Candidate stint `Fernando, M___Fiji___1897`

- Staff-list name: **Fernando, M** | colony: **Fiji** | listed 1897–1906 | editions [1897, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | M. Fernando | — | Printing Office | — | — |
| 1898 | M. Fernando | Compositor | Printing Office | — | — |
| 1899 | M. Fernando | Compositors | Printing Office | — | — |
| 1900 | M. Fernando | Compositor | Printing Office | — | — |
| 1905 | M. Fernando | Composer | Printing Office | — | — |
| 1906 | M. Fernando | Compositor | Printing Office | — | — |

### Deterministic checks: `fernando_marcus-h_e1883` vs `Fernando, M___Fiji___1897`

- [PASS] surname_gate: bio 'FERNANDO' vs stint 'Fernando, M' (exact)
- [PASS] initials: bio ['M', 'H'] ~ stint ['M']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1906
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

