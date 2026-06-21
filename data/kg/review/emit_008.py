import json, re
def nws(s): return re.sub(r"\s+"," ",(s or "")).strip().lower()
BATCH="data/kg/review/residue/batch_008.jsonl"; OUT="data/kg/review/verdicts/verdicts_res_008.jsonl"
GEC="Gilbert and Ellice Islands Colony"
D={
("kgp_col1948-p409b20","events[12].place"):("keep","Cyp. dist.",None),
("kgp_col1939-p928b14","events[9].place"):("keep","S. dist.",None),
("kgp_col1939-p929b2","events[10].place"):("keep","N. dist.",None),
("kgp_col1940-p877b3","events[0].year_end"):("drop","",None),
("kgp_col1940-p877b3","events[1].year_end"):("drop","",None),
("kgp_col1940-p877b3","events[2].year_end"):("drop","",None),
("kgp_col1940-p877b3","events[7].year_end"):("drop","",None),
("kgp_col1948-p417b21","events[0].year_end"):("drop","",None),
("kgp_col1940-p881b14","events[4].place"):("keep","Imp. Coll. of Sci.",None),
("kgp_col1940-p884b6","events[2].place"):("keep","legis. coun.",None),
("kgp_col1940-p884b6","events[3].place"):("keep","legis. coun.",None),
("kgp_col1940-p884b6","events[4].place"):("keep","legis. coun.",None),
("kgp_col1940-p884b6","events[5].place"):("keep","legis. coun.",None),
("kgp_col1940-p884b6","events[6].place"):("keep","legis. coun.",None),
("kgp_col1951-p494b14","events[1].place"):("keep","sup. ct.",None),
("kgp_col1951-p494b14","events[2].place"):("keep","sup. ct.",None),
("kgp_col1951-p494b14","events[3].place"):("keep","sup. ct.",None),
("kgp_col1951-p494b14","events[4].place"):("keep","sup. ct.",None),
("kgp_col1939-p945b11","events[2].place"):("keep","legis. coun.",None),
("kgp_col1939-p945b11","events[3].place"):("keep","legis. coun.",None),
("kgp_col1939-p945b11","events[4].place"):("keep","legis. coun.",None),
("kgp_col1939-p945b11","events[5].place"):("keep","legis. coun.",None),
("kgp_col1939-p945b11","events[6].place"):("keep","legis. coun.",None),
("kgp_col1957-p310b18","events[1].place"):("keep","J'ca",None),
("kgp_col1957-p310b18","events[2].place"):("keep","J'ca",None),
("kgp_col1957-p310b18","events[3].place"):("keep","J'ca",None),
("kgp_col1957-p310b18","events[4].place"):("keep","J'ca",None),
("kgp_col1957-p310b18","events[5].place"):("keep","J'ca",None),
("kgp_col1957-p310b18","events[6].place"):("keep","J'ca",None),
("kgp_col1940-p897b24","events[0].year_end"):("drop","",None),
("kgp_col1937-p878b6","events[2].place"):("keep",'dist. "A,"',None),
("kgp_col1940-p901b16","events[4].place"):("keep","exec. coun.",None),
("kgp_col1937-p879b16","events[3].place"):("keep","exec. coun.",None),
("kgp_col1939-p967b7","events[0].place"):("keep",'dist. "F"',None),
("kgp_col1939-p967b7","events[5].place"):("keep",'dist. "E"',None),
("kgp_col1913-p665b5","events[1]"):("keep","9th Aug., 1897",None),
("kgp_col1939-p970b8","events[2].place"):("keep","cust. dept.",None),
("kgp_col1951-p532b17","events[4].place"):("keep","2nd dist.",None),
("kgp_col1949-p459b15","events[2].place"):("correct","G. & E. Is. Col.",GEC),
("kgp_col1940-p926b22","events[2].place"):("keep","S. dist.",None),
("kgp_col1966-p235b18","events[2].place"):("correct","G. & E.Is. Col.",GEC),
("kgp_col1951-p537b6","events[0].year_end"):("drop","",None),
("kgp_col1951-p537b6","events[1].year_end"):("drop","",None),
("kgp_col1951-p537b6","events[2].year_end"):("drop","",None),
("kgp_col1951-p537b6","events[3].year_end"):("drop","",None),
("kgp_col1951-p537b6","events[4].year_end"):("drop","",None),
("kgp_col1951-p537b6","events[5].year_end"):("drop","",None),
("kgp_col1951-p537b6","events[6].year_end"):("drop","",None),
("kgp_col1939-p985b23","events[5].year_end"):("drop","",None),
("kgp_col1958-p330b17","events[2].place"):("keep","dist. A",None),
("kgp_col1953-p272b11","events[2].place"):("drop","",None),
("kgp_col1936-p897b16","events[2].place"):("keep","P.W.D.",None),
("kgp_col1939-p999b8","events[2].place"):("keep","P.W.D.",None),
("kgp_col1940-p940b11","events[7].place"):("keep","N. dist.",None),
("kgp_col1939-p1004b3","events[1].place"):("keep","Coll. of Med.",None),
("kgp_col1939-p1004b3","events[2].place"):("keep","Coll. of Med.",None),
("kgp_col1940-p951b18","events[7].place"):("keep","dist. F.",None),
("kgp_col1940-p958b11","events[5].place"):("keep","cust.",None),
("kgp_col1940-p958b11","events[6].place"):("keep","cust.",None),
("kgp_col1963-p342b18","events[0].place"):("keep","J'ca constab.",None),
("kgp_col1940-p962b18","events[6].place"):("keep","W. dist.",None),
("kgp_dol1935-p917b16","events[3].place"):("keep","Br. Sol. Is. Prot.",None),
("kgp_col1958-p360b22","events[0].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1958-p360b22","events[1].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1958-p360b22","events[2].place"):("keep","B. Sol. Is. Prot.",None),
("kgp_col1880-p388b14","events[9].year_end"):("drop","",None),
("kgp_col1955-p322b25","events[7]"):("drop","",None),
("kgp_col1950-p548b5","events[0].place"):("drop","",None),
("kgp_col1960-p400b21","events[0].place"):("keep","Pal. rlys.",None),
("kgp_col1940-p993b6","events[3].place"):("drop","",None),
("kgp_col1940-p993b6","events[4].place"):("drop","",None),
("kgp_col1940-p1000b12","events[7].place"):("keep","Prot.",None),
("kgp_col1940-p1000b12","events[8].place"):("keep","Prot.",None),
("kgp_col1950-p567b7","events[0].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1950-p567b7","events[3].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1950-p567b7","events[5].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1950-p567b7","events[6].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1950-p567b7","events[8].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1950-p567b7","events[13].place"):("correct","G. and E. Is. Col.",GEC),
("kgp_col1950-p567b7","events[14].place"):("keep","S. Pac. comsn.",None),
("kgp_col1867-p249b17","events[1]"):("keep","Feb. 1865",None),
("kgp_col1954-p323b10","events[1].place"):("drop","",None),
("kgp_col1951-p616b16","events[0].place"):("keep","J'ca. constab.",None),
("kgp_col1951-p616b16","events[1].place"):("keep","J'ca. constab.",None),
("kgp_col1951-p616b16","events[2].place"):("keep","J'ca. constab.",None),
("kgp_col1951-p616b16","events[3].place"):("keep","J'ca. constab.",None),
("kgp_col1939-p1067b14","events[2].place"):("drop","",None),
("kgp_col1937-p988b12","events[1].place"):("keep",'dist. "D,"',None),
("kgp_col1937-p988b12","events[3].place"):("keep",'dist. "E,"',None),
("kgp_dol1935-p967b15","events[0].place"):("keep","Can. Pac. Rly.",None),
("kgp_col1958-p406b6","events[1].place"):("keep","G.P.O.",None),
("kgp_col1958-p406b6","events[2].place"):("keep","G.P.O.",None),
("kgp_col1940-p1024b8","events[0].place"):("keep","Emm. Coll.",None),
("kgp_col1867-p255b23","events[4]"):("drop","",None),
("kgp_col1937-p1002b10","events[7]"):("drop","",None),
("kgp_col1931-p1120b12","events[1].place"):("keep",'dist. "E."',None),
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
