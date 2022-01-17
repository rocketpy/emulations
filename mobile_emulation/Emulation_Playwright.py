# Playwright - can be used to simulate browser behavior on a mobile device

# https://playwright.dev/python/docs/emulation

# 
from playwright.sync_api import sync_playwright


def run(playwright):
    pixel_2 = playwright.devices['Pixel 2']
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **pixel_2,
    )

with sync_playwright() as playwright:
    run(playwright)
