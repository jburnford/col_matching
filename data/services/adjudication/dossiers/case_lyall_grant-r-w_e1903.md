<!-- {"case_id": "case_lyall_grant-r-w_e1903", "bio_ids": ["lyall_grant-r-w_e1903"], "stint_ids": ["Lyall, G. W___Uganda___1910"]} -->
# Dossier case_lyall_grant-r-w_e1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lyall, G. W___Uganda___1910` is also gate-compatible with biography(ies) outside this case: ['lyall_george_e1903'] (already linked elsewhere or filtered).

## Biography `lyall_grant-r-w_e1903`

- Printed name: **LYALL, Grant R. W.**
- Birth year: not printed
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L54143.v` — printed in editions [1922]:**

> LYALL, Grant R. W., M.A. (Aberdeen). L.L.B. (Edin.)—Vans Dunlop schol. in law, Edin. Univ.; called to Scottish bar, 1903; practised till 1909; atty.-gen., Nyasaland, Apr., 1909; ag. judge, high ct., Sept., 1909 to June, 1910, and from Aug., 1912 to May, 1913; judge of high ct., Aug., 1914, and mem., H.B.M. Ct. of Appeal for Eastern Africa; chmn., native rising commn., 1915; chmn. of claims bd. for Nyasaland, under Br. prots. defence O. in C., 1916-19; judge advoc. to Nyasaland-Rhodesia Field Force, 1917-18; atty.-gen., Kenya, July, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903–1903 | called to Scottish bar | — | [1922] |
| 1 | 1909–1909 | atty.-gen. | Nyasaland | [1922] |
| 2 | 1909–1913 | ag. judge, high ct. | — | [1922] |
| 3 | 1914–1914 | judge of high ct., and mem., H.B.M. Ct. of Appeal for Eastern Africa | — | [1922] |
| 4 | 1915–1915 | chmn., native rising commn. | — | [1922] |
| 5 | 1916–1919 | chmn. of claims bd. | Nyasaland | [1922] |
| 6 | 1917–1918 | judge advoc. to Nyasaland-Rhodesia Field Force | — | [1922] |
| 7 | 1920–1920 | atty.-gen. | Kenya | [1922] |
| 8 | ?–1909 | practised | — | [1922] |

## Candidate stint `Lyall, G. W___Uganda___1910`

- Staff-list name: **Lyall, G. W** | colony: **Uganda** | listed 1910–1923 | editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1919, 1920, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | G. W. Lyall | Confidential and Chief Clerk | Administration | — | — |
| 1911 | G. W. Lyall | 2nd Assistant Secretary | Administration | — | — |
| 1912 | G. W. Lyall | 2nd Assistant Secretary | Administration | — | — |
| 1913 | G. Lyall | 2nd Assistant Secretary | Administration | — | — |
| 1914 | G. Lyall | 2nd Assistant Secretary | Administration | — | — |
| 1915 | G. Lyall | 2nd Assistant Secretary | Administration | — | — |
| 1917 | G. Lyall | 1st Assistant Secretary | Administration | — | — |
| 1919 | G. Lyall | 1st Assistant Secretary | Civil Establishment | — | — |
| 1920 | G. Lyall | 1st Assistant Secretary | Administration | — | — |
| 1922 | G. Lyall | 1st Assistant Secretary | Administration | — | — |
| 1923 | G. Lyall | Senior Assistant Secretary | Administration | — | — |

### Deterministic checks: `lyall_grant-r-w_e1903` vs `Lyall, G. W___Uganda___1910`

- [PASS] surname_gate: bio 'LYALL' vs stint 'Lyall, G. W' (exact)
- [PASS] initials: bio ['G', 'R', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1923
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

