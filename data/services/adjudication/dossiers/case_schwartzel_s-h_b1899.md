<!-- {"case_id": "case_schwartzel_s-h_b1899", "bio_ids": ["schwartzel_s-h_b1899"], "stint_ids": ["Schwartzel, S. H___Uganda___1949"]} -->
# Dossier case_schwartzel_s-h_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schwartzel_s-h_b1899`

- Printed name: **SCHWARTZEL, S. H**
- Birth year: 1899 (attested in editions [1958, 1959, 1960])
- Honours: M.B.E (1957)
- Appears in editions: [1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1958-L26716.v` — printed in editions [1958, 1959, 1960]:**

> SCHWARTZEL, S. H., M.B.E. (1957).—b. 1899; ed. Kenya Govt. Schs.; architectural asst., Ken., 1924; Uga., 1936; architect, 1947-59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | architectural asst. | Kenya | [1958, 1959, 1960] |
| 1 | 1936 | architectural asst. | Uganda | [1958, 1959, 1960] |
| 2 | 1947–1959 | architect | Uganda *(inherited from previous clause)* | [1958, 1959, 1960] |

## Candidate stint `Schwartzel, S. H___Uganda___1949`

- Staff-list name: **Schwartzel, S. H** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. H. Schwartzel | Architects, Grade II | Public Works | — | — |
| 1951 | S. H. Schwartzel | Architects, Grade II | Public Works | — | — |

### Deterministic checks: `schwartzel_s-h_b1899` vs `Schwartzel, S. H___Uganda___1949`

- [PASS] surname_gate: bio 'SCHWARTZEL' vs stint 'Schwartzel, S. H' (exact)
- [PASS] initials: bio ['S', 'H'] ~ stint ['S', 'H']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 64 vs bar 60: 'architect' ~ 'Architects, Grade II'
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

