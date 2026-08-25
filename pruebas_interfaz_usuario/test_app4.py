from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/ajax")

    btn = page.get_by_role("button", name="Button Triggering AJAX Request")
    btn.click()

    paragraph = page.locator("p.bg-success")
    paragraph.wait_for()
    expect(paragraph).to_be_visible()
    
