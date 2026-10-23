from pathlib import Path
from playwright.sync_api import sync_playwright

html_file = Path(__file__).resolve().with_name('index.html')
url = html_file.as_uri()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 1200})
    page.goto(url)

    page.wait_for_timeout(1500)

    title = page.title()
    heading = page.locator('h1').text_content()
    buttons = page.locator('button').count()
    cards = page.locator('#statTotal').text_content()

    print(f'TITLE={title}')
    print(f'HEADING={heading}')
    print(f'BUTTONS={buttons}')
    print(f'TOTAL_TASKS={cards}')

    errors = page.locator('text=error').count()
    if errors:
        raise SystemExit('UI error detected')

    browser.close()
