<!-- {"case_id": "case_bayfield_charles-mahon_b1908", "bio_ids": ["bayfield_charles-mahon_b1908"], "stint_ids": ["Bayfield, C. M___Gold Coast___1950"]} -->
# Dossier case_bayfield_charles-mahon_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bayfield_charles-mahon_b1908`

- Printed name: **BAYFIELD, Charles Mahon**
- Birth year: 1908 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956])
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1948-L31042.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]:**

> BAYFIELD, Charles Mahon.—b. 1908; ed. King Edward VII Sch., Kings Lynn, and Emmanuel Coll., Camb., B.A. (hons.) (Cantab.); prob. surv., Nig., 1931; asst. surv., N. Rhod., 1931; clr., customs, G.C., 1933; senr. collr., 1943; ch. inspr., cust. and excise, Nig., 1945; asst. compt., G.C., 1949; dep. compt., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | prob. surv. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 1 | 1931 | asst. surv. | Northern Rhodesia | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 2 | 1933 | clr., customs | Gold Coast | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 3 | 1943 | senr. collr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 4 | 1945 | ch. inspr., cust. and excise | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 5 | 1949 | asst. compt. | Gold Coast | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |

## Candidate stint `Bayfield, C. M___Gold Coast___1950`

- Staff-list name: **Bayfield, C. M** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | C. M. Bayfield | Deputy Comptroller of Customs and Excise | Customs and Excise | — | — |
| 1951 | C. M. Bayfield | Deputy Comptroller of Customs and Excise | Customs and Excise Department | — | — |

### Deterministic checks: `bayfield_charles-mahon_b1908` vs `Bayfield, C. M___Gold Coast___1950`

- [PASS] surname_gate: bio 'BAYFIELD' vs stint 'Bayfield, C. M' (exact)
- [PASS] initials: bio ['C', 'M'] ~ stint ['C', 'M']
- [PASS] age_gate: stint starts 1950, birth 1908 (age 42)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 32 vs bar 60: 'asst. compt.' ~ 'Deputy Comptroller of Customs and Excise'
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

