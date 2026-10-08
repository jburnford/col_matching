import asyncio, json, sys
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    base = sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:4178/'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage'])
        page = await browser.new_page(viewport={'width':1440,'height':1100})
        errors=[]
        page.on('pageerror', lambda e: errors.append(str(e)))
        for pid in ('kgp_col1878-p447b3','kgp_iol1889_jan-c2242376'):
            await page.goto(base+'?p='+pid, wait_until='domcontentloaded')
            await page.wait_for_function("window.ATLAS?.App.careers && document.querySelectorAll('.ros-entry').length > 0",timeout=45000)
            text = await page.locator('#reg-body').inner_text()
            assert 'Venezuela' in text and 'Cape Colony' in text and 'Belize City' in text,text
            assert 'Belmopan' not in text and 'Union of South Africa' not in text,text
            print(pid, 'passed')
            if pid.startswith('kgp_col'):
                await page.screenshot(path='/tmp/wodehouse-repaired.png',full_page=True)
        await page.evaluate("ATLAS.App.selectPerson('kgp_col1918-p696b8')")
        await page.locator('details summary').click()
        text=await page.locator('#reg-body').inner_text()
        assert 'electoral defeat; not an appointment' in text,text
        assert '1912–16' not in text,text
        await page.screenshot(path='/tmp/brewster-repaired.png',full_page=True)
        # A person without a mapped event remains searchable and readable.
        pid=await page.evaluate("Object.entries(ATLAS.App.careers.persons).find(([id,p])=>!p.st.length && p.un.length)[0]")
        await page.evaluate('(pid)=>ATLAS.App.selectPerson(pid)',pid)
        assert '0 located postings' in await page.locator('#reg-body').inner_text()
        assert await page.locator('details').count()==1
        # Check every guided tour step against new dated plotting nodes.
        await page.evaluate("ATLAS.Tours.start(1)")
        for i in range(10):
            await page.evaluate("if (!ATLAS.Tours.wrap.hidden) ATLAS.Tours.next()")
        await page.evaluate("ATLAS.Tours.dismiss(); ATLAS.App.reset()")
        assert 'Geography corrections and audit' in await page.locator('#reg-body').inner_text()
        await page.set_viewport_size({'width':390,'height':844})
        await page.evaluate("ATLAS.App.selectPerson('kgp_col1878-p447b3')")
        await page.wait_for_timeout(600)
        await page.screenshot(path='/tmp/atlas-mobile.png', full_page=True)
        overflow = await page.evaluate("[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right > innerWidth+2 && getComputedStyle(e).position !== 'absolute').slice(0,8).map(e=>[e.tagName,e.id,e.className,e.getBoundingClientRect().right])")
        print('mobile overflow:', overflow)
        assert await page.evaluate('document.documentElement.scrollWidth <= innerWidth + 2')
        assert not errors,errors
        print('Brewster, unplaced record, tours, summary and mobile passed; no browser errors')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
