<!-- {"case_id": "case_thorne_richard-everard_b1901", "bio_ids": ["thorne_richard-everard_b1901"], "stint_ids": ["Thorne, R. E___Tanganyika___1933"]} -->
# Dossier case_thorne_richard-everard_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `thorne_richard-everard_b1901`

- Printed name: **THORNE, Richard Everard**
- Birth year: 1901 (attested in editions [1955])
- Appears in editions: [1951, 1955]

### Verbatim printed entry text (OCR)

**Version `col1955-L23030.v` — printed in editions [1955]:**

> THORNE, R. E.—b. 1901; ed. Haileybury; mil. serv., 1941-49, lt.-col.; asst. insp., police, Tang., 1925; asst. supt., 1928; supt., 1946; senr. supt., 1949; Zanz., 1952.

**Version `col1951-L43177.v` — printed in editions [1951]:**

> THORNE, Richard Everard.—b. 1901; ed. Haileybury Coll.; asst. supt., police, T.T., 1930; supt., 1946; senr., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | asst. insp., police | Tanganyika | [1955] |
| 1 | 1928 | asst. supt | Tanganyika *(inherited from previous clause)* | [1955] |
| 2 | 1930 | asst. supt., police, T.T | — | [1951] |
| 3 | 1946 | supt | Tanganyika *(inherited from previous clause)* | [1951, 1955] |
| 4 | 1949 | senr. supt | Tanganyika *(inherited from previous clause)* | [1951, 1955] |
| 5 | 1952 | senr. supt | Zanzibar | [1955] |

## Candidate stint `Thorne, R. E___Tanganyika___1933`

- Staff-list name: **Thorne, R. E** | colony: **Tanganyika** | listed 1933–1949 | editions [1933, 1934, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. E. Thorne | Assistant Superintendent | Police | — | — |
| 1934 | R. E. Thorne | Assistant Superintendents | Police | — | — |
| 1940 | R. E. Thorne | Assistant Superintendents | Police Department | — | — |
| 1949 | R. E. Thorne | Superintendent | Police | — | — |

### Deterministic checks: `thorne_richard-everard_b1901` vs `Thorne, R. E___Tanganyika___1933`

- [PASS] surname_gate: bio 'THORNE' vs stint 'Thorne, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1933, birth 1901 (age 32)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1949
- [FAIL] position_sim: best 44 vs bar 60: 'supt' ~ 'Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

