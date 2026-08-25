from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    #pixel_5_args = playwright.devices["Pixel 5"]

    context = browser.new_context(#is_mobile=True,has_touch=True, 
                                  viewport={"width":300, "height":500},
                                  color_scheme="dark",
                                  )

    page= context.new_page()
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="Get started")
    link.click()

    page.set_viewport_size({"width":1000, "height":1000})
