<!-- {"case_id": "case_hawkins_a-cesar_e1836", "bio_ids": ["hawkins_a-cesar_e1836"], "stint_ids": ["Hawkins, A. C___Natal___1879"]} -->
# Dossier case_hawkins_a-cesar_e1836

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hawkins_a-cesar_e1836`

- Printed name: **HAWKINS, A. CESAR**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1886-L33961.v` — printed in editions [1886]:**

> HAWKINS, A. CESAR.—Ensign in the 1st royals, Feb., 1836, and retired after 12 years' service; resident magistrate of the Weenen, Natal, Sept., 1852, and removed to resident magistracy of the Upper Umcomanzi division of that colony, Feb., 1853; was a major in the Natal carabiniers.

**Version `col1888-L33928.v` — printed in editions [1888, 1889]:**

> HAWKINS, A. CESAR.—Ensign in the 1st royals, Feb., 1836, retired, 1848; R.M., Weenen, Natal, Sept., 1852; ditto Upper Umcomanzi, Feb., 1855; was a major in the Natal carabiniers.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1836–1848 | Ensign in the 1st royals | — | [1886, 1888, 1889] |
| 1 | 1852 | resident magistrate | Natal | [1886, 1888, 1889] |
| 2 | 1853 | resident magistracy of the Upper Umcomanzi division | Natal | [1886] |
| 3 | 1855 | R.M. | Natal | [1888, 1889] |

## Candidate stint `Hawkins, A. C___Natal___1879`

- Staff-list name: **Hawkins, A. C** | colony: **Natal** | listed 1879–1886 | editions [1879, 1880, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | A. C. Hawkins | Resident Magistrate | Magisterial Department and Staff | — | — |
| 1880 | A. C. Hawkins | Clerk and Interpreter | Magisterial Department and Staff | — | — |
| 1886 | A. C. Hawkins | — | Resident Magistrates | — | — |

### Deterministic checks: `hawkins_a-cesar_e1836` vs `Hawkins, A. C___Natal___1879`

- [PASS] surname_gate: bio 'HAWKINS' vs stint 'Hawkins, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1886
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

