from playwright.sync_api import Page, expect, Route


def on_route(route: Route):
    
    response = route.fetch()
    body = response.text().replace(" enables reliable web automation for testing, scripting, and AI agents.",
                                    " is an awesome framework for web automation!")
    
    #route.fulfill(status=200, body="<html><body><h1>Custom Response!</h1></body></html>")
    route.fulfill(response=response, body=body)


def test_docs_link(page: Page):
    page.route("https://playwright.dev/python", on_route)
    page.goto("https://playwright.dev/python")
    page.pause()