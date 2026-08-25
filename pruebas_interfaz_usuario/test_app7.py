from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")

    btn = page.get_by_role("button", name="Hiding Button")
    btn.scroll_into_view_if_needed()
    btn.click()
    page.screenshot(path="test.jpg")
    #expect(btn).to_have_text(query)