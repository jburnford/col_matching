"""Browser verification of corrected records, audit coverage, tours and resize."""
import asyncio, sys
from playwright.async_api import async_playwright

async def main():
 base=(sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:4178/').rstrip('/')+'/'
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  page=await browser.new_page(viewport={'width':1440,'height':1000});errors=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto(base+'?p=kgp_col1896-p581b17',wait_until='domcontentloaded')
  await page.wait_for_function("window.ATLAS?.App.careers && document.querySelectorAll('.ros-entry').length>0",timeout=60000)
  data=await page.evaluate("({p:ATLAS.App.careers.persons['kgp_col1896-p581b17'],places:ATLAS.App.places})")
  assert not any(s[1]==1865 and data['places'][s[0]]['entity_qid']=='Q17' for s in data['p']['st'])
  assert any(u[0]==1865 and 'not taken up' in u[4] for u in data['p']['un'])
  assert 'Read review 1' in await page.locator('#reg-body').inner_text()
  assert await page.evaluate("ATLAS.Arcs.indicesForPerson('kgp_col1896-p581b17').length") == 22
  await page.screenshot(path='/tmp/ford-restored.png',full_page=False)
  await page.evaluate("ATLAS.App.selectPerson('kgp_col1918-p704b7')")
  await page.wait_for_timeout(1000)
  assert await page.evaluate("""() => {
    const A=ATLAS.App, keys=A.careers.persons['kgp_col1918-p704b7'].st.map(s=>s[0]);
    const edge=document.getElementById('register').getBoundingClientRect().left;
    return keys.every(k=>{const p=A.places[k],xy=A.map.latLngToContainerPoint([p.lat,p.lon]);
      return xy.x>=0 && xy.x<edge && xy.y>=0 && xy.y<innerHeight && ATLAS.Places.markers[k];});
  }""")
  assert await page.evaluate("ATLAS.App.arcs.some(a=>a[3]==='kgp_col1918-p704b7' && a[0]===1884 && a[2]==='Q30059027')")
  assert await page.evaluate("ATLAS.Places.markers['Q3557236'].options.fillOpacity") == .6
  assert await page.evaluate("""() => {
    const A=ATLAS.Arcs, incoming=A.arcs.map((a,i)=>({a,i})).filter(({a})=>
      a[3]==='kgp_col1918-p704b7' && a[2]==='Q3557236');
    return incoming.length===1 && incoming.every(({a,i})=>a[0]===1914 && a[1]==='Q2660774@Q41547' && !a[5] && A.hl.includes(i));
  }""")
  # Verify actual canvas rendering, not just a marker or an array entry.
  assert await page.evaluate("""() => {
    const A=ATLAS.Arcs, ctx=A.ctx, stroke=ctx.stroke, curve=ctx.quadraticCurveTo;
    const p=ATLAS.App.places['Q3557236'], target=A.map.latLngToContainerPoint([p.lat,p.lon]);
    let end=null, drawn=0;
    ctx.quadraticCurveTo=function(cx,cy,x,y){end=[x,y];return curve.call(this,cx,cy,x,y);};
    ctx.stroke=function(){if(end && Math.abs(end[0]-target.x)<1 && Math.abs(end[1]-target.y)<1 && !this.getLineDash().length)drawn++;return stroke.call(this);};
    try {A.draw();} finally {ctx.stroke=stroke;ctx.quadraticCurveTo=curve;}
    return drawn===1;
  }""")
  assert 'Dashed:' in await page.locator('.route-legend').inner_text()
  assert await page.evaluate("!ATLAS.App.careers.persons['kgp_col1918-p704b7'].st.some(s=>s[0]==='Q1930@place')")
  await page.locator('details summary').click()
  assert 'Conference participation' in await page.locator('#reg-body').inner_text()
  await page.screenshot(path='/tmp/cameron-africa.png',full_page=False)
  await page.evaluate("ATLAS.App.selectPerson('kgp_col1879-p423b19')")
  await page.wait_for_timeout(700)
  assert await page.evaluate("""() => {
    const A=ATLAS.App, st=A.careers.persons['kgp_col1879-p423b19'].st;
    return st.filter(s=>s[1]===1871 || s[1]===1872).length===2 &&
      st.every(s=>{const p=A.places[s[0]]; return p.lat>43 && p.lat<48 && p.lon>-80 && p.lon<-70;}) &&
      st.filter(s=>s[1]===1871 || s[1]===1872).every(s=>A.places[s[0]].capital_qid==='Q1930' && A.places[s[0]].entity_qid==='Q16') &&
      Object.values(A.places).filter(p=>p.entity_qid==='Q1121436').every(p=>p.lat>43 && p.lat<48 && p.lon>-80 && p.lon<-70);
  }""")
  await page.screenshot(path='/tmp/province-canada-corrected.png',full_page=False)
  for pid in ['kgp_col1897-p478b29_s1','kgp_col1897-p481b20','kgp_col1921-p816b11','kgp_col1898-p520b7','kgp_col1897-p546b17','kgp_col1918-p827b6']:
   await page.evaluate('(pid)=>ATLAS.App.selectPerson(pid)',pid)
   await page.wait_for_timeout(300)
   assert await page.evaluate("""pid => {
     const A=ATLAS.App, st=A.careers.persons[pid].st;
     return st.some(s=>A.places[s[0]].entity_qid==='Q1533623') &&
       st.every(s=>!['Q671431','Q1989'].includes(A.places[s[0]].entity_qid)) &&
       !!ATLAS.Places.markers['Q1533623@place'];
   }""",pid)
   assert 'Prince Albert (Cape)' in await page.locator('#reg-body').inner_text()
  await page.screenshot(path='/tmp/prince-albert-cape.png',full_page=False)
  for pid,needle in [('kgp_col1906-p730b6','Prince Albert (Cape)'),('kgp_col1932-p883b6','Belfast (Transvaal)'),('kgp_col1886-p405b4','Alexandria (Cape)')]:
   await page.evaluate('(pid)=>ATLAS.App.selectPerson(pid)',pid)
   assert needle in await page.locator('#reg-body').inner_text()
  await page.evaluate("ATLAS.App.selectPerson('kgp_col1897-p494b18')")
  assert '0 located postings' in await page.locator('#reg-body').inner_text()
  assert 'combines several people' in await page.locator('#reg-body').inner_text()
  await page.locator('details summary').click()
  assert 'Attribution must be reconstructed' in await page.locator('#reg-body').inner_text()
  await page.screenshot(path='/tmp/top500-composite.png',full_page=True)
  await page.evaluate("ATLAS.Tours.start(1)")
  for i in range(10):await page.evaluate("if (!ATLAS.Tours.wrap.hidden) ATLAS.Tours.next()")
  await page.evaluate("ATLAS.Tours.dismiss();ATLAS.App.selectPerson('kgp_col1896-p581b17')")
  await page.set_viewport_size({'width':390,'height':844});await page.wait_for_timeout(700)
  await page.screenshot(path='/tmp/top500-atlas-mobile.png',full_page=False)
  assert await page.evaluate('document.documentElement.scrollWidth<=innerWidth+2')
  await page.goto(base+'review/top-500/#rank-500',wait_until='domcontentloaded')
  await page.wait_for_selector('.career',timeout=30000)
  assert await page.locator('.career').count()==500
  assert await page.locator('#rank-500').get_attribute('open') is not None
  await page.locator('#filter').fill('kgp_col1896-p581b17')
  assert '1 careers' in await page.locator('#shown').inner_text()
  await page.locator('#filter').fill('')
  assert '500 careers' in await page.locator('#shown').inner_text()
  assert await page.evaluate('document.documentElement.scrollWidth<=innerWidth+2')
  await page.screenshot(path='/tmp/top500-review-mobile.png',full_page=False)
  await page.set_viewport_size({'width':1440,'height':1000})
  await page.goto(base+'review/top-500/#rank-1',wait_until='domcontentloaded')
  await page.wait_for_selector('.career',timeout=30000)
  await page.wait_for_function("document.querySelector('#rank-1').open")
  await page.screenshot(path='/tmp/top500-review-desktop.png',full_page=False)
  assert not errors,errors
  print('Six Prince Albert Cape careers and Province of Canada checks passed. Cameron: Ottawa retained in text, temporary Windward posting mapped, solid Gambia arc rendered. Ford, homonyms, composite withdrawal, tour, mobile resize, 500 review rows, search and deep links passed; no browser errors.')
  await browser.close()

if __name__=='__main__':asyncio.run(main())
