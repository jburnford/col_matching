<!-- {"case_id": "case_stone_b-g_b1903", "bio_ids": ["stone_b-g_b1903"], "stint_ids": ["Stone, B___Kenya___1920"]} -->
# Dossier case_stone_b-g_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stone_b-g_b1903`

- Printed name: **STONE, B. G**
- Birth year: 1903 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1955)
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1960-L28404.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965]:**

> STONE, B. G., O.B.E. (1955).—b. 1903; ed. Bromsgrove Sch., and Sidney Sussex Coll., Camb.; cadet, Nig., 1925; asst. dist. offr., 1928; dist. offr., 1935; invalided 1936; temp. principal, C.O., 1947; principal (open comp.), 1949; head, students branch, 1956; secon. D.T.C., 1961; trans. O.D.M., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | cadet | Nigeria | [1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1928 | asst. dist. offr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1935 | dist. offr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1936 | invalided | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1947 | temp. principal | Colonial Office | [1960, 1961, 1962, 1963, 1964, 1965] |
| 5 | 1949 | principal (open comp.) | Colonial Office *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 6 | 1956 | head, students branch | Colonial Office *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 7 | 1961 | secon. D.T.C | Colonial Office *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 8 | 1964 | trans. O.D.M | Colonial Office *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Stone, B___Kenya___1920`

- Staff-list name: **Stone, B** | colony: **Kenya** | listed 1920–1934 | editions [1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | B. Stone | Deputy Registrars of the High Court | Judicial | — | — |
| 1922 | B. Stone | Deputy Registrars of the Supreme Court | Judicial | — | — |
| 1923 | B. Stone | Deputy Registrars of the Supreme Court | Judicial | — | — |
| 1924 | B. Stone | Deputy Registrars of the Supreme Court | Judicial | — | — |
| 1925 | B. Stone | Assistant Registrar-General | Registrar-General's Department | — | — |
| 1927 | B. Stone | Assistant to Registrar-General | Registrar-General's Department | — | — |
| 1928 | B. Stone | Assistant to Registrar-General | Registrar-General's Department | — | — |
| 1929 | B. Stone | Assistant to Registrar-General | Registrar-General's Department | — | — |
| 1930 | B. Stone | Assistant to Registrar-General | Registrar-General's Departments | — | — |
| 1931 | B. Stone | Assistant to Registrar General, Public Trustee and Official Receiver | Registrar General's Department | — | — |
| 1932 | B. Stone | Assistant to Registrar General, Public Trustee and Official Receiver | Registrar General's Department | — | — |
| 1934 | B. Stone | Assistant to Registrar General, Public Trustees and Official Receiver | Registrar General's Department | — | — |

### Deterministic checks: `stone_b-g_b1903` vs `Stone, B___Kenya___1920`

- [PASS] surname_gate: bio 'STONE' vs stint 'Stone, B' (exact)
- [PASS] initials: bio ['B', 'G'] ~ stint ['B']
- [PASS] age_gate: stint starts 1920, birth 1903 (age 17)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1934
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

