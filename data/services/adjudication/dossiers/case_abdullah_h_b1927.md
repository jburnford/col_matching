<!-- {"case_id": "case_abdullah_h_b1927", "bio_ids": ["abdullah_h_b1927"], "stint_ids": ["Abdullah, Hanafiah bin___Brunei___1953"]} -->
# Dossier case_abdullah_h_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['abdullah_h_b1927'] carry a single initial only — the namesake trap applies.

## Biography `abdullah_h_b1927`

- Printed name: **ABDULLAH, H**
- Birth year: 1927 (attested in editions [1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L12783.v` — printed in editions [1966]:**

> ABDULLAH, H.—b. 1927; med. offr., H.K., 1954; senr. med. and health offr., 1963.

**Version `col1965-L13076.v` — printed in editions [1965]:**

> ABDULLAH, H.—b. 1927; med. offr., H.K., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1954 | med. offr. | Hong Kong | [1965, 1966] |
| 1 | 1963 | senr. med. and health offr | Hong Kong *(inherited from previous clause)* | [1966] |

## Candidate stint `Abdullah, Hanafiah bin___Brunei___1953`

- Staff-list name: **Abdullah, Hanafiah bin** | colony: **Brunei** | listed 1953–1955 | editions [1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | Hanafiah bin Abdullah | Officer-in-Charge of Audit | Civil Establishment | — | — |
| 1954 | Hanafiah bin Abdullah | Officer-in-Charge of Audit | Civil Establishment | — | — |
| 1955 | Hanafiah bin Abdullah | Officer-in-Charge of Audit | Civil Establishment | — | — |

### Deterministic checks: `abdullah_h_b1927` vs `Abdullah, Hanafiah bin___Brunei___1953`

- [PASS] surname_gate: bio 'ABDULLAH' vs stint 'Abdullah, Hanafiah bin' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1953, birth 1927 (age 26)
- [FAIL] colony: no placed event resolves to 'Brunei'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1955
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

