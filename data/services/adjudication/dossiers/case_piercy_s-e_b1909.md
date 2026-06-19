<!-- {"case_id": "case_piercy_s-e_b1909", "bio_ids": ["piercy_s-e_b1909"], "stint_ids": ["Piercy, S. E___Kenya___1949"]} -->
# Dossier case_piercy_s-e_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `piercy_s-e_b1909`

- Printed name: **PIERCY, S. E**
- Birth year: 1909 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1953-L18715.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959]:**

> PIERCY, S. E.—b. 1909; ed. Sedbergh Sch., Durham Univ. and Royal Vet. Coll.; vet. res. offr., Ken., 1939; senr., 1947; chief, 1952; dep. dir., E.A.V.R.O., 1954-58; author pp. in scient. journals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | vet. res. offr. | Kenya | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1947 | senr | Kenya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 2 | 1952 | chief | Kenya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 3 | 1954–1958 | dep. dir., E.A.V.R.O | Kenya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |

## Candidate stint `Piercy, S. E___Kenya___1949`

- Staff-list name: **Piercy, S. E** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. E. Piercy | Veterinary Research Officers | Veterinary | — | — |
| 1950 | S. E. Piercy | Veterinary Research Officer | Veterinary | — | — |
| 1951 | S. E. Piercy | Veterinary Research Officers | VETERINARY | — | — |

### Deterministic checks: `piercy_s-e_b1909` vs `Piercy, S. E___Kenya___1949`

- [PASS] surname_gate: bio 'PIERCY' vs stint 'Piercy, S. E' (exact)
- [PASS] initials: bio ['S', 'E'] ~ stint ['S', 'E']
- [PASS] age_gate: stint starts 1949, birth 1909 (age 40)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 26 vs bar 60: 'senr' ~ 'Veterinary Research Officer'
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

