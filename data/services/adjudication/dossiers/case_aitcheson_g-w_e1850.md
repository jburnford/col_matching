<!-- {"case_id": "case_aitcheson_g-w_e1850", "bio_ids": ["aitcheson_g-w_e1850"], "stint_ids": ["Aitchison, G. W___Cape of Good Hope___1877"]} -->
# Dossier case_aitcheson_g-w_e1850

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Aitchison, G. W___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['aitchison_g-w_e1850'] (already linked elsewhere or filtered).

## Biography `aitcheson_g-w_e1850`

- Printed name: **AITCHESON, G. W**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26147.v` — printed in editions [1883, 1886]:**

> AITCHESON, G. W.—Was in the post-office 1850 to 1853, and audit office 1853 to 1857; secretary and accountant-in-general, General Post Office, Cape, 1860 to 1868; civil commissioner and resident magistrate of Tullbagh Division, 1869; Postmaster General, Cape, 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850–1853 | Was in the post-office | — | [1883, 1886] |
| 1 | 1853–1857 | audit office | — | [1883, 1886] |
| 2 | 1860–1868 | secretary and accountant-in-general, General Post Office | Cape of Good Hope | [1883, 1886] |
| 3 | 1869 | civil commissioner and resident magistrate of Tullbagh Division | Cape of Good Hope *(inherited from previous clause)* | [1883, 1886] |
| 4 | 1873 | Postmaster General | Cape of Good Hope | [1883, 1886] |

## Candidate stint `Aitchison, G. W___Cape of Good Hope___1877`

- Staff-list name: **Aitchison, G. W** | colony: **Cape of Good Hope** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. W. Aitchison | Postmaster-General | General Post-Office | — | — |
| 1878 | G. W. Aitchison | Postmaster-General | General Post Office | — | — |
| 1879 | G. W. Aitchison | Postmaster-General | General Post Office | — | — |
| 1880 | G. W. Aitchison | Postmaster-General | General Post Office | — | — |
| 1883 | G. W. Aitchison | Postmaster-General | General Post Office | — | — |
| 1888 | G. W. Aitchison | Postmaster-General | General Post Office | — | — |
| 1889 | G. W. Aitchison | Postmaster-General | General Post Office | — | — |
| 1890 | G. W. Aitchison | Postmaster-General | General Post Office | — | — |

### Deterministic checks: `aitcheson_g-w_e1850` vs `Aitchison, G. W___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'AITCHESON' vs stint 'Aitchison, G. W' (fuzzy:1)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1890
- [FAIL] position_sim: best 57 vs bar 60: 'Postmaster General' ~ 'Postmaster-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1883] pos~57 (bar: >=2)
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

