<!-- {"case_id": "case_easmon_john-farrell_e1880", "bio_ids": ["easmon_john-farrell_e1880"], "stint_ids": ["Easmon, J. F___Gold Coast___1889"]} -->
# Dossier case_easmon_john-farrell_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Easmon, J. F___Gold Coast___1889` is also gate-compatible with biography(ies) outside this case: ['easmen_j-f_e1880'] (already linked elsewhere or filtered).

## Biography `easmon_john-farrell_e1880`

- Printed name: **EASMON, JOHN FARRELL**
- Birth year: not printed
- Terminal: resigned 1897 — “resig., 1897.”
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L33221.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897]:**

> EASMON, JOHN FARRELL.—Assistant colonial surgeon, Gold Coast Colony, 7th Sept., 1880; health officer, Accra, 1884; acted as chief medical officer in 1884-5-6; chairman, central committee, Gold Coast section, Colonial and Indian Exhibition, 1886; has acted several times as chief medical officer.

**Version `col1898-L33197.v` — printed in editions [1898]:**

> EASMON, JOHN FARRELL.—Asst. col. surg., G. Coast Colony, Sept., 1880; health offr., Accra, 1881; chmn., central comttee, G. Coast section Col. and Ind. Exhib., 1886; acted several times as ch. med. offr.; ch. med. offr., 1893; resig., 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Assistant colonial surgeon | Gold Coast Colony | [1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1880 | Asst. col. surg., G. Coast Colony | — | [1898] |
| 2 | 1881 | health offr., Accra | — | [1898] |
| 3 | 1884 | health officer | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 4 | 1884–1886 | acted as chief medical officer | — | [1888, 1889, 1890, 1894, 1896, 1897] |
| 5 | 1886–1886 | chairman, central committee, Gold Coast section, Colonial and Indian Exhibition | Gold Coast Colony | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 6 | 1893 | ch. med. offr | — | [1898] |

## Candidate stint `Easmon, J. F___Gold Coast___1889`

- Staff-list name: **Easmon, J. F** | colony: **Gold Coast** | listed 1889–1897 | editions [1889, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | J. F. Easmon | Assistant Colonial Surgeon | Medical Department | — | — |
| 1890 | J. F. Easmon | Assistant Colonial Surgeon | Medical Department | — | — |
| 1894 | J. F. Easmon | Chief Medical Officer | Medical Department | — | — |
| 1896 | J. F. Easmon | Chief Medical Officer | Medical Department | — | — |
| 1897 | J. F. Easmon | Chief Medical Officer | Medical Department | — | — |

### Deterministic checks: `easmon_john-farrell_e1880` vs `Easmon, J. F___Gold Coast___1889`

- [PASS] surname_gate: bio 'EASMON' vs stint 'Easmon, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1897
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

