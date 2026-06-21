import json, re
def nws(s): return re.sub(r"\s+"," ",(s or "")).strip().lower()
BATCH="data/kg/review/residue/batch_015.jsonl"; OUT="data/kg/review/verdicts/verdicts_res_015.jsonl"
GEC="Gilbert and Ellice Islands Colony"
D={
("kgp_col1966-p258b15","events[5].place"):("correct","min. of inf.","Ministry of Information"),
("kgp_col1965-p291b16","events[1].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1966-p277b23","events[0].year_end"):("drop","",None),
("kgp_col1966-p277b23","events[1].year_end"):("drop","",None),
("kgp_col1965-p308b22","events[0].year_end"):("drop","",None),
("kgp_col1966-p295b9","events[0].year_end"):("drop","",None),
("kgp_col1966-p295b9","events[1].year_end"):("drop","",None),
("kgp_col1966-p308b7","events[0]"):("keep","admly., 9",None),
("kgp_col1966-p308b7","events[1]"):("keep","9–52",None),
("kgp_col1966-p308b6","events[0]"):("drop","",None),
("kgp_col1966-p308b4","events[3].year_end"):("drop","",None),
("kgp_col1966-p308b4","events[4]"):("keep","0–54",None),
("kgp_col1966-p308b13","events[0]"):("drop","",None),
("kgp_col1966-p308b5","events[0]"):("keep","3–47",None),
("kgp_col1966-p308b5","events[1]"):("keep","3–47",None),
("kgp_col1966-p308b5","events[5]"):("keep","4–65",None),
("kgp_col1966-p326b12","events[1].place"):("keep","P.O.",None),
("kgp_col1949-p512b18","events[0].year_end"):("drop","",None),
("kgp_col1950-p550b19","events[4].place"):("keep","P.W.D.",None),
("kgp_col1949-p542b6","events[0].year_end"):("drop","",None),
("kgp_col1949-p542b6","events[1].year_end"):("drop","",None),
("kgp_col1949-p545b12","events[2].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1949-p545b2","events[0].year_end"):("drop","",None),
("kgp_col1949-p545b2","events[1].year_end"):("drop","",None),
("kgp_col1949-p545b2","events[2].year_end"):("drop","",None),
("kgp_col1949-p545b2","events[4].year_end"):("drop","",None),
("kgp_col1949-p545b2","events[6].year_end"):("drop","",None),
("kgp_col1949-p577b3","events[0].year_end"):("drop","",None),
("kgp_col1909-p695b21","events[1]"):("keep","Oct., 1901",None),
("kgp_col1909-p695b21","events[2]"):("keep","Dec., 1906",None),
("kgp_col1909-p695b21","events[3]"):("keep","Apr., 1908",None),
("kgp_col1909-p729b21","events[1]"):("keep","Oct., 1901",None),
("kgp_col1909-p729b21","events[2]"):("keep","Dec., 1906",None),
("kgp_col1909-p729b21","events[3]"):("keep","Apr., 1908",None),
("kgp_col1919-p861b14","events[1].place"):("keep","Ont. legis.",None),
("kgp_col1939-p1046b12","events[4].place"):("keep","harbr. dept.",None),
("kgp_col1931-p1053b9","events[1]"):("keep","901-2",None),
("kgp_col1931-p1089b7","events[1].year_end"):("drop","",None),
("kgp_col1931-p1089b7","events[2].year_end"):("drop","",None),
("kgp_col1931-p1089b7","events[3].year_end"):("drop","",None),
("kgp_col1931-p1089b7","events[4].year_end"):("drop","",None),
("kgp_col1931-p1089b7","events[5].year_end"):("drop","",None),
("kgp_col1931-p1089b7","events[6].year_end"):("drop","",None),
("kgp_col1931-p1089b7","events[7].year_end"):("drop","",None),
("kgp_col1931-p1089b7","events[12].year_end"):("drop","",None),
("kgp_col1931-p1055b3","events[13]"):("keep","cls. 1b, 21",None),
("kgp_col1931-p1055b3","events[14]"):("keep","opium comtee., 23",None),
("kgp_col1931-p1055b3","events[15]"):("keep","F.M.S., 924",None),
("kgp_col1931-p1055b3","events[16]"):("keep","924",None),
("kgp_col1960-p376b14","events[0].year_end"):("drop","",None),
("kgp_col1960-p376b14","events[1].year_end"):("drop","",None),
("kgp_col1908-p622b7","events[0].place"):("keep","Turkish troops",None),
("kgp_col1908-p622b7","events[1].place"):("keep","Egyp. camp.",None),
("kgp_col1908-p622b7","events[2].place"):("keep","Egyp. army",None),
("kgp_col1908-p722b13","events[6].place"):("keep",'dist. "E,"',None),
("kgp_col1908-p646b12","events[1]"):("keep","1899-1900",None),
("kgp_col1908-p646b12","events[2]"):("keep","Pretoria, 1900",None),
("kgp_col1908-p646b12","events[3]"):("keep","1900-1901",None),
("kgp_col1908-p646b12","events[4]"):("keep","Pretoria, 1901",None),
("kgp_col1908-p646b12","events[7]"):("keep","1901-1902",None),
("kgp_col1908-p646b12","events[8]"):("keep","Nov., 1902",None),
("kgp_col1908-p646b12","events[10]"):("keep","ord., 1902",None),
("kgp_col1908-p646b12","events[11]"):("keep","Asiatics, 1903",None),
("kgp_col1949-p479b2","events[2].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1948-p487b11","events[1].place"):("keep","Pal. civ. admin.",None),
("kgp_col1948-p529b13","events[3].place"):("keep","P.W.D.",None),
("kgp_col1948-p532b9","events[0].year_end"):("drop","",None),
("kgp_col1948-p532b9","events[1].year_end"):("drop","",None),
("kgp_col1948-p532b9","events[2].year_end"):("drop","",None),
("kgp_col1886-p443b4","events[4].year_end"):("keep","1 Dec., 1871",None),
("kgp_col1883-p407b14","events[1]"):("keep","June, 1881",None),
("kgp_col1886-p429b5","events[1]"):("keep","1st Mar., 1872",None),
("kgp_col1886-p429b5","events[2]"):("keep","Mar., 1873",None),
("kgp_col1886-p429b5","events[3]"):("keep","4th Aug., 1873",None),
("kgp_col1886-p429b5","events[4]"):("keep","19th Nov., 1873",None),
("kgp_col1886-p429b5","events[5]"):("keep","1st Jan., 1874",None),
("kgp_col1886-p429b5","events[6]"):("keep","Oct., 1875",None),
("kgp_col1886-p429b5","events[7]"):("keep","18th Oct., 1879",None),
("kgp_col1886-p429b5","events[8]"):("keep","1st Jan., 1880",None),
("kgp_col1886-p429b5","events[9]"):("keep","1st April, 1880",None),
("kgp_col1886-p429b5","events[10]"):("keep","29th May, 1880",None),
("kgp_col1886-p429b5","events[11]"):("keep","17th Aug., 1880",None),
("kgp_col1886-p429b5","events[12]"):("keep","28th Jan., 1881",None),
("kgp_col1886-p429b5","events[13]"):("keep","3rd Feb., 1881",None),
("kgp_col1886-p429b5","events[14]"):("keep","17th Sept., 1881",None),
("kgp_col1886-p429b5","events[15]"):("keep","17th Sept., 1881",None),
("kgp_col1886-p429b5","events[16]"):("keep","Moka, 1882",None),
("kgp_col1886-p517b20","events[1]"):("keep","Jan., 1874",None),
("kgp_col1867-p208b10","events[0].year_end"):("drop","",None),
("kgp_col1867-p208b10","events[3].year_end"):("drop","",None),
("kgp_col1867-p227b21","events[2]"):("keep","4th Feb. 1842",None),
("kgp_col1867-p227b21","events[3]"):("keep","16th May, 1848",None),
("kgp_col1867-p227b21","events[4]"):("keep","2nd Nov. 1849",None),
("kgp_col1867-p227b21","events[5]"):("keep","army in 1851",None),
("kgp_col1867-p227b21","events[6]"):("keep","army in 1851",None),
("kgp_col1867-p227b21","events[7]"):("keep","August, 1854",None),
("kgp_col1867-p227b21","events[8]"):("keep","May, 1858",None),
("kgp_col1867-p227b21","events[9]"):("keep","Nov. 1860",None),
("kgp_col1867-p227b21","events[10]"):("keep","Oct. 1865",None),
("kgp_col1867-p247b17","events[2].year_end"):("drop","",None),
("kgp_col1867-p253b18","events[4]"):("drop","",None),
("kgp_col1867-p253b18","events[5]"):("drop","",None),
("kgp_col1867-p256b9","events[1]"):("keep","Nov. 19, 1860",None),
("kgp_col1913-p801b4","events[1]"):("keep","May, 1905",None),
("kgp_col1913-p801b4","events[2]"):("keep","1st July, 1906",None),
("kgp_col1913-p801b4","events[3]"):("keep","supt. of pol., 1910",None),
("kgp_col1899-p556b3","events[2].place"):("keep","Dub. dist.",None),
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
            "confidence":0.9,"rationale":"main-loop review"})
extra=[k for k in D if k not in allkeys]
print("packets:",npk,"decided:",len(rows),"missing:",len(missing),"badev:",len(badev),"extra:",len(extra))
for m in missing[:50]:print("  MISSING",m)
for b in badev[:50]:print("  BADEV",b)
for e in extra[:50]:print("  EXTRA",e)
if not missing and not badev and not extra:
    open(OUT,"w").write("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
    from collections import Counter; c=Counter(r["verdict"] for r in rows)
    print("WROTE",OUT,len(rows),"| keep=%d correct=%d drop=%d"%(c['keep'],c['correct'],c['drop']))
else: print("NOT WRITTEN")
