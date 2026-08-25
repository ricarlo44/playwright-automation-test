from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser= playwright.chromium.launch(
        headless=False, slow_mo=500
    )
    page= browser.new_page()
    page.goto("https://bootswatch.com/default")

    link = page.locator("a.dropdown-item").first
    link.click()

    browser.close()

