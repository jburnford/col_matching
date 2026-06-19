<!-- {"case_id": "case_millson_alvan_e1882", "bio_ids": ["millson_alvan_e1882", "millson_alyan_e1882"], "stint_ids": ["Billson, A. A___Australia___1912"]} -->
# Dossier case_millson_alvan_e1882

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['millson_alvan_e1882', 'millson_alyan_e1882'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Billson, A. A___Australia___1912'] have more than one claimant biography in this case.

## Biography `millson_alvan_e1882`

- Printed name: **MILLSON, ALVAN**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34927.v` — printed in editions [1888, 1889, 1890]:**

> MILLSON, ALVAN.—Private secretary to Sir R. Harley and General Turton, 1882-3; district magistrate, British Honduras, 1883; district commissioner, Lagos, 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882–1883 | Private secretary to Sir R. Harley and General Turton | — | [1888, 1889, 1890] |
| 1 | 1883 | district magistrate | British Honduras | [1888, 1889, 1890] |
| 2 | 1887 | district commissioner | Lagos | [1888, 1889, 1890] |

## Biography `millson_alyan_e1882`

- Printed name: **MILLSON, ALYAN**
- Birth year: not printed
- Appears in editions: [1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1894-L33031.v` — printed in editions [1894, 1896]:**

> MILLSON, ALYAN, M.A.—Private secretary to Sir R. Harley and General Turton, 1882-3; district magistrate, British Honduras, 1883; district commissioner, Lagos, 1887; assistant colonial secretary, 1889; sp. commissur, to Yorubaland Jan. to May, 1890; acting dist. commissur, eastern dist., Jan., 1892; acting col. sec. Mar. to Oct., 1892, and June, 1893; dep. gov., 3rd to 24th Aug., 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882–1883 | Private secretary to Sir R. Harley and General Turton | — | [1894, 1896] |
| 1 | 1883 | district magistrate | British Honduras | [1894, 1896] |
| 2 | 1887 | district commissioner | Lagos | [1894, 1896] |
| 3 | 1889 | assistant colonial secretary | Lagos *(inherited from previous clause)* | [1894, 1896] |
| 4 | 1890 | sp. commissur, to Yorubaland | Lagos *(inherited from previous clause)* | [1894, 1896] |
| 5 | 1892 | acting dist. commissur, eastern dist | Lagos *(inherited from previous clause)* | [1894, 1896] |
| 6 | 1893 | acting col. sec | Lagos *(inherited from previous clause)* | [1894, 1896] |

## Candidate stint `Billson, A. A___Australia___1912`

- Staff-list name: **Billson, A. A** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. A. Billson | Minister of Education and Railways | Cabinet | — | — |
| 1913 | A. A. Billson | Minister of Public Instruction | Cabinet | — | — |
| 1913 | Hon. A. A. Billson | Minister of Public Instruction | Department of Education | — | — |

### Deterministic checks: `millson_alvan_e1882` vs `Billson, A. A___Australia___1912`

- [PASS] surname_gate: bio 'MILLSON' vs stint 'Billson, A. A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A', 'A']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `millson_alyan_e1882` vs `Billson, A. A___Australia___1912`

- [PASS] surname_gate: bio 'MILLSON' vs stint 'Billson, A. A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A', 'A']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

