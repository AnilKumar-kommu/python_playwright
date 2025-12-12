import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_page():
    """Launch browser and return a fresh page for each test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
