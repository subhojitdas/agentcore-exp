from playwright.sync_api import Playwright, sync_playwright
from browserbase import Browserbase
import os

bb = Browserbase(api_key=os.environ["BROWSERBASE_API_KEY"])


def run(playwright: Playwright) -> None:
    session = bb.sessions.create(project_id='7f29b497-3707-459b-8534-dee9879106d3')

    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(session.connect_url)
    context = browser.contexts[0]
    page = context.pages[0]

    try:
        page.goto("https://amazon.in")
        page_title = page.title()
        print(f"Page title: {page_title}")
    finally:
        page.close()
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)