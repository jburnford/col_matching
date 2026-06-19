<!-- {"case_id": "case_dias_harry_e1847", "bio_ids": ["dias_harry_e1847"], "stint_ids": ["Dias, H___Ceylon___1880"]} -->
# Dossier case_dias_harry_e1847

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dias_harry_e1847'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Dias, H___Ceylon___1880` is also gate-compatible with biography(ies) outside this case: ['dias_h_e1879'] (already linked elsewhere or filtered).

## Biography `dias_harry_e1847`

- Printed name: **DIAS, HARRY**
- Birth year: not printed
- Terminal: retired 1892 — “retired, July, 1892.”
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1894-L31223.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1900]:**

> DIAS, SIR HARRY, KNT. BACH., 1893.—Barrister-at-law, Middle Temple, 1847; jun. puiano justice, Ceylon, 5th July, 1879; retired, July, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1847 | Barrister-at-law, Middle Temple | — | [1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1879 | jun. puiano justice | Ceylon | [1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Dias, H___Ceylon___1880`

- Staff-list name: **Dias, H** | colony: **Ceylon** | listed 1880–1889 | editions [1880, 1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | Hon. H. Dias | Junior Puisme Judge | Judicial Establishment | — | — |
| 1883 | Hon. H. Dias | Junior Puise Judge | Judicial Establishment | — | — |
| 1886 | Hon. H. Dias | Junior Puisne Judge | Judicial Establishment | — | — |
| 1888 | H. Dias | Junior Puisne Judge | Judicial Establishment | — | — |
| 1889 | H. Dias | Junior Private Judge | Judicial Establishment | — | — |

### Deterministic checks: `dias_harry_e1847` vs `Dias, H___Ceylon___1880`

- [PASS] surname_gate: bio 'DIAS' vs stint 'Dias, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1889
- [FAIL] position_sim: best 59 vs bar 60: 'jun. puiano justice' ~ 'Junior Puisne Judge'
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

