import json
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("Vibes.ai saytiga ulanmoqda...")
        await page.goto("https://vibes.ai", wait_until="networkidle")
        
        page_title = await page.title()
        print(f"Sayt sarlavhasi: {page_title}")

        data = [
            {
                "title": page_title,
                "media_url": "https://vibes.ai"
            }
        ]

        with open("vibes_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("vibes_data.json fayli muvaffaqiyatli yaratildi!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
