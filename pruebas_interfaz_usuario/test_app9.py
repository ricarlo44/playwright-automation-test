from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/verifytext")

    text = page.locator("div.bg-primary").get_by_text("Welcome")

    expect(text).to_have_text("Welcome UserName!")