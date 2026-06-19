<!-- {"case_id": "case_beeton_william-hugh_b1903", "bio_ids": ["beeton_william-hugh_b1903"], "stint_ids": ["Beeton, W. H___Gold Coast___1934"]} -->
# Dossier case_beeton_william-hugh_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beeton_william-hugh_b1903`

- Printed name: **BEETON, William Hugh**
- Birth year: 1903 (attested in editions [1950, 1951, 1953, 1954])
- Honours: C.M.G (1954)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1950-L33566.v` — printed in editions [1950, 1951, 1953, 1954]:**

> BEETON, W. H., C.M.G. (1954).—b. 1903; ed. Strathallan Sch., Forgandenny, Perthshire and Lond. Univ.; asst. dist. comsnr., G.C., 1926; dist. comsnr., 1932; admin. offr., cl. II, 1939; senr. asst. col. sec., 1944; admin. offr., cl. I (asst. ch. comsnr., Ashanti), 1946; ch. comsnr., 1950; title changed to ch. regional offr., 1952.

**Version `col1948-L31087.v` — printed in editions [1948, 1949]:**

> BEETON, William Hugh, B.Sc. (Econ.).—b. 1903; ed. Strathallan Sch., Fergandenny, Perth and London Univ.; asst. dist. comsnr., G.C., 1926; dist. comsnr., 1932; admin. offr., cl. II, 1943; cl. I, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. dist. comsnr. | Gold Coast | [1948, 1949, 1950, 1951, 1953, 1954] |
| 1 | 1932 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954] |
| 2 | 1939 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 3 | 1943 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1944 | senr. asst. col. sec | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 5 | 1946 | admin. offr., cl. I (asst. ch. comsnr. | Ashanti) | [1948, 1949, 1950, 1951, 1953, 1954] |
| 6 | 1950 | ch. comsnr | Ashanti) *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 7 | 1952 | title changed to ch. regional offr | Ashanti) *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |

## Candidate stint `Beeton, W. H___Gold Coast___1934`

- Staff-list name: **Beeton, W. H** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | W. H. Beeton | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | W. H. Beeton | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `beeton_william-hugh_b1903` vs `Beeton, W. H___Gold Coast___1934`

- [PASS] surname_gate: bio 'BEETON' vs stint 'Beeton, W. H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1934, birth 1903 (age 31)
- [PASS] colony: 8 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
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

