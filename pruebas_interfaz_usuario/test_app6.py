from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/textinput")

    query = "great stuff"
    input = page.get_by_label("Set New Button Name")
    input.fill(query)
    btn = page.locator("button.btn-primary")
    btn.click()
    expect(btn).to_have_text(query)
    
    
    