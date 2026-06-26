import json, re
QMAP={}
def add(insts,qid,label,source):
    for i in insts: QMAP[i]=(qid,label,source)

def rule(inst):
    n=' '+inst+' '
    has=lambda *ws: any((' '+w+' ') in n for w in ws)
    if 'clerk of works' in inst: return None
    if 'lieut governor' in inst or 'lieutenant governor' in inst or 'lt governor' in inst or 'lieut gov' in inst: return None
    if 'brigade major' in inst or 'brigade maj' in inst or 'brig major' in inst or 'brig maj' in inst: return ('Q4967158','brigade major')
    if 'commander in chief' in inst or 'comdr in chief' in inst or 'commander of the forces' in inst or 'commander of the troops' in inst or inst.startswith('commanded'): return None
    # private secretary (before generic secretary/anything)
    if 'private secretary' in inst or 'priv secretary' in inst or 'pvte secretary' in inst or 'priv sec' in inst \
       or inst.startswith('ps to') or inst.startswith('ps ') or inst in ('ps',) or 'ps governor' in inst or 'ps apptmts' in inst:
        return ('Q131408743','private secretary')
    if 'aide de camp' in inst or inst.startswith('adc') or ' adc ' in n: return ('Q369894','aide-de-camp')
    if 'vice consul' in inst or 'vice cons' in inst: return ('Q56292679','vice consul')
    if 'dent surg' in inst or 'dental' in inst: return ('Q27349','dentist')
    if 'solicitor general' in inst: return ('Q7557772','solicitor general')
    if 'attorney general' in inst: return ('Q1501926','attorney general')
    if 'surveyor general' in inst: return ('Q7647118','surveyor general')
    if 'auditor general' in inst or ('comptroller' in inst and 'auditor' in inst) or ('cont' in inst and 'auditor' in inst): return ('Q5785176','auditor general')
    if 'accountant general' in inst: return ('Q4672765','accountant general')
    if 'chief accountant' in inst: return ('Q12096582','chief accountant')
    # members / legislators / MPs
    if inst.startswith('member') or inst.startswith('mp ') or inst=='mp' or 'unofficial member' in inst or 'official member' in inst or 'ex officio member' in inst or inst.startswith('elected member') or 'legislative councillor' in inst:
        if 'parliament' in inst or 'parlt' in inst or 'parlmt' in inst or 'house of commons' in inst or 'h of c' in inst or 'house of reps' in inst or 'house of representatives' in inst or 'h of r' in inst or inst.startswith('mp'):
            return ('Q16707842','Member of Parliament')
        if 'legislative' in inst or 'legislature' in inst or 'assembly' in inst or 'assem' in inst or 'council of government' in inst or 'executive council' in inst or 'house of assembly' in inst or 'legisassem' in inst or 'legislative councillor' in inst:
            return ('Q4175034','legislator')
        return None
    if 'municipal councillor' in inst or 'town councillor' in inst or 'city councillor' in inst or 'borough councillor' in inst: return ('Q708492','council member')
    if has('school','schls','schools','schl') and (has('inspector','insptr','inspg') or 'inspect' in inst): return ('Q1958649','school inspector')
    if 'inspector general' in inst or 'inspector gen' in inst: return None
    if has('clerk','clerks'): return ('Q738142','clerk')
    if has('magistrate','magistracy','magistrates'): return ('Q4594605','magistrate')
    if has('registrar','registar','regisr','regiar','registrars'): return ('Q6104047','registrar')
    if 'chief justice' in inst: return ('Q3188089','chief justice')
    if has('judge'): return ('Q16533','judge')
    if 'quantity surveyor' in inst or 'qty surveyor' in inst: return ('Q2067634','quantity surveyor')
    if has('surveyor'): return ('Q294126','surveyor')
    if (has('vet','vety') and has('surg','surgeon')) or 'veterinary' in inst: return ('Q202883','veterinarian')
    if 'mechanical engineer' in inst or 'mech engineer' in inst: return ('Q1906857','mechanical engineer')
    if 'electrical engineer' in inst or 'elec engineer' in inst or 'elect engineer' in inst: return ('Q1326886','electrical engineer')
    if 'marine engineer' in inst: return ('Q1644847','marine engineer')
    if 'civil engineer' in inst: return ('Q13582652','civil engineer')
    if has('engineer','engngr','engrr','engrn','engnr','engur'): return ('Q81096','engineer')
    if has('inspector','insptr'): return ('Q27214348','inspector')
    if has('auditor','audtr'): return ('Q10949665','auditor')
    if has('accountant','acctg','accts','acctng'): return ('Q3929433','accountant')
    if 'customs' in inst: return ('Q247797','customs officer')
    if 'prime minister' in inst: return None
    if has('minister'): return ('Q83307','minister')
    if inst.startswith('governor of') or inst.startswith('governor general') or inst.startswith('governor and') or inst.startswith('governor in chief'): return ('Q132050','governor')
    if has('director'): return ('Q1162163','director')
    if has('surgeon','surg'): return ('Q774306','surgeon')
    if 'medical officer' in inst or has('moh','dmo','mo','gmo') or 'physician' in inst: return ('Q39631','physician')
    if has('speaker'): return ('Q1758037','speaker')
    if has('teacher') or 'headmast' in inst or 'schoolmaster' in inst or has('instructor') or has('instr'): return ('Q37226','teacher')
    if 'professor' in inst or inst.startswith('prof ') or ' prof of ' in n: return ('Q121594','professor')
    if has('lecturer'): return ('Q1569495','lecturer')
    if has('comptroller','controller','compt','contlr','contrl','cont') or ' contr ' in n: return ('Q673633','comptroller')
    if has('treasurer'): return ('Q388338','treasurer')
    if 'immigration' in inst or 'imigr' in inst or 'immigr' in inst or 'emigration' in inst or 'immigt' in inst: return ('Q6005116','immigration officer')
    if 'paymaster' in inst or 'paymr' in inst: return ('Q7156771','paymaster')
    if 'postmaster' in inst or 'postmstr' in inst or 'postmsr' in inst or inst.startswith('pmg'): return ('Q1416611','postmaster')
    if 'harbour' in inst and ('master' in inst or ' mr ' in n or 'mast' in inst): return ('Q1489454','harbourmaster')
    if 'consul' in inst: return ('Q207978','consul')
    if has('chairman','chairperson','chairwoman'): return ('Q140686','chairperson')
    if has('bishop'): return ('Q29182','bishop')
    if 'missionary' in inst: return ('Q219477','missionary')
    if has('botanist'): return ('Q2374149','botanist')
    if has('chaplain'): return ('Q208762','chaplain')
    if has('librarian','librn'): return ('Q182436','librarian')
    if has('curator'): return ('Q674426','curator')
    if has('architect'): return ('Q42973','architect')
    if has('pharmacist'): return ('Q105186','pharmacist')
    if 'nursing sister' in inst or has('nurse'): return ('Q186360','nurse')
    if has('matron'): return ('Q1396008','matron')
    if has('cashier'): return ('Q1735282','cashier')
    if has('coroner'): return ('Q1134614','coroner')
    if has('economist'): return ('Q188094','economist')
    if has('horticulturist'): return ('Q3140857','horticulturist')
    if has('actuary'): return ('Q179985','actuary')
    if 'anaesthetist' in inst or 'anesthet' in inst: return ('Q28837','anesthesiologist')
    if 'solicitor' in inst: return ('Q14284','solicitor')
    if 'barrister' in inst: return ('Q808967','barrister')
    if has('advocate','advoc'): return ('Q380075','advocate')
    if has('telegraphist','telist'): return ('Q2024200','telegraphist')
    if has('draughtsman','draftsman','dftsman','dtfsmn','dftsmn','dftsmn'): return ('Q683754','drafter')
    # ranks (after offices so 'lieut governor'->governor etc.)
    if 'lieut commdr' in inst or 'lieut comdr' in inst or 'lt commdr' in inst or 'lieutenant commander' in inst: return ('Q837582','lieutenant commander')
    if 'sgt maj' in inst or 'sergt maj' in inst or 'sergeant major' in inst or 'serjeant major' in inst: return ('Q157696','sergeant')
    if 'lieutenant colonel' in inst or 'lieut colonel' in inst or 'lt colonel' in inst: return ('Q493898','lieutenant colonel')
    if 'lieutenant general' in inst or 'lieut general' in inst or 'lt general' in inst: return ('Q152951','lieutenant general')
    if 'major general' in inst or 'maj general' in inst: return ('Q157148','major general')
    if has('brigadier') or 'brigadier general' in inst: return ('Q23016362','brigadier-general')
    if has('lieutenant','lieut','lt'): return ('Q186024','lieutenant')
    if has('captain','capt'): return ('Q19100','captain')
    if has('major','maj'): return ('Q983927','major')
    if has('colonel'): return ('Q104680','colonel')
    if has('sergeant','sergt','sgt'): return ('Q157696','sergeant')
    if has('corporal','corp'): return ('Q17378201','corporal')
    if has('midshipman'): return ('Q11141137','midshipman')
    if has('commander','comdr'): return ('Q6620231','commander')
    return None

AMBIG_RE = re.compile(r'^(served|serving|entered|entd|ent |attached|attchd|attd|transferred|trans |returned|return to|came|called|elected|el to|re el|re elect|resigned|resig|retired|ret |ret on|emigrated|promoted|redesig|officiated|acted|administered|admstd|admstrd|admtd|adminst|on the staff|on staff|on nav|on sp|on spec|on special|on active|commanded|repd|del to|deleg|accredited|in practice|priv prac|pvte prac|confirmed in|relieved|seconded|secon |appointed|joined|took|sent|conducted|employed|defeated|nom |demob|wounded|unsuccessful|represented|re aptd|retired)')
AMBIG=set([
 'wams','natal mounted police','cape mounted rifles','regular army','reg army r of o','hm forces','natal rebellion',
 're signals','milly service','mily service re sr','sp service','sp military duty','polit service','political service',
 'diplomatic service','sudan polit service','indian polit service','local government','local government service',
 'natal civil service','sudan government','tanzania government service','colonial legislative service','customs service',
 'general cler service','general department','forest department','loco department','police department','judicial department',
 'land office','immigration department','agr department','board of trade','board of health','board of agriculture',
 'legislative council','executive council','command','aden','som','twi','ken','cons','econ','statn','suptd','speclst',
 'probtnr','admsnr','commsr','collectr','st l','hco','afo','gmo','smoh','oeta','w regn','snc','pas','first appointment',
 'sokoto expedn','field cornet','municipal councillor','civil servant','command','hm forces','spec gr','higher grade','higher gr',
])

def slug(s): return 'colkg:'+re.sub(r'[^a-z0-9]+','_',s.strip().lower()).strip('_')

from col_match.kg.paths import kg_out
_ROOT=kg_out()
cache=set(json.loads(l)['institution'] for l in open(_ROOT/'role_grounding.jsonl'))
rows=[]
for l in open(_ROOT/'position_worklist.jsonl'):
    r=json.loads(l); inst=r['institution']
    if inst.startswith('_') or inst in cache: continue
    if r['count']>=1: rows.append(r)
print('uncached count>=2 rows:',len(rows))

out=[]; counts={'mcp':0,'reuse':0,'internal':0,'ambiguous':0}
for r in rows:
    inst=r['institution']; typ=r['type']
    if inst in AMBIG or AMBIG_RE.match(inst):
        qid=None;label=inst;src='ambiguous';mt='ambiguous_non_role'
    else:
        rr=rule(inst)
        if rr: qid,label=rr;src='reuse';mt='reuse_variant'
        else: qid=slug(inst);label=inst;src='internal';mt='internal_mint'
    out.append({'institution':inst,'type':typ,'id':qid,'label':label,'instance_of':[],
                'country_qid':None,'source':src,'match_type':mt})
    counts[src]+=1

_OUTP=str(_ROOT/'role_folds_rules.jsonl')
with open(_OUTP,'w') as f:
    for o in out: f.write(json.dumps(o)+'\n')
print('counts:',counts)
from collections import Counter
c=Counter((o['id'],o['label']) for o in out if o['source']=='reuse')
print('=== REUSE by QID (top 30) ==='); [print(f'  {q:11} {l:22} x{n}') for (q,l),n in c.most_common(30)]
