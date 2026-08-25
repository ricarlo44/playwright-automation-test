from playwright.sync_api import Page, expect 

#DOCS_URL = "https://playwright.dev/python/docs/intro"


#@pytest.fixture(autouse=False) 
    
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    dropdown_menu = page.locator("ul.dropdown__menu")
    #link.click()

    expect(dropdown_menu).to_contain_text("Python")
    expect(dropdown_menu).to_contain_text("Java")
    expect(dropdown_menu).to_contain_text("Node.js")