from playwright.sync_api import Page, expect

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/classattr")

    #existen 3 botones con el mismo nombre

    primary_btn = page.locator("button.btn-primary")

    #primary_btn = page.locator("//button[contains(@class, 'btn-primary')]") #asi se busca el boton con Xpath

    expect(primary_btn).to_be_visible()

    primary_btn.click()