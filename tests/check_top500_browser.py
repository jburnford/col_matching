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
  await page.screenshot(path='/tmp/cameron-africa.png',full_page=False)
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
  print('Ford, homonyms, composite withdrawal, tour, mobile resize, 500 review rows, search and deep links passed; no browser errors.')
  await browser.close()

if __name__=='__main__':asyncio.run(main())
