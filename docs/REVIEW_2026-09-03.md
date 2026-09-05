# Project review 2026-09-03 — remaining errors in linking, grounding, visualization

Five empirical audits run against the current data (CO = `data/kg/graph_stage3`,
IOL = `data/iol/graph_stage3`, volume layer = `data/volume`, atlas = `docs/`).
Every QID in the graph was re-fetched from Wikidata (QLever + wd-mcp) and
type-checked; identity screens were run on both corpora; the atlas was loaded
headlessly. Nothing in the repo was changed by the review. Items marked
**[verified]** were re-checked by hand; **[check]** need a human look.

Detail files (scripts + raw outputs) were left in the session scratchpad
(`persons/`, `insts/`, `linking/`, `places/`, `viz/`).

---

## A. Stale build artefacts — fix these first, they invalidate downstream numbers

1. **IOL edge layers are stale vs the persons spine** [verified]. `persons.jsonl` /
   `career_events.jsonl` were re-emitted 2026-07-11 22:10 (bios-fix cycle, 19,513
   persons); `role_edges`, `honour_edges`, `education_edges`, `employment_edges`,
   `qualification_edges` date from 14:06. Orphan edges: role 5,351 rows / 991
   persons; honour 487/307; education 272/185; employment 209/82; qualification
   44/35. Inverse gap: 1,159 IOL persons have events but zero role edges; 897
   persons in `honours.jsonl` have no honour edge. CO has 0 orphans.
   Fix: full `reemit_dedup.sh iol` (incl. `kg_remap_edge_layers.py`), then assert
   orphans = 0 in a check script.
2. **Volume census tables predate the B1 careers rebuild** [verified by mtime].
   `career_classes(_measured).jsonl` 05:32 vs `careers.jsonl` 11:24 (same day). 2,596
   non-suspect careers (11,424 records) are now neither linked nor classed
   (`ANTIGUA|gordon|31`, `BARBADOS|clarke|110`, `BARBADOS|smith|223`). Headline
   drift: CLASSC.md linked 23,226 → 20,516; "33,785/179,147 (18.9%)" → 31,075/179,033
   (17.4%); never-bio'd from files 135,080 (the 134,433 in the kickoff doc comes from
   no file). Fix: "linked-or-classed" invariant in `volume_identity_check.py`; rerun
   `volume_classc_worklist.py` → judge delta → `volume_apply_classc_links.py`.
3. **Atlas built from the older IOL spine** [verified]. `docs/data` built 2026-07-06
   (meta roster.io 17,922); 898 of 17,490 IOL ids in `careers.json`/`search.json` no
   longer exist in `persons.jsonl`. `docs/data_edu` (2026-07-03) is older still (it
   carries Q7981360 with edges that no longer exist). 37 search rows have name "?".
4. **Published counts disagree with each other** — README 27,739 persons / 180,830
   events vs `kg_stats.json` 27,636 / 180,564; static `index.html` 47,360 officials /
   22,485 transfers vs rendered 45,558 / 35,824; about.html + blog "46,000"; IOL
   persons 17,922 / 19,351 / 19,513 across docs; header "1820–1966" beside
   "OFFICIALS, 1815–1966" in the same panel; IOL never-bio'd 25,828 / 31,743 / 32,287;
   A7 "15" vs 4 remaining.

## B. Place / colony grounding

5. **"Union of S. Africa" / "S. Africa" / "S.A." → Q5155572 British South Africa
   Company territory (Rhodesia), 960 CO events** [verified]. Five rows in
   `data/kg/places_grounding.jsonl`, all `match_type=manifest query="South Africa"`
   — the manifest join matched by containment. Q193619 Union of South Africa
   already exists. The atlas plots this node at Harare with 283 in / 289 out arcs.
   Fix the 5 cache rows → Q193619 (pre-1910 "S. Africa" is ambiguous, ~100 ev),
   add a containment guard in `kg_join_manifest.py`, re-emit.
6. **Penang → Q188096 (state of Malaysia, 1957+)**, 1,083 place / 1,292 colony CO
   events; label-locked so it looks right. Target: Q1150673 place, colony Straits
   Settlements Q376178 pre-1946 (via `colony_canon.json` + crosswalk).
7. **Baluchistan colony = Q843 Pakistan** (50 IOL events; label says "Baluchistan",
   atlas shows two "Baluchistan" nodes). Q2336399 also duplicates Q3303188.
   `colony_canon.json` Q843→Q3303188, fold Q2336399.
8. **Ambiguous city surfaces flat-grounded to the wrong hemisphere**: Perth → Scotland
   (25 ev, 21 are W. Australians), Albany → WA (40 ev, mostly Cape), Newcastle →
   upon Tyne (37, mostly Natal), Bathurst → Banjul (20, mostly Cape/NSW), Kingston
   Jamaica 74 vs Ontario 9. Route through `resolve_context.py`.
9. **Non-place / wrong-entity QIDs**: Southampton→Q8842 *Virgo* (IOL), Anglesey→Q62870
   *human*, Wigan→Q151588 *film*, "Nagpur, Central Provinces"→Q14112 *Corsica* (3,
   mcp_verified!), Ahmedabad City→Q1129 *Hainaut*, Lourenco Marques→Q3922 *Detmold*,
   St Pancras→Q2349413 (Slovenia), Dharwar→Q3852743 **redirect** (48), Belize→
   Q115829224 (an *event*, 81 ev), Western Pacific→Q1545934 (a *commission*, no
   coords, 153 ev), Transkei→Q466551 (1976 bantustan, 46 ev), **S.E. Asia →
   colony British New Guinea** (28 ev, the case TODO #10 called fixed).
10. **IOL modern-state stragglers** (seeded via `seed_iol1937`, missed by the
    reground list): Sudan Q1049 (41), Scinde Q37211 Pakistan province (30), Bahrein
    Q398 (20), Koweit Q817, Burma circle/Prov. Q836 Myanmar (12), South Africa
    Q258 (94), Singapore Q334, Sikkim/Assam/Mysore modern states on the CO side,
    China CO Q29520 (geographic concept) vs IOL Q148 PRC, Ireland CO island vs IOL
    Republic, Persia CO Iran vs IOL Qajar. Extend `kg_reground_colonies.py`.
11. **Q252 Indonesia labelled "Dutch East Indies (British Occupation)"** still takes
    Java/Sumatra/Batavia/Borneo (30 ev) via crosswalk `admin_walk`.
12. **Samoa canon reversed**: `colony_canon.json` folds period Q7988268 → modern Q683
    (opposite direction to every other entry).
13. **IOL "Central Prov." / "Cent. Provs." / "C.P." ≈ 1,250 events ungrounded** though
    Q521864 already carries 2,077 — abbreviations never reached the cache.
14. **Modern labels on correct QIDs** (Kolkata 1,880 ev, Yangon 525, Prayagraj 318,
    Varanasi, Pune, Shimla, Mumbai, Chennai, Makhanda, Banjul, Maputo…; Ceylon vs
    British Ceylon, Kenya vs Kenya Colony differ between corpora). Needs a
    `place_label_lock.json` applied at emit for both corpora.
15. TODO #12 still open: 8 grounded persons whose every colony is Q84 (Anderson,
    Coghlan, Nash…), 46 grounded persons with no colony at all; British West Africa
    Q918150 (122 ev) rolls to the UK metropole.

## C. Institution / role / honour / organisation grounding

16. **"Pol. Agent" → "police agent"** [verified]: `col_match/kg/normalize.py:83`
    expands `pol→police` although `pol` is in `_PRE_AMBIGUOUS`. IOL 1,195 edges on
    `colkg:police_agent` (+64 compounds, 73 folded into magistrate) vs 379 on
    `political_agent`.
17. **"Lieut.-Col." → "lieut colonial" → folded into *lieutenant* Q186024**: IOL 468,
    CO 159 edges (`col→colonial` expansion + the lieutenant fold rule).
18. **Four role/honour QIDs are Wikidata redirects**: inspector Q27214348→Q11977377
    (CO 2,545 / IOL 612 edges), accountant Q3929433→Q326653 (1,579/530), chief
    accountant Q12096582→Q10783678, F.R.S.A. Q15271633→Q4905728. Hard-coded in
    `kg_role_fold_rules.py` and the grounding caches.
19. **IOL education recall**: "Trained at …" / "Appointed from …" never parsed
    (`education_parsed.jsonl` → `institutions: []`). Cooper's Hill 669 mentions → 50
    edges; Thomason 117 → 57; Haileybury 120 rows no edge; 6,533 / 11,047 IOL
    education rows unlinked. Degrees inside education strings (IOL B.A. 1,549, M.A.
    1,377, LL.B. 322, B.L. 360; CO B.A. 1,680) never reach the qualification layer.
20. **Haileybury conflation**: 94/109 edges are pre-1858 ICS men attached to the 1862
    public school Q5639263 instead of the East India Company College Q142599.
    **CO Sandhurst** cached to the 1947 Academy Q575618 (50 edges, attendees b.1827–81)
    instead of Q17020147.
21. **CO honours internal-minted although QIDs exist**: M.V.O. (75), K.C.V.O. (44),
    C.I.E./C.S.I./K.C.S.I./G.C.S.I./G.C.I.E., V.D. (44), Croix de Guerre split over 4
    nodes, IOL Kaisar-i-Hind over 6 nodes. Grade granularity differs between corpora
    (IOL grounds all CIE grades to the order Q93710; CO per grade).
22. **CO worklist drops abbreviated-parent forms**: "Royal College, Maur.", "Lyceum,
    Malta", "Queen's College, B. Guiana", "Harrison College, Barb.", "Edin.
    University", "Christ's Hosp." absent from `education_worklist.jsonl`; 7,227 /
    19,220 CO education rows have no edge, 4,591 of them contain an institution word.
    Plus 55 apostrophe/"The " variants internal-minted beside their QID surface, and
    108 "<school>, <university city>" garbage mints from the parent binder.
23. **Ambiguous-surface rule violations**: "St. Ignatius College" → Galway (contexts
    Malta ×2, Stamford Hill); "Royal Grammar School" → one QID (Lancaster/Newcastle/
    Colchester contexts). [check] "St Paul's School" → London (CO 133 + IOL 105; some
    Grenada/Malta/Darjeeling), "Royal College" → Curepipe (2 are Colombo), "St
    Andrew's College" → Dublin (6 Grahamstown vs 3 Dublin). IOL "St. Xavier's High
    School, Bombay" → Q26258687 (1957 academy) should be Q7592184.
24. **Anachronistic labels not locked; the lock is CO-only** (`kg_ground_institutions.py:39`
    hard-codes `data/kg`). IOL: Thomason College shows as "IIT Roorkee" (94),
    Rangoon → Yangon (45), Presidency College → Presidency University, Agra → Dr.
    Bhimrao Ambedkar University, Sibpur → IIEST, M.A.O. → Aligarh Muslim. CO: Owen's
    College → University of Manchester (115), S. African College → UCT (119), King's
    College Durham → Newcastle University, East London College → QMUL, Canterbury
    College, Acadia/Dalhousie/Brandon "University". All visible in the education atlas.
25. **Role folds that conflate offices**: private secretary → secretary Q80687 (187);
    member of governor's executive council → *legislator* (307); governor general →
    governor (50); surgeon major → major (142); judge advocate → judge; IOL
    collector spread across generic magistrate / `colkg:collector` /
    `collector_and_magistrate`; `colkg:first_commission` (1,007) and
    `colkg:arrived_in_india` (488) are events, not roles.
26. [check] Orgs: Kowloon–Canton Railway *Corporation* Q838436 (1982) for 1913–38
    edges; Crown Agents Ltd Q5189307 (1997) for 1901–22; Uganda Railway Q500115 is a
    line not an employer.

## D. Person identity and person→Wikidata grounding

27. **Namesake mis-groundings that a death-date veto would catch** [verified against
    WD P570]: `kgp_col1929-p1058b14` STEWART Charles (Premier of Alberta, events to
    1921) → Q130573420 army officer d.1916; `kgp_col1966-p313b9` STOTT D. (N.
    Rhodesia roads engineer 1949–62) → Q5295192 NZ SOE officer d.1945. [check]
    COWAN James `kgp_col1907-p635b7` → Q6131820 (d.1890, event 1897); BRABANT
    `kgp_col1911-p636b4`. 8 birth-year mismatches where the KG birth is wrong
    (Lagden 1861 vs 1851, Lockhart 1865 vs 1858 …). Add P570 < last-event veto to
    `verify_person_qids.py`. Item #13 (QIDs on ≥2 persons) is closed: 0 remain.
28. **IOL under-merge on the 1945/1947 editions**: 120 identical (surname, full given,
    birth) edition-disjoint pairs, 83 with one side only in 1945/47 (BRAY Denys de
    Saumarez `kgp_iol1945-c807765` / `kgp_iol1929-c2829375`; COLVIN; BISWAS;
    RUNGANADHAN/RUNGANATHAN OCR pair); 1,701 identical-full-name edition-disjoint
    pairs never assessed. The Jul-11 merge-audit apply reopened splits
    (17,922 → 19,513). Rerun `kg_dedup_apptchain_candidates.py` on the current spine
    plus an exact-name+birth block.
29. **CO under-merges across the 1940→1948 gap** (given names normalised differently
    post-war: "John Sloman" vs "JOHN SLOMAN"): BENNETT `kgp_col1948-p416b11` /
    `kgp_col1956-p286b5`, MARNHAM, HAYWARD, BAYLY Z.S. ×3. A6 same-honour duplicates:
    CO 175 groups / IOL 101 (confirmed dupes: AZOPARDI, ASHWORTH, BEADLES, BARKER,
    BARNARD, BARNES).
30. **Peerage titles** (item #3 still open): under-merges NOVAR = MUNRO-FERGUSON,
    ONSLOW ×2, CROMER = "Baring, Evelyn"; 22 CO + 10 IOL titled governors/viceroys
    ungrounded (Willingdon, Lansdowne, Lugard, Tweedsmuir, Curzon, Kitchener,
    Linlithgow, Wavell …); cross-corpus bridges missing for Irwin/Halifax, Willingdon,
    Islington, Dufferin/Blackwood, Elgin/Bruce. 10 of 20 probed senior ungrounded
    CO officials are groundable with exact birth (Smith→Q18546195, Young→Q4800773,
    O'Malley→Q16029358 …). IOL has **no person grounding at all** (423 strict-senior
    persons; Gait = Q5341525 etc.).
31. **Garbled years driving the age/span screens**: births ≥ 1950 (CO 3, IOL 1),
    birth == honour year (12), birth ≥ first event (71 CO), spans > 65 yr (35, all
    one garbled year: Prinsep "1741", Taylor "1812"); duplicate (honour, year) rows on
    72 CO persons ("K.B.E." + "B.E." 1921). Suggest a plausibility rule in
    `kg_apply_year_fixups.py`.
32. **Junk person records**: 110 CO null-surname persons (56 with 0 events); 131 CO /
    46 IOL 0-event persons; supplement fragments with surname "A.", "C.B.", "BACH" ×8,
    "6)", "JOHN OF JERUSALEM" (the Order parsed as a person); IOL "JUNE, LAPHAI ZAU",
    "January, MUHAMMAD", "THE, U Po"; peerage boilerplate in given_names (109).
33. FARR `kgp_col1939-p985b23` over-merge still unsplit. Bridges exist only in
    `docs/data/bridges.json` (no field in persons.jsonl); `iol_col_links.jsonl` ≈73%
    precision on a 15-link read (YOUNG, BROWN, WALLACE, GRIFFITH wrong) and is
    unmeasured in IOL_COL_JOIN.md.

## E. Volume linking (COL roster → career → person)

34. **Nothing from the COL silver action list was applied** — the 3 applied-link FPs
    (musgrave|20409, maclure|38002, bach|133384) and the Buchanan false-B are
    untouched; all checkers report green because they do not test these.
35. **Judged-'different' false negatives ≈ 4,400 careers**: 2,101 of 11,425 class-C
    never-bio'd careers sit in the rare-surname + era-overlap stratum where the
    silver FN rate was 76%. Prompt defects in `nibi/qwen_classc_worker.py` (judge
    not told a candidate's existing links; edition lag; retrospective governor
    lists; 'in addn').
36. **Colony gate has 53 sub-colony→parent gaps** (`_colony_target_set`, match.py:55):
    Lagos / Eastern & Northern Provinces / Kaduna / Enugu / Ibadan → Nigeria; Northern
    Territories → Gold Coast; Transkei / Griqualand → Cape; Zululand → Natal;
    BC / Sask / Alberta / PEI → Canada; Labrador, Gozo, Perim, Transjordan, BCA,
    NE/NW Rhodesia, Pemba, Sabah, Ellice, Carriacou, Barbuda, Cayman, Rodrigues,
    Rangoon, Calcutta, Kowloon, Suva, Khartoum. 629 bio persons have a gap-place
    event; re-testing class B with rollups converts 160 careers to class C. Fix via
    `data/services/place_rollup.json`.
37. **apply_t3 = 752 links, all inexact-initials, 79% precision (≈160 FPs)**; 1,299
    links carry at least one deterministic flag (senior row with silent bio 305,
    rank contradictions 225, junk surname 92; `HONG KONG|smith|4536..4543` = 5
    careers on one person).
38. **Junk careers past the `suspect` flag**: 6,188 non-suspect careers / 11,830
    records (office-word surnames 1,367 — hospital 245, vacant 125, commissioner 47,
    undersecretary 100; digits-in-given 1,862; "A and B" 1,869; ditto marks 211;
    same-year same-dept different-salary accretion 1,220). 4,637 of these are counted
    never-bio'd; 116 carry bio links. CAREERS.md's own "longest careers" lists
    `Point, Morant` and `Gormanston, Lord` 1888–1948.
39. **Chain conflations never adjudicated**: 854 careers with two same-year
    departments in disjoint services (522 never-bio'd); 1,225 with ≥3 departments in
    one year; 67 spans ≥45 yr (`CANADA|macdonald|15434` 61y). A3/A4/A5 outputs
    (116/141/218) were never fed to a ledger.
40. **IOL layer state**: A7 events-after-death — 4 persist, 2 judged *same* (Harcourt
    1910:259, Annandale 1924:275) = confirmed over-merges unsplit; the Bhate
    suppress override carries a stale person id; `roll_conflicts.jsonl` stale (32
    verdicts exist); the no-bio layer is split across two generations
    (`nobio_measured.json` vs PROVISIONAL `nobio_persons.jsonl`) with `res_abc /
    res_nobio / res_chain` never applied.

## F. Visualization

41. Pages load clean: 0 console errors, 0 failed requests at 1400×900 and 390×844;
    Esri tiles 200 without a key; no CARTO URLs remain; DOI 302 resolves.
42. Data problems visible on the map: BSAC node at Harare = the South Africa bug (5);
    two "Baluchistan" nodes (7); "Singapore Crown Colony" and "Aden Protectorate"
    duplicated labels; "Dutch East Indies" at Jakarta (11); Penang as a modern state.
43. `LABEL_FIX` (6 entries: Q16, Q30, Q408, Q833, Q148, Q117) is still live in
    `build_static_atlas.py` — display-only masking of modern-collapse labels; retire
    once (14) exists.
44. Education atlas shows 12 modern institution labels (24) and is two builds stale.
45. Leaflet/markercluster come from unpkg.com; fine for GitHub Pages but a single
    point of failure — consider vendoring.

## Suggested order

A1 → A2 → B5 (South Africa) → C16/C17/C18 (one-line normaliser + redirect fixes)
→ B6/B7/B9 (canon + crosswalk rows) → D27 (death veto) → E36 (rollup file) →
E34/E37 (apply silver verdicts, gate apply_t3) → D28/D29 (rerun dedup on current
spines) → B14/C24 (label locks both corpora) → rebuild atlas + edu atlas → A4 (numbers).

---

## Status 2026-09-04 (fix session)

Applied, in the suggested order, all verified against the rebuilt data
(commits 8c4ceb6 … this one):

- **A1** IOL overlay layers re-emitted on the bios-fix spine; overlay orphans
  0; `iol_identity_check` now pins `gs3_orphan_overlay_refs` and
  `gs3_events_no_role_edge`. (Do NOT use `reemit_dedup.sh iol` — its
  school-map re-apply reverts the audited map; the IOL chain is emit +
  overlays, see the A1 commit.)
- **A2** class table rerun on the B1 careers (158,517 classed; 2,596 formerly
  unclassed); verdicts re-keyed by content; `classc_worklist_delta.jsonl` =
  3,540 pairs for the next Nibi batch; `career_unlinked_unclassed` pinned 0.
- **E36** colony gate: `data/services/kg_place_colony.json`
  (`build_kg_place_colony.py`, KG career_events → colony QID → roster header
  via curated `colony_qid_roster.json`); gap events 33,197 → 16,286.
- **E34/E37** `classc_hand_verdicts.jsonl` ledger (3 silver FPs suppressed,
  28 overturned negatives applied); `apply_t3` gated to det=hard. Links
  10,559 → 10,009.
- **B5–B10, B14** place caches patched (`kg_patch_place_cache.py` ←
  `place_qid_patches.json`), crosswalk/canon/seat overrides, place label
  lock; both spines re-emitted. B8 homonym towns resolved per person
  (emitter now consults the context map before the flat cache hit).
- **C16–C18, C20, C21, C23–C25** normaliser (pol./col. by neighbour token),
  redirect QIDs, honour grades, Sandhurst/Haileybury, ambiguous colleges,
  corpus-overlayable institution label lock, role-fold fixes.
- **D27** `verify_person_deaths.py` (P570 veto): 21 groundings dropped.
- **D28/D29** 131 deterministic appointment-chain unions (IOL 19,513 →
  19,400). The "120 exact name+birth 1945/47 pairs" do not reproduce on the
  current table (0 pairs); the 498 apptchain candidates the Nibi batch judged
  *different* were left as judged (a deterministic-vs-judge conflict pool).
- **A3/A4** both atlases rebuilt (roster 27,526 CO / 19,400 IOL, 36,431
  arcs); 110 nameless spine stubs dropped at emit; README / index / about
  counts reconciled to `kg_stats.json` + `meta.json`.

Still open (not attempted): B11 (Q252 crosswalk admin_walk), B12 (Samoa canon
direction), B13 (Central Prov. abbreviations), B15 (Q84-only persons), C19
(IOL education recall: "Trained at…"), C22 (CO abbreviated-parent worklist
forms), C26 (org anachronisms), D30–33 as listed, E35 (judge-prompt defects —
Nibi), E38/E39 (junk careers + chain conflations → ledger), F40–45, and the
`kg_join_manifest` containment guard (the wrong rows are patched; the guard
only matters for the next worklist run). A7 pool: McArthur
`kgp_iol1917-c3754007`. Kingston, Ontario rolls to Dominion of Canada (Q1904
override not applied because a crosswalk row already existed).
