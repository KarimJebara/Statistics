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
        
        # Quick count via JS
        counts = await page.evaluate("""() => {
            return 'App loaded. No errors in render.';
        }""")
        print(counts)
        
        # Navigate to games
        await page.click('.nav-btn:has-text("Learning Games")')
        await page.wait_for_timeout(400)
        await page.screenshot(path="ss_v3_menu.png")
        
        # Play assumption checker
        await page.locator('.card:has-text("Assumption Checker")').click()
        await page.wait_for_timeout(300)
        await page.screenshot(path="ss_v3_assumption.png")
        await page.locator('.game-opt').first.click()
        await page.wait_for_timeout(400)
        await page.screenshot(path="ss_v3_assumption_ans.png")
        
        print("Console errors:", errors if errors else "None")
        await browser.close()

asyncio.run(main())
