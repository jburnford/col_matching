#!/usr/bin/env python3
"""India Office List variant of build_mobility_video.py.

A time-lapse of EVERY career transfer in the IOL knowledge graph -- officials of
the Indian Empire moving between presidencies (Bengal/Madras/Bombay), provinces
(Punjab, United Provinces, Sind, Assam, the Frontier...), princely states, and the
imperial periphery (Burma, Aden, Mesopotamia). Canvas animation over a Leaflet/CARTO
basemap centred on the subcontinent: a clock runs 1821->1947, each transfer flies as
a glowing arc and settles into a persistent faint web of imperial circulation.
Frames captured by render_iol_mobility.py, encoded to MP4."""
import json

data = json.load(open("/tmp/iol_transfers.json"))
coords = json.load(open("/tmp/iol_transfer_coords.json"))
T = [t for t in data["transfers"] if t["from"] in coords and t["to"] in coords and t["from"] != t["to"]]
T.sort(key=lambda t: t["yr"])
# compact transfer list: [year, fromLat,fromLon, toLat,toLon]
arcs = [[t["yr"], coords[t["from"]][0], coords[t["from"]][1], coords[t["to"]][0], coords[t["to"]][1]] for t in T]
y0, y1 = arcs[0][0], arcs[-1][0]
npeople = len({t["pid"] for t in T})
print(f"{len(arcs):,} mapped transfers, {npeople:,} officials, {y0}-{y1}")

HTML = """<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
 html,body{margin:0;height:100%%;background:#0a0f07;overflow:hidden;font-family:Georgia,serif}
 #map{height:100%%;background:#0a0f07}
 #cv{position:absolute;top:0;left:0;z-index:500;pointer-events:none}
 #hud{position:absolute;z-index:1000;top:24px;left:34px;color:#f5ecd6;text-shadow:0 2px 10px #000}
 #hud h1{margin:0;font-size:30px;color:#ffcf6e;letter-spacing:.3px}
 #hud p{margin:6px 0 0;font-size:16px;color:#e6ddc9;font-family:system-ui,sans-serif;max-width:560px;line-height:1.35}
 #year{position:absolute;z-index:1000;bottom:26px;left:34px;color:#fff;font-family:system-ui,sans-serif;text-shadow:0 2px 8px #000}
 #year .y{font-size:62px;font-weight:800;color:#ffcf6e;line-height:1}
 #year .c{font-size:17px;color:#e0d7c2;margin-top:2px}
 #credit{position:absolute;z-index:1000;bottom:14px;right:14px;color:#8a8266;font-size:12px;font-family:system-ui,sans-serif}
 .leaflet-control-attribution{display:none}
</style></head><body>
<div id="hud"><h1>Moving the Raj</h1>
 <p>Every recorded career transfer of an India Office official, 1820s&ndash;1940s &mdash;
    one officer moving between presidencies, provinces, and princely states, one arc.
    9,000+ moves by 4,000 officials.</p></div>
<div id="year"><div class="y" id="yr">1821</div><div class="c"><span id="cn">0</span> transfers</div></div>
<div id="credit">India Office List career data &middot; Wikidata coordinates</div>
<div id="map"></div>
<canvas id="cv"></canvas>
<script>
const ARCS=%(arcs)s, Y0=%(y0)d, Y1=%(y1)d, TOTAL=ARCS.length;
const W=1280,H=720;
const map=L.map('map',{zoomControl:false,attributionControl:false}).setView([21.5,73.5],4.3);
L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',{subdomains:'abcd',maxZoom:8}).addTo(map);
const cv=document.getElementById('cv'); cv.width=W; cv.height=H;
const ctx=cv.getContext('2d');
// persistent (accumulating) web canvas, never cleared
const pc=document.createElement('canvas'); pc.width=W; pc.height=H; const pctx=pc.getContext('2d');

let PIX=null;
function project(){ // place lat/lon -> container pixels (view is fixed)
 PIX=ARCS.map(a=>{const p1=map.latLngToContainerPoint([a[1],a[2]]),p2=map.latLngToContainerPoint([a[3],a[4]]);
   return [p1.x,p1.y,p2.x,p2.y];});
}
function arcCurve(x1,y1,x2,y2){ // quadratic control point lifted perpendicular
 const mx=(x1+x2)/2,my=(y1+y2)/2,dx=x2-x1,dy=y2-y1,len=Math.hypot(dx,dy)||1;
 const lift=Math.min(len*0.22,150);
 return [mx - dy/len*lift, my + dx/len*lift];
}
function pointAt(x1,y1,cx,cy,x2,y2,t){const u=1-t;
 return [u*u*x1+2*u*t*cx+t*t*x2, u*u*y1+2*u*t*cy+t*t*y2];}

const FLIGHT=1.4;                 // years an arc spends "flying"
let lastDrawn=0;                  // index into ARCS already burned into persistent web
let curYear=Y0;

// renderFrame(tYears): tYears = years elapsed since Y0 (continuous)
window.renderFrame=function(tYears){
 if(!PIX) project();
 const nowYear = Y0 + tYears;
 curYear = nowYear;
 // 1) burn newly-completed arcs into the persistent faint web
 while(lastDrawn<TOTAL && ARCS[lastDrawn][0] + FLIGHT <= nowYear){
  const p=PIX[lastDrawn], [cx,cy]=arcCurve(p[0],p[1],p[2],p[3]);
  pctx.strokeStyle='rgba(255,205,130,0.07)'; pctx.lineWidth=0.7;
  pctx.beginPath(); pctx.moveTo(p[0],p[1]); pctx.quadraticCurveTo(cx,cy,p[2],p[3]); pctx.stroke();
  lastDrawn++;
 }
 // 2) compose: persistent web + active flights this frame
 ctx.clearRect(0,0,W,H);
 ctx.drawImage(pc,0,0);
 let active=0, done=lastDrawn;
 for(let i=lastDrawn;i<TOTAL;i++){
  const yr=ARCS[i][0];
  if(yr>nowYear) break;                 // not started yet (ARCS sorted by year)
  const f=(nowYear-yr)/FLIGHT;          // 0..1 flight progress
  if(f<0||f>1) continue;
  active++;
  const p=PIX[i], [cx,cy]=arcCurve(p[0],p[1],p[2],p[3]);
  // trailing arc up to head
  ctx.strokeStyle='rgba(255,225,150,'+(0.55*(1-f)+0.12)+')'; ctx.lineWidth=1.2;
  ctx.beginPath(); ctx.moveTo(p[0],p[1]);
  const steps=14; for(let s=1;s<=steps*f;s++){const pt=pointAt(p[0],p[1],cx,cy,p[2],p[3],s/steps); ctx.lineTo(pt[0],pt[1]);}
  ctx.stroke();
  // glowing head
  const hd=pointAt(p[0],p[1],cx,cy,p[2],p[3],f);
  ctx.beginPath(); ctx.fillStyle='rgba(255,248,220,0.95)'; ctx.arc(hd[0],hd[1],2.4,0,7); ctx.fill();
 }
 document.getElementById('yr').textContent=Math.floor(nowYear);
 document.getElementById('cn').textContent=(done).toLocaleString();
};
map.whenReady(()=>{ setTimeout(()=>{project(); window.renderFrame(0); window.__ready=true;}, 600); });
</script></body></html>"""

open("docs/iol_mobility_anim.html", "w").write(HTML % {"arcs": json.dumps(arcs), "y0": y0, "y1": y1})
print("wrote docs/iol_mobility_anim.html")
