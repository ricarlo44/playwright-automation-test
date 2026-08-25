from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/mouseover")

    link = page.get_by_title("Click me")
    link.hover()

    active_link = page.get_by_title("Active link")
    #active_link.dblclick() #para usar mas de 2 clicks se puede usar el argumento .click(click_count=10)
    active_link.click(click_count=2)


    click_count = page.locator("span#clickCount")

    expect(click_count).to_have_text("2")