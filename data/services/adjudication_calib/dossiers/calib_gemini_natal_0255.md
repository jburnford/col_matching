<!-- {"case_id": "calib_gemini_natal_0255", "bio_ids": ["lamond_george_e1853"], "stint_ids": ["Lamond, G___Natal___1879"]} -->
# Dossier calib_gemini_natal_0255

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lamond_george_e1853'] carry a single initial only — the namesake trap applies.

## Biography `lamond_george_e1853`

- Printed name: **LAMOND, GEORGE**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900]

### Verbatim printed entry text (OCR)

**Version `col1883-L28292.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900]:**

> LAMOND, GEORGE.—Postmaster at Compensation, Natal, 1853; clerk in the audit office, 1854; second clerk in the colonial secretary's office, 1859; 1st clerk, 1864; chief clerk, 1875; and registrar of deeds and distributor of stamps, and registrar-general of births, deaths, and marriages, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1853 | Postmaster at Compensation | Natal | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900] |
| 1 | 1854 | clerk in the audit office | Natal *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900] |
| 2 | 1859 | second clerk in the colonial secretary's office | Natal *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900] |
| 3 | 1864 | 1st clerk | Natal *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900] |
| 4 | 1875 | chief clerk | Natal *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900] |
| 5 | 1878 | and registrar of deeds and distributor of stamps, and registrar-general of births, deaths, and marriages | Natal *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900] |

## Candidate stint `Lamond, G___Natal___1879`

- Staff-list name: **Lamond, G** | colony: **Natal** | listed 1879–1900 | editions [1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | G. Lamond | Registrar of Deeds, and Registrar-General of Births, Deaths, and Marriages | Registrar of Deeds Department | — | — |
| 1880 | G. Lamond | Registrar of Deeds, and Registrar-General of Births, Deaths, and Marriages | Registrar of Deeds | — | — |
| 1883 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1886 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1888 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1889 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1890 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1894 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1896 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1898 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1899 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |
| 1900 | G. Lamond | Registrar of Deeds, and Registrar-General | Registrar of Deeds | — | — |

### Deterministic checks: `lamond_george_e1853` vs `Lamond, G___Natal___1879`

- [PASS] surname_gate: bio 'LAMOND' vs stint 'Lamond, G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1879-1900
- [PASS] position_sim: best 100 vs bar 60: 'and registrar of deeds and distributor of stamps, and registrar-general of births, deaths, and marriages' ~ 'Registrar of Deeds, and Registrar-General'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 5 agreeing edition-year(s) [1883, 1886, 1888, 1889, 1890] pos~100 (bar: >=2)
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

