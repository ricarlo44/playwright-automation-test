from playwright.sync_api import Page, expect, Request, Response


def on_request(request: Request):
    print("Sent Request:", request)

def on_response(response: Response):
    print("Got Response:", response)

def test_docs_link(page: Page):
    page.on("request", on_request)
    page.on("response", on_response) 
    page.goto("https://playwright.dev/python")

    docs_link = page.get_by_role("link", name="Docs")
    docs_link.click()

    expect(page).to_have_url("https://playwright.dev/python/docs/intro")


#def test_docs_search(page: Page):
#   query = "assertions"
#   homepage = PlaywrightPage(page)
#   homepage.search(query)

#    expect(homepage.search_results()).to_contain_text("List of assertions")