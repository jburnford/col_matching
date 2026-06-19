<!-- {"case_id": "case_duff_grant-m-e_e1857", "bio_ids": ["duff_grant-m-e_e1857"], "stint_ids": ["Duff, G. M___Jamaica___1909"]} -->
# Dossier case_duff_grant-m-e_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `duff_grant-m-e_e1857`

- Printed name: **DUFF, GRANT, M. E.**
- Birth year: not printed
- Honours: F.R.S. (1880)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1886-L33156.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]:**

> DUFF, GRANT, THE Rt. Hon. M. E., P.C., G.C.S.I.; C.I.E., F.R.S. (1880).—Educated at Balliol College, Oxford, B.A. 1850; under-secretary of state for India, 1868 to 1874; lord rector of Aberdeen University, 1866 to 1872; parliamentary under secretary of state for the colonies, April 29, 1880, to Aug. 5, 1881; governor of Madras, 1881-6; M.P. for Elgin district, 1857 to 1881.

**Version `col1883-L27269.v` — printed in editions [1883]:**

> DUFF, GRANT, THE Rt. HON. M. E., M.P.—Parliamentary under secretary of state for the colonies, 29 April, 1880, to 5 August, 1881, when he was appointed governor of Madras.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857–1881 | M.P. | — | [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 1 | 1866–1872 | lord rector | — | [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 2 | 1868–1874 | under-secretary of state | India | [1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 3 | 1880–1881 | parliamentary under secretary of state for the colonies | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 4 | 1881–1886 | governor | Madras | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Duff, G. M___Jamaica___1909`

- Staff-list name: **Duff, G. M** | colony: **Jamaica** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | G. M. Duff | Secretary | Board of Education | — | — |
| 1910 | G. M. Duff (acting) | Secretary | Board of Education | — | — |

### Deterministic checks: `duff_grant-m-e_e1857` vs `Duff, G. M___Jamaica___1909`

- [PASS] surname_gate: bio 'DUFF' vs stint 'Duff, G. M' (exact)
- [PASS] initials: bio ['G', 'M', 'E'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1910
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

