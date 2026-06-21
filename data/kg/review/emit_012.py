import json, re
def nws(s): return re.sub(r"\s+"," ",(s or "")).strip().lower()
BATCH="data/kg/review/residue/batch_012.jsonl"; OUT="data/kg/review/verdicts/verdicts_res_012.jsonl"
GEC="Gilbert and Ellice Islands Colony"
D={
("kgp_col1951-p525b19","events[2].place"):("keep","dist. admin.",None),
("kgp_col1949-p453b10","events[1].place"):("keep","Br. Sol. Is. Prot.",None),
("kgp_col1949-p453b10","events[4].place"):("keep","G. & E. Is. Prot.",None),
("kgp_col1951-p527b24","events[0].year_end"):("drop","",None),
("kgp_col1951-p527b24","events[1].year_end"):("drop","",None),
("kgp_col1951-p527b24","events[2].year_end"):("drop","",None),
("kgp_col1950-p496b7","events[2].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1949-p458b9","events[0].place"):("drop","",None),
("kgp_col1951-p542b11","events[1].place"):("correct","G. and E.I. Col.",GEC),
("kgp_col1867-p230b4","events[5].year_end"):("drop","",None),
("kgp_col1867-p230b4","events[6]"):("drop","",None),
("kgp_col1951-p552b20","events[6].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1867-p235b18","events[0].year_end"):("drop","",None),
("kgp_col1951-p563b19","events[0].year_end"):("drop","",None),
("kgp_col1950-p528b6","events[2].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1948-p487b2","events[0].year_end"):("drop","",None),
("kgp_col1950-p550b15","events[0].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1950-p557b16","events[1].place"):("keep","P.W.D.",None),
("kgp_col1951-p598b5","events[0].place"):("keep","J'ca.",None),
("kgp_col1951-p598b5","events[1].place"):("keep","J'ca.",None),
("kgp_col1951-p598b5","events[2].place"):("keep","J'ca.",None),
("kgp_col1951-p598b5","events[3].place"):("keep","J'ca.",None),
("kgp_col1951-p598b5","events[4].place"):("keep","J'ca.",None),
("kgp_col1951-p598b5","events[5].place"):("keep","J'ca.",None),
("kgp_col1951-p598b5","events[6].place"):("keep","J'ca.",None),
("kgp_col1951-p603b5","events[0].year_end"):("drop","",None),
("kgp_col1951-p603b5","events[1].year_end"):("drop","",None),
("kgp_col1959-p428b5","events[0].year_end"):("drop","",None),
("kgp_col1959-p428b5","events[1].year_end"):("drop","",None),
("kgp_col1959-p428b5","events[2].year_end"):("drop","",None),
("kgp_col1951-p623b10","events[0].place"):("keep","J'ca.",None),
("kgp_col1951-p623b10","events[1].place"):("keep","J'ca.",None),
("kgp_col1951-p623b10","events[2].place"):("keep","J'ca.",None),
("kgp_col1951-p623b10","events[3].place"):("keep","J'ca.",None),
("kgp_col1951-p623b10","events[4].place"):("keep","J'ca.",None),
("kgp_col1951-p623b10","events[5].place"):("keep","J'ca.",None),
("kgp_col1951-p623b10","events[6].place"):("keep","J'ca.",None),
("kgp_col1956-p375b12","events[8].place"):("keep","S. Pac. comsn.",None),
("kgp_col1948-p520b10","events[0].year_end"):("drop","",None),
("kgp_col1948-p520b10","events[1].year_end"):("drop","",None),
("kgp_col1951-p647b11","events[0].year_end"):("drop","",None),
("kgp_col1951-p654b11","events[0].place"):("keep","J'ca.",None),
("kgp_col1951-p654b11","events[1].place"):("keep","J'ca.",None),
("kgp_col1951-p654b11","events[2].place"):("keep","J'ca.",None),
("kgp_col1951-p654b11","events[3].place"):("keep","J'ca.",None),
("kgp_col1951-p654b11","events[4].place"):("keep","J'ca.",None),
("kgp_col1951-p654b11","events[5].place"):("keep","J'ca.",None),
("kgp_col1951-p654b10","events[0].place"):("keep","J'ca.",None),
("kgp_col1951-p654b10","events[1].place"):("keep","J'ca.",None),
("kgp_col1951-p654b10","events[2].place"):("keep","J'ca.",None),
("kgp_col1951-p654b10","events[3].place"):("keep","J'ca.",None),
("kgp_col1951-p654b10","events[4].place"):("keep","J'ca.",None),
("kgp_col1951-p654b10","events[5].place"):("keep","J'ca.",None),
("kgp_col1951-p654b10","events[6].place"):("keep","J'ca.",None),
("kgp_col1951-p657b20","events[0].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1950-p613b4","events[4].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1950-p613b4","events[5].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1950-p613b4","events[6].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1950-p613b4","events[7].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1948-p546b17","events[0].place"):("drop","",None),
("kgp_col1948-p557b21","events[0].place"):("keep","Uga.",None),
("kgp_col1950-p634b13","events[2].place"):("drop","",None),
("kgp_col1950-p634b13","events[3].place"):("keep","E.A. vet. res. organ.",None),
("kgp_col1951-p689b5","events[5].place"):("keep","Univ. of Mal.",None),
("kgp_col1934-p840b3","events[0]"):("drop","",None),
("kgp_col1934-p836b6","events[1].year_end"):("drop","",None),
("kgp_col1934-p844b9","events[11].place"):("keep","N. dist.",None),
("kgp_col1934-p882b6","events[2]"):("keep","919 to Mar., 1920",None),
("kgp_col1934-p880b10","events[0]"):("keep","Lon- 895",None),
("kgp_col1934-p896b10","events[0]"):("drop","",None),
("kgp_col1934-p912b3","events[0].year_end"):("drop","",None),
("kgp_col1934-p910b7","honours[0].year"):("drop","",None),
("kgp_col1934-p914b5","events[0].year_end"):("keep","Apr. to 84",None),
("kgp_col1934-p914b5","events[7]"):("keep","G. Coast Col., 895",None),
("kgp_col1934-p914b5","events[8]"):("keep","895",None),
("kgp_col1934-p914b5","events[9]"):("keep","895",None),
("kgp_col1934-p908b10","events[15].year_end"):("keep","periods -33",None),
("kgp_col1934-p930b4","events[0]"):("keep","cadet, 906",None),
("kgp_col1934-p930b4","events[2]"):("drop","",None),
("kgp_col1934-p930b10","events[2]"):("drop","",None),
("kgp_col1934-p980b3","events[2]"):("keep","919, 1923",None),
("kgp_col1934-p980b7","events[4]"):("drop","",None),
("kgp_col1937-p880b3","events[2].place"):("drop","",None),
("kgp_col1934-p980b11","events[7]"):("keep","8th Dec., 17",None),
("kgp_col1937-p902b7","events[5]"):("keep","surveys 925",None),
("kgp_col1937-p942b3","events[0].place"):("keep","E. a Prot.",None),
("kgp_col1937-p910b3","events[5].year_end"):("keep","4-19",None),
("kgp_col1937-p902b8","events[11].year_end"):("keep","to Jan., 92",None),
("kgp_col1937-p902b8","events[12].year_end"):("keep","to Jan.. 92",None),
("kgp_col1937-p866b5","events[2].year_end"):("drop","",None),
("kgp_col1937-p962b5","events[2].place"):("keep","bd. of educn.",None),
("kgp_col1937-p996b6","events[2].year_end"):("keep","1926 and 27",None),
("kgp_col1937-p992b9","events[1]"):("keep","Canada, 1902",None),
("kgp_col1937-p992b9","events[2]"):("keep","Apr., 1911",None),
("kgp_col1937-p992b9","events[4]"):("drop","",None),
("kgp_col1937-p992b9","events[5]"):("drop","",None),
("kgp_col1937-p992b9","events[6]"):("keep","U.K., 1928",None),
("kgp_col1937-p992b9","events[7]"):("keep","Nov., 1931",None),
("kgp_col1937-p988b3","honours[0].year"):("drop","",None),
("kgp_col1937-p988b3","events[8]"):("keep","in 24-26",None),
("kgp_col1937-p988b3","events[9]"):("keep","in 24-26",None),
("kgp_col1937-p1028b4","events[4]"):("keep","July, 33",None),
("kgp_col1937-p1054b5","events[1]"):("drop","",None),
("kgp_col1937-p1028b3","events[8].year_end"):("keep","6-8",None),
("kgp_col1937-p1028b3","events[10]"):("keep","Rugby, 0-22",None),
("kgp_col1937-p1028b3","events[16].place"):("keep","comsnr. of wks.",None),
("kgp_col1937-p1054b8","birth_year"):("keep","B. 73",None),
("kgp_col1937-p1054b8","events[2]"):("keep","major 13",None),
("kgp_col1914-p661b4","events[6]"):("keep","Mar. 1903",None),
("kgp_col1914-p661b4","events[7]"):("keep","2nd Apr. to 17th June, 1907",None),
("kgp_col1914-p661b4","events[8]"):("keep","Sept., 1908",None),
("kgp_col1888-p444b15","events[1]"):("keep","22nd Nov., 1880",None),
("kgp_col1888-p444b15","events[2]"):("keep","June, 1884",None),
("kgp_col1888-p444b15","events[3]"):("keep","in 1886",None),
("kgp_col1877-p358b23","events[0].year_end"):("drop","",None),
("kgp_col1877-p358b23","events[1].year_end"):("drop","",None),
("kgp_col1877-p358b23","events[2]"):("drop","",None),
("kgp_col1877-p358b23","events[5].year_end"):("drop","",None),
("kgp_col1888-p477b10","events[1]"):("keep","Dec., 1879",None),
("kgp_col1877-p384b12","events[0].year_end"):("keep","1st of Feb., 1860",None),
}
rows=[]; missing=[]; badev=[]; npk=0; allkeys=set(); seen=set()
recs=[json.loads(l) for l in open(BATCH)]
for o in recs:
    for pk in o["packets"]: allkeys.add((o["person_id"],pk["field_path"]))
for o in recs:
    nsrc=nws(o["source_text"])
    for pk in o["packets"]:
        npk+=1; key=(o["person_id"],pk["field_path"])
        if key in seen: continue
        seen.add(key)
        if key not in D: missing.append(key); continue
        v,ev,corr=D[key]
        if v in ("keep","correct") and nws(ev) not in nsrc: badev.append((key,ev))
        rows.append({"person_id":o["person_id"],"field_path":pk["field_path"],"flagged_value":pk["flagged_value"],
            "reason":pk["reason"],"verdict":v,"corrected_value":corr,"source_evidence":ev,
            "confidence":0.9,"rationale":"main-loop review"})
extra=[k for k in D if k not in allkeys]
print("uniq:",len(seen),"raw:",npk,"decided:",len(rows),"missing:",len(missing),"badev:",len(badev),"extra:",len(extra))
for m in missing[:40]:print("  MISSING",m)
for b in badev[:40]:print("  BADEV",b)
for e in extra[:40]:print("  EXTRA",e)
if not missing and not badev and not extra:
    open(OUT,"w").write("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
    from collections import Counter; c=Counter(r["verdict"] for r in rows)
    print("WROTE",OUT,len(rows),"| keep=%d correct=%d drop=%d"%(c['keep'],c['correct'],c['drop']))
else: print("NOT WRITTEN")
