import asyncio
from playwright.async_api import async_playwright
from ai_parser.prompt_parser import parse_prompt
import time

# Prompt list
prompts = [
    "Type tomsmith into the username field",
    "Type SuperSecretPassword! into the password field",
    "Click the login button"
]

async def run_playwright_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # bisa True jika ingin headless
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://the-internet.herokuapp.com/login")

        for i, prompt in enumerate(prompts, start=1):
            print(f"🔍 Step {i}: {prompt}")
            instruksi = parse_prompt(prompt)

            action = instruksi.get("action")
            selector = instruksi.get("selector")

            if action == "type":
                await page.fill(selector, instruksi.get("value"))
            elif action == "click":
                await page.click(selector)
                await page.wait_for_timeout(2000)

            if "login" in prompt.lower():
                content = await page.content()
                if "You logged into a secure area!" in content:
                    print("✅ Login successful!")
                else:
                    print("❌ Login failed.")

        await browser.close()

# Jalankan
asyncio.run(run_playwright_test())
