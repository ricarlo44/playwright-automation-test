from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/nbsp")


    page.locator("//button[text()='My\u00a0Button']").click(timeout=2000)

