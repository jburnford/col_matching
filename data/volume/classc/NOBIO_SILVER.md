# COL silver-standard scores

200 hand-labeled items across 4 pools (4 unsure, excluded from denominators). Labeled 2026-07-12 by close reading with full context (career records + person events; bio_persons searched by surname variant for the A/B pool).

## 1. Applied-link precision (career_person_links.jsonl)

| stratum | correct (silver=same) |
|---|---|
| all | 40/40 = 100% (CI 91–100%) |
| det:hard | 19/19 = 100% (CI 83–100%) |
| det:llm_only | 7/7 = 100% (CI 65–100%) |
| det:place | 9/9 = 100% (CI 70–100%) |
| det:possim | 5/5 = 100% (CI 57–100%) |
| policy:apply_t1 | 28/28 = 100% (CI 88–100%) |
| policy:apply_t2 | 7/7 = 100% (CI 65–100%) |
| policy:apply_t3 | 5/5 = 100% (CI 57–100%) |

## 2. Judged-'different' reliability (measured never-bio'd negatives)

| stratum | judge 'different' correct |
|---|---|
| all | 21/49 = 43% (CI 30–57%) |
| general | 14/20 = 70% (CI 48–85%) |
| hirisk | 7/29 = 24% (CI 12–42%) |

A silver 'same' here is a FALSE NEGATIVE: a real link judged away, i.e. a career counted never-bio'd that has a bio person. The hirisk stratum oversamples rare surnames with era-overlapping candidates by design.

## 3. Career-chain coherence (careers.jsonl, never-bio'd multi-record chains)

| stratum | confirm | reject (conflation) | junk (non-person) |
|---|---|---|---|
| all | 40/49 = 82% (CI 69–90%) | 2 | 7 |
| general | 28/35 = 80% (CI 64–90%) | 1 | 6 |
| hirisk | 12/14 = 86% (CI 60–96%) | 1 | 1 |

## 4. Class A/B spot-checks (career_classes_measured.jsonl)

| stratum | confirmed never-bio'd | reject (bio exists) | junk (non-person) |
|---|---|---|---|
| all | 44/49 = 90% (CI 78–96%) | 1 | 4 |
| class A | 21/25 = 84% (CI 65–94%) | 0 | 4 |
| class B | 23/24 = 96% (CI 80–99%) | 1 | 0 |

## Judge agreement (classc_results vs silver, pair pools)

- judged pairs scoreable: 98; agreement 67/98 = 68% (CI 59–77%)
- (applied pool selects on judge 'same', negatives pool on judge 'different'; the blended rate is composition-dependent — read the per-pool sections above.)

## Junk-name exemplars recorded as labels

- `AUSTRALIA|side|95657`: non-person: 'Chief Clerk (Criminal Side)' of the Law Officers' Department parsed as a person named 'Criminal Side'; duplicated rows per year
- `CAPE OF GOOD HOPE|brand|2069`: multi-person fusion: given names swallow four other men ('N. Thevissen. J. E. Wood. W. R. Thomson. J. F. Ziervogel. Sir C. J'); the two 1867 rows (1,000l. Kt vs 200l.) are probably different people
- `GOLD COAST|bursar|154935`: non-person: office 'Senior Bursar' (girls' schools) parsed as surname=bursar, given=Senior
- `BERMUDA|august|96183`: non-person: date phrase 'In August' parsed as a name; seven Education 150l. rows accrete to it — month-word junk-name class
- `NEW SOUTH WALES|maitland|50195`: place-as-surname: MAITLAND is the NSW lands district; the person is the actual given-field content 'A. J. Park'; position column holds the other district (Armidale)
- `JAMAICA|administrator|202405`: non-person: office 'Marketing Administrator' parsed as surname=administrator, given=Marketing
- `JAMAICA|dept|167609`: non-person: 'Tech. Dept' parsed as a name; four Board of Education 450l. rows accrete to it
- `LEEWARD ISLANDS|revenue|167811`: non-person: 'Customs Revenue' totals rows parsed as a person; the 'salaries' (49,132l.) are colony revenue totals — also inflates rank=senior
- `AUSTRALIA|undersecretary|99419`: non-person: 'Under Secretary ... M.L.A.' parsed as surname=undersecretary, given=M.L.A; the row is the Secretary for Mines 1,394l.
- `GOLD COAST|pressmen|114997`: non-person: staff-count row '3 Pressmen' parsed as surname=pressmen, given=3
- `AUSTRALIA|undersecretary|99430`: non-person: same 'Under Secretary...M.L.A.' junk-name class as career 99419, here on the Secretary for Lands row

## Disagreement / action list (hand re-adjudication queue)

- MISSED LINK [hirisk] TRINIDAD AND TOBAGO|shuel|147568::kgp_col1950-p605b20: MISSED LINK: rare surname; bio sub-inspr. of constab. Trinidad 1921-25 = roster T&T constabulary sub-inspector; 1925 Nigeria transfer is edition lag; 1923 row also carries a fused 'T. R. Lambert' garble
- MISSED LINK [hirisk] NIGERIA|campton|165543::kgp_col1950-p474b9: PROBABLE MISSED LINK: rare surname, single candidate; Nigeria marine officer from 1928 and marine staff print under [Customs] in 1930-31 editions (cf. Jones E.H.); officer-band salary fits
- MISSED LINK [hirisk] TRANSVAAL|mehliss|92845::kgp_col1923-p880b15: MISSED LINK: judge geography error — Rietfontein hosp. IS Transvaal (public-health hospital); 'Med. supt.' 1900 = roster Medical Superintendent, Public Health Dept 1905-10; rare surname
- MISSED LINK [hirisk] BARBADOS|stoute|87153::kgp_col1931-p1141b12: MISSED LINK: judge age arithmetic wrong (b.1882 = 23 in 1905); clk. dept. of agr. 1898 fits Botanical Dept clerical assistant 75l. 1905; rare surname, C.E.=Cyril Eustace
- MISSED LINK [hirisk] CANADA|forget|44565::kgp_col1909-p712b11: MISSED LINK: unique accented full name 'Amédée E. Forget' printed both sides; roster rows are retrospective Lieutenant-Governors + Privy Council lists of the former Lt.-Gov. of Sask.
- MISSED LINK [hirisk] SOUTH AUSTRALIA|whitington|46860::kgp_col1909-p817b4: MISSED LINK: bio 'chief clk., audit off.' from 1875 (S. Aust. career, later comsnr. of audit) = roster Chief Clerk and Accountant, Audit Department 1886/1890 exactly
- MISSED LINK [hirisk] KENYA|simmonds|175835::kgp_col1958-p429b6: MISSED LINK: dist. offr. Kenya 1935 = cadet 350l. 1936-37; K.W.=Kenneth Willison; 1948 Uganda dep. fin. sec. departure matches roster ending 1948 (edition lag)
- MISSED LINK [hirisk] LEEWARD ISLANDS|harney|100337::kgp_col1955-p311b11: PROBABLE MISSED LINK: roster prints given name 'Clarence A'; bio C.A. Harney b.1902 is a Leeward Is. junior clerk exactly 1922-26; printing-dept post unlisted in bio but grade/era/colony all fit
- MISSED LINK [hirisk] NIGERIA|beeley|169098::kgp_col1950-p457b20: PROBABLE MISSED LINK: rare surname, single candidate, J.H. exact; 1929 Nigeria cadet plausibly sitting as police magistrate 1931-33; bio silent (not contradictory) for 1929-47
- MISSED LINK [hirisk] CAPE OF GOOD HOPE|stanford|17728::kgp_col1914-p814b12: PROBABLE MISSED LINK: Transkeian magistracy printed under the Cape PM's portfolio (Native Affairs branch); senior res. mag. by 1896 fits the 600l. row; asst. chief mag. 1897 follows
- MISSED LINK [hirisk] NIGERIA|pollock|148995::kgp_col1948-p521b10: MISSED LINK: bio prints admin. offr. Nigeria 1923 and asst. sec. Nigeria 1927 = roster Assistant Secretaries 1929-30; J.H.H. exact; 1930 Palestine return matches roster end
- MISSED LINK [hirisk] MALTA|buhagiar|56360::kgp_col1953-p257b21: PROBABLE MISSED LINK: roster row carries B.A,LL.D — the law professor/treasury counsel's profile; Malta 'Prisons (Corradino)' header bleed already seen on the 1936 Rector row; junior legal salary fits 1940
- MISSED LINK [hirisk] SIERRA LEONE|bodley|182972::kgp_col1959-p306b22: MISSED LINK: bio cr. coun. Sierra Leone 1938 = the 1939 Judicial 630l. row (edition lag); rare surname, A.S.=Albert Selwyn; 1939 Tanganyika res. mag. is the departure
- MISSED LINK [hirisk] LEEWARD ISLANDS|sweetescott|98360::kgp_col1930-p1097b3: MISSED LINK: bio itself prints 'gov. [Leeward Is.]' 1906 — Sir E. Bickham Sweet-Escott, Governor L.I. 1906-12, K.C.M.G. both sides; judge claimed he never served there
- MISSED LINK [hirisk] TRINIDAD AND TOBAGO|maingot|54614::kgp_col1940-p998b2: MISSED LINK: bio check clk., customs Trinidad 1915 -> roster 4th clerk Customs 1917 75l.; J.H.=Joseph Henry, rare surname; career name is a ditto-mark garble ('4th „ „ „ J. H')
- MISSED LINK [hirisk] NIGERIA|hartill|193974::kgp_col1958-p351b24: MISSED LINK: rare surname, exact initials; acctnt. Nigeria 1947 and dep. acctnt.-gen. EASTERN Nigeria 1955 bracket the 1949-50 Eastern Provinces rows; judge invented a 'Chief Commissioner' rank from the section heading
- MISSED LINK [hirisk] JAMAICA|mordecai|148715::kgp_col1961-p412b15: MISSED LINK: bio 'cler. asst., treasury' Jamaica 1920 -> roster Treasury 2nd class clerk 1930-37, 1st class 1939-40 -> bio fin. clk 1942, asst. treas. 1944; continuous one-office arc (Sir John Mordecai)
- MISSED LINK [hirisk] WINDWARD ISLANDS|dopwell|137831::kgp_col1957-p329b9: MISSED LINK: St. Vincent IS a Windward Island; bio clk. 1918 -> roster Grenadines/Postal 2nd clerk 1920-23 -> bio customs offr. 1923, ch. clk. G.P.O. 1930; rare surname
- MISSED LINK [hirisk] NORTHERN RHODESIA|knaggs|191284::kgp_col1965-p281b10: MISSED LINK: NR cadet 1946 -> Clerk of the Councils 1952-55 -> seconded sec. to govt. Seychelles 1955 (roster ends exactly then); rare surname, exact initials
- MISSED LINK [hirisk] LEEWARD ISLANDS|foreman|37123::kgp_col1915-p708b11: PROBABLE MISSED LINK: bio ag. mag. + M.L.C. Virgin Is. (a Leeward presidency) in exactly 1880; 200l. fits combined med./mag. post; initial-only key keeps this med
- MISSED LINK [hirisk] BERMUDA|kitchener|104955::kgp_col1912-p714b3: MISSED LINK: Lt.-Gen. Sir F. Walter Kitchener, gov. Bermuda 1908 (bio) = roster Governor & C-in-C 1909-12 with C.B->K.C.B; post-1912 rows are the retrospective governors list ('Lieut.-Gen. — 1908')
- MISSED LINK [hirisk] STRAITS SETTLEMENTS|tongue|158074::kgp_col1940-p1065b3: MISSED LINK: bio 'asst. supt., pol.' 1929/1930 = roster Police Assistant Superintendents 1931-36; the 1934 estate-duties post is 'in addn' (held concurrently) — judge missed that
- MISSED LINK [general] BRITISH GUIANA|chalmers|1197::kgp_col1940-p898b4: MISSED LINK: C.G.C. exact three initials; 4th class Customs 1921 -> bio sub.-comptr., cust. 1928 is continuous progression; same person already applied-linked on his 1928 career row
- MISSED LINK [general] NIGERIA|skinner|157813::kgp_col1951-p650b5: PROBABLE MISSED LINK: roster row is 'Marine Officers, Grade II' under Customs 1929; bio mate, marine dept. Nigeria 1927 -> senr. marine offr. 1940; initial-only key keeps this med
- MISSED LINK [general] WINDWARD ISLANDS|boyd|47588::kgp_col1899-p485b19: MISSED LINK: rare honour fingerprint L.K.Q.C.P.I + L.R.C.S.I printed on BOTH sides; dist. med. offr. Grenada 1883 -> house surgeon Colony Hospital 1886-98 -> Kingston 1898 departure
- MISSED LINK [general] AUSTRALIA|mitchell|78487::kgp_col1939-p1062b6: MISSED LINK: roster row 'Colonial Treasurer (also Premier, etc.)' K.C.M.G. 1922 IS Sir James Mitchell, Premier-and-Treasurer of W.A. 1919-24; K.C.M.G. + premiership printed both sides
- MISSED LINK [general] HONG KONG|edwards|56984::kgp_col1939-p986b6: PROBABLE MISSED LINK: bio HK cadet 1933; the 1934 '?' row at 450-475l. matches the HK cadet scale; only compatible candidate; judge underestimated HK cadet pay
- MISSED LINK [general] BARBADOS|chandler|42507::kgp_col1937-p876b11: MISSED LINK: roster prints 'Sir William K. Chandler, K.C.M.G.' Exec. Council 1929 = the William Kellman Chandler already linked on his 1905 judgeship; judge hallucinated an 1884 death
- CHAIN JUNK [hirisk] AUSTRALIA|side|95657: non-person: 'Chief Clerk (Criminal Side)' of the Law Officers' Department parsed as a person named 'Criminal Side'; duplicated rows per year
- CHAIN REJECT [hirisk] AUSTRALIA|walter|86231: CONTAMINATED CHAIN: core W.A. magistrate/electoral-registrar arc is one man, but 1917-20 Mines rows put him simultaneously in Kimberley/Gascoyne and Coolgardie, and the 1919 row fuses three other men's names ('J. E. Geary...Dr. A. Adams'); Police Dept 'Diocesan Treasurer' is header bleed
- CHAIN JUNK [general] CAPE OF GOOD HOPE|brand|2069: multi-person fusion: given names swallow four other men ('N. Thevissen. J. E. Wood. W. R. Thomson. J. F. Ziervogel. Sir C. J'); the two 1867 rows (1,000l. Kt vs 200l.) are probably different people
- CHAIN JUNK [general] GOLD COAST|bursar|154935: non-person: office 'Senior Bursar' (girls' schools) parsed as surname=bursar, given=Senior
- CHAIN JUNK [general] BERMUDA|august|96183: non-person: date phrase 'In August' parsed as a name; seven Education 150l. rows accrete to it — month-word junk-name class
- CHAIN JUNK [general] NEW SOUTH WALES|maitland|50195: place-as-surname: MAITLAND is the NSW lands district; the person is the actual given-field content 'A. J. Park'; position column holds the other district (Armidale)
- CHAIN REJECT [general] AUSTRALIA|parkinson|77255: CONFLATION: engineer arc (Railways maintenance -> Engineer i/c Irrigation 1,000l.) is one man, but 1940 also prints him Superintendent of POSTAL Services concurrently — a second C.E. Parkinson
- CHAIN JUNK [general] JAMAICA|administrator|202405: non-person: office 'Marketing Administrator' parsed as surname=administrator, given=Marketing
- CHAIN JUNK [general] JAMAICA|dept|167609: non-person: 'Tech. Dept' parsed as a name; four Board of Education 450l. rows accrete to it
- FALSE A/B [B] NIGERIA|buchanan|124926: FALSE B — compatible bio EXISTS and is the same man: G.A. Buchanan b.1876, 'divnl. engr' Lagos railway 1927 = roster Railway Divisional Engineers 960l. 1931; the colony gate failed to map Lagos->Nigeria

