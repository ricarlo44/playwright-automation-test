import pytest  
from playwright.sync_api import Page  

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True, scope="function") #or scope="session" para que ejecute solo por sesion de ingreso una sola vez es mejor por funcion este ejemplo
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python")
    yield page
    page.close()
    print("\n[Fixture]: page closed!")

def test_page_has_docs_link(page: Page):

    link = page.get_by_role("link", name="Docs")

    assert link.is_visible()

def test__get_started_visits_docs(page: Page):

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == DOCS_URL