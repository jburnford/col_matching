<!-- {"case_id": "case_heslip_isaac_b1876", "bio_ids": ["heslip_isaac_b1876"], "stint_ids": ["Heslip, I___Sierra Leone___1911"]} -->
# Dossier case_heslip_isaac_b1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['heslip_isaac_b1876'] carry a single initial only — the namesake trap applies.

## Biography `heslip_isaac_b1876`

- Printed name: **HESLIP, ISAAC**
- Birth year: 1876 (attested in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930])
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1929, 1930]

### Verbatim printed entry text (OCR)

**Version `col1923-L55184.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930]:**

> HESLIP, MAJOR ISAAC.—B. 1876; 3rd batt., R. Irish Rifles; passed course of instrn., R.I.C., Dublin; Hvthe certif.; asst. comsrr., pol., Sierra Leone, 8th Feb., 1911; comsrr., pol. and sherif., 8th July, 1914; dist. comsrr., 22nd Sept., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. comsrr., pol. | Sierra Leone | [1923, 1924, 1925, 1927, 1928, 1929, 1930] |
| 1 | 1914 | comsrr., pol. and sherif | Sierra Leone *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1929, 1930] |
| 2 | 1920 | dist. comsrr | Sierra Leone *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1929, 1930] |

## Candidate stint `Heslip, I___Sierra Leone___1911`

- Staff-list name: **Heslip, I** | colony: **Sierra Leone** | listed 1911–1920 | editions [1911, 1912, 1913, 1915, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | I. Heslip | Assistant Commissioner | Civil Police | — | Captain |
| 1912 | I. Heslip | Assistant Commissioner | Civil Police | — | Captain |
| 1913 | I. Heslip | Assistant Commissioner | Civil Police | — | Captain |
| 1915 | Capt. I. Heslip | Commissioner of Police | Civil Police | — | Captain |
| 1918 | I. Heslip | Commissioner of Police | Civil Police | — | Major |
| 1919 | Major I. Heslip | Commissioner of Police | Civil Police | — | Major |
| 1920 | I. Heslip | Commissioner of Police | Civil Police | — | Major |

### Deterministic checks: `heslip_isaac_b1876` vs `Heslip, I___Sierra Leone___1911`

- [PASS] surname_gate: bio 'HESLIP' vs stint 'Heslip, I' (exact)
- [PASS] initials: bio ['I'] ~ stint ['I']
- [PASS] age_gate: stint starts 1911, birth 1876 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1911-1920
- [FAIL] position_sim: best 54 vs bar 60: 'asst. comsrr., pol.' ~ 'Assistant Commissioner'
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

