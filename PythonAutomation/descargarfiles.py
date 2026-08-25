from playwright.sync_api import sync_playwright

def on_download(download):
    print("Download received!")
    download.save_as("night.jpg")

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto("https://unsplash.com/photos/NDRwHCC7JuI")

    page.once("download",on_download)

    btn = page.get_by_role("link", name="Descargar gratis")

    with page.expect_download() as download_info:
        btn.click()

    #download = download_info.value
    #download.save_as("moon.jpg")

    browser.close()