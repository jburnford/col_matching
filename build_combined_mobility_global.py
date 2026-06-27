#!/usr/bin/env python3
"""COMBINED global mobility video: BOTH corpora on one world stage, colour-coded.

Same look as the CO empire_mobility / IOL global videos (Leaflet/CARTO dark world
view, accumulating canvas web, gold clock), but overlays BOTH career-transfer
datasets at once:
  * Colonial Office List officials  -> BLUE arcs   (16,156 transfers)
  * India Office List officials      -> GOLD arcs   (9,037 transfers)
so the two imperial civil services can be contrasted in a single frame: the CO web
sprawls across Africa, the Caribbean, the Pacific and Canada; the IO web concentrates
into a dense knot over the subcontinent.  ~25,000 moves by ~12,000 officials, 1820-1966.

Frames captured by render_combined_mobility_global.py, encoded to MP4."""
import json

def mapped(transfers_path, coords_path, corpus):
    data = json.load(open(transfers_path))
    coords = json.load(open(coords_path))
    T = [t for t in data["transfers"] if t["from"] in coords and t["to"] in coords and t["from"] != t["to"]]
    return [[t["yr"], coords[t["from"]][0], coords[t["from"]][1],
             coords[t["to"]][0], coords[t["to"]][1], corpus] for t in T], len({t["pid"] for t in T})

co, co_n   = mapped("/tmp/transfers.json",     "/tmp/transfer_coords.json",     0)  # 0 = Colonial Office (blue)
iol, iol_n = mapped("/tmp/iol_transfers.json", "/tmp/iol_transfer_coords.json", 1)  # 1 = India Office (gold)
arcs = sorted(co + iol, key=lambda a: a[0])
y0, y1 = arcs[0][0], arcs[-1][0]
print(f"CO {len(co):,} arcs / {co_n:,} officials   IOL {len(iol):,} arcs / {iol_n:,} officials   total {len(arcs):,}  {y0}-{y1}")

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
 html,body{margin:0;height:100%%;background:#070d16;overflow:hidden;font-family:Georgia,serif}
 #map{height:100%%;background:#070d16}
 #cv{position:absolute;top:0;left:0;z-index:500;pointer-events:none}
 #hud{position:absolute;z-index:1000;top:24px;left:34px;color:#f3e7c9;text-shadow:0 2px 10px #000}
 #hud h1{margin:0;font-size:30px;color:#ffd98a;letter-spacing:.3px}
 #hud p{margin:6px 0 0;font-size:16px;color:#dfe7ef;font-family:system-ui,sans-serif;max-width:580px;line-height:1.35}
 #legend{margin-top:10px;font-family:system-ui,sans-serif;font-size:15px}
 #legend span{display:inline-block;margin-right:18px}
 #legend i{display:inline-block;width:13px;height:13px;border-radius:3px;margin-right:6px;vertical-align:-1px}
 #year{position:absolute;z-index:1000;bottom:26px;left:34px;color:#fff;font-family:system-ui,sans-serif;text-shadow:0 2px 8px #000}
 #year .y{font-size:62px;font-weight:800;color:#ffd98a;line-height:1}
 #year .c{font-size:16px;color:#cfdae6;margin-top:3px}
 #year .c b{font-weight:700}
 #credit{position:absolute;z-index:1000;bottom:14px;right:14px;color:#7e8ea0;font-size:12px;font-family:system-ui,sans-serif}
 .leaflet-control-attribution{display:none}
</style></head><body>
<div id="hud"><h1>Two Services, One Empire</h1>
 <p>Every recorded career transfer of a <b style="color:#9ec9ff">Colonial Office</b> and an
    <b style="color:#ffcf6e">India Office</b> official, 1820s&ndash;1960s &mdash; one officer
    changing post, one arc. 25,000+ moves by 12,000 officials.</p>
 <div id="legend"><span><i style="background:#9ec9ff"></i>Colonial Office</span>
    <span><i style="background:#ffcf6e"></i>India Office</span></div></div>
<div id="year"><div class="y" id="yr">1820</div>
 <div class="c"><b style="color:#9ec9ff" id="cnCO">0</b> Colonial Office &nbsp;&middot;&nbsp;
   <b style="color:#ffcf6e" id="cnIO">0</b> India Office</div></div>
<div id="credit">Colonial Office List &amp; India Office List career data &middot; Wikidata coordinates</div>
<div id="map"></div>
<canvas id="cv"></canvas>
<script>
const ARCS=%(arcs)s, Y0=%(y0)d, Y1=%(y1)d, TOTAL=ARCS.length;
const W=1280,H=720;
const map=L.map('map',{zoomControl:false,attributionControl:false}).setView([14,12],2.3);
L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',{subdomains:'abcd',maxZoom:8}).addTo(map);
const cv=document.getElementById('cv'); cv.width=W; cv.height=H;
const ctx=cv.getContext('2d');
const pc=document.createElement('canvas'); pc.width=W; pc.height=H; const pctx=pc.getContext('2d');

// per-corpus palette: 0 = Colonial Office (blue), 1 = India Office (gold)
const WEB =['rgba(120,180,255,0.065)','rgba(255,200,110,0.065)'];
const TRAIL=[[150,200,255],[255,205,120]];
const HEAD =['rgba(220,238,255,0.95)','rgba(255,244,210,0.95)'];

let PIX=null;
function project(){
 PIX=ARCS.map(a=>{const p1=map.latLngToContainerPoint([a[1],a[2]]),p2=map.latLngToContainerPoint([a[3],a[4]]);
   return [p1.x,p1.y,p2.x,p2.y];});
}
function arcCurve(x1,y1,x2,y2){
 const mx=(x1+x2)/2,my=(y1+y2)/2,dx=x2-x1,dy=y2-y1,len=Math.hypot(dx,dy)||1;
 const lift=Math.min(len*0.22,150);
 return [mx - dy/len*lift, my + dx/len*lift];
}
function pointAt(x1,y1,cx,cy,x2,y2,t){const u=1-t;
 return [u*u*x1+2*u*t*cx+t*t*x2, u*u*y1+2*u*t*cy+t*t*y2];}

const FLIGHT=1.4;
let lastDrawn=0;
let doneCO=0, doneIO=0;

window.renderFrame=function(tYears){
 if(!PIX) project();
 const nowYear = Y0 + tYears;
 // 1) burn newly-completed arcs into the persistent web (coloured by corpus)
 while(lastDrawn<TOTAL && ARCS[lastDrawn][0] + FLIGHT <= nowYear){
  const a=ARCS[lastDrawn], p=PIX[lastDrawn], [cx,cy]=arcCurve(p[0],p[1],p[2],p[3]);
  pctx.strokeStyle=WEB[a[5]]; pctx.lineWidth=0.7;
  pctx.beginPath(); pctx.moveTo(p[0],p[1]); pctx.quadraticCurveTo(cx,cy,p[2],p[3]); pctx.stroke();
  if(a[5]===0) doneCO++; else doneIO++;
  lastDrawn++;
 }
 // 2) compose: persistent web + active flights
 ctx.clearRect(0,0,W,H);
 ctx.drawImage(pc,0,0);
 for(let i=lastDrawn;i<TOTAL;i++){
  const a=ARCS[i], yr=a[0];
  if(yr>nowYear) break;
  const f=(nowYear-yr)/FLIGHT;
  if(f<0||f>1) continue;
  const p=PIX[i], [cx,cy]=arcCurve(p[0],p[1],p[2],p[3]), tr=TRAIL[a[5]];
  ctx.strokeStyle='rgba('+tr[0]+','+tr[1]+','+tr[2]+','+(0.55*(1-f)+0.12)+')'; ctx.lineWidth=1.2;
  ctx.beginPath(); ctx.moveTo(p[0],p[1]);
  const steps=14; for(let s=1;s<=steps*f;s++){const pt=pointAt(p[0],p[1],cx,cy,p[2],p[3],s/steps); ctx.lineTo(pt[0],pt[1]);}
  ctx.stroke();
  const hd=pointAt(p[0],p[1],cx,cy,p[2],p[3],f);
  ctx.beginPath(); ctx.fillStyle=HEAD[a[5]]; ctx.arc(hd[0],hd[1],2.4,0,7); ctx.fill();
 }
 document.getElementById('yr').textContent=Math.floor(nowYear);
 document.getElementById('cnCO').textContent=doneCO.toLocaleString();
 document.getElementById('cnIO').textContent=doneIO.toLocaleString();
};
map.whenReady(()=>{ setTimeout(()=>{project(); window.renderFrame(0); window.__ready=true;}, 600); });
</script></body></html>"""

open("docs/combined_mobility_anim.html", "w").write(HTML % {"arcs": json.dumps(arcs), "y0": y0, "y1": y1})
print("wrote docs/combined_mobility_anim.html")
