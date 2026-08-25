from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/hiddenlayers")

    #existe un boton que cambia de color de verde a azul con un click

    green_btn = page.locator("button#greenButton")

    #expect(green_btn).to_be_visible()

    green_btn.click()

    with pytest.raises(TimeoutError):
        green_btn.click(timeout=2000)