<!-- {"case_id": "case_callcott_john-hope_e1883", "bio_ids": ["callcott_john-hope_e1883", "callcott_john-hope_e1883-2"], "stint_ids": ["Callcott, J. H___Straits Settlements___1880"]} -->
# Dossier case_callcott_john-hope_e1883

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Callcott, J. H___Straits Settlements___1880'] have more than one claimant biography in this case.
- Phase 1 found `callcott_john-hope_e1883` ↔ `Callcott, J. H___Straits Settlements___1880` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `callcott_john-hope_e1883-2` ↔ `Callcott, J. H___Straits Settlements___1880` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `callcott_john-hope_e1883`

- Printed name: **CALLCOTT, JOHN HOPE**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1896, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L32498.v` — printed in editions [1898, 1899, 1900]:**

> CALLCOTT, JOHN HOPE.—Supl. of wks. and surveys, S. Sttlnts, 1883; has four times acted as dep. col. engr., and survr.-gen., Penang; is J.P., dep. engr., and survr.-gen., Penang, Oct., 1897.

**Version `col1888-L32450.v` — printed in editions [1888, 1889, 1890, 1896]:**

> CALCOTT, J. H.—Superintendent of works and surveys, Straits Settlements, 1883; has twice acted as Dep. Col. Engineer and Surveyor Gen., Penang. Is a J.P.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Supl. of wks. and surveys, S. Sttlnts | — | [1898, 1899, 1900] |
| 1 | 1883 | Superintendent of works and surveys | Straits Settlements | [1888, 1889, 1890, 1896] |
| 2 | 1897 | is J.P., dep. engr., and survr.-gen., Penang | — | [1898, 1899, 1900] |

## Biography `callcott_john-hope_e1883-2`

- Printed name: **CALLCOTT, John Hope**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L31149.v` — printed in editions [1897]:**

> CALLCOTT, John Hope—Sup. of works and surveys, S.S., 1883; has four times acted as Dep. Col. Engineer and Surveyor-Gen., Penang. Is a J.P.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | Sup. of works and surveys | Straits Settlements | [1897] |

## Candidate stint `Callcott, J. H___Straits Settlements___1880`

- Staff-list name: **Callcott, J. H** | colony: **Straits Settlements** | listed 1880–1897 | editions [1880, 1888, 1889, 1890, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | J. H. Callcott | Clerk of Works and Draftsman | Public Works and Survey Departments | — | — |
| 1888 | J. H. Callcott | Superintendent of Works and Surveys | Public Works and Survey Departments | — | — |
| 1889 | J. H. Callcott | Superintendent of Works and Surveys | Public Works and Survey Departments | — | — |
| 1890 | J. H. Callcott | Superintendent of Works and Surveys | Public Works and Survey Departments | — | — |
| 1896 | J. H. Callcott | Superintendent of Works and Surveys | Public Works and Survey Departments | — | — |
| 1897 | J. H. Callcott | Superintendent of Works and Surveys | Public Works and Survey Departments | — | — |

### Deterministic checks: `callcott_john-hope_e1883` vs `Callcott, J. H___Straits Settlements___1880`

- [PASS] surname_gate: bio 'CALLCOTT' vs stint 'Callcott, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1897
- [PASS] position_sim: best 100 vs bar 60: 'Superintendent of works and surveys' ~ 'Superintendent of Works and Surveys'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1888, 1889, 1890, 1896] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `callcott_john-hope_e1883-2` vs `Callcott, J. H___Straits Settlements___1880`

- [PASS] surname_gate: bio 'CALLCOTT' vs stint 'Callcott, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1897
- [PASS] position_sim: best 91 vs bar 60: 'Sup. of works and surveys' ~ 'Superintendent of Works and Surveys'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1897] pos~91 (bar: >=2)
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

