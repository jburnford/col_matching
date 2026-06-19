<!-- {"case_id": "case_sackey_ebenezer-amos_b1899", "bio_ids": ["sackey_ebenezer-amos_b1899"], "stint_ids": ["Sackey, E. A___Gold Coast___1934", "Sackey, E. A___Gold Coast___1950"]} -->
# Dossier case_sackey_ebenezer-amos_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sackey_ebenezer-amos_b1899`

- Printed name: **SACKEY, Ebenezer Amos**
- Birth year: 1899 (attested in editions [1954, 1955])
- Honours: A.M.I.E.E, O.B.E (1954)
- Appears in editions: [1950, 1951, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1954-L22137.v` — printed in editions [1954, 1955]:**

> SACKEY, E. A., O.B.E. (1954)—b. 1899; ed. Mfantsipim Sch., Cape Coast, and Fara-day Hse., Lond.; elec. improver, G.C., 1928; African asst. elec. engr., 1931; elec. engr., 1947; senr., 1949; dep. ch., 1952.

**Version `col1950-L39271.v` — printed in editions [1950, 1951]:**

> SACKEY, Ebenezer Amos, A.M.I.E.E.—b. 1899; ed. Mfantsipim Sch., Cape Coast, and Faraday Hse.; elec. improver, G.C., 1928; African asst. elec. engnr., 1931; elec. engr., elec. dept., 1947; senr., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | elec. improver | Gold Coast | [1950, 1951, 1954, 1955] |
| 1 | 1931 | African asst. elec. engr | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1954, 1955] |
| 2 | 1947 | elec. engr | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1954, 1955] |
| 3 | 1949 | senr | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1954, 1955] |
| 4 | 1952 | dep. ch | Gold Coast *(inherited from previous clause)* | [1954, 1955] |

## Candidate stint `Sackey, E. A___Gold Coast___1934`

- Staff-list name: **Sackey, E. A** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | E. A. Sackey | African Assistant Electrical Engineer | Railway and Harbour Department | — | — |
| 1936 | E. A. Sackey | African Assistant Electrical Engineer | Railway and Harbour Department | — | — |

### Deterministic checks: `sackey_ebenezer-amos_b1899` vs `Sackey, E. A___Gold Coast___1934`

- [PASS] surname_gate: bio 'SACKEY' vs stint 'Sackey, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1934, birth 1899 (age 35)
- [PASS] colony: 5 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 75 vs bar 60: 'African asst. elec. engr' ~ 'African Assistant Electrical Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Sackey, E. A___Gold Coast___1950`

- Staff-list name: **Sackey, E. A** | colony: **Gold Coast** | listed 1950–1956 | editions [1950, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. A. Sackey | Electrical Engineers | Electrical Department | — | — |
| 1956 | E. A. Sackey | Chief Electrical Engineer | Civil Establishment | — | — |

### Deterministic checks: `sackey_ebenezer-amos_b1899` vs `Sackey, E. A___Gold Coast___1950`

- [PASS] surname_gate: bio 'SACKEY' vs stint 'Sackey, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1950, birth 1899 (age 51)
- [PASS] colony: 5 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1950-1956
- [PASS] position_sim: best 62 vs bar 60: 'elec. engr' ~ 'Electrical Engineers'
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

