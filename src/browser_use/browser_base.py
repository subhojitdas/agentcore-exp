from playwright.sync_api import Playwright, sync_playwright
from browserbase import Browserbase
import os

bb = Browserbase(api_key=os.environ["BROWSERBASE_API_KEY"])


def run(playwright: Playwright) -> None:
    # Create a session on Browserbase
    session = bb.sessions.create(project_id='7f29b497-3707-459b-8534-dee9879106d3')

    # Connect to the remote session
    chromium = playwright.chromium
    browser = chromium.connect_over_cdp(session.connect_url)
    context = browser.contexts[0]
    page = context.pages[0]

    try:
        # Execute Playwright actions on the remote browser tab
        page.goto("https://news.ycombinator.com/")
        page_title = page.title()
        print(f"Page title: {page_title}")
        page.screenshot(path="screenshot.png")
    finally:
        page.close()
        browser.close()

    print(f"Done! View replay at https://browserbase.com/sessions/{session.id}")

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)