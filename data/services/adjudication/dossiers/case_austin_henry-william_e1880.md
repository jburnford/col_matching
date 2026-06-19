<!-- {"case_id": "case_austin_henry-william_e1880", "bio_ids": ["austin_henry-william_e1880", "austin_henry-william_e1880-2"], "stint_ids": ["Austin, Henry W___Bahamas___1886"]} -->
# Dossier case_austin_henry-william_e1880

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 51 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Austin, Henry W___Bahamas___1886'] have more than one claimant biography in this case.
- Phase 1 found `austin_henry-william_e1880` ↔ `Austin, Henry W___Bahamas___1886` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `austin_henry-william_e1880-2` ↔ `Austin, Henry W___Bahamas___1886` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `austin_henry-william_e1880`

- Printed name: **AUSTIN, HENRY WILLIAM**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L26270.v` — printed in editions [1883, 1886, 1888, 1890]:**

> AUSTIN, HENRY WILLIAM, chief justice, Bahamas, August, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | chief justice | Bahamas | [1883, 1886, 1888, 1890] |

## Biography `austin_henry-william_e1880-2`

- Printed name: **AUSTIN, Henry William**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L31595.v` — printed in editions [1889]:**

> AUSTIN, Henry William—Chief justice, Bahamas, August, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Chief justice | Bahamas | [1889] |

## Candidate stint `Austin, Henry W___Bahamas___1886`

- Staff-list name: **Austin, Henry W** | colony: **Bahamas** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | Henry W. Austin | Chief Justice, Chancellor, and Judge of Admiralty | Judicial Establishment | — | — |
| 1888 | Henry W. Austin | Chief Justice, Chancellor, and Judge of Admiralty | Judicial Establishment | — | — |
| 1889 | Henry W. Austin | Chief Justice, Chancellor, and Judge of Admiralty | Judicial Establishment | — | — |
| 1890 | Henry W. Austin | Chief Justice, Chancellor, and Judge of Admiralty | Judicial Establishment | — | — |

### Deterministic checks: `austin_henry-william_e1880` vs `Austin, Henry W___Bahamas___1886`

- [PASS] surname_gate: bio 'AUSTIN' vs stint 'Austin, Henry W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1890
- [PASS] position_sim: best 100 vs bar 60: 'chief justice' ~ 'Chief Justice, Chancellor, and Judge of Admiralty'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1886, 1888, 1890] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `austin_henry-william_e1880-2` vs `Austin, Henry W___Bahamas___1886`

- [PASS] surname_gate: bio 'AUSTIN' vs stint 'Austin, Henry W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1890
- [PASS] position_sim: best 100 vs bar 60: 'Chief justice' ~ 'Chief Justice, Chancellor, and Judge of Admiralty'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1889] pos~100 (bar: >=2)
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

