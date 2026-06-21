import json, re
def nws(s): return re.sub(r"\s+"," ",(s or "")).strip().lower()
BATCH="data/kg/review/residue/batch_009.jsonl"; OUT="data/kg/review/verdicts/verdicts_res_009.jsonl"
GEC="Gilbert and Ellice Islands Colony"
D={
("kgp_col1936-p992b18","events[2].place"):("keep","J'lem dist.",None),
("kgp_col1936-p992b18","events[8].place"):("keep","J'lem dist.",None),
("kgp_col1936-p992b18","events[10].place"):("keep","J'lem dist.",None),
("kgp_col1954-p335b16","events[1].place"):("correct","air min.","Air Ministry"),
("kgp_col1937-p1019b15","events[1]"):("keep","tech. inst., 35",None),
("kgp_col1937-p1019b15","events[2]"):("keep","tech. inst., 35",None),
("kgp_col1940-p1054b20","events[0].place"):("keep","dept. agr.",None),
("kgp_col1937-p1030b7","honours[0].year"):("keep","O.B.E. (29)",None),
("kgp_dol1935-p1005b17","events[6].place"):("keep","(Can.)",None),
("kgp_dol1935-p1005b17","events[7].place"):("keep","(Can.)",None),
("kgp_col1950-p622b12","events[0].place"):("keep","J'ca.",None),
("kgp_col1950-p622b12","events[1].place"):("keep","J'ca.",None),
("kgp_col1950-p622b12","events[2].place"):("keep","J'ca.",None),
("kgp_col1950-p622b12","events[3].place"):("keep","J'ca.",None),
("kgp_col1940-p1064b9","events[5].place"):("keep","pub. wks. dept.",None),
("kgp_col1949-p567b16","events[0].place"):("drop","",None),
("kgp_col1940-p1062b5","events[1].place"):("keep","dept. of just.",None),
("kgp_col1950-p625b13","events[11].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1954-p348b7","events[0].place"):("drop","",None),
("kgp_col1954-p348b7","events[9].place"):("drop","",None),
("kgp_col1940-p1070b5","events[0].place"):("keep","Wye Coll.",None),
("kgp_col1940-p1070b17","events[1].year_end"):("keep","1899-02",None),
("kgp_col1950-p642b4","events[2].place"):("drop","",None),
("kgp_col1959-p286b19","events[3].place"):("keep","fed. sup. ct.",None),
("kgp_col1959-p288b7","events[1].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1957-p289b17","events[0].place"):("drop","",None),
("kgp_col1957-p289b17","events[1].place"):("drop","",None),
("kgp_col1964-p228b14","events[0].year_end"):("drop","",None),
("kgp_col1956-p286b20","events[9].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1953-p257b14","events[1].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1951-p499b20","events[3].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1959-p313b15","events[0].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1963-p277b2","events[3].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1963-p281b3","events[2].place"):("keep","dist. admin.",None),
("kgp_col1963-p281b3","events[3].place"):("keep","dist. admin.",None),
("kgp_col1963-p281b3","events[4].place"):("keep","dist. admin.",None),
("kgp_col1963-p281b3","events[5].place"):("keep","dist. admin.",None),
("kgp_col1963-p281b3","events[6].place"):("keep","dist. admin.",None),
("kgp_col1950-p477b11","events[2].place"):("keep","educ. dept., Ken.",None),
("kgp_col1951-p512b2","events[2].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1964-p253b6","events[1].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1954-p291b20","events[2].place"):("keep","sup. ct.",None),
("kgp_col1950-p504b10","events[0].year_end"):("drop","",None),
("kgp_col1950-p504b10","events[1].year_end"):("drop","",None),
("kgp_col1950-p504b10","events[2].year_end"):("drop","",None),
("kgp_col1959-p354b11","events[9].place"):("keep","fed. sup. ct., Nig.",None),
("kgp_col1959-p359b9","events[3].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1948-p475b20","events[1].place"):("keep","Ken. govt.",None),
("kgp_col1956-p343b12","events[3].place"):("keep","govt. sch.",None),
("kgp_col1955-p321b8","events[4].place"):("keep","Mal. met. servs.",None),
("kgp_col1955-p321b8","events[5].place"):("keep","Mal. met. servs.",None),
("kgp_col1951-p584b13","events[0].place"):("keep","J'ca.",None),
("kgp_col1951-p584b13","events[1].place"):("keep","J'ca.",None),
("kgp_col1951-p584b13","events[2].place"):("keep","J'ca.",None),
("kgp_col1951-p584b13","events[3].place"):("keep","J'ca.",None),
("kgp_col1951-p584b13","events[4].place"):("keep","J'ca.",None),
("kgp_col1951-p584b13","events[5].place"):("keep","J'ca.",None),
("kgp_col1951-p584b13","events[6].place"):("keep","J'ca.",None),
("kgp_col1955-p325b14","events[9].place"):("keep","maj. wks. comtee.",None),
("kgp_col1951-p593b2","events[0].year_end"):("drop","",None),
("kgp_col1951-p593b2","events[1].year_end"):("drop","",None),
("kgp_col1951-p593b2","events[2].year_end"):("drop","",None),
("kgp_col1951-p593b2","events[3].year_end"):("drop","",None),
("kgp_col1951-p593b2","events[4].year_end"):("drop","",None),
("kgp_col1966-p274b17","events[3].place"):("keep","1st dist., St. L.",None),
("kgp_col1953-p298b13","events[0].place"):("keep","J'ca",None),
("kgp_col1953-p298b13","events[1].place"):("keep","J'ca",None),
("kgp_col1953-p298b13","events[2].place"):("keep","J'ca",None),
("kgp_col1953-p298b13","events[3].place"):("keep","J'ca",None),
("kgp_col1953-p298b13","events[5].place"):("keep","J'ca",None),
("kgp_col1953-p298b13","events[6].place"):("keep","Ken.",None),
("kgp_col1953-p298b13","events[7].place"):("keep","Ken.",None),
("kgp_col1953-p298b13","events[8].place"):("keep","Ken.",None),
("kgp_col1954-p323b11","events[0].place"):("drop","",None),
("kgp_col1961-p433b2","events[0].year_end"):("drop","",None),
("kgp_col1961-p433b2","events[1].year_end"):("drop","",None),
("kgp_col1961-p433b2","events[2].year_end"):("drop","",None),
("kgp_col1965-p318b14","events[2].year_end"):("keep","1955/6",None),
("kgp_col1964-p364b4","events[0].year_end"):("drop","",None),
("kgp_col1964-p364b4","events[1].year_end"):("drop","",None),
("kgp_col1963-p423b15","events[0].place"):("keep","J'ca.",None),
("kgp_col1963-p423b15","events[1].place"):("keep","Carib. comsn.",None),
("kgp_col1950-p605b16","events[2].place"):("drop","",None),
("kgp_col1958-p428b12","events[0].place"):("drop","",None),
("kgp_col1956-p392b7","events[1].place"):("drop","",None),
("kgp_col1950-p607b4","events[0].year_end"):("drop","",None),
("kgp_col1955-p353b16","events[4].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1957-p448b11","events[0].place"):("drop","",None),
("kgp_col1964-p397b23","events[3].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1965-p355b20","events[0].place"):("keep","Barb.",None),
("kgp_col1965-p355b20","events[1].place"):("keep","Barb.",None),
("kgp_col1965-p355b20","events[2].place"):("keep","Barb.",None),
("kgp_col1965-p355b20","events[3].place"):("keep","Barb.",None),
("kgp_col1937-p1047b19","birth_year"):("drop","",None),
("kgp_col1908-p605b12","events[6].place"):("keep","S. Nig. regt.",None),
("kgp_col1907-p637b9","events[2].place"):("keep","N. (now W.) Dist.",None),
("kgp_col1909-p663b18","events[2]"):("keep","rebellion, 1896",None),
("kgp_col1909-p663b18","events[3]"):("keep","May, 1899",None),
("kgp_col1909-p663b18","events[4]"):("keep","1900-2",None),
("kgp_col1909-p663b18","events[5]"):("keep","1902-4",None),
("kgp_col1909-p663b18","events[6]"):("keep","4th Nov., 1904",None),
("kgp_col1909-p663b18","events[7]"):("keep","Aug., 1905",None),
("kgp_col1912-p658b18","events[2].place"):("keep","W. dist.",None),
("kgp_col1912-p658b18","events[4].place"):("keep","S. dist.",None),
("kgp_col1909-p666b23","events[6].year_end"):("keep","31st Aug., 1902",None),
("kgp_col1913-p675b17","events[16].place"):("keep","N. dist.",None),
("kgp_col1910-p679b15","events[4].place"):("drop","",None),
("kgp_col1909-p691b6","events[2].place"):("keep","bd. of educn.",None),
}
rows=[]; missing=[]; badev=[]; npk=0; allkeys=set()
recs=[json.loads(l) for l in open(BATCH)]
for o in recs:
    for pk in o["packets"]: allkeys.add((o["person_id"],pk["field_path"]))
for o in recs:
    nsrc=nws(o["source_text"])
    for pk in o["packets"]:
        npk+=1; key=(o["person_id"],pk["field_path"])
        if key not in D: missing.append(key); continue
        v,ev,corr=D[key]
        if v in ("keep","correct") and nws(ev) not in nsrc: badev.append((key,ev))
        rows.append({"person_id":o["person_id"],"field_path":pk["field_path"],"flagged_value":pk["flagged_value"],
            "reason":pk["reason"],"verdict":v,"corrected_value":corr,"source_evidence":ev,
            "confidence":0.95,"rationale":"main-loop review"})
extra=[k for k in D if k not in allkeys]
print("packets:",npk,"decided:",len(rows),"missing:",len(missing),"badev:",len(badev),"extra:",len(extra))
for m in missing[:40]:print("  MISSING",m)
for b in badev[:40]:print("  BADEV",b)
for e in extra[:40]:print("  EXTRA",e)
if not missing and not badev and not extra:
    open(OUT,"w").write("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
    from collections import Counter; c=Counter(r["verdict"] for r in rows)
    print("WROTE",OUT,len(rows),"| keep=%d correct=%d drop=%d"%(c['keep'],c['correct'],c['drop']))
else: print("NOT WRITTEN")
