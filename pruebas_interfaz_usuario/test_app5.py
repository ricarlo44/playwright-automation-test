from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/click")

    btn = page.get_by_role("button", name="Button That Ignores DOM Click Event")
    btn.click()

    expect(btn).to_have_class("btn btn-success")
    