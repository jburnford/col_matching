import json, re
def nws(s): return re.sub(r"\s+"," ",(s or "")).strip().lower()
BATCH="data/kg/review/residue/batch_007.jsonl"; OUT="data/kg/review/verdicts/verdicts_res_007.jsonl"
D={
("kgp_col1940-p947b14","events[11].place"):("keep","cust.",None),
("kgp_col1948-p484b11","events[1].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1948-p484b11","events[2].place"):("correct","G. and E. Is. Col.","Gilbert and Ellice Islands Colony"),
("kgp_col1954-p309b16","events[1].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1957-p392b5","events[0].year_end"):("drop","",None),
("kgp_col1948-p513b10","events[0].year_end"):("drop","",None),
("kgp_col1940-p1063b10","events[3].place"):("drop","",None),
("kgp_col1940-p1063b10","events[4].place"):("drop","",None),
("kgp_col1940-p1063b10","events[5].place"):("drop","",None),
("kgp_col1948-p556b9","events[4].place"):("keep","dept. of agric.",None),
("kgp_col1905-p607b13","events[0].year_end"):("drop","",None),
("kgp_col1905-p607b13","events[1].year_end"):("drop","",None),
("kgp_col1905-p607b13","events[2].year_end"):("drop","",None),
("kgp_col1905-p607b13","events[3].year_end"):("drop","",None),
("kgp_col1905-p607b13","events[4].year_end"):("drop","",None),
("kgp_col1905-p607b13","events[5].year_end"):("drop","",None),
("kgp_col1905-p607b13","events[6].year_end"):("drop","",None),
("kgp_col1905-p607b13","events[7].year_end"):("drop","",None),
("kgp_col1924-p786b20","events[2].place"):("keep",'dist. "A.,"',None),
("kgp_col1924-p786b20","events[3].place"):("keep",'dist. "A.,"',None),
("kgp_col1924-p786b20","events[4].place"):("keep",'dist. "F.,"',None),
("kgp_col1924-p786b20","events[5].place"):("keep",'dist. "F.,"',None),
("kgp_col1924-p786b20","events[6].place"):("keep",'dist. "B.,"',None),
("kgp_col1924-p786b20","events[7].place"):("keep",'dist. "B.,"',None),
("kgp_col1907-p620b10","events[0].place"):("keep","E. and A. dept.",None),
("kgp_col1922-p768b9","events[0].place"):("keep","sup. ct.",None),
("kgp_col1940-p905b7","events[0].place"):("keep","Bri. tel. serv.",None),
("kgp_col1923-p787b15","events[3].place"):("keep","Matabele War",None),
("kgp_col1923-p787b15","events[4].place"):("keep","Matabele Rebellion",None),
("kgp_col1951-p519b5","events[0].place"):("keep","G.P.O.",None),
("kgp_col1951-p519b5","events[1].place"):("keep","G.P.O.",None),
("kgp_col1951-p519b5","events[2].place"):("keep","G.P.O.",None),
("kgp_col1951-p519b5","events[3].place"):("keep","G.P.O.",None),
("kgp_col1951-p519b5","events[4].place"):("keep","G.P.O.",None),
("kgp_col1951-p519b5","events[5].place"):("keep","G.P.O.",None),
("kgp_col1919-p753b12","events[1]"):("keep","1904-5",None),
("kgp_col1919-p753b12","events[2]"):("keep","1906-7",None),
("kgp_col1919-p753b12","events[4]"):("keep","London, 1916",None),
("kgp_col1909-p704b20","events[0].year_end"):("drop","",None),
("kgp_col1918-p729b18","events[0].place"):("keep","Wye coll.",None),
("kgp_col1909-p704b16","events[2].place"):("keep","dist. F.",None),
("kgp_col1923-p802b6","events[0].place"):("keep","Wye Coll.",None),
("kgp_col1918-p730b5","events[2].place"):("keep","dist. F.",None),
("kgp_col1909-p707b4","events[2]"):("keep","1903-04",None),
("kgp_col1909-p707b4","events[3]"):("keep","28th Sept., 1906",None),
("kgp_col1914-p706b3","events[2]"):("keep","17th Aug., 1911",None),
("kgp_col1914-p706b3","events[3]"):("keep","1st Apr., 1913",None),
("kgp_col1940-p930b14","events[1].place"):("keep",'dist. "A"',None),
("kgp_col1957-p343b6","events[1].year_end"):("drop","",None),
("kgp_col1909-p718b7","events[2]"):("keep","1896-7",None),
("kgp_col1909-p718b7","events[3]"):("keep","1902 to 1907",None),
("kgp_col1909-p718b7","events[4]"):("keep","22nd Mar., 1907",None),
("kgp_col1921-p832b17","events[8].place"):("keep",'dist. "D."',None),
("kgp_col1909-p729b5","events[0].place"):("correct","G. C. Col.","Gold Coast Colony"),
("kgp_col1909-p729b5","events[1].place"):("correct","G. C. Col.","Gold Coast Colony"),
("kgp_col1922-p817b8","events[0].place"):("correct","G. C. Col.","Gold Coast Colony"),
("kgp_col1922-p817b8","events[1].place"):("correct","G. C. Col.","Gold Coast Colony"),
("kgp_col1939-p1011b7","events[20].place"):("keep","educn. dept.",None),
("kgp_col1965-p268b6","events[4].place"):("keep","fed. govt.",None),
("kgp_col1927-p943b10","events[2].place"):("keep","law schl.",None),
("kgp_col1925-p900b2","events[5].place"):("keep","dist. II.",None),
("kgp_col1957-p370b11","events[1].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1918-p777b3","events[1]"):("keep","1900-1901",None),
("kgp_col1918-p777b3","events[2]"):("keep","Sept., 1905",None),
("kgp_col1911-p716b17","events[3].place"):("keep","Canadian H. of C.",None),
("kgp_col1917-p798b18","events[2]"):("keep","Cornwall, 1894",None),
("kgp_col1917-p798b18","events[3]"):("keep","Niger Coast Prot., 1896",None),
("kgp_col1917-p798b18","events[4]"):("keep","15th May, 1898",None),
("kgp_col1917-p798b18","events[5]"):("keep","5th July, 1900",None),
("kgp_col1917-p798b18","events[6]"):("keep","July, 1902",None),
("kgp_col1917-p798b18","events[7]"):("keep","1902-4",None),
("kgp_col1917-p798b18","events[8]"):("keep","Oct., 1904",None),
("kgp_col1921-p872b14","events[0].year_end"):("drop","",None),
("kgp_col1951-p597b9","events[0].place"):("drop","",None),
("kgp_col1912-p736b22","events[2]"):("keep","1st Apr., 03",None),
("kgp_col1951-p615b11","events[0].place"):("keep","J'ca.",None),
("kgp_col1951-p615b11","events[1].place"):("keep","J'ca.",None),
("kgp_col1951-p615b11","events[2].place"):("keep","J'ca.",None),
("kgp_col1951-p615b11","events[3].place"):("keep","J'ca.",None),
("kgp_col1951-p615b11","events[4].place"):("keep","J'ca.",None),
("kgp_col1951-p615b11","events[5].place"):("keep","J'ca.",None),
("kgp_col1922-p880b4","events[1]"):("keep","1900-1902",None),
("kgp_col1922-p880b4","events[3]"):("keep","S. Nigeria, 1905",None),
("kgp_col1922-p880b4","events[4]"):("keep","S. Nigeria, 1907",None),
("kgp_col1922-p880b4","events[5]"):("keep","Gold Coast, 1914",None),
("kgp_col1922-p880b4","events[6]"):("keep","Togoland Field Force, 1914",None),
("kgp_col1925-p957b4","events[10].year_end"):("keep","Sept., 23",None),
("kgp_col1925-p957b4","terminal.year"):("keep","Sept., 23",None),
("kgp_col1912-p761b24","events[2]"):("keep","10th May, 1904",None),
("kgp_col1912-p761b24","events[3]"):("keep","supt. of pol., 1910",None),
("kgp_col1922-p900b17","events[1]"):("keep","12th Jan., 1906",None),
("kgp_col1878-p433b20","events[1]"):("keep","6th June, 1854",None),
("kgp_col1878-p433b20","events[2]"):("keep","Christmas Day, 1854",None),
("kgp_col1878-p433b20","events[3]"):("keep","China war, 1860",None),
("kgp_col1912-p779b6","events[1].place"):("keep","educn. dept.",None),
("kgp_col1965-p345b7","events[0].place"):("keep","Tang.",None),
("kgp_col1965-p345b7","events[1].place"):("keep","E.A.C.S.O.",None),
("kgp_col1965-p345b7","events[2].place"):("keep","E.A.C.S.O.",None),
("kgp_col1965-p345b7","events[3].place"):("keep","H.K.",None),
("kgp_col1925-p1006b16","events[1]"):("keep","E. Prot., May, 1905",None),
("kgp_col1925-p1006b16","events[2]"):("keep","July, 1906",None),
("kgp_col1925-p1006b16","events[3]"):("keep","supt. of pol., 1910",None),
("kgp_col1925-p1006b16","events[4]"):("keep","Kenya, Apr., 1920",None),
("kgp_col1925-p1006b16","events[5]"):("keep","Nov., 1921",None),
("kgp_col1966-p198b9","events[1].place"):("keep","Nig. Prot.",None),
("kgp_col1966-p198b9","events[2].place"):("keep","Nig. Prot.",None),
("kgp_col1937-p847b15","events[1].year_end"):("drop","",None),
("kgp_col1937-p847b15","events[2]"):("drop","",None),
("kgp_col1937-p847b15","events[3].year_end"):("drop","",None),
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
