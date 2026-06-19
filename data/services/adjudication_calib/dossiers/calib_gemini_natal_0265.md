<!-- {"case_id": "calib_gemini_natal_0265", "bio_ids": ["hyslop_j_e1882"], "stint_ids": ["Hyslop, J. H___Natal___1883"]} -->
# Dossier calib_gemini_natal_0265

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hyslop_j_e1882'] carry a single initial only — the namesake trap applies.

## Biography `hyslop_j_e1882`

- Printed name: **HYSLOP, J**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34162.v` — printed in editions [1886]:**

> HYSLOP, DR. J.—Resident surgeon, lunatic asylum, Pietermaritzburg, Natal, 4 July, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Resident surgeon, lunatic asylum, Pietermaritzburg | Natal | [1886] |

## Candidate stint `Hyslop, J. H___Natal___1883`

- Staff-list name: **Hyslop, J. H** | colony: **Natal** | listed 1883–1910 | editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1900, 1905, 1906, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | Dr. J. Hyslop | Resident Surgeon | Medical Department | — | — |
| 1886 | Dr. J. Hyslop | Resident Surgeon | Medical Department | — | — |
| 1888 | Dr. J. Hyslop | Resident Surgeon | Medical Department | — | — |
| 1889 | J. Hyslop | Resident Surgeon | Medical Department | — | — |
| 1890 | Dr. J. Hyslop | Medical Superintendent | Medical Department | — | — |
| 1894 | J. Hyslop | Medical Superintendent | Medical Department | — | — |
| 1896 | J. Hyslop | Medical Superintendent | Medical Department | — | — |
| 1898 | Dr. J. Hyslop | Medical Superintendent | Medical Department | — | — |
| 1900 | Dr. J. Hyslop | Medical Superintendent | Medical Department | — | — |
| 1905 | J. Hyslop | Medical Superintendent | Natal Government Asylum | D.S.O. | — |
| 1906 | J. Hyslop | Medical Superintendent | Medical Department | D.S.O. | — |
| 1907 | J. Hyslop | Medical Superintendent | Medical Department | D.S.O. | — |
| 1910 | J. Hyslop | Medical Superintendent | Medical Department | D.S.O. | — |

### Deterministic checks: `hyslop_j_e1882` vs `Hyslop, J. H___Natal___1883`

- [PASS] surname_gate: bio 'HYSLOP' vs stint 'Hyslop, J. H' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1910
- [PASS] position_sim: best 100 vs bar 60: 'Resident surgeon, lunatic asylum, Pietermaritzburg' ~ 'Resident Surgeon'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1886] pos~100 (bar: >=2)
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

