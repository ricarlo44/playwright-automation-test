import pytest  
from playwright.sync_api import Page, expect 

DOCS_URL = "https://playwright.dev/python/docs/intro"


#@pytest.fixture(autouse=False) 

#def trace_test(context: BrowserContext):
    #start the setup del tracing para que tenga screenshot frame by frame 
    #context.tracing.start(name="playwright", screenshots=True, snapshots=True, sources=True)
    #yield
    #context.tracing.stop(path="trace.zip")
    
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    link = page.get_by_role("link", name="Get python")
    #link.click()

    #assert page.url == DOCS_URL
    expect(link).to_be_hidden()