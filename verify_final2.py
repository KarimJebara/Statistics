import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 900})
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        await page.goto("file:///sessions/dreamy-awesome-franklin/mnt/Documents/Statistics/study-app.html")
        await page.wait_for_timeout(3000)
        
        # Rapid test: each game
        for g in ['Test Selector','Error Detective','Speed Round','Assumption Checker','Output Reader','Calculation Blitz','Exam Simulator']:
            await page.click('.nav-btn:has-text("Learning Games")')
            await page.wait_for_timeout(200)
            try:
                await page.locator(f'.card:has-text("{g}")').click(timeout=3000)
                await page.wait_for_timeout(200)
                opts = page.locator('.game-opt')
                if await opts.count() > 0:
                    await opts.first.click()
                    await page.wait_for_timeout(500)
                print(f"  {g}: OK")
            except Exception as e:
                print(f"  {g}: FAILED - {e}")
        
        # Final screenshot of game menu
        await page.click('.nav-btn:has-text("Learning Games")')
        await page.wait_for_timeout(300)
        await page.screenshot(path="ss_final_v4.png")
        
        print(f"\nConsole errors: {errors if errors else 'None'}")
        await browser.close()

asyncio.run(main())
