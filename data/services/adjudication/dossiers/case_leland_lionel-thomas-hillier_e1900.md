<!-- {"case_id": "case_leland_lionel-thomas-hillier_e1900", "bio_ids": ["leland_lionel-thomas-hillier_e1900"], "stint_ids": ["Leland, L. T. H___Grenada___1910", "Leland, L. T. H___Weihaiwei___1910"]} -->
# Dossier case_leland_lionel-thomas-hillier_e1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `leland_lionel-thomas-hillier_e1900`

- Printed name: **LELAND, Lionel Thomas Hillier**
- Birth year: not printed
- Appears in editions: [1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1912-L45632.v` — printed in editions [1912, 1913]:**

> LELAND, Lionel Thomas Hillier.—Capt., 4th Batt. S. Staffs. Regt. (late lieut., Worcester Regt.); ed. at St. Columba's Coll. and Dublin Univ.; 2nd lieut., Mid-Ulster Art., 1900; P.S. certif.; apptd. to take draft of Irish Ycomanny to S. Africa; attached to 1st M.I.; operations, 1901-1902 (Queen's medal with five clasps); comanr., R.G.R., passed A. and B.; M.I. certif.; long course Hythe certif.; special topographical employment; served in Canada 3½ yrs., until withdrawal of Imperial garrison in 1905; transf'd. to Worcester regt. and posted to 1st Batt., 1906; passed C. and D.; ast. instr. in topography; resigned, Nov., 1908; apptd. 2nd clk. to gov', Windward Is., Dec., 1908; priv. sec. and A.D.C. to Sir J. H. Sadler, gov. of Windward Is., Aug., 1909; ast. dist. comanr., E.A.P., Mar., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | 2nd lieut., Mid-Ulster Art | — | [1912, 1913] |
| 1 | 1901–1902 | operations | — | [1912, 1913] |
| 2 | 1905 | served in Canada 3½ yrs., until withdrawal of Imperial garrison in | — | [1912, 1913] |
| 3 | 1906 | transf'd. to Worcester regt. and posted to 1st Batt | — | [1912, 1913] |
| 4 | 1908 | resigned | — | [1912, 1913] |
| 5 | 1908 | apptd. 2nd clk. to gov', Windward Is | — | [1912, 1913] |
| 6 | 1909 | priv. sec. and A.D.C. to Sir J. H. Sadler, gov. of Windward Is | — | [1912, 1913] |
| 7 | 1912 | ast. dist. comanr. | East Africa Protectorate | [1912, 1913] |

## Candidate stint `Leland, L. T. H___Grenada___1910`

- Staff-list name: **Leland, L. T. H** | colony: **Grenada** | listed 1910–1911 | editions [1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | L. T. H. Leland | Private Secretary and A.D.C. | Governor | — | — |
| 1911 | L. T. H. Leland | Private Secretary and A.D.C. | Governor | — | Captain |

### Deterministic checks: `leland_lionel-thomas-hillier_e1900` vs `Leland, L. T. H___Grenada___1910`

- [PASS] surname_gate: bio 'LELAND' vs stint 'Leland, L. T. H' (exact)
- [PASS] initials: bio ['L', 'T', 'H'] ~ stint ['L', 'T', 'H']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Grenada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1911
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Leland, L. T. H___Weihaiwei___1910`

- Staff-list name: **Leland, L. T. H** | colony: **Weihaiwei** | listed 1910–1911 | editions [1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | L. T. H. Leland | Private Secretary | Civil Establishment | — | — |
| 1911 | Lieut. L. T. H. Leland | Private Secretary and A.D.C. | Civil Establishment | — | — |

### Deterministic checks: `leland_lionel-thomas-hillier_e1900` vs `Leland, L. T. H___Weihaiwei___1910`

- [PASS] surname_gate: bio 'LELAND' vs stint 'Leland, L. T. H' (exact)
- [PASS] initials: bio ['L', 'T', 'H'] ~ stint ['L', 'T', 'H']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Weihaiwei'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1911
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

