<!-- {"case_id": "case_hossack_frederick-john_b1903", "bio_ids": ["hossack_frederick-john_b1903"], "stint_ids": ["Hossack, F. J___Palestine___1927"]} -->
# Dossier case_hossack_frederick-john_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hossack_frederick-john_b1903`

- Printed name: **HOSSACK, Frederick John**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33458.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOSSACK, Frederick John, B.Sc. (eng.) (Lond.).—b. 1903; ed. Rutlish Sch. and Lond. Univ.; interned S'pore.; ch. draughtsman and survr., rlwys. Pal., 1926; dist. engrnr., rlwys., F.M.S., 1938; dist. engrnr., rlwys., Pal., 1946; construct. engrnr., E.A.R. & H., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | ch. draughtsman and survr., rlwys. Pal | — | [1948, 1949, 1950, 1951] |
| 1 | 1938 | dist. engrnr., rlwys. | Federated Malay States | [1948, 1949, 1950, 1951] |
| 2 | 1946 | dist. engrnr., rlwys. | Palestine | [1948, 1949, 1950, 1951] |
| 3 | 1948 | construct. engrnr., E.A.R. & H | Palestine *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hossack, F. J___Palestine___1927`

- Staff-list name: **Hossack, F. J** | colony: **Palestine** | listed 1927–1932 | editions [1927, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. J. Hossack | Chief Draughtsman and Surveyor | Palestine Railways | — | — |
| 1929 | F. J. Hossack | Chief Draughtsman and Surveyor | Palestine Railways | — | — |
| 1930 | F. J. Hossack | Chief Draughtsman and Surveyor | Palestine Railways | — | — |
| 1931 | F. J. Hossack | Chief Draughtsman and Surveyor | Palestine Railways | — | — |
| 1932 | F. J. Hossack | Chief Draughtsman and Surveyor | Palestine Railways | — | — |

### Deterministic checks: `hossack_frederick-john_b1903` vs `Hossack, F. J___Palestine___1927`

- [PASS] surname_gate: bio 'HOSSACK' vs stint 'Hossack, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1927, birth 1903 (age 24)
- [PASS] colony: 2 placed event(s) resolve to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1932
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

