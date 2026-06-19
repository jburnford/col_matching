<!-- {"case_id": "case_pinder_john-hothersall_e1887", "bio_ids": ["pinder_john-hothersall_e1887"], "stint_ids": ["Pinder, H___South Australia___1894"]} -->
# Dossier case_pinder_john-hothersall_e1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pinder_john-hothersall_e1887`

- Printed name: **PINDER, JOHN HOTHERSALL**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1905-L45310.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911]:**

> PINDER, JOHN HOTHERSALL.—Ed. Marl. Coll. and Caius Coll., Camb., M.A. (2nd cl. class. trip.); admitted solicitor (Eng.) 1887; ch. registr., Lagos, 1901; called to the bar, Linc.’s Inn, 1904; dist. comsnr., Lagos, 1904.

**Version `col1912-L46925.v` — printed in editions [1912]:**

> PINDER, JOHN HOTHERSALL.—Ed. at Caius Coll., Camb., M.A. (2nd cl. class admitted solicitor (Eng.) 1887; ch. regtr., 1901; called to the bar, Linc.'s Inn, 1901; Comsnr., Lagos, 1904.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887 | admitted solicitor (Eng.) | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911] |
| 1 | 1901 | ch. registr. | Lagos | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 2 | 1901 | called to the bar, Linc.'s Inn | — | [1912] |
| 3 | 1904 | called to the bar, Linc.’s Inn | Lagos | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Pinder, H___South Australia___1894`

- Staff-list name: **Pinder, H** | colony: **South Australia** | listed 1894–1900 | editions [1894, 1896, 1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | H. Pinder | Landing Waiter | Northern Territory | — | — |
| 1896 | H. Pinder | Landing Wailer | Northern Territory | — | — |
| 1898 | H. Pinder | Landing Waiter | Northern Territory | — | — |
| 1900 | H. Pinder | Landing Waiter | Northern Territory | — | — |

### Deterministic checks: `pinder_john-hothersall_e1887` vs `Pinder, H___South Australia___1894`

- [PASS] surname_gate: bio 'PINDER' vs stint 'Pinder, H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
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

