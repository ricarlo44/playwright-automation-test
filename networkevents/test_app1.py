from playwright.sync_api import Page, expect, Route


def on_route(route: Route):
    if route.request.resource_type == "image":
    #route.request.post_data = "data"
    #route.continue_()
    #print("Request aborted:", route.request)
        route.abort()
    else:
        route.continue_()

def test_docs_link(page: Page):
    page.route("**", on_route)
    page.goto("https://playwright.dev/python")

    page.screenshot(path="playwright.jpg", full_page=True)