<!-- {"case_id": "case_ker_alan_e1842", "bio_ids": ["ker_alan_e1842"], "stint_ids": ["Ker, Alan___Jamaica___1877"]} -->
# Dossier case_ker_alan_e1842

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ker_alan_e1842'] carry a single initial only — the namesake trap applies.

## Biography `ker_alan_e1842`

- Printed name: **KER, Alan**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L28208.v` — printed in editions [1883, 1886]:**

> KER, Alan.—Called to the bar at the Middle Temple, Nov. 1842; chief justice of Nevis, 1854; chief justice of Dominica, 1856; and assistant judge of the supreme court of Jamaica, 1861; acted as attorney-general of Antigua, from August, 1851, to March, 1854.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1842–1842 | barrister | — | [1883, 1886] |
| 1 | 1851–1854 | acting attorney-general | Antigua | [1883, 1886] |
| 2 | 1854–1854 | chief justice | Nevis | [1883, 1886] |
| 3 | 1856–1856 | chief justice | Dominica | [1883, 1886] |
| 4 | 1861–1861 | assistant judge of the supreme court | Jamaica | [1883, 1886] |

## Candidate stint `Ker, Alan___Jamaica___1877`

- Staff-list name: **Ker, Alan** | colony: **Jamaica** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Alan Ker | Puisne Judge of the Supreme Court | Judicial Establishment | — | — |
| 1879 | Alan Ker | Puisne Judge of the Supreme Court | Judicial Establishment | — | — |
| 1880 | Alan Ker | Puisne Judge of the Supreme Court | Judicial Establishment | — | — |
| 1883 | Alan Ker | Puisne Judge of the Supreme Court of Judicature | Judicial Establishment | — | — |

### Deterministic checks: `ker_alan_e1842` vs `Ker, Alan___Jamaica___1877`

- [PASS] surname_gate: bio 'KER' vs stint 'Ker, Alan' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

