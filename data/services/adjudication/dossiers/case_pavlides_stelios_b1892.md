<!-- {"case_id": "case_pavlides_stelios_b1892", "bio_ids": ["pavlides_stelios_b1892"], "stint_ids": ["Pavlides, Stelios___Cyprus___1936"]} -->
# Dossier case_pavlides_stelios_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pavlides_stelios_b1892'] carry a single initial only — the namesake trap applies.
- Phase 1 found `pavlides_stelios_b1892` ↔ `Pavlides, Stelios___Cyprus___1936` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Pavlides, Stelios___Cyprus___1936` is also gate-compatible with biography(ies) outside this case: ['pavlides_spyros_b1901'] (already linked elsewhere or filtered).

## Biography `pavlides_stelios_b1892`

- Printed name: **PAVLIDES, Stelios**
- Birth year: 1892 (attested in editions [1929, 1930, 1931, 1933, 1934, 1936, 1937, 1939, 1940])
- Honours: C.M.G (1951)
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1929-L62977.v` — printed in editions [1929, 1930, 1931, 1933, 1934, 1936, 1937, 1939, 1940]:**

> PAVLIDES, Stelios.—B. 1892; barrister-at-law, Gray's Inn, 1916; crown coun., Cyprus, Dec., 1927; ag. solr.-gen., for various periods, 1928-31.

**Version `col1932-L63073.v` — printed in editions [1932]:**

> PAVLIDES, STELIOS.—B. 1892; barrister-at-law, Gray's Inn, 1916; crown coun., Cyprus, Dec., 1927; ag. solr.-gen., for various periods, 1928-31.

**Version `col1948-L35156.v` — printed in editions [1948, 1950, 1951]:**

> PAVLIDES, Stelios, C.M.G. (1951), K.C.—b. 1892; barrister-at-law, Gray's Inn; on mil. serv. 1940-41, 2nd lieut.; cr. coun., Cyp., 1927; solr.-gen., 1940; atty.-gen., 1944.

**Version `col1949-L34835.v` — printed in editions [1949]:**

> PAVILIDES, Stelios, K.C.—b. 1892; barrister-at-law, Gray's Inn; on mil. serv. 1940-41, 2nd lieut.; crown coun., Cyp., 1927; solr.-gen., 1940; atty.-gen., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | barrister-at-law, Gray's Inn | — | [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |
| 1 | 1927 | crown coun. | Cyprus | [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951] |
| 2 | 1928–1931 | ag. solr.-gen., for various periods | Cyprus *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1939, 1940] |
| 3 | 1940 | solr.-gen | Cyprus *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1944 | atty.-gen | Cyprus *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Pavlides, Stelios___Cyprus___1936`

- Staff-list name: **Pavlides, Stelios** | colony: **Cyprus** | listed 1936–1952 | editions [1936, 1939, 1946, 1949, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | S. Pavlides | Crown Counsel | Judicial Department | — | — |
| 1939 | S. Pavlides | Crown Counsel | Legal Department | — | — |
| 1946 | S. Pavlides | Attorney-General | Executive Council | — | — |
| 1949 | Stelios Pavlides | Attorney-General | Legal | — | — |
| 1951 | S. G. Pavlides | Medical Officer Specialist (Radiologist) | Research | — | — |
| 1951 | Stelios Pavlides | Attorney-General | Legal | C.M.G. | — |
| 1952 | S. Pavlides | Attorney-General | Civil Establishment | C.M.G. | — |

### Deterministic checks: `pavlides_stelios_b1892` vs `Pavlides, Stelios___Cyprus___1936`

- [PASS] surname_gate: bio 'PAVLIDES' vs stint 'Pavlides, Stelios' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1936, birth 1892 (age 44)
- [PASS] colony: 4 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1952
- [PASS] position_sim: best 64 vs bar 60: 'atty.-gen' ~ 'Attorney-General'
- [PASS] honour: shared: C.M.G
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1949, 1951] pos~64 (bar: >=2)
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

