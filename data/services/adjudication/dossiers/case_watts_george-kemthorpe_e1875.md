<!-- {"case_id": "case_watts_george-kemthorpe_e1875", "bio_ids": ["watts_george-kemthorpe_e1875"], "stint_ids": ["Watts, G. K___Kenya___1909"]} -->
# Dossier case_watts_george-kemthorpe_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Watts, G. K___Kenya___1909` is also gate-compatible with biography(ies) outside this case: ['watts_george-kempthorne_e1875'] (already linked elsewhere or filtered).

## Biography `watts_george-kemthorpe_e1875`

- Printed name: **WATTS, George Kemthorpe**
- Birth year: not printed
- Honours: A.M.I.C.E.
- Appears in editions: [1908]

### Verbatim printed entry text (OCR)

**Version `col1908-L48108.v` — printed in editions [1908]:**

> WATTS, George Kemthorpe, A.M.I.C.E.—Ch. engr., India pub. wks. dept.; trained at K.I.E. Coll., apptd. 1st Oct., 1875, and posted to Hyderabad; exec. engr., Nov., 1881; asst. to suptgd. engr., Sept., 1886; transf. to Assam, 1895; to N.W. Provinces, and Oudh, Dec., 1900; suptgd. engr., Dec., 1900; to Cent. Provinces; officiating ch. engr., and sec. to ch. commr., July, 1905; confirmed, Sept., 1905; commr. of wks., E. Africa Prot., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | — | Hyderabad | [1908] |
| 1 | 1881 | exec. engr. | — | [1908] |
| 2 | 1886 | asst. to suptgd. engr. | — | [1908] |
| 3 | 1895 | — | Assam | [1908] |
| 4 | 1900 | — | North-West Provinces and Oudh | [1908] |
| 5 | 1900 | suptgd. engr. | — | [1908] |
| 6 | 1905 | officiating ch. engr., and sec. to ch. commr. | — | [1908] |
| 7 | 1905 | — | — | [1908] |
| 8 | 1907 | commr. of wks. | East Africa Protectorate | [1908] |
| 9 | ? | Ch. engr. | India | [1908] |
| 10 | ? | — | Central Provinces | [1908] |

## Candidate stint `Watts, G. K___Kenya___1909`

- Staff-list name: **Watts, G. K** | colony: **Kenya** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | G. K. Watts | Commissioner | Public Works | — | — |
| 1910 | G. K. Watts | Commissioner | Public Works | — | — |

### Deterministic checks: `watts_george-kemthorpe_e1875` vs `Watts, G. K___Kenya___1909`

- [PASS] surname_gate: bio 'WATTS' vs stint 'Watts, G. K' (exact)
- [PASS] initials: bio ['G', 'K'] ~ stint ['G', 'K']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1910
- [FAIL] position_sim: best 42 vs bar 60: 'commr. of wks.' ~ 'Commissioner'
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

