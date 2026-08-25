from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com")

    load_delay_link = page.get_by_role("link", name="Load Delay")
    load_delay_link.click() #inicia la navegacion a la segunda pantalla

    btn_delay = page.get_by_role("button", name="Button Appearing After Delay")
    btn_delay.wait_for(timeout=10000)

    expect(btn_delay).to_be_visible()

    btn_delay.click()

