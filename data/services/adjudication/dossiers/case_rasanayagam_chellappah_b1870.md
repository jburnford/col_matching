<!-- {"case_id": "case_rasanayagam_chellappah_b1870", "bio_ids": ["rasanayagam_chellappah_b1870"], "stint_ids": ["Rasananayagam, C___Ceylon___1921"]} -->
# Dossier case_rasanayagam_chellappah_b1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rasanayagam_chellappah_b1870'] carry a single initial only — the namesake trap applies.

## Biography `rasanayagam_chellappah_b1870`

- Printed name: **RASANAYAGAM, CHELLAPPAH**
- Birth year: 1870 (attested in editions [1924, 1925, 1927, 1928, 1929])
- Appears in editions: [1924, 1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1924-L57408.v` — printed in editions [1924, 1925, 1927, 1928, 1929]:**

> RASANAYAGAM, CHELLAPPAH.—B. 1870; apptd. to cls. V., Ceylon civ. serv., Sept., 1923; extra officio ass't, Jaffna kach., Sept., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | apptd. to cls. V., Ceylon civ. serv | Ceylon | [1924, 1925, 1927, 1928, 1929] |

## Candidate stint `Rasananayagam, C___Ceylon___1921`

- Staff-list name: **Rasananayagam, C** | colony: **Ceylon** | listed 1921–1922 | editions [1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | C. Rasananayagam | Deputy Registrar of Supreme Court | Judicial Establishment | — | — |
| 1922 | C. Rasananayagam | Third Deputy Registrar of Supreme Court | Judicial Establishment | — | — |

### Deterministic checks: `rasanayagam_chellappah_b1870` vs `Rasananayagam, C___Ceylon___1921`

- [PASS] surname_gate: bio 'RASANAYAGAM' vs stint 'Rasananayagam, C' (fuzzy:2)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1921, birth 1870 (age 51)
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1922
- [FAIL] position_sim: best 38 vs bar 60: 'apptd. to cls. V., Ceylon civ. serv' ~ 'Third Deputy Registrar of Supreme Court'
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

