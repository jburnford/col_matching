<!-- {"case_id": "case_chappel_majorie-carnsew_b1894", "bio_ids": ["chappel_majorie-carnsew_b1894"], "stint_ids": ["Chappel, M. C___Gold Coast___1929"]} -->
# Dossier case_chappel_majorie-carnsew_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chappel_majorie-carnsew_b1894`

- Printed name: **CHAPPEL, Majorie Carnsew**
- Birth year: 1894 (attested in editions [1948, 1949, 1950, 1951])
- Honours: L.R.C.P, M.R.C.S
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31723.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CHAPPEL, Majorie Carnsew, M.R.C.S., L.R.C.P.—b. 1894; ed. Alice Ottley Sch., Worcester and Lond. (Royal Free Hospital) Sch. of Med. for Women, cert. of L.S.T. Med.; hse. surg. and obstetric asst., Elizabeth Garrett Anderson Hosp., Lond.; med. offr., G.C., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | med. offr. | Gold Coast | [1948, 1949, 1950, 1951] |

## Candidate stint `Chappel, M. C___Gold Coast___1929`

- Staff-list name: **Chappel, M. C** | colony: **Gold Coast** | listed 1929–1936 | editions [1929, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | M. C. Chappel | Women Medical Officer | Sanitation Branch | — | — |
| 1932 | M. C. Chappel | Women Medical Officer | Sanitation Branch | — | — |
| 1936 | M. C. Chappel | Women Medical Officers | Health Branch | — | — |

### Deterministic checks: `chappel_majorie-carnsew_b1894` vs `Chappel, M. C___Gold Coast___1929`

- [PASS] surname_gate: bio 'CHAPPEL' vs stint 'Chappel, M. C' (exact)
- [PASS] initials: bio ['M', 'C'] ~ stint ['M', 'C']
- [PASS] age_gate: stint starts 1929, birth 1894 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1936
- [FAIL] position_sim: best 55 vs bar 60: 'med. offr.' ~ 'Women Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

