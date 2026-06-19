<!-- {"case_id": "case_obeyesekere_stanley_b1882", "bio_ids": ["obeyesekere_stanley_b1882"], "stint_ids": ["Obeyesekere, S. C___Ceylon___1927"]} -->
# Dossier case_obeyesekere_stanley_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['obeyesekere_stanley_b1882'] carry a single initial only — the namesake trap applies.

## Biography `obeyesekere_stanley_b1882`

- Printed name: **OBEYESEKERE, STANLEY**
- Birth year: 1882 (attested in editions [1931, 1932])
- Honours: K.C
- Appears in editions: [1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1931-L67104.v` — printed in editions [1931, 1932]:**

> OBEYESEKERE, STANLEY, K.C., B.A (Cantab.), Barrister-at-law, Inner Temple—B. 1882; crown coun., Ceylon, 1912; dep. solr.-gen., Mar., 1925; ag. atty.-gen., Mar., 1929; solr.-gen., May, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | crown coun. | Ceylon | [1931, 1932] |
| 1 | 1925 | dep. solr.-gen | Ceylon *(inherited from previous clause)* | [1931, 1932] |
| 2 | 1929 | ag. atty.-gen | Ceylon *(inherited from previous clause)* | [1931, 1932] |

## Candidate stint `Obeyesekere, S. C___Ceylon___1927`

- Staff-list name: **Obeyesekere, S. C** | colony: **Ceylon** | listed 1927–1929 | editions [1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | S. Obeyesekere | Deputy Solicitor-General | Judicial Establishment | — | — |
| 1928 | S. Obeyesekere | Deputy Solicitor-General | Judicial Establishment | — | — |
| 1929 | S. Obeyesekere | Deputy Solicitor-General | Judicial Establishment | — | — |

### Deterministic checks: `obeyesekere_stanley_b1882` vs `Obeyesekere, S. C___Ceylon___1927`

- [PASS] surname_gate: bio 'OBEYESEKERE' vs stint 'Obeyesekere, S. C' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S', 'C']
- [PASS] age_gate: stint starts 1927, birth 1882 (age 45)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1929
- [PASS] position_sim: best 65 vs bar 60: 'dep. solr.-gen' ~ 'Deputy Solicitor-General'
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

