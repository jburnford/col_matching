<!-- {"case_id": "case_bain_arthur-humbert_e1895", "bio_ids": ["bain_arthur-humbert_e1895"], "stint_ids": ["Bain, A. H___Cape of Good Hope___1898", "Bain, A___Northern Nigeria___1905"]} -->
# Dossier case_bain_arthur-humbert_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bain_arthur-humbert_e1895`

- Printed name: **BAIN, ARTHUR HUMBERT**
- Birth year: not printed
- Appears in editions: [1933, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1933-L57573.v` — printed in editions [1933, 1935, 1936, 1937]:**

> BAIN, ARTHUR HUMBERT.—Clk., Sept., 1895; examr., deeds, April, 1912; 1st gr. examr., deeds, Oct., 1919; astl. regnr., deeds, King Williamstown, Nov., 1919; astl. regnr., deeds, Natal, Jan., 1926; astl. regnr., deeds, Cape Town, Oct., 1928; regnr., deeds, Natal, Jan., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | Clk | — | [1933, 1935, 1936, 1937] |
| 1 | 1912 | examr., deeds | — | [1933, 1935, 1936, 1937] |
| 2 | 1919 | 1st gr. examr., deeds | — | [1933, 1935, 1936, 1937] |
| 3 | 1919 | astl. regnr., deeds, King Williamstown | — | [1933, 1935, 1936, 1937] |
| 4 | 1926 | astl. regnr., deeds | Natal | [1933, 1935, 1936, 1937] |
| 5 | 1928 | astl. regnr., deeds, Cape Town | Cape of Good Hope | [1933, 1935, 1936, 1937] |
| 6 | 1932 | regnr., deeds | Natal | [1933, 1935, 1936, 1937] |

## Candidate stint `Bain, A. H___Cape of Good Hope___1898`

- Staff-list name: **Bain, A. H** | colony: **Cape of Good Hope** | listed 1898–1909 | editions [1898, 1899, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | A. H. Bain | Clerk | Surveyor-General's Office | — | — |
| 1899 | A. H. Bain | Clerk | Surveyor-General's Office | — | — |
| 1905 | A. H. Bain | Clerk | Deeds Office | — | — |
| 1906 | A. H. Bain | Clerk | Deeds Office | — | — |
| 1907 | A. H. Bain | Clerk | Deeds Office | — | — |
| 1908 | A. H. Bain | Clerk | Deeds Office | — | — |
| 1909 | A. H. Bain | Clerk | Deeds Office | — | — |

### Deterministic checks: `bain_arthur-humbert_e1895` vs `Bain, A. H___Cape of Good Hope___1898`

- [PASS] surname_gate: bio 'BAIN' vs stint 'Bain, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bain, A___Northern Nigeria___1905`

- Staff-list name: **Bain, A** | colony: **Northern Nigeria** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. Bain | Commissioner and Sheriff | Police and Prisons | — | Major |
| 1906 | Major A. Bain | Commissioner and Sheriff | Police and Prisons | — | Major |
| 1907 | A. Bain | Commissioner and Sheriff | Constabulary and Prisons | — | Major |
| 1908 | Major A. Bain | Commissioner and Sheriff | Constabulary and Prisons | — | Major |

### Deterministic checks: `bain_arthur-humbert_e1895` vs `Bain, A___Northern Nigeria___1905`

- [PASS] surname_gate: bio 'BAIN' vs stint 'Bain, A' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Northern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1908
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

