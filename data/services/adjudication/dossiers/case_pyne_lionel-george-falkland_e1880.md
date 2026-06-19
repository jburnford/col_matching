<!-- {"case_id": "case_pyne_lionel-george-falkland_e1880", "bio_ids": ["pyne_lionel-george-falkland_e1880"], "stint_ids": ["Pyne, L. G. F___Trinidad___1886"]} -->
# Dossier case_pyne_lionel-george-falkland_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Pyne, L. G. F___Trinidad___1886` is also gate-compatible with biography(ies) outside this case: ['pyne_lionel-g-f_e1880'] (already linked elsewhere or filtered).

## Biography `pyne_lionel-george-falkland_e1880`

- Printed name: **PYNE, Lionel George Falkland**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L35617.v` — printed in editions [1888, 1890]:**

> PYNE, Lionel George Falkland.—4th clerk, colonial secretary's office, Trinidad, Oct., 1880; 4th clerk, treasury, Jan., 1883; 3rd clerk, April, 1884; private secretary to administrator, Oct., 1885; chief clerk med. dept., July, 1888; entered Middle Temple, 1889.

**Version `col1889-L35225.v` — printed in editions [1889]:**

> PYNE, LIONEL GEORGE FALKLAND.—4th clerk, colonial secretary's office, Trinidad, Oct., 1880; 4th clerk, treasury, Jan., 1883; 3rd clerk, April, 1884; private secretary to administrator, Oct., 1885; chief clerk med. dept., July, 1888.

**Version `col1886-L35367.v` — printed in editions [1886]:**

> PYNE, LIONEL G. F.—Appointed 4th clerk, Colonial Secretary's Department, Trinidad, 4th October, 1880; 4th clerk, receiver-general's department, 1 Jan., 1883; 3rd clerk, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | 4th clerk, colonial secretary's office | Trinidad | [1886, 1888, 1889, 1890] |
| 1 | 1883 | 4th clerk, treasury | Trinidad *(inherited from previous clause)* | [1886, 1888, 1889, 1890] |
| 2 | 1884 | 3rd clerk | Trinidad *(inherited from previous clause)* | [1886, 1888, 1889, 1890] |
| 3 | 1885 | private secretary to administrator | Trinidad *(inherited from previous clause)* | [1888, 1889, 1890] |
| 4 | 1888 | chief clerk med. dept | Trinidad *(inherited from previous clause)* | [1888, 1889, 1890] |
| 5 | 1889 | entered Middle Temple | Trinidad *(inherited from previous clause)* | [1888, 1890] |

## Candidate stint `Pyne, L. G. F___Trinidad___1886`

- Staff-list name: **Pyne, L. G. F** | colony: **Trinidad** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | L. G. F. Pyne | 3rd Clerk (Accountant) | Receiver-General's Department | — | — |
| 1888 | L. G. F. Pyne | 3rd Clerk (Accountant) | Treasury, Excise, and Savings Bank Department | — | — |
| 1889 | L. G. F. Pyne | Chief Clerk | Medical Establishment | — | — |
| 1890 | L. G. F. Pyne | Chief Clerk | Medical Establishment | — | — |

### Deterministic checks: `pyne_lionel-george-falkland_e1880` vs `Pyne, L. G. F___Trinidad___1886`

- [PASS] surname_gate: bio 'PYNE' vs stint 'Pyne, L. G. F' (exact)
- [PASS] initials: bio ['L', 'G', 'F'] ~ stint ['L', 'G', 'F']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1886-1890
- [PASS] position_sim: best 100 vs bar 60: '3rd clerk' ~ '3rd Clerk (Accountant)'
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

