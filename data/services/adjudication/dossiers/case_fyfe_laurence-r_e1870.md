<!-- {"case_id": "case_fyfe_laurence-r_e1870", "bio_ids": ["fyfe_laurence-r_e1870"], "stint_ids": ["Fyfe, L. R___Jamaica___1880"]} -->
# Dossier case_fyfe_laurence-r_e1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fyfe_laurence-r_e1870`

- Printed name: **FYFE, LAURENCE R.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L27575.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> FYFE, LAURENCE R.—Educated at Aber. Univ.; temporary clerk, colonial secretary's office, Jamaica, 1870; subsequently appointed a 2nd class clerk in the audit office, and in June, 1871, transferred to the colonial secretary's office; private secretary to Sir W. Grey, 1875, and to Sir A. Musgrave in 1883; 1st class clerk, colonial secretary's office, April, 1875; is one of the compilers of the "Handbook of Jamaica;" secretary to the royal commission to inquire into the condition of elementary education, 1885; ag. protector of immigrants, Jan., 1884; special commissioner to report on Grand Cayman, Aug., 1887; accompanied Sir H. Norman as secy. on special visit to Cayman Islands, May, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870–1870 | temporary clerk, colonial secretary's office | Jamaica | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1871–1871 | 2nd class clerk | — | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1875–1883 | private secretary | — | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1875–1875 | 1st class clerk, colonial secretary's office | — | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1884–1884 | ag. protector of immigrants | — | [1883, 1886, 1888, 1889, 1890] |
| 5 | 1885–1885 | secretary to the royal commission to inquire into the condition of elementary education | — | [1883, 1886, 1888, 1889, 1890] |
| 6 | 1887–1887 | special commissioner | Grand Cayman | [1883, 1886, 1888, 1889, 1890] |
| 7 | 1888–1888 | secy. | Cayman Islands | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Fyfe, L. R___Jamaica___1880`

- Staff-list name: **Fyfe, L. R** | colony: **Jamaica** | listed 1880–1889 | editions [1880, 1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | L. R. Fyfe | Clerks, 1st Class | Colonial Secretary's Office | — | — |
| 1883 | L. R. Fyfe | Clerks, 1st Class | Colonial Secretary's Office | — | — |
| 1886 | L. R. Fyfe | Clerk, 1st Class | Colonial Secretary's Department | — | — |
| 1888 | L. R. Fyfe | Clerks, 1st Class | Colonial Secretary's Office | — | — |
| 1889 | L. R. Fyfe | Clerk, 1st Class | Colonial Secretary's Office | — | — |

### Deterministic checks: `fyfe_laurence-r_e1870` vs `Fyfe, L. R___Jamaica___1880`

- [PASS] surname_gate: bio 'FYFE' vs stint 'Fyfe, L. R' (exact)
- [PASS] initials: bio ['L', 'R'] ~ stint ['L', 'R']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1889
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

