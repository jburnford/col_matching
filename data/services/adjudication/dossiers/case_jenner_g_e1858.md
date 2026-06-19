<!-- {"case_id": "case_jenner_g_e1858", "bio_ids": ["jenner_g_e1858"], "stint_ids": ["Jenner, G___Mauritius___1877"]} -->
# Dossier case_jenner_g_e1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['jenner_g_e1858'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Jenner, G___Mauritius___1877` is also gate-compatible with biography(ies) outside this case: ['jenner_g_e1875'] (already linked elsewhere or filtered).

## Biography `jenner_g_e1858`

- Printed name: **JENNER, G**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34217.v` — printed in editions [1888, 1889, 1890]:**

> JENNER, G.—Served in the army for nine and a-half years, Crimean medals with clasps, Alma, Inkerman, and Sebastopol; inspector of police, Mauritius, Feb., 1858; police magistrate, Rodrigues, April, 1862; inspector of immigrants, May, 1872; district and stipendiary magistrate of the lesser dependencies, June, 1874; sanitary warden of Port Louis, Jan., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | inspector of police | Mauritius | [1888, 1889, 1890] |
| 1 | 1862 | police magistrate | Rodrigues | [1888, 1889, 1890] |
| 2 | 1872 | inspector of immigrants | Rodrigues *(inherited from previous clause)* | [1888, 1889, 1890] |
| 3 | 1874 | district and stipendiary magistrate of the lesser dependencies | Rodrigues *(inherited from previous clause)* | [1888, 1889, 1890] |
| 4 | 1875 | sanitary warden of Port Louis | Rodrigues *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Jenner, G___Mauritius___1877`

- Staff-list name: **Jenner, G** | colony: **Mauritius** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1883, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. Jenner | Sanitary Warden | General Board of Health Office | — | — |
| 1878 | G. Jenner | Sanitary Warden | General Board of Health Office | — | — |
| 1879 | G. Jenner | Sanitary Warden | General Board of Health Office | — | — |
| 1880 | G. Jenner | Sanitary Warden | General Board of Health Office | — | — |
| 1883 | G. Jenner | Sanitary Warden | General Board of Health Office | — | — |
| 1888 | G. Jenner | Sanitary Warden | General Board of Health Office | — | — |

### Deterministic checks: `jenner_g_e1858` vs `Jenner, G___Mauritius___1877`

- [PASS] surname_gate: bio 'JENNER' vs stint 'Jenner, G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

