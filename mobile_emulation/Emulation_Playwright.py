# Playwright - can be used to simulate browser behavior on a mobile device

# https://playwright.dev/python/docs/emulation


# Sync
from playwright.sync_api import sync_playwright


def run(playwright):
    pixel_2 = playwright.devices['Pixel 2']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **pixel_2,
    )

with sync_playwright() as playwright:
    run(playwright)
    
    
# Async
import asyncio
from playwright.async_api import async_playwright


async def run(playwright):
    pixel_2 = playwright.devices['Pixel 2']
    browser = await playwright.webkit.launch(headless=False)
    context = await browser.new_context(
        **pixel_2,
    )

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())


#  User Agent
# Sync
context = browser.new_context(user_agent='My user agent')

# Async
context = await browser.new_context(user_agent='My user agent')

