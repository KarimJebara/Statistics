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
        
        # Go to games
        await page.click('.nav-btn:has-text("Learning Games")')
        await page.wait_for_timeout(300)
        
        # Scroll to see exam simulator
        await page.evaluate("window.scrollTo(0, 900)")
        await page.wait_for_timeout(300)
        await page.screenshot(path="ss_exam_card.png")
        
        # Click exam simulator
        await page.locator('.card:has-text("Exam Simulator")').click()
        await page.wait_for_timeout(400)
        await page.screenshot(path="ss_exam_q1.png")
        
        # Answer 3 questions
        for i in range(3):
            opts = page.locator('.game-opt')
            if await opts.count() > 0:
                await opts.first.click()
                await page.wait_for_timeout(500)
                if i == 0:
                    await page.screenshot(path="ss_exam_ans1.png")
                # Click next
                next_btn = page.locator('.btn-primary:has-text("Next")')
                if await next_btn.count() > 0:
                    await next_btn.click()
                    await page.wait_for_timeout(300)
        
        await page.screenshot(path="ss_exam_q3.png")
        
        print("Console errors:", errors if errors else "None")
        await browser.close()

asyncio.run(main())
