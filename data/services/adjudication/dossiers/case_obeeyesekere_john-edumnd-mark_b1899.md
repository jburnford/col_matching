<!-- {"case_id": "case_obeeyesekere_john-edumnd-mark_b1899", "bio_ids": ["obeeyesekere_john-edumnd-mark_b1899"], "stint_ids": ["Obeysekere, J. E. M___Ceylon___1934"]} -->
# Dossier case_obeeyesekere_john-edumnd-mark_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `obeeyesekere_john-edumnd-mark_b1899`

- Printed name: **OBEEYESEKERE, JOHN EDUMND MARK**
- Birth year: 1899 (attested in editions [1930])
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L67212.v` — printed in editions [1930]:**

> OBEEYESEKERE, JOHN EDUMND MARK.—B. 1899; barrister-at-law, Gray's Inn, 1922; advoo. of sup. ct., Ceylon; ag. crown coun., Ceylon, Sept., 1924; crown coun., Jan., 1927; law lecturer; Council of Legal Educn., Colombo (in addn. to own duties), Jan., 1928 to Mar., 1929; edr., Vols. I-V, "Times of Ceylon Law Repts."

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | barrister-at-law, Gray's Inn | — | [1930] |
| 1 | 1924 | ag. crown coun. | Ceylon | [1930] |
| 2 | 1927 | crown coun | Ceylon *(inherited from previous clause)* | [1930] |
| 3 | 1928–1929 | Council of Legal Educn., Colombo (in addn. to own duties) | Ceylon *(inherited from previous clause)* | [1930] |

## Candidate stint `Obeysekere, J. E. M___Ceylon___1934`

- Staff-list name: **Obeysekere, J. E. M** | colony: **Ceylon** | listed 1934–1937 | editions [1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | J. E. M. Obeysekere | Crown Counsel | Law Officers’ Department | — | — |
| 1937 | J. E. M. Obeysekere | Public Trustee | Public Trustee's Department | — | — |

### Deterministic checks: `obeeyesekere_john-edumnd-mark_b1899` vs `Obeysekere, J. E. M___Ceylon___1934`

- [PASS] surname_gate: bio 'OBEEYESEKERE' vs stint 'Obeysekere, J. E. M' (fuzzy:2)
- [PASS] initials: bio ['J', 'E', 'M'] ~ stint ['J', 'E', 'M']
- [PASS] age_gate: stint starts 1934, birth 1899 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1937
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

